# one_step.py
#
# a function that takes a word and returns a list with all possible edits 
#to the word that change a single letter. Your list should be sorted.
# Usage:
#      % python one_step.py 
#
# Himanshu Mohan, Oct 29, 2019
from typing import List
import string

def one_step(word: str) -> List[str]:
    "Return all lower case strings Hamming Distance 1 away"
    word1=word.lower()
    word2 = ''
    res = []
    text = string.ascii_lowercase

    for i in range(0, len(word1), 1):
        for j in range(0, len(text), 1):
            if word1[i] != text[j]:
                word2 = word1[0:i]+text[j]+word1[i+1:]

                res.append(word2)


    return sorted(res)

lst = one_step('Aa')
print(lst)
print(len(lst))