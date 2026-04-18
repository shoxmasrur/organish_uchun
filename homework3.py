
"""1.bosqich"""
class MenuItem:
    def __init__(self, nomi:str, turi:str, ichimlik=20, shirinlik=10):
        self.nomi=nomi
        self.turi=turi
        self.ichimlik=ichimlik
        self.shirinlik=shirinlik

    def serve(self, miqdor:int):
        print("buyurmangiz tayyorlanmoqda")

        if miqdor>20:
            print(f"bu bir oz vaqt oladi chunki bizda bunday miqdor mavjud emas edi")
            self.restock()

        if self.turi=="ichimlik":
            self.ichimlik-=miqdor
        else :
            self.shirinlik-=miqdor

        print("buyurtmangiz tayyor")

        if miqdor<=0:
            self.restock(self)
            print("buyurtmanbiz tayyor")
        
        
    def restock(self):
        self.ichimlik=20
        self.shirinlik=10

a=input("ichimlik/shirinlik: ")
if a=="ichimlik":
    b=input("choy/kofe/sok: " )
else :
    b=input("tort/keks/pirojni: ")


class Customer:
    def __init__(self, name,  Item:MenuItem, balance=100):
        pass


client1=MenuItem(b,a)
client1.serve(int(input("miqdorni kiriting: ")))

"""Bahrom aka bularni shunchaki o'rganish uchun yozyapman bilasiz GIt dan 
foydalanishga qiynalyotgan edim shunga bularni yozyapman"""








  
  
