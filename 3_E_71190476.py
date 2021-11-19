if __name__ == '__main__':
    nama1 = input ("masukkan daftar siswa :").title().split(",")
    nama1 = list(x.strip() for x in nama1)
    print(" Daftar Siswa:", nama1)
    namaBaru = input("masukkan siswa yang ingin di tambahkan :").title()

    if namaBaru in nama1 :
        print ("Siswa atas nama {} sudah berada dalam dsaftar siswa". format (namaBaru.upper()))
    else :
        nama1.append(namaBaru.upper())
        print("Hasil penambahan pada daftar siswa:",nama1)
