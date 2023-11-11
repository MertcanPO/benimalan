def pisagor_ucgeni():

    pisagor_listesi = list()

    for i in range(1,101):
        for j in range(1,101):

            a = (i ** 2 + j ** 2) ** 0.5

            if a == int(a):
                pisagor_listesi.append((i,j,int(a)))

    return pisagor_listesi

for i in pisagor_ucgeni():
    print(i)