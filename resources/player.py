import pygame
import resources 
class Player(pygame.sprite.Sprite): 
    def __init__(self,size_x, size_y,color='red'):
        super().__init__()
        self.image = pygame.surface.Surface((size_x, size_y))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.v = 0
    def get_position(self):
       return (self.rect.x,self.rect.y)
    
    def set_position(self, x,y):
       self.rect.x = x
       self.rect.y = y
    def handle_keys(self, dt,key_up, key_down,key_right,key_left,screen):
        key = pygame.key.get_pressed()
        self.v = 5
        x = self.v * dt
        
      
         
        if key[ord(key_left)]:
           self.rect.move_ip(-x, 0)
        if key[ord(key_right)]:
           self.rect.move_ip(x, 0)
        if key[ord(key_up)]:
           self.rect.move_ip(0, -x)
        if key[ord(key_down)]:
           self.rect.move_ip(0, x)

        self.rect.clamp_ip(screen.get_rect())
        
      
         
            



            
            
          

     
       

