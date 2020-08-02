nama = input("Masukkan namamu: ")
umur = int(input("Berapa usiamu ? "))

if 18 <= umur < 31:
    print("Selamat berpesta di cafe ini, {0}".format(nama))
else:
    print("Maaf usiamu tidak mencukupi untuk berpesta")