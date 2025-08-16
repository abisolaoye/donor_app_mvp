import pandas as pd
import os
import csv

FILE = "donations.csv"

def save_donation(donation):
    df = pd.DataFrame([donation])
    if os.path.exists(FILE):
        df.to_csv(FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(FILE, index=False, quoting=csv.QUOTE_ALL)

def load_donations():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)
    return pd.DataFrame(columns=["name", "email", "amount", "message"])
