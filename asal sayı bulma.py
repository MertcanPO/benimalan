def asal_mi(sayı):
    if sayı == 1:
        return False

    elif (sayı == 2):
        return True

    else:
        for i in range(2,sayı):
            if sayı % i == 0:
                return False
        return True


while True:

    sayı = input("Sayı:")

    if sayı == 'q':
        print("Çıkış yapılıyor.")
        break

    else:
        sayı = int(sayı)

        if asal_mi(sayı):
            print(sayı,"bir asal sayıdır..")
        else:
            print(sayı,"bir asal sayı değil..")
