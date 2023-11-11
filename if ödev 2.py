a = int(input("Birinci sayı:"))
b = int(input("İkinci sayı:"))
c = int(input("Üçüncü sayı:"))

if b < a and c < a :
    print("En büyük sayı: {}".format(a))
elif a < b and c < b:
    print("En büyük sayı: {}".format(b))
elif b < c and a < c:
    print("En büyük sayı: {}".format(c))