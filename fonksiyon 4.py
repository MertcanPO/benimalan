birler = ['','bir','iki','üç','dört','beş','altı','yedi','sekiz','dokuz',]
onlar = ['','on','yirmi','otuz','kırk','elli','altmış','yetmiş','seksen','doksan']

def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10

    return onlar[ikinci] + "" +birler[birinci]

sayı = int(input("Sayı:"))

print(sayı,"------->",okunus(sayı))
