@echo off
REM Script untuk build kalkulator menjadi executable

echo Memulai proses build...
echo =======================

REM Install dependensi
echo Menginstall dependensi...
pip install -r requirements.txt

REM Buat direktori build jika belum ada
if not exist "build" mkdir build

REM Hapus build sebelumnya untuk memastikan build yang bersih
if exist "build\*" (
    echo Membersihkan build sebelumnya...
    rmdir /s /q build
    mkdir build
)

REM Build dengan PyInstaller
echo Membuat executable dengan PyInstaller...
pyinstaller --onefile --console --clean --distpath=build --workpath=build\temp --specpath=build calculator.py

REM Periksa apakah build berhasil
if exist "build\calculator.exe" (
    echo.
    echo =======================
    echo Build BERHASIL!
    echo File executable ada di: %CD%\build\calculator.exe
    echo =======================
    
    REM Jalankan kalkulator
    echo.
    echo Menjalankan kalkulator...
    echo =======================
    start "" cmd /k "cd /d %CD% && build\calculator.exe"
) else (
    echo.
    echo =======================
    echo Build GAGAL!
    echo Periksa pesan error di atas.
    echo =======================
    exit /b 1
)

echo.
pause
