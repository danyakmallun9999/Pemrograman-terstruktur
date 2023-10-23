# Membuat hasil nilai mahasiswa
# Jika nilai > 90 dapat A, Jika > 80 dapat B, Jika > 70 dapat c, Selain itu dapat D

nama_mahasiswa = input("Masukkan namamu : ")
nilai_mahasiswa = int(input("Masukkan nilai : "))

print(" ")
print(" ")

print("Nama :", nama_mahasiswa)

if nilai_mahasiswa >= 90 :
    print("Kamu mendapatkan Nilai A")
elif nilai_mahasiswa >= 80 :
    print("Kamu mendapatkan Nilai B")
elif nilai_mahasiswa >= 70 :
    print("Kamu mendapatkan nilai C")
else :
    print("Kamu mendapatkan Niali D")