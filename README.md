# 🍔 Interactive Food Order CLI
My 3rd Python project: A terminal-based restaurant menu app demonstrating functions, loops, and error handling.
A dynamic and interactive Command Line Interface (CLI) application built with Python to simulate a restaurant ordering system. This is my third Python project, focusing heavily on modularity, functions, and bulletproof user input validation.

## 📖 Description
This program allows users to choose between different food menus (Italian or Indian) and place an order. It is designed to be "crash-proof" by handling unexpected user inputs gracefully, ensuring a smooth ordering experience from start to finish.

## ✨ Features
* **Smart Input Handling:** Uses `.strip()` and `.title()` to process messy user inputs (e.g., typing "iTaLiAn" or "  indian  " will automatically be corrected).
* **Bulletproof Validation:** Implements `while True` loops and `try-except` blocks to prevent the program from crashing if a user inputs letters instead of numbers for the order amount.
* **Modular Code Structure:** Logic is broken down into specific, reusable functions (`select_meal`, `find_meal`, `create_summary`) that pass data using `return` statements rather than just printing everything.
* **Dynamic Menu Searching:** Matches user input against existing menu lists to ensure only available items can be ordered.

## 🚀 How to Run
1. Ensure Python is installed on your machine.
2. Clone this repository or download the script (e.g., `food_order.py`).
3. Open your terminal or command prompt.
4. Run the script using the following command:
   ```bash
   python food_order.py

## 🧠 What I Learned
Building this project leveled up my understanding of several core Python concepts:
* **The Power of return**: I learned the crucial difference between merely displaying data (print) and actually handing data back to the program to be used by other functions (return).
* **Infinite Loops for Validation**: Using while True to trap the user in a prompt until they provide valid data, preventing downstream errors.
* **String Manipulation**: Using .strip(), .lower(), and .title() to clean up unpredictable user input before processing it.
* **Modularity**: Breaking a large problem into smaller, interconnected "magic boxes" (functions) that rely on arguments and parameters.

## 🛠️ Future Improvements (UI/UX Focus)
While the current version uses basic string formatting (like \n for newlines and simple strings for borders), my next goal is to level up the terminal aesthetics. Future updates will focus on:
* **Dynamic Borders**: Creating a custom function that draws ==== or ---- borders that automatically adjust their length based on the text inside them.
* **Terminal Clearing**: Implementing os.system('clear') (or cls on Windows) to refresh the screen between menu changes, so the terminal doesn't scroll down endlessly.
* **Text Alignment**: Learning to use Python's advanced string formatting (like f"{item:<20}") to create perfectly aligned, tabular menu layouts instead of basic lists.
* **Colors and Styles**: Exploring libraries like colorama or ANSI escape codes to add colors (e.g., red for errors, green for success) to make the terminal output pop.
