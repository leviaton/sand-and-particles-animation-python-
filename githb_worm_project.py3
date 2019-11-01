
import numpy 
import random

import cv2
import sys

dim_x = 1540            
dim_y = 750             
worm_size = 0       
worm_number = 10     
number_group = 500
offset_position_begin_x = 700      
offset_position_begin_y = 380     
offset_position_end_x = 752      
offset_position_end_y = 432     

activation_obstacles = False 
activation_trap = False   
info_box = True              
direction_change=False
vortex = True
v_sp = 5
v_jk =  3

def move_randomly(x,y,wind=None):
    if wind == None:
        wind = [0,0,0,0,0,0,0,0]
   
    ox = random.randint(-wind[1]-1,wind[1]+1)
   
    oy = random.randint(-wind[3]-1,wind[3]+1)

    clr1=random.randint(0,150)  ###########> r color
    clr2=random.randint(130,256)  ###########> g color
    clr3=random.randint(150,250)  ###########> b color

    x1=x2=x
    x1=y2=y

    if map_matrix[y2][x2] == 4 :
        return [x2 , y2]

    if   (x2>(wind[4]) and x2<(wind[5])) and (y2 >(wind[6]) and y2<(wind[7])) :
        x1 = x2 +wind[0]+ox 
        
        y1 = y2 +wind[2]+oy
    else:
        x1 = x2 + ox 
        y1 = y2 + oy

    if x1 in range(1 ,dim_x)  and y1 in range(1,dim_y) and map_matrix[y1][x1] !=1 and map_matrix[y1][x1] !=3 and map_matrix[y1][x1] !=4:
        
        
        cv2.circle(Fra, (x2,y2),worm_size ,(0,0,0),-1)   
        map_matrix[y2][x2] = 0                           
        

        cv2.circle(Fra, (x1,y1),worm_size ,(clr1,clr2,clr3),-1) 
        map_matrix[y1][x1] = 1                                  
        
        return [x1 , y1]  
    
        return [x2 , y2] 
    elif x1 <= dim_x and x1 >= 0 and y1 <= dim_y and y1 >= 0 and map_matrix[y1][x1] !=1 and map_matrix[y1][x1] !=3 and map_matrix[y1][x1] ==4 :
        
        cv2.circle(Fra, (x2,y2),worm_size ,(50,50,255),-1)
        map_matrix[y2][x2] = 4
        
        return [x2 , y2] 
    else :
        
        cv2.circle(Fra, (x2,y2),worm_size ,(clr1,clr2,clr3),-1)
        map_matrix[y2][x2] = 1
        
        return [x2 , y2] 
    
def print_inthebox(text_box, box_count ,y_box,x_box):
    show_text = text_box+str(box_count)

    cv2.putText(Fra,show_text,(y_box,x_box), font, 0.4, (0,0,0), 1, cv2.LINE_AA) 

def trap_box(x1,x2,y1,y2):

    for i in range(x1 ,x2):

        for t in range(y1 ,y2):
            cv2.circle(Fra,(i,t),0,(33,33,130),-1)
            map_matrix[t][i]=4
    return abs((y2-y1)*(x2-x1))
def obstecle_box(x1,x2 ,y1 ,y2):
    for i in range(x1 ,x2):

        for t in range(y1 ,y2):
            cv2.circle(Fra,(i,t),0,(85,50,10),-1)
            map_matrix[t][i]=3
def cell_generator(y):
    

    
    for i in range(worm_number):   
    
            worm = [random.randint(offset_position_begin_x,offset_position_end_x),random.randint(offset_position_begin_y,offset_position_end_y)]
            worms.append(worm)
            while worm  in worms and y <0 :    
                worm   =   move_randomly(worms[i][0],worms[i][1])
                y = y -1
            
    return y


Fra = numpy.zeros((dim_y, dim_x, 4),numpy.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.namedWindow('Lotfi Leviaton worm simulation Dz -------------  Version-2.4 ------------------------ I hope !', cv2.WINDOW_NORMAL)
cv2.rectangle(Fra,(0,0),(dim_x+1,dim_y+1),(93,89,87),-1) 


map_matrix = numpy.full((dim_y+1,dim_x+1),2) 
print(sys.getsizeof(map_matrix) , 1 in map_matrix)

worms =[]
worm = []
count_iteration = 0

worms_max_exided_number = (offset_position_end_y-offset_position_begin_y)*(offset_position_end_x-offset_position_begin_x)

print('maximum wors =', worms_max_exided_number,'worm_number', worm_number,'len(worms)', len(worms))
    
vx= round(((offset_position_end_x- offset_position_end_x)/2) + offset_position_begin_x)
vy =round(((offset_position_end_y- offset_position_end_y)/2) + offset_position_begin_y)


if vortex == True :

    wind_effect =[[-v_sp,v_jk,v_sp,v_jk,0,vx,0,vy],[v_sp,v_jk,v_sp,v_jk,0,vx,vy,dim_y+1]
    ,[-v_sp,v_jk,-v_sp,v_jk,vx,dim_x+1,0,vy],[v_sp,v_jk,-v_sp,v_jk,vx,dim_x+1,vy,dim_y+1]] 

else : 
    wind_effect =[[0,5,10,5,0,1540,0,750]]

if activation_obstacles == True :   
    
    obstecle_box(800,890,0,751)
    
    obstecle_box(800,820,160,245)
    
    obstecle_box(800,820,255,600)
    
    obstecle_box(550, 600, 500, 550)

    obstecle_box(0, 800, 550, 751)


trap1 =trap2 =trap3= trap4 =0
if activation_trap == True :
    
    trap1 =trap_box(400,420,200,220)
    
    #trap2 =trap_box(800,820,140,160)
    
    #trap3 = trap_box(800,820,180,300)
    
    #trap4 =trap_box( 730,780,700,750)
    


if info_box == True:
    
    obstecle_box(0, 255, 0, 100)


while worms_max_exided_number-worm_number >=0 :
    cv2.imshow('Lotfi Leviaton worm simulation Dz -------------  Final Version------------------------- I hope !', Fra)

    
    count_iteration += 1 


    if count_iteration%30 == 0 and direction_change==True and count_iteration>300 :

        wind_effect=[[random.randint(-10,10),random.randint(10,15),random.randint(-10,10),random.randint(10,15),0,1540,0,751]]


    
    if count_iteration%5 == 0   and number_group >0: 
        
        worms_max_exided_number=cell_generator(worms_max_exided_number)
        number_group -=1

    for t in wind_effect: 
        for i , worm in enumerate(worms) : 
            worms[i] =   move_randomly(worms[i][0],worms[i][1],t)
             

    if info_box == True :
        cv2.rectangle(Fra,(10,5),(240,95),(200,200,200),-1)
        total_traps =trap1+trap2+trap3+trap4 

        print_inthebox(' Total number of cells = ',(map_matrix==1).sum(),10,20)
        print_inthebox(' Total of dead cells = ', (map_matrix==4).sum()-total_traps ,10,50)
        print_inthebox(' Number of iteration = ',count_iteration,10,80)


    k = cv2.waitKey(10) 
    if k == 27:
        
        print((map_matrix==1).sum()-(map_matrix==4).sum()+total_traps ,worms_max_exided_number, count_iteration)
        
        break



cv2.destroyAllWindows()
