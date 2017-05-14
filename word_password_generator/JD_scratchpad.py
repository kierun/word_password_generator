# Add user input here for file path & name, also for whether they want a 4, 5 or 6 word password
# Check for 'file exists', can we also check for valid format (UTF-8)?
import magic
from pathlib import Path

print('Please enter the path to the word list file:')
file_path_input = input()
file_path = Path(file_path_input)
if file_path.is_file():
    file_test = open(file_path).read()
    m = magic.open(magic.MAGIC_MIME_ENCODING)
    m.load()
    encoding = m.buffer(file_test)
    if(encoding != 'utf-8'):
        print('File is not UTF-8 encoding, please try again...')
        exit
elif(not file_path.is_file()):
    print('File not present at specified location, please try again...')
    exit

    

# Apparently this should open the file, stream out the contents as asked for then closes the file?
# Tried just loading the whole file into memory, but it crapped out, so we'll do this
with open(file_path) as datafile:
    words = (word.rstrip('\r\n') for word in datafile)
    desiredWords = list()
    for word in words:
        if(len(word) <=6 and len(word) >= 4):
            # Try adding the filtered word list to an array of strings?
            desiredWords.append(word)
    for desiredWord in desiredWords:
        print(desiredWord)
    print(str(len(desiredWords)))
        # Here, maybe get the string-array length and feed that in as the top end of a random number generator
        # Use user-input for number of words desired to cycle through the array and pick random words out

