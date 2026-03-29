import random
def RockPaperScissors():
    n=int(input("How many rounds do you want to play?: "))
    com_score=0
    user_score=0
    choices= ["R","S","P"]
    for i in range(n):
        user_input=str(input("Enter your move:\nR for Rock\nS for Scissors\nP for Paper\n"))
        a= random.choice(choices)
        if a == user_input:
            print("TIE!")
        elif a == "R" and user_input == "S":
            print("COMPUTER WON!")
            com_score+=1
        elif a == "R" and user_input == "P":
            print("YOU WON!")
            user_score+=1
        elif a == "S" and user_input == "R":
            print("YOU WON!")
            user_score+=1
        elif a == "S" and user_input == "P":
            print("COMPUTER WON")
            com_score+=1
        elif a == "P" and user_input == "R":
            print("COMPUTER WON!")
            com_score+=1
        elif a == "P" and user_input == "S":
            print("YOU WON")
            user_score+=1
    print(f"------------------\nFINAL SCORE\nYOU\t\t\t{user_score}\nCOMPUTER\t{com_score}\n------------------")
            
RockPaperScissors()
    
