import random
import time

print("""****************************

Sayı tahmini oyunumuza hoş geldiniz...


1 ile 40 arasındaki sayıyı tahmin ediniz...


İyi eğlenceler.


*****************************


""")



rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7

while True:
    tahmin = int(input('Tahmininiz:'))

    if tahmin_hakkı == 0:
        print('Bilgiler kontrol ediliyor...')
        time.sleep(1)
        print('Tahmin hakkınız bitti..','Sayımız:',rastgele_sayı)
        break

    elif tahmin < rastgele_sayı:
        print('Bilgiler kontrol ediliyor....')
        time.sleep(1)


        print('Daha büyük bir sayı tahmin ediniz..')

        tahmin_hakkı -= 1

    elif tahmin > rastgele_sayı:

        print('Bilgiler kontrol ediliyor....')
        time.sleep(1)

        print('Daha düşük bir sayı tahmin ediniz...')

        tahmin_hakkı -= 1

    else:
        print('Bilgiler kontrol ediliyor...')
        time.sleep(1)

        print('Tebrikler sayımızı bildiniz!','Sayımız:',rastgele_sayı)
        break

















