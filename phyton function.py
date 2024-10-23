#1
def konversi_suhu(nilai,satuan):
    if satuan == 'C':
        # Konversi dari Celsius ke Fahrenheit
        return (nilai * 9/5) + 32
    elif satuan == 'F':
        # Konversi dari Fahrenheit ke Celsius
        return (nilai - 32) * 5/9
    else:
        return "Satuan tidak valid! Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."

# Input dari pengguna
nilai_suhu = float(input("Masukkan nilai suhu: "))
satuan_suhu = input("Masukkan satuan suhu ('C' untuk Celsius, 'F' untuk Fahrenheit): ")

# Panggil fungsi konversi suhu
hasil_konversi = konversi_suhu(nilai_suhu, satuan_suhu)
print(f"Hasil konversi: {hasil_konversi}")

#2
import math#karna ada fungsi mtk

# Fungsi lambda untuk menghitung luas lingkaran (mendaklarasikan fungsi seperti def)
luas_lingkaran = lambda jari_jari: math.pi * jari_jari**2 #jari-jari sbg parameter,math.pi rumus luas lingkaran

# Input dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Panggil fungsi lambda untuk menghitung luas lingkaran(output)
luas = luas_lingkaran(jari_jari)
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah: {luas}")#hasil perhitungan disimpan pada variabel luas
#f memasukkan nilai variabel langsung ke dalam string