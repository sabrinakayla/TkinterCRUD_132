Penjelasan Struktur:

1. `main.py` File utama yang dijalankan untuk menampilkan jendela GUI aplikasi, memproses logika prediksi berdasarkan nilai tertinggi, serta menghubungkannya dengan penyimpanan database SQLite.

* `import sqlite3`: Perintah buat ngambil modul SQLite supaya aplikasi bisa membuat database, tabel, dan menyimpan data secara lokal.
* `import tkinter as tk`: Perintah buat ngambil modul Tkinter supaya komponen GUI bisa dipakai.
* `def inisialisasi_db()`: Fungsi buat bikin database file `database_nilai.db` dan tabel `nilai_siswa` secara otomatis saat aplikasi pertama kali dijalankan.
* `def hitung_prediksi()`: Fungsi buat ngatur aksi pas tombol diklik, isinya buat memvalidasi input, menentukan prodi berdasarkan nilai tertinggi (Biologi, Fisika, atau Inggris), dan menyimpan data siswa ke database.
* `tk.Tk()`: Buat bikin jendela utama aplikasi (*main window*).
* `tk.Label()`: Buat nampilin teks di layar, seperti judul aplikasi, label nama siswa, mata pelajaran, dan hasil prediksi.
* `tk.Frame()`: Wadah atau kontainer buat ngelompokkan dan merapikan susunan form input serta kotak hasil.
* `tk.Entry()`: Kolom teks satu baris buat nerima masukan nama siswa serta nilai Biologi, Fisika, dan Inggris.
* `tk.Button()`: Tombol bertuliskan "Hasil Prediksi" yang kalau diklik bakal manggil fungsi `hitung_prediksi()`.
* `root.mainloop()`: Perintah penutup buat ngejalanin event loop utama supaya jendela aplikasinya tetap terbuka dan merespons interaksi user.