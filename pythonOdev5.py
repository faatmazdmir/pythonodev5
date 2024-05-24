"""
Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik,Fizik,Kimya notları tutulur.
Kullanıcıdan isim ve ders ismi(Matematik,Fizik,Kimya) istenir ve bu bilgilere göre çıktı verilir.

Sözlük üzerinde değerleri değiştirme,yeni değer ekleme,kullanıcıya ulaşmak istediği bilgileri sorma gibi uygulamalar yapın.
"""
ogrenci_not = {
 'Ali': {"Matematik": 85, "Fizik": 60, "Kimya": 70},
 'Melis':{"Matematik": 50, "Fizik": 90,"Kimya":84},
 'Yağmur':{"Matematik": 92, "Fizik": 85,"Kimya":80},
 'Sinan':{"Matematik": 45, "Fizik":48, "Kimya": 56}
}

def not_goruntule(isim,ders):
    try:
        not_degeri = ogrenci_not[isim][ders]
        print(f"{isim} adlı öğrencinin {ders} notu: {not_degeri}")
    except KeyError:
        print("Girilen isim ya da ders bulunamadı!")

def not_degistirme(isim,ders,yeni_not):
    try:
        ogrenci_not[isim][ders] = yeni_not
        print(f"{isim} adlı öğrencinin {ders} notu {yeni_not} olarak değiştirildi. ")
    except KeyError:
        print("Girilen isim ya da ders bulunamadı!")

def ogrenci_ekle(isim,notlar):
    if isim in ogrenci_not:
        print(f"{isim} adlı öğrenci sistemde mevcuttur.")
    else:
        ogrenci_not[isim] = notlar
        print(f"{isim} adlı öğrenci sisteme eklendi.")

while True:
    print("\n1.Not Görüntüleme")
    print("2.Not Değiştirme")
    print("3.Öğrenci Ekleme")
    print("4.Çıkış")
    secim = input("Yapmak istediğiniz işlemi seçiniz (1/2/3/4): ")

    if secim == "1":
        isim = input("Öğrencinin ismi: ")
        ders = input("Ders ismi giriniz (Matematik,Fizik,Kimya): ")
        not_goruntule(isim,ders)
    elif secim == "2":
        isim = input("Öğrencinin ismi: ")
        ders = input("Ders ismi giriniz (Matematik,Fizik,Kimya): ")
        yeni_not = int(input(f"Yeni {ders} notu: "))
        not_degistirme(isim,ders,yeni_not)
    elif secim == "3":
        isim = input("Yeni öğrencinin ismi: ")
        matematik = int(input("Matematik notu: "))
        fizik = int(input("Fizik notu: "))
        kimya = int(input("Kimya notu: "))
        notlar = {"Matematik": matematik, "Fizik": fizik, "Kimya": kimya}
        ogrenci_ekle(isim,notlar)
    elif secim == "4":
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyiniz! ")