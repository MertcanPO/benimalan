print("""*****************************

Hoş geldiniz!!

Çıkış yapmak için lütfen 'q' ya basınız.



""")

toplam = 0

while True:

    sayı = input("Sayı:")



    if sayı == "q":
        break


    sayı = int(sayı)



    toplam += sayı

print("Girdiğiniz sayılar toplamı:",toplam)

