import datetime
import json 
import matplotlib.pyplot as plt


expenses = []

def load_expenses():
  try:
    with open('expenses.json','r') as f:
      return json.load(f)
  except FileNotFoundError:
    return[]



def save_expenses():

  with open('expenses.json','w')as f:
    json.dump(expenses,f)


def add_expense():
  while True:
    date_input = input("Enter the date (YYYY-MM-DD): ")
    try:
      date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
      break
    except ValueError:
      print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")


  amount= float(input("Enter the amount"))
  category = ["Food","Travel", "Enterainment", "Utilities","others"]
  print("Categories:", ",".join(category))

  if category not in category:
    print("Unknow Category, cagtegorizing as others")
    category = "others"


  description = input("Enter a description")



  expense = {
      'date' : str(date),
      'amount': amount,
      'category': category,
      'description': description
  }

  expenses.append(expense)
  save_expenses()
  print("Expense added successfully\n!")




def view_expenses():

  if not expenses:
    print("NO expenses recorded yet.\n")
    return

  filtere_expenses = expenses

  if filter_by =='date':
    start_date = input("Enter start date (YYYY-MM-DD) :")
    end_date = input("Enter end date(YYYY-MM-DD):")
    filtere_expenses = [expense for expense in expenses if start_date <= expense['date'] <= end_date]


  elif filter_by =='category':
    category = input("Enter category to filter by :")
    filtere_expenses = [expense for expense in expenses if expense['category'] == category]


  for expense in filtere_expenses:
    print(f"Date:{expense['date']}")
    print(f"Amount:{expense['amount']:.2f}")
    print(f"Category:{expense['category']}")
    print(f"Description:{expense['description']}\n")



def view_summary():
  total_amount = sum(expense['amount'] for expense in expenses)
  print(f"Total amount spent: ${total_amount:.2f}\n")


  categories = {}

  for expense in expenses:
    if expense['category'] in categories:
      categories[expense['category']]+= expense['amount']

    else:
      categories[expense['category']] = expense['amount']



    print("Spending by category")
    for category, amount in categories.items():
      print(f"{category}: £{amount:.2f}")


    plt.bar(categories.keys(),categories.values(), color='skyblue')
    plt.xlabel('Category')
    plt.ylabel("Amount spent")
    plt.title("Expenses by category")
    plt.show()



def set_budget():
  budget = float(input("Enter your budget"))
  total_spent = sum(expense['amount'] for expense in expenses)
  reamining_budget = budget - total_spent
  print(f"Total Spent £{total_spent:.2f}")
  print(f"Reamining Budget £{reamining_budget}")
  plt.pie([total_spent,reamining_budget], labels=['Spent', 'Remaining'], autopct='%1.1f%%')
  plt.title('Budget vs Spending')
  plt.show()


def main_menu():
  while True:
    print("Expense Tracker Menu:")
    print("1. Add expense")#
    print("2. View all expenses")
    print("3. View summary")
    print("4. Set Budget")
    print("5. Exit")
    choice = input("Choose an option:")
    if choice == '1':
      add_expense()
    elif choice =='2':
      view_expenses()

    elif choice =='3':
      view_summary()

    elif choice =='4':
      set_budget()

    elif choice =='5':
      print("Exiting the program.")
      break

    else:
      print("Invalid option, please try again.\n")


if __name__=="__main__":
  expenses = load_expenses()
  main_menu()
  save_expenses()





















  
