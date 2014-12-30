from __future__ import print_function
from sys import argv

script, filename = argv


def clean_word(w):
    result = ''
    for letter in w:
        lower_letter = letter.lower()
        if lower_letter in 'abcdefghijklmnopqrstuvwxyz':
            result += lower_letter
    return result

wordCount = {}
with open(filename, 'r') as f:
    for line in f:
        for word in line.split():
            word = clean_word(word)
            if word is not '':
                if word in wordCount:
                    wordCount[word] = wordCount.get(word) + 1
                else:
                    wordCount[word] = 1


wordCount = sorted(wordCount.items(), key=lambda count: count[1], reverse=True)
for each in wordCount:
    print(each)

