from typing import Any
import pygame
import os
import hotdog

pygame.init()
score = 0
font = pygame.font.Font("PAPYRUS.TTF", 14)
big_font = pygame.font.Font("LCALLIG.TTF", 60)
mega_font = pygame.font.Font("LCALLIG.TTF", 80)
black = (0,0,0)
green = (14, 181, 11)
red = (194, 17, 17)
#Events
white_bunE = pygame.USEREVENT + 1
pretzel_bunE = pygame.USEREVENT + 2
wholewheat_bunE = pygame.USEREVENT + 3
glutenfree_bunE = pygame.USEREVENT + 4
crispy_bunE = pygame.USEREVENT + 5
vegandogE = pygame.USEREVENT + 6
beef_hotdogE = pygame.USEREVENT + 7
chicken_hotdog = pygame.USEREVENT + 8
ketchupE = pygame.USEREVENT + 9
mustardE = pygame.USEREVENT + 10
lettuceE = pygame.USEREVENT + 11
mayoE = pygame.USEREVENT + 12
pepperonionE = pygame.USEREVENT + 14
chilli_cheeseE = pygame.USEREVENT + 15
nathan_dogE = pygame.USEREVENT + 16

class clicksprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, callback):
        self.image = image
        self.x = x
        self.y = y
        self.callback = callback
        self.rect = self.image.get_rect()
    
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback()

velo = 5
chef_height = 100
chef_width = 100
width = 1500
height = 800
fps = 60

game_over = False

hotdogshop = pygame.image.load(os.path.join("assets", "hotdogshop_real.jpg"))
hotdogshop = pygame.transform.scale(hotdogshop,(width,height))
beef_hotdog = pygame.image.load(os.path.join("assets", "Beef hotdog-1.png"))
chicken_hotdog = pygame.image.load(os.path.join("assets", "Chicken hotdog2-1.png"))
chicken_hotdog = pygame.transform.scale(chicken_hotdog, (110, 110))
chilli_cheese = pygame.image.load(os.path.join("assets", "chilli cheese-1.png"))
chilli_cheese = pygame.transform.scale(chilli_cheese, (150, 110))
crispybun = pygame.image.load(os.path.join("assets", "crispy buns-1.png"))
crispybun = pygame.transform.scale(crispybun, (150, 150))
glutenfree = pygame.image.load(os.path.join("assets", "gluten free buns-1.png"))
glutenfree = pygame.transform.scale(glutenfree, (200, 150))
ketchup = pygame.image.load(os.path.join("assets", "ketchup-1.png"))
ketchup = pygame.transform.scale(ketchup, (200, 200))
lettuce = pygame.image.load(os.path.join("assets", "lettuce-1.png"))
lettuce = pygame.transform.scale(lettuce, (200, 200))
mayo = pygame.image.load(os.path.join("assets", "mayo-1.png"))
mayo = pygame.transform.scale(mayo, (200, 200))
mustard = pygame.image.load(os.path.join("assets", "mustard-1.png"))
mustard = pygame.transform.scale(mustard, (200, 200))
pepperonion = pygame.image.load(os.path.join("assets", "pepper and onion-1.png"))
pepperonion = pygame.transform.scale(pepperonion, (200, 200))
pretzelbun = pygame.image.load(os.path.join("assets", "pretzel bun-1.png"))
vegandog = pygame.image.load(os.path.join("assets", "Vegan dog-1.png"))
vegandog = pygame.transform.scale(vegandog, (200, 200))
wholewheat = pygame.image.load(os.path.join("assets", "whole wheat buns-1.png"))
wholewheat = pygame.transform.scale(wholewheat, (200, 200))
white = pygame.image.load(os.path.join("assets", "white buns-1.png"))
white = pygame.transform.scale(white, (200, 200))
nathan = pygame.image.load(os.path.join("assets", "Nathans hotdogs hotdog-1.png"))
nathan = pygame.transform.scale(nathan, (200, 200))
chef = pygame.image.load(os.path.join("assets", "chef-1.png"))
chef = pygame.transform.scale(chef, (chef_width, chef_height))
trash = pygame.image.load(os.path.join("assets", "trash-1.png"))
trash = pygame.transform.scale(trash, (150, 150))
winscreen = pygame.image.load(os.path.join("assets", "winning screen-1.png"))
winscreen = pygame.transform.scale(winscreen,(width,height))
losescreen = pygame.image.load(os.path.join("assets", "losing screen-1.png"))
losescreen = pygame.transform.scale(losescreen,(width,height))
win = pygame.display.set_mode((width, height))

pygame.display.set_caption('Nathans better hotdogs')

def get_orders():
    orders = hotdog.customers()
    return orders

def draw_window(the_chef,text,color1,color2,color3, time):
    global game_over
    time = time // 60
    if game_over:
        if score < 10:
            win.blit(losescreen,(0,0))
        else:
            win.blit(winscreen,(0,0))
    else:
        win.blit(hotdogshop,(0,0))
        win.blit(chef, (the_chef.x-10, the_chef.y-45))
        buntext = font.render(text[0],True,color1)
        dogtext = font.render(text[1],True,color2)
        toptext = font.render(text[2],True,color3)
        timetext = big_font.render(str(time), True, black)
        score_text = mega_font.render(str(score), True, black)
        win.blit(buntext, (10, 80))
        win.blit(dogtext, (10, 110))
        win.blit(toptext, (10, 140))
        win.blit(score_text, (1370, 100))
        win.blit(timetext, (40, 170))
        win.blit(trash, (250, 50))

    pygame.display.update()

def handle_movement(key_press, chef):
    if key_press[pygame.K_a] and chef.x - velo > 0:
        chef.x-= velo

    if key_press[pygame.K_d] and chef.x + velo + chef_width < width:
        chef.x+= velo

    if key_press[pygame.K_w] and chef.y - velo > 0:
        chef.y-= velo

    if key_press[pygame.K_s] and chef.y + velo + chef_height < height:
        chef.y+= velo

def main():
    color = (0,0,0)
    global score
    global game_over
    hotdog_list = []
    the_chef = pygame.Rect(width//2, height//2, chef_width//2, chef_height//4)
    clock = pygame.time.Clock()
    run = True
    order_complete = True
    check_chili = True
    check_glutenfree = True
    check_pretzel = True
    check_wholewheat = True
    check_crispy = True
    check_nathan = True
    check_chicken = True
    check_beef = True
    check_vegan = True
    check_pepper = True
    check_lettuce = True
    check_ketchup = True
    check_mustard = True
    check_mayo = True
    check_final = True
    check_trash = False
    orders = get_orders()
    current_customer = orders[0]
    
    
    
    while run:
        if order_complete == True:
            order_complete = False
            check_chili = True
            check_glutenfree = True
            check_pretzel = True
            check_wholewheat = True
            check_white = True
            check_crispy = True
            check_nathan = True
            check_chicken = True
            check_beef = True
            check_vegan = True
            check_pepper = True
            check_lettuce = True
            check_ketchup = True
            check_mustard = True
            check_mayo = True
            if check_trash == False:
                time_limit = current_customer.time * 60
                current_customer = orders[0]
                current_order = current_customer.get_order()
            check_trash = False

        white_bunR = pygame.Rect(1370,280,90,30)
        
        glutenfree_bunR = pygame.Rect(1330,390,90,30)
        
        pretzel_bunR= pygame.Rect(1310,440,90,30)
        
        wholewheat_bunR = pygame.Rect(1350,340,90,30)
        
        crispy_bunR = pygame.Rect(1310,500,90,30)
        
        nathan_dogR = pygame.Rect(1040,565,140,80)
        
        chicken_dogR = pygame.Rect(830,565,140,80)
        
        beef_hotdogR = pygame.Rect(580,565,140,80)
        
        vegandogR = pygame.Rect(370,565,140,80)
        
        pepperR = pygame.Rect(0,350,135,30)
        
        lettuceR = pygame.Rect(0,485,170,60)
        
        ketchupR = pygame.Rect(1230,550,30,80)
        
        mustardR = pygame.Rect(240,550,30,80)
        
        mayoR = pygame.Rect(0,410,155,45)
        
        chiliR = pygame.Rect(0,300,125,30)
        
        trashR = pygame.Rect(250, 50, 150, 150)

        order_station = pygame.Rect(450,0,500,300)

        if 'White bun' in hotdog_list:
            check_white = False

        if the_chef.colliderect(white_bunR) and check_white:
            hotdog_list.append('White bun')

        if 'Gluten free bun' in hotdog_list:
            check_glutenfree = False

        if the_chef.colliderect(glutenfree_bunR) and check_glutenfree:
            hotdog_list.append('Gluten free bun')

        if 'Whole wheat bun' in hotdog_list:
            check_wholewheat = False

        if the_chef.colliderect(wholewheat_bunR) and check_wholewheat:
            hotdog_list.append('Whole wheat bun')

        if 'Pretzel bun' in hotdog_list:
            check_pretzel = False

        if the_chef.colliderect(pretzel_bunR) and check_pretzel:
            hotdog_list.append('Pretzel bun')

        if 'Crispy bun' in hotdog_list:
            check_crispy = False

        if the_chef.colliderect(crispy_bunR) and check_crispy:
            hotdog_list.append('Crispy bun')

        if 'Vegan dog' in hotdog_list:
            check_vegan = False

        if the_chef.colliderect(vegandogR) and check_vegan:
            hotdog_list.append('Vegan dog')

        if 'Beef dog' in hotdog_list:
            check_beef = False

        if the_chef.colliderect(beef_hotdogR) and check_beef:
            hotdog_list.append('Beef dog')

        if 'Chicken dog' in hotdog_list:
            check_chicken = False

        if the_chef.colliderect(chicken_dogR) and check_chicken:
            hotdog_list.append('Chicken dog')

        if 'Nathans hotdogs dog' in hotdog_list:
            check_nathan = False

        if the_chef.colliderect(nathan_dogR) and check_nathan:
            hotdog_list.append('Nathans hotdogs dog')

        if 'Ketchup' in hotdog_list:
            check_ketchup = False

        if the_chef.colliderect(ketchupR) and check_ketchup:
            hotdog_list.append('Ketchup')

        if 'Mustard' in hotdog_list:
            check_mustard = False

        if the_chef.colliderect(mustardR) and check_mustard:
            hotdog_list.append('Mustard')

        if 'Lettuce' in hotdog_list:
            check_lettuce = False

        if the_chef.colliderect(lettuceR) and check_lettuce:
            hotdog_list.append('Lettuce')

        if 'Mayo' in hotdog_list:
            check_mayo = False

        if the_chef.colliderect(mayoR) and check_mayo:
            hotdog_list.append('Mayo')

        if 'Peppers and Onion' in hotdog_list:
            check_pepper = False

        if the_chef.colliderect(pepperR) and check_pepper:
            hotdog_list.append('Peppers and Onion')

        if 'Chili Cheese' in hotdog_list:
            check_chili = False

        if the_chef.colliderect(chiliR) and check_chili:
            hotdog_list.append('Chili Cheese')

        clock.tick(fps)

        if the_chef.colliderect(trashR):
            hotdog_list = []
            color1 = black
            color2 = black
            color3 = black
            check_trash = True
            order_complete = True

        if len(hotdog_list) >= 3:
            check_final = True
        
        if the_chef.colliderect(order_station) and check_final:
            if hotdog_list == current_order:
                score += 1

            else:
                score -= 1
            if len(orders) > 1:
                orders.pop(0)
            else:
                game_over = True
            hotdog_list = []
            check_final = False
            order_complete = True
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key_press = pygame.key.get_pressed()
        handle_movement(key_press, the_chef)
        if len(hotdog_list) == 1:
            if hotdog_list[len(hotdog_list)-1] == current_order[len(hotdog_list)-1]:
                color1 = green
            else:
                color1 = red
        elif len(hotdog_list) == 2:
            if hotdog_list[len(hotdog_list)-1] == current_order[len(hotdog_list)-1]:
                color2 = green
            else:
                color2 = red
        elif len(hotdog_list) == 3:
            if hotdog_list[len(hotdog_list)-1] == current_order[len(hotdog_list)-1]:
                color3 = green
            else:
                color3 = red
        else:
            color1 = black
            color2 = black
            color3 = black
        draw_window(the_chef, current_order,color1,color2,color3, time_limit)
        time_limit -= 1
            
        
        
        if time_limit <= 0:
            score -= 1
            hotdog_list = []
            order_complete = True
    

        pygame.display.update()


if __name__ == '__main__':
    main()
    
        