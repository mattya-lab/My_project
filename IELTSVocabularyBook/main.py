# -*- coding: utf-8 -*-
from function import Level_dataset, SentenceSplit
import random
import time
import turtle

class IELTS_Vocabrary:
    def __init__(self):
        #""" Read dataset from requested file """ 
        self.dirrect="G:\マイドライブ\IELTS word 3500\Dataset\\"
        self.level1 = Level_dataset(self.dirrect, "Level1", 1001, 1500) #level5.5
        self.level2 = Level_dataset(self.dirrect, "level2", 1501, 2000) #level6.0
        self.level3 = Level_dataset(self.dirrect, "Level3", 2001, 2500) #level6.5
        self.level4 = Level_dataset(self.dirrect, "Level4", 2501, 3000) #level7.0
        
        #"""Display each data contents"""
        self.number = None
        self.word = None
        self.sentence = None
        self.color = ['orangered', 'green', 'chartreuse', 'blue', 'aqua',
                      'hotpink', 'white', 'gold', 'orange', 'purple']
        self.font_size = [45, 60, 75]
        
    
    def BookOrderWord(self, level, num):
        if level == 0:
            self.number = self.level1[num][0]
            self.word = self.level1[num][1]
            self.sentence = self.level1[num][2]
            
        elif level == 1:
            self.number = self.level2[num][0]
            self.word = self.level2[num][1]
            self.sentence = self.level2[num][2]
            
        elif level == 2:
            self.number = self.level3[num][0]
            self.word = self.level3[num][1]
            self.sentence = self.level3[num][2]
            
        elif level == 3:
            self.number = self.level4[num][0]
            self.word = self.level4[num][1]
            self.sentence = self.level4[num][2]
            
        num = num + 1
        if num == 500:
            level = level + 1
            if num == 500 and level == (3 + 1):
                level = 0
            num = 0
            
        return self.number, self.word, self.sentence, level, num 
           
    def RandomGetWord(self):
        level = random.randint(0, 3)
        num = random.randint(0, 500-1)
        
        if level == 0: #level1(over 5.5 score)
            self.number = self.level1[num][0]
            self.word = self.level1[num][1]
            self.sentence = self.level1[num][2]
            
        elif level == 1: #level2(over 6.0 score)
            self.number = self.level2[num][0]
            self.word = self.level2[num][1]
            self.sentence = self.level2[num][2]
            
        elif level == 2: #level3(over 6.5score)
            self.number = self.level3[num][0]
            self.word = self.level3[num][1]
            self.sentence = self.level3[num][2]
        
        else:
            self.number = self.level4[num][0]
            self.word = self.level4[num][1]
            self.sentence = self.level4[num][2]
            
        return self.number, self.word, self.sentence
    
    def Graphic_Drawing(self):
        tur = turtle.Turtle()
        tur.shape('turtle')
        turtle.bgcolor("black")
        level = num = 0

        while (True):
            x = -500
            y = 100
            tur.clear()
            try:
                self.number, self.word, self.sentence = self.RandomGetWord()
                #self.number, self.word, self.sentence, level, num = self.BookOrderWord(level, num)
 
                
                color_num = random.randint(0, len(self.color) - 1)
                tur.pencolor(self.color[color_num])
                tur.pu()
                #--- word number ---
                for i in range( len(self.number) ):
                    tur.goto(x, y)
                    tur.write(self.number[i], align="center", font=("Arial", self.font_size[-1], "normal"))
                    tur.pu()
                    x += 80
                    time.sleep(2/10)
                    
                #--- word --- 
                x = abs(-400 + 200)
                tur.goto(x, y)
                if len(self.word) >= 12:
                    tur.write(self.word, align="center", font=("Arial", self.font_size[-2], "normal"))
                else:
                    tur.write(self.word, align="center", font=("Arial", self.font_size[-1], "normal"))
                time.sleep(2)

                #--- sentence ---
                x = 0  
                y = -100
                tur.goto(x, y)
                nowecnt = 0
                ans, ecnt = SentenceSplit(self.sentence)
                
                if ans == False:
                    tur.write(self.sentence, align="center", font=("Arial", self.font_size[-2], "normal"))
                    time.sleep(5)
                else:
                    for  i in range(len(self.sentence)):
                        if self.sentence[i] == " ":
                            nowecnt += 1
                            if nowecnt == ( int(ecnt/2) + 1 ):
                                upsentence = self.sentence[:i]
                                undersentence = self.sentence[i+1:-1]
                                    
                    tur.write(upsentence, align="center", font=("Arial", self.font_size[0], "normal"))
                    time.sleep(2)
                    tur.goto(x, y-100)
                    tur.write(undersentence, align="center", font=("Arial", self.font_size[0], "normal"))
                    time.sleep(6)
                    
            except KeyboardInterrupt:
                break            
        
    def SearchWord(self):
        word = input("Search Word: ")
        for i in range(500):
            if word == self.level1[i][1]:
                print(self.level1[i][0] + " " + self.level1[i][1] + ":" + self.level1[i][2])            
            elif word == self.level2[i][1]:
                print(self.level2[i][0] + " " + self.level2[i][1] + ":" + self.level2[i][2])            
            elif word == self.level3[i][1]:
                print(self.level3[i][0] + " " + self.level3[i][1] + ":" + self.level3[i][2])              
            elif word == self.level4[i][1]:
                print(self.level4[i][0] + " " + self.level4[i][1] + ":" + self.level4[i][2])
                
IELTS = IELTS_Vocabrary()
#IELTS.SearchWord()
IELTS.Graphic_Drawing()