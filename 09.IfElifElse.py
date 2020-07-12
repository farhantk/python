nilai = int(input("Masukan nilai kamu : "))
print("Nilai kamu adalah ",nilai)
print(50*"=")

if 90 < nilai <= 100:
    print("Nilai kamu adalah A")
elif 80 < nilai <= 90:
    print("Nilai kamu adalah B")
elif 70 < nilai <= 80:
    print("Nilai kamu adalah C")
elif 60 <= nilai <= 70:
    print("Nilai kamu adalah D")
else:
    print("Kamu tidak lulus, tolong lakukan perbaikan")

print(50*"=")

makanan = ["nasi goreng", "indomie", "gorengan", "goyobod"]
beli = input("Apa yang mau kamu pesan : ")
if beli in makanan:
    print('"saya pesan', beli, '2 porsi"')
else:
    print("Pedangan tidak menjual ", beli)
