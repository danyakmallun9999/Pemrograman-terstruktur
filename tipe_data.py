# Tipe data
# Ada 6 tipe data di python
# 1). Integer (int)
# 2). Float(float)
# 3). String(str)
# 4). Boolean(bool)
# 5). Complex(complex)
# 6). Ctypes(diambil dari bahasa C)

# Tipe data integer ( int )
integer = 20
print('Nilai = ', integer, 'Tipe datanya = ', type(integer))

# Tipe data float = angka dengan koma
tipe_data_float = 20.1
print('Nilai = ', tipe_data_float, 'Tipe datanya = ', type(tipe_data_float))

# Tipe data string = Kumpulan sebuah karakter
tipe_data_string = "Sella"
print('Nilai = ', tipe_data_string, 'Tipe datanya = ', type(tipe_data_string))

# Tipe data bool = true / false
tipe_data_boolean = True
print('Nilai = ', tipe_data_boolean, 'Tipe datanya = ', type(tipe_data_boolean))

# Bilangan kompleks atau khsusus
# biasa digunakan sama anak matematika

# bilangan kompleks
tipe_data_kompleks = complex(5,6)
print('Nilai = ', tipe_data_kompleks, 'Tipe datanya = ', type(tipe_data_kompleks))

# tipe data dari bahasa c
from ctypes import c_double, c_bool

data_c_double = c_double(10.8)
print('Nilai = ', data_c_double, 'Tipe datanya = ', type(data_c_double))