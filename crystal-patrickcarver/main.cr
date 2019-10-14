require "json"

START_TIME = Time.monotonic

INPUT_DATA    = size_and_letter_count(ARGV[0])
LETTER_SCORES = letter_scores_from_json("../data/letters.json")
WORDS         = File.read_lines("../data/dictionary.txt")

memo = {word: "", score: 0}

WORDS.each do |word|
  if word.size <= INPUT_DATA[:size]
    word_chars = word.chars
    word_letter_count = letter_count(word_chars)

    if is_subset(INPUT_DATA[:letter_count], word_letter_count)
      score = score(word_chars)

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
  subset.each do |letter, count|
    return false if superset[letter] != count
  end

  true
end

def size_and_letter_count(input)
  {size: input.size, letter_count: letter_count(input.chars)}
end

def letter_scores_from_json(file)
  JSON
    .parse(File.read(file))
    .as_h
    .transform_keys { |key| key.char_at(0) }
    .transform_values { |value| value["score"].as_i }
end

def score(word_chars)
  word_chars.reduce(0) { |acc, letter| acc + LETTER_SCORES[letter] }
end

STOP_TIME = Time.monotonic

EXECUTION_TIME = (STOP_TIME - START_TIME).milliseconds

puts [
  "patrickcarver",
  "Crystal",
  memo[:word],
  memo[:score],
  EXECUTION_TIME,
  "your face is a #{memo[:word]}",
].join(", ")
