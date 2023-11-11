liste = ["1251", "1516", "sdfsd2115", "5sfa15", "sdaf", "12sf15", "12651"]

for i in liste:

    try:

        i = int(i)

        print(i)

    except ValueError:
        pass