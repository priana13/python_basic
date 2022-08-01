
# function biasa
# def jumlahkan(satu,dua):
#     total = satu * dua
#     print(f"Total {satu} x {dua} = {total}")

# jumlahkan(40,7)

# ====================
#untuk membuat artgument list cukup menambahkan bintang di depan parameter
#jika ingin menggunakan lebih dari 1 parameter, argument list diletakan paling belakang
#argument list hanya bisa satu saja

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total ({list_angka}) = {total}")

jumlahkan(40,7,90)