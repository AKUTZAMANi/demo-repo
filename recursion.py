# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 12:44:23 2022

@author: omololu
"""

def permute(s):
    out = []
    if len(s) == 1:
        return s
    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [let + perm]
    return out

if __name__ == '__main__':
#    #EXAMPLE
    out = 'bust'
    print('Input:', out)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', permute(out))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
#   This means nothing

    pass #delete this line and replace with your code here
