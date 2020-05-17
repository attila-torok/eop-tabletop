# Downloads the latest cards.yaml from Adam Shostack's git, append the Privacy suit and create a CVS to upload to playcards.io

PLAYINGCARDS_CVS = "playingcards_eop.csv"
CARDS_GITHUB_RAW_URL = "https://raw.githubusercontent.com/adamshostack/eop/master/cards.yaml"
CARDS_YAML = "eop.yaml"
EXPANSION_YAML = "expansion_cards.yaml"

import yaml
import csv
import requests

#download cards.yaml and remove lines starting with  '//'  -- otherwise it would break yaml load
open("cards.yaml", 'wb').write(requests.get(CARDS_GITHUB_RAW_URL).content)
with open(CARDS_YAML, "w") as f:
    for i,line in enumerate(open("cards.yaml", "r")):
        if not line.startswith('//'):
            f.write(line)
    f.write('\n')

#add privacy expansion suit
print("cards.yaml downloaded and cleaned:",CARDS_YAML)
cards = yaml.safe_load(open(CARDS_YAML))  #load clean yaml (no // lines)
print("loading expansions from:",EXPANSION_YAML)

expansion_cards = yaml.safe_load(open(EXPANSION_YAML))
for suit in expansion_cards["suit_order"]:
    
    print("\texpansion:", suit)
    cards["suit_order"].append(suit)
    for i in expansion_cards['suits']:
        cards['suits'].update({i:expansion_cards['suits'][i]})

#create a new file with merged yaml
yaml.dump(cards,open(CARDS_YAML, 'w'))

#parse complete yaml and export to cvs
print("decks merged to:",CARDS_YAML)
cards = yaml.safe_load(open(CARDS_YAML))
print("exporting to cvs")

with open(PLAYINGCARDS_CVS, "w") as cvsfile:
    wr = csv.writer(cvsfile, lineterminator="\n")
    # wr.writeheader()
    wr.writerow(["label", "suit", "rank", "threat"])
    for suit in cards["suit_order"]:
        print("\t"+suit)
        for rank, threat in cards["suits"][suit].items():
            wr.writerow(["".join([str(rank), " of ", suit]), suit, rank, threat])
            # print(suit,rank,threat)

print("exported to:",PLAYINGCARDS_CVS)