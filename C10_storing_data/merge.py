# merge.py
#
# a function that takes two strings representing sorted lists, 
# and returns a sorted list of the merged values
# Usage:
#      % python merge.py 
#
# Himanshu Mohan, Nov 11, 2019

from typing import List
import re

def merge(s1: str, s2: str) -> List:
    """Take two strings representing sorted lists
       Return a a list holding the merged values"""

    invalid = re.compile('[^0-9]')    
    ls1 = list(s1+s2)

    new_list=[]
    cleaned_ls1 = [int(i) for i in ls1 if not invalid.search(i)]

    n = len(cleaned_ls1)
    for i in range(n):
        for j in range(1,n):
            if cleaned_ls1[j-1] > cleaned_ls1[j]:
                (cleaned_ls1[j-1], cleaned_ls1[j]) = (cleaned_ls1[j], cleaned_ls1[j-1])
                
    return (cleaned_ls1)

    
print(merge('[4, 3, 1]', '[4, 2, 6]') )