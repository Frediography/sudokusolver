# First - Import the puzzle as a list.
puzzle = list("000079065000003002005060093340050106000000000608020059950010600700600000820390000")
n = range(1,10) # Set the range of numbers we are looking for (1 - 9)
note = [] # empty list to note the places that we find blanks
possibles = [] # create an empty list of possibles that we'll use throughout

# Define a variable that we can use to count iterations throughout
x = 0
# Print the puzzle in a nice format:
print("You have imported the following puzzle:           The positions on the board will be referred to as:")
while x <= (9*9)-1: # This just tells it when to stop looping
    y = x + 9 # created y as a counter
    print(str(puzzle[x:y]) + "     " + str(range(x,y))) # The actual print command
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

# Function to find the numbers that could be on each blank on the horizontal (based just on that line)
def horicheck(l):
    x = 0 # define a variable for the counter
    h = l + 9 # define a variable for the Higher of the range
    y = 1
    while x <= 8: # to make sure we stay on one horizontal line
        if str(y) not in puzzle[l:h]: # if the number isn't in the line, it's a possible
            possibles.append(n[x])
            x += 1
            y += 1
        else: # if the number is in the line, it's not a possible.
            x += 1 # so just move on to the next one
            y += 1
    print("the possibilities for this row, based just on this row, are: " + str(possibles))
# Function to add the numbers onto the line that we have found
def horiadd(x, l):
    print("Lets add the possibilities to the row just analysed: ")
    h = x + 9 # Higher boundary
    while note[l] < h:
        del puzzle[note[l]]  # delete that piece
        puzzle.insert(note[l], possibles) # then insert the range of numbers it could be
        print("the following location has been amended: " + str(note[l]) + ". the following list has been added in it's place: " + str(possibles))
        l += 1

# Now execute the functions:
x = 0
e = x
horicheck(x)
horiadd(x, e)
possibles = [] #clear out this stream
x += 9
print("- " * 100)
horicheck(x)
e = int(note.index(x))
horiadd(x, e)
possibles = [] #clear out this stream
print("- " * 100)
x += 9
horicheck(x)
e = int(note.index(x))
horiadd(x, e)
