# Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    first = name[:3]
    second = name[3:]
    return first.capitalize() + second.capitalize()

# Given a sentence, return a sentence with the words reversed
def master_yoda(sentence):
    new = sentence.split()
    new.reverse()
    return " ".join(new)


# Given an integer n, return True if n is within 10 of either 100 or 200    
def almost_there(n):
    return abs(100-n) <= 10 or abs(200-n) <= 10    
