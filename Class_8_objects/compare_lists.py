# compare_lists.py
#
# function eval() to turn the strings into lists, and return a sorted list
# holding elements found in both lists.
# Usage:
#      % python compare_lists.py 
#
# Himanshu Mohan, Oct 29, 2019

from typing import List

def compare_lists(s1: str, s2: str) -> List:
    "What items are on both lists?"
    s1_eval=eval(s1)
    s2_eval=eval(s2)
    len_s1=len(s1_eval)
    len_s2=len(s2_eval)
    comp_list=[]
    if len_s1<=len_s2:
        for i in range(len_s1):
            if s1_eval[i] in s2_eval:
                comp_list.append(s1_eval[i])
    else:
        for i in range(len_s2):
            if s2_eval[i] in s1_eval:
                comp_list.append(s2_eval[i])
                
    comp_list.sort()            
    return (comp_list)

print (compare_lists('[1, 3, 2]', '[3, 2, 1]'))