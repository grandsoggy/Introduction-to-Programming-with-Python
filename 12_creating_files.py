# This program will create a .csv file.

# Initialize variables.
path = '/Users/<username>/ALISON MODULES/FILES/file.csv'
WRITE = 'w'

# Create and write to .csv file.
with open(path, WRITE) as f :
   f.write('Doyle McCarty, 27\n')
   f.write('Jodi Mills, 25\n')
   f.write('Nicholas Rose, 32\n')
   f.write('Kian Goddard, 36\n')
   f.write('Zuha Hanania, 26')

# Salutation.
print('\n\'creating_files.csv\' was successfully created.')
print('Thank you, goodbye.\n')
