# University Progression Outcome System 🎓📊

This is a Python-based console application that determines and records student progression outcomes based on their credit scores. It supports both student and staff users, allows multiple entries, generates a histogram of results using the `graphics.py` module, and saves all progression outcomes into a text file.

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Progression Rules](#progression-rules)
- [Sample Output](#sample-output)
- [Credits](#credits)

---

## 📖 Overview

This program helps determine the academic progression outcome of students based on three credit types:

- **Pass credits**
- **Defer credits**
- **Fail credits**

It provides two modes:
- **Student mode**: Input is accepted once, and the result is displayed.
- **Staff mode**: Multiple records can be entered, outcomes are stored, a histogram is displayed, and the results are saved to a text file.

---

## ✅ Features

- Input validation (range and type checking)
- Two modes: Student and Staff
- Automatic progression outcome determination
- Stores outcomes in categorized lists
- Generates a graphical histogram using `graphics.py`
- Saves results into a text file (`test.txt`)
- Displays all saved progression data
