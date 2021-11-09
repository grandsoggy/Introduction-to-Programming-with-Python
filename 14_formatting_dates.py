# This program will get a date from user and format it, as specified.
# Note: Program will need an update after year 9999.


def main() :
   # Initialize variables.
   usrYear = ''
   usrMonth = ''
   usrDay = ''
   usrDate = ''

   # Greeting.
   print('\nHello, let\'s format a date.')

   # Get user information.
   usrYear = getYear()
   usrMonth = getMonth()
   usrDay = getDay(usrYear, usrMonth)
   usrDate = formatDate(usrDay, usrMonth, usrYear)

   # Print user-specified formatted date.
   print('\nDate:')
   print(usrDate)

   # Salutation.
   print('\nThank you, goodbye.\n')

   return


# Function to collect a valid year value from user.
def getYear() :
   # Initialize variables.
   year = input('Year(yyyy): ')

   # Check for valid year value.
   while (int(year) < 0) or (int(year) > 9999):
      print('Please enter a valid year between 0000 and 9999.')
      year = input('Year(yyyy): ')

   # Check formatting.
   if (len(year) == 1) :
      year = '000' + year
   elif (len(year) == 2) :
      year = '00' + year
   elif (len(year) == 3) :
      year = '0' + year

   return year


# Function to collect a valid month value from user.
def getMonth() :
   # Initialize variables.
   month = input('Month(mm): ')

   # Check for valid month value.
   while (int(month) < 1) or (int(month) > 12) :
         print('Please enter a valid month.')
         month = input('Month(mm): ')

   # Check formatting.
   if (len(month) == 1) :
      month = '0' + month

   return month


# Function to collect a valid day value from user.
def getDay(year, month) :
   # Initialize variables.
   day = input('Day(dd): ')

   # Check for valid day value.
   # Months with 31 days.
   if (month == '01') or (month == '03') or (month == '05') or (month == '07') or \
      (month == '08') or (month == '10') or (month == '12') :
      while (int(day) < 1) or (int(day) > 31) :
         print('Please enter a valid day.')
         day = input('Day(dd): ')
   # Months with 30 days.
   elif (month == '04') or (month == '06') or (month == '09') or (month == '11') :
      while (int(day) < 1) or (int(day) > 30) :
         print('Please enter a valid day.')
         day = input('Day(dd): ')
   # Months with 29 days.
   elif (month == '04') or (month == '06') or (month == '09') or (month == '11') :
      while (int(day) < 1) or (int(day) > 29) :
         print('Please enter a valid day.')
         day = input('Day(dd): ')
   # February handling; month == '02'.
   else :
      # Check for leapyear.
      if (float(year) % 4 == 0) :
         while (int(day) < 1) or (int(day) > 29) :
            print('Please enter a valid day.')
            day = input('Day(dd): ')
      else :
         while (int(day) < 1) or (int(day) > 28) :
            print('Please enter a valid day.')
            day = input('Day(dd): ')

   # Check formatting.
   if (len(day) == 1) :
      day = '0' + day

   return day


# Function to allow user to specify which format to use.
def formatDate(day, month, year) :
   # Initialize variables.
   format = ''
   date = ''

   # Get user-preferred format.
   print('\nChoose format:')
   print('(a) mm/dd/yyyy')
   print('(b) dd/mm/yyyy')
   format = input().lower()
   # Check valid input.
   while (format != 'a') and (format != 'b') :
      print('Please choose from the list.')
      format = input().lower()

   if (format == 'a') :
      date = month + '/' + day + '/' + year
   else :
      date = day + '/' + month + '/' + year

   return date


main()