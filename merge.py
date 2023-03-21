"""
A function that mergers two sorted arrays into one sorted array
and returns one sorted array
"""

def merge(list1,list2):
    list3 = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    
    while i < len(list1):
        list3.append(list1[i])
        i += 1
    
    while j < len(list2):
        list3.append(list2[j])
        j += 1

    return list3



"""
list11 = [1,3,5,7]
list22 = [2,4,6]
print(merge(list11,list22))
Output: [1, 2, 3, 4, 5, 6, 7]
-------------------------------------
list11 = [1,2,3,5]
list22 = [1,2,4,5,6]
print(merge(list11,list22))
Output: [1, 1, 2, 2, 3, 4, 5, 5, 6]
-------------------------------------
list11 = [1,5,9]
list22 = []
print(merge(list11,list22))
Output: [1, 5, 9]
"""