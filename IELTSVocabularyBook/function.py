# -*- coding: utf-8 -*-
import numpy as np

def Level_dataset(dirrect, level, start, end):
    dataset = []
    for i in range(start, end, 50):
        with open(dirrect+"\\"+level+"\\"+str(i)+"-"+str((i+50)-1)+".txt", "r") as f:
            for j in range(50):
                wdata = f.readline().split(":")
                number_word = wdata[0].split() 
                if j < (50-1): #delete "\n"
                    dataset.append( [number_word[0], number_word[1], wdata[1][:-1]] )
                else: #last loop    
                    dataset.append( [number_word[0], number_word[1], wdata[1]] )
              
    dataset = np.array(dataset) 
    return dataset 

def SentenceSplit(sentence):
    ans = False
    ecnt = slen = slencnt = 0
    
    for i in range(len(sentence)):
        if sentence[i] == " ":
            ecnt += 1
            if slen > 8:
                slencnt += 1
            
        elif sentence == ",":
            ans = True
                
        else:    
            slen += 1
    
    if slencnt >= 2:
        ans = True
        
    return ans, ecnt
