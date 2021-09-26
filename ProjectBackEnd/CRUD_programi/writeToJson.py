
import json
from os import name

# connect to file 

name=input("adinizi daxil edin : ")
surname=input("soyadinizi daxil edin : ")


stud={
    "ad" : name ,
    "soyad": surname,
}

convertDictToJson=json.dumps(stud)

# file.write(f"{stud['ad']} , {stud['soyad']}")

# file.write(convertDictToJson)
