import random

def random_word():
    word_list = ['color','tree','icecream','resturant','mathematics','grammer','language','computer','parentheses','names','banana','televison','coordinates','center','emotion','chalkboard','whiteboard','fight','overpowered','kindness','element','dimension','temperature','globe','iphone','switch','cringe','machine']
    rand_word = random.choice(word_list)

    return rand_word

def guess_word(guessing):
    final_guess = input("what do you think the word is?")
    if  final_guess == guessing:
        print(f"Congrats!!!the correct word was {final_guess}! you did no typos and ur gud")
    else:
        print(f"boo hoo you lost. the correct word was actually {guessing}. Maybe you did a typo or ur bad. git gud")

def blank_spaces(fill_in_letters,slot,tell_letter):
    for num in slot:
        fill_in_letters = fill_in_letters[:num-1] + tell_letter + fill_in_letters[num:]
    return fill_in_letters

while True:
    dont_repeat_letters = []

    word = random_word()

    length_of_word = len(word)

    lives = 7

    print(f"the length of your word is {length_of_word} letters long")
    blank = ""

    for x in range(length_of_word):
        blank += "_"

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

        slot = []

        for ch in word:
            if guess == ch:
                print(f"{guess} is CORRECT. {guess} is in the {count} slot")
                slot.append(count)
                check = True
            count += 1

        blank = blank_spaces(blank,slot,guess)
        print(blank)

        if check == False:
            lives -=1
            print(f"omg you lost a life! you have {lives} left")
        print("--------------------------------------------\n")
        if lives == 0:
            print(f"ggs you lost. the word was {word}.")
            break
    play = input("do you want to play again?")
    if play == "no":
        print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(:( :( :( :( :( :( :( :( :( :( :( :( :( :( :(:( :( :( :( :( :( :( :( :( :( :( :( :( :( :(:( :( :( :( :( :( :( :( :( :( :( :( :( :( :(:( :( :( :( :( :( :( :( :( :( :( :( :( :( :(:( :( :( :( :( :( :( :( :( :( :( :( :( :( :( WAHHH")
        break
    else:
        print("----------------------------\n")
