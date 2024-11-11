'''
Nama: Ilyassa Putra
NIM: 2402741
kELAS: 1c-rpl
praktikum 2
'''

def hitung_total(angka):
    total = sum(angka)
    rata_rata =total/len(angka)
    return total,rata_rata

input_angka = [2,3,5,10]
total, rata_rata = hitung_total(input_angka)

print(f"Total: {input_angka} = {total}")
print(f"Rata-rata: {total}/{len(input_angka)} = {rata_rata}")