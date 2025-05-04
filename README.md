# 🧮 CalcMate: Calculus-Powered Graphing App
![image](https://github.com/user-attachments/assets/a5f9cd58-46c9-45eb-9fe7-84cb24d2a657)

*CalcMate** is a Python-based calculator with a graphical user interface (GUI) built using `tkinter`. It lets users input mathematical functions and perform numerical integration with ease.

## Project Structure

```
Build/
├── assets/
│   └── frame0/
│       └── (image assets)
├── gui.py
├── calculations.py
└── README.md
```
## Features

- Input mathematical functions using Python syntax (e.g., `x**3-3*x`)
- Calculate numerical integrals using scipy.integrate.quad()
- Display integration results
- Modern and user-friendly interface

## Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)
- pyglet
- sympy
- scipy
- numpy

## Installation

1. Clone this repository:
   ```
   https://github.com/Tetsuuya/CalcMate.git
   cd calculator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   
   ```

3. Run

## Usage

1. Enter a mathematical function in the input field using Python syntax (e.g., `x**3-3*x`)
2. Enter the lower and upper limits for integration
3. Click the "Calculate" button to compute the integral
4. The result will be displayed in the "Result for numerical integration" field
