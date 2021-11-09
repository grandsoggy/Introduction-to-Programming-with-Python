# This program will ask the user for a list of names, sort the list
# alphabetically, and print the sorted list.

# Initialize variables.
itemList = []
userEntry = ''


# Greeting.
print('\nHello, let\'s alphabetize your list.')
# Get user info.
print('Please press \'enter\' after each item, and \'f\' when finished.')
userEntry = input('1. ')

# Check user has not quit.
while userEntry != 'f' :
   # Update the list with user's entry.
   itemList.append(userEntry)

   # Get next item from user.
   userEntry = input(str(len(itemList) + 1) + '. ')

# Sort list alphabetically.
itemList.sort()

# Check list is not empty.
if len(itemList) > 0 :
   # Print sorted list.
   print('\nYour alphabetized list:')

   for currItem in itemList :
      print(str(itemList.index(currItem) + 1) + '. ' + currItem)

# Salutation.
print('\nThank you, goodbye.\n')
