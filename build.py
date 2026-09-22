#!/usr/bin/env python3
"""Build app.html from app_src.html + data/*.json.

The source template carries /*__NAME__*/ placeholders; each is replaced with the
minified contents of the matching dataset. Everything ships in one file because
the artifact CSP blocks same-origin fetch for data.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).parent
DATA = {
    "__WEB__":   "web_gospels.json",     # WEB English, 3,779 verses
    "__GK__":    "greek_gospels.json",   # SBLGNT/MorphGNT, lemmatised
    "__HARM__":  "harmony.json",         # 209-pericope alignment
    "__GEO__":   "geo.json",             # Natural Earth, clipped
    "__PLC__":   "places.json",          # gazetteer + journeys
    "__PLINK__": "place_links.json",     # pericope -> place index
    "__MAT__":   "material.json",       # flora/fauna/money/objects
}

def main():
    html = (ROOT / "app_src.html").read_text(encoding="utf-8")
    for key, fname in DATA.items():
        token = f"/*{key}*/"
        if token not in html:
            sys.exit(f"missing placeholder {token} in app_src.html")
        blob = json.loads((ROOT / "data" / fname).read_text(encoding="utf-8"))
        html = html.replace(token, json.dumps(blob, ensure_ascii=False, separators=(",", ":")))
    leftover = re.findall(r"/\*__[A-Z_]+__\*/", html)
    if leftover:
        sys.exit(f"unreplaced placeholders (add them to DATA): {sorted(set(leftover))}")
    out = ROOT / "app.html"
    out.write_text(html, encoding="utf-8")
    print(f"built {out.name} — {len(html)/1024/1024:.2f} MB")

if __name__ == "__main__":
    main()
