print("******************************************************")
print("------ Program Perulangan While dengan Inputan -------")
print("******************************************************")

kalimat_di_cetak  =     input("Masukkan Kalimat yang ingin dicetak : ")
berapa_kali_cetak = int(input("Masukkan berapa kali pencetakan     : "))

nilai = 0
while (nilai < berapa_kali_cetak):
    print(kalimat_di_cetak)
    nilai += 1