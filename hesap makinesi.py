import math
print("""***************************


Hesap makinesine hoş geldiniz.

Çıkış yapmak için 'q' ya basınız.

***********************

""")
def toplama(x,y):
    return x + y
def çıkarma(x,y):
    return x - y
def çarpma(x,y):
    return x * y
def bölme(x,y):
    if y == 0:
        return 'Bölen sıfır olamaz.'
    return x / y
def karekök():
    return math.sqrt()
def üs_alma(x,y):
    return math.pow(x,y)
def logaritma():
    return math.log()
def trigonometri(rad,sin,cos,tan):
    return trigonometri(rad) == math.pi / 4
    return trigonometri(sin) == math.sin(trigonometri(rad))
    return trigonometri(cos) == math.cos(trigonometri(rad))
    return trigonometri(tan) == math.tan(trigonometri(rad))
def mutlak_deger(x):
    return math.fabs(x)
def pi_sayısı():
    return math.pi
def euler_sayısı():
    return math.e

while True:

    işlem = input('İşleminiz:')


    if işlem == 'q':
        print('Hesap makinesi kapatılıyor...')
        break
    elif işlem not in logaritma(x) or karekök():
        sayı1 = float(input('Birinci Sayı:'))
        sayı2 = float(input('İkinci Sayı:'))

    elif işlem == toplama(x,y):
        print('Sonuç:',toplama(x,y))

    elif işlem == çıkarma(x,y):
        print('Sonuç:',çıkarma(x,y))

    elif işlem == çarpma(x,y):
        print('Sonuç:',çarpma(x,y))

    elif işlem == bölme(x,y):
        print('Sonuç:',bölme(x,y))

    elif işlem == karekök(x):
        print('Sonuç:',bölme(x,y))

    elif işlem == üs_alma(x,y):
        print('Sonuç:',üs_alma(x,y))

    elif işlem == logaritma(x):
        print('Sonuç:',logaritma(x))

    elif işlem == trigonometri(rad,sin,cos,tan):
        print('Sinüs:',trigonometri(sin))
        print('Cosinüs:',trigonometri(cos))
        print('Tanjant:',trigonometri(tan))

    elif işlem == mutlak_deger(x):
        print('Sonuç:',mutlak_deger(x))

    elif işlem == pi_sayısı():
        print('Pi değeri:',pi_sayısı())

    else:
        işlem == euler_sayısı()
        print('Euler sayı:',euler_sayısı())





