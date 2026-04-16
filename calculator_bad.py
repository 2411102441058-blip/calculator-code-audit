def x():
    print("KALKULATOR")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    a = input("Masukkan angka pertama: ")
    b = input("Masukkan angka kedua: ")
    c = input("Masukkan operasi: ")

    if c == "1":
        print("Hasil:", float(a) + float(b))
    elif c == "2":
        print("Hasil:", float(a) - float(b))
    elif c == "3":
        print("Hasil:", float(a) * float(b))
    elif c == "4":
        if float(b) == 0:
            print("Tidak bisa dibagi 0")
        else:
            print("Hasil:", float(a) / float(b))
    else:
        print("Salah")

x()