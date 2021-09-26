import json

file=open("sample.json","a")

dataFromJason=file.read()
convertJsonToDict=json.loads(dataFromJason)

for dct in convertJsonToDict:
    if dct ["ad"]=="elchin":
        convertJsonToDict.remove(dct)
print(convertJsonToDict)