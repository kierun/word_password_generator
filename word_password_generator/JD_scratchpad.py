# Add user input here for file path & name, also for whether they want a 4, 5 or 6 word password
# Check for 'file exists', can we also check for valid format (UTF-8)?

# import magic # So, I tried to use this but for some reason it doesn't want to import...
from pathlib import Path
import sys
from random import randrange

print('How many words would you like in your password (4-6)?')
number_of_words = input()
while(int(number_of_words) < 4) or (int(number_of_words) > 6):
    print('That value is outside the accepted range (4-6), please try again:')
    number_of_words = input()

print('Please enter the path to the word list file:')
file_path_input = input()
file_path = Path(file_path_input)
if not file_path.is_file():
    print('File not present at specified location, please run again...')
    exit()

    

# Apparently this should open the file, stream out the contents as asked for then closes the file?
# Tried just loading the whole file into memory, but it crapped out, so we'll do this
with open(file_path) as datafile:
    words = (word.rstrip('\r\n') for word in datafile)
    desiredWords = list()
    for word in words:
        if(len(word) <=6 and len(word) >= 4):
            # Try adding the filtered word list to an array of strings?
            desiredWords.append(word)
    # Here, maybe get the string-array length and feed that in as the top end of a random number generator
    # Use user-input for number of words desired to cycle through the array and pick random words out
    list_length = len(desiredWords)
    output_list = list()
    for count in range(0, int(number_of_words)):
        selection = randrange(0, list_length, 1)
        new_word = desiredWords[selection]
        # print('Word number: ' + str(selection +1) + ', ' + new_word)
        while(new_word in output_list):
            # print('DUPLICATE!!!')
            selection = randrange(0, list_length, 1)
            new_word = desiredWords[selection]
            # print('Word number: ' + str(selection +1) + ', ' + new_word)
        output_list.append(new_word)
        count += 1
    for output_words in output_list:
        print(output_words, end=',')
    print('\nAre these words acceptable (Y/N)?')
    acceptance = input().upper()
    while (acceptance != 'Y') and (acceptance !='N'):
        print('Y or N, please!')
        acceptance = input().upper()
    if(acceptance == 'Y'):
        print('Happy password usage!')
    else:
        print('Sorry about that - please run again...')
    

   
