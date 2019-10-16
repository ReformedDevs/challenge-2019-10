import json
import sys
import time


def read_letter_scores(filename='../data/letters.json'):
    with open(filename) as letters:
        return json.loads(letters.read())


def is_legal(word, tile_freq):
    tiles = tile_freq.keys()
    for letter in word:
        if letter not in tiles or word.count(letter) > tile_freq[letter]:
            return False
    return True


def get_legal_words(tiles, filename='../data/dictionary.txt'):
    limit = len(tiles)
    tile_freq = {letter: tiles.count(letter) for letter in set(tiles)}
    with open(filename) as dictionary:
        parse = [line.strip().replace('-', '') for line in dictionary]
        return [x for x in parse if len(x) <= limit and is_legal(x, tile_freq)]


def get_score(word, letter_scores):
    return sum(letter_scores[letter]['score'] for letter in word)


def solve(words, scores, solution=None, max_score=0):
    if not len(words):
        return solution, max_score
    if scores[0] > max_score:
        return solve(words[1:], scores[1:], words[0], scores[0])
    return solve(words[1:], scores[1:], solution, max_score)


def main():
    input_tiles = sys.argv[1] if len(sys.argv) > 1 else ''
    lang = 'Python 3'
    user = 'Kyle Nweeia'

    start = 1000 * time.perf_counter()
    legal_words = get_legal_words(input_tiles)
    letter_scores = read_letter_scores()
    word_scores = [get_score(word, letter_scores) for word in legal_words]
    solution, score = solve(legal_words, word_scores)
    duration = 1000 * time.perf_counter() - start
    print(f'{user}, {lang}, {solution}, {score}, {duration},')


if __name__ == '__main__':
    main()
