import random
terbesar = 10

jawaban = random.randint(1, terbesar)
print(jawaban)
tebakan = 0
print("Tolong tebak angka dari 1 sampai {} : ".format(terbesar))
while tebakan != jawaban:
    tebakan = int(input())

    if tebakan < jawaban:
        print("tebakan masih kurang")
    elif tebakan > jawaban:
        print("tebakan kebanyakan")
    else:
        print("sudah tepat")