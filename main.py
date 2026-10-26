import sqlite3
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk membuat database dan tabel SQLite
def inisialisasi_db():
    conn = sqlite3.connect("database_nilai.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    """)
    conn.commit()
    conn.close()

    # Fungsi untuk memproses prediksi dan menyimpan ke database
def hitung_prediksi():
    nama = entry_nama.get().strip()
    if not nama:
        messagebox.showwarning("Peringatan", "Silakan masukkan nama siswa terlebih dahulu!")
        return
    
    try:
        bio = int(entry_biologi.get().strip())
        fis = int(entry_fisika.get().strip())
        ing = int(entry_inggris.get().strip())
    except ValueError:
        messagebox.showerror("Error", "Nilai Biologi, Fisika, dan Inggris harus berupa angka!")
        return

    # Kondisi penentuan prodi sesuai ketentuan praktikum
    if bio > fis and bio > ing:
        prediksi = "Kedokteran"
    elif fis > bio and fis > ing:
        prediksi = "Teknik"
    elif ing > bio and ing > fis:
        prediksi = "Bahasa"
    else:
        prediksi = "Teknologi Informasi"