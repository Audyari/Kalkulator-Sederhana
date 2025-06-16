import math

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

def akar(a):
    if a < 0:
        return "Error: Tidak bisa menghitung akar dari bilangan negatif"
    return math.sqrt(a)

def pangkat(a, b):
    return a ** b

def persen(a, b):
    return (a * b) / 100

def main():
    print("Kalkulator Sederhana")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Akar Kuadrat")
    print("6. Pangkat")
    print("7. Persentase")
    
    pilihan = input("Masukkan pilihan (1/2/3/4/5/6/7): ")
    
    if pilihan in ('1', '2', '3', '4', '6', '7'):
        try:
            num1 = float(input("Masukkan angka pertama: "))
            
            if pilihan == '5':
                print(f"Akar kuadrat dari {num1} = {akar(num1)}")
            else:
                num2 = float(input("Masukkan angka kedua: "))
                if pilihan == '1':
                    print(f"Hasil: {tambah(num1, num2)}")
                elif pilihan == '2':
                    print(f"Hasil: {kurang(num1, num2)}")
                elif pilihan == '3':
                    print(f"Hasil: {kali(num1, num2)}")
                elif pilihan == '4':
                    print(f"Hasil: {bagi(num1, num2)}")
                elif pilihan == '6':
                    print(f"{num1} pangkat {num2} = {pangkat(num1, num2)}")
                elif pilihan == '7':
                    print(f"{num1}% dari {num2} = {persen(num1, num2)}")
        except ValueError:
            print("Error: Masukan tidak valid")
    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
