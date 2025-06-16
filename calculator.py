def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol"
    return a / b

def main():
    print("Kalkulator Sederhana")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    
    if pilihan in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
            
            if pilihan == '1':
                print(f"Hasil: {tambah(num1, num2)}")
            elif pilihan == '2':
                print(f"Hasil: {kurang(num1, num2)}")
            elif pilihan == '3':
                print(f"Hasil: {kali(num1, num2)}")
            elif pilihan == '4':
                print(f"Hasil: {bagi(num1, num2)}")
        except ValueError:
            print("Error: Masukan tidak valid")
    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
