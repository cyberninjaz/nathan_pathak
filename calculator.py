while True:
    choice = int(input("pick a number"))
    choice_2 = int(input ("pick another number"))

    operator = input("what operation do you want?")

    if operator == "multiplication":
        print("your operation is multiplication")
        print(f"{choice} * {choice_2} = {choice * choice_2}  ")

    elif operator == "division":
        print("your operation is division")
        print(f"{choice} / {choice_2} = {choice / choice_2} ") 

    elif operator == "addition":
        print("your operation is addition")
        print(f"{choice} + {choice_2} = {choice + choice_2}")

    elif operator == "subtraction":
        print("your operation is subtraction")
        print(f"{choice} - {choice_2} = {choice - choice_2} ")
    
    loop_again = input("do you want to use the best calculator again?")

    if loop_again == "no":
        print("......................................................:(")
        break

    if loop_again == "No":
        input(">:( do you want to use the BEST calculator again?")

    if loop_again == "NO":
        print("fine :(")
        break

rating = input("how do you rate the best calculator from 1-5?")

if rating == "1":
    print(":/................WAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

elif rating == "2":
    print(":L.....................................ok")

elif rating == "3":
    print(":).....................................yay")

elif rating == "4":
    print(";)TYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")

elif rating == "5":
    print(":D YAUAYAYAYAAYAYYAYAYAYAYAYAYAAYAYAYAYYAAYAYAYAYAYAY")

else:
    print("OMGGGGGGGGGGUALUAL TYYYYYYYYYYYYYYYYYYYY IM CRYING TYYYY C;")
