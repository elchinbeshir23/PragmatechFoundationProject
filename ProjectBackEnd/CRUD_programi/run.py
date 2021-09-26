

from functions import *


while True:

    print("""

             - Yeni istifadechi yaratmaq uchun 1 duymesine basin .
             - istifadechileri gorebilmek uchun 2 duymesine basin .
             - istifadechini deyishmek uchun 3 duymesine basin .
             - istifadechi silmek uchun 4 duymesine basin .
             - Proqramdan chixmaq uchun 5 duymesine basin .
             
             
              """)

    order=input("istediyiniz emeliyyat nomresini daxil edin :")
    

    if order=="1":
        addUsers()
    elif order=="2":
        showAllUsers()
    elif order=="3":
        uptadeUser()
    elif order=="4":
        deleteUser()
    elif order=="5":
        break