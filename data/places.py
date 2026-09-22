# -*- coding: utf-8 -*-
"""Gospel gazetteer. elev = metres relative to sea level.
cert: 3=securely identified  2=probable  1=disputed (rival candidate sites)."""
import json
P=[
# name, lat, lon, elev, cert, region, aliases
("Jerusalem",31.7781,35.2356,754,3,"Judea","Jerusalem|Zion"),
("Bethlehem",31.7054,35.2024,775,3,"Judea","Bethlehem"),
("Bethany",31.7719,35.2631,710,3,"Judea","Bethany"),
("Bethphage",31.7761,35.2531,730,2,"Judea","Bethphage"),
("Mount of Olives",31.7784,35.2464,826,3,"Judea","Mount of Olives|Olivet"),
("Gethsemane",31.7794,35.2397,700,2,"Judea","Gethsemane"),
("Golgotha",31.7784,35.2297,760,2,"Judea","Golgotha|Calvary|skull"),
("Jericho",31.8569,35.4606,-258,3,"Judea","Jericho"),
("Emmaus",31.8397,35.0219,350,1,"Judea","Emmaus"),
("Ephraim",31.9333,35.2833,700,1,"Judea","Ephraim"),
("Hebron",31.5326,35.0998,930,3,"Judea","Hebron"),
("Ein Karem",31.7658,35.1628,650,1,"Judea","hill country"),
("Wilderness of Judea",31.7400,35.3800,200,2,"Judea","wilderness"),
("Bethany beyond Jordan",31.8372,35.5453,-370,1,"Jordan Valley","beyond the Jordan|Bethabara"),
("Jordan River",31.9000,35.5500,-350,3,"Jordan Valley","Jordan"),
("Salim / Aenon",32.3200,35.5600,-200,1,"Jordan Valley","Aenon|Salim"),
("Machaerus",31.5661,35.6244,700,2,"Perea","Machaerus"),
("Nazareth",32.7019,35.2978,350,3,"Galilee","Nazareth"),
("Capernaum",32.8808,35.5752,-210,3,"Galilee","Capernaum"),
("Cana",32.7461,35.3419,250,1,"Galilee","Cana"),
("Bethsaida",32.9106,35.6306,-200,1,"Galilee","Bethsaida"),
("Chorazin",32.9106,35.5642,-30,3,"Galilee","Chorazin|Chorazim"),
("Magdala",32.8247,35.5158,-200,2,"Galilee","Magdala|Magdalene"),
("Tiberias",32.7922,35.5312,-200,3,"Galilee","Tiberias"),
("Nain",32.6317,35.3444,200,3,"Galilee","Nain"),
("Gennesaret",32.8450,35.5300,-200,2,"Galilee","Gennesaret"),
("Sea of Galilee",32.8200,35.5900,-211,3,"Galilee","Sea of Galilee|sea of Tiberias|lake"),
("Mount Tabor",32.6869,35.3906,588,2,"Galilee","Tabor"),
("Kursi (Gergesa)",32.8244,35.6497,-190,1,"Decapolis","Gerasenes|Gadarenes|Gergesenes"),
("Caesarea Philippi",33.2486,35.6944,350,3,"Iturea","Caesarea Philippi"),
("Mount Hermon",33.4164,35.8572,2814,3,"Iturea","Hermon|high mountain"),
("Tyre",33.2705,35.2038,10,3,"Phoenicia","Tyre"),
("Sidon",33.5571,35.3719,10,3,"Phoenicia","Sidon"),
("Gadara",32.6556,35.6847,350,3,"Decapolis","Gadara"),
("Gerasa",32.2811,35.8911,585,3,"Decapolis","Gerasa"),
("Hippos",32.7783,35.6600,350,2,"Decapolis","Hippos"),
("Scythopolis",32.5000,35.5000,-120,3,"Decapolis","Beth Shean|Scythopolis"),
("Sychar",32.2139,35.2806,550,1,"Samaria","Sychar|Jacob's well"),
("Mount Gerizim",32.2000,35.2725,881,3,"Samaria","this mountain|Gerizim"),
("Samaria (Sebaste)",32.2769,35.1917,430,3,"Samaria","Samaria"),
("Caesarea Maritima",32.5000,34.8917,5,3,"Coast","Caesarea"),
("Joppa",32.0536,34.7522,30,3,"Coast","Joppa"),
("Dead Sea",31.5000,35.4700,-430,3,"Judea","Salt Sea"),
]
JOURNEYS=[
 {"id":"infancy","name":"Infancy","color":"--jn",
  "stops":["Nazareth","Bethlehem","Jerusalem","Bethlehem","Nazareth"],
  "offmap":"Egypt","note":"Matthew sends the family to Egypt and back; Luke sends them straight home to Nazareth. The gospels do not agree on this route."},
 {"id":"baptism","name":"Baptism & temptation","color":"--lk",
  "stops":["Nazareth","Bethany beyond Jordan","Wilderness of Judea"],
  "note":"From the hills of Galilee down to the lowest river on earth — a descent of roughly 720 m."},
 {"id":"galilee","name":"Early Galilean ministry","color":"--mk",
  "stops":["Nazareth","Cana","Capernaum","Chorazin","Bethsaida","Gennesaret","Nain"],
  "note":"Capernaum becomes the base of operations. Almost everything in Mark 1–6 happens within a day's walk of this shore."},
 {"id":"north","name":"Northern withdrawal","color":"--mt",
  "stops":["Capernaum","Tyre","Sidon","Kursi (Gergesa)","Bethsaida","Caesarea Philippi","Mount Hermon"],
  "note":"The gentile arc. Between the two feedings Mark runs the whole circuit through Phoenicia and the Decapolis — which is why the second crowd is fed on foreign ground."},
 {"id":"tojerusalem","name":"The road to Jerusalem","color":"--lk",
  "stops":["Capernaum","Scythopolis","Sychar","Bethany beyond Jordan","Jericho","Bethany","Jerusalem"],
  "note":"Luke's travel narrative — ten chapters of it. The last leg from Jericho climbs 1,012 m in about 24 km."},
 {"id":"passion","name":"Passion week","color":"--mk",
  "stops":["Bethany","Bethphage","Mount of Olives","Jerusalem","Gethsemane","Golgotha"],
  "note":"Six days inside a five-kilometre radius."},
 {"id":"resurrection","name":"After the resurrection","color":"--jn",
  "stops":["Jerusalem","Emmaus","Jerusalem","Sea of Galilee"],
  "note":"Luke keeps the appearances around Jerusalem; Matthew and John send the disciples back to Galilee. Another route the gospels do not agree on."},
]
places=[{"name":n,"lat":la,"lon":lo,"elev":e,"cert":c,"region":r,"alias":a.split("|")}
        for n,la,lo,e,c,r,a in P]
json.dump({"places":places,"journeys":JOURNEYS},open("places.json","w"),ensure_ascii=False,indent=0)
print(len(places),"places |",len(JOURNEYS),"journeys")
print("elev range:",min(p['elev'] for p in places),"to",max(p['elev'] for p in places),"m")
missing=[s for j in JOURNEYS for s in j["stops"] if s not in {p["name"] for p in places}]
print("unresolved stops:",missing or "none")
