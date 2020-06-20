# Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    code = [0, 0, 7]
    for i in nums:
        if i == code[0]:
            code.pop(0)
            if not code:
                return True
    return False
    
# Write a function that returns the number of prime numbers that exist up to and including a given number    
def count_primes(num):
    if num < 2:
        return 0
    cont = 1
    x = 3
    while x <= num:
        for i in range(3,x,2):
            if x%i == 0:
                x += 2
                break
        else:
            cont += 1
            x += 2
    return cont
