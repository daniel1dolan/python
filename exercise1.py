# 1 Tip Calculator
# bill_amount = input("Total bill amount?" )
# service_qual = input("Level of service: good, fair, or bad?" )
# bill_amount = float(bill_amount)

# if service_qual == "good":
#     tip = bill_amount * 0.2
#     print("Tip amount: $" + "%.2f" % tip)
# elif service_qual == "fair":
#     tip = bill_amount * 0.15
#     print("Tip amount: $" + "%.2f" % tip)
# elif service_qual == "bad":
#     tip = bill_amount * 0.1
#     print("Tip amount: $" + "%.2f" % tip)
# else: 
#     print("You are not an elite Yelper.")

# total = bill_amount + tip
# print("Total amount: $" + "%.2f" % total)

#2 Tip Calculator 2
# bill_amount = input("Total bill amount?" )
# service_qual = input("Level of service: good, fair, or bad?" )
# num_splits = input("Split how many ways?" )
# bill_amount = float(bill_amount)
# num_splits = int(num_splits)

# if service_qual == "good":
#     tip = bill_amount * 0.2
#     print("Tip amount: $" + "%.2f" % tip)
# elif service_qual == "fair":
#     tip = bill_amount * 0.15
#     print("Tip amount: $" + "%.2f" % tip)
# elif service_qual == "bad":
#     tip = bill_amount * 0.1
#     print("Tip amount: $" + "%.2f" % tip)
# else: 
#     print("You are not an elite Yelper.")

# total = bill_amount + tip
# amt_per_person = total / num_splits
# print("Total amount: $" + "%.2f" % total)
# print("Amount per person: $" + "%.2f" % amt_per_person)

#3 Coins
# coins = 0
# while True:
#     print(f"You have {coins} coins.")
#     response = input("Do you want another?")
#     if response.lower() == "yes" or "y":
#         coins += 1
#     if response.lower() == "no" or "n":
#         print("Bye, have a beautiful time.")
#         break

#4 Box
# width = int(input("Width?"))
# height = int(input("Height?"))
# print("*" * width)
# for i in range((height - 2)):
#     print("*" + " " * (width - 2) + "*")
# print("*" * width)

#5 Triangle
# n = 7
# for i in range(n):
#     print(" " * (n-i-1) + "*" * (2*i+1))

#6 Multiplication Table
# for i in range(1, 11):
#     for n in range(1,11):
#         result = i * n
#         print(str(i) + " " + "X" + " " + str(n) + " = " + str(result))
        

    