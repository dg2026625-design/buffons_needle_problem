Web VPython 3.2
#Buffon's needle
import random
'''
needle_length  = 2
line_distant = 4

Percentage = 2*(needle_length) / pi * (line_distant)
so,pi = 2*(needle_length) / Percentage * line_distant

'''
counter_met = 0
counter_total =  0
#total number
needle_length = 3
Line_distant = 4

box(pos = vec(-50,Line_distant * 5-1,0),size = vec(1,Line_distant *10,1))
box(pos = vec(50,Line_distant * 5-1,0),size = vec(1,Line_distant *10,1))

box(pos = vec(0,-2,0),size = vec(100,1,1))
box(pos = vec(0,Line_distant * 10,0),size = vec(100,1,1))
#simulation framework

for i in range(10):
    A = box(pos = vec(0,Line_distant * i,0),size = vec(100,0.1,0.1))
    #creates untill y is 0,...,Line_disant*i

while True:
    rate(100)
    key = keysdown()
    if ' ' in key:
        imformation = []
        counter_total += 1
        #number plused
        
        box_x = random.uniform(-50,50)
        box_y = random.uniform(0,Line_distant*9)
        radian = random.uniform(0,360) * (pi/360)
        B = box(pos = vec(box_x,box_y,0),size = vec(needle_length,0.1,0.1))
        B.rotate(angle = radian,axis = vec(0,0,1))
        #needle is thrown to frameworks in every time        
        
        if 0 <= box_y <= Line_distant/2:
            distant = box_y
        
        elif Line_distant/2 <= box_y <= Line_distant*(3/2):
            distant = abs(Line_distant-box_y)
        
        elif Line_distant*(3/2) <= box_y <= Line_distant*(5/2):
            distant = abs(Line_distant*2-box_y)
        
        elif Line_distant*(5/2) <= box_y <= Line_distant*(7/2):
            distant = abs(Line_distant*3-box_y)
        
        elif Line_distant*(7/2) <= box_y <= Line_distant*(9/2):
            distant = abs(Line_distant*4-box_y)
            
        elif Line_distant*(9/2) <= box_y <= Line_distant*(11/2):
            distant = abs(Line_distant*5-box_y)
            
        elif Line_distant*(11/2) <= box_y <= Line_distant*(13/2):
            distant = abs(Line_distant*6-box_y)
            
        elif Line_distant*(13/2) <= box_y <= Line_distant*(15/2):
            distant = abs(Line_distant*7-box_y)
            
        elif Line_distant*(15/2) <= box_y <= Line_distant*(17/2):
            distant = abs(Line_distant*8-box_y)
            
        elif Line_distant*(17/2) <= box_y <= Line_distant*(19/2):
            distant = abs(Line_distant*9-box_y)
        #NoGaDa, calculating distant between line and needle
        
        if distant <= sin(radian)*(needle_length/2):
            B.color = vec(1,0,0)
            counter_met += 1
                #the time when the needle met 
        imformation.append(needle_length)
        imformation.append(Line_distant)
        imformation.append(counter_met/counter_total)#percentage

        print(f'pi predicted_val:{(2*needle_length/Line_distant)/(imformation[2])} , total_num = {counter_total}')
        #this val is going to pi   
