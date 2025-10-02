# Kaprekar's Constant Explorer

A Python script that explores the fascinating mathematical phenomenon of Kaprekar's constant (6174) using the rich library for beautiful console output.

## What is Kaprekar's Constant?

Kaprekar's constant is 6174, discovered by Indian mathematician D. R. Kaprekar. The process works as follows:

1. Take any 4-digit number where all digits are different
2. Arrange the digits in descending order (A)
3. Arrange the digits in ascending order (B)
4. Calculate A - B
5. Repeat the process with the result
6. Eventually, you will reach 6174, and it will stay at 6174

## Features

- ✅ Input validation for 4-digit numbers with unique digits
- ✅ Beautiful console output using the rich library
- ✅ Step-by-step visualization of the process
- ✅ Configurable step limit (default: 50)
- ✅ Interactive mode with multiple number testing
- ✅ Progress indicators and colored output

## Installation

1. Install the required dependency:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python3 kaprekar_explorer.py
```

The script will prompt you to enter a 4-digit number with all different digits. It will then show you the step-by-step process until it reaches 6174 or hits the step limit.

## Example

```
Enter a 4-digit number: 1234

Step-by-Step Sequence:
┌──────┬────────┬────────────────────────────┐
│ Step │ Number │ Process                    │
├──────┼────────┼────────────────────────────┤
│ Start│ 1234   │ Initial number             │
│ 1    │ 3087   │ 4321 - 1234 = 3087         │
│ 2    │ 8352   │ 8730 - 0378 = 8352         │
│ 3    │ 6174   │ 8532 - 2358 = 6174         │
└──────┴────────┴────────────────────────────┘
```

## Requirements

- Python 3.6+
- rich library (>=13.0.0)

## Notes

- The script validates that all 4 digits are different
- There's a default limit of 50 steps to prevent infinite loops
- The process always converges to 6174 for valid inputs
# kaprekars_constant
