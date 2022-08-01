#Belajar tipe data Dictionary

customer = {
    "name" : "Eko",
    "age": 30,
    "address": "Subang"
}

name = customer["name"]
print(name)

#Ubah data
customer["name"] = "Andi"

#hapus data
del customer['address']



for key, value in customer.items():  
    print(f"{key}: {value}")