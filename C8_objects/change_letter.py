# change_letter.py
#
# function that replaces a letter in a word at the given index. 
# Usage:
#      % python change_letter.py 
#
# Himanshu Mohan, Oct 29, 2019

def change_letter(word: str, pos: int, ch: str) -> str:
    "Change the letter in position 'pos' to 'ch'"
    
    new_word=''  # New word to store change word
    for i in range(len(word)):
        if i==pos:
            new_word=new_word+ch
        else:
            new_word=new_word+word[i]

    return new_word

print(change_letter('bat', 0, 'c'))