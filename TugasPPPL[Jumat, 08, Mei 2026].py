data=[]

angka=input("Masukkan list (dipisah spasi) :")
data=angka.split()
K=int(input("Masukan K :"))


k = K % len(data)
hasil = data[-k:] + data[:-k]
print(f"Hasil Rotasi:{hasil}")