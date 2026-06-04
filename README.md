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

```text
adopt_project/
  settings.py
  urls.py

pets/
  models.py
  views.py
  forms.py
  urls.py
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

## Catatan Development

- Pastikan MySQL/Laragon aktif sebelum menjalankan server.
- `media/` digunakan untuk upload foto hewan dan avatar user.
- Data halaman tidak statis; katalog, detail, dashboard, dan riwayat adopsi membaca data dari database.
- `static/css/output.css` perlu diperbarui setelah mengubah `static/css/input.css`.
- Dashboard custom hanya untuk user dengan `is_staff=True`.
- User biasa tidak bisa mengakses dashboard admin.
- Admin tidak bisa mengajukan adopsi.

