print("welcome to the best calcualtor!")
print("this calculator has certain stuff you need to abide by")

while True:
    print("RULE 1................always check your spelling for typos")
    print("--------------------------------------------------------------------------------------------------------------")
    print("RULE 2................this calculator only has the four main operations. if you do anything else, itll not work")
    rules = input("do you understand?")
    print("--------------------------------------------------------------------------------")
    if rules == "no":
        print("then lets review it again")

    if rules == "yes":
        break


while True:
    choice = int(input("pick a number"))
    print("------------------------------------------------")
    
    choice_2 = int(input ("pick another number"))
    print("-------------------------------------------------")
    
    operator = input("what operation do you want?")
    print("---------------------------------------------------------")
    
    operator_2 = input ("do you want another operaton?")
    print("--------------------------------------------------------")
    

    if operator_2 == "yes":
        another_choice_2 = int(input("pick another another number")) 
        print("------------------------------------------------------")
        another_operater = input("what operation do you want?")
        print("-------------------------------------------------------")
        
        another_choice = int(input("pick another number"))
        
        print("--------------------------------------------------")
        if operator == "multiplication" and another_operater == "multiplication":
            print("your operation is multiplication and multiplication")
            print(f"{choice} * {choice_2} + {another_choice} * {another_choice_2} = {choice * choice_2 + another_choice * another_choice_2}  ")
 
        print("------------------------------------------------------")
        
        if operator == "multiplication" and another_operater == "division":
            print("your operation is multiplication and division")
            print(f"{choice} * {choice_2} + {another_choice} / {another_choice_2} = {choice * choice_2 + another_choice * another_choice_2}")

        if operator == "multiplication" and operator_2 == "addition":
            print("your operation is multiplication and division")
            print(f"{choice} * {choice_2} + {another_choice} + {another_choice_2} = {choice * choice_2 + another_choice + another_choice_2}")

        if operator == "multiplication" and operator_2 == "subtraction":
            print("your operation is multiplication and subtraction")
            print(f"{choice} * {choice_2} + {another_choice} - {another_choice_2} = {choice * choice_2 + another_choice - another_choice_2 }")


        if operator == "division" and operator_2 == "multiplication":
            print("your operation is multiplication and subtraction")
            print(f"{choice} * {choice_2} + {another_choice} - {another_choice_2} = {choice * choice_2 + another_choice - another_choice_2 }")

        if operator == "division" and another_operater == "division":
            print("your operation is division and division")
            print(f"{choice} / {choice_2} + {another_choice} / {another_choice_2} = {choice / choice_2 + another_choice / another_choice_2}")

        if operator == "division" and another_operater == "addition":
            print("your operation is division and addition")
            print(f"{choice} / {choice_2} + {another_choice} + {another_choice_2} = {choice / choice_2 + another_choice + another_choice_2}")

        if operator == "division" and another_operater == "subtraction":
            print("your operation is division and subtraction")
            print(f"{choice} / {choice_2} + {another_choice} - {another_choice_2} = {choice / choice_2 + another_choice - another_choice_2}")
    
        if operator == "addition" and operator_2 == "multiplication":
            print("your operation is addition and multiplication")
            print(f"{choice} + {choice_2} + {another_choice} * {another_choice_2} = {choice + choice_2 + another_choice * another_choice_2}")

        if operator == "addition" and operator_2 == "division":
            print("your operation is addition and division")
            print(f"{choice} + {choice_2} + {another_choice} / {another_choice_2} = {choice + choice_2 + another_choice / another_choice_2}")

        if operator == "addition" and operator_2 == "addition":
            print("your operation is addition and addition")
            print(f"{choice} + {choice_2} + {another_choice} + {another_choice_2} = {choice + choice_2 + another_choice + another_choice_2}")

        if operator == "addition" and operator_2 == "subtraction":
            print("your operation is addition and subtraction")
            print(f"{choice} + {choice_2} + {another_choice} - {another_choice_2} = {choice + choice_2 + another_choice - another_choice_2}")
   
        
   
   
   
    else:
        print("ok") 
     




    if operator == "subtraction" and "multiplication":
        print("your operation is subtraction and multiplication")
        print(f"{choice} - {choice_2} + {another_choice} * {another_choice_2} = {choice - choice_2 + another_choice * another_choice_2}")
    
    elif operator == "subtraction" and operator_2 == "division":
        print("your operation is subtraction and division")
        print(f"{choice} - {choice_2} + {another_choice} * {another_choice_2} = {choice - choice_2 + another_choice / another_choice_2}")

    elif operator == "subtraction" and operator_2 == "addition":
        print("your operation is subtraction and addition")
        print(f"{choice} - {choice_2} + {another_choice} + {another_choice_2} = {choice - choice_2 + another_choice + another_choice_2}")

    elif operator == "subtraction" and operator_2 == "subtraction":
        print("your operation is subtraction and subtraction")
        print(f"{choice} - {choice_2} + {another_choice} - {another_choice_2} = {choice - choice_2 + another_choice - another_choice_2}")

    elif operator == "multiplication":
        print("your operation is multiplication")
        print(f"{choice} * {choice_2} = {choice * choice_2}")

    elif operator == "division":
        print("your operation is division")
        print(f"{choice} / {choice_2} = {choice / choice_2}")

    elif operator == "addition":
        print("your operation is addition")
        print(f"{choice} + {choice_2} = {choice + choice_2}")

    elif operator == "subtraction":
        print("your operation is subtraction")
        print(f"{choice} - {choice_2} = {choice - choice_2}")


    loop_again = input("do you want to use the best calculator again?")

    if loop_again == "yes":
       print("I AM SOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO HAPPPPPPPPPPPPPPPPPYYYYYYYYYYYY :D")

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
    input("but do you actually want to use this again?")
else:
    print("OMGGGGGGGGGGUALUAL TYYYYYYYYYYYYYYYYYYYY IM CRYING TYYYY C;")
