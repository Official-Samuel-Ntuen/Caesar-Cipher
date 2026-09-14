### 🔐 Caesar Cipher — Encryption & Decryption Tool

> A real-time encryption and decryption web application built on the Caesar Cipher algorithm with a red hacker theme and brute force attack simulation.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

---

## 🎯 About The Project

This project was built as part of my **Cybersecurity Internship at DecodeLabs (Batch 2026)**.

Project 2 focuses on the **confidentiality logic** of cybersecurity — understanding how data is protected in transit using encryption. The Caesar Cipher is the foundation of all modern cryptography, from DES to AES-256.

> *\"We do not shift letters; we shift integers.\"* — DecodeLabs

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🔒 Real-time Encryption | Encrypt any message using Caesar Cipher |
| 🔓 Instant Decryption | Decrypt ciphertext with the correct shift key |
| 💀 Brute Force Simulator | Simulate all 25 possible decryption attempts |
| 🎚️ Shift Key Slider | Interactive slider to select shift key (1-25) |
| 📋 Copy Output | One-click copy of encrypted/decrypted text |
| 🔴 Red Hacker Theme | Matrix rain effect with red cybersecurity aesthetic |

---

## 🧮 The Math Behind It

**Encryption Formula:**

E(x) = (x + n) % 26


**Decryption Formula:**

D(x) = (x - n) % 26


Where:
- x = Character position (ASCII value)
- n = Shift key

**Example with shift 3:**

Plain: H E L L O

ASCII: 72 69 76 76 79

Encrypted: K H O O R


---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Algorithm:** Caesar Cipher (Mono-alphabetic Substitution)
- **Theme:** Red Hacker with Matrix Rain Effect

---

## 📁 Project Structure

Caesar-Cipher/
│
├── app.py # Flask backend & cipher logic
│
├── templates/
│ └── index.html # Frontend HTML
│
├── static/
│ ├── css/
│ │ └── style.css # Red hacker styling
│ └── js/
│ └── script.js # Matrix rain & cipher logic
│
└── README.md


---

## ▶️ How To Run

```bash
git clone https://github.com/Official-Samuel-Ntuen/Caesar-Cipher.git
cd Caesar-Cipher
pip3 install flask
python3 app.py
```

Then open your browser and go to:

http://127.0.0.1:5000


---

## 🧠 What I Learned

- Caesar Cipher mathematics and implementation
- How encryption protects data in transit
- Why small key spaces are vulnerable to brute force
- The evolution from Caesar Cipher to AES-256
- Flask routing and REST API design
- JavaScript async/await and fetch API
- Canvas API for Matrix rain animation

---

## 🔐 Security Concepts Covered

- **Confidentiality** — Encrypting data so only authorized parties can read it
- **Brute Force Attacks** — Why Caesar Cipher is vulnerable (only 25 keys)
- **Key Space** — Why modern encryption uses 128-256 bit keys
- **Symmetric Encryption** — Same key encrypts and decrypts

---

## 👨‍💻 Author

**Samuel Ntuen**
Junior Cybersecurity Analyst | DecodeLabs Intern 2026

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/yourprofile)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat-square&logo=github)](https://github.com/Official-Samuel-Ntuen)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> *\"You cannot hash what is weak. Filter entropy before Argon2id.\"* — DecodeLabs
'''
with open('README.md', 'w') as f:
    f.write(content)
print('README created!')
"
