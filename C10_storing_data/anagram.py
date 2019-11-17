# anagram.py
#
# a function that decides if two strings are anagrams
# Usage:
#      % python anagram.py 
#
# Himanshu Mohan, Nov 11, 2019

def is_anagram(word1: str, word2: str) -> bool:
    "Is word2 an anagram of word1?"
 
    try:
        if word1.lower()==word2.lower():
            raise AssertionError
       
    except AssertionError:
            print("Did not expect", word1, "and", word2, "to be anagrams")
            return False
    # Get lengths of both strings 
    n1 = len(word1)  
    n2 = len(word2)  

    # If lenght of both strings is not same, then  
    # they cannot be anagram  
    if n1 != n2:  
        return False
  
    # Sort both strings  
    word1_list = sorted(word1.lower()) 
    #print(sorted(word1.lower()))
    word2_list = sorted(word2.lower())
    #print(sorted(word2.lower()))
  
    # Compare sorted strings  
    for i in range(0, n1):  
        if word1_list[i] != word2_list[i]:  
            return 0
  
    return True

print(is_anagram('silent','Listen'))