siswa = input ('Masukan nilai siswa :')

if int(siswa) >= 90:
    print ('Siswa Dinyatan Lulus')
elif int(siswa) >= 80:
    print('Nilai A')
elif int(siswa) >= 70:
    print ('Nilai B')
elif int(siswa) >= 60:
    print ('Nilai C')
elif int(siswa) >= 50:
    print ('Nilai D')
else:
    print ('Siswa Dinyatakan Tidak Lulus')