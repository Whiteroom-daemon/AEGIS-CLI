# ✦ AEGIS CLI ✦
**Advanced AI-Powered Static Application Security Testing (SAST) Auditor**

AEGIS is an elite, command-line interface (CLI) security tool engineered to perform deep static analysis on source code. Powered by **Llama-3.1 via Groq API**, it autonomously scans, detects, and provides remediation strategies for critical security vulnerabilities like SQL Injection, XSS, and hardcoded credentials.

---

### 🚀 Features
* **AI Threat Engine:** Leverages Llama-3.1 for high-precision vulnerability detection.
* **Cyber-Aesthetic UI:** Beautiful, color-coded terminal reports built with the `rich` library.
* **Instant Remediation:** Doesn't just find bugs; it tells you exactly how to fix them.
* **Lightweight & Portable:** Runs natively on any Linux/Unix terminal (including Termux).

---

### 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Whiteroom-daemon/AEGIS-CLI.git
   
2. **Navigate to the folder:**
   ```bash
   cd AEGIS-CLI
   
3. **Running AEGIS:**
After navigating into the folder, run the tool using the following command:
   ```bash
   python aegis.py your_target_file.py

4.**💻 Usage:**

Run the scanner on any target file to start the security audit:

* **Scan a single Python file:** 
  `python aegis.py your_code.py`
  (This runs the full analysis, identifying vulnerabilities and providing remediation steps.)

* **Check the tool info and version:**
  `python aegis.py --about`
  (Use this to see developer information and tool capabilities.)

* **Scan for quick vulnerability detection:**
  `python aegis.py --fast target_file.py`
  (Use this flag if you want a rapid, focused scan for critical bugs only.)
  
