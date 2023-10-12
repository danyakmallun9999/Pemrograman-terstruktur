print (" ")

print ("**************************************************************")
print ("********** Program Menghitung Nilai Akhir Semester ***********")
print ("**************************************************************")

print (" ")
print (" ")

nama            = input (" masukan Nama Mahasiswa                 : ")
nim             = input (" masukan NIM Mahasiswa                  : ")
matakuliah      = input (" masukan Mata Kuliah                    : ")
uts             = input (" masukan Nilai UTS                      : ")
uas             = input (" masukan Nilai UAS                      : ")
tugas           = input (" masukan Nilai Tugas                    : ")
keaktifan       = input (" masukan Nilai Keaktifan                : ")
kehadiran       = input (" masukan Nilai Kehadiran                : ")
adalah          = 0.25 * float(uts) + 0.25 * float(uas) + 0.15 * float(tugas) + 0.15 * float(keaktifan) + 0.20 * float(kehadiran)


print (" ")

print ("Nilai Akhir Semester")
print ("nama mahasiswa                          : ",nama)
print ("nim mahasiswa                           : ",nim)
print ("mata kuliah                             : ",matakuliah)
print ("adalah                                  : ",float(adalah))
print ("Nilai Dibulatkan menjadi                : ",round(adalah))


