#sewa angkutan 
naela_jarak = float(input("masukan jarak tempuh:"))

if naela_jarak == 1:
   naela_harga = 4500
else:
    naela_harga = 4500+ (naela_jarak-1)*2000
    
print("harga sewa angkutan: Rp.", naela_harga)