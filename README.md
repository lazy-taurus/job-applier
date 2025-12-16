# 🚀 JobApplyPro

**JobApplyPro** is an intelligent, AI-powered automation tool designed to streamline the job application process. It monitors your clipboard for job descriptions, researches the company in real-time, and instantly generates a tailored, high-quality cover note or "Why do you want to work here?" response.

Built with **Python**, **Google Gemini AI**, and **DuckDuckGo Search**.

## ✨ Key Features

  * **📋 Smart Clipboard Listener:** Automatically detects when you copy a job description.
  * **🧠 Context-Aware AI:** Uses Google Gemini (Free Tier) to analyze the job role and your resume.
  * **🕵️ Automated Research:** Fetches real-time info about the company using DuckDuckGo to make your application stand out.
  * **🎭 Dual Personality Modes:**
      * **Startup Mode (F9):** Energetic, passionate, and vision-focused.
      * **Corporate Mode (F10):** Professional, structured, and efficiency-focused.
  * **⌨️ Global Hotkeys:** Control the bot from anywhere without switching windows.

-----

## 🛠️ Installation & Setup

### 1\. Clone the Repository

```
git clone [https://github.com/YOUR_USERNAME/JobApplyPro.git](https://github.com/YOUR_USERNAME/JobApplyPro.git)
cd JobApplyPro
```

### 2\. Install Dependencies

```
pip install -r requirements.txt
```

### 3\. Configure Your Secrets (Important\!)

Since this project uses API keys, you must create a local configuration file. This file is ignored by Git for security.

1.  Create a file named `secrets.py` inside the `config/` folder.

2.  Add your Google Gemini API Key:

    # config/secrets.py

    GEMINI\_API\_KEY = "AIzaSy\_YOUR\_API\_KEY\_HERE"

### 4\. Add Your Resume

1.  Create a file named `my_resume.txt` inside the `data/` folder.
2.  Paste your raw resume text into it.

-----

## 🚀 How to Use

1.  **Run the Application:**

    ```
    python main.py
    ```

2.  **Copy a Job Description:** Highlight text on LinkedIn or a job board and press `Ctrl+C`.

3.  **Get Your Answer:** The AI will research the company and copy a perfect cover note to your clipboard automatically.

4.  **Paste & Submit:** Just press `Ctrl+V` in the application box\!

### ⌨️ Hotkeys

| Key | Action |
| :--- | :--- |
| **F9** | Switch to **Startup Mode** (High Energy) |
| **F10** | Switch to **Corporate Mode** (Professional) |
| **F8** | **Pause/Resume** the Bot |

-----

## 📂 Project Structure

```
JobApplyPro/
├── core/                  # AI & Research Logic
│   ├── generator.py       # Gemini AI Handler
│   └── researcher.py      # DuckDuckGo Searcher
├── config/                # Configuration Files
│   ├── settings.yaml      # Prompts & Modes
│   └── secrets.py         # API Keys (GitIgnored)
├── data/                  # User Data
│   └── my_resume.txt      # Your Resume (GitIgnored)
├── main.py                # Application Entry Point
└── requirements.txt       # Python Dependencies
```

## 📦 Build as Executable

To turn this script into a portable `.exe` file for Windows:

```
pip install pyinstaller
pyinstaller --onefile --name JobApplyPro main.py
```

*Note: You must manually place the `config` and `data` folders next to the generated `.exe` for it to work.*

-----

## 📜 Disclaimer

This tool is for personal productivity. Please review all AI-generated text before submitting.