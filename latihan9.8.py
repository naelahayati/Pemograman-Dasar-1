#menghitung garji bersih karyawan 
naela_gaji_pokok = float(input("masukan gaji pokok:"))
naela_tunjangan= naela_gaji_pokok* 0.20
naela_pajak= naela_gaji_pokok * 0.10

naela_gaji_bersih = naela_gaji_pokok + naela_tunjangan - naela_pajak

print("pajak:", naela_pajak)
print("tunjangan:", naela_tunjangan)
print("gaji bersih:",naela_gaji_bersih)