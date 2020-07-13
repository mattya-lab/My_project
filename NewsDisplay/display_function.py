# -*- coding: utf-8 -*-

import numpy as np

def BBC_display(x, y, BBC_top_news, tur):

    for i in range(11):
        if i == 0:
            tur.write("BBC News", align="left", font=("Arial", 20, "normal"))
            y = y - 50 #30
        else :
            tur.write(str(i)+" : "+BBC_top_news[i-1], 
                       align="left", font=("Arial", 15, "normal"))
            y = y - 35 #28
        tur.goto(x, y)
        tur.pu()
    
    y = y - 50
    tur.goto(x, y)
    tur.pu()
    return x, y


def Japan_Economy_display(x, y, Japan_Economy_top_news, tur):
    for i in range(11):
        if i == 0:
            tur.write("Japan Economy News", align="left", font=("Arial", 20, "normal"))
            y = y - 50#30
        else :
            tur.write(str(i)+" : "+Japan_Economy_top_news[i-1], align="left", font=("Arial", 15, "normal"))
            y = y - 35#25
        tur.goto(x, y)
            
        
    x = 450 #330
    y = 400 #280
    tur.goto(x, y)
    
    return x, y


def World_time_display(x, y, tokyo_time, berlin_time, newyork_time, tur):
    tur.write("Tokyo/Japan : Berlin/Europe : NewYork/USA", align="center", font=("Arial", 20, "normal"))
    y = y - 50 #28
    tur.goto(x, y)
    tur.write(tokyo_time+"     "+berlin_time+"     "+newyork_time, 
              align="center", font=("Arial", 20, "normal"))
    
    return x, y


def Part_Train_Display(x, y, hour, color, dirrect, nowtime, tur):
    temp = x   
    x = x - 250
    y = -320
    tur.goto(x, y)
    
    # Search Current Hour (Kyoubashi)
    hour_index = -1
    hour = np.array(hour)
    for i in range(len(hour)):
        if int(hour[i]) == int(nowtime.hour):
            hour_index = i
        #print(hour_index)
            
    if hour_index == -1:
        return False
    
    train_num_cnt = 0
    train_num_bool = True
    dis_cnt = 0
    # Current train time schedule   
    for j in range(20):
        if color[hour_index][j] == int(1):
            tur.pencolor("white")
        else : #self.color == 2 or self.color == 3:
            tur.pencolor("orange")
                    
        if dirrect[hour_index][j] == 0:
            break
               
        if nowtime.minute < dirrect[hour_index][j]:
            
            if train_num_bool == True:
                for k in range(20):
                    if dirrect[hour_index][j + k] == 0:
                        train_num_bool = False
                        break
                    train_num_cnt = train_num_cnt + 1
                print(train_num_cnt)
            
            if train_num_cnt > 8:
                if dis_cnt < 8:
                    tur.goto(x, -310)#-270
                    tur.write(str(dirrect[hour_index][j]), 
                              align="center", font=("Arial", 15, "normal"))
                    x = x + 40 #30
                    if dis_cnt == 7:
                        x = temp - 250
                else:
                    tur.goto(x, -340)#290
                    tur.write(str(dirrect[hour_index][j]), 
                              align="center", font=("Arial", 15, "normal"))
                    x = x + 40 #30
                    
                dis_cnt = dis_cnt + 1
                
                
            else :  
            #print(nowtime.minute, "<", self.kyoubashi[hour_index][j])
                print(hour[i])
                tur.write(str(dirrect[hour_index][j]), 
                          align="center", font=("Arial", 15, "normal"))   
                x = x + 40 #30
                tur.goto(x, -320)#-280
    x = temp     
    x = x - 250        
    tur.goto(x, -370)
    
    # Next train hour time (kyoubashi)        
    for j in range(20):
        #print( len(hour), int(hour_index)+1 )
        if len( hour ) == ( int(hour_index) + 1 ):
            #print(len(self.hour), "==", hour_index+1)
            break
        
        if color[hour_index+1][j] == int(1):
            tur.pencolor("white")
        else : #self.color == 2 or self.color == 3:
            tur.pencolor("orange")
                
        if dirrect[hour_index+1][j] == 0:
            break
        #if nowtime.minute < self.kyoubashi[hour_index+1][j]:
        tur.write(str(dirrect[hour_index+1][j]), 
                  align="center", font=("Arial", 10, "normal"))  
        x = x + 30 #20
        tur.goto(x, -370)
      
    return True
        
def Train_display(x, y, hour, hour2, color, color2, 
                  kyoubashi, shijounawate, nowtime, tur):
    
    display_time_bool = False
    
    tur.goto(x, -250)
    tur.write("Kyoubashi"+"                 "+"Doushisha", 
              align="center", font=("Arial", 20, "normal"))

    #nowtime = datetime.datetime.now()
    display_time_bool = Part_Train_Display(330, y, hour, color, kyoubashi, nowtime, tur)
    display_time_bool = Part_Train_Display(750, y, hour2, color2, shijounawate, nowtime, tur)
    #600
    print(display_time_bool)
    
    tur.pencolor("white")
    tur.goto(450, 0)
    
    return x, y