şekil = input("Hangi şeklin tipini öğrenmek istiyorsunuz:")

if şekil == "dörtgen":
    print("Kenarları sırayla giriniz.")
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    d = int(input("Kenar-4:"))

    if a == b and a == c and a == d:
        print("Kare...")
    elif (a == c and b == d) or (a == b and c == d):
        print("Dikdörtgen...")
    else:
        print("Dörtgen...")

elif şekil == "üçgen":
    print("Kenarları sırasıyla giriniz.")
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))

    if (abs(a + b > c) and abs(a + c > b) and abs(b + c > a)):
        if a == b == c:
            print("Eşkenar üçgen...")
        elif a == b or a == c or b == c:
            print("Bu bir ikizkenar üçgen...")
        else:
            print("Bu bir çeşitkenar üçgen...")
    else:
        print("Üçgen belirtmiyor...")
else:
    print("Geçersiz şekil girişi...")
