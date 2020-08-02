age = int(input("Berapa Usiamu ? "))

# if age >= 16 and age <= 45:
#opsi 1
if 16 <= age <= 45:
    print("Kamu bisa bekerja disini")
else:
    print("Waktumu bebas untuk santuy")

print("-"*50)
# opsi 2
if age in range(16, 46):
    print("Kamu bisa bekerja disini")
else:
    print("Waktumu bebas untuk santuy")