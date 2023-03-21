"""
A function that takes a list and calculate its length 
and returns ture if the list is a palidrome, otherwise returns false.
"""

def palindrome(aList):
    length = len(aList)
    for i in range(length // 2):
        if aList[i] != aList[(length - i) - 1]:
            return False
    return True

"""
aList11 = [1,2, "Espresso", "Madeline", 2, 1]
factor1 = palindrome(aList11)
print(factor1)
Output: False
------------------------------------------------
aList12 = ['a',True, False, False, True, 'a']
factor2 = palindrome(aList12)
print(factor2)
Output: True
------------------------------------------------
aList13 = [3]
factor3 = palindrome(aList13)
print(factor3)
Output: True
"""