import datetime
import json
import os
from unittest import case

# Define the path to the JSON file where expenses will be stored
DATA_FILE = "/home/moharsh529/Coding/CLI_Finance_Manager/expenses.json"

# Initialize an empty list to hold the session expenses
session_expenses = []

# Ensure the directory for the data file exists
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

if os.path.exists(DATA_FILE):
    try:
        with open(DATA_FILE, "r") as f:
            session_expenses = json.load(f)
    except (json.JSONDecodeError, OSError):
        session_expenses = []

# Main loop to add expenses
while True:
    
    menu = str(input("1. Add Expense \n2. View All \n3.Show Total \n4. Exit" + "\n")).strip()
    
    match menu:
        case "1":
            category = input("Labor/material: ").strip().lower()
            amount = int(input("Enter the amount: "))
            description = input("Describe the expense: ").strip().lower()
            expense = {
                "category": category,
                "amount": amount,
                "description": description,
                "date": datetime.datetime.now().strftime("%Y-%m-%d")
            }
            session_expenses.append(expense)
            print(session_expenses)
        case "2":
            for expense in session_expenses:
                print(f"{expense['date']} - {expense['category']}: ${expense['amount']} - {expense['description']}")
        case "3":
            total = sum(expense["amount"] for expense in session_expenses)
            print(f"Total Expenses: ${total}")
        case "4":
            break
            print("\033[H\033[J", end="")
        case _:
            print("Please choose between 1-4.")
    
# Save the session expenses back to the JSON file
with open(DATA_FILE, "w") as f:
    json.dump(session_expenses, f, indent=4)


