class çalışan():
    def __init__(self, isim, soyisim, maaş, departman, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.maaş = int(maaş)
        self.departman = departman
        self.diller = list(diller)

    def çalışan_bilgileri(self):
        print('Bilgiler tanımlandı....')
        print("""İsim: {}\nSoyisim: {}\nMaaş: {}\nDepartman: {}\nDiller: {}""".format(self.isim, self.soyisim, self.maaş, self.departman, self.diller))

    def zam_yap(self, zam_miktarı):
        print('Bilgiler güncelleniyor...')
        self.maaş += zam_miktarı

    def dil_ekle(self, eklenen):
        print('Bilgiler güncelleniyor...')
        self.diller.append(eklenen)

    def departman_değiştir(self, yeni_dep):
        print('Yeni atama yapılıyor...')
        self.departman = yeni_dep



class yönetici(çalışan):
    def __init__(self, isim, soyisim, maaş, departman, diller, sorumlu_kişi):
        super().__init__(isim, soyisim, maaş, departman, diller)
        self.sorumlu_kişi = sorumlu_kişi

    def çalışan_bilgileri(self):
        print('Bilgiler tanımlandı....')
        print("""İsim: {}\nSoyisim: {}\nMaaş: {}\nDepartman: {}\nDiller: {}\nSorumlu kişi: {}""".format(self.isim, self.soyisim, self.maaş, self.departman, self.diller, self.sorumlu_kişi))

çalışan = çalışan('Mertcan','POYRAZ',4000,'Yazılımcı',['Python','C','Java'])

yönetici1 = yönetici('Tahsincan', 'POYRAZ', 8000, 'Müdür yardımcısı', ['Türkçe', 'İngilizce'], 'Mertcan')

çalışan.çalışan_bilgileri()

yönetici1.çalışan_bilgileri()
