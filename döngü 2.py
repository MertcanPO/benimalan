sayı = input("Sayı:")
basamak_sayısı = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

geçici_sayı = sayı


while geçici_sayı > 0:

    basamak = geçici_sayı % 10
    toplam += basamak ** basamak_sayısı
    geçici_sayı //= 10

    if sayı == toplam:

        print(sayı,"Armstrong sayısı..")

    else:
        print(sayı,"Armstron sayısı değil...")

