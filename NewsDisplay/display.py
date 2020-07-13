# -*- coding: utf-8 -*-
# main.py 

import turtle
turtle.Screen().bgcolor("black")

import time
import datetime
import calendar
from news_scrape import news_scrape
from train_time import Train_time
from worldtime import Real_time
from display_function import *


class Display():
    def __init__(self, top_news, worldtime, train_time):
        self.top_news = top_news
        
        self.Japan_Economy_top_news = None
        
        self.world_time = worldtime
        self.tokyo_time = None
        self.berin_time = None
        self.newyork_time = None
        
        self.train_time = train_time

        self.x = -900 #-570
        self.y = +400 # 280
        self.once_get_train = True
        self.tokyou_economy_get_news = True
        
    def Get_train_news(self, nowtime):
        
        if self.once_get_train == True or nowtime.hour == 4:
            self.train_time.Scrape()
            
            self.once_get_train = False

        
    def display(self):
        tur =  turtle.Turtle()
        tur.shape('turtle')
 
        while (True):
            x = self.x
            y = self.y
            tur.goto(x, y)
            tur.pu()
            tur.clear()
            
            nowtime = datetime.datetime.now()
            self.Get_train_news(nowtime)
            #time.sleep(1)
            tur.pencolor("white")
            
            # Display BBC top news 10 
            x, y = BBC_display(x, y, self.top_news.BBC_Scrape(), tur)

            if nowtime.hour != int(5) or nowtime.hour != int(17):
                flag = False

            if (nowtime.hour == int(5) or nowtime.hour == int(17) ) and flag == False:
                self.tokyou_economy_get_news = True
                flag = True

            # Display Japan_economy top news 10
            if self.tokyou_economy_get_news == True : 
                self.Japan_Economy_top_news = self.top_news.Japan_Economy_Scrape()
                self.tokyou_economy_get_news = False
            x, y = Japan_Economy_display(x, y, self.Japan_Economy_top_news, tur)

            # DIsplay World time
            self.tokyo_time, self.berlin_time, self.newyork_time = self. world_time.Get_Time()
            x, y = World_time_display(x, y, self.tokyo_time, self.berlin_time, self.newyork_time, tur)
         
            nowtime = datetime.datetime.now()
            x, y = Train_display(x, y, self.train_time.hour, self.train_time.hour2, 
                                 self.train_time.color, self.train_time.color2, 
                                 self.train_time.kyoubashi, self.train_time.shijounawate, nowtime, tur)
            
            #tur.goto(x, -200)
            #tur.write("Suminodo Station", 
            #          align="center", font=("Arial", 20, "normal"))

            tur.write(str(nowtime.hour)+" : "+str(nowtime.minute), 
                          align="center", font=("Arial", 100, "normal")) 
            
            tur.goto(450, -75)
            weekday = datetime.date.today().weekday()
            weekday_name = calendar.day_name[weekday]
            tur.write("(" + weekday_name + ")", align="center", font=("Arial", 45, "normal")) 
             
            time.sleep(10)

            
if __name__ == '__main__':
    top_news = news_scrape()
    world_time = Real_time() 
    train_time = Train_time()

    now_display = Display(top_news, world_time, train_time)
    now_display.display()
        