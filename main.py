import pygame
import sys
import threading
from resources.client import connect_server,send,recv
from resources import *

connect_server()
thread = threading.Thread(target=recv)
thread.start()


screen = pygame.display.set_mode((1000, 600))
pygame.init()

# player set up
player = pygame.sprite.Group()
p1 = Player(100,100,'Red')
p2 = Player(100,100,'Blue')
player.add(p1)
player.add(p2)
p1.set_position(500,100)
player_pos = p1.get_position()


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            send("!DISCONNECT")
            exit()



    now = time.time()
    dt = (now - prev_time) * 100 
    prev_time = now


    p1.handle_keys(dt,'w','s','d','a',screen)
    player.draw(screen)
     
    if(player_pos != p1.get_position()):
        player_pos = p1.get_position()
        player_pos = 'p' + str(player_pos[0]) + ' ' + str(player_pos[1])
        send(player_pos)
        
    

    pygame.display.flip()
    screen.fill((12, 24, 36))

    
    
    clock.tick(FPS)


