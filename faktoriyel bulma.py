print("""*****************************************

Faktöriyel Bulma

Çıkmak için 'q' ya basınız.

*****************************************




""")


while True:
    sayı = input("Sayı:")
    if (sayı == "q"):
        print("Program sonlandırılıyor.")
        break

    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range(2,sayı+1):
            print("Faktöriyel:",faktoriyel,"i:",i)
            faktoriyel *= i
        print("Faktöriyel",faktoriyel)