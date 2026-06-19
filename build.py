#!/usr/bin/env python3
"""
Génère en.html (version anglaise, servie sur /en) à partir de index.html.

index.html est la SOURCE UNIQUE : il contient déjà tout le contenu FR + EN
(blocs .fr / .en) et l'attribut <html lang="fr">. Ce script produit la version
anglaise en changeant uniquement la langue par défaut et le <head> SEO
(title, description, OG/Twitter, og:url, og:locale, canonical).

À relancer après chaque modif du contenu :  python3 build.py
"""
import pathlib
import re

SRC = pathlib.Path(__file__).parent / "index.html"
OUT = pathlib.Path(__file__).parent / "en.html"

# Équivalents anglais du <head> (zéro tiret cadratin).
EN = {
    "title": "MyWedGame: a custom video game for your wedding",
    "description": "Give your guests a unique video game, fully personalized to your love story. From €499.",
    "og:title": "MyWedGame: a custom video game for your wedding",
    "og:description": "A unique, interactive video game created from your love story. Playable on any device.",
    "twitter:title": "MyWedGame: a custom video game for your wedding",
    "twitter:description": "A unique, interactive video game created from your love story. Playable on any device.",
    "og:url": "https://mywedgame.com/en",
    "og:locale": "en_US",
    "og:locale:alternate": "fr_FR",
    "canonical": "https://mywedgame.com/en",
}


def set_meta(html: str, attr: str, key: str, value: str) -> str:
    pat = re.compile(r'(<meta ' + attr + r'="' + re.escape(key) + r'" content=")[^"]*(">)')
    new, n = pat.subn(lambda m: m.group(1) + value + m.group(2), html, count=1)
    if n == 0:
        raise SystemExit(f"build.py: balise introuvable -> {attr}={key}")
    return new


def main() -> None:
    html = SRC.read_text(encoding="utf-8")

    # Langue par défaut de la page.
    html, n = re.subn(r'<html lang="fr">', '<html lang="en">', html, count=1)
    if n == 0:
        raise SystemExit("build.py: <html lang=\"fr\"> introuvable")

    # Titre.
    html, n = re.subn(r"<title>.*?</title>", lambda m: f"<title>{EN['title']}</title>", html, count=1, flags=re.S)
    if n == 0:
        raise SystemExit("build.py: <title> introuvable")

    # Métas.
    html = set_meta(html, "name", "description", EN["description"])
    html = set_meta(html, "property", "og:title", EN["og:title"])
    html = set_meta(html, "property", "og:description", EN["og:description"])
    html = set_meta(html, "property", "og:url", EN["og:url"])
    html = set_meta(html, "property", "og:locale", EN["og:locale"])
    html = set_meta(html, "property", "og:locale:alternate", EN["og:locale:alternate"])
    html = set_meta(html, "name", "twitter:title", EN["twitter:title"])
    html = set_meta(html, "name", "twitter:description", EN["twitter:description"])

    # Canonique (self-referencing vers /en).
    html, n = re.subn(
        r'(<link rel="canonical" href=")[^"]*(">)',
        lambda m: m.group(1) + EN["canonical"] + m.group(2),
        html,
        count=1,
    )
    if n == 0:
        raise SystemExit("build.py: <link rel=canonical> introuvable")

    # Garde-fou anti tiret cadratin.
    if "—" in html:
        raise SystemExit("build.py: tiret cadratin (—) détecté, à corriger dans index.html")

    banner = "<!DOCTYPE html>\n<!-- Genere par build.py depuis index.html, ne pas editer a la main -->"
    html = html.replace("<!DOCTYPE html>", banner, 1)

    OUT.write_text(html, encoding="utf-8")
    print(f"OK -> {OUT.name} ({len(html)} octets)")


if __name__ == "__main__":
    main()
