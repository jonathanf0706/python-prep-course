from text_analyzer import (
    count_words,
    count_characters,
    find_longest_word
)

sample = "The quick brown fox jumps over the lazy dog"

print(count_words(sample))
print(count_characters(sample))
print(count_characters(sample, include_spaces=True))
print(find_longest_word(sample))
