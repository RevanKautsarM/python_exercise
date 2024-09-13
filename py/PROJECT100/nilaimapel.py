ipas = int(input('Masukan nilai IPAS : '))
bahasa_indo = int(input('Masukan nilai B.Indonesia : '))
bahasa_inggris = int(input('Masukan nilai B.Inggris : '))
matematika = int(input('Masukan nilai Matematika : '))
total_nilai = ipas + bahasa_indo + bahasa_inggris + matematika

if total_nilai >= 200:
    print('Kamu Lulus')

else:
    print('Kamu Tidak Lulus')