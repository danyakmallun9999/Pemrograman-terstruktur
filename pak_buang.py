# Inisialisasi variabel total dengan nilai awal 0.
total = 0

# Inisialisasi variabel nilai dengan nilai awal 2.
nilai = 2

# Selama nilai kurang dari atau sama dengan 16384, lakukan langkah-langkah berikut:
while nilai <= 16384:
    # Tambahkan nilai ke total.
    total = total + nilai
    # Gantilah nilai dengan nilai baru yang didapatkan dengan mengalikannya dengan 2.
    nilai = nilai * 2

# Cetak nilai total sebagai hasil.
print(total)
