# This program calculates shipping charges for a shopper.

# Get shopper info.
print ("\nHello, please enter the total amount of your purchase:")
totalPurchase = float(input("$"))

# Add shipping fee.
if totalPurchase < 50.00 :
   print ("\nShipping will be an additional $10.00.")
   totalPurchase += 10.00
else :
   print ("\nShipping is free!")

# Output total cost.
print ("Your total is:\n$" + str("{:.2f}" .format(totalPurchase)))
