# 🌐 NETRUNNER OS // AKIRA EDITION

![Version](https://img.shields.io/badge/Version-4.5-cyan)
![Platform](https://img.shields.io/badge/Environment-Termux-red)
![Status](https://img.shields.io/badge/Connection-STABLE-green)

A high-fidelity, web-based tactical interface for mobile penetration testing environments. This system bridges a **Python 3 Flask Backend** with a **Cyberpunk-inspired React/HTML Frontend**, allowing for remote shell execution directly from a browser.

---

## 🛠️ CORE ARCHITECTURE
* **Engine:** Python 3.12 (Flask)
* **Link:** Bi-directional REST API with Token Handshake
* **UI:** Tactical Grid Interface with CSS Scanlines
* **Arsenal:** Direct integration with `allhackertools`

## 🚀 DEPLOYMENT PROTOCOL

### 1. Initialize the Engine
Navigate to the core directory and fire the ignition script:
```bash
cd netrunner-final
./start_netrunner.sh
```
*Expected Output:* `SYSTEM STABLE - AWAITING DECK CONNECTION`

### 2. Launch the Deck
In a secondary terminal tab, serve the UI:
```bash
php -S 0.0.0.0:8080
```
Access the interface at: `http://localhost:8080`

## 🛡️ TACTICAL FEATURES
* **Automated Armory:** One-tap access to Nmap, Sqlmap, and Metasploit.
* **Grave Protocol:** Hardened security token authentication.
* **Real-time Logs:** Full stdout/stderr feedback loop.
* **Grid Interface:** Mobile-optimized tactical display.

## 📁 REPOSITORY STRUCTURE
| File | Function |
| :--- | :--- |
| `main.py` | The Flask Backend (The Brain) |
| `index.html`| The Web Interface (The Deck) |
| `start_netrunner.sh` | The Ignition Script |
| `.gitignore` | Prevents secret leaks during push |

---
**OPERATOR:** Akira
**STATUS:** ACTIVE
**ENCRYPTION:** OMEGA-99 ENABLED
