# 1. Buatlah program sederhana dengan tema bebas menggunakan rumus Elif (not/and/or)
# Program sederhana menggunakan if, elif, dan operator logika
# program Nilai Menggunakan AND

print('=====================================================================')
print('==================== Program Pemberian Nilai ========================')
print('=====================================================================')
print('')

nama_mahasiswa = 'Dany Akmallun Niam'
nilai = 100

# Mengevaluasi nilai menggunakan if, elif, dan operator logika
if nilai >= 90 and nilai <= 100:
    print("Nilai", nama_mahasiswa, ": A")
elif nilai >= 80 and nilai < 90:
    print("Nilai", nama_mahasiswa, ": B")
elif nilai >= 70 and nilai < 80:
    print("Nilai", nama_mahasiswa, ": C")
elif nilai >= 60 and nilai < 70:
    print("Nilai", nama_mahasiswa, ": D")
elif nilai < 60 and nilai >= 1:
    print("Nilai", nama_mahasiswa, ": E")
else:
    print(nama_mahasiswa, "Tidak niat kuliah")
