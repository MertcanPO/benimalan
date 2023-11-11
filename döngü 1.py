print("""****************************

Mükemmel sayı bulmaya hoş geldiniz.

Çıkış yapmak için 'q' ya basınız.




""")

while True:
    sayı = (input("Sayı:"))

    if sayı == 'q':
        print("Çıkış yapılıyor...")
        break

    sayı = int(sayı)

    bölenler = []

    toplam = 0

    for i in range(1,sayı):

        if sayı % i == 0:
            bölenler.append(i)

            toplam += i



    if toplam == sayı:
        print("Bu bir mükemmel sayıdır.")

    else:
        print("Mükemmel sayı değil.")






