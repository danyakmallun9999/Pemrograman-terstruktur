nama_mahasiswa =      input("Masukkan nama mahasiswa  : ")
nilai_mahasiswa = int(input("Masukkan nilai mahasiswa : "))

print(" ")

print("Cetak :")
print("Nama Mahasiswa : ",nama_mahasiswa)
if nilai_mahasiswa >= 85:
    print('Keterangan : A')
elif nilai_mahasiswa >= 75:
    print('Keterangan : B')
elif nilai_mahasiswa >= 60:
    print('Keterangan : C')
elif nilai_mahasiswa >= 50:
    print('Keterangan : D')
else :
    print('Keterangan : E')
