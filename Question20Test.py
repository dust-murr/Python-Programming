def calcNetIncome(revenue, expenses):
    netIncome = revenue - expenses 
    return netIncome

def main():
    revenue = float(input("Please enter the total revenue: "))
    expenses = float(input("Please enter the total expenses: "))
    netIncome = calcNetIncome (revenue, expenses)
    print("The total net income is: $" ,netIncome)

main()
