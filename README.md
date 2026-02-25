# KeepassXC Cracker 🔓

---

- 🎯 Target: KeepassXC

- 🟢 Severity: **Low**

- 📜 License: MIT
  
- 📅 Date: 25/2/2026

---

> ETHICAL DISCLAIMER ⚠️ — I am @r4shsec, the creator of this script. This script is only a **Proof of Concept (PoC)** and shouldn't be used for any illegal activities. The author isn't liable for any damages or legal action that may result from the use of this script. If you have malicious intent, **please do not use this script.** 

---

KeepassXC Cracker is an offensive security tool made by @r4shsec as a Proof-of-Concept (PoC) that a popular password manager, KeepassXC, is vulnerable to brute force attacks.

## Installation ⚙️

```bash
git clone https://github.com/r4shsec/KeepassXC-Cracker.git
cd KeepassXC-Cracker
pip install -r requirements.txt
```

## Usage ⚙️

```bash
usage: keepass_cracker.py [-h] -f FILE -w WORDLIST

An offensive security tool to break into KeepassXC databases.

options:
  -h, --help            show this help message and exit
  -f, --file FILE       KeePassXC database file.
  -w, --wordlist WORDLIST
                        Crack the password from a wordlist.
```

```
python3 -f [keepass file] -w [wordlist file]
```

## Security Advisory 🛡️

Always use **strong KeepassXC passwords** to secure your KeepassXC database against brute force attacks like this.

