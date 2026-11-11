-- Skema database ALPHA AI (referensi).
-- Tabel dibuat otomatis oleh server saat start (database/session.py -> init_db),
-- file ini disediakan jika ingin membuat tabel secara manual.
-- Kompatibel dengan SQLite dan PostgreSQL (untuk PostgreSQL ganti
-- "INTEGER PRIMARY KEY" menjadi "SERIAL PRIMARY KEY").

CREATE TABLE IF NOT EXISTS users (
    id                INTEGER PRIMARY KEY,
    email             VARCHAR(255) NOT NULL UNIQUE,
    hashed_password   VARCHAR(255) NOT NULL,
    subscription_tier VARCHAR(20)  NOT NULL DEFAULT 'free',  -- free, creator, pro
    created_at        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS generation_logs (
    id         INTEGER PRIMARY KEY,
    user_id    INTEGER REFERENCES users(id),  -- NULL = pengguna tamu
    prompt     TEXT        NOT NULL,
    result     TEXT,
    model      VARCHAR(100),
    status     VARCHAR(20) NOT NULL DEFAULT 'success',  -- success, error
    created_at TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_users_email ON users (email);
