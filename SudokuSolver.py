# First - Import the puzzle as a list.
puzzle = list("000079065000003002005060093340050106000000000608020059950010600700600000820390000")
n = range(1,10) # Set the range of numbers we are looking for (1 - 9)
note = [] # empty list to note the places that we find blanks
possibles = [] # create an empty list of possibles that we'll use throughout

# Define a variable that we can use to count iterations throughout
x = 0
# Print the puzzle in a nice format:
print("You have imported the following puzzle:")
while x <= (9*9)-1: # This just tells it when to stop looping
    y = x + 9 # created y as a counter
    print(puzzle[x:y]) # The actual print command
    x += 9 # Go to the next line
print("- " * 100)
x = 0 # reset our counters
y = 0 # reset our counters

# Then; ask the user what the blanks are represented as, and make it a variable:
b = "0" # Use the following for input: input("What are the blank spaces represented as in this puzzle? ")
# Let's find the blanks and put all possible integers in, before starting to look at other numbers
while x <= (9*9)-1: # same loop as earlier
    if b in puzzle[x]: # if the character for a blank is in that piece:
        del puzzle[x]  # delete that piece
        puzzle.insert(x, range(1,10)) # then insert the range of numbers it could be (1 - 9)
        note.append(x)
        x += 1 # add 1 to x to continue the loop
    else:
        x += 1 # else, skip that space and move to the next one
# - Print out the numbers that have been found to be blanks:
print("Blanks are at the following locations, and under variable 'note': ")
print(note)
print("- " * 100)

#### Print out again
#### Print out again
#### Print out again
#### Print out again - puzzle should be the same with blanks replaced w/ arrays
""" print("The puzzle now looks like: ")
x = 0
while x <= (9*9)-1: # This just tells it when to stop looping
    y = x + 9 # created y as a counter
    print(puzzle[x:y]) # The actual print command
    x += 9 # Go to the next line
print("- " * 100)"""

# Function to find the numbers that could be on each blank on the horizontal (based just on that line)
def horicheck(x):
    l = x # define a variable for the Lower of the range
    h = l + 8 # define a variable for the Higher of the range
    while x <= h: # if x is on the top line
        if str(n[x]) not in puzzle[l:h]: # if the number isn't in the line, it's a possible
            possibles.append(n[x])
            x += 1
        else: # if the number is in the line, it's not a possible.
            x += 1 # so just move on to the next one

# Function to add the numbers onto the line that we have found
def horiadd(x):
    l = x # Lower - set the boundaries again
    h = l + 8 # Higher boundary
    while note[l] <= h:
        del puzzle[note[l]]  # delete that piece
        puzzle.insert(note[l], possibles) # then insert the range of numbers it could be
        print("the following location has been amended: " + str(note[l]) + " with the following string: " + str(possibles))
        l += 1

# Now execute the functions:
x = 0
horicheck(x)
print("The following numbers are 'possibles' on line " + str(x) + " (based only on this row): " + str(possibles))
print("- " * 100)
horiadd(x)
print("- " * 100)
