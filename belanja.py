daftar_belanja = ["susu", "beras", "gula", "kecap", "indomi", "roti"]
# opsi 1
# for item in daftar_belanja:
#     if item != "kecap":
#         print("Beli "+ item)

# opsi 2 menggunakan continue
for item in daftar_belanja:
    if item == "kecap":
        continue
    print("Beli "+ item)