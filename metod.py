def faktoriyel(sayı):
    faktoriyel = 1
    if (sayı == 0 or sayı == 1):
        print("Faktoriyel:",faktoriyel)
    else:
        while (sayı >= 2):
            faktoriyel *= sayı
            sayı -= 1

        print("Faktoriyel:",faktoriyel)

faktoriyel(3)
