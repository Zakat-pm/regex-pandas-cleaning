import pandas as pd
import re

def clean_contacts(df):
    """
    Clean raw contact data: extract emails, normalize phone numbers, remove tags.
    """
    # Extract email
    df['email'] = df['raw_data'].str.extract(r'([\w\.-]+@[\w\.-]+\.\w+)')

    # Extract phone numbers
    df['phone_raw'] = df['raw_data'].str.extract(r'(\+?\d[\d\s-]+)(?=\s|#|,|\)|$)')

    # Keep only digits
    df['digits_only'] = df['phone_raw'].str.replace(r'\D', '', regex=True)

    # Normalize to +380 format
    df['phone'] = df['digits_only'].str.replace(r'^380|^0', '+380', regex=True)

    # Remove hashtags (#work, #personal, etc.)
    df['raw_data'] = df['raw_data'].str.replace(r'(#.*)', '', regex=True)

    return df[['email', 'phone']]