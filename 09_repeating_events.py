# This program will use the 'turtle' module to draw a shape.
import turtle

# Define variables.
sides = 0
userResponse = 'n'


# Prompt user for shape.
print('\nHello, lets draw a shape!')
sides = input('Number of sides: ')

# Prompt user for smaller clone inside.
print('\nWould you like to add magic? (Y/n)')
userResponse = input()

# Draw shape; each side length = 40.
for steps in range(0, int(sides)) :
   turtle.forward(40)
   turtle.right(360 / int(sides))
   # Draw smaller clone inside; each side length = 10.
   if userResponse == 'Y' :
      for steps in range(0, int(sides)) :
         turtle.forward(10)
         turtle.right(360 / int(sides))
turtle.mainloop()

# Salutation.
print('\nThank you.\n')
