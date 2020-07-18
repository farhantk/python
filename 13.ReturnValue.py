def fungsi(x):
    hasil = x**2
    print(x,"** 2 = ",hasil)
    return hasil

def kali(y,z):
    hasil = y*z
    print(y ,"x", z, "= ", hasil)
    return hasil

a = fungsi(6)
b = kali(5,a)
print(b)
