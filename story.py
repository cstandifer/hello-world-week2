Python Madlib:

# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your poems info
month = input("Enter your favorite month: ")
animal = input("What is your favorite animal?: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
verb1 = input("A verb ending in ing that is something you enjoy: ")
place = input("A place in nature you enjoy: ")
verb2 = input("An action verb: ")
verb3 = input("Another action verb: ")
verb4 = input("One last action verb: ")
season = input("Season your favorite month is in: ")


poem = month + " is a " + animal + "'s " + "dream\n" \
"the " + adjective1 + " grass is growing\n" \
"the " + adjective2 + " breeze is blowing\n" \
"the air all full of " + verb1 + " feels just right\n" \
"so no excuses now\n" \
"we're going to the " + place + "\n" \
"to " + verb2 + " and " + verb3 + " and " + verb4 + "\n" \
"and I will make you see\n" \
"what " + season + " is all about"

print(poem)
