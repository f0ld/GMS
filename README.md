# Get My Script - GMS

A lightweight Python/Playwright automation script that logs into a password-protected MyST (Jupyter Book / Sphinx) online course script, iterates through all chapters automatically, and merges them into a single, offline-ready PDF.

Built for university students dealing with flaky campus Wi-Fi who want to keep a local, clean copy of their lecture notes.

## ✨ Features
* **Automated Navigation:** Automatically finds and clicks the specific "Next Page" button (`myst-footer-link-next`) until the end of the script is reached.
* **Basic Auth & SSL Bypass:** Handles standard HTTP Basic Authentication and explicitly ignores invalid university/internal SSL certificates (e.g., `.sslip.io` domains).
* **Auto-Merge & Cleanup:** Stitches all downloaded pages together into one perfectly formatted A4 PDF document and deletes the temporary files afterwards.

## 🚀 Prerequisites
* Python 3.8 or newer
* A stable internet connection for the initial download of the script

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)
   cd YOUR-REPO-NAME

2. ** Install the required Python packages:**
   ```bash
    python3 -m pip install playwright pypdf

3. ** Install the Playwright Chromium Browser:**
   ```bash
   playwright install chromium
   
   
## ⚙️ Configuration & Security
⚠️ CRITICAL: Never commit your passwords to GitHub! The provided config.json is only a dummy file. Before doing anything else, make sure you have a .gitignore file in your repository that includes the configuration file if you have cloned this repo. You can create it by running this command in your terminal:
```bash
  echo "config.json" >> .gitignore
```

Create a file named config.json in the exact same directory as your Python script and add your credentials and target URL (Or just use the provided example. You just need to enter your data before running the script)

## Usage
Run the script from your terminal:
```bash
python3 gms.py
```
(this command assumes you are at the path of the script)

## Disclaimer
Please ensure you have permission from your professor or the copyright holder to download and store the course materials offline. This tool is meant for personal educational use and offline studying only.
