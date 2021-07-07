# Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. Adın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.Əgər adını düzgün daxil edərsə, soyadının daxil etməsini istəyin. Soyad 5 hərfdən kiçik, 15 hərfdən uzun olmasın. Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin. Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır. Sonra email daxil etməsini tələb edin. Emailin uzunluğu 10 hərifdən qısa 22 hərfdən uzzun olmasın, tərkibində @gmail.com olsun və bu hissə daxil etdiyi emailin sonunda olsun. Ardınca parol axil etsin. Parol 6-13 simvol aralığında olmalıdır. Sonra parolu təsdiqləməyini tələb edin. Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır. Bütün bunlar düzgün daxil edilərsə, Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın detallarına baxmaq istəyib-istəməməsi soruşulsun. Əgər hə desə, aşağıdakı görüntü çapa verilsin: (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə, hər verdiyibiz şərtə uyğun error tipli mesaj verin. Məsələn doğum ilini 5 simvoldan ibarət daxil etsə, mesaj verilsin ki, 4 simvol daxil edin. Yəni hər şərti müvafiq mesajlar ilə userə izah edin. ============================================= Ad: Murad Soyad: Əliyev Yaş: 22 Email: muradaliyev1996@gmail.com Parol: 123456789 ============================================= Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın.

from typing import ChainMap


ad=input("Adinizi daxil edin : ")
if 3<int(len(ad))<11:
    print("adi uygun daxil etmisiniz")
    soyad=input("Soyadinizi daxil edin : ")
    if 5<int(len(soyad))<15:
        print("soyad uygun daxil edilib")
        il=(input("ilinizi daxil edin : "))
        if len(il)==4:
            print("ili duzgun daxil etmisiniz")
            email=input("Emailinizi daxil edin : ")
            if 10<int(len(email))<22:
                print("uygun daxil etmisiniz")
                parol=input("Parolunuzu daxil edin : ")
                if 6<int(len(parol))<13:
                    print("dogru daxil etmisiniz")
                else:
                    print("parol 6 13 herf araliginda olmalidir")
                    paroluDogrula=input("Parolunuzu daxil edin : ")
                    if parol==paroluDogrula:
                        print("qeydiyyat tamamlandi")
                        detallar=input("detallara baxmaq isteyerdiniz ??? : ")
                        if detallar=="he":
                            print("Ad:{} Soyad:{} yash: {} Email: {} Parol:{}".format(ad , soyad , 2021-int(il) , email ,parol))
                        else:
                            print("{} {} Uğurlar! Yazılsın.".format(ad ,soyad))
            else:
                print("emailiniz 10 herfden qisa 22 herfden uzun olmamalidi")
        else:
            print("4 simvoldan ibaret olalidi")
    else:
        print("soyad 5 herfden kichik 15 herfden chox olmamalidi")
    
else:
    print("ad 3-den kichik 11-den boyuk olmamalidir")
    







