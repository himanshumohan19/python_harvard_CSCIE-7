# one_step_word.py
#
# a function that takes a string, and returns a sorted list with all words 
# from Downey's word list /course/data/words.txt that are Hamming Distance 1 away.
# Usage:
#      % python one_step_word.py 
#
# Himanshu Mohan, Oct 29, 2019

from typing import List

# Function to find hamming distance between 2 words
def distance(word1, word2):
    difference = 0
    if len(word1)==len(word2):
        for x,y in zip (word1, word2):
            if x != y:
                difference += 1
    else :
        pass
    
    return difference


def one_step_words(word: str) -> List[str]:
    with open('/Users/hmoha3/Downloads/words.txt',"r")  as f:
        mylist = f.read().splitlines() 
    
    onestepwordlist=[]
    for words in mylist:
        hamming=distance(words,word)
        #print(hamming)
        if hamming ==1:
            onestepwordlist.append(words)
        else:
            pass
    
    
    f.close()
    return(sorted(onestepwordlist) )

          
    
print(one_step_words('cat'))