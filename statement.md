# Attendance Calculator – Problem Statement & Scope

## 1. Problem Statement

Students often struggle to track their attendance accurately and to calculate how many upcoming classes they need to attend in order to maintain a required percentage. Manual calculation is repetitive, time-consuming, and may lead to errors.

This project aims to solve this problem by developing a **Python-based command-line Attendance Calculator** that allows students to:

- Check their **existing attendance percentage** for a subject, and
- **Predict** future attendance based on either:
  - the number of classes they plan to attend, or
  - the percentage they want to achieve.

The system provides a simple, guided, menu-driven interface that removes calculation effort and improves planning.

---

## 2. Scope of the Project

The scope of the project includes:

- Development of a **CLI (Command Line Interface)** tool using Python.
- Support for two subject categories with fixed total classes per semester:
  - **English** → 10 classes
  - **Other subjects** → 26 classes
- Two functional modes:
  1. **Existing Attendance Mode**
     - User selects subject
     - Inputs classes attended
     - System returns attendance percentage
  2. **Attendance Prediction Mode**
     - Option 1: Enter number of planned classes → system returns percentage
     - Option 2: Enter target percentage → system returns required classes
- Basic input validation (e.g., class limits, percentage range)

Out of scope for this version:

- Data storage or saving past records
- Multi-user login system
- Customizable total classes
- Graphical or web interface

These features may be implemented in future extensions.

---

## 3. Target Users

The system is designed for:

- **College and university students**
- Students with fixed-count semester attendance systems
- Individuals needing to:
  - Check current attendance percentage
  - Maintain minimum attendance requirements (e.g., 75%)
  - Plan upcoming attendance to avoid shortage

---

## 4. High-Level Features

1. **Subject Selection**
   - Choose between English and other subjects

2. **Existing Attendance Calculation**
   - Input: classes attended
   - Output: attendance percentage

3. **Attendance Prediction – Percentage from Planned Classes**
   - Input: number of classes student will attend
   - Output: predicted attendance percentage

4. **Attendance Prediction – Required Classes from Percentage**
   - Input: target attendance percentage
   - Output: minimum number of classes to attend

5. **Input Validation**
   - Ensures valid class count (0–10 or 0–26)
   - Ensures percentage ranges are logical (0–100)

These features align with the required **functional modules**, **logical workflow**, and **clear input/output structure** as specified in the project guidelines.

