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
            print("Input harus berupa angka. Silakan coba lagi.")


def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        return "Error: tidak bisa membagi dengan nol."
    return first_number / second_number


def calculate(choice, first_number, second_number):
    if choice == "1":
        return add(first_number, second_number)
    if choice == "2":
        return subtract(first_number, second_number)
    if choice == "3":
        return multiply(first_number, second_number)
    if choice == "4":
        return divide(first_number, second_number)
    return "Pilihan operasi tidak valid."


def main():
    while True:
        show_menu()
        choice = input("Pilih operasi: ")

        if choice == "0":
            print("Program selesai.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Pilihan tidak tersedia.")
            continue

        first_number = get_number("Masukkan angka pertama: ")
        second_number = get_number("Masukkan angka kedua: ")

        result = calculate(choice, first_number, second_number)
        print("Hasil:", result)


if __name__ == "__main__":
    main()