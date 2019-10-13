import json
import os
import sys
from time import time

dictionary_path = os.path.join('..', 'data', 'dictionary.txt')
letters_path = os.path.join('..', 'data', 'letters.json')

def find_all_possible_words(input_string):
    """
    Checks each entry in a dictionary file for words
    that can be formed from the letters of an input string.
    """
    words = []
    input_length = len(input_string)
    max_line_length = input_length + 1

    with open(dictionary_path, 'r') as dictionary_file:
        for line in dictionary_file:
            line_length = len(line)

            # You can't form a word that's longer than the input string
            if line_length <= max_line_length:
                input_letters = list(input_string)
                line = line[:-1]

                # Check that each letter in the word is in the input string
                for letter in line:
                    try:
                        input_letters.remove(letter)
                    except:
                        # A letter wasn't in the input string, so this word can't be formed
                        break
                
                # All the letters were found in the input string
                else:
                    # If all letters were used, this is the best word
                    if line_length - 1 == input_length:
                        return [line]

                    words.append(line)

    return words

def get_best_word_and_score(words):
    """ Returns the highest scoring word and its score from a list of words """
    with open(letters_path, 'r') as letters_file:
        letters_data = json.load(letters_file)
        return max((word, sum(letters_data[letter]['score'] for letter in word)) for word in words)

def format_output(word, score, time):
    print(f'pathfinder216, Python 3, {word}, {score}, {time}, optimized grute force')

if __name__ == '__main__':
    start = time()

    input_string = sys.argv[1]

    possible_words = find_all_possible_words(input_string)
    best_word, max_points = get_best_word_and_score(possible_words)

    end = time()

    format_output(best_word, max_points, end - start)
