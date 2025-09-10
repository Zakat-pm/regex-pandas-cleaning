# Regex & Pandas Data Cleaning Project

This project uses **Regex** and **Pandas** to clean messy contact data.  
It extracts emails, normalizes phone numbers, and removes tags like #work or #personal.

## Features
- Extracts valid email addresses
- Cleans and standardizes phone numbers into +380 format
- Removes text tags (#work, #personal)

## Installation
Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage
Run the example script:
```bash
python example.py
```

## Example Output
```
                 email         phone
0      alice@gmail.com  +380501234567
1       bob@yahoo.com  +380971234567
2  carol123@company.net  +380631234567
```