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