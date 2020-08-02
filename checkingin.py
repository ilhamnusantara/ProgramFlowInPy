#in and not in
#in
# kalimat = "Norwegia Blue"
# angka_dalam_kalimat = input("Masukkan sebuah karakter: ")
#
# if angka_dalam_kalimat in kalimat:
#     print("karakter {} terdapat pada kalimat {}".format(angka_dalam_kalimat, kalimat))
# else:
#     print("Aku tidak menemukan dalam surat")

#not in
aktifitas = input("Aktifitas apa yang kamu suka hari ini ? ")
# casefold() digunakan untuk membaca besar atau kecil kalimat
if "cinema" not in aktifitas.casefold():
    print("tetapi aku tetap pergi melihat cinema")
else:
    print("Beli daging 20 ton buat nonton")