a = float(input("Boyunuzu giriniz:"))
b = float(input("Kilonuzu giriniz:"))

endeks = b / (a * a)

print("Beden kitle endeksiniz: {}\n".format(endeks))

if endeks <= 18.5:
    print("Zayıf")
elif endeks <= 25:
    print("Normal")
elif endeks <= 30:
    print("Fazla kilolu")
else:
    print("Obez")