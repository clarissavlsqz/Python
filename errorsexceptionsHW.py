#Problem 1
try:    
    for i in ['a','b','c']:
        print(i**2)
except:
    print("ERROR")


#Problem 2
x = 5
y = 0

try:
    z = x/y
except: 
    print("Error")
finally:
    print("All Done")


def ask():
    while True:
        try:
            result = int(input("Input an integer: "))
        except:
            print("Try Again")
        else:
            result = result ** 2
            print("Right input, your number squared is {}".format(result))
            break;
        


ask()