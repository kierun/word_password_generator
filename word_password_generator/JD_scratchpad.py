# Add user input here for file path & name, also for whether they want a 4, 5 or 6 word password
# Check for 'file exists', can we also check for valid format (UTF-8)?

# Apparently this should open the file, stream out the contents as asked for then closes the file?
# Tried just loading the whole file into memory, but it crapped out, so we'll do this
with open('F:\Code\Python\Password_Gen\wordlist.10000.txt') as datafile: #hard-coded right now while I work things out
    words = (word.rstrip('\r\n') for word in datafile)
    for word in words:
        if(len(word) <=6 and len(word) >= 4):
            # Try adding the filtered word list to an array of strings?
            print(word)
        # Here, maybe get the string-array length and feed that in as the top end of a random number generator
        # Use user-input for number of words desired to cycle through the array and pick random words out

