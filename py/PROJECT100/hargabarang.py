print('='*40)
print('               HARGA BARANG               ')
print('='*40)

harga_barang = int(input('Masukan harga barang :'))
diskon = 12.5/100

if int(harga_barang) >= 100000:
    hitung = harga_barang*diskon
    print(hitung)
elif int(harga_barang) >= 50:
    print('Barang tidak dijual10')
elif int(harga_barang) <= 10:
    print('Barang harus di restock')


else:
    print('Barang tidak mendapatkan diskon')