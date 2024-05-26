import csv
import color
import os
from collections import defaultdict

DATA = "data/expenses_data.csv"

def add_expense(date, category, amount, description):
    try:
        with open(DATA, mode="a") as file:
            writer = csv.writer(file)
            writer.writerow([date,category,amount,description])
            print(f"{color.GREEN} Expenses added successfully")
    except IOError as e:
        print(f"{color.RED} An IOError occured: {e}")
    
    except Exception as e:
         print(f"{color.RED} An unexpected error occured: {e}")


def view_expenses():
    expenses = []
    if os.path.exists(DATA):
        with open(DATA , mode="r") as file:
            reader = csv.reader(file)
            expenses = list(reader)
        return expenses
    

def view_summary():
    summary_record = defaultdict(float)
    if os.path.exists(DATA):
        with open(DATA, mode="r") as file:
             reader = csv.reader(file)
             for row in reader:
                category = row[1]
                amount = float(row[2])
                summary_record[category] += amount
        return summary_record


def delete_entry(category):
    with open(DATA, mode= "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    # Iterate over the data and remove the entry with the specified date
    modified_data = [row for row in data if row[1] != category]
    with open(DATA, mode="w") as file:
            writer = csv.writer(file)
            writer.writerows(modified_data)      
    return modified_data

