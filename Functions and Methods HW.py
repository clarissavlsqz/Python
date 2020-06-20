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
    
    
