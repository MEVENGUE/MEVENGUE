#!/usr/bin/env python3
"""Validation du hub profil MEVENGUE — README + wiki.json."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
WIKI = ROOT / ".devin" / "wiki.json"

REQUIRED_README_MARKERS = [
    "MEVENGUE FRANCK",
    "mevenguefranck-siteweb.vercel.app",
    "SUPFile",
    "MentorGPT",
    "3D Canvas",
    "github-readme-stats",
]

REQUIRED_WIKI_KEYS = ["version", "owner", "projects_index", "pages"]
MIN_PAGES = 25
MIN_PROJECTS = 8


def validate_readme() -> list[str]:
    errors: list[str] = []
    if not README.exists():
        return ["README.md introuvable"]
    text = README.read_text(encoding="utf-8")
    for marker in REQUIRED_README_MARKERS:
        if marker not in text:
            errors.append(f"README: marqueur manquant « {marker} »")
    if len(text) < 3000:
        errors.append(f"README: trop court ({len(text)} caractères, min 3000)")
    return errors


def validate_wiki() -> list[str]:
    errors: list[str] = []
    if not WIKI.exists():
        return [".devin/wiki.json introuvable"]
    try:
        wiki = json.loads(WIKI.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"wiki.json: JSON invalide — {e}"]

    for key in REQUIRED_WIKI_KEYS:
        if key not in wiki:
            errors.append(f"wiki.json: clé manquante « {key} »")

    pages = wiki.get("pages", [])
    if len(pages) < MIN_PAGES:
        errors.append(f"wiki.json: {len(pages)} pages (min {MIN_PAGES})")

    projects = wiki.get("projects_index", [])
    if len(projects) < MIN_PROJECTS:
        errors.append(f"wiki.json: {len(projects)} projets (min {MIN_PROJECTS})")

    for page in pages:
        if not page.get("content"):
            errors.append(f"wiki.json: page « {page.get('title')} » sans contenu")

    for project in projects:
        if not project.get("repo"):
            errors.append(f"wiki.json: projet « {project.get('id')} » sans repo")

    # URLs avec point final parasite (ex. vercel.app. en fin de lien)
    raw = WIKI.read_text(encoding="utf-8")
    bad_urls = re.findall(r'https://[^\s"\'|]+?\.(?=["\'\s,|\n])', raw)
    if bad_urls:
        errors.append(f"wiki.json: URLs avec point final parasite: {bad_urls[:3]}")

    return errors


def main() -> int:
    errors = validate_readme() + validate_wiki()
    print("=== Validation hub profil MEVENGUE ===\n")
    if errors:
        for e in errors:
            print(f"✗ {e}")
        print(f"\n{len(errors)} erreur(s)")
        return 1
    wiki = json.loads(WIKI.read_text(encoding="utf-8"))
    print(f"✓ README.md ({README.stat().st_size} octets)")
    print(f"✓ wiki.json v{wiki.get('version')} — {len(wiki['pages'])} pages, {len(wiki['projects_index'])} projets")
    print("\n✅ Hub profil validé avec succès.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
