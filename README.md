# Attendance Calculator – CLI Project

A simple Python-based command-line tool to help students calculate and predict their attendance for different subjects in a semester.

This project is built as part of the **“Build Your Own Project”** flipped course evaluation and aligns with the requirements of functional modules, clear input/output, and a logical workflow.  

---

## 🎯 Project Overview

The **Attendance Calculator** allows a student to:

- Check their **existing attendance percentage** for:
  - English (fixed total of 10 classes per semester)
  - Any other subject (fixed total of 26 classes per semester)
- Predict their **future attendance** either by:
  - Providing how many classes they plan to attend  
  - Providing the percentage they want to maintain and getting the **minimum number of classes** they must attend

All interactions happen through a simple text-based menu using the terminal/command line.

---

## ✨ Features

1. **Existing Attendance Calculator**
   - Choose subject: English or Other subject  
   - Enter number of classes attended  
   - Get attendance percentage as output  

2. **Attendance Prediction – Percentage from Classes**
   - Choose subject  
   - Enter how many classes you plan to attend  
   - Get predicted attendance percentage  

3. **Attendance Prediction – Classes from Percentage**
   - Choose subject  
   - Enter desired attendance percentage  
   - Get the **minimum number of classes** you must attend to maintain that percentage  

4. **Basic Input Validation**
   - Rejects class counts greater than total possible classes  
   - Ensures percentage is within a valid range (0–100) in the improved version  

---

## 🧰 Tech Stack / Tools Used

- **Language:** Python 3.x  
- **Environment:** Any system with Python 3 installed (Windows / macOS / Linux)  
- **Interface:** Command Line Interface (CLI)  
- **Version Control (recommended):** Git & GitHub  

---

## 📁 Project Structure

Example structure of the repository:

bash
attendance-calculator/
├── attendance.py        # Main Python script containing the attendance() function
├── README.md            # Project documentation
├── statement.md         # Problem statement & scope document
└── (optional) docs/     # Design diagrams, report, etc.

---

## installation and running instructions
Make sure Python is installed on your computer.
Open Command Prompt or Terminal and type:
python --version
If a version number appears, Python is installed.
Download the project folder (or ZIP file) to your computer.
Open the project folder.
Open Command Prompt or Terminal inside the folder.
Type the following to run the program:
python attendance.py
(If that doesn't work, type python3 attendance.py)
Follow the instructions shown on the screen.

---

✅ Testing Instructions

You can manually test the program by trying different inputs:
Valid test cases
English, attended 5 out of 10 classes → Expect 50%
Other subject, attended 13 out of 26 → Expect 50%
Prediction: 8 English classes out of 10 → Expect 80%
Prediction: Want 75% in other subject →
Required classes = 0.75 × 26 ≈ 19 or 20 (depending on your logic)
Invalid test cases
Enter more than 10 for English classes → Should show invalid input
Enter more than 26 for other subject → Should show invalid input
Enter negative classes or negative percentages → Should be handled or rejected
You can also add simple print() statements for debugging while developing and then remove them in the final version.

---

## project structure
attendance-calculator/
  attendance.py
  README.md
  statement.md

---

## author
Anushka Soni
VIT student
course: Introduction to problem solving

---

## license
This project is created for academic purposes under the VITyarthi Build Your Own Project guidelines.
