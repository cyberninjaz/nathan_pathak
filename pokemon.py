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
                template(80, 10, .50, "Isobase", 95, 50, "FLYING"),template(100, 80, .20, "Conniption",50, 60, "ICE"),
                template(200, 30, .10, "Reaganator", 10, 10, "ROCK"),template(300, 40, .40, "Garfield", 50, 40, "FLYING"),
                template(100, 50, .30,"Jurymast", 90, 80, "FIRE"),template(150, 30, .75, "Oble", 50, 70, "NORMAL")]

enemy_list = [template(150, 40, .60, "Fulgaral", 60, 50, "FIRE"),template(100, 20, .80, "Keeve", 90, 30, "WATER"),
                template(120, 60, .30, "Nucleus", 50, 80, "WATER"),template(80, 30, .70, "Plagate", 91, 70, "ROCK"),
                template(80, 10, .50, "Isobase", 95, 50, "FLYING"),template(100, 80, .20, "Conniption",50, 60, "ICE"),
                template(200, 30, .10, "Reaganator", 10, 10, "ROCK"),template(300, 40, .40, "Garfield", 50, 40, "FLYING"),
                template(100, 50, .30,"Jurymast", 90, 80, "FIRE"),template(150, 30, .75, "Oble", 50, 70, "NORMAL")]


party = [pokemon_list[0], pokemon_list[4], pokemon_list[7], pokemon_list[5]]
enemy_party = [random.choice(enemy_list), random.choice(enemy_list), random.choice(enemy_list), random.choice(enemy_list)]

def battle():
    
    global pokemon_list
    global party
    global enemy_party

    current_pokemon = party[0]

    enemy = enemy_party[0]

    print(f"{current_pokemon.name} vs {enemy.name}")
    print(f"Your stats for pokemon. Health stat: {current_pokemon.health} and  Damage stat: {current_pokemon.damage} and Type stat: {current_pokemon.type}")
    print(f"Your opponents stats. Health stat: {enemy.health} and  Damage stat: {enemy.damage} and Type stat: {enemy.type}")


    while True:
        
        if enemy.health <= 0:
            print("Enemy is unconscious!")
            enemy_party.remove(enemy)           
            if len(enemy_party) == 0:
                print("All enemies are unconscious! You win :D")
                break
            enemy = enemy_party[0]
            print(f"your new enemy is {enemy.name}")

        if current_pokemon.health <= 0:
            party.remove(current_pokemon)
            
            if len(party) == 0:
                print("all of your pokemon became unconscious and you lost :(")
                break

            print(f"your {current_pokemon.name} is unconscious")
            print(f"choose your next pokemon")

            another_count = 1

            for poke in party:
                print(f"{another_count}: {party[another_count -1].name}")
                another_count += 1
            new_poke_choice = int(input("choose the number of the pokemon you want"))
            current_pokemon = party[new_poke_choice -1]

        choice = input("attack, switch or heal?").upper()
        
        if current_pokemon.speed > enemy.speed:
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

battle()
