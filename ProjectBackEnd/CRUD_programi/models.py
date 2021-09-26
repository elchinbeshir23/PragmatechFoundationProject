class User:
    def __init__(self,id,ad,soyad,email,tel):
            self.id=id
            self.ad=ad
            self.soyad=soyad
            self.email=email
            self.tel=tel
    def showUsersData(self):
        print(f"{self.ad} {self.soyad} {self.email} {self.tel}")
users=[]