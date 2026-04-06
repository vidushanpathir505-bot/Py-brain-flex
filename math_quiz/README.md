# 🧮 Math Quiz

A command-line arithmetic quiz game that tests your mental math skills across 10 randomly generated questions.

## How It Works

Each round presents 10 questions using randomly selected numbers (1–10) and operators. After answering all questions, your final score is displayed out of 10.

**Supported operations:** Addition `+`, Subtraction `-`, Multiplication `*`, Division `/`

## Getting Started

**Requirements:** Python 3.x (no external dependencies)

```bash
python math_quiz.py
```

## Gameplay Example

```
1. 7 + 3
Enter your answer: 10
Correct!
2. 8 / 4
Enter your answer: 3
 Wrong! The answer was 2.0
...
🚩Final score: 8/10
```

## Features

- 10 random questions per session
- All four basic arithmetic operations
- Division answers rounded to 2 decimal places
- Input validation — invalid entries prompt a retry without losing the question

## Future Improvements

- **Difficulty levels** — Easy / Medium / Hard with varying number ranges and operators
- **Timer per question** — limit response time to add pressure
- **Negative numbers support** — extend number range below zero
- **Score percentage display** — show results as a percentage alongside the raw score
- **Save high scores to file** — persist and display a leaderboard across sessions
- **GUI version** — rebuild the interface using Tkinter
