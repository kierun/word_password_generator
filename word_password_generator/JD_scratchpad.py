from pathlib import Path
from random import randrange

def AskNumberOfWords():
    # Ask the user for a number in the range 4 to 6 to use later for number of words selected
    print('How many words would you like in your password (4-6)?')
    number_of_words = input()
    # Make sure we do only take a number in the range 4 to 6!
    while(int(number_of_words) < 4) or (int(number_of_words) > 6):
        print('That value is outside the accepted range (4-6), please try again:')
        number_of_words = input()
    return number_of_words

def AskForFileLocation():
    # Ask the user for the path to the word list file - wanted to do more here, but analysing
    # the format of text files seems tough and I wanted to get this done
    print('Please enter the path to the word list file:')
    file_path_input = input()
    file_path = Path(file_path_input)
    # We can at least check the file location is legitimate
    if not file_path.is_file():
        print('File not present at specified location, please run again...')
        file_path = AskForFileLocation()
    return file_path


def SelectWordsFromList(word_list, number_of_words):
    # Here, get the string-array length and feed that in as the top end of a random number generator
    # Use user-input for number of words desired to cycle through the array and pick random words out
    list_length = len(word_list)
    output_list = list()
    for count in range(0, int(number_of_words)):
        selection = randrange(0, list_length, 1)
        new_word = word_list[selection]
        # print('Word number: ' + str(selection +1) + ', ' + new_word)
        while(new_word in output_list):
            # print('DUPLICATE!!!')
            selection = randrange(0, list_length, 1)
            new_word = word_list[selection]
            # print('Word number: ' + str(selection +1) + ', ' + new_word)
        output_list.append(new_word)
        count += 1
    return output_list


def main():
    # Ask for the desired number of words
    number_of_words = AskNumberOfWords()
    # Ask for a word list file
    file_path = AskForFileLocation()

    # use 'with' to open and process the file contents so that when completed the resources are freed
    with open(file_path) as datafile:
        words = (word.rstrip('\r\n') for word in datafile)
        desired_words = list()
        # Loop down the list of words and store the desirable ones
        for word in words:
            if(len(word) <=6 and len(word) >= 4):
                # Try adding the filtered word list to an array of strings?
                desired_words.append(word)
        # Select a unique set of words from the stored list, number defined earlier by the user
        output_list = SelectWordsFromList(desired_words, number_of_words)
        # Output the word selection to the console and see if the user likes them
        for output_words in output_list:
            print(output_words, end=',')
        print('\nAre these words acceptable (Y/N)?')
        acceptance = input().upper()
        while (acceptance != 'Y') and (acceptance !='N'):
            print('Y or N, please!')
            acceptance = input().upper()
        # As long as the user doesn't like the selection, make another one
        while(acceptance == 'N'):
            print('Sorry about that, let\'s try again!')
            output_list = SelectWordsFromList(desired_words, number_of_words)
            for output_words in output_list:
                print(output_words, end=',')
            print('\nAre these words acceptable (Y/N)?')
            acceptance = input().upper()
            while (acceptance != 'Y') and (acceptance !='N'):
                print('Y or N, please!')
                acceptance = input().upper()
        print('Happy password usage!')

   
if __name__ == "__main__":
    main()


    

   
