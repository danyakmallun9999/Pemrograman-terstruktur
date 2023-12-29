# Soal :  Buatlah program sederhana dengan tema bebas menggunakan rumus gabungan (Elif/For/While/Break)
# Program sederhana penghitung luas
# Menggunakan while, if dan elif, break

print("============================================================================")
print("========================= Aplikasi Penghitung Luas =========================")
print("============================================================================")
print("================ 1. untuk menghitung luas persegi panjang  =================")
print("=================   2. untuk menghitung luas Segitiga    ===================")
print("=================== 3. untuk menghitung luas Lingkaran =====================")
print("================= 4. untuk keluar dari program sederhana ===================")
print("============================================================================")
print("========================= Aplikasi Penghitung Luas =========================")
print("============================================================================")
print(" ")
print(" ")

while True:
    nilai_pilihan = int(input('Masukkan Pilihan Program 1/2/3/4: '))
    print(" ")

    if nilai_pilihan == 4:
        break

    elif nilai_pilihan == 1:
        print("==== Anda Memilih Program menghitung luas persegi panjang ====")
        print(" ")
        panjang = int(input("Masukkan Panjang = "))
        lebar   = int(input("Masukkan Panjang = "))
        hasil   = panjang * lebar
        print(" ")
        print("Luas Persegi Panjang Adalah = ", hasil)
       

    elif nilai_pilihan == 2:
        print("======== Anda Memilih Program menghitung luas Segitiga =======")
        print(" ")
        setengah = 0.5
        alas     = int(input("Masukkan Alas   = "))
        tinggi   = int(input("Masukkan Tinggi = "))
        hasil    = setengah * alas * tinggi
        print(" ")
        print("Luas Segitiga Adalah = ", hasil)
       

    elif nilai_pilihan == 3:
        print("======= Anda Memilih Program menghitung luas lingkaran =======")
        print(" ")
        pi    = 3.14
        r     = int(input("Masukkan Jari-jari   = "))
        hasil = pi * r ** 2
        print(" ")
        print("Luas Lingkara Adalah = ", hasil)

    else :
        print("================ Anda Salah Memilih Program ==================")
      

print(" ")
print("====================== Terima Kasih ==========================")
print(" ")
