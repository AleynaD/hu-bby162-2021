def menu():
    menu = """
  Kataloğa Hoşgeldiniz...
  İşlem Seçiniz:

  [1] Kayıt Listele
  [2] Yeni Eser Kaydet
  [3] Kayıt Silme
  [4] Kayıt Güncelleme
  [5] Dosya Verilerini Silme
  [X] uygulamayı kapat
  """
    print(menu)


def eserKaydet(eserAdi, yazarAdi, yayinEvi, basimTarihi, isbnNo):
    f = open("final.txt", "a")
    f.write(eserAdi + ", " + yazarAdi + ", " + yayinEvi + ", " + basimTarihi + ", " + isbnNo + "\n")
    f.close()
    print("Ekleme başarıyla gerçekleşti..")


def eserListele():
    f = open("final.txt", "r")
    print(f.read())
    f.close()


def txtİciniTemizle():
    f = open("final.txt", "w")
    f.close()


def cikis():
    tercih = input("Çıkış yapmak istediğinize emin misiniz: (E/H)? ")
    if (tercih == "E" or tercih == "e"):
        exit()


def eserSil():
    silinecekEser = input("Lutfen Silmek İstediğiniz Eseri Giriniz:")
    oku = open("final.txt")
    icerik = oku.readlines()
    k = open("final.txt", "w")
    for x in icerik:
        bolunenDeger = x.split(",")
        if bolunenDeger[0] != silinecekEser:
            k.write(x)
    print("Eser Başarıyla Silindi..")


def eserGüncelle():
    güncellenecekEser = input("Lutfen Güncellemek İstediğiniz Eseri Giriniz:")
    oku = open("final.txt")
    icerik = oku.readlines()

    k = open("final.txt", "w")
    for x in icerik:
        bolunenDeger = x.split(",")
        if bolunenDeger[0] != güncellenecekEser:
            k.write(x)
    eserAdi = input("Yeni Eser Adını giriniz : ")
    yazarAdi = input("Yeni Yazar Adını giriniz :")
    yayinEvi = input("Yeni Yayınevini giriniz :")
    basimTarihi = input("Yeni Basım Tarihini giriniz :")
    isbnNo = input("Yeni ISBN numarasını giriniz : ")

    k.write(eserAdi + ", " + yazarAdi + ", " + yayinEvi + ", " + basimTarihi + ", " + isbnNo + "\n")
    print("Eser Başarıyla Güncellendi..")


def eserBilgileriAlim():
    eserAdi = input("Eser Adını giriniz : ")
    if eserAdi == "":
        print("Boş Veri Girişi Yaptınız...")
        return ""
    yazarAdi = input("Yazar Adını giriniz : ")
    if yazarAdi == "":
        print("Boş Veri Girişi Yaptınız...")
        return ""
    yayinEvi = input("Yayınevini giriniz : ")
    if yayinEvi == "":
        print("Boş Veri Girişi Yaptınız...")
        return ""
    basimTarihi = input("Basım Tarihini giriniz : ")
    if basimTarihi == "":
        print("Boş Veri Girişi Yaptınız...")
        return ""
    isbnNo = input("ISBN numarasını giriniz : ")
    if isbnNo == "":
        print("Boş Veri Girişi Yaptınız...")
        return ""
    eserKaydet(eserAdi, yazarAdi, yayinEvi, basimTarihi, isbnNo)


while True:
    menu()
    secim = input("Yapmak istediğiniz işlemi seçiniz : ")
    if secim == "1":
        eserListele()

    if secim == "2":
        eserBilgileriAlim()

    if secim == "3":
        eserSil()

    if secim == "4":
        eserGüncelle()
    if secim == "5":
        txtİciniTemizle()
    if secim == "X":
        cikis()

    kullaniciSoru = input("Ana Menüye Dönmek İçin 'Evet' yada 'Hayır' Yazınız : ")
    if kullaniciSoru == "Evet" or kullaniciSoru=="evet":
        continue
    if kullaniciSoru == "Hayır" or kullaniciSoru=="hayır":
        cikis()