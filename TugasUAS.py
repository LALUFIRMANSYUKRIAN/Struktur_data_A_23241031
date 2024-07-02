def main():
    print("Selamat datang di program Percabangan dan Perulangan")

    # Contoh Percabangan
    Nama = input("Masukkan Angka: ")
    angka = int(Nama)

    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap.")
    else:
        print(f"{angka} adalah bilangan ganjil.")


    # Contoh Perulangan
    print("\nPerulangan menggunakan list:")
    bil = [0, 1, 2, 3, 4, 5]
    print(bil)

    for i in bil:
        print(f"Nilai i sekarang -> {i}")
    print("Program Telah Selesai.")


    print("\nPerulangan menggunakan range:")
    bil = range(0, 6)

    for i in bil:
        print(i)
    print("Program Telah Selesai.")

if __name__ == "__main__":
    main()