daftar_belanja = ["susu", "beras", "gula", "kecap", "indomi", "roti"]
item_dicari ="indomi"
tidak_ada = None

#for index di dalam range(6) banyak daftar belanja
# for index in range(len(daftar_belanja)):
#     if daftar_belanja[index] == item_dicari:
#         tidak_ada = index
#         break

# simpel pencarian dengan if kondisinya ada in
if item_dicari in daftar_belanja:
    tidak_ada = daftar_belanja.index(item_dicari)

if tidak_ada is not None:
    print("Item yang anda cari ditemukan pada posisi index ke-{} ".format(tidak_ada))
else:
    print("{} tidak ditemukan".format(item_dicari))