class yazilimci():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maaş = int(maaş)
        self.diller = diller

    def bilgileri_goster(self):
        print("""
        
        İsim: {}
        
        Soyisim: {}
        
        Numara: {}
        
        Maaş: {}
        
        Bildiği diller: {}
        
        
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))

    def zam_yap(self,zam_miktari):
        print("Zam yapılıyor...")

        self.maaş += zam_miktari

    def dil_ekleme(self,eklenen_dil):
        print("Dil ekleniyor...")
        self.diller.append(eklenen_dil)

    def numara_guncelleme(self,yeni_numara):
        print('Numara yenileniyor...')
        self.numara = yeni_numara

    def isim_değiştir(self,yeni_isim):
        print('İsim güncelleniyor...')
        self.isim = yeni_isim
    def dil_kaldırma(self,silinecek_dil):
        print('Diller güncelleniyor...')

        self.diller.pop(silinecek_dil)

yazilimci = yazilimci("Mertcan",'POYRAZ','5435','5000',['Java','C','Python'])


yazilimci.dil_ekleme('PHP')

yazilimci.bilgileri_goster()

yazilimci.numara_guncelleme('654345')

yazilimci.bilgileri_goster()

yazilimci.zam_yap(6000)

yazilimci.bilgileri_goster()

yazilimci.isim_değiştir('Tahsincan')

yazilimci.bilgileri_goster()

yazilimci.dil_kaldırma(1)

yazilimci.bilgileri_goster()




