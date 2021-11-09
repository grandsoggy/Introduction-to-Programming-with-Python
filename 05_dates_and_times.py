import datetime

# Initialize today's.
currentDate = datetime.date.today()

# Get user input.
print ("Hello, what date is your assignment due? (mm/dd/yyyy)")
dueDate = input()
# Format user input.
dueDateFormatted = datetime.datetime.strptime(dueDate, "%m/%d/%Y").date()

# Caluclate time remaining.
timeDifference = dueDateFormatted - currentDate
# Calculate total days remaining.
daysRemainingTotal = timeDifference.days
# Calculate spare days after weeks are subtracted.
daysRemaining = int(daysRemainingTotal) % 7
# Calculate weeks remaining.
weeksRemaining = (daysRemainingTotal - daysRemaining) / 7

# Output statement.
print ("\nYou have " + str(int(weeksRemaining)) + " weeks and " + str(daysRemaining) + \
   " days until your assignment is due.")