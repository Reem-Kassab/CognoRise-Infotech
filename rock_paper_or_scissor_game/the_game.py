import random


options=("Rock","Paper","Scissor")
p_score=0
c_score=0
running=True

while running:
    player=None
    computer=random.choice(options)

    while player not in options:
        player=input("Enter a choice ( Rock , Paper , Scissor) : ")

    print(f"player : {player}")
    print(f"computer : {computer}")

    if player==computer:
        print("it is a tie")
    elif player=="Rock" and computer=="Scissor":
        p_score+=1
        print("You win")
        print(f"your score is : {p_score}")
        print(f"Computer score is : {c_score}")
    elif player=="Paper" and computer=="Rock":
        p_score+=1
        print("You win")
        print(f"your score is : {p_score}")
        print(f"Computer score is : {c_score}")
    elif player=="Scissor" and computer=="Paper":
        p_score+=1
        print("You win")
        print(f"your score is : {p_score}")
        print(f"Computer score is : {c_score}")
    else:
        c_score+=1
        print("You lose")
        print(f"your score is : {p_score}")
        print(f"Computer score is : {c_score}")
    play=input("Play again ? (y/n):").lower()
    if not play =="y":
        running=False
print("Thanks for playing")