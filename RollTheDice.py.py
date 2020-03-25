import random

play1=0
play2=0
value=False
value1=False
game_still_on=True
while game_still_on:
    if play1>=20:
        value=True
        
        break
    else:
        print("player1 roll the dice")
        player1=random.randint(0,6)
        print("The player1 dice value",player1)
        print("\n")
        play1+=player1
        if play1>=20:
            value=True
            break
       
    if play2>=20:
        value1=True
        
        break
    else:
        print("player2 roll the dice")
        player2=random.randint(0,6)
        print("The player2 dice value",player2)
        print("\n")
        play2+=player2
        if play2>=20:
            value1=True
            break
        
if value == True:
    print("player1 won")  
elif value1 == True:
    print("player2 won")