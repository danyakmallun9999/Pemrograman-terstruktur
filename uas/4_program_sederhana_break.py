# Soal : Buatlah program sederhana dengan tema bebas menggunakan rumus break
# Membuat kalkulator sederhana

print("=====================================================")
print("=============== Kalkulator sederhana ================")
print("=====================================================")
print("")

while True:
    angka1 = float(input("Masukkan angka pertama : "))
    angka2 = float(input("Masukkan angka kedua   : "))

    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    operasi = input("Masukkan nomor operasi (1/2/3/4) atau 'q' untuk keluar: ")

    if operasi == 'q':
        print("Terima kasih telah menggunakan kalkulator sederhana.")
        break

    if operasi not in ['1', '2', '3', '4']:
        print("Error: Pilihan operasi tidak valid.")
        break

    if operasi == "1":
        hasil = angka1 + angka2
    elif operasi == "2":
        hasil = angka1 - angka2
    elif operasi == "3":
        hasil = angka1 * angka2
    elif operasi == "4":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            print("Error: Pembagian dengan nol tidak diizinkan.")
            break

    print("Hasil :", hasil)
