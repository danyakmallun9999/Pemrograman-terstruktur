print("============================================================================")
print("========================= Aplikasi Penghitung Luas =========================")
print("============================================================================")
print("================ 1. untuk menghitung luas persegi panjang  =================")
print("=================   2. untuk menghitung luas Segitiga    ===================")
print("=================== 3. untuk menghitung luas Lingkaran =====================")
print("============================================================================")
print("========================= Aplikasi Penghitung Luas =========================")
print("============================================================================")
print(" ")
print(" ")
nilai_pilihan = int(input('Masukkan Pilihan Program : '))
print(" ")

if nilai_pilihan == 1:
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
    alas  = int(input("Masukkan Jari-jari   = "))
    hasil = pi * alas ** 2
    print(" ")
    print("Luas Lingkara Adalah = ", hasil)

else :
    print("================ Anda Salah Memilih Program ==================")

print(" ")
print("====================== Terima Kasih ==========================")