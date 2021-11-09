# Variable declaration/initialization.
loanAmt = 0.00
interestRate = 0.00
years = 0.00
monthlyPaymnt = 0.00

# Get user info.
print ("\nHello, welcome to the loan calculator.")
print ("\nWhat is the total amount of your loan?")
loanAmt = input()
print ("What is the interest rate on your loan (enter X% as a decimal 0.0X?")
interestRate = input()
print ("How many years will it take to pay off your loan?")
years = input()

# Calculate monthly payment.
monthlyPaymnt = float(loanAmt) * ((float(interestRate) * (1 + float(interestRate)) * float(years)) \
   / (((1 + float(interestRate)) * float(years)) - 1))

# Output monthly payment amount to user.
print ("\nYour monthly payment is: ${0:.2f}" .format(monthlyPaymnt))
print ("\nThank you!\n")
