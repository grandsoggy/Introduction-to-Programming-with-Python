# This program will translate the abbreviated phrases used in text messages to plain english.
import csv


def main() :
   # Initialize variables.
   usrText = ''

   # Greeting.
   print('\nHello, what would you like translated? ("q" to quit)')

   # Get user information.
   usrText = input('Text: ')

   getTranslation(usrText)

   # Salutation.
   print('\nThank you, goodbye.\n')

   return


# Function prints the translation of the user-specified text.
def getTranslation(text) :
   # Initialize variables.
   READ = 'r'
   PATH = '/Users/<username>/ALISON MODULES/15_translations.csv'
   fileDataList = []
   locatedFlag = False

   while (text != 'q') :
      # Open file and copy to a list.      
      with open(PATH, mode = READ) as translations :
         fileDataList = csv.reader(translations)

         for currLine in fileDataList :
            if (currLine[0] == text.upper()) :
               locatedFlag = True
               print(': '.join(currLine))
      
      # User input not found in data.
      if not locatedFlag :
         print('\n' + text + ' not recognized.')
         print('\nWould you like to try another? ("q" to quit)')
         text = input('Text: ')
      # Reset condition.
      else :
         print('\nContinue? ("q" to quit)')
         text = input('Text: ')
         locatedFlag = False

   return


main()