angka = "9,223;372:036 854,775;807"
pemisah = "";
for char in angka:
    if not char.isnumeric():
        pemisah = pemisah + char
print(pemisah)

values = "".join(char if char not in pemisah else " " for char in angka).split()
print(sum([int(val) for val in values]))