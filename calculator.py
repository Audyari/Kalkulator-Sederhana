import math
import os
import platform

def clear_screen():
    """Membersihkan layar terminal"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def tampilkan_menu():
    clear_screen()
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
            print("\nError: Masukan harus berupa angka. Silakan coba lagi.")
        except KeyboardInterrupt:
            print("\nOperasi dibatalkan.")
            raise

def tampilkan_hasil(operasi, hasil):
    print("\n" + "="*50)
    print(f"HASIL: {operasi} = {hasil}")
    print("="*50)

def tanya_lanjut():
    while True:
        jawaban = input("\nApakah Anda ingin melakukan perhitungan lagi? (y/n): ").lower()
        if jawaban in ('y', 'n'):
            return jawaban == 'y'
        print("Masukan tidak valid. Silakan jawab 'y' untuk Ya atau 'n' untuk Tidak.")

# Fungsi-fungsi operasi matematika
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        raise ValueError("Tidak bisa membagi dengan nol")
    return a / b

def akar(a):
    if a < 0:
        raise ValueError("Tidak bisa menghitung akar dari bilangan negatif")
    return math.sqrt(a)

def pangkat(a, b):
    return a ** b

def persen(a, b):
    return (a * b) / 100

def main():
    clear_screen()
    print("Selamat datang di Kalkulator Sederhana!")
    input("Tekan Enter untuk melanjutkan...")
    
    while True:
        try:
            tampilkan_menu()
            pilihan = input("\nMasukkan pilihan (1-8): ")
            
            if pilihan == '8':
                print("\nTerima kasih telah menggunakan kalkulator ini!")
                break
                
            if pilihan not in ('1', '2', '3', '4', '5', '6', '7'):
                print("\nError: Pilihan tidak valid. Silakan pilih 1-8.")
                input("\nTekan Enter untuk melanjutkan...")
                continue
                
            try:
                if pilihan == '5':  # Akar kuadrat
                    num = dapatkan_angka("\nMasukkan angka: ")
                    hasil = akar(num)
                    tampilkan_hasil(f"√{num}", hasil)
                else:
                    num1 = dapatkan_angka("\nMasukkan angka pertama: ")
                    num2 = dapatkan_angka("Masukkan angka kedua: ")
                    
                    if pilihan == '1':
                        hasil = tambah(num1, num2)
                        tampilkan_hasil(f"{num1} + {num2}", hasil)
                    elif pilihan == '2':
                        hasil = kurang(num1, num2)
                        tampilkan_hasil(f"{num1} - {num2}", hasil)
                    elif pilihan == '3':
                        hasil = kali(num1, num2)
                        tampilkan_hasil(f"{num1} × {num2}", hasil)
                    elif pilihan == '4':
                        hasil = bagi(num1, num2)
                        tampilkan_hasil(f"{num1} ÷ {num2}", hasil)
                    elif pilihan == '6':
                        hasil = pangkat(num1, num2)
                        tampilkan_hasil(f"{num1} ^ {num2}", hasil)
                    elif pilihan == '7':
                        hasil = persen(num1, num2)
                        tampilkan_hasil(f"{num1}% dari {num2}", hasil)
                
                if not tanya_lanjut():
                    print("\nTerima kasih telah menggunakan kalkulator ini!")
                    break
                    
            except ValueError as e:
                print(f"\nError: {str(e)}")
                input("\nTekan Enter untuk melanjutkan...")
                
        except KeyboardInterrupt:
            print("\n\nOperasi dibatalkan oleh pengguna.")
            break
        except Exception as e:
            print(f"\nTerjadi kesalahan tak terduga: {str(e)}")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
