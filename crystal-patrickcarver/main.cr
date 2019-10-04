require "json"

USER     = "patrickcarver"
LANGUAGE = "Crystal"
NOTES    = ""

START_TIME = Time.monotonic

INPUT = {size: ARGV[0].size, letter_count: letter_count(ARGV[0].chars)}

LETTER_SCORES =
  JSON
    .parse(File.read("../data/letters.json"))
    .as_h
    .transform_keys { |key| key.char_at(0) }
    .transform_values { |value| value["score"].as_i }

WORDS = File.read_lines("../data/dictionary.txt")

memo = {word: "", score: 0}

WORDS.each do |word|
  word_size = word.size

  if word_size <= INPUT[:size]
    word_chars = word.chars
    word_letter_count = letter_count(word.chars)

    if is_subset(INPUT[:letter_count], word_letter_count)
      score = word_chars.reduce(0) { |acc, letter| acc + LETTER_SCORES[letter] }

      if score > memo[:score]
        memo = {word: word, score: score}
      end
    end
  end
end

def letter_count(word)
  hash = Hash(Char, Int32).new(0)

  word.each do |letter|
    hash[letter] ||= 0
    hash[letter] += 1
  end

  hash
end

def is_subset(superset, subset)
  subset.each do |letter, _|
    return false if letter_count_does_not_match(superset[letter], subset[letter])
  end

  true
end

def letter_count_does_not_match(superset_letter, subset_letter)
  superset_letter == 0 || (subset_letter != superset_letter)
end

STOP_TIME = Time.monotonic

EXECUTION_TIME = (STOP_TIME - START_TIME).milliseconds

puts [USER, LANGUAGE, memo[:word], memo[:score], EXECUTION_TIME, NOTES].join(", ")
