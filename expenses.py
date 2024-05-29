import color
import os
import expenses_data
from collections import defaultdict
from expenses_data import DATA

def save_data(data):
    with open("expenses_data.py", mode="w") as file:  
        file.write("DATA = [\n")
        for entry in data:
            file.write(f" \n{entry},\n")
        file.write("]\n")


def add_expenses(date, category, amount, description):
    global DATA
    expense = {
            "date" : date,
            "category" : category ,
            "amount": amount,
            "description" : description
        }
    try:
        DATA.append(expense)
        print(f"{color.GREEN} \nExpenses added successfully. {color.RESET}")
        save_data(DATA)

    except Exception as e:
         print(f"{color.RED} \nAn unexpected error occured: {e}")


def view_expenses():
     headers = list(DATA[0].keys())
     data_values = [list(expense.values()) for expense in DATA]
     return headers,data_values

def view_summary():
    summary_record = defaultdict(float)
    for expense in DATA:
        category = expense['category']
        amount =  float(expense['amount'])
        summary_record[category] += amount
    return (summary_record)

def delete_entry(category):
    global DATA
    initial_length = len(DATA)
    DATA = [expense for expense in DATA if expense['category'] != category]
    final_length = len(DATA)
    if (initial_length == final_length):
        print(f"{color.RED}No expenses found for category '{category}'.{color.RESET}")
    else:
        save_data(DATA)
        print (f"{color.GREEN}Expenses with category '{category}' have been deleted.{color.RESET}")

