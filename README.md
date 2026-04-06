# My Cool Beach Project (MVP)

A simple, reliable daily beach report system for Oahu.  
This MVP loads a list of beaches, checks weather conditions using the Open-Meteo API, evaluates beach-day quality, sends a daily email summary, and logs each run for traceability.

---

## 🌤️ Features
- Loads beach coordinates from a JSON file
- Fetches daily weather (temperature + cloudiness) via Open-Meteo
- Applies custom beach-day rules
- Sends a formatted email report using Gmail SMTP
- Saves run history to a log file
- Fully local, Windows-only MVP

---

## 📁 Project Structure
mcbp_mvp/
├── src/               # Python source code
│   └── beach_report.py
├── data/              # Input data
│   └── Beaches.json
├── docs/              # Screenshots + documentation
├── logs/              # Run history (auto-generated)
│   └── beach_report.log
├── README.md
└── .gitignore


---

## ▶️ How to Run

### 1. Install dependencies:
   pip install requests

### 2. Run the script:
   python src/beach_report.py

## Email Setup
- Uses Gmail SMTP to send the daily beach report
- SMTP SSL enabled
- Requires a Gmail App Password (needed for Python scripts)
- Sender and recipient can be the same for MVP
- sender = "your_email@gmail.com"
- password = "your_app_password"
- recipient = "your_email@gmail.com"


## Future Improvements
- Add UI or dashboard
- Add multi-day forecast logic

## How to View Logs
All run history is saved to:

mcbp_mvp/logs/beach_report.log

To view the log file:
1. Open the "logs" folder in the project root.
2. Open "beach_report.log" using Notepad, VS Code, or any text editor.
3. Each run is separated by a divider and includes:
   - Timestamp of the run
   - Weather results for each beach
   - Beach-day evaluation
   - Email send confirmation

## Updates to Project
- Added logging
- Added log file location
- Added how to view logs
