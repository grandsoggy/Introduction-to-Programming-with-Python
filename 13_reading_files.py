# This program will print the data contained in a .csv file.

import csv

# Initialize variables.
path = '/Users/<username>/ALISON MODULES/FILES/file.csv'
READ = 'r'


# Greeting.
print('\nHello, the data in the file is:\n')
# Access file.
with open(path, mode = READ) as f :
   dataFromFile = csv.reader(f)

   for currRow in dataFromFile :
      print(', '.join(currRow))

# Salutation
print('\nThank you, goodbye.\n')
