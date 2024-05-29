import color
from expenses import add_expenses, view_expenses, view_summary,delete_entry
import re
from collections import defaultdict
from tabulate import tabulate


def validate_date(date):
    # Define a regular expression pattern for YYYY-MM-DD format
    pattern = r'\d{4}-\d{2}-\d{2}'
    if re.match(pattern, date):
        return True
    else:
        print(f"{color.RED}Invalid date format. Please enter date in YYYY-MM-DD format.{color.RESET}")
        return False

def validate_amount(amount):
    # Check if amount is a valid float number
    try:
        float(amount)
        return True
    except ValueError:
        print(f"{color.RED}Invalid amount format. Please enter a valid number.{color.RESET}")
        return False
    

def main ():
    name = input(f"{color.YELLOW} What is your name? {color.RESET}")
    print(f"{color.GREEN} welcome {name} to your Personal Expense Tracker")
    while True:
        print("1  Add expense")
        print("2  View expense")
        print("3  Summarize Weekly expenses")
        print("4 Delete a category" )
        print("5 Exit")
        choice = input(f"{color.YELLOW} Please choose an option from the menu above: {color.RESET}")

        if choice == "1":
            date = input(f"{color.YELLOW} Enter date (YYYY-MM-DD):{color.RESET}")
            while not validate_date(date):
                    date = input(f"{color.YELLOW}Enter date (YYYY-MM-DD): {color.RESET}")
            category = input(f"{color.YELLOW} Enter category: {color.RESET}")
            amount =input(f"{color.YELLOW} Enter amount: {color.RESET}")
            while not validate_amount(amount):
                    amount = input(f"{color.YELLOW}Enter amount: {color.RESET}")
            description =input(f"{color.YELLOW} Enter description: {color.RESET}")
            add_expenses(date,category,amount,description)
            break


        elif choice == "2":
            headers, data_values = view_expenses() 
            if headers and data_values:
                print(tabulate(data_values, headers=headers, tablefmt="grid"))
                print(f"{color.GREEN} Viewed expenses successfully{color.RESET}")
            else:
                 print(f"{color.RED} No expenses found.{color.RESET}")  
            break
        

        elif choice == "3":
            summary = view_summary()
            if summary:
                summary_list = [[category, amount] for category, amount in summary.items() ]
                print(tabulate(summary_list, headers=["Category", "Amount"], tablefmt="grid"))
                print (f"{color.GREEN} summarized expenses successfully")
            break


        elif choice == "4":
             headers, data_values = view_expenses()
             if headers and data_values:
                print(tabulate(data_values, headers=headers, tablefmt="grid"))
                delete_item = input(f"Enter category to be deleted from above: {color.RESET}")
                delete_entry(delete_item)
             break
        
        elif choice == "5":
            print (f"{color.GREEN} Exiting....")
            break
        
        else:
            print (f"{color.RED} Invalid option, Please pick an option from the menu.")



# note here that In this case, main() will only be executed if the script is run directly. If the script is imported as a module into another script, main() won't be automatically executed, 
# allowing the importing script to use the functions and classes defined in the imported script without running the main program logic.
if  __name__ == "__main__":
    main()
