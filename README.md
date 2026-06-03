# AdoptMe - Platform Adopsi Hewan Peliharaan

AdoptMe adalah aplikasi web berbasis Django yang dirancang untuk mempertemukan hewan peliharaan yang membutuhkan rumah dengan calon pengadopsi. Aplikasi ini memiliki antarmuka publik yang ramah pengguna dan dashboard khusus admin yang dikembangkan dari nol untuk mengelola CRUD hewan serta menyetujui pengajuan adopsi.

---

## ✨ Fitur Utama

### 👤 Halaman Pengguna (Publik & Member)
- **Landing Page Publik:** Semua orang dapat melihat daftar hewan peliharaan yang tersedia tanpa harus login.
- **Pencarian & Filter:** Mencari hewan berdasarkan nama atau memfilternya berdasarkan jenis spesies (Kucing, Anjing, Lainnya).
- **Detail Informasi Hewan:** Melihat informasi rinci tentang hewan (umur, status, foto, dan deskripsi).
- **Sistem Pengajuan Adopsi:** Pengguna yang sudah login dapat mengisi formulir pengajuan adopsi terperinci (alasan & pengalaman).
- **Profil Pengguna:** Halaman profil bagi pengguna untuk memperbarui informasi kontak (Nomor Telepon, Alamat, Foto Profil).
- **Riwayat Adopsi:** Pengguna dapat melacak status pengajuan hewan adopsinya sendiri.
- **Validasi Keamanan Password:** Indikator kekuatan password (minimal 8 karakter & angka) secara *real-time* disertai toggle buka/tutup kata sandi.
- **Pagination & UI Dinamis:** Menampilkan data secara modular (8-10 per halaman) dengan desain antarmuka berbasis Tailwind CSS yang responsif dan modern.

### 🎨 Estetika & Interaktivitas Premium (GSAP)
- **Minimalist Stage Preloader:** Transisi layar pembuka berupa tirai penutup gelap yang terangkat ke atas secara sinematik saat pertama kali membuka halaman utama.
- **Agency-Style Text Reveal:** Judul utama halaman landing terkuak (*reveal*) mulus dari bawah baris teks.
- **Magnetic CTA Button:** Tombol aksi utama secara interaktif mendekat dan menempel halus mengikuti gerakan kursor mouse pengguna.
- **3D Tilt Hover Effects:** Kartu hewan peliharaan bereaksi miring secara tiga dimensi mengikuti arah kursor mouse ketika disentuh (*hover*).
- **Floating Parallax Elements:** Ornamen abstrak di latar belakang yang bergeser perlahan sesuai pergerakan mouse memberikan efek kedalaman ruang (parallax).

### 🛡️ Dashboard Admin (Khusus Admin/Staff)
- **Autentikasi Aman:** Dashboard *hanya* dapat diakses oleh admin yang sudah login.
- **CRUD Hewan Peliharaan:** Fitur lengkap untuk Tambah (Create), Baca (Read), Ubah (Update), dan Hapus (Delete) data hewan.
- **Manajemen Permintaan Adopsi:** Admin dapat meninjau alasan dan pengalaman calon pengadopsi, kemudian memutuskan untuk **Setujui** atau **Tolak** permohonan secara langsung.
- **Notifikasi (Toast):** Memberikan umpan balik instan setiap kali Admin melakukan suatu aksi (berhasil ditambah, disetujui, dll).

---

## 🛠️ Teknologi & Framework

- **Backend:** [Django (Python)](https://www.djangoproject.com/)
- **Database:** MySQL
- **Frontend / Styling:** [Tailwind CSS](https://tailwindcss.com/)
- **Ikon:** Heroicons (SVG)

---

## ⚙️ Panduan Instalasi & Penggunaan

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek ini di *local machine* Anda.

### 1. Prasyarat (*Prerequisites*)
Pastikan perangkat Anda sudah terinstal:
- **Python 3.9+**
- **Node.js & npm** (untuk *build* Tailwind CSS)
- **MySQL Server** (XAMPP, Laragon, dsb.)

### 2. Konfigurasi Database
1. Buka MySQL Anda (misal lewat phpMyAdmin).
2. Buat database baru dengan nama: **`db_adoptme`**.
3. Pastikan username MySQL Anda adalah `root` dan password kosong (`''`). Jika berbeda, Anda bisa menyesuaikannya di file `adopt_project/settings.py` pada bagian `DATABASES`.

### 3. Setup *Virtual Environment* & Dependensi Python
Buka terminal/CMD di direktori proyek, lalu jalankan:

```bash
# Membuat virtual environment
python -m venv venv

# Aktivasi virtual environment (Windows)
.\venv\Scripts\activate
# Aktivasi virtual environment (Mac/Linux)
# source venv/bin/activate

# Install dependensi (Django, mysqlclient, dll)
pip install django mysqlclient pillow
```

### 4. Setup Dependensi Node (Tailwind CSS)
Buka terminal baru atau gunakan terminal yang sama, pastikan Anda berada di direktori proyek:
```bash
# Install paket npm (tailwindcss, dsb)
npm install

# Build CSS awal
npm run build:css
```
*(Catatan: Anda dapat membiarkan `npm run build:css` berjalan di belakang jika Anda ingin mengubah styling)*

### 5. Migrasi Database
Kembali ke terminal tempat *virtual environment* Python aktif, jalankan:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Buat Akun Superuser (Admin)
Untuk mengakses Dashboard Admin, Anda perlu membuat akun superuser:
```bash
python manage.py createsuperuser
```
*(Ikuti instruksi pengisian username, email, dan password).*

### 7. Jalankan Aplikasi
```bash
python manage.py runserver
```
Akses aplikasi melalui browser di: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔗 Struktur Navigasi Aplikasi

- **Beranda Publik:** `http://127.0.0.1:8000/`
- **Login / Register:** Dapat diakses melalui tombol di Navbar.
- **Dashboard Admin:** `http://127.0.0.1:8000/dashboard/` *(Login menggunakan akun superuser yang Anda buat di Langkah 6).*

---

## 📁 Struktur Direktori Penting

- `adopt_project/` - Inti konfigurasi dan pengaturan Django (`settings.py`, `urls.py`).
- `pets/` - Aplikasi utama (Model, View, Form, URL untuk publik dan admin).
- `templates/` - Berisi seluruh file antarmuka (HTML).
  - `templates/dashboard/` - Antarmuka khusus untuk Dashboard Admin.
- `static/` - Berisi file aset statis dan hasil kompilasi CSS Tailwind (`output.css`).
- `media/` - Tempat penyimpanan file unggahan (*Uploads*), seperti foto hewan dan foto profil pengguna.
