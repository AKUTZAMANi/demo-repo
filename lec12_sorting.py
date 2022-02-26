# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:21:39 2016

@author: ericgrimson
"""
# compare consecutive pairs of elements
# swap elements in pair such that smaller is first
#start over again, when list ends
#stop when no swaps have been made

def bubble_sort(L):
    swap = False
    while not swap:# for doing multiple passes until no more swaps O(len(L))
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)): #O(len(L))
            if L[j-1] > L[j]:   #comparisons
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

testList = [1,9,42,2,61,3,5,7,2,6,25,18,13]

print('')
print(bubble_sort(testList))
print(testList)


def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):# logn
        print(suffixSt)
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
 
testList = [1,3,5,7,2,6,25,18,13]
       
print('')
print(selection_sort(testList))
print(testList)


def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i]< right[j]: #left and right sublists are ordered move indices for
                                # sublists depending on which sublist holds next smallest element
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
    return result

def merge_sort(L):  # merge sort algorithm --- recursive
    print('merge sort: ' + str(L))
    if len(L) < 2:   # base case
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])   #divide list
        right = merge_sort(L[middle:])
        return merge(left, right) #conquer with the merge step
        
testList = [1,3,5,7,2,6,25,18,13]

print('')
print(merge_sort(testList))
# best case: O(n) where n is len(L) to check if sorted
# worst case: O(?) it is unbounded if really unlucky

# import random
# def bogo_sort(L):
#     while not is_sorted(L):
#         random.shuffle(L)
# List = [1,3,5,7,2,6,25,18,13]
# print(bogo_sort(List))
def lastNameFirstName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
        return arg1[1] < arg2[1]
    else: #last names the same, sort by first name
        return arg1[0] < arg2[0]
def firstNameLastName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else: #first names the same, sort by last name
        return arg1[1] < arg2[1]
L = ['Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
newL = merge_sort(L, lastNameFirstName)
print('Sorted by last name =', newL)
newL = merge_sort(L, firstNameLastName)
print('Sorted by first name =', newL)
