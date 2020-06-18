from random import randint
getrand = randint(1,100)
mylist = [0]
while True:
    print("WELCOME TO GUESS ME!")
    print("I'm thinking of a number between 1 and 100")
    print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
    print("If your guess is within 10 of my number, I'll tell you you're WARM")
    print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
    print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
    print("LET'S PLAY!")
    num = int(input("Guess the number:"))
    if int(num) < 1 or int(num) > 100:
        print("OUT OF BOUNDS")
        continue
    if num == getrand:
        print("You guessed the number! \n It's " + str(getrand))
        print(f"You guessed {len(mylist)} times")
        break
    mylist.append(num)
    if mylist[-2]:
        if abs(getrand - num) < abs(getrand - mylist[-2]):
            print("WARMER")
        else:
            print ("COLDER")
    else:
        if abs(getrand - num) <= 10:
            print("WARM!")
        else: 
            print("COLD!")
