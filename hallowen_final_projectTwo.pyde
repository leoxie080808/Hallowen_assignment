
page = 0
text_size = 30


def setup():
    
    
    global back_img
    global fence_img
    back_img = loadImage("wall_preview.png")
    fence_img = loadImage("fence_preview.png")
    
    
    size(1920,1080)
    
char_head = 0
char_body = 0
char_position = 0

ghost_head = 0
ghost_body = 0
    
def draw():
   
        
       
    
       background(0)
       image(back_img, 0,0,1920,1080)
    
       global char_head
       global char_body
       global char_position
       global ghost_head
       global ghost_body

       image(fence_img, 300, 300, 80, 80) #current position at left gateway
       image(fence_img, 710, 65, 80, 80)#middle-left top gate 
       image(fence_img, 1020, 65, 80, 80)
       image(fence_img, 935, 880, 80, 80)
       image(fence_img, 1500, 850, 80, 80)
       image(fence_img, 1580, 850, 80, 80)
       image(fence_img, 1420, 850, 80, 80)
       image(fence_img, 1370, 65, 80, 80)
    
    
       noStroke()
                        
    #character    
       fill(160,82,45) #head section
       rect(char_position+220+50,char_body+900-100,30,30)
    
       fill(255,235,205)#body
       rect(char_position+222.5+50, char_body+930-100, 25, 28)
    
       fill(255,222,173)#arms and legs
       rect(char_position+212+50, char_body+932-100, 10,10)#left arm
       rect(char_position+246+50, char_body+932-100, 10,10)# right arm
    
       rect(char_position+222+50, char_body+955-100, 10,10)#left leg
       rect(char_position+238+50, char_body+955-100, 10, 10)#right leg    
        
       ghost_body +=1
       if ghost_body > 10:
           ghost_body = 0
    
       #ghost in the corner 
       fill(255,255,255)#put a swuare, then rectangle with over-lapping sides but not as tall, then some small cubes on bottom as feet
       rect(ghost_head+100, 50, 40, 40)
       rect(ghost_head+90, 60, 60,50)
       rect(ghost_body+90, 110, 10, 10)
       rect(ghost_body+110, 110, 10, 10)
       rect(ghost_body+130, 110, 10, 10)
       fill(255, 255, 255) #for number two
       rect(ghost_head+300, 350, 40, 40)
       rect(ghost_head+290, 360, 60, 50)
       rect(ghost_body+290, 410, 10, 10)
       rect(ghost_body+310, 410, 10, 10)
       rect(ghost_body+330, 410, 10, 10)
       fill(255, 255, 255)#for number three 
       rect(ghost_head+1500, 380+20, 40, 40)
       rect(ghost_head+1490, 390+20, 60, 50)
       rect(ghost_body+1490, 440+20, 10, 10)
       rect(ghost_body+1510, 440+20, 10, 10)
       rect(ghost_body+1530, 440+20, 10, 10)
       (255,255,254) # FOURTH GHOST
       rect(ghost_head+1200, 280, 40, 40)
       rect(ghost_head+1190, 290, 60, 50)
       rect(ghost_body+1190, 340, 10, 10)
       rect(ghost_body+1210, 340, 10, 10)
       rect(ghost_body+1230, 340, 10, 10) 
           
                     #sum eyes
       fill(0)
       rect(ghost_head+105, 60, 10, 10)
       rect(ghost_head+125, 60, 10, 10)
       rect(ghost_head+100, 75, 10, 10)
       rect(ghost_head+110, 85, 10, 10)
       rect(ghost_head+120, 85, 10, 10)
       rect(ghost_head+130, 75, 10, 10)
    
       fill(0)#for number two
       rect(ghost_head+305, 360, 10, 10)
       rect(ghost_head+325, 360, 10, 10)
       rect(ghost_head+300, 375, 10, 10)
       rect(ghost_head+310, 385, 10, 10)
       rect(ghost_head+320, 385, 10, 10)
       rect(ghost_head+330, 375, 10, 10)
    
       #for number three 
       fill(0)
       rect(ghost_head+1505, 410, 10, 10)
       rect(ghost_head+1525, 410, 10, 10)
       rect(ghost_head+1500, 425, 10, 10)
       rect(ghost_head+1510, 435, 10, 10)
       rect(ghost_head+1520, 435, 10, 10)
       rect(ghost_head+1530, 425, 10, 10)
       
       fill(0)#the last ghost 
       rect(ghost_head+1205, 290, 10, 10)
       rect(ghost_head+1225, 290, 10, 10)
       rect(ghost_head+1200, 305, 10, 10)
       rect(ghost_head+1210, 315, 10, 10)
       rect(ghost_head+1220, 315, 10, 10)
       rect(ghost_head+1230, 305, 10, 10)
    
def keyPressed():
    global char_position
    global char_body
    if key =='d':
        char_position = char_position+7
    if key =='w':
        char_body = char_body-7
    if key =='a':
        char_position = char_position - 7
    if key =='s':
        char_body = char_body +7  
    
   
