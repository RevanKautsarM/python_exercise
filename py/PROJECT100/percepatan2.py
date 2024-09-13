print('\033[1m========================================')
print('          PERCEPATAN RATA RATA          ')
print('----------------------------------------')

v2 = float(input('Kecepatan Awal(v2) : ')) 
v1 = float(input('Kecepatan Akhir (v1) : '))
t2 = float(input('Waktu Awal (t2) : ')) 
t1 = float(input('Waktu Akhir (t1) : ')) 

v = v2 - v1
t = t2 - t1
a = v / t

print('\033[95mHasil : \033[1m', a ,'m/s')