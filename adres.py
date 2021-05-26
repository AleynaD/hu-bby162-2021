#Aleyna Demirkıran
# 21865586

f=open("adres.txt","w")
anahtar=1
while anahtar==1:
  isim=input("İsminizi Giriniz : ")
  soyisim=input("Soyisminizi Giriniz : ")
  mail=input("Mail adresinizi Giriniz : ")
  f.write(isim+" "+soyisim+" "+mail+" \n")
  print(isim,soyisim,mail)
  kosul=input("Veri Girişine devam etmek için bir tuşa basın (E/H) : ")
  if kosul=="E" or kosul=="e":
    anahtar=1
  elif kosul=="H" or kosul=="h":
    anahtar=0
  else:
    print("Yanlış Değer Girdiniz...\nProgram kapatıldı.\n")
    anahtar=0
f.close()
f=open("adres.txt")
print(f.read())