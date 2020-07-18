# Local
nama = "farhan"
def gantinama(namabaru):
    nama = namabaru
    print("nama baru saya ",nama)
gantinama("tirta")
print(nama)

print(30*"-")
# Global
nama1 = "farhan"
def gantinama1(namabaru1):
    global nama1
    nama1 = namabaru1
    print("nama1 baru saya", namabaru1)
gantinama1("tirta")
print(nama1)
