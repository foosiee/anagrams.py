# code from medium article
dict = {}

f = open("words.txt", "r")

for line in f.readlines():
    word = line.strip().lower()
    sortedLetters = sorted(list(word))
    sortedWord = "".join(sortedLetters)
    if sortedWord in dict:
        dict[sortedWord].append(word)
    else:
        dict[sortedWord] = [word]

import pickle
with open('words.pickle', 'wb') as f:
    pickle.dump(dict, f)

