import json
import re
import requests
import csv

from shared import *

data_type = 'item-attribute'

def read_poke_move():
    pokeId = 1
    while True:
        try:
            with open('../in/' + data_type + '_' + str(pokeId) + '.json', 'r') as dataFile:
                pokeData = json.loads(dataFile.read())

                # Move Localization
                for lang in fileLangs:
                    # name = pokeData['name']
                    name = getLocalText(lang, 'name', pokeData['names'])
                    description = getLocalText(lang, 'description', pokeData['descriptions'])
                    dataLocal = {"id": pokeId, "name": name, "description": description}
                    pokeDataLangs[lang].append(dataLocal)
                    
                print('pokeId: ' + str(pokeId))
                pokeId += 1
        except FileNotFoundError:
            break

    # Write to each poke moves lang
    for lang in fileLangs:
        with open('../out/item_attribute_' + lang + '.json', 'w') as langFile:
            json.dump(pokeDataLangs[lang], langFile)

if __name__ == '__main__':
    read_poke_move()