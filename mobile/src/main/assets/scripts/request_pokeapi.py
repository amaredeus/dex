import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('data_type', help = 'The pokeapi data type to request from.')
dataString = parser.parse_args().data_type
startId = 1
baseUrl = 'http://localhost:8000/api/v2/'

while True:
    # Call the poke moves request
    url = baseUrl + dataString + '/' + str(startId)
    response = requests.get(url)

    if response.status_code == requests.codes.not_found:
        print('Finished.')
        break

    dataJson = response.json()

    fileName = dataString + '_'+ str(startId) + '.json'
    with open('../in/' + fileName, 'w') as dataFile:
        json.dump(dataJson, dataFile)
        print(fileName)

    startId += 1