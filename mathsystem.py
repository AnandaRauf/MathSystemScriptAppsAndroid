print (' ////****** 13 Mei 2018 PT.MrvDevelopment™ ********\\\ ')
print (' Aplikasi Math System Version 1.0 ')
print (" Pilih Pelajaran Matematika Yang Anda Butuhkan" )
def menu():
                print "Menu Pilihan:"
                print
                print "1.","anutias"
                print "2.","barisanaritmetika"
                print "3.","deretaritmetika"
                print "4.","sisipanbarisanaritmetika"
                
menu()
pilih = input("Masukkan Pilihan Menu Anda : ")
if pilih == 1:
                anutias= "anutias(M, P, A, jumlah_suku_bunga, jumlah_pinjaman, hasil_b1, jumlah_besar_anutias, a1)";
elif pilih == 2:
                barisanaritmetika()
elif pilih == 3:
                deretaritmetika();
elif pilih == 4:
                sisipanbarisanaritmetika();
else:
     print "Maaf Pilihan Anda Tidak Ada"
     exit()
class anutias("M, P, A, jumlah_suku_bunga, jumlah_pinjaman, hasil_b1, jumlah_besar_anutias, a1"):
    M = int(input("Masukkan Pinjaman Uang:"))
    P = int(input("Masukkan Suku Bunga:"))
    A = int(input("Masukan Besar Anutias:"))
print "rumus_bunga_ke_atau_b = P * M"
jumlah_suku_bunga= P
jumlah_pinjaman= M
print "rumus_b_atau_Bunga_Ke_= p * m"
hasil_b1= P * M
jumlah_besar_anutias= str('A')
print "Rumus_a1= A - b1"
a1= A - hasil_b1
print "Jadi Angsuran Pertama Adalah:", a1
anutias();

       
    

