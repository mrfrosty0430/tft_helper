import requests
import json
import string


def buildTraits(champs):
    champFile = open("champions.json")
    champData = json.load(champFile)
    traitFile = open("traits.json")
    traitData = json.load(traitFile)

    traits = dict()
    for user_champ in champs:

        for champ in champData:
            if champ["name"] == (user_champ).strip():
                traits[(user_champ).strip()] = champ["traits"]
                break
    return traits

def start():
    apiKey = "RGAPI-9fa98d84-5df6-46d9-ae80-f8a1f71827a2"
    itemFile = open("items.json")
    itemData = json.load(itemFile)

    champFile = open("champions.json")
    champData = json.load(champFile)
    print(champData)

    traitFile = open("traits.json")
    traitData = json.load(traitFile)
    print(traitData)

    champ_input = input("choose champions, separated with a comma\n")
    print(champ_input)

    champs = champ_input.split(",")
    print(champs)
    champTraits = buildTraits(champs)
    print(champTraits)
    traitCount = dict()
    for champ in champTraits:
        print(champ)
        for trait in champTraits[champ]:
            traitCount[trait] = traitCount.get(trait, 0) + 1

    print(traitData[0])

    traitSynergy = dict()
    for user_trait in traitCount:
        for trait in traitData:
            if trait["key"] == user_trait:
                trait_val = traitCount[user_trait]
                trait_label = "n/a"
                for label in trait["sets"]:
                    label_min = label["min"]
                    if traitCount[user_trait] >= label_min:
                        trait_label = label["style"]
                traitSynergy[user_trait] = (trait_label,traitCount[user_trait])
    print(traitSynergy)



if __name__ == "__main__":
    start()