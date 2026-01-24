![OneStore Banner](assets/onestore.png)

# 🔐 OneStore

**Your Ultimate CLI Password Manager**

OneStore is a secure command-line password manager that stores your credentials in the cloud with end-to-end encryption. It uses a unique 5-word keyphrase system to encrypt your passwords locally before syncing to Supabase, ensuring that only you can access your data. Features include secure password generation, encrypted storage and retrieval, and automatic session management—all from your terminal.

---

## ✨ Features

- 🔒 **End-to-End Encryption** — Passwords are encrypted locally using Fernet (AES-128) before being stored
- 🗝️ **5-Word Keyphrase System** — Unique recovery system that only you know
- ☁️ **Cloud Sync** — Access your passwords from anywhere via Supabase
- 🔑 **Password Generator** — Generate strong, random passwords with custom length
- 🔄 **Auto-Login** — Secure session management for seamless access
- 🎨 **Beautiful CLI** — Colorful, user-friendly terminal interface

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vasipallie/OneStore.git
   cd OneStore
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run OneStore**
   ```bash
   cd cli
   python cli.py
   ```

---

## 📖 Usage

### Commands

| Command | Description |
|---------|-------------|
| `help` | Show all available commands |
| `auth` | Login, signup, or manage your account |
| `password-gen` | Generate a secure random password |
| `passstore` | Store a new password |
| `passretrieve` | Retrieve your stored passwords |
| `clear-passstore` | Clear all stored passwords |
| `support` | Get support information |
| `exit` | Exit OneStore |

### First Time Setup

1. Run `auth` and select **Signup**
2. Enter your email and create a password
3. **IMPORTANT:** Write down your 5 keyphrases — these are required to decrypt your passwords and cannot be recovered!
4. Confirm your keyphrases to complete registration

### Storing Passwords

1. Login with `auth` → **Login**
2. Enter your 5 keyphrases
3. Use `passstore` to save a new password, or `password-gen` to generate and save one

---

## 🔒 Security

OneStore takes your security seriously:

- **Local Encryption**: All passwords are encrypted on your device using Fernet symmetric encryption (AES-128-CBC with HMAC) before being sent to the cloud
- **Zero-Knowledge**: Your keyphrases never leave your device — only a salted hash is stored for verification
- **Keyphrase-Derived Key**: Your encryption key is derived from your 5 keyphrases using SHA-256
- **No Password Recovery**: Without your keyphrases, your passwords cannot be decrypted — not even by us

> ⚠️ **Warning**: If you lose your keyphrases, your passwords are **permanently unrecoverable**. Store them safely!

---

## 🛠️ Tech Stack

- **Python** — Core application
- **Supabase** — Authentication & database
- **Cryptography** — Fernet encryption
- **WonderWords** — Random keyphrase generation

---

## 📁 Project Structure

```
OneStore/
├── cli/
│   ├── cli.py          # Main application
│   └── backup.py       # Backup utilities
├── server/
│   ├── index.js        # Server endpoints
│   └── package.json
├── assets/
│   └── onestore.png
├── requirements.txt
└── readme.md
```

---

## 🤝 Contributing

Contributions are welcome to OneStore! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📬 Support

Having issues? [Open an issue](https://github.com/vasipallie/OneStore/issues) on GitHub.

---

## 📄 License

This project is open source and available under the [APGL License](LICENSE).

---
