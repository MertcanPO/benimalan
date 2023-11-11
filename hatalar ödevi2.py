def cift_mi(integer):
    if sayı % 2 == 0:
        return integer
    else:
        raise ValueError
liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

for i in liste:
    try:
        print(çift_mi(i))
    except ValueError:
        pass