print("""****************************************


Atm'mize hoş geldiniz.

işlemler;

1.Bakiye sorgulama

2.Nakit yatırma 


3.Nakit çekme




Programdan çıkmak için L ye basın.



""")


bakiye = 1000

while True:
    işlem = input("İşlem seçiniz:")

    if (işlem == "q"):
        print("Yine bekleriz.")
        break

    elif (işlem == "1"):
        print("Bakiyeniz {} tl'dir.".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Miktar giriniz:"))

        bakiye += miktar
        print("Bakiyeniz {} tl olmuştur.".format(bakiye))

    elif (işlem == "3"):
        miktar = int(input("Miktarı giriniz:"))
        bakiye -= miktar
        print("Bakiyenizin güncel durumu {} tl'dir.".format(bakiye))

        if bakiye - miktar < 0 :
            print("Hesabınızda yeterli bakiye bulunmamaktadır.")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz işlem....")


