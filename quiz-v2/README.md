# 🧠 Quiz App

A multiple-choice quiz application built with Python and Tkinter, featuring 100 questions across 10 categories, live answer feedback, a score tracker, and a session timer.

---

## 📁 Project Structure

```
quiz-app/
├── main.py            # Entry point
├── gui.py             # Tkinter UI and screen management
├── logic.py           # Quiz engine (question flow, scoring)
├── questions.py       # Question bank (100 questions, 10 categories)
└── time_calculate.py  # Session timer
```

---

## 🚀 Features

- 📋 10 randomly selected questions per session from a pool of 100
- 🟢 Instant answer feedback — green for correct, red for wrong
- ✅ Correct answer revealed when a wrong choice is made
- 📊 Live score counter during the quiz
- ⏱️ Session timer that tracks total time taken
- 🔄 Restart without closing the app
- 💡 Clean 3-screen flow — Start → Quiz → Results

---

## 📚 Question Categories

| # | Category |
|---|---|
| 1 | General Knowledge & Daily Life |
| 2 | Science & Nature |
| 3 | Food & Household |
| 4 | Geography & Places |
| 5 | Animals & Insects |
| 6 | Sports & Entertainment |
| 7 | Technology & Modern Life |
| 8 | Health & Body |
| 9 | Time & Measurements |
| 10 | Miscellaneous |

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/vidushanpathir505-bot/Py-brain-flex
```

2. Navigate to the project folder:
```bash
cd quiz-v2
```

3. Run the app:
```bash
python main.py
```

---

## 📦 Requirements

- Python 3.x
- Tkinter *(included with Python — no installation needed)*

---

## 🖥️ App Screens

| Screen | Description |
|---|---|
| Start | App title with a START button |
| Quiz | Question, 4 answer buttons, live score and timer |
| Results | Final score, total time taken, and a RESTART button |

---

## 💡 Future Improvements

- 🗂️ Category selection before the quiz starts
- ⏳ Per-question countdown timer with auto-advance on timeout
- 📈 Score percentage display on the results screen
- 📝 Review screen — see all questions with correct answers after finishing
- 🏆 Local leaderboard — save and display high scores
- 📊 Category performance breakdown — identify weak areas

---

## 👨‍💻 Author

**Vidushan Pathirana**

⭐ If you like this project, give it a star!
