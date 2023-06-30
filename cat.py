while True:
    choice = input("How old are you?")

    years_old = int(choice)

    time = 100 - years_old

    print(f"You are going to be 100 in {time} years ")

    if  time >= 90:
        print("You are young")
    else:
        print ("You are old") 
    yay = input("do you want to make computer tell you how many years until your 100 again?")
    
    if yay == "no":

        print("WHYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY :(")
        break
