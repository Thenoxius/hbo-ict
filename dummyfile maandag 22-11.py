import json
print('hello world')
with open('steam.json', 'r') as json_file:
    data = json.load(json_file)
    aantalgames = 0
    for names in data:
        aantalgames+=1
        print(names['name'])
    print(aantalgames)
    print(len(data))