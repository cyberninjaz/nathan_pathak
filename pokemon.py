import random

class template: 
    def __init__(self,health, damage, rarity, name, defense, speed, type):
        self.health = health
        self.damage = damage
        self.rarity = rarity
        self.name = name
        self.defense = defense
        self.speed = speed
        self.type = type

    def take_dmg(self, dmg):
        self.health -= dmg

    def healing(self, heal):
        self.health += heal

pokemon_list = [template(150, 40, .60, "Fulgaral", 60, 50, "FIRE"),template(100, 20, .80, "Keeve", 90, 30, "WATER"),
                template(120, 60, .30, "Nucleus", 50, 80, "WATER"),template(80, 30, .70, "Plagate", 91, 70, "ROCK"),
                template(80, 10, .50, "Isobase", 95, 50, "FLYING"),template(100, 75, .20, "Conniption",50, 60, "ICE"),
                template(200, 30, .10, "Reaganator", 10, 10, "ROCK"),template(300, 40, .40, "Garfield", 50, 40, "FLYING"),
                template(100, 50, .30,"Jurymast", 90, 80, "FIRE"),template(150, 30, .75, "Oble", 50, 70, "NORMAL"),
                template(100, 60, .40, "Cynical", 65, 70, "POISON"),template(100, 50, .45, "Kalon", 60, 50, "POISON"),
                template(105, 30, .75, "Orchidaceous", 80, 70, "NORMAL"),template(100, 40, .60, "Ciiz", 50, 50, "NORMAL")]

enemy_list = [template(150, 40, .60, "Fulgaral", 60, 50, "FIRE"),template(100, 20, .80, "Keeve", 90, 30, "WATER"),
                template(120, 60, .30, "Nucleus", 50, 80, "WATER"),template(80, 30, .70, "Plagate", 91, 70, "ROCK"),
                template(80, 10, .50, "Isobase", 95, 50, "FLYING"),template(100, 75, .20, "Conniption",50, 60, "ICE"),
                template(200, 30, .10, "Reaganator", 10, 10, "ROCK"),template(300, 40, .40, "Garfield", 50, 40, "FLYING"),
                template(100, 50, .30,"Jurymast", 90, 80, "FIRE"),template(150, 30, .75, "Oble", 50, 70, "NORMAL"),
                template(100, 60, .40, "Cynical", 65, 70, "POISON"),template(100, 50, .45, "Kalon", 60, 50, "POISON"),
                template(105, 30, .75, "Orchidaceous", 80, 70, "NORMAL"),template(100, 40, .60, "Ciiz", 50, 50, "NORMAL")]


party = []
enemy_party = [random.choice(enemy_list), random.choice(enemy_list), random.choice(enemy_list), random.choice(enemy_list)]
enemy_trainers = 4
pokemon_balls = 12

def battle():
    
    global pokemon_list
    global party
    global enemy_party

    current_pokemon = party[0]

    enemy = enemy_party[0]

    global enemy_trainers

    poke_enemy = len(enemy_party)

    global pokemon_balls

    print(f"{current_pokemon.name} vs {enemy.name}")
    print(f"Your stats for pokemon. Health stat: {current_pokemon.health} and  Damage stat: {current_pokemon.damage} and Type stat: {current_pokemon.type}")
    print(f"Your opponents stats. Health stat: {enemy.health} and  Damage stat: {enemy.damage} and Type stat: {enemy.type}")


    while True:
        
        if enemy.health <= 0:
            print("Enemy is unconscious!")
            enemy_party.remove(enemy)           
            poke_enemy -= 1
            print(f"only {poke_enemy} more enemies left to win the battle")

            if len(enemy_party) == 0:
                print("All enemies are unconscious! You win the battle! :D")
                enemy_trainers -= 1
                print(f"only {enemy_trainers} more trainers left")
                return True

            if enemy_trainers == 0:
                print("Congrats! you beat the game!!!! Ggs")
                return True

            enemy = enemy_party[0]
            print(f"your new enemy is {enemy.name}")

        if enemy_trainers == 0:
            print("You win the game! GG! :)")
            break


        if current_pokemon.health <= 0:
            party.remove(current_pokemon)
            
            if len(party) == 0:
                print("all of your pokemon became unconscious and you lost :(")
                break

            print(f"your {current_pokemon.name} is unconscious!")
            print(f"choose your next pokemon")

            another_count = 1

            for poke in party:
                print(f"{another_count}: {party[another_count -1].name}")
                another_count += 1
            new_poke_choice = int(input("choose the number of the pokemon you want"))
            current_pokemon = party[new_poke_choice -1]

        choice = input("attack, switch, heal, or catch?").upper()
        
        if choice == "CATCH":
            check = catch_pokemon(enemy.health)
            
            if check == True:
                party.append(enemy)
                enemy_party.pop(0)
                print(f"you caught a(n) {enemy.name}!")
                enemy = enemy_party[0]
                pokemon_balls -= 1
                print(f"you have {pokemon_balls} poke balls left")

            else:
                print(f"you failed to catch {enemy.name}")
                pokemon_balls -= 1
                print(f"you have {pokemon_balls} poke balls left")

            if pokemon_balls <= 0:
                print("you have zero poke balls left so you cant catch")

        elif current_pokemon.speed > enemy.speed:
            if choice == 'ATTACK':
                hit = random.randint(0,100)

                if enemy.defense + hit <= 110:
                    multiplier = 1
                    
                    if current_pokemon.type == enemy.type:
                        multiplier = 1
                    
                    elif current_pokemon.type == 'FIRE' and enemy.type == 'WATER':
                        multiplier = .5

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'ROCK':
                        multiplier = 2

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'FLYING':
                        multiplier = 2

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'ICE':
                        multiplier = .5

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'NORMAL':
                        multiplier = 1

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'POISON':
                        multiplier = 1

                    elif current_pokemon.type == 'WATER' and enemy.type == 'FIRE':
                        multiplier = 2

                    elif current_pokemon.type == 'WATER' and enemy.type == 'ROCK':
                        multiplier = .5

                    elif current_pokemon.type == 'WATER' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'WATER' and enemy.type == 'ICE':
                        multiplier = 1

                    elif current_pokemon.type == 'WATER' and enemy.type == 'NORMAL':
                        multiplier = 2

                    elif current_pokemon.type == 'WATER' and enemy.type == 'POISON':
                        multiplier = .5

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'FIRE':
                        multiplier = .5

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'WATER':
                        multiplier = 2

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'ICE':
                        multiplier = .5

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'NORMAL':
                        multiplier = 1

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'POISON':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'FIRE':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'WATER':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'ROCK':
                        multiplier = 2

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'ICE':
                        multiplier = 2

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'NORMAL':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'POISON':
                        multiplier = 2

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'FIRE':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'WATER':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'ROCK':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'ICE':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'POISON':
                        multiplier = 1

                    elif current_pokemon.type == 'ICE' and enemy.type == 'FIRE':
                        multiplier = .5

                    elif current_pokemon.type == 'ICE' and enemy.type == 'WATER':
                        multiplier = 1

                    elif current_pokemon.type == 'ICE' and enemy.type == 'ROCK':
                        multiplier = 1

                    elif current_pokemon.type == 'ICE' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'ICE' and enemy.type == 'POISON':
                        multiplier = .5

                    elif current_pokemon.type == 'ICE' and enemy.type == 'NORMAL':
                        multiplier == 1

                    elif current_pokemon.type == 'POISON' and enemy.type == 'FIRE':
                        multiplier = 2

                    elif current_pokemon.type == 'POISON' and enemy.type == 'WATER':
                        multiplier = 2

                    elif current_pokemon.type == 'POISON' and enemy.type == 'ROCK':
                        multiplier = 2

                    elif current_pokemon.type == 'POISON' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'POISON' and enemy.type == 'ICE':
                        multiplier = 2

                    elif current_pokemon.type == 'POISON' and enemy.type == 'NORMAL':
                        multiplier == .5

                    if multiplier == 2:
                        print("you did double damage!")

                    if multiplier == .5:
                        print("you did half damage!")

                    enemy.take_dmg(current_pokemon.damage * multiplier)
                    print(f"you did {current_pokemon.damage * multiplier} damage to {enemy.name}")

                else:
                    print(f"your {current_pokemon.name} missed!")

            elif choice == 'SWITCH':
                if len(party) > 1:
                    
                    count = 1
                    
                    for poke in party:
                        print(f"{count}: {poke.name}")
                        count += 1

                    switch_pokemon = int(input("type the number of the pokemon you want: "))
                    current_pokemon = party[switch_pokemon -1]

                    print(f"you switched to {current_pokemon.name} who is a {current_pokemon.type} type!")

                else:
                    print("you only have 1 pokemon so you cant switch")

            else:
                current_pokemon.healing(25)
                print("you healed!")

            enemy_choice = random.randint(1,3)

            if enemy_choice == 1 and enemy.health <= 70:
                enemy.healing(25)
                print("your opponent healed!")
            
            else:
                hit = random.randint(0,100)

                if enemy.defense + hit <= 110:
                    
                    multiplier = 1

                    if current_pokemon.type == enemy.type:
                        multiplier = 1
                    
                    elif current_pokemon.type == 'FIRE' and enemy.type == 'WATER':
                        multiplier = 2

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'ROCK':
                        multiplier = .5

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'FLYING':
                        multiplier = .5

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'ICE':
                        multiplier = 2

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'NORMAL':
                        multiplier = 1

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'POISON':
                        multiplier = 2

                    elif current_pokemon.type == 'WATER' and enemy.type == 'FIRE':
                        multiplier = .5

                    elif current_pokemon.type == 'WATER' and enemy.type == 'ROCK':
                        multiplier = 2

                    elif current_pokemon.type == 'WATER' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'WATER' and enemy.type == 'ICE':
                        multiplier = 1

                    elif current_pokemon.type == 'WATER' and enemy.type == 'NORMAL':
                        multiplier = .5

                    elif current_pokemon.type == 'WATER' and enemy.type == 'POISON':
                        multiplier = 1

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'FIRE':
                        multiplier = 2

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'WATER':
                        multiplier = .5

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'ICE':
                        multiplier = 2

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'NORMAL':
                        multiplier = 1

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'POISON':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'FIRE':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'WATER':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'ROCK':
                        multiplier = .5

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'ICE':
                        multiplier = .5

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'NORMAL':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'POISON':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'FIRE':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'WATER':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'ROCK':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'ICE':
                        multiplier = 1
                    
                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'POISON':
                        multiplier = 1

                    if multiplier == 2:
                        print("you took double damage!")

                    if multiplier == .5:
                        print("you took half damage!")

                    current_pokemon.take_dmg(enemy.damage  * multiplier)
                    print(f"the opposing {enemy.name} did {enemy.damage * multiplier} to your {current_pokemon.name}")

                else:
                    print(f"the opposing {enemy.name} missed!")
            
        else:
            enemy_choice = random.randint(1,3)

            if enemy_choice == 1 and enemy.health <= 70:
                enemy.healing(25)
                print("your opponent healed!")

            else:
                hit = random.randint(0,100)

                if enemy.defense + hit <= 110:
                    multiplier = 1

                    if current_pokemon.type == enemy.type:
                        multiplier = 1
                    
                    elif current_pokemon.type == 'FIRE' and enemy.type == 'WATER':
                        multiplier = 2

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'ROCK':
                        multiplier = .5

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'FLYING':
                        multiplier = .5

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'ICE':
                        multiplier = 2

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'NORMAL':
                        multiplier = 1

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'POISON':
                        multiplier = 1

                    elif current_pokemon.type == 'WATER' and enemy.type == 'FIRE':
                        multiplier = .5

                    elif current_pokemon.type == 'WATER' and enemy.type == 'ROCK':
                        multiplier = 2

                    elif current_pokemon.type == 'WATER' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'WATER' and enemy.type == 'ICE':
                        multiplier = 1

                    elif current_pokemon.type == 'WATER' and enemy.type == 'NORMAL':
                        multiplier = .5

                    elif current_pokemon.type == 'WATER' and enemy.type == 'POISON':
                        multiplier = 1

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'FIRE':
                        multiplier = 2

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'WATER':
                        multiplier = .5

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'ICE':
                        multiplier = 2

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'NORMAL':
                        multiplier = 1

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'POISON':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'FIRE':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'WATER':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'ROCK':
                        multiplier = .5

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'ICE':
                        multiplier = .5

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'NORMAL':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'POISON':
                        multiplier = 2

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'FIRE':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'WATER':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'ROCK':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'ICE':
                        multiplier = 1
  
                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'POISON':
                        multiplier = 1

                    elif current_pokemon.type == 'ICE' and enemy.type == 'FIRE':
                        multiplier = 2

                    elif current_pokemon.type == 'ICE' and enemy.type == 'WATER':
                        multiplier = 1

                    elif current_pokemon.type == 'ICE' and enemy.type == 'ROCK':
                        multiplier = 1

                    elif current_pokemon.type == 'ICE' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'ICE' and enemy.type == 'POISON':
                        multiplier = 2

                    elif current_pokemon.type == 'ICE' and enemy.type == 'NORMAL':
                        multiplier == 1
                    
                    elif current_pokemon.type == 'POISON' and enemy.type == 'FIRE':
                        multiplier = .5

                    elif current_pokemon.type == 'POISON' and enemy.type == 'WATER':
                        multiplier = 1

                    elif current_pokemon.type == 'POISON' and enemy.type == 'ROCK':
                        multiplier = 1

                    elif current_pokemon.type == 'POISON' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'POISON' and enemy.type == 'ICE':
                        multiplier = .5

                    elif current_pokemon.type == 'POISON' and enemy.type == 'NORMAL':
                        multiplier == 1

                    if multiplier == 2:
                        print("you took double damage!")

                    if multiplier == .5:
                        print("you took half damage!")


                    current_pokemon.take_dmg(enemy.damage * multiplier)
                    print(f"the opposing {enemy.name} did {enemy.damage * multiplier} to your {current_pokemon.name}")

                else:
                    print(f"the opposing {enemy.name} missed!")
            
            if choice == 'ATTACK':
                hit = random.randint(0,100)

                if enemy.defense + hit <= 110:
                    
                    multiplier = 1

                    if current_pokemon.type == enemy.type:
                        multiplier = 1
                    
                    elif current_pokemon.type == 'FIRE' and enemy.type == 'WATER':
                        multiplier = .5

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'ROCK':
                        multiplier = 2

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'FLYING':
                        multiplier = 2

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'ICE':
                        multiplier = .5

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'NORMAL':
                        multiplier = 1

                    elif current_pokemon.type == 'FIRE' and enemy.type == 'POISON':
                        multiplier = 1

                    elif current_pokemon.type == 'WATER' and enemy.type == 'FIRE':
                        multiplier = 2

                    elif current_pokemon.type == 'WATER' and enemy.type == 'ROCK':
                        multiplier = .5

                    elif current_pokemon.type == 'WATER' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'WATER' and enemy.type == 'ICE':
                        multiplier = 1

                    elif current_pokemon.type == 'WATER' and enemy.type == 'NORMAL':
                        multiplier = 2

                    elif current_pokemon.type == 'WATER' and enemy.type == 'POISON':
                        multiplier = 1

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'FIRE':
                        multiplier = .5

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'WATER':
                        multiplier = 2

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'ICE':
                        multiplier = .5

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'NORMAL':
                        multiplier = 1

                    elif current_pokemon.type == 'ROCK' and enemy.type == 'POISON':
                        multiplier = 2

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'FIRE':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'WATER':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'ROCK':
                        multiplier = 2

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'ICE':
                        multiplier = 2

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'NORMAL':
                        multiplier = 1

                    elif current_pokemon.type == 'FLYING' and enemy.type == 'POISON':
                        multiplier = 2

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'FIRE':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'WATER':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'ROCK':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'ICE':
                        multiplier = 1

                    elif current_pokemon.type == 'NORMAL' and enemy.type == 'POISON':
                        multiplier = 1

                    elif current_pokemon.type == 'ICE' and enemy.type == 'FIRE':
                        multiplier = .5

                    elif current_pokemon.type == 'ICE' and enemy.type == 'WATER':
                        multiplier = 1

                    elif current_pokemon.type == 'ICE' and enemy.type == 'ROCK':
                        multiplier = 1

                    elif current_pokemon.type == 'ICE' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'ICE' and enemy.type == 'POISON':
                        multiplier = .5

                    elif current_pokemon.type == 'ICE' and enemy.type == 'NORMAL':
                        multiplier == 1
                    
                    elif current_pokemon.type == 'POISON' and enemy.type == 'FIRE':
                        multiplier = 2

                    elif current_pokemon.type == 'POISON' and enemy.type == 'WATER':
                        multiplier = 1

                    elif current_pokemon.type == 'POISON' and enemy.type == 'ROCK':
                        multiplier = 1

                    elif current_pokemon.type == 'POISON' and enemy.type == 'FLYING':
                        multiplier = 1

                    elif current_pokemon.type == 'POISON' and enemy.type == 'ICE':
                        multiplier = 2

                    elif current_pokemon.type == 'POISON' and enemy.type == 'NORMAL':
                        multiplier == 1

                    if multiplier == 2:
                        print("you did double damage!")

                    if multiplier == .5:
                        print("you did half damage!")

                    enemy.take_dmg(current_pokemon.damage * multiplier)
                    print(f"you did {current_pokemon.damage * multiplier} damage to {enemy.name}")

                else:
                    print(f"your {current_pokemon.name} missed!")

            elif choice == 'SWITCH':
                
                if len(party) > 1:
                    
                    count = 1

                    for poke in party:
                        print(f"{count}: {poke.name}")
                        count += 1

                    switch_pokemon = int(input("type the number of the pokemon you want: "))
                    current_pokemon = party[switch_pokemon -1]

                    print(f"you switched to {current_pokemon.name}")

                else:
                    print("you only have 1 pokemon so you cant switch")

            else:
                current_pokemon.healing(25)
                print("you healed!")

        print(f"your {current_pokemon.name} is at {current_pokemon.health} health and your enemy, {enemy.name} is at {enemy.health} health")
        print("-------------------------------------------")

        if current_pokemon.health <= 35 and current_pokemon.health >=5:
            run_or_stay = input(f"your {current_pokemon.name} is low at health, do you want to run or stay?").upper()

            if run_or_stay == "RUN":
                return True
            
            else:
                print("ok..")

def choose_pokemon():
    global pokemon_list
    global party
    count_start = 1
    for poke in pokemon_list:
        print(f"{count_start}: {poke.name}")
        count_start += 1
    choose_the_pokemon = int(input("choose the number of the first pokemon you want"))
    choose_the_pokemon_2 = int(input("choose the number of the second pokemon you want"))
    party.append(pokemon_list[choose_the_pokemon - 1])
    party.append(pokemon_list[choose_the_pokemon_2 - 1])
    return True

def catch_pokemon(health):
    
    global enemy_party
    global party

    chance = random.randint(0,10)
    
    if health <= 100 and health >= 70:
        if chance == 10 or chance == 4:
            return True
        
    elif health < 70 and health >= 35:
        if chance <= 5:
            return True
        
    elif health < 35:
        if chance <= 9:
            return True
        
    else:
        if chance == 0:
            return True
        
        else:
            return False

def wild_pokemon():
    
    global pokemon_balls
    global pokemon_list

    while True:

        wild_pokemon = random.choice(pokemon_list)

        while True:

            rarity = wild_pokemon.rarity

            the_rarity_of_poke = random.randint(1,10)

            if rarity * the_rarity_of_poke < 500:
                break

            else:
                wild_pokemon = random.choice(pokemon_list)

        pokemon_real = wild_pokemon
        wild_pokemon = wild_pokemon.name
        
        print(f"you found a wild {wild_pokemon}!")

        while True:
            print("------------------------------------------------------")

            catch_or_wait = input("wait or catch?").upper()

            if catch_or_wait == "WAIT":
                
                wild_pokemon_chance = random.randint(0,10)
                if wild_pokemon_chance <= 10 and wild_pokemon_chance > 6:
                    print(f"the wild {wild_pokemon} doesnt see you...")

                else:
                    print("the wild pokemon ran away :(")
                    return True

            elif catch_or_wait == "CATCH":
                
                other_wild_pokemon_chance = random.randint(0,10)
                if other_wild_pokemon_chance <= 10 and other_wild_pokemon_chance > 6:
                    print(f"the wild {wild_pokemon} ran away :(")
                    pokemon_balls -= 1
                    print(f"you have {pokemon_balls} pokemon balls left")
                    return True

                else:
                    print(f"you successfully caught a wild {wild_pokemon}!")
                    party.append(pokemon_real)
                    pokemon_balls -= 1
                    print(f"you have {pokemon_balls} pokemon balls left")
                    return True

while True:

    choose_pokemon()
    print("------------------------------------------------------------------------------------------------------------------------------------------")

    while True:
        
        function_chance = random.randint(1,5)
        if function_chance == 1:  
            wild_pokemon()
        
        if function_chance == 2:
            fight = input("you found a pokemon trainer. do you want to fight or not?").upper()
            
            if fight == "FIGHT":
                print(f"you have {pokemon_balls} pokemon balls left to fight")
                battle()

                if pokemon_balls == 0:
                    are_you_sure = input("are you sure? poke balls dont really matter but do. so yes or no?").upper()

                    if are_you_sure == "YES":
                        print("alright")
                        battle()

                    else:
                        print("sure")

                if True:
                    print("Wowie!")
                    print(f"you have {pokemon_balls} poke balls left")

            if fight == "NOT":
                print("coward")

        if function_chance == 3:
            print("you found nothing :(")

        if function_chance == 4:
            print("you found something quite suspicous..")
            more_chance = random.randint(1,4)

            if more_chance < 2 and more_chance >= 1:
                print("you found a Poke Ball!")
                pokemon_balls += 1
                print(f"you have {pokemon_balls} poke balls left")

            if more_chance == 2:
                print("you found nothing")

            else:
                wild_pokemon()
        
        if function_chance == 5:
            print("you found a poke healing center!")
            heal_choice = input ("do you want to go to the healing center?").upper()

            if heal_choice == "YES":
                for poke in party:
                    poke.healing(60)
                print("all of you pokemon are healed!")
                for poke in party:
                    print(f"{poke.name}: Health is {poke.health}")


            else:
                print("you didnt heal")

        elif len(party) == 0:
            break

        elif enemy_trainers == 0:
            break

        print("----------------------------------------------")

    play_again = input("do you want to play again?").upper()

    if play_again == "YES":
        print("Yay! :D")

    else:
        print("oh ok :(")
        break
