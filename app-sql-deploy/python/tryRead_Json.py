import json

with open('../json/fileA.json', 'r') as data:
    data = json.load(data)
    print(json.dumps(data, indent = 4))