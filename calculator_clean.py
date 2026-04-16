def show_menu():
    print("\n=== KALKULATOR SEDERHANA ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("0. Keluar")


def get_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Input harus berupa angka.")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: tidak bisa dibagi nol"
    return a / b


def main():
    while True:
        show_menu()
        pilihan = input("Pilih operasi: ")

        if pilihan == "0":
            break

        if pilihan not in ["1", "2", "3", "4"]:
            print("Pilihan tidak valid")
            continue

        a = get_number("Masukkan angka pertama: ")
        b = get_number("Masukkan angka kedua: ")

        if pilihan == "1":
            hasil = add(a, b)
        elif pilihan == "2":
            hasil = subtract(a, b)
        elif pilihan == "3":
            hasil = multiply(a, b)
        elif pilihan == "4":
            hasil = divide(a, b)

        print("Hasil:", hasil)


if __name__ == "__main__":
    main()