# This program will allow users to draw using the 'turtle' module, by
# specifying line legnths, angles and colors.
import turtle

# Initialize variables.
length = '0'
direction = 'right'
angle = '0'
color = 'black'


# Greeting.
print('\nHello, let\'s begin drawing!')
# Initialize drawing.
turtle.forward(0)

# Get user input.
print('Please enter the following: (Set Length: 0 to quit.)')
length = input('Length: ')
# Check length != 0.
while length != '0' :
   color = input('Color: ').lower()
   direction = input('Turn left or right: ')
   angle = input('Angle: ')

   # Call 'turtle' module to draw the user-specified line.
   # Change pen color.
   turtle.pencolor(color)
   # Check whether directionis left or right.
   if direction.lower() == 'right' :
      turtle.right(int(angle))
   else :
      turtle.left(int(angle))
   # Draw line
   turtle.forward(int(length))

   # Re-set loop condition.
   length = input('\nLength: ')

# Salutation.
print('\nThank you, goodbye.')
