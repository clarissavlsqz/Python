def old_macdonald(name):
    first = name[:3]
    second = name[3:]
    return first.capitalize() + second.capitalize()
    
def master_yoda(sentence):
    new = sentence.split()
    new.reverse()
    return " ".join(new)
    
def almost_there(n):
    return abs(100-n) <= 10 or abs(200-n) <= 10    
