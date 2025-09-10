import pandas as pd
from regex_cleaning import clean_contacts

# Example dataset
df = pd.DataFrame({
    "raw_data": [
        "Email: alice@gmail.com, Phone: +38 050-123-45-67 #work",
        "Contact bob@yahoo.com at 380971234567 (mobile)",
        "carol123@company.net | Phone: 0631234567 #personal"
    ]
})

# Clean and print
cleaned = clean_contacts(df)
print(cleaned)