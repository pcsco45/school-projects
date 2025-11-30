question = "yes"
while question == "yes":
    
    import random

    RPSnum = random.randint(1, 3)

    value = "lol"

    if RPSnum == 1:
        value = "rock"
    elif RPSnum == 2:
        value = "paper"
    else:
        value = "scissors"

    userinput = input("Enter rock, paper or scissors")

    if value == "rock" and userinput == "rock":
        print ("Computer said rock, draw")
    elif value == "rock" and userinput == "paper":
        print ("Computer said rock, you win")
    elif value == "rock" and userinput == "scissors":
        print ("Computer said rock, you lose")
    elif value == "paper" and userinput == "rock":
        print ("Computer said paper, you lose")
    elif value == "paper" and userinput == "paper":
        print ("Computer said paper, draw")
    elif value == "paper" and userinput == "scissors":
        print ("Computer said paper, you win")
    elif value == "scissors" and userinput == "rock":
        print ("Computer said scissors, you win")
    elif value == "scissors" and userinput == "paper":
        print ("Computer said scissors, you lose")
    elif value == "scissors" and userinput == "scissors":
        print ("Computer said scissors, draw")
    
    question = input("Would you like to play again?")
