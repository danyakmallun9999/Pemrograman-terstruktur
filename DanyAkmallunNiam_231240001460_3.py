#Program kasir toko

print("                       Tahunan Jepara / 0235                     ")
print("                      PT. Pencari Cinta Sejatie                  ")
print("                    Jl. Raya Mayong Jepara KM.23                 ")
print("                             Jepara                              ")
print("                    NPWP : 01.233.876.8.1098.098                 ")
print("24-10-23 | 21.20                                   401460/DANY/01")
print(" ")

nama_barang_1      = input("Masukkan Nama Barang 1               : ")
jumlah_pembelian_1 = input("Masukkan Jumlah Pembelian Barang 1   : ")
harga_barang_1     = input("Masukkan Harga Barang 1              : ")
nama_barang_2      = input("Masukkan Nama Barang 2               : ")
jumlah_pembelian_2 = input("Masukkan Jumlah Pembelian Barang 2   : ")
harga_barang_2     = input("Masukkan Harga Barang 2              : ")
nama_barang_3      = input("Masukkan Nama Barang 3               : ")
jumlah_pembelian_3 = input("Masukkan Jumlah Pembelian Barang 3   : ")
harga_barang_3     = input("Masukkan Harga Barang 3              : ")
uang_bayar         = input("Masukkan Pembayaran                  : ")

print(" ")
print("-----------------------------------------------------------------")
print(" ")

jumlah_harga_1 = (int(jumlah_pembelian_1) * int(harga_barang_1))
jumlah_harga_2 = (int(jumlah_pembelian_2) * int(harga_barang_2))
jumlah_harga_3 = (int(jumlah_pembelian_3) * int(harga_barang_3))

print(nama_barang_1, jumlah_pembelian_1, harga_barang_1, jumlah_harga_1)
print(nama_barang_2, jumlah_pembelian_2, harga_barang_2, jumlah_harga_2)
print(nama_barang_3, jumlah_pembelian_3, harga_barang_3, jumlah_harga_3)
print(" ")

print("-----------------------------------------------------------------")
print(" ")

harga_jual = jumlah_harga_1 + jumlah_harga_2 + jumlah_harga_3

print("Harga jual   :           ", harga_jual)
print(" ")
print("-----------------------------------------------------------------")
print(" ")

uang_bayar = int(uang_bayar)

print("Total        :           ", harga_jual)
print("Bayar        :           ", uang_bayar)
print("Kembalian    :           ", uang_bayar - harga_jual)

print(" ")
print("********** Terimakasih sudah belanja di DANYMART ***********")
print(" ")
