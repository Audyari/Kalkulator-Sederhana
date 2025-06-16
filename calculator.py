"""
Kalkulator Sederhana

Program kalkulator dengan fitur:
- Operasi dasar (+, -, *, /)
- Akar kuadrat
- Pangkat
- Persentase
- Riwayat perhitungan

Author: [Nama Anda]
Version: 1.0.0
"""

import math
import os
import platform
from datetime import datetime
from typing import List, Dict, Optional, Union, Tuple

# Inisialisasi variabel global untuk riwayat perhitungan
riwayat: List[Dict[str, Union[str, float]]] = []

# Konstanta untuk batasan input
MIN_NUMBER = -1e100
MAX_NUMBER = 1e100
MAX_DECIMALS = 10
MAX_HISTORY = 10
MAX_ATTEMPTS = 3

def clear_screen() -> None:
    """Membersihkan layar terminal sesuai sistem operasi."""
    os.system('cls' if platform.system() == "Windows" else 'clear')

def validasi_angka(angka_str: str) -> Optional[float]:
    """
    Memvalidasi input angka dan mengembalikan float jika valid.
    
    Args:
        angka_str: String input dari pengguna
        
    Returns:
        float: Angka yang sudah divalidasi
        None: Jika input tidak valid
    """
    try:
        angka = float(angka_str)
        
        if not MIN_NUMBER <= angka <= MAX_NUMBER:
            print(f"\nError: Angka harus berada di antara {MIN_NUMBER} dan {MAX_NUMBER}")
            return None
            
        if '.' in angka_str:
            bagian_desimal = angka_str.split('.')[1]
            if len(bagian_desimal) > MAX_DECIMALS:
                angka = round(angka, MAX_DECIMALS)
                print(f"\nPeringatan: Nilai dibulatkan menjadi {angka}")
        
        return angka
        
    except ValueError:
        print("\nError: Masukan harus berupa angka")
        return None

def dapatkan_angka(pesan: str) -> Optional[float]:
    """
    Meminta input angka dengan validasi dan batas percobaan.
    
    Args:
        pesan: Pesan yang ditampilkan ke pengguna
        
    Returns:
        float: Angka yang valid
        None: Jika melebihi batas percobaan
    """
    for attempt in range(MAX_ATTEMPTS):
        try:
            input_str = input(pesan).strip()
            
            if not input_str:
                print("\nError: Input tidak boleh kosong")
                continue
                
            if angka := validasi_angka(input_str):
                return angka
                
        except KeyboardInterrupt:
            print("\n\nOperasi dibatalkan oleh pengguna.")
            raise
            
        sisa_attempts = MAX_ATTEMPTS - (attempt + 1)
        if sisa_attempts > 0:
            print(f"\nSisa percobaan: {sisa_attempts}")
    
    print("\nBatas maksimum percobaan tercapai. Kembali ke menu utama...")
    return None

def format_angka(angka: float) -> str:
    """Format angka agar mudah dibaca."""
    return f"{angka:,.10f}".rstrip('0').rstrip('.')

def tampilkan_menu() -> None:
    """Menampilkan menu kalkulator."""
    clear_screen()
    print("\n" + "="*50)
    print("KALKULATOR SEDERHANA".center(50))
    print("="*50)
    print("\nPilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (×)")
    print("4. Pembagian (÷)")
    print("5. Akar Kuadrat (√)")
    print("6. Pangkat (^)")
    print("7. Persentase (%)")
    print("8. Lihat Riwayat")
    print("9. Keluar")

def tambah(a: float, b: float) -> float:
    """Menjumlahkan dua angka."""
    return a + b

def kurang(a: float, b: float) -> float:
    """Mengurangi a dengan b."""
    return a - b

def kali(a: float, b: float) -> float:
    """Mengalikan dua angka."""
    return a * b

def bagi(a: float, b: float) -> float:
    """
    Membagi a dengan b.
    
    Raises:
        ValueError: Jika b adalah nol
    """
    if b == 0:
        raise ValueError("Tidak bisa membagi dengan nol")
    return a / b

def akar(a: float) -> float:
    """
    Menghitung akar kuadrat dari a.
    
    Raises:
        ValueError: Jika a adalah negatif
    """
    if a < 0:
        raise ValueError("Tidak bisa menghitung akar dari bilangan negatif")
    return math.sqrt(a)

def pangkat(a: float, b: float) -> float:
    """Menghitung pangkat a dengan b."""
    return a ** b

def persen(a: float, b: float) -> float:
    """Menghitung persentase a dari b."""
    return (a * b) / 100

def tampilkan_riwayat() -> None:
    """Menampilkan riwayat perhitungan."""
    clear_screen()
    print("\n" + "="*50)
    print("RIWAYAT PERHITUNGAN".center(50))
    print("="*50)
    
    if not riwayat:
        print("\nBelum ada riwayat perhitungan.")
    else:
        for i, hitung in enumerate(riwayat, 1):
            print(f"\n{i}. {hitung['waktu']} - {hitung['operasi']} = {hitung['hasil']}")
    
    input("\nTekan Enter untuk kembali ke menu utama...")

def tampilkan_hasil(operasi: str, hasil: float) -> None:
    """Menampilkan hasil perhitungan."""
    print("\n" + "="*50)
    print(f"HASIL: {operasi} = {hasil}")
    print("="*50)

def tambah_ke_riwayat(operasi: str, hasil: float) -> None:
    """Menambahkan perhitungan ke dalam riwayat."""
    riwayat.append({
        'waktu': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'operasi': operasi,
        'hasil': hasil
    })
    # Batasi riwayat hanya 10 entri terakhir
    if len(riwayat) > MAX_HISTORY:
        riwayat.pop(0)

def tanya_lanjut() -> bool:
    """Menanyakan apakah ingin melanjutkan."""
    while True:
        jawaban = input("\nApakah Anda ingin melakukan perhitungan lagi? (y/n): ").lower()
        if jawaban in ('y', 'n'):
            return jawaban == 'y'
        print("Masukan tidak valid. Silakan jawab 'y' untuk Ya atau 'n' untuk Tidak.")

def main() -> None:
    """Fungsi utama untuk menjalankan kalkulator."""
    clear_screen()
    print("Selamat datang di Kalkulator Sederhana!")
    input("Tekan Enter untuk melanjutkan...")
    
    while True:
        try:
            tampilkan_menu()
            pilihan = input("\nMasukkan pilihan (1-9): ").strip()
            
            if pilihan == '9':
                print("\nTerima kasih telah menggunakan kalkulator ini!")
                break
                
            if pilihan == '8':
                tampilkan_riwayat()
                continue
                
            if pilihan not in ('1', '2', '3', '4', '5', '6', '7'):
                print("\nError: Pilihan tidak valid. Silakan pilih 1-9.")
                input("\nTekan Enter untuk melanjutkan...")
                continue
                
            try:
                if pilihan == '5':
                    if (num := dapatkan_angka("\nMasukkan angka: ")) is None:
                        input("\nTekan Enter untuk melanjutkan...")
                        continue
                        
                    hasil = akar(num)
                    operasi = f"√{num}"
                    tampilkan_hasil(operasi, hasil)
                    tambah_ke_riwayat(operasi, hasil)
                else:
                    if (num1 := dapatkan_angka("\nMasukkan angka pertama: ")) is None or \
                       (num2 := dapatkan_angka("Masukkan angka kedua: ")) is None:
                        input("\nTekan Enter untuk melanjutkan...")
                        continue
                    
                    # Mapping pilihan ke fungsi yang sesuai
                    operations = {
                        '1': (tambah, f"{num1} + {num2}"),
                        '2': (kurang, f"{num1} - {num2}"),
                        '3': (kali, f"{num1} × {num2}"),
                        '4': (bagi, f"{num1} ÷ {num2}"),
                        '6': (pangkat, f"{num1} ^ {num2}"),
                        '7': (persen, f"{num1}% dari {num2}")
                    }
                    
                    func, operasi = operations[pilihan]
                    hasil = func(num1, num2) if pilihan != '7' else func(num1, num2)
                    
                    tampilkan_hasil(operasi, hasil)
                    tambah_ke_riwayat(operasi, hasil)
                
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
