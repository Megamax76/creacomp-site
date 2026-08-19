#!/usr/bin/env python3
"""Extrait le référentiel CreaComp du document source Word vers framework.fr.json.

Le document source structure chaque compétence en un tableau de sept lignes :
intitulé, définition, composantes, en-tête, puis les quatre niveaux. Les rubriques
sont introduites par un titre de niveau 1 suivi de l'objet, du chapeau et de la
clause de frontière. Ce script suit cette structure et échoue bruyamment si elle
n'est pas respectée, plutôt que de produire des données silencieusement fausses.
"""

import json
import re
import sys
import unicodedata
import zipfile
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

SOURCE = "/Users/maximehebert/Downloads/DCLIC référentiel final/DCLIC_V7_Referentiel.docx"
TARGET = "/Users/maximehebert/CreaComp Site/src/data/fr/framework.json"

RUBRIC_COLORS = {
    1: "petrole",
    2: "indigo",
    3: "carmin",
    4: "terre",
    5: "foret",
    6: "sarcelle",
    7: "bronze",
}

LEVEL_IDS = ["N1", "N2", "N3", "N4"]


def para_text(p):
    return "".join(t.text or "" for t in p.iter(W + "t")).strip()


def para_style(p):
    pPr = p.find(W + "pPr")
    if pPr is None:
        return ""
    s = pPr.find(W + "pStyle")
    return s.get(W + "val") if s is not None else ""


def cell_paragraphs(tc):
    return [t for t in (para_text(p) for p in tc.findall(W + "p")) if t]


def table_rows(tbl):
    return [
        [cell_paragraphs(tc) for tc in tr.findall(W + "tc")]
        for tr in tbl.findall(W + "tr")
    ]


def slugify(text):
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower().replace("'", " ").replace("’", " ")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-{2,}", "-", text).strip("-")


def parse_entry_table(rows, where):
    """Lit un tableau de compétence ou de fil transversal."""
    if len(rows) != 8:
        raise SystemExit(f"{where} : {len(rows)} lignes au lieu de 8")

    title_cell = rows[0][0]
    code, _, title = title_cell[0].partition("  ")
    code, title = code.strip(), title.strip()
    if not code or not title:
        raise SystemExit(f"{where} : intitulé illisible « {title_cell[0]} »")

    definition_cell = rows[1][0]
    if definition_cell[0] != "Définition":
        raise SystemExit(f"{where} : ligne 2 attendue « Définition »")
    definition = " ".join(definition_cell[1:])

    components_cell = rows[2][0]
    if components_cell[0] != "Composantes":
        raise SystemExit(f"{where} : ligne 3 attendue « Composantes »")
    components = components_cell[1:]

    header = rows[3]
    if header[0][0] != "Niveau":
        raise SystemExit(f"{where} : ligne 4 attendue « Niveau »")

    levels = {}
    for level_id, row in zip(LEVEL_IDS, rows[4:]):
        if len(row) != 3:
            raise SystemExit(f"{where} / {level_id} : {len(row)} cellules au lieu de 3")
        if not row[0][0].startswith(level_id):
            raise SystemExit(f"{where} : niveau {level_id} attendu, trouvé « {row[0][0]} »")
        levels[level_id] = {
            "descriptor": " ".join(row[1]),
            "evidence": " ".join(row[2]),
        }

    return {
        "code": code,
        "slug": f"{code.replace('.', '-').lower()}-{slugify(title)}",
        "title": title,
        "definition": definition,
        "components": components,
        "levels": levels,
    }


def main():
    body = ET.fromstring(zipfile.ZipFile(SOURCE).read("word/document.xml")).find(W + "body")
    children = list(body)

    rubrics, competences, threads = [], [], []
    current_rubric = None
    pending_paragraphs = []
    in_threads = False

    for node in children:
        if node.tag == W + "p":
            style, text = para_style(node), para_text(node)
            if not text:
                continue
            match = re.match(r"^Rubrique (\d) — (.+)$", text)
            if style == "Heading1" and match:
                number, name = int(match.group(1)), match.group(2)
                current_rubric = {
                    "id": number,
                    "slug": slugify(name),
                    "title": name,
                    "color": RUBRIC_COLORS[number],
                }
                rubrics.append(current_rubric)
                pending_paragraphs = []
                continue
            if style == "Heading1" and text.startswith("Les trois fils"):
                in_threads = True
                current_rubric = None
                continue
            if style.startswith("Heading"):
                pending_paragraphs = []
                continue
            if current_rubric is not None:
                pending_paragraphs.append(text)
                if len(pending_paragraphs) == 3:
                    current_rubric["object"] = pending_paragraphs[0]
                    current_rubric["intro"] = pending_paragraphs[1]
                    current_rubric["boundary"] = pending_paragraphs[2].removeprefix(
                        "Frontière : "
                    ).removeprefix("Frontière et clause de longévité : ")
            continue

        if node.tag == W + "tbl":
            rows = table_rows(node)
            if not rows or not rows[0] or not rows[0][0]:
                continue
            first = rows[0][0][0]
            if in_threads and re.match(r"^T\d\s", first):
                entry = parse_entry_table(rows, first)
                entry["code"] = entry["code"].split()[0]
                name, _, subtitle = entry["title"].partition(" — ")
                entry["title"] = name.strip().capitalize()
                entry["subtitle"] = subtitle.strip()
                entry["slug"] = f"{entry['code'].lower()}-{slugify(name)}"
                threads.append(entry)
            elif re.match(r"^\d\.\d\s", first):
                if current_rubric is None:
                    raise SystemExit(f"Compétence « {first} » hors rubrique")
                entry = parse_entry_table(rows, first)
                entry["rubricId"] = current_rubric["id"]
                competences.append(entry)

    if len(rubrics) != 7:
        raise SystemExit(f"{len(rubrics)} rubriques extraites au lieu de 7")
    if len(competences) != 28:
        raise SystemExit(f"{len(competences)} compétences extraites au lieu de 28")
    if len(threads) != 3:
        raise SystemExit(f"{len(threads)} fils extraits au lieu de 3")
    for rubric in rubrics:
        for key in ("object", "intro", "boundary"):
            if key not in rubric:
                raise SystemExit(f"Rubrique {rubric['id']} : « {key} » manquant")

    payload = {"rubrics": rubrics, "competences": competences, "threads": threads}
    with open(TARGET, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    descriptors = 4 * (len(competences) + len(threads))
    print(f"{len(rubrics)} rubriques · {len(competences)} compétences · "
          f"{len(threads)} fils · {descriptors} descripteurs → {TARGET}")


if __name__ == "__main__":
    sys.exit(main())
