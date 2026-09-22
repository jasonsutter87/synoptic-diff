# Bible Companion — Synoptic Diff

**[Open the app →](https://jasonsutter87.github.io/synoptic-diff/)**

A multi-level Bible study tool. The premise: every Bible app ships the same flat
reader, so this one reads a passage at **four depths** and treats the gospels as
something you can **diff**.

## The four layers

| | | |
|---|---|---|
| **L1** | Historical | What can actually be established — archaeology, dating, geography, what's disputed |
| **L2** | Literal | What the text plainly says, and what it asks of a life |
| **L3** | Symbolic | The pattern beneath — recurring images, numbers, structure |
| **L4** | Spiritual | The path of becoming, readable without requiring belief |

This is not invented. It maps onto **PaRDeS** (Peshat / Remez / Derash / Sod) and
the Christian **Quadriga** (literal / allegorical / tropological / anagogical) —
how scripture was read for roughly 1,500 years. The remix here is splitting the
literal into a *historical* layer and a *plain-text* layer, because "did any of
this actually happen?" is the real barrier for a modern reader and no Bible app
answers it honestly.

## What's built

**`index.html`** — all four gospels. This is the built app.

- **209 pericopes** covering every verse of Matthew, Mark, Luke and John.
  Machine-verified at **100% verse coverage, zero overlaps**.
- **Structural diff** — what each gospel places either side of a given unit.
  Reordering becomes the finding rather than diff noise.
- **Textual diff** — LCS word alignment across the gospels that carry a unit,
  in English *or* Greek. Diff the Greek and you're comparing evangelists;
  diff the English and you're comparing translators.
- **Word study** — lemma search across 64,499 Greek words, with per-gospel
  distribution and clickable occurrences.
- **Map** — 43 places with real coordinates, elevations and certainty flags;
  7 toggleable journeys; elevation profiles measured against sea level.
  Every place links to the pericopes that name it.
- **Material world** — 28 entries across flora, fauna, money and objects, with
  47 tracked lemmas and live counts. Selection rule: an entry earns its place
  only when the real thing changes how the passage reads.
- **Reader** — type a reference (`Matthew 19`, `mk 8`, `John 3:16`,
  `Matthew 5:1-12`) and read it straight through, in English or Greek. The
  reader marks where each **pericope begins** and prints its parallels beside
  the seam, so the structure of a chapter is visible while you read it.
  Anything that isn't a reference is searched as text across all 3,779 verses.

**`prototype.html`** — the original two-passage prototype (Fig Tree & Temple,
the Two Feedings). Kept because it's a tighter read of the core idea.

## The material world

Darnel (*Lolium temulentum*) is visually indistinguishable from wheat until it
heads, which is why the parable says to leave it — you cannot identify it early,
let alone pull it. Mustard is a weed that reaches 3 m from a 1 mm seed. The
Syrophoenician woman is offered the **diminutive** *kynarion*, a house dog, not
the insult *kyōn*. Greek has three words for "net" — a one-man cast net, a
sweeping dragnet, and a generic one — and the kingdom parable uses the dragnet
precisely because it takes everything. English prints one word for all three.

## Two things the data proved

**The baskets never cross.** κόφινος appears 6 times and σπυρίς 4 times across
the whole four-gospel corpus. Every *kophinos* belongs to the feeding of the
5,000; every *spyris* to the 4,000. Zero exceptions. English prints "basket"
both times, so the distinction — twelve for the tribes of Israel, seven for the
nations — is invisible in every English Bible app that exists.

**23 verses have no Greek**, and they're exactly the famous textual variants:
the pericope adulterae (John 7:53–8:11), the angel at Bethesda, Mark 7:16,
9:44, 9:46, 11:26, 15:28, Matthew 17:21, 18:11, 23:14, Luke 17:36, 23:17.
The app flags each as *present in the Byzantine/KJV tradition, absent from
SBLGNT* rather than hiding it. This fell out of comparing two datasets; it
wasn't a planned feature.

## Build

```sh
python3 build.py          # app_src.html + data/*.json -> index.html
```

Everything is inlined into a single file — the artifact CSP blocks same-origin
`fetch`, so external data loading isn't available. No dependencies, no bundler,
no server. Open `index.html` in a browser.

Regenerate the derived datasets:

```sh
cd data
python3 harmony.py        # -> harmony.json   (the alignment table)
python3 places.py         # -> places.json    (gazetteer + journeys)
```

## Data sources and licences

| Dataset | Source | Licence |
|---|---|---|
| English text | World English Bible, via bible-api.com | Public domain |
| Greek text | SBLGNT (Logos Bible Software & SBL) | **CC BY 4.0** |
| Greek lemmas/morphology | MorphGNT | **CC BY-SA 3.0** |
| Coastline, lakes, rivers | Natural Earth 10m | Public domain |
| Pericope divisions | Robertson (1922), Stevens & Burton (1904), Eusebian canons | Public domain |
| Harmony, gazetteer, material-world notes | Written for this project | — |

Full terms, including the required attribution string, are in
**[NOTICE.md](NOTICE.md)**. Project source is MIT — see [LICENSE](LICENSE).

⚠️ **MorphGNT is share-alike.** The lemma data embedded in `index.html` carries
CC BY-SA 3.0, which propagates to anything distributing it. If this ever ships
commercially, either honour the SA terms or swap the morphology layer for a
permissive source.

## Colour

The four gospel colours are validated, not chosen by eye. The first palette
(rubric red for Mark, gold for Matthew) **failed**: ΔE 12.6 in normal vision and
4.2 under deuteranopia — Matthew and Mark were near-identical, in an app whose
whole purpose is telling them apart. Current set passes lightness-band, chroma,
CVD-separation, normal-vision and contrast checks in both light and dark:

| | Light | Dark |
|---|---|---|
| Matthew | `#1263A8` | `#4A90D9` |
| Mark | `#B8500A` | `#CE7430` |
| Luke | `#0A7D5A` | `#2BA075` |
| John | `#9B4F96` | `#B96FB3` |

## Known limits

- **Four-layer commentary covers two studies.** 209 pericopes × 4 layers is
  ~200,000 words that all have to be *good*; generic filler would kill the thing
  that makes this work. The app says so plainly instead of faking coverage.
- **The harmony is one editorial opinion.** Where a pericope begins and ends is a
  judgment call and I made 209 of them; Robertson and Aland disagree with each
  other in places. `data/harmony.py` is one line per pericope, readable and
  editable.
- **Journey routes are schematic.** The gospels give sequences of places, not
  roads. Two journeys (Infancy, Resurrection) are routes the gospels actively
  disagree about, and the app says so.
- **Place links find pericopes that *name* a place**, which is not always where
  the scene is set.
- **Lemma counts are verses, not word instances.** A lemma appearing twice in one
  verse counts once (τάλαντον: 14 words across 8 verses). The UI says "verses".

## Next

- Ground L1–L3 in the public-domain commentaries (Matthew Henry, Keil &
  Delitzsch, Pulpit) so they're citable rather than invented. Keep L4
  hand-written — that voice is the part that can't be outsourced.
- **Gergesenes vs Gadarenes.** Matthew names one place, Mark and Luke another,
  for the same exorcism — and Gadara sits 10 km inland with no cliff, while
  Kursi is on the shore with one. First case where the diff engine and the map
  argue with each other.
- The symbolic web (L3), the git-graph timeline, and the relationship graph —
  all queries against this same dataset rather than separate apps.
