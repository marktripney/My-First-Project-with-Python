# Write your code here
# print("Prices:\nBubblegum: $2\nToffee: $0.2\nIce cream: $5\nMilk chocolate: $4\nDoughnut: $2.5\nPancake: $3.2")

total_sales = 0
earnings = {
    'Bubblegum': 202,
    'Toffee': 118,
    'Ice cream': 2250,
    'Milk chocolate': 1680,
    'Doughnut': 1075,
    'Pancake': 80,
}

print("Earned amount:")
for item, sales in earnings.items():
    print(f'{item}: ${sales}')
    total_sales += sales

print(f"\nIncome: ${total_sales}")

staff_expenses = int(input("Staff expenses:\n"))
other_expenses = int(input("Other expenses:\n"))
total_expenses = staff_expenses + other_expenses

print(f"Net income: ${total_sales - total_expenses}")
