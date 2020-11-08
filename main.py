from pymongo import MongoClient
import json

# Jackie
# e0dG51i6aWL6k2WG

def clientCreate(name):
    return MongoClient("mongodb+srv://Jackie:e0dG51i6aWL6k2WG@cluster.kce3k.mongodb.net/"+name+"?retryWrites=true&w=majority")

def collCreate(name, client):
    db = client[name]
    coll = db[name+'Coll']
    return coll

def openf(jsonFile):
    with open('data/'+jsonFile+'.json', 'r', encoding='utf-8') as data:
        jsonList = json.load(data)
        return jsonList

def insert(dataJSON, st):
    for state in dataJSON:
        st.insert_one(state)

client1 = clientCreate('gas')
client2 = clientCreate('heatSupply')
client3 = clientCreate('sewerage')
client4 = clientCreate('smn')
client5 = clientCreate('water')

gasState = collCreate('gas',client1)
hsState = collCreate('heatSupply',client2)
sewerageState = collCreate('sewerage',client3)
smnState = collCreate('smn',client4)
waterState = collCreate('water',client5)

gasJSON = openf('GasSupplyNetworks')
hsJSON = openf('HeatSupplyNetworks')
sewerageJSON = openf('SewerageNetworks')
smnJSON = openf('ShareOfModernNetworks')
waterJSON = openf('WaterSupplyNetworks')

insert(gasJSON, gasState)
insert(hsJSON, hsState)
insert(sewerageJSON, sewerageState)
insert(smnJSON, smnState)
insert(waterJSON, waterState)