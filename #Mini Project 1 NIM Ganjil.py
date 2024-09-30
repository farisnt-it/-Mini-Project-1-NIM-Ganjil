# Mini Project 1 NIM Ganjil

# Login 
print("Selamat datang! Silakan login terlebih dahulu.")
A = input("Masukkan nama Anda:")
B = input("Masukkan NIM Anda:")

Nama = "Abdurrahman Al Farisy"
NIM  = "2409116055"

if Nama == A and NIM == B:
    print("Login Berhasil")
    while True:
        print("Ingin Menghitung Gaji?")
        pilihan = str(input("iya atau tidak:"))

        if pilihan == "iya":
            # Menghitung Gaji
            jam_kerja = float(input("Masukan Jam Kerja:"))
            tarif_kerja = float(input("Masukan Tarif Kerja:"))
            # Mengtotalkan hasil Gaji
            if jam_kerja > 160:
                gaji = jam_kerja * tarif_kerja
                bonus = gaji * 0.1
                total_gaji = gaji + bonus
                print("selamat anda mendapatkan bonus")
                print("gaji anda adalah:")
                print(total_gaji)
            else:
                gaji = jam_kerja * tarif_kerja
                print("maaf anda tidak mendapat bonus")
                print("gaji anda adalah:")
                print(gaji)
        elif pilihan == "tidak":
            print("Program selesai")
            break
        else:
            print("pilihan tidak valid")

else:
    print("Login Gagal")
