import pygame 
import random
pygame.init()
pygame.font.init()


lost=False
H,W=750,1200
q=0
laservel=2
screen=pygame.display.set_mode((W,H))
bg=pygame.transform.scale(pygame.image.load("background.png"),(600,750))
bg_height=bg.get_height()
bg_width=bg.get_width()

ship=pygame.image.load("ship.png")
ship2=pygame.image.load("ship+.png")
blueship=pygame.image.load("blue.png")
greenship=pygame.image.load("green.png")

yellowship=pygame.image.load("yellow.png")
redship=pygame.image.load("red.png")

health=pygame.image.load("health.png")
shiplaser=pygame.image.load("goldenlaser2.png")
enemylaser_red=pygame.image.load("pixel_laser_red.png")
enemylaser_blue=pygame.image.load("pixel_laser_blue.png")
enemylaser_green=pygame.image.load("pixel_laser_green.png")
enemylaser_yellow=pygame.image.load("pixel_laser_yellow.png")
main_font=pygame.font.SysFont("arial",40,1)
score_font=pygame.font.SysFont("arial",30,1)

health_height=health.get_height()
health_width=health.get_width()

collision_music=pygame.mixer.Sound("laser11.wav")
collision_music.set_volume(.6)
triumph=pygame.mixer.Sound("won.wav")





class laser():

    def __init__(self,x,y,w,h,laserimg,d):
        self.x= x+w/2-d
        self.y= y+h/2
        self.height=laserimg.get_height()
        self.width=laserimg.get_width()
        self.img=laserimg
        self.mask=pygame.mask.from_surface(self.img)
       
        
      
    def load_laser_pos(self):
        screen.blit(self.img,(self.x,self.y))
    def updatinglaser(self,laservel):

        self.y-=laservel
    def collision(self,obj,val,neg=0):
        
        offset=(int(self.x-obj.x-neg),int(self.y-obj.y))
        if self.mask.overlap(obj.mask,offset) != None :
            obj.health-=val
            return True
        return False
            
    
    


class ships():
    def   __init__(self,shipimg,x,y,laserimg,vel,health):
        self.shipimg=shipimg
        self.x=x
        self.y=y
        self.height=self.shipimg.get_height()
        self.width=self.shipimg.get_width()
        self.mask=pygame.mask.from_surface(self.shipimg)
        self.laserimg=laserimg
        self.health=health
        self.vel=vel
        
       
        self.mask=pygame.mask.from_surface(self.shipimg)
    def load_ship(self):
         self.Ship=screen.blit(self.shipimg,(self.x,self.y))
    def move(self):
        self.y+=self.vel
    
            
    

    
        

class playership (ships):
    
    def __init__(self,shipimg):
        super().__init__(shipimg,W/2-50,H-150,shiplaser,50,50)
        self.laser_list=[]
      
        
    def load_laser(self):
        
            l=laser(self.x,self.y,self.width,-self.height,self.laserimg,8)
            self.laser_list.append(l)

        
   
        

            
           
            
       
        
        
    def healthbar(self):
         
        green_rect= pygame.draw.rect(screen,(0,255,0),pygame.Rect(self.x-5,self.y+self.height+15,self.width+10,10)) 
        red_rect= pygame.draw.rect(screen,(255,0,0),pygame.Rect(self.x-5,self.y+self.height+15,(self.width+10)-(self.width+10)*(self.health/50),10)) 
        
    
     
        
    
class enemyship(ships):
    Color_ship={"Red":(redship,enemylaser_red),
            "Yellow":(yellowship,enemylaser_yellow),
            "Blue":(blueship,enemylaser_blue),
            "Green":(greenship,enemylaser_green)}
    def __init__(self,xcolor,x,y,vel,health=20):
        img=self.Color_ship[xcolor][0]
        limg=self.Color_ship[xcolor][1]
        
       
        super().__init__(img,x,y,limg,vel,health)
        
        self.laser_list=[]
    def load_laser(self):
        l=laser(self.x,self.y,self.width,self.height,self.laserimg,42.5)
        self.laser_list.append(l)
    def collision(self,obj,val,neg=(0,0)):
        offset=(int(self.x-obj.x),int(self.y-obj.y))
        if self.mask.overlap(obj.mask,offset) != None :
            obj.health-=val
            return True
        return False
            
    




def loadscreencomponents(level,lives,score):

               

                
                  
             
                  
                screen.blit(bg,(W/4,0))  
                level_label=main_font.render(f"LEVEL:{level}",True,(195,185,200))
                level_label_width,level_label_height=level_label.get_width(),level_label.get_height()
                screen.blit(level_label,(3*W/4-level_label_width-18,level_label_height-40))
                   
                   
                x=0
                for i in range(lives):
                       
                       screen.blit(health,(x+W/4,10))
                       x+=health_width+5
                if lost :
                        gameover(score)
              
def score_blit(score,wid,hgh):
    score=score_font.render(f"HIGHSCORE :{score}",True,(233,193,200))
  
    screen.blit(score,(wid,hgh))

def gameover (score):
    
    
    
    over=main_font.render("GAME OVER!!",True,(233,193,200))
    over_height=over.get_height()
    over_width=over.get_width()
    screen.blit(over,(W/4+bg_width/2-over_width/2,bg_height/2-over_height/2))
    score_blit(score,W/4+bg_width/2-over_width/2+10,bg_height/2-over_height/2+50)
   
def main_menu():
    screen.blit(bg,(W/4,0))
    begin=main_font.render("PRESS MOUSE TO START!!",True,(255,255,255))
    begin_height,begin_width=begin.get_height(),begin.get_width()
    screen.blit(begin,(W/4+bg_width/2-begin_width/2,bg_height/2-begin_height))
    pygame.mixer.music.load("OCT_26_2018_Harmorx2_Warplanets_game_loop_harmorX3_Space_scene_music.ogg")
    

    
    run=True
    while run :
            pygame.display.update()
            for events in pygame.event.get():
                if events.type== pygame.QUIT :
                    run=False
                if events.type==pygame.MOUSEBUTTONDOWN :
                      pygame.mixer.music.play(-1)
                      play()
                      run=False
                      quit()
            
def pause():
    
    begin=main_font.render("PRESS MOUSE TO CONTINUE",True,(255,255,255))
    begin_height,begin_width=begin.get_height(),begin.get_width()
    screen.blit(begin,(W/4+bg_width/2-begin_width/2,bg_height/2-begin_height))
   
    pygame.mixer.music.pause()


    run =True
    

    while run :
            pygame.display.update()
            for events in pygame.event.get():
                if events.type== pygame.QUIT :
                    run=False
                    quit()
                if events.type==pygame.MOUSEBUTTONDOWN :
                      run=False
                      pygame.mixer.music.unpause()
                     
def winner(score):
    screen.blit(bg,(W/4,0))
    won=main_font.render("YOU WON!!",True,(233,193,200))
    won_height=won.get_height()
    won_width=won.get_width()
    screen.blit(won,(W/4+bg_width/2-won_width/2,bg_height/2-won_height/2))
    score_blit(score,W/4+bg_width/2-won_width/2+10,bg_height/2-won_height/2+50)
    pygame.mixer.Sound.play(triumph)
    pygame.mixer.music.stop()
    

def restart ():
        pygame.mixer.music.pause()
        screen.blit(bg,(W/4,0))
        restrt=main_font.render("PRESS MOUSE TO RESTART !!",True,(255,255,255))
        restrt_height,restrt_width=restrt.get_height(),restrt.get_width()
        screen.blit(restrt,(W/4+bg_width/2-restrt_width/2,bg_height/2-restrt_height))
        run =True
    

        while run :
            pygame.display.update()
            for events in pygame.event.get():
                if events.type== pygame.QUIT :
                    run=False
                    quit()
                if events.type==pygame.MOUSEBUTTONDOWN :
                      run=False
                      pygame.mixer.music.play()
                      play()
     

    

        
def play():
    

    
    
    clock=pygame.time.Clock()
    player=playership(ship)
    vel=15
    wavelenght=5
    enemies=[]
    run=True
    
    c=0
    lives=5
    
    level=0
    laserlevel=2
    y_val=0
  
    countr = 0
    score=0
    
    
    while run:
            pygame.display.update()

            for event in pygame.event.get():
                   if event.type== pygame.QUIT:
                      quit()
                
            keys=pygame.key.get_pressed()
            if keys[pygame.K_a] and player.x -vel >= W/4:
                           player.x-=vel
            elif keys[pygame.K_d] and  (player.x+ vel + player.width ) <  W/4+bg_width:
                           player.x+=vel
            elif keys[pygame.K_w] and player.y - vel >200 :
                           player.y-=10
            elif keys[pygame.K_s] and player.y+vel+player.width  < H-50:
                           player.y+=10
            elif keys[pygame.K_p] :
                  pause()
            elif keys[pygame.K_SPACE] and (len(player.laser_list)==0 or player.laser_list[-1].y<player.y -100 ):
                        
                            player.load_laser()
                            
                  
            loadscreencomponents(level,lives,score)
            
            player.load_ship()
            player.healthbar()
           
            if lives==0 :
                     
                      
                      if countr !=300 :
                          gameover(score)
                          countr+=1
                      elif countr==300:
                          run=False
                          restart()
                      continue
            if player.health<=0 :
                lives-=1 
                player.health=50
            if level == 10:
                winner(score)
               
               
           

                      
               
            
            
           


            
            if len(enemies)==0 and lives!=0:
               level+=1
               wavelenght +=1
               
               
               for i in range(wavelenght):
                    while abs(y_val -c)<100:
                        y_val=random.randrange(-1000,-100,100)
                    c=y_val
                        
                            

                    enemy=enemyship(random.choice(["Red","Yellow","Green","Blue"]),random.randrange(W/4+50,W/4+bg_width-50,50),y_val,random.randrange(2,4))
                    
                    enemies.append(enemy)
                    enemy.load_ship()
            else :
              for i in enemies[:]:
                    if i.y+ i.height + i.vel< H :
                        i.load_ship()
                      
                        i.move()
                        if len(i.laser_list)==0 and i.y >50  and player.y-i.y>200 :
                            i.load_laser()
                           
                            
                        for j in i.laser_list[:]:
                            if  j.y > j.height + i.y + i.height/2 +500 and len(i.laser_list)<laserlevel and i.y +i.height/2 < player.y -player.height:
                                i.load_laser()
                            elif j.y + i.vel+2 <= H :
                               j.load_laser_pos()
                               j.updatinglaser( -i.vel-2)
                               if j.collision(player,2):
                                   pygame.mixer.Sound.play(collision_music)
                                   i.laser_list.remove(j)
                               
                               
                            
                          
                            else :
                               i.laser_list.remove(j)
                               
                       

                              
                    elif i.health<=0 :
                        enemies.remove(i)
                        
                    
                         
                    elif i.y+i.height+i.vel==H:
                    
                        enemies.remove(i)
                       # lost = True
                        #break
                    else :
                        enemies.remove(i)
                        lives-=1
                    if i.collision(player,5) :
                                
                                enemies.remove(i)
                    
                    
            

                        
            for i in player.laser_list[:]:
                if i.y - 10 >= 0- i.height :
                    i.load_laser_pos()
                    i.updatinglaser(10)
                    
                    
                    for enemy in enemies[:] :
                       if   i.collision(enemy,20,enemy.width) and i in player.laser_list[:] :
                           pygame.mixer.Sound.play(collision_music)
                           player.laser_list.remove(i)
                           enemies.remove(enemy)
                           
                           
                           score+=1
                           
                
                else :
                    player.laser_list.remove(i)
            
               

              
            


                        
                

           
            
            
            clock.tick(59)
           


main_menu()
quit()
#quit()

           


