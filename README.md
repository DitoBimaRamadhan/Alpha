# ALPHA AI

Aplikasi web untuk membuat konten teks dengan AI (Groq). Proyek ini dibagi menjadi
lima bagian yang terpisah dengan jelas: **HTML, CSS, JavaScript, Server, dan Database**.

## Struktur Proyek

```
Alpha/
├── frontend/                 # Tampilan (disajikan langsung oleh server)
│   ├── index.html            # HTML  - halaman generator teks
│   ├── pricing.html          # HTML  - halaman harga
│   ├── css/
│   │   └── style.css         # CSS   - semua gaya tampilan
│   └── js/
│       └── app.js            # JavaScript - logika halaman & pemanggilan API
├── server/                   # Server (Python + FastAPI)
│   ├── main.py               # titik masuk: API + file frontend
│   ├── config.py             # pengaturan dari .env
│   ├── routes/
│   │   ├── text.py           # POST /api/text/generate
│   │   └── health.py         # GET  /api/health
│   └── services/
│       └── ai_service.py     # pemanggilan model AI di Groq
├── database/                 # Database (SQLAlchemy)
│   ├── session.py            # koneksi & pembuatan tabel
│   ├── models.py             # tabel users & generation_logs
│   └── schema.sql            # skema SQL (referensi / buat manual)
├── .env.example              # contoh konfigurasi
└── requirements.txt          # dependensi Python
```

| Bagian     | Lokasi                 | Fungsi |
|------------|------------------------|--------|
| HTML       | `frontend/*.html`      | Struktur halaman generator dan harga |
| CSS        | `frontend/css/`        | Tampilan modern (tema gelap, responsif) |
| JavaScript | `frontend/js/`         | Kirim prompt ke API, tampilkan hasil, render paket harga |
| Server     | `server/`              | API FastAPI + menyajikan frontend, memanggil Groq |
| Database   | `database/`            | Menyimpan riwayat generate (SQLite / PostgreSQL) |

## Cara Menjalankan

Butuh Python 3.10 atau lebih baru.

```bash
# 1. Buat virtual environment & install dependensi
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 2. Siapkan konfigurasi
cp .env.example .env            # Windows: copy .env.example .env
# lalu isi GROQ_API_KEY di file .env (ambil di https://console.groq.com/keys)

# 3. Jalankan server (dari folder root proyek)
uvicorn server.main:app --reload
```

Buka **http://localhost:8000** di browser. Satu perintah ini menjalankan semuanya:
halaman web, API, dan database. Tabel database dibuat otomatis saat server start.

## Konfigurasi (`.env`)

| Variabel        | Default                | Keterangan |
|-----------------|------------------------|------------|
| `GROQ_API_KEY`  | *(kosong)*             | Wajib untuk generate. Tanpa ini server tetap jalan, tapi API membalas pesan error yang jelas. |
| `GROQ_MODEL`    | `openai/gpt-oss-20b`   | Model Groq. Daftar model: https://console.groq.com/docs/models |
| `DATABASE_URL`  | SQLite `alpha.db`      | Contoh PostgreSQL: `postgresql+psycopg2://user:password@localhost:5432/alpha` |
| `CORS_ORIGINS`  | `*`                    | Origin yang boleh memanggil API, dipisah koma |

> File `.env` dan `alpha.db` tidak ikut di-commit (sudah ada di `.gitignore`).

## API

| Method | Endpoint              | Keterangan |
|--------|-----------------------|------------|
| GET    | `/api/health`         | Status server, model aktif, dan apakah API key sudah diatur |
| POST   | `/api/text/generate`  | Body: `{"prompt": "..."}` → `{"result": "..."}` |

Dokumentasi interaktif tersedia di **http://localhost:8000/docs**.

Setiap permintaan generate (berhasil maupun gagal) dicatat di tabel `generation_logs`.

## Roadmap

- [ ] Login pengguna (JWT) menggunakan tabel `users`
- [ ] Batas kuota per paket (Free 5, Creator 100, Pro tanpa batas)
- [ ] Pembayaran (Stripe)
- [ ] Generate gambar
