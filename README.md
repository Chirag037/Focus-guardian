# 🔒 Focus Guardian – Smart Productivity Tracker

> A minimalist and intelligent desktop application to track your focus sessions, detect distractions, and help build disciplined work habits.

---

## 📌 Features

- ⏱️ **Start/Stop Focus Timer** – Manual Pomodoro-style focus sessions
- 💤 **Idle Detection** – Detects inactivity using mouse/keyboard silence
- 💬 **Motivational Quotes** – Boost morale after each session
- 📊 **Daily Report Chart** – Visual overview of time spent focusing
- 💾 **Local Database** – Saves sessions in SQLite automatically
- 🧠 **100% GUI-Based** – No terminal needed

---

## 🖼️ Screenshot
> _Add a screenshot of the UI here_  
> `Start`, `Stop`, and `Show Report` buttons with a motivational message display.

---

## 🛠 Installation

1. **Clone the repository**
```bash
https://github.com/Chirag037/Focus-guardian
cd FocusGuardian
Install required packages

bash
Copy
Edit
pip install matplotlib pynput
Run the app

bash
Copy
Edit
python FocusGuardian.py
🧰 Tech Stack
Component	Tool
GUI	tkinter
DB	SQLite
Charts	matplotlib
Idle Detection	pynput

📁 Project Structure
bash
Copy
Edit
FocusGuardian/
├── FocusGuardian.py        # Main app file with GUI + logic
├── focus_data.db           # (Auto-generated) SQLite DB
├── README.md               # Project overview
└── requirements.txt        # Optional: dependencies list
💡 Future Features (Ideas)
Voice reminders (e.g., “Stay focused!” using pyttsx3)

Daily focus goals and progress bars

Dark/light mode toggle

Export report to PDF/CSV

🙋 Author
Chirag
🔗 GitHub
