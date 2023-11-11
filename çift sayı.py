def çift_mi(sayı):

    if sayı % 2 == 0:
        return sayı

    else:
        raise ValueError

liste = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for i in liste:

    try:
        print(çift_mi(i))

    except ValueError:
        pass

