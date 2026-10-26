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

    # Simpan ke database SQLite
    try:
        conn = sqlite3.connect("database_nilai.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        """, (nama, bio, fis, ing, prediksi))
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error Database", f"Gagal menyimpan data: {e}")
        return

    lbl_hasil.config(text=prediksi, fg="#2563eb")
    lbl_status.config(text=f"Selamat {nama}, data disimpan & cocok di prodi ini!", fg="#16a34a")
    messagebox.showinfo("Sukses", "Data nilai berhasil diproses dan disimpan ke database!")

    inisialisasi_db()

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("480x600")
root.configure(bg="#f8fafc")
root.resizable(False, False)

tk.Label(root, text="PREDIKSI PRODI PILIHAN", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#0f172a").pack(pady=(15, 2))
tk.Label(root, text="Masukkan nilai Biologi, Fisika, dan Inggris", font=("Segoe UI", 9), bg="#f8fafc", fg="#64748b").pack(pady=(0, 10))

frame_form = tk.Frame(root, bg="#ffffff", bd=1, relief="solid", padx=20, pady=15)
frame_form.pack(padx=25, pady=5, fill="both", expand=True)

tk.Label(frame_form, text="Nama Siswa", font=("Segoe UI", 9, "bold"), bg="#ffffff", fg="#334155").grid(row=0, column=0, sticky="w", pady=(0, 5))
entry_nama = tk.Entry(frame_form, font=("Segoe UI", 10), bg="#f8fafc", relief="solid", bd=1)
entry_nama.grid(row=0, column=1, sticky="ew", pady=(0, 5), ipady=3)

tk.Frame(frame_form, height=1, bg="#e2e8f0").grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)

tk.Label(frame_form, text="Nilai Biologi", font=("Segoe UI", 9), bg="#ffffff", fg="#475569").grid(row=2, column=0, sticky="w", pady=6)
entry_biologi = tk.Entry(frame_form, font=("Segoe UI", 9), width=12, bg="#f8fafc", relief="solid", bd=1, justify="center")
entry_biologi.grid(row=2, column=1, sticky="w", pady=6, ipady=2)

tk.Label(frame_form, text="Nilai Fisika", font=("Segoe UI", 9), bg="#ffffff", fg="#475569").grid(row=3, column=0, sticky="w", pady=6)
entry_fisika = tk.Entry(frame_form, font=("Segoe UI", 9), width=12, bg="#f8fafc", relief="solid", bd=1, justify="center")
entry_fisika.grid(row=3, column=1, sticky="w", pady=6, ipady=2)

tk.Label(frame_form, text="Nilai Inggris", font=("Segoe UI", 9), bg="#ffffff", fg="#475569").grid(row=4, column=0, sticky="w", pady=6)
entry_inggris = tk.Entry(frame_form, font=("Segoe UI", 9), width=12, bg="#f8fafc", relief="solid", bd=1, justify="center")
entry_inggris.grid(row=4, column=1, sticky="w", pady=6, ipady=2)

frame_form.columnconfigure(1, weight=1)