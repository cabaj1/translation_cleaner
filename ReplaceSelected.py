# Run this file when you have gone over 'notFoundFinal' and made a selection
# Save each key on a new line and name it as 'notfoundfinal_lookedThrough.json'
# todo: make it a txt.
import codecs
import json

with codecs.open('notfoundfinal_lookedThrough.json','r','utf-8') as notfound:
    keys = notfound.read().splitlines()

with codecs.open('path/to/translation.json','r','utf-8') as json_file:
    data = json.load(json_file)

print(keys)
print(data)

for key in keys:
    if key in data:
        del data[key]

json_string = json.dumps(data, ensure_ascii=False).encode('utf8')
decodedJson = json_string.decode()

print(decodedJson)

with codecs.open('outputManuallyChecked.json', 'w','utf-8') as theJsonFile:
    json.dump(json.loads(decodedJson),theJsonFile, indent=4, ensure_ascii=False)
