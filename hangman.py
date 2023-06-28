import random

def random_word():
    word_list = ['color','tree','icecream','resturant','mathematics','grammer','language','computer','parentheses','names','banana','televison','coordinates','center','emotion','chalkboard','whiteboard','fight','overpowered','kindness','element','dimension','temperature','globe','iphone','switch','cringe','machine']
    rand_word = random.choice(word_list)

    return rand_word

def guess_word(guessing):
    final_guess = input("what do you think the word is?")
    if  final_guess == guessing:
        print(f"Congrats!!!the correct word was {final_guess}")
    else:
        print(f"boo hoo you lost. the correct word was actually {guessing}. ")
  



while True:
    dont_repeat_letters = []

    word = random_word()

    length_of_word = len(word)

    lives = 7

    print(f"the length of your word is {length_of_word} letters long")

    while True:

        if len(dont_repeat_letters) > 0:
            choice  = input("do you want to guess the word yet?")
            if "yes" == choice:
                guess_word(word)
                break
            print(f"the letters you guessed already are {dont_repeat_letters}")


        guess = input("pick a letter")

        dont_repeat_letters.append(guess)


        count = 1
        check = False

        for ch in word:
            if guess == ch:
                print(f"{guess} is CORRECT. {guess} is in the {count} slot")
                check = True
            count += 1

        if check == False:
            lives -=1
            print(f"omg you lost a life! you have {lives} left")

        if lives == 0:
            print(f"ggs you lost. the word was {word}.")
            break
    play = input("do you want to play again?")
    if play == "no":
        print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(:( :( :( :( :( :( :( :( :( :( :( :( :( :( :(:( :( :( :( :( :( :( :( :( :( :( :( :( :( :(:( :( :( :( :( :( :( :( :( :( :( :( :( :( :(:( :( :( :( :( :( :( :( :( :( :( :( :( :( :(:( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
        break
    else:
        print("----------------------------\n")