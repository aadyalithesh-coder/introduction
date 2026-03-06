Actual_price=float(input("Enter actual price:"))
Sales_amount=float(input("Enter sales amount:"))
if Sales_amount>Actual_price:
    profit=Sales_amount-Actual_price
    print("Profit of",profit)

else :
    print("loss")
