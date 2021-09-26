
import json
file=open("sample.json","a")

dataFromJason=file.read()

convertJsonToDict=json.loads(dataFromJason)

print(dataFromJason)