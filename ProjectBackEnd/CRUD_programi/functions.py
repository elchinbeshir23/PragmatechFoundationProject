
from models import *
import json
id=1
def addUsers():
    while True:
        global id
        ad=input("ad :")
        soyad=input("soyad :")
        email=input("email :")
        tel=input("tel :")
        user=User(id,ad,soyad,email,tel)
        users.append(user.__dict__)
        id+=1
        file=open("sample.json","a")
        userJson=json.dumps(users)
        file.write(userJson)
        emr=input("yeni istifadechi elave etmek isteyirsiniz mi ??? Y/N : ")
        if emr=="N":
            break
    
                        
def showAllUsers():
    file=open("sample.json","r")
    dataFromJason=file.read()
    convertJsonToDict=json.loads(dataFromJason)
    for n in convertJsonToDict:
        print(f"istifadechinin adi {n['ad']} , istifadechinin soyadi {n['soyad']}")

    # for user in users:
    #     user.showUsersData()
def deleteUser():
        silinecekId=int(input("silinecek istifadechinin id sini yazin :"))
        file=open("sample.json","r")
        dataFromJason=file.read()
        convertJsonToDict=json.loads(dataFromJason)
        for n in convertJsonToDict:
            if n["id"]==silinecekId:
                convertJsonToDict.remove(n)
        file=open("sample.json","r")
        userJson=json.dumps(convertJsonToDict)
        file.write(userJson)
        
def uptadeUser():
        deyishdirilecekIstifadechi=int(input("deyishdirilecek istifadechinin id sini yazin :"))
        file=open("sample.json","r")
        dataFromJason=file.read()
        convertJsonToDict=json.loads(dataFromJason)
        for n in convertJsonToDict:
            if n["id"]==deyishdirilecekIstifadechi:
                ad=input("silinecek adi daxil edin : ")
                n["ad"]=ad
        file=open("sample.json","w")
        userJson=json.dumps(convertJsonToDict)
        file.write(userJson)