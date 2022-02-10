
import function

# list of dictionary
daftar_kontak = []
daftar_kontak.append({
    "nama" : "Eko",
    "email" : "priana.yhc@gmail.com",
    "telepon" : "089554444"
})

#menu program

while True:
    print("#. Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar")

    menu = input("Pilih menu: ")

    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":        
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)

print("program selesai berjalan, sampai jumpa")