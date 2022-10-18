amount_due=50

while amount_due > 0 :
    print("Amount Due:",amount_due)
    coin=int(input("Insert Coin: "))
    if coin in [25,5,10]:
        amount_due=amount_due-coin
    else:
        print("Wrong Coin")
        break
#The Python abs() function return the absolute value and remove the negative sign of a number in Python.

change=abs(amount_due)
print("Change Owed:",change)
