print ("pilihan menu :")
nilai1= print("1.pangkat 2 (kuadrat)")
nilai2= print("2.pangkat 3 (kubik)")
nilai3= print("3.akar kuadrat")


menu = int(input("Masukkan menu yang ingin anda pilih : "))
if menu == 1 :
    angka = int(input("Masukkan bilangan yang ingin dipangkatkan :"))
    hasil = angka ** 2
    print("Hasil dari pemangkatan bilangan" ,angka ,"dengan 2 (kuadrat)  adalah" ,hasil)
elif menu == 2 :
    angka = int(input("Masukkan bilangan yang ingin dipangkatkan :"))
    hasil = angka ** 3
    print ("Hasil dari pemangkatan bilangan " ,angka ,"dengan 3 (kubik) adalah" ,hasil)
elif menu == 3 :
    angka = int(input("Masukkan bilangan yang ingin dipangkatkan :"))
    hasil = angka ** (1.0/2)
    print ("Hasil dari akar kuadrat dari bilangan" ,angka ,"adalah" ,hasil)
                
else:
    print ("pilihan menu yang tidak dimasukkan tidak sesuai!")
