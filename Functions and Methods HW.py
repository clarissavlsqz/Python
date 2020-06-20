#Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    return (4/3)*3.14*(rad**3)

#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    if num in range(low,high+1):
        print(f"{num} is in the range between {low} and {high}")
    else:
        print(f"{num} is not in the range of {low} and {high}")
        
def ran_bool(num, low, high):
    return num in range(low,high+1)
    
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    contUp = 0
    contLo = 0
    for i in s:
        if i.isupper():
            contUp += 1
        elif i.islower():
            contLo += 1
    print("Original String: " + s)
    print(f"No. of Upper case chars: {contUp}")
    print(f"No. of Lower case chars: {contLo}")
    
    
# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    return list(set(lst))
    
# Write a Python function to multiply all the numbers in a list.
def multiply(nums):
    res = 1
    for num in nums:
        res *= num
    return res
#Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
    s = s.replace(' ','')
    newStr = s[::-1]
    for i in range(len(s)):
        if s[i] != newStr[i]:
            return False
    return True

def palindrome(s):
    s = s.replace(' ','')
    return s == s[::-1]

#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphabet_set = set(alphabet)
    str1 = str1.replace(' ','')
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphabet_set
