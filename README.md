# Calculator App with Tkinter

This project is a simple yet functional calculator built using Python's Tkinter library. It supports standard arithmetic operations along with a unique feature that calculates the estimated number of weeks left to live based on the user's age.

## Features

- Basic arithmetic operations: `+`, `-`, `*`, `/`, `%`, power (`^`, `**2`), and multiplication by π
- Clear (`CLR`), delete (`DEL`), and equals (`=`) functionality

## Usage

1. Run the program:
```bash
python calculator_app.py
```
![image](https://github.com/user-attachments/assets/75d800e5-11a8-4203-9a92-0967938f1839)   ![image](https://github.com/user-attachments/assets/2f66699c-1729-42c7-bb6a-62b0558e7796)



2. Use the on-screen buttons to perform calculations.
3. Click the ⛧ button to enter "weeks left" mode and input your age.

## How It Works
- User input is collected via an `Entry` widget.
- Calculations are evaluated safely using the `ast` module.
- The grid layout organizes buttons by function.
- The ⛧ button launches a sub-feature prompting age input and performs a simple arithmetic calculation.

## Purpose
This project was created to learn GUI development with Tkinter and explore how to integrate creative features into basic applications.
