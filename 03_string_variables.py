# Get user name.
print ("Hello! Lets write a love letter.\nWhat is your name?")
userName = input()
# Greeting
print ("\nHi, " + userName + "!")
print ("To get a better idea of who I'm writing for, please")
print ("provide some answers to the following questions.")
print ("Some things to keep in mind while answering:")
print (" -Read the questions thoroughly.")
print (" -Only capitalize names.")
print (" -Don't include any unnecessary spaces in your answers.")
print (" -Have a little fun with it!")
# Get user info.
print ("\nWhat is your favorite animal?")
animal = input()
print ("What is your singular favorite thing to receive?")
noun3 = input()
print ("Your second singular favorite thing to receive?")
noun4 = input()
print ("Your favorite sensory organ? (eyes/ears/nose/tongue/skin)")
bodyPart1 = input()
print ("Your favorite body part?")
bodyPart2 = input()
print ("Your favorite number?")
number1 = input()
print ("Your second favorite number?")
number2 = input()
print ("Your favorite singular thing to see?")
noun5 = input()
print ("And your favorite singular thing to do?")
verb2 = input()
# Get user fillers.
print ("\nNow, still with yourself in mind, give me;")
print ("A fragrant noun:")
noun1 = input()
print ("An action verb:")
verb1 = input()
print ("Another action verb:")
verb3 = input()
print ("Another [verb]:")
verb6 = input()
print ("And another [verb]:")
verb7 = input()
print ("An adverb: (adjective + \"ly\")")
adverb1 = input()
print ("Another [adverb]:")
adverb2 = input()
print ("And one more [adverb]:")
adverb3 = input()
# Capitalize adverb for closer.
adverb3 = adverb3.upper()
print ("A past-tense verb: (verb + \"ed\")")
verb4 = input()
print ("And one last past-tense verb:")
verb5 = input()

# Get partner info.
print ("\nNow, what is the name of your lover?")
loverName = input()
print ("What adjective would you use to describe them?")
adjective1 = input()
print ("What is a second adjective you would use to decribe them?")
adjective2 = input()
print ("How about one [adjective] that ends in -\"ness\"?")
adjective3 = input()
print ("What is something that they have, that you want?")
noun2 = input()
print ("What is something, a word, a phrase, that they say often.")
phrase = input()

# Thank you message.
print ("\nThank you! Your letter has been created.")
filler = input("Enter 'v' to view it now!  ")

# Story print-out.
print ("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Header.
print ("\nDear " + loverName + ",")
# New paragraph.
print ("\n   When we first met, you looked " + adjective1 + " and " + adjective2 + ".")
print ("I couldn't believe my " + bodyPart1 + "! You smelled like " + noun1 + " and walked")
print ("as graceful as a " + animal + ". I couldn't wait to " + verb1 + " to you.")
# New paragraph.
print ("\n   I " + adverb1 + " asked you if I could have your " + noun2 + ". I could see")
print ("a look of " + adjective3 + " in your eyes. You hesitated for a moment,")
print ("then gave me a " + noun3 + ".")
# New paragraph.
print ("\n   I finally got to take you on our first date. I loved spending time")
print ("with you. You could make me " + verb2 + " so easily, like no one")
print ("had before. When you touched me, I felt " + noun4 + " up my")
print (bodyPart2 + ". When you looked at me, I could see")
print (noun5 + ". I knew we were meant to be together.")
# New paragraph.
print ("\n   After that " + adverb2 + " night, I was so close to bringing you")
print ("home. I longed to " + verb3 + " you again. You looked at me and")
print ("said, '" + phrase + "' and I just knew. You " + verb4)
print ("me and I " + verb5 + " you.")
# New paragraph.
print ("\n   Here we are after all this time. It feels like it's been")
print (number1 + " years! I look forward to " + number2 + " more.")
print ("You make me want to " + verb6 + " and I will " + verb6 + " you")
print ("forever. Nobody else could " + verb7 + " me, like you do.")
# Closer.
print ("\n\n" + adverb3 + " yours,")
print (userName + " <3")
print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")