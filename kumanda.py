import time
import random

class Kumanda():
    def __init__(self, tv_durum="kapalı", tv_ses=10, tv_kanal="Trt", kanal_listesi=["", "Trt"]):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.tv_kanal = tv_kanal
        self.kanal_listesi = kanal_listesi

    def tv_aç(self):
        if self.tv_durum == "kapalı":
            self.tv_durum = "açık"
        else:
            print("Televizyon zaten açık....")

    def tv_kapat(self):
        if self.tv_durum == "açık":
            self.tv_durum = "kapalı"
        else:
            print("Televizyon zaten kapalı....")

    def ses_ayarları(self):
        while True:
            print(">,<,e")
            cevap = input("işleminiz:")
            if cevap == "<":
                if self.tv_ses > 0:
                    self.tv_ses -= 1
                    print("Ses:", self.tv_ses)
            elif cevap == ">":
                if self.tv_ses < 30:
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)
            else:
                if cevap == "e":
                    print("Çıkış yapılıyor...")
                    break

    def kanal_ekleme(self, kanal_ismi):
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal ekleniyor....")
        time.sleep(1)
        print("Kanal başarıyla eklendi...")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi) - 1)
        self.tv_kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal:", self.tv_kanal)

    def kanal_seçme(self, seçilen_kanal):
        kanal = input("+,-,sayı")
        if kanal == "+":
            index = self.kanal_listesi.index(self.tv_kanal)
            if index == len(self.kanal_listesi) - 1:
                self.tv_kanal = self.kanal_listesi[0]
            else:
                self.tv_kanal = self.kanal_listesi[index + 1]
        elif kanal == "-":
            index = self.kanal_listesi.index(self.tv_kanal)
            if index == 0:
                self.tv_kanal = self.kanal_listesi[-1]
            else:
                self.tv_kanal = self.kanal_listesi[index - 1]
        else:
            try:
                kanal_index = int(kanal)
                if 0 <= kanal_index < len(self.kanal_listesi):
                    self.tv_kanal = self.kanal_listesi[kanal_index]
                else:
                    print("Geçersiz kanal girişi....")
            except ValueError:
                print("Geçersiz giriş işlemi.. Lütfen bir sayı giriniz....")

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv durum: {}\nTv ses: {}\nŞu anki kanal: {}".format(self.tv_durum, self.tv_ses, self.tv_kanal)


# Sınıfı kullanarak kumanda nesnesini oluşturuyoruz
kumanda = Kumanda()

print("""
TV'ye hoş geldiniz.
Yapmak istediğiniz işlemi seçiniz...
1. Tv açma
2. Tv kapatma
3. Ses ayarları
4. Kanal ekleme
5. Rastgele kanal
6. Kanal seçimi
7. Televizyon bilgilerini göster
""")

while True:
    işlem = input("İşleminizi giriniz:")
    if işlem == "1":
        kumanda.tv_aç()
    elif işlem == "2":
        kumanda.tv_kapat()
    elif işlem == "3":
        kumanda.ses_ayarları()
    elif işlem == "4":
        kanal_listesi = input("Kanal isimlerini aralarına ',' koyarak giriniz:")
        kanal_listesi = kanal_listesi.split(",")
        for eklenecek_kanal in kanal_listesi:
            kumanda.kanal_ekleme(eklenecek_kanal)
    elif işlem == "5":
        kumanda.rastgele_kanal()
    elif işlem == "6":
        secilen_kanal = input("Kanal seçiniz:")
        kumanda.kanal_seçme(secilen_kanal)
    elif işlem == "7":
        print(kumanda)
    else:
        print("Geçersiz işlem....")
