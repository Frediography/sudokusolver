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
x = 0 # reset the counters used
y = 0 # reset the counters used

print("----------------------------------------")
print("Blanks at locations (of note): ")
print(note)
print("----------------------------------------")

#    while note != []: # This function keeps iterating until we have no unknowns left.

# Function to take out numbers that are on the horizontal
l = 0 # define a variable for the lower of the range
h = 0 # define a variable for the higher of the range
while x <= 8: # if x is on the top line
    l = 0
    h = 8
    if str(n[x]) not in puzzle[l:h]: # if the number isn't in the line, it's a possible
        possibles.append(n[x])
        x += 1
    else: # if the number is in the line, it's not a possible.
        x += 1 # so just move on to the next one

# Now we need to find out where to add these to.
#del puzzle[x]  # delete that piece
#puzzle.insert(x, range(1,10)) # then insert the range of numbers it could be (1 - 9)

print("the following are possible numbers for the gaps at the top:")
print(possibles)
print("----------------------------------------")
while note[y] <= 8: # so; this is to make sure we're not going beyond the top line
    del puzzle[note[y]]  # delete that piece
    puzzle.insert(note[y], possibles) # then insert the range of numbers it could be
    print("the following location has been amended: " + str(note[y]))
    print(puzzle)
    y += 1
y = 0
z = 0
print(len(puzzle))
print(puzzle)
print("----------------------------------------")
print(note)
print("----------------------------------------")
while x <= (9*9)-1: # This just tells it when to stop looping
    y = x + 9 # created y as a counter
    print(puzzle[x:y]) # The actual print command
    x += 9 # Go to the next line
x = 0 # reset our counters
y = 0 # reset our counters
