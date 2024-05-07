Jumlah_barang = int(input("Masukkan jumlah barang: "))

Harga_Total = 0

for i in range(Jumlah_barang):
    price = float(input(f"Masukkan harga barang ke-{i + 1}: "))
    Harga_Total += price

print("Total harga belanjaan:", Harga_Total)
