### Bir mesajı dəyişəndə saxlayın və sonra mesajı çapa verin
# e="Azerbaycan respublikasina xidmet edirem"
# print(e)

## input( "adinizi qeyd edin : ")
# input("Adinizi qeyd edin : ")

### ad və soyad dəyişkənləri yaradın və onlara istədiyiniz kiçik hərflərdən ibarət dəyər verin. Sonra tam_ad adlı dəyərdə ad və soyadın ilk hərflərini böyük şəkildə çapa verərək həmin şəxsə Salam verin.
# ad="ragim "
# soyad="gagli"
# tam_ad=ad.capitalize()+soyad.capitalize()
# print("Salam " +tam_ad)

### İki ədədi iki müxtəlif dəyişkənə mənimsədin sonra isə onların bir birlərinə olan qüvvətini tapın

# a = 2 
# b = 3
# c = a**b
# print(c)

# str tipinden int diline chevire bilmerik chunku int tipinde noqte herf ve s. istifade etmek olmaz eger str ye yazilanin xarakteri herfdirse.

# y="4.92"
# d=int(float("4.92"))
# print(int(d))

### İstifadəçidən havanın temperaturunu soruşun. 10 dərəcədən aşağı olarsa temperatur, ekrana soyuq, 20 dərəcə olarsa, Normal, 30 dərəcədən yüksək olarsa İsti sözü yazılsın.

# ht= int(input(" havanin temperaturu neche derecedir ??? : "))
# if ht <10:
#     print("soyuq")
# elif  ht==20:
#    print("Normal")
# if ht>30:
#    print("cehennem istisi")

### 'Proqramlaşdırma' sözündə 'x' hərfinin olub-olmamasının yoxlayın

# R="Programlashdirma"
# print ("x" in R )

### iki dənə string tipində dəyişkən yaradıb onları başqa bir string dəyərdə birləşdirib saxlayın və həmin string dəyəri ekrana yazdırın.
# fa="SALAM "
# la=" ALEYKUM"
# do=fa+la
# print(do)

### homework Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.
# a = 4
# b = 4
# c = a*b
# print(c)

### Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.

# reqemler=[87,99,34,42]
# for i in reqemler:
#     if i==max(reqemler):
#         print(i)

# girish=(input())
# enBoyukReeqem=[87,99,34,42]
# for i in range (1,girish+1):
#     reqem=int(f"{i} reqem yazin")
#     print(max(enBoyukReeqem))
#     enBoyukReeqem.append(reqem)

###  Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.

# print("alma","heyva","armud","nar")
# meyveler_ve_qiymetleri={"alma":"1azn","armud":"1.50azn","heyva":"5_azn","nar":"2,50_azn"}

# for meyve in meyveler_ve_qiymetleri.keys():
#     print(meyve)
# sechilmishMeyve=input("menudan bir meyve sechin ve bura daxil edin ")

# if sechilmishMeyve in meyveler_ve_qiymetleri.keys():
#         print(meyveler_ve_qiymetleri[sechilmishMeyve])
# else :
#         print("yoxdur")

### Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. Adın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.Əgər adını düzgün daxil edərsə, soyadının daxil etməsini istəyin. Soyad 5 hərfdən kiçik, 15 hərfdən uzun olmasın. Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin. Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır. Sonra email daxil etməsini tələb edin. Emailin uzunluğu 10 hərifdən qısa 22 hərfdən uzzun olmasın, tərkibində @gmail.com olsun və bu hissə daxil etdiyi emailin sonunda olsun. Ardınca parol axil etsin. Parol 6-13 simvol aralığında olmalıdır. Sonra parolu təsdiqləməyini tələb edin. Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır. Bütün bunlar düzgün daxil edilərsə, Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın detallarına baxmaq istəyib-istəməməsi soruşulsun. Əgər hə desə, aşağıdakı görüntü çapa verilsin: (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə, hər verdiyibiz şərtə uyğun error tipli mesaj verin. Məsələn doğum ilini 5 simvoldan ibarət daxil etsə, mesaj verilsin ki, 4 simvol daxil edin. Yəni hər şərti müvafiq mesajlar ilə userə izah edin. ============================================= Ad: Murad Soyad: Əliyev Yaş: 22 Email: muradaliyev1996@gmail.com Parol: 123456789 ============================================= Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın.

# ad=input("Adinizi daxil edin : ")
# if 3<int(len(ad))<11:
#     print("adi uygun daxil etmisiniz")
#     soyad=input("Soyadinizi daxil edin : ")
#     if 5<int(len(soyad))<15:
#         print("soyad uygun daxil edilib")
#         il=(input("ilinizi daxil edin : "))
#         if len(il)==4:
#             print("ili duzgun daxil etmisiniz")
#             email=input("Emailinizi daxil edin : ")
#             if 10<int(len(email))<22:
#                 print("uygun daxil etmisiniz")
#                 parol=input("Parolunuzu daxil edin : ")
#                 if 6<int(len(parol))<13:
#                     print("dogru daxil etmisiniz")
#                 else:
#                     print("parol 6 13 herf araliginda olmalidir")
#                     paroluDogrula=input("Parolunuzu daxil edin : ")
#                     if parol==paroluDogrula:
#                         print("qeydiyyat tamamlandi")
#                         detallar=input("detallara baxmaq isteyerdiniz ??? : ")
#                         if detallar=="he":
#                             print("Ad:{} Soyad:{} yash: {} Email: {} Parol:{}".format(ad , soyad , 2021-int(il) , email ,parol))
#                         else:
#                             print("{} {} Uğurlar! Yazılsın.".format(ad ,soyad))
#             else:
#                 print("emailiniz 10 herfden qisa 22 herfden uzun olmamalidi")
#         else:
#             print("4 simvoldan ibaret olalidi")
#     else:
#         print("soyad 5 herfden kichik 15 herfden chox olmamalidi")
    
# else:
#     print("ad 3-den kichik 11-den boyuk olmamalidir")

### homework

# Write a Python function to sum all the numbers in a list.

# def numberlist():
#     numbers=[8,2,3,0,7]
#     sum=0
#     for i in numbers:
#         sum+=i
#     print(sum)
#     return sum

# numberlist()

# -Write a Python function to multiply all the numbers in a list.

# def numberlist():
#     numbers=[8, 2, 3, -1, 7]
#     sum=1
#     for i in numbers:
#         sum *=i
#         print(sum)
#     return sum
# numberlist()

# -Write a function called returnDay. This function takes in one parameter ( a number from 1-7)
# and returns the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or
# greater
# than 7, the function should return None.


# def returnsday():
#     weekday=int(input("eded daxil edin : "))
#     weekdays={1:"Monday",2"Thursday","wednesday":3,"thoursday":4,"friday":5,"saturday":6,"sunday":7}
#     if 1<=weekday<=7:
#         print(weekdays[weekday])
#     else:
#         print("bir le yeddi araliginda reqem yazin")
    

# returnsday()

# def numbers(listtt):
#     if len(listtt)>0:
#         print(listtt[-1])
#     else:
#         print(None)
# numbers([1,2,3,4,5,6,7,8])

# def evenNumbers(numbers):
#      evenNums=[]
#      for i in numbers:
#          if i%2==0:
#              evenNums.append(i)
#      print(*evenNums)

# evenNumbers([1,2,3,4,5,6,7,8,9])




# from _typeshed import WriteableBuffer


# class qeydiyyatFormu:
#     def __init__(self,name,surname,email,password):
#         self.name=name
#         self.surname=surname
#         self.email=email
#         self.password=password




# w1= Worker("elchin","beshirzade","elchin.mail.com","slfnlksnlksn1232424")
# w2 = Worker("memmed","hesenov","memmedemail.com","mm14463")
# print(w1.name)
# print(w2.surname)

# connect to file 
# # open() json ve ya txt fayli varsa onun ichine yazir ve ya yoxdusa ozu yaradir ve sonra yazilari daxil edir oxuyur deyishir.
# file=open("sample.json","a")  

# name=input('adinizi daxil edin : ')
# surname=input('soyadinizi daxil edin : ')
# file.write(name+'\n' )
# # data=file.read()
# print(name )

# stud={
#     "ad" : name ,
#     "soyad": surname,
# }

# file.write(f"{stud['ad']} , {stud['soyad']}")


# # # Decorator

#  BU bir DECORATOR'dur ve Class'lara benzeyir.
# 
# qablashdir() funksiyasi bize parametr verir .
# def qablashdir(heykelDuzelt):
#     def daxiliIshGorenMethod():
#         heykel=heykelDuzelt()
#         return heykel +" qablashdirma et"
#     return daxiliIshGorenMethod

# funksiyalarimizi yazirig .
# @qablashdir
# def tamHeykelduzelt():
#     return " tam boy heykel"
# def bustDuzelt():
#     return " bust "

# # deyishene funksiyamizi menimsedib istediyimiz parametri veririy.
# ishGorenAparat=qablashdir(tamHeykelduzelt)
# print(ishGorenAparat())
# bu ishimizi daha da sadeleshdirmek ve qisa etmek uchun @qablasdir yazirig funksiyanin uzerine ve print'e veririk.

### Decorator

#  BU bir DECORATOR'dur ve Class'lara benzeyir.
# qablashdir() funksiyasi bize parametr verir .
# def qablashdir(heykelDuzelt):
#     def daxiliIshGorenMethod():
#         heykel=heykelDuzelt()
#         return heykel +" qablashdirma et"
#     return daxiliIshGorenMethod

# # funksiyalarimizi yazirig .
# @qablashdir
# def tamHeykelduzelt():
#     return " tam boy heykel"
# @qablashdir
# def bustDuzelt():
#     return " bust "

# print(bustDuzelt())

# deyishene funksiyamizi menimsedib istediyimiz parametri veririy.
# ishGorenAparat=qablashdir(tamHeykelduzelt)
# print(ishGorenAparat())
# bu ishimizi daha da sadeleshdirmek ve qisa etmek uchun @qablasdir yazirig funksiyanin uzerine ve print'e veririk.