# Third-party data notice

This project bundles several external datasets. The built file `index.html`
embeds all of them inline, so **`index.html` as distributed is subject to the
terms below**, not to the project's MIT licence alone.

## Bundled datasets

### SBLGNT — Greek New Testament text
`data/greek_gospels.json` (word forms)

The Greek New Testament: SBL Edition. Copyright © 2010 Society of Biblical
Literature and Logos Bible Software.
Licensed under **CC BY 4.0** — https://creativecommons.org/licenses/by/4.0/
Source: https://sblgnt.com

### MorphGNT — morphological annotation and lemmas
`data/greek_gospels.json` (lemma assignments)

MorphGNT: morphologically parsed SBLGNT. Copyright © James Tauber and
contributors.
Licensed under **CC BY-SA 3.0** — https://creativecommons.org/licenses/by-sa/3.0/
Source: https://github.com/morphgnt/sblgnt

> ⚠️ **Share-alike.** CC BY-SA 3.0 requires that adaptations of this data be
> distributed under the same or a compatible licence. Because `index.html`
> embeds the lemma assignments, anyone redistributing that built file — or a
> modified version of it — must honour the share-alike term and provide
> attribution. This repository is public and attributed, which satisfies it
> here. **If you fork this for a commercial or closed product, either comply
> with CC BY-SA 3.0 or replace the morphology layer with a permissive source.**

### World English Bible — English text
`data/web_gospels.json`

The World English Bible is in the **public domain**. No permission is required.
Retrieved via https://bible-api.com

### Natural Earth — coastline, lakes, rivers
`data/geo.json`

Natural Earth raster and vector map data is in the **public domain**.
Source: https://www.naturalearthdata.com — made with Natural Earth.
Geometry here is clipped to the Levant and simplified.

## Project-authored content

The following are original to this project and carry the MIT licence:

| File | Content |
|---|---|
| `data/harmony.py` → `harmony.json` | The 209-pericope alignment table |
| `data/places.py` → `places.json` | Gazetteer, elevations, certainty flags, journeys |
| `data/material.py` → `material.json` | Flora / fauna / money / objects entries |
| `data/place_links.json` | Derived index (generated from WEB text) |
| `app_src.html` | Application source |

The pericope divisions are informed by public-domain harmonies — A. T.
Robertson, *A Harmony of the Gospels* (1922); Stevens & Burton, *A Harmony of
the Gospels for Historical Study* (1904) — and by the Eusebian canon tables
(c. 330 AD). The specific boundaries, groupings and titles here are this
project's own editorial choices, and no copyrighted synopsis was copied.

## Attribution string

If you reuse the built file, this covers the required credits:

> Greek text: SBLGNT © 2010 Society of Biblical Literature and Logos Bible
> Software (CC BY 4.0). Morphology and lemmas: MorphGNT © James Tauber and
> contributors (CC BY-SA 3.0). English: World English Bible (public domain).
> Map data: Natural Earth (public domain).
