mata_angin = ["utara", "selatan", "timur", "barat"]
pilihan = ""
while pilihan not in mata_angin:
    pilihan = input("masukan pilihan mata angin lagi : ")
    if pilihan.casefold() == "quit":
        print("Anda Gagal")
        break
print("mata angin ada sudah ditemukan")