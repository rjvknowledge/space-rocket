import pygame
pygame.init()
import random

#color

white = ( 255 , 255 , 255 )
red = ( 255 , 0 , 0 )
aqua = ( 0 , 255 , 255 )
wheat1 = ( 255 , 231 , 86 )

medium_spring_green = (0,250,154)
spring_green = (0,255,127)


#creating window

window_length = 1200
window_breadth = 600


window = pygame.display.set_mode((window_length , window_breadth ))
caption = pygame.display.set_caption(" game ")



#text function
font = pygame.font.SysFont ( None , 50 )

def text_screen( text , color ,x , y ):
    screen_text = font.render ( text , True , color )
    window.blit (screen_text , [ x, y] )

    
#button

def button( color_1 , color_2 , button_x , button_y ):
    pygame.draw.rect(window , color_1 ,[ button_x + 5 , button_y  + 5 , 50 , 50 ])
    pygame.draw.rect(window , color_2 ,[ button_x  , button_y , 50 , 50 ])






# start screen

def game_start():
    start = pygame.image.load("C:\\Python34\\rajeev\\image\\start button.png")
    start = pygame.transform.scale( start , ( 130 , 50 ))
    game_over = False
    while not game_over :

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN :
                mx , my = pygame.mouse.get_pos()
                
                if mx > 803 and mx < 927 and my > 204 and my < 249 :
                    game_over = True

        
        window.fill (white)
        text_screen ( "space rocket" , red , 300 ,200 )
        window.blit(start , ( 800 , 200 ))

        

        pygame.display.update()






#game loop

def gameloop ():

    #game variable 

    game_exit = False
   

    rocket_x = 500
    rocket_y = 400

    # rock_y
    rock_velocity = 10


    rock_y = -1
    rock_y2 = -100
    rock_y3 = -30
    rock_y4 = -800
    rock_y5 = -500
    rock_y6 = -300

    rock_y7 = -600
    rock_y8 = -501
    rock_y10 = -30
    rock_y9 = -300
    rock_y11 = -1000
    rock_y12 = -800
    rock_y13 = -350

    clock = pygame.time.Clock()
    fps = 30

    rocket_velocity = 50

    rock_l = 50
    rock_b = 50

    #image load
    space = pygame.image.load("C:\\Python34\\rajeev\\image\\space.png")
    space = pygame.transform.scale(space , (window_length , window_breadth )).convert_alpha()

    rocket = pygame.image.load( "C:\\Python34\\rajeev\\image\\rocket.png" )
    rocket = pygame.transform.scale( rocket , ( 70 , 140))

    rock = pygame.image.load ( "C:\\Python34\\rajeev\\image\\bomb.png" )
    rock = pygame.transform.scale (rock , ( rock_l , rock_b ))


    while not game_exit :

    # rock variable
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if rocket_x < 1100 :
                        rocket_x += rocket_velocity

                if event.key == pygame.K_LEFT:
                    if rocket_x > 0 :
                        rocket_x -= rocket_velocity
                


          
        window.blit( space , (0 , 0) )
        
        window.blit ( rocket , (rocket_x , rocket_y))

    #rock
        
        window.blit( rock , ( 50 , rock_y ))
        rock_y += rock_velocity
        if rock_y > window_breadth + rock_b :
            rock_y = -100

        window.blit( rock , ( 500 , rock_y2 ))
        rock_y2 += rock_velocity
        if rock_y2 > window_breadth + rock_b :
            rock_y2 = -500



        window.blit( rock , ( 1000 , rock_y3 ))
        rock_y3 += rock_velocity
        if rock_y3 > window_breadth + rock_b :
            rock_y3  = -300

        
        window.blit( rock , ( 1100 , rock_y4 ))
        rock_y4 += rock_velocity
        if rock_y4 > window_breadth + rock_b :
            rock_y4 = -800


        window.blit( rock , ( 300 , rock_y5 ))
        rock_y5 += rock_velocity
        if rock_y5 > window_breadth + rock_b :
            rock_y5 = -500


        window.blit( rock , ( 800 , rock_y6 ))
        rock_y6 += rock_velocity
        if rock_y6 > window_breadth + rock_b :
            rock_y6 = -300





        window.blit( rock , ( 100 , rock_y7 ))
        rock_y7 += rock_velocity
        if rock_y7 > window_breadth + rock_b :
            rock_y7 = -100

        window.blit( rock , ( 300 , rock_y8 ))
        rock_y8 += rock_velocity
        if rock_y8 > window_breadth + rock_b :
            rock_y8 = -500



        window.blit( rock , ( 9000 , rock_y9 ))
        rock_y9 += rock_velocity
        if rock_y9 > window_breadth + rock_b :
            rock_y9  = -300

        
        window.blit( rock , ( 1100 , rock_y10 ))
        rock_y10 += rock_velocity
        if rock_y10 > window_breadth + rock_b :
            rock_y10 = -800


        window.blit( rock , ( 700 , rock_y11 ))
        rock_y11 += rock_velocity
        if rock_y11 > window_breadth + rock_b :
            rock_y11 = -500


        window.blit( rock , ( 800 , rock_y12 ))
        rock_y12 += rock_velocity
        if rock_y12 > window_breadth + rock_b :
            rock_y12 = -300


        window.blit( rock , ( 600 , rock_y13 ))
        rock_y13 += rock_velocity
        if rock_y13 > window_breadth + rock_b :
            rock_y13 = -300




        pygame.draw.rect( window , aqua , [ 0 , 0 , window_length , 30 ] )
        clock.tick(fps)
        pygame.display.update()

game_start()

gameloop()


        

           
   

pygame.quit()
quit()
