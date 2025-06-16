#!/bin/bash

# Script untuk build kalkulator menjadi executable di Linux/Mac

echo "Memulai proses build..."
echo "======================="

# Install dependensi
echo "Menginstall dependensi..."
pip install -r requirements.txt

# Buat direktori build jika belum ada
mkdir -p build

# Hapus build sebelumnya untuk memastikan build yang bersih
if [ "$(ls -A build/)" ]; then
    echo "Membersihkan build sebelumnya..."
    rm -rf build/*
fi

# Build dengan PyInstaller
echo "Membuat executable dengan PyInstaller..."
pyinstaller --onefile --console --clean --distpath=build --workpath=build/temp --specpath=build calculator.py

# Periksa apakah build berhasil
if [ -f "build/calculator" ]; then
    echo ""
    echo "======================="
    echo "Build BERHASIL!"
    echo "File executable ada di: $(pwd)/build/calculator"
    echo "======================="
    
    # Jalankan kalkulator
    echo ""
    echo "Menjalankan kalkulator..."
    echo "======================="
    ./build/calculator
else
    echo ""
    echo "======================="
    echo "Build GAGAL!"
    echo "Periksa pesan error di atas."
    echo "======================="
    exit 1
fi

echo ""
read -p "Tekan Enter untuk melanjutkan..."
