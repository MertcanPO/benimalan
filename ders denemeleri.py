print("""***********************************
Kullanıcı Girişi Programı************************************* """)

sys_kullanıcı_adı = "Mertcan"
sys_parola = "12345"
giriş_hakkı = 3

while True:

    kullanıcı_adı = input("Kullanıcı adı:")
    parola = input("Parola:")

    if (sys_kullanıcı_adı != kullanıcı_adı and sys_parola == parola):
        print("Kullanıcı adı hatalı...")
        giriş_hakkı -= 1
    elif (sys_kullanıcı_adı == kullanıcı_adı and sys_parola != parola):
        print("Parola Hatalı...     ")
        giriş_hakkı -= 1
    elif (sys_kullanıcı_adı != kullanıcı_adı and sys_parola != parola):
        print("Kullanıcı adı ve parola hatalı...")
        giriş_hakkı -= 1
    else:
        print("Sisteme başarıyla giriş yapıldı!")
        break

    if giriş_hakkı == 0:
        print("Giriş hakkınız doldu erişiminiz engellendi!!!")
        break

