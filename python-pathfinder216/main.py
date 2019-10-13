import json
import os
import sys
from collections import defaultdict
from time import time

dictionary_path = os.path.join('..', 'data', 'dictionary.txt')
letters_path = os.path.join('..', 'data', 'letters.json')

def find_all_possible_words(input_string):
    words = []
    input_length = len(input_string)
    max_line_length = input_length + 1
    with open(dictionary_path, 'r') as dictionary_file:
        for line in dictionary_file:
            line_length = len(line)
            if line_length <= max_line_length:
                input_letters = list(input_string)
                line = line[:-1]

                for letter in line:
                    try:
                        input_letters.remove(letter)
                    except:
                        break
                else:
                    words.append(line)
                    if line_length - 1 == input_length:
                        return words

    return words

def get_best_word_and_score(words):
    with open(letters_path, 'r') as letters_file:
        letters_data = json.load(letters_file)
        return max((word, sum(letters_data[letter]['score'] for letter in word)) for word in words)

def format_output(word, score, time):
    print(f'pathfinder216, Python 3, {word}, {score}, {time}, optimized grute force')

if __name__ == '__main__':
    start = time()

    input_string = sys.argv[1]

    possible_words = find_all_possible_words(input_string)
    found_words = time()
    best_word, max_points = get_best_word_and_score(possible_words)

    end = time()

    format_output(best_word, max_points, end - start)
