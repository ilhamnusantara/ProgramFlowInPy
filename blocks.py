name = input("Masukkan nama anda : ")
age = int(input("Berapa Umur mu, {0}? ".format(name)))
print(age)

if age < 18 :
    print("Tolong datang dalam kembali {0} tahun mendatang".format(18 - age))
elif age >= 100:
    print("Mungkin anda terlalu tua bro")
else:
    print("Kamu bisa melakukan voting")
    print("silahkan ambil beras 100 ton")
# for i in range(1, 13):
#     print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i **3))
# print("*" * 80)
