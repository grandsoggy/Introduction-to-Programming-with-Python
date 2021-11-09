# This program will create and write to a file using functions to simplify the code.


def main() :
   # Initialize variables.
   WRITE = 'w'
   dataList = []
   path = '/Users/<username>/ALISON MODULES/FILES'
   fileName = ''

   # Greeting.
   print('\nHello, let\'s create a file.')

   fileName = getFileName()
   dataList = getFileData()

   # Update the path to include the user-specified file name.
   path = path + '/' + fileName
   # Create/open the file.
   with open(path, mode = WRITE) as f :
      # Check list is not empty.
      if len(dataList) > 0 :
         # Write the user-specified data in the list to the file, line by line.
         # Check if list is just 1 item long.
         if len(dataList) == 1 :
            f.write(dataList[0])
         
         else :
            for currItem in range(len(dataList) - 1) :
               f.write(dataList[currItem] + '\n')
            # Eliminates the inclusion of a new line at the end of file.
            f.write(dataList[currItem + 1])

   # Salutation.
   print('\nThank you, goodbye.\n')

   return

# Function to collect a user-specified name of file.
def getFileName() :
   # Initialize variables.
   fileName = ''

   # Collect user information.
   print('File name:')
   fileName = input()

   return fileName

# Function to collect user-specified data to fill a file with.
def getFileData() :
   # Initialize variables.
   dataList = []
   currData = ''

   # Collect user information until user is finished.
   print('\nFile content: (\'f\' to finish)')
   currData = input()

   while currData != 'f' :
      # Add user entry to list.
      dataList.append(currData)
      # Update user entry.
      currData = input()

   return dataList

main()