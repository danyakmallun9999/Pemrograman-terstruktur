# print("Jika anda yakin untuk melanjutkan program ini, tekan y untuk melanjutkan")
# print(" ")
# n = input("Yakin (y/t) ? :")
# print(" ")
# if n == "y":
#     print("Baiklah, tunggu sebentar, program akan segera dilanjutkan")
#     print("Siapkan perlengkapanya")
#     print("...")
# elif n == "t":
#     print("Maaf anda tidak dapat melanjutkan program ini")
# elif n == "z":
#     print("Maaf system komputer anda tidak mendukung program ini")
# else:
#     print("Pi;ihanya y, t, atau z")


print(" ")

print("****************************************************")
print("**** Contoh program IF menggunakan operator NOT ****")
print("****************************************************")

print(" ")
print(" ")

n = input("Masukkan huruf/angka/symbol = ")
if not n:
    print("Kok huruf yang anda masukkan kosong?")
else:
    print("Anda Memasukkan huruf/angka/symbol = " + n)