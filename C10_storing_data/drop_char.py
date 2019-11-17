# drop_char.py
#
#  a function that uses a List Comprehension to take a string and 
#returns a list of all lower case strings you can obtain by removing 
# a single character.
# Usage:
#      % python drop_char.py 
#
# Himanshu Mohan, Nov 11, 2019
from typing import List

def drop_char(word: str) -> List[str]:
    "Return all lower case strings obtained by dropping one char"
    new_word=word.lower()
    new_list=[ new_word[0:i]+new_word[i+1:] for i in range(len(new_word))]

    return(new_list)

drop_char('Total')