def giris():
    kullanici_adi = input("Kullanici adinizi girin: ")
    sifre = input("Şifrenizi girin: ")

    with open("kullanici_bilgileri.txt", "r") as dosya:
        for satir in dosya:
            bilgiler = satir.strip().split(",")
            dosya_kullanici_adi = bilgiler[0]
            dosya_sifre = bilgiler[1]

            if kullanici_adi == dosya_kullanici_adi and sifre == dosya_sifre:
                print("Giriş yapildi.")
                return

    print("Kullanici adi veya şifre hatali.")
