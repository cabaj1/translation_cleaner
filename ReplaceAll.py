import codecs
import json
import csv
import os

with codecs.open('path/to/translation.json','r','utf-8') as json_file:
    data = json.load(json_file)

print(data)
if os.path.exists("data.csv"):
  os.remove("data.csv")
codecs.open("data.csv","x",'utf-8')

if os.path.exists("notfound.json"):
  os.remove("notfound.json")
codecs.open("notfound.json","x",'utf-8')

if os.path.exists("output.json"):
  os.remove("output.json")
codecs.open("output.json","x",'utf-8')

if os.path.exists("outputSorted.json"):
  os.remove("outputSorted.json")
codecs.open("outputSorted.json","x",'utf-8')

with codecs.open('data.csv', 'r+','utf-8') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in data.items():
        writer.writerow([key, value])

# with codecs.open('data.csv', 'r+','utf-8') as fd:
    #     lines = fd.readlines()
    # fd.seek(0)
    # fd.writelines(line for line in lines if line.strip())
    #  fd.truncate()

os.system("RemoveUnusedTranslationKeys.sh")

print("Script is over")

with codecs.open('notfoundfinal.json','r','utf-8') as notfound:
    keys = notfound.read().splitlines()

print(keys)

for key in keys:
    if key in data:
        del data[key]

print("printing data")
print(data)


json_string = json.dumps(data, ensure_ascii=False).encode('utf8')
decodedJson = json_string.decode()
print(decodedJson)

# subprocess.call(['sh', './test.sh'])

# theJsonOutputFile = open('output.json','w')
# theJsonOutputFile.write(json.loads(decodedJson), indent=4)
# theJsonOutputFile.close()

with codecs.open('output.json', 'w','utf-8') as theJsonFile:
    json.dump(json.loads(decodedJson),theJsonFile, indent=4, ensure_ascii=False)

with codecs.open('outputSorted.json','w', 'utf-8') as theJsonFile:
    json.dump(json.loads(decodedJson),theJsonFile,indent=4, ensure_ascii=False, sort_keys=True)


