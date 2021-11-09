# This program will find and open a file. If the file cannot be found, an error will be output to user.
import sys
import csv


def main() :
   # Greeting.
   print('\nHello, let\'s open a file.')

   openFile()

   # Salutation.
   print('\nThank you. Goodbye.\n')

   return


# Function opens, and reads from, user-specified file.
def openFile() :
   # Initialize variables.
   READ = 'r'
   dataFromFile = []
   path = getPath()
   errorFlag = True

   # Error handling.
   while (errorFlag == True) :
      try :
         with open(path, mode = READ) as file :
            dataFromFile = csv.reader(file)

            # Print file content.
            print('\nFile content:')
            for currItem in dataFromFile :
               print(currItem)
  
         errorFlag = False
      # Handle specific file error encountered while testing.
      except FileNotFoundError:
         print('\nError: No such file. Make sure your file name is correct.\n')

         # Allow user to try an alternative file entry.
         path = getPath()
         errorFlag = True
      # Handle specific directory error encountered while testing.
      except IsADirectoryError:
         print('\nError: No such file or directory. Make sure your path is correct.\n')

         # Allow user to try an alternative path entry.
         path = getPath()
         errorFlag = True
      except :
         print('Something went wrong:')
         print(sys.exc_info()[0])

         # Exit program.
         sys.exit()
      
   return


# Function collects file path from user.
def getPath() :

   print('Please enter the path to the file you would like to access. (\'q\' to quit)')
   path = input('PATH: ')

   # Allow user to end program.
   if (path == 'q') :
      sys.exit()

   return path


main()