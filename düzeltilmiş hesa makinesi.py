import math

print("""***************************

Hesap makinesine hoş geldiniz.

Çıkış yapmak için 'q' ya basınız.

***********************

""")

def toplama(x, y):
    return x + y

def çıkarma(x, y):
    return x - y

def çarpma(x, y):
    return x * y

def bölme(x, y):
    if y == 0:
        return 'Bölen sıfır olamaz.'
    return x / y

def karekök(x):
    return math.sqrt(x)

def üs_alma(x, y):
    return math.pow(x, y)

def logaritma(x):
    return math.log(x)

def trigonometri(rad):
    sinüs = math.sin(rad)
    cosinüs = math.cos(rad)
    tanjant = math.tan(rad)
    return sinüs, cosinüs, tanjant

def mutlak_deger(x):
    return math.fabs(x)

def pi_sayısı():
    return math.pi

def euler_sayısı():
    return math.e

while True:
    işlem = input('İşleminiz: ')

    if işlem == 'q':
        print('Hesap makinesi kapatılıyor...')
        break

    if işlem not in ('9', '10'):  # Karekök ve logaritma için ayrı işlem kodları
        sayı1 = float(input('Birinci Sayı: '))
        sayı2 = float(input('İkinci Sayı: '))

    if işlem == '1':
        print('Sonuç:', toplama(sayı1, sayı2))
    elif işlem == '2':
        print('Sonuç:', çıkarma(sayı1, sayı2))
    elif işlem == '3':
        print('Sonuç:', çarpma(sayı1, sayı2))
    elif işlem == '4':
        print('Sonuç:', bölme(sayı1, sayı2))
    elif işlem == '5':
        print('Sonuç:', karekök(sayı1))
    elif işlem == '6':
        print('Sonuç:', üs_alma(sayı1, sayı2))
    elif işlem == '7':
        print('Sonuç:', logaritma(sayı1))
    elif işlem == '8':
        radian = math.radians(sayı1)  # Dereceyi radyana dönüştürüyoruz
        sinüs, cosinüs, tanjant = trigonometri(radian)
        print('Sinüs:', sinüs)
        print('Cosinüs:', cosinüs)
        print('Tanjant:', tanjant)
    elif işlem == '9':
        print('Sonuç:', mutlak_deger(sayı1))
    elif işlem == '10':
        print('Pi değeri:', pi_sayısı())
    else:
        print('Euler sayı:', euler_sayısı())
