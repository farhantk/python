data = ["meja","kursi","buku"]
print(data)

# Menambah list
data.append("kartu")
print(data)

# Meremove list
data.remove("kursi")
print(data)

# Menambah dibagian tertentu
data.insert(2,"meja")
print(data)

# Menghitung benda di list
jumlah = data.count("meja")
print("jumlah meja ada ",jumlah)
