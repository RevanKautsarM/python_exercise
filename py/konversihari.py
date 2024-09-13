TAHUN_HARI = 365
BULAN_HARI = 30
hari = int(input('Hari: '))
tahun = int(hari / TAHUN_HARI)
hari = hari % TAHUN_HARI
bulan = int(hari/BULAN_HARI)
hari = hari % BULAN_HARI

print(tahun, 'Tahun: ', bulan , 'Bulan: ', hari , 'Hari: ')