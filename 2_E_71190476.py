tubuh=float(input("Masukkan suhu tubuh Anda :"));
suhu=50
if tubuh > suhu:
    print("Anda bukan Manusia :)");
elif tubuh <= 32:
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat!");
elif tubuh <= 37.5:
    print("Suhu Anda normal!");
elif tubuh == 36:
    print("Suhu Anda normal!");
else:
    print("Anda demam! Jangan berpergian ke tempat fasilitas Umum.")
