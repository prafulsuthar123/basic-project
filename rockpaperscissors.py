import random
l=["rock", "scissor", "paper"]
com_input=random.choice(l)
comp=0
usp=0
r=int(input("Enter the no. of round:- \n"))
while True:
    user_choice = int(input('''
Game start.........
1 YES
2 NO | EXIT\n                      
'''))
    if user_choice == 1:
        for a in range(r):
            user_input = int(input('''
1 ROCK
2 SCISSOR
3 PAPER\n                             
'''))
            if user_choice == 1:
                uch="rock"
            elif user_choice ==2:
                uch="scissor"
            elif user_choice ==3:
                uch="paper"
            else:
                print("invalid")

            if com_input==uch:
                print("computer value", com_input)
                print("user choice", uch)
                print("Tie")
                usp+=1
                comp+=1
            
            elif (uch=="rock" and com_input=="scissor") or (uch == "paper" and com_input=="rock") or (uch=="scissor" and com_input=="paper"):
                print("computer value", com_input)
                print("user choice", uch)
                print("user win")
                usp+=1 
            
            else:
                print("computer value", com_input)
                print("user choice", uch)
                print("computer win")
                comp+=1
        print("\n")       
        if usp==comp:
            print("tie")
            print("user score",usp)
            print("computer score", comp)
        elif usp>comp:
            print("user win")        
            print("user score",usp)
            print("computer score", comp)
        else:
            print("computer winr")
            print("user score",usp)
            print("computer score", comp)
    else:
        break
