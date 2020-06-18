# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    new = ""
    for i in text:
        new += i * 3
    return new
    
# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'    
def blackjack(n1,n2,n3):
    if sum([n1,n2,n3]) <= 21:
        return sum([n1,n2,n3])
    else:
        if 11 in (n1,n2,n3) and sum([n1,n2,n3])-10 <= 21:
            return sum([n1,n2,n3]) - 10
        else:
            return "BUST" 
            
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.
def summer_69(arr):
    cant = 0
    i = 0
    cont = True
    while i != len(arr):
        if arr[i] != 6 and cont:
            cant += arr[i]
        else:
            cont = False
            if arr[i] == 9:
                cont = True
        i += 1
    return cant
