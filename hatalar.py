try:
    a = int(input("sayı1:"))
    b = int(input("sayı2:"))
    print(a/b)

except ValueError:
    print("Lütfen doğru bir input seçiniz.")

except ZeroDivisionError:

    print("Sıfıra bölüm hatası...")

print("Bloklar sonlandırılıyor...")