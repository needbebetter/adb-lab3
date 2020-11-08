from pymongo import MongoClient
import json

# Jackie
# e0dG51i6aWL6k2WG

def clientCreate(name):
    return MongoClient("mongodb+srv://Jackie:e0dG51i6aWL6k2WG@cluster.kce3k.mongodb.net/"+name+"?retryWrites=true&w=majority")

client1 = clientCreate('gas')
client2 = clientCreate('heatSupply')
client3 = clientCreate('sewerage')
client4 = clientCreate('smn')
client5 = clientCreate('water')

# hsDB = client2['heatSupply']
# hsColl = hsDB['heatSupplyColl']

def collCreate(name, client):
    db = client[name]
    coll = db[name+'Coll']
    return coll

hsState = collCreate('heatSupply',client2)

def openf(jsonk):
    with open('data/'+jsonk+'.json', 'r', encoding='utf-8') as data:
        jsonS = json.load(data)
        return jsonS

hsJSON = openf('HeatSupplyNetworks')

for state in hsJSON:
    # print(state)
    hsState.insert_one(state)