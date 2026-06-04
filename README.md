# AdoptMe - Platform Adopsi Hewan Peliharaan

AdoptMe adalah aplikasi web Django untuk mengelola dan mengajukan adopsi hewan peliharaan. Aplikasi ini memiliki halaman publik untuk calon pengadopsi, dashboard custom untuk admin/staff, dan integrasi Django Admin bawaan.

Desain saat ini memakai konsep **Dark Editorial Pet Sanctuary**: antarmuka publik bernuansa gelap, hangat, sinematik, dan beraksen terracotta. Dashboard admin dibuat lebih operasional dengan tema light-warm yang tetap konsisten dengan identitas visual AdoptMe.

---

## Fitur Utama

### Pengguna Publik & Member
- Melihat daftar hewan yang tersedia untuk diadopsi.
- Mencari hewan berdasarkan nama.
- Filter hewan berdasarkan spesies: Kucing, Anjing, dan Lainnya.
- Melihat detail hewan, foto, umur, deskripsi, dan status adopsi.
- Register dan login akun pengguna.
- Mengajukan adopsi dengan alasan dan pengalaman memelihara hewan.
- Melihat riwayat pengajuan adopsi sendiri berdasarkan data `AdoptionRequest`.
- Mengelola profil kontak: nomor telepon, alamat, dan avatar.

### Admin / Staff
- Dashboard custom di `/dashboard/`.
- Statistik data hewan dan permintaan adopsi.
- CRUD data hewan: tambah, edit, hapus.
- Review permintaan adopsi.
- Setujui atau tolak pengajuan adopsi.
- Link langsung ke Django Admin bawaan di `/admin/`.
- Admin tidak dapat mengajukan adopsi, termasuk melalui URL langsung.

### UI & Interaksi
- Tema publik dark editorial dengan font Cormorant Garamond, DM Sans, dan Space Mono.
- Preloader halaman utama.
- GSAP animation untuk reveal, hover, cursor, dan scroll effects.
- Custom status badge untuk Tersedia, Pending, Diadopsi, Disetujui, dan Ditolak.
- Halaman auth compact dengan panel gambar hewan dari CDN.
- Dashboard admin dengan sidebar gelap, kartu statistik beraksen, dan tabel warm-light.

---

## Teknologi

- Backend: Django 5.2.14
- Database: MySQL
- Frontend styling: Tailwind CSS + custom CSS variables
- Animasi: GSAP + ScrollTrigger CDN
- Media upload: Django `ImageField`
- Font: Google Fonts
- Runtime frontend tooling: Node.js + Tailwind CSS

---

## Struktur Data Utama

### `Pet`
Menyimpan data hewan:
- nama
- spesies
- umur dalam bulan
- deskripsi
- foto
- status adopsi: `Available`, `Pending`, `Adopted`
- adopter

### `AdoptionRequest`
Menyimpan pengajuan adopsi:
- hewan
- user pengaju
- alasan adopsi
- pengalaman memelihara
- status: `Pending`, `Approved`, `Rejected`

### `UserProfile`
Menyimpan profil tambahan user:
- nomor telepon
- alamat
- avatar

---

## Prasyarat

Pastikan sudah tersedia:

- Python 3.10+
- MySQL Server, misalnya Laragon atau XAMPP
- Node.js dan npm
- Git

---

## Setup Project

### 1. Masuk ke folder project

```powershell
cd "C:\Users\Lenovo\Downloads\Fitrah\Tugas\Lab PPL\UAS"
```

### 2. Aktifkan virtual environment

Jika folder `venv` sudah ada:

```powershell
.\venv\Scripts\activate
```

Jika belum ada:

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install django pymysql pillow
```

Catatan: project ini memakai backend MySQL Django. Pastikan dependency MySQL yang digunakan di environment sudah sesuai dengan konfigurasi lokal.

### 3. Siapkan database MySQL

Buat database:

```sql
CREATE DATABASE db_adoptme;
```

Konfigurasi database berada di `adopt_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_adoptme',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Jika username/password MySQL berbeda, ubah bagian tersebut.

### 4. Jalankan migrasi

```powershell
python manage.py migrate
```

### 5. Buat akun admin

```powershell
python manage.py createsuperuser
```

Admin/staff dapat mengakses:

- Dashboard custom: `http://127.0.0.1:8000/dashboard/`
- Django Admin: `http://127.0.0.1:8000/admin/`

### 6. Install dependency frontend

```powershell
npm install
```

Build CSS:

```powershell
npm run build:css
```

Watch CSS saat development:

```powershell
npm run watch:css
```

Catatan: file yang dibaca browser adalah `static/css/output.css`. Custom design token utama berada di `static/css/input.css`.

### 7. Jalankan server

```powershell
python manage.py runserver 127.0.0.1:8000
```

Buka:

```text
http://127.0.0.1:8000/
```

---

## Route Penting

| Route | Keterangan |
|---|---|
| `/` | Halaman utama dan katalog hewan |
| `/pet/<id>/` | Detail hewan |
| `/login/` | Login user |
| `/register/` | Register user |
| `/logout/` | Logout |
| `/adopt/<id>/` | Form pengajuan adopsi |
| `/my-adoptions/` | Riwayat pengajuan adopsi user |
| `/profile/` | Profil user |
| `/dashboard/` | Dashboard custom admin |
| `/dashboard/pet/add/` | Tambah hewan |
| `/dashboard/pet/edit/<id>/` | Edit hewan |
| `/dashboard/pet/delete/<id>/` | Hapus hewan |
| `/admin/` | Django Admin bawaan |

---

## Struktur Folder

Struktur folder berikut memisahkan konfigurasi project, logika aplikasi, template tampilan, aset statis, dan file upload. Pembagian ini dibuat agar kode lebih mudah dibaca, dirawat, dan dijelaskan saat presentasi.

```text
manage.py
package.json
tailwind.config.js

adopt_project/
  __init__.py
  settings.py
  urls.py
  asgi.py
  wsgi.py

pets/
  __init__.py
  admin.py
  apps.py
  models.py
  views.py
  forms.py
  urls.py
  tests.py
  migrations/

templates/
  base.html
  home.html
  pet_detail.html
  adopt_form.html
  my_adoptions.html
  profile.html
  login.html
  register.html
  dashboard/
    base.html
    index.html
    pet_form.html
    pet_confirm_delete.html

static/
  css/
    input.css
    output.css

media/
  pets/
  avatars/
```

### Penjelasan Struktur

| Folder/File | Fungsi |
|---|---|
| `manage.py` | Entry point command Django, digunakan untuk menjalankan server, migrasi, membuat superuser, dan perintah maintenance lain. |
| `adopt_project/` | Folder konfigurasi utama project Django. |
| `adopt_project/settings.py` | Menyimpan konfigurasi project seperti database MySQL, static/media file, installed apps, middleware, dan template directory. |
| `adopt_project/urls.py` | URL root project. File ini menghubungkan route `/admin/` bawaan Django dan route aplikasi `pets`. |
| `adopt_project/asgi.py` dan `adopt_project/wsgi.py` | Konfigurasi entry point server ASGI/WSGI jika aplikasi dideploy. |
| `pets/` | Aplikasi utama AdoptMe. Semua fitur inti adopsi berada di folder ini. |
| `pets/models.py` | Mendefinisikan tabel database: `Pet`, `AdoptionRequest`, dan `UserProfile`. |
| `pets/views.py` | Menyimpan logic halaman: katalog hewan, detail hewan, pengajuan adopsi, profil user, auth, dashboard admin, approval, dan reject pengajuan. |
| `pets/forms.py` | Menyimpan form Django untuk data hewan, registrasi user, pengajuan adopsi, dan profil user. |
| `pets/urls.py` | Menyimpan route aplikasi seperti `/`, `/login/`, `/register/`, `/dashboard/`, dan route CRUD hewan. |
| `pets/admin.py` | Tempat registrasi model ke Django Admin jika ingin dikelola melalui `/admin/`. |
| `pets/migrations/` | Riwayat perubahan struktur database yang dijalankan melalui `python manage.py migrate`. |
| `templates/` | Folder semua file HTML yang dirender Django. |
| `templates/base.html` | Layout dasar halaman publik: navbar, footer, toast, cursor, dan script global. |
| `templates/home.html` | Halaman utama/katalog hewan, search, filter spesies, pagination, hero section, dan pet cards. |
| `templates/pet_detail.html` | Halaman detail satu hewan, status hewan, informasi lengkap, dan CTA pengajuan adopsi. |
| `templates/adopt_form.html` | Form pengajuan adopsi yang terhubung dengan model `AdoptionRequest`. |
| `templates/my_adoptions.html` | Riwayat pengajuan adopsi user berdasarkan data database. |
| `templates/profile.html` | Halaman profil user untuk nomor telepon, alamat, dan avatar. |
| `templates/login.html` dan `templates/register.html` | Halaman autentikasi compact dengan visual hewan dari CDN. |
| `templates/dashboard/` | Folder template dashboard custom khusus admin/staff. |
| `templates/dashboard/base.html` | Layout dashboard admin: sidebar, link dashboard, link website, link Django Admin, dan user info. |
| `templates/dashboard/index.html` | Halaman utama dashboard: statistik, daftar hewan, tabel data, dan review queue pengajuan. |
| `templates/dashboard/pet_form.html` | Form tambah/edit data hewan. |
| `templates/dashboard/pet_confirm_delete.html` | Halaman konfirmasi hapus data hewan. |
| `static/` | Folder aset statis project. |
| `static/css/input.css` | Source CSS utama berisi Tailwind directives, design token, komponen UI, tema dashboard, dan custom styles. |
| `static/css/output.css` | File CSS hasil build yang dibaca browser. File ini harus diperbarui setelah mengubah `input.css`. |
| `media/` | Folder upload dari user/admin saat aplikasi berjalan. |
| `media/pets/` | Tempat penyimpanan foto hewan. |
| `media/avatars/` | Tempat penyimpanan foto profil user. |
| `package.json` | Konfigurasi script npm untuk build/watch Tailwind CSS. |
| `tailwind.config.js` | Konfigurasi Tailwind: path template, font, warna, animasi, dan token tambahan. |

Alur sederhananya: user membuka route dari `pets/urls.py`, request diproses di `pets/views.py`, data diambil dari model pada `pets/models.py`, form berasal dari `pets/forms.py`, lalu hasilnya dirender ke file HTML di `templates/` dengan styling dari `static/css/output.css`.

---

## Perintah Verifikasi

Gunakan perintah berikut untuk memastikan project aman dijalankan:

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py showmigrations pets
```

Compile file Python:

```powershell
python -m compileall adopt_project pets
```

Build CSS:

```powershell
npm run build:css
```

---
