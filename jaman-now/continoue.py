# contonue berfungsi untuk skip proses tertentu dalam looping

#contoh berikut hanya ngeprint yang angka ganjil saja
for i in range(1,100):
    if i % 2 == 0:
        continue    
    print(i)