#Program menghitung nilai tugas

print("*************************************************************************")
print("****************** Program Menghitung Nilai Tugas ***********************")
print("*************************************************************************")
print(" ")
print(" ")

nama_mahasiswa    = input("Masukkan Nama Mahasiswa    : ")
nim_mahasiswa     = input("Masukkan Nim Mahasiswa     : ")
mata_Kuliah       = input("Masukkan Mata Kuliah       : ")
nilai_tugas_satu  = input("Masukkan Nilai Tugas 1     : ")
nilai_tugas_dua   = input("Masukkan Nilai Tugas 2     : ")
nilai_tugas_tiga  = input("Masukkan Nilai Tugas 3     : ")

print(" ")
print(" ")
print("-------------------------------------------------------------------------")
print(" ")
print(" ")

# Kalkulasi nilai
# rumus = ( nilai1 + nilai2 + nilai3 ) / 3 lalu dibulatkan kebawah
total_nilai = (float(nilai_tugas_satu) + float(nilai_tugas_dua) + float(nilai_tugas_tiga)) / 3

print("Nilai Tugas")
print("Nama Mahasiswa               :", nama_mahasiswa)
print("Nama Nim Mahasiswa           :", nim_mahasiswa)
print("Mata Kuliah                  :", mata_Kuliah)
print("Total nilai adalah           :", total_nilai)
print("Nilai dibulatkan menjadi     :", round(total_nilai))

print(" ")
print(" ")
print("-------------------------------------------------------------------------")
print(" ")
print(" ")

print("******************** Tingkatkan Lagi Belajarnya *************************")
