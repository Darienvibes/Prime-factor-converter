# Prime Factor Tool

A simple Python script that helps you convert numbers between **decimal** and **prime factor notation** — and vice versa! Inspired by the way it's used in certain Discord communities, this CLI tool makes it quick and easy to encode or decode numbers using their prime factorization.



## Features

- Convert a **decimal number** into a string of **prime factors** (e.g., `360` → `2 ^ 3 * 3 ^ 2 * 5`)
- Convert a **prime factor expression** back into a **decimal number** (e.g., `2 ^ 6 * 5` → `320`)
- Runs in an **endless loop** until you choose to exit
- Clean user-friendly terminal interface
- Error handling for invalid input



## Getting Started

### 1. Clone this Repository

```bash
git clone https://github.com/yourusername/prime-factor-tool.git
cd prime-factor-tool

2. Install Dependencies

The only required library is sympy. Install it using pip:

pip install sympy

3. Run the Tool

python primefactor_tool.py
```




# Usage Example

=== Prime Factor Tool ===

Choose an option:
1. Decimal to Prime Factor Language
2. Prime Factor Language to Decimal
3. Exit
Enter your choice (1, 2, or 3): 1
Enter a decimal number: 90
➡ Prime factor format: 2 * 3 ^ 2 * 5

Choose an option:
1. Decimal to Prime Factor Language
2. Prime Factor Language to Decimal
3. Exit
Enter your choice (1, 2, or 3): 2
Enter prime factor format (e.g., 2 ^ 3 * 5): 2^3 * 3^2 * 5
➡ Decimal value: 360




# How It Works

SymPy's factorint() function is used to break down decimal numbers into their prime factors.

The tool parses and safely evaluates prime factor expressions using Python's eval() after converting caret ^ to exponentiation (**).

It supports flexible input like 2^6*5, 2 ^ 6 * 5, etc.



# Requirements

Python 3.6+

sympy package
