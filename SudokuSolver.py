# First - Import the puzzle as a list.
debug = 1 # Debug for printing! (Thanks Dom)
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
    print(str(x/9) + ": " +str(puzzle[x:y]) + "     " + str(range(x,y))) # The actual print command
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
if debug == 1:
    print("Blanks are at the following locations, and under variable 'note': ")
    print(note)
    print("- " * 100)
    print("START WITH ROW 0: ")

# Function to find the numbers that could be on each blank on the horizontal (based just on that line)
def check(l):
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
    if debug == 1:
        print("the possibilities for this row, based just on this row, are: " + str(possibles))
# Function to add the numbers onto the line that we have found
def horiadd(x, l):
    if debug == 1:
        print("Lets add the possibilities to the row just analysed: ")
    if x + 9 > 80:
        h = 80
    else:
        h = x + 9 # Higher boundary
    while note[l] < h:
        del puzzle[note[l]]  # delete that piece
        puzzle.insert(note[l], possibles) # then insert the range of numbers it could be
        if debug == 1:
            print("the following location has been amended: " + str(note[l]) + ". the following list has been added in it's place: " + str(possibles))
        l += 1

# Now execute the functions:
x = 0 # reset the counter
e = x # e is used as the index number of the next blank in the 'note' variable
q = x # q is used as another counter, but this time it's for the 'note' variable; so IF the number at the start of a row isn't a blank; we can check for the next number.
while x <= 9*8: # while x is in low enough to look at the rows
    if q not in note: # if the number at the start of the row isn't blank - look for the next plank
        q += 1 # by adding 1 to q
    else:
        e = int(note.index(q)) # use the integer!
        check(x) # call the function defined earlier
        horiadd(x, e) # call the other function defined earlier
        possibles = [] # clear our the possible number variable each time after you've added the numbers
        x += 9 # go to the next row
        q = x # refresh q to be the number of the start of the next row
        d = (note[e]/9) + 1 # d is just to say what row we are starting on next
        if debug == 1:
            print("- " * 100)
        if int(d) < 9:
            if debug == 1:
                print("MOVING TO ROW: " + str(d))
        else:
            break # finish"""

####
#### NOW MOVE ONTO VERTICALS
####
def verticheck (l):
        x = 0 # define a variable for the counter
        y = 1
        while x <= 8: # to make sure we stay on one horizontal line
            if str(y) not in puzzle[l:h]: # if the number isn't in the line, it's a possible
                possibles.append(n[x])
                x += 1
                y += 1
            else: # if the number is in the line, it's not a possible.
                x += 1 # so just move on to the next one
                y += 1
        if debug == 1:
            print("the possibilities for this row, based just on this row, are: " + str(possibles))

### This is looking at the columns/verticals
c = 0 # this is a variable for the column number
notpossibles = [] # create a not - possibles variable
possibles = [] # empty the possibles variable
for c in range (0, 9, 1): # create a loop to do this 9 times over
    notpossibles = [] # clear out the not possibles variable for the following loop
    possibles = [] # clear out the possibles variable for the following loop
    if debug == 1:
        print("MOVE TO COLUMN: " + str(c))
    for c in range (c, 81, 9): # this is the loop to ensure we only look at the verticals together
        for x in range(1, 10, 1): # this loop is each integer we are looking for on the vertical
            if str(x) in puzzle[c]: # if the x is in the puzzle at the point (c) we are looking at
                if debug == 1:
                    print(str(x) + " is in the puzzle at point: " + str(c))
                notpossibles.append(x) # add the number that is in the column to the not possibles
    if debug == 1:
        print("The following numbers are on column " + str(c-72) + ": " + str(notpossibles))
    for x in range(1, 10, 1): # loop to add possibles
        if x not in notpossibles: # if the number isn't in the not-possibles
            possibles.append(x) # add the number to the possibles variable
                #
                #
                #
                # This is where we add the logic to narrow down the numbers
                #
                #
                #
    if debug == 1:
        print("Leaving the following numbers as possibles: " + str(possibles))
    if debug == 1:
        print("- " * 100)

### This is looking at blocks
b = [0, 3, 6, 27, 30, 33, 54, 57, 60] # this is the block starting points
x = 0 # this is the variable for the start of the block
c = 0 # this is the index of the puzzle compared to c
i = 0 # this is just to run through each block
notpossibles = [] # create a not - possibles variable
possibles = [] # empty the possibles variable
for i in range (0, 9, 1):
    x = b[i]
    if debug == 1:
        print("BLOCK START LOCATION: " + str(x))
    for x in range (x, x + 19, 9): # This is a single block, where x is the starting point
        for c in range (0, 3, 1): # This is to make sure it's just going through 3 places
            for h in range (1, 10, 1):
                if str(h) in puzzle[c + x]:
                    notpossibles.append(h)
                    if debug == 1:
                        print(str(h) + " is in the puzzle at point: " + str(c + x))
            #
            # This is where we put the block stuff
            #
            #
        x += 9 # jump to the next row
    print("- " * 100)
