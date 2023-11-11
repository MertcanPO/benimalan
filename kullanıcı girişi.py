print("""
****************************
Kullanıcı Girişi
*************************


""")

sys_kullanıcı_adı = "Mertcan"
sys_parola = "12345"

kullanıcı_adı = input("Kullanıcı Adı:")
parola = input("Parola:")





if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    print("Parola Hatalı...")
elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola == parola):
    print("Kullanıcı adı geçersiz...")
elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola != parola):
    print("Kullanıcı adı ve şifre yanlış!")

else:
    print("Sisteme başarıyla giriş yapıldı.")