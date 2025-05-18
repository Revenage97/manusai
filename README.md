#!/bin/bash

# Panduan Instalasi dan Penggunaan Dashboard Manajemen Stok

## Persyaratan Sistem
- Python 3.8 atau lebih baru
- pip (Python package manager)

## Langkah Instalasi

1. Ekstrak file zip ke direktori pilihan Anda
2. Buat virtual environment Python:
   ```
   python -m venv venv
   ```
3. Aktifkan virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependensi:
   ```
   pip install -r requirements.txt
   ```
5. Masuk ke direktori inventory_dashboard:
   ```
   cd inventory_dashboard
   ```
6. Jalankan migrasi database:
   ```
   python manage.py migrate
   ```
7. Buat superuser (admin):
   ```
   python manage.py createsuperuser
   ```
   Ikuti petunjuk untuk membuat username dan password

## Menjalankan Aplikasi

1. Pastikan virtual environment aktif
2. Jalankan server Django:
   ```
   python manage.py runserver
   ```
3. Buka browser dan akses: http://localhost:8000

## Fitur Utama

- Login dan autentikasi
- Dashboard untuk melihat stok
- Upload file Excel
- Backup file Excel
- Log aktivitas
- Ubah password

## Format File Excel

File Excel yang diupload harus memiliki kolom berikut:
- Kode
- Nama Barang
- Kategori
- Harga Jual
- Total Stok

## Deployment ke Render

Untuk deployment ke Render, ikuti langkah-langkah berikut:

1. Buat akun di Render.com
2. Buat repository Git dan upload kode ini
3. Di dashboard Render, pilih "New Web Service"
4. Hubungkan dengan repository Git Anda
5. Isi informasi berikut:
   - Name: nama_aplikasi_anda
   - Environment: Python
   - Build Command: pip install -r requirements.txt && python inventory_dashboard/manage.py migrate
   - Start Command: cd inventory_dashboard && gunicorn inventory_dashboard.wsgi:application
   - Plan: Free

Untuk informasi lebih lanjut, silakan hubungi pengembang.
