#Mencetak Menu
def menu():
print "Menu Pilihan"
print
print "1. PersegiPanjang"
print "2. Lingkaran"
print "3. Segitiga"
print "4. Keluar"

defpersegi():
print "MenghitungLuasPersegiPanjang"
    p = input("MasukkanPanjang : ")
    l = input("MasukkanLebar   : ")
luas = p*l
print "LuasPersegiPanjangadalah ",luas
print
print "Mau cobalagi [Y/N]? "
back = raw_input().upper()
if back == "Y":
menu()
else:
exit()

deflingkaran():
print "MenghitungLuasLingkaran"
    r = input("MasukkanJari-Jari : ")
luas = 3.14*(r**2)
print "LuasLingkaranadalah ",luas
print
print "Mau cobalagi [Y/N]? "
back = raw_input().upper()
if back == "Y":
menu()
else:
exit()

defsegitiga():
print "MenghitungLuasSegitiga"
    a = input("Masukkan Alas     : ")
    t = input("MasukkanTinggi   : ")
luas = (a*t)/2
print "LuasSegitigaadalah ",luas
print
print "Mau cobalagi [Y/N]? "
back = raw_input().upper()
if back == "Y":
menu()
else:
exit()
#Program MenghitungLuas
print "SelamatDatang di Program UntukMenghitungLuas"
print "-----------------------------------------------"
print
menu()
while 1:
#input
pilih = input("Masukkanpilihan : ")

ifpilih == 1:
persegi()
elifpilih == 2:
lingkaran()
elifpilih == 3:
segitiga()
elifpilih == 4:
print "\n"*100
break
else:
print "Maafpilihan yang andamasukkantidakterdaftar"
print "Cobalagi [Y/N] ? "
coba = raw_input().upper()
ifcoba == "Y":
menu()
else:
print "\n"*1000
break
