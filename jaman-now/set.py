# tipe data set digunakan untuk menyimpan data uniqu, jadi klo ada yang sama akan dihapus
# set tidak bisa diakses menggunakan index jadi hanya bisa di loop

pelanggan = {"Priana","Andi","Agus","Priana"}

# print(pelanggan)

# set juga bisa ditambah isi dengan perintah .add klo list ([]) menggunakan append

pelanggan.add("Saputra")

for i in pelanggan:
    print(i)

# kita juga bisa menghapus data

pelanggan.remove("Priana")

for i in pelanggan:
    print(i)

