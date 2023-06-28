import random
hs = 0
cs = 0
while True:
    x = input("What will you choose?")

    c = random.randint(0,2)

    if c ==0:
        c = "rock"
    elif c ==1:
        c = "paper"
    else:
        c = "scissors"

    if c == x:
        print("its a tie!")
        a = input("Do you want to play again?")
        if a == "no":
            break
    elif c == "rock" and x == "paper":
        print("Human wins!")
        hs = hs +1
        a = input("Do you want to play again?")
        if a == "no":
            break

    elif c == "paper" and x == "scissors":
        print("oh computer doesnt win")
        hs = hs +1
        a = input("Do you want to play again?")
        if a == "no":
            break

    elif c == "scissors" and x == "rock":
        print("git gud computer")
        hs = hs +1
        a = input("Do you want to play again?")
        if a == "no":
            break
    elif c == "rock" and x== "scissors":
        print("human dumb")
        cs = cs +1
        a = input("Do you want to play again?")
        if a == "no":
            break

    elif c == "scissors" and x== "paper":
        print("AI is smarter than human")
        cs = cs +1
        a = input("Do you want to play again?")
        if a == "no":
            break

    elif c == "paper" and x == "rock":
        print("dummy")
        cs = cs +1
        a = input("Do you want to play again?")
        if a == "no":
            break
    print(f"Human score is {hs} and computer score is {cs}")
print(f"human score is {hs} and computer score is {cs} BYEEEEEE ")