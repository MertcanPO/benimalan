#lambda return tanımının tek satırda yazılmış halidir.


# bu iki ifade de aynı anlama gelmektedir.

def toplama(x,y,z):
    return x + y + z
print(toplama(10,11,12))


toplama = lambda x , y , z : x + y + z

print(toplama(3,4,5))

#lambda ifadeleri büyük fonksiyonlarda kullanılmaz
