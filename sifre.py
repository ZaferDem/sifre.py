import random 

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre_uzunlugu = int(input("şifrenizin uzunluğu ne kadar olacak?"))

parola = ""

for i in range(sifre_uzunlugu):

    parola = parola+random.choice(karakterler)

    print("oluşturulan parola:" , parola)
