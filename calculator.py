import math

def tampilkan_menu():
    print("\n" + "="*50)
    print("KALKULATOR SEDERHANA".center(50))
    print("="*50)
    print("\nPILIH OPERASI:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Akar Kuadrat (√)")
    print("6. Pangkat (^)")
    print("7. Persentase (%)")
    print("8. Keluar")

def dapatkan_angka(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Error: Masukan harus berupa angka. Silakan coba lagi.")

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
    while True:
        tampilkan_menu()
        
        try:
            pilihan = input("\nMasukkan pilihan (1-8): ")
            
            if pilihan == '8':
                print("\nTerima kasih telah menggunakan kalkulator ini!")
                break
                
            if pilihan not in ('1', '2', '3', '4', '5', '6', '7'):
                print("\nError: Pilihan tidak valid. Silakan pilih 1-8.")
                continue
                
            if pilihan == '5':  # Akar kuadrat
                num = dapatkan_angka("\nMasukkan angka: ")
                hasil = akar(num)
                print(f"\n√{num} = {hasil}")
            else:
                num1 = dapatkan_angka("\nMasukkan angka pertama: ")
                num2 = dapatkan_angka("Masukkan angka kedua: ")
                
                if pilihan == '1':
                    hasil = tambah(num1, num2)
                    print(f"\n{num1} + {num2} = {hasil}")
                elif pilihan == '2':
                    hasil = kurang(num1, num2)
                    print(f"\n{num1} - {num2} = {hasil}")
                elif pilihan == '3':
                    hasil = kali(num1, num2)
                    print(f"\n{num1} × {num2} = {hasil}")
                elif pilihan == '4':
                    hasil = bagi(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {hasil}")
                elif pilihan == '6':
                    hasil = pangkat(num1, num2)
                    print(f"\n{num1} ^ {num2} = {hasil}")
                elif pilihan == '7':
                    hasil = persen(num1, num2)
                    print(f"\n{num1}% dari {num2} = {hasil}")
            
            # Tunggu user menekan enter sebelum melanjutkan
            input("\nTekan Enter untuk melanjutkan...")
            
        except KeyboardInterrupt:
            print("\n\nOperasi dibatalkan oleh pengguna.")
            break
        except Exception as e:
            print(f"\nTerjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    main()
