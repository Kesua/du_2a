import json
def nahrani_dat():
    with open('export.geojson') as f:
        data = json.load(f)
        A = []
    for feature in data ['features']:
    #print feature ['geometry']['coordinates']
        A.append(feature['geometry']['coordinates'])

print A
    #features = data['features']
    #souradnice = coordinates('features',"geometry")
    #print(souradnice)























#souradnice = data ['geometry']['coordinates']
#for feature in data['features']:
    #print feature['geometry']['type']
    #print feature['geometry']['coordinates']