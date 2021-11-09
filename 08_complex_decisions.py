# This program will calculate Canadian taxes.

# Initialize variables.
orderTotal = 0.00
country = province = "NONE"

# Get user order total.
orderTotal = float(input("Order Total: $"))
# Get user country.
print ("\nWe're glad you're shopping with us!")
print ("What country are you ordering from?")
country = input().upper()

# Charge additional tax for respective province in Canada
if country == "CANADA" :
   print ("Which province?")
   province = input().upper()

   if province == "ALBERTA" :
      print ("\n+GST 0.05%")
      orderTotal += (orderTotal * 0.0005)
   elif province == "ONTARIO" or province == "NEW BRUNSWICK" \
      or province == "NOVA SCOTIA" :
      print ("\n+HST 0.13%")
      orderTotal += (orderTotal * 0.0013)
   else :
      print ("\n+PST 0.06%")
      print ("\n+GST 0.05%")
      orderTotal += (orderTotal * 0.0011)

# Print total charge.
print ("\nTotal Charges: $" + str("{:.2f}" .format(orderTotal)))
print ("Thank you!")
