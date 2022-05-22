# Tip calculator
print("Welcome to the tip calculator")
bill = float(input("What is the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
percentage = (tip/100)*bill
people = int(input("How many people to split the bill? "))

payment = round((bill + percentage)/people, 2)
payment_format = "{:.2f}".format(payment)
print(f"Each person should pay: $ {payment_format}")
