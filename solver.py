import pickle
from itertools import combinations
with open('words.pickle', 'rb') as f:
    dict = pickle.load(f)

def sort_letters(a):
    return "".join(sorted(list(a)))
def solver(a):
    sorted_a = sort_letters(a)
    if sorted_a in dict:
        return dict[sorted_a]
    else:
        return []

x = input("enter anagram phrase: ")
x = [''.join(l) for i in range(len(x)) for l in combinations(x, i+1)]


arr = []

for word in x:
    if len(word) >= 3:
        arr.append(word)

words = []

for gram in arr:
    print(solver(gram))

                  