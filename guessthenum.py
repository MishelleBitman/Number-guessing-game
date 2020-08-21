import random
num = random.randint(1,10)
for i in range(4):
    guess=int(input("Guess the number"))
    if abs(guess-num)==0:
        print ("You guessed it! the number was" ,num)
        break
    if abs(guess-num)==1 or abs(guess-num)==2:
        print ("hot")
    elif abs(guess-num)==3 or abs(guess-num)==4:
        print ("worm")
    elif abs(guess-num)==5 or abs(guess-num)==6 or abs(guess-num)==7:
        print ("cold")
    elif abs(guess-num)==8 or abs(guess-num)==8:
        print ("freezing")
    if i==3 and (guess-num)!=0:
        print ("The game is over:( You did not guess the number, but you can try again!")
        
        
