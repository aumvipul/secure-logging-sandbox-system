# 🔐 Cyber Security Monitoring System

A secure and interactive system implementing:
- **Tamper-Evident Logging System**
- **Controlled Execution Sandbox**

This project was developed as part of a Cybersecurity & Network Security Internship Assessment.

---

## 🚀 Features

### 🔐 Tamper-Evident Logging System
- Hash-chain based logging (blockchain-inspired)
- Detects:
  - Log modification
  - Log deletion
  - Log reordering
- Integrity verification system
- Persistent storage using JSON

---

### 🛡️ Controlled Execution Sandbox
- Executes untrusted Python code safely
- Detects and blocks:
  - Unauthorized imports (os, sys, etc.)
  - Dangerous functions (eval, exec, open)
- Timeout protection (prevents infinite loops)
- Resource control (CPU & memory limits on supported systems)
- Suspicious behavior detection

---

### 🌐 Web Dashboard (Flask)
- Add logs via UI
- Verify log integrity
- Execute sandboxed code
- View logs in structured format
- Real-time alerts for threats

---

## 🧠 System Architecture

---

## ⚙️ Technologies Used

- Python 3
- Flask
- Hashing (SHA-256)
- Subprocess module
- JSON (data storage)

---

## 📁 Project Structure

---cybersec_pro/
│
├── app.py
├── config.py
│
├── tamper_log/
│ ├── log_system.py
│ ├── verifier.py
│ └── logs.json
│
├── sandbox/
│ ├── sandbox.py
│ └── analyzer.py
│
├── templates/
│ └── index.html
│
├── static/
│ └── styles.css
│
└── requirements.txt

## ▶️ How to Run

1. Clone the repository:  git clone https://github.com/aumvipul/secure-logging-sandbox-system
2. Install dependencies:
   pip install -r requirements.txt
3.  Run the application:
   python app.py
4.Open in browser:
http://127.0.0.1:5000


---

## 🔍 Security Analysis

- Prevents unauthorized system access
- Ensures log integrity using cryptographic linking
- Detects tampering attempts in real-time
- Restricts execution of malicious inputs

---

## ⚠️ Limitations

- Not a fully isolated OS-level sandbox
- Keyword-based filtering can be bypassed in advanced attacks
- Resource control limited on Windows systems

---

## 🎯 Future Enhancements

- Docker-based sandboxing
- Database integration (MongoDB/PostgreSQL)
- Authentication system
- Real-time alert notifications

---

## 👨‍💻 Author

**Aum Vipul**

---

## 📌 Note

This project demonstrates core cybersecurity principles including integrity protection, secure execution, and threat detection in a controlled environment.
