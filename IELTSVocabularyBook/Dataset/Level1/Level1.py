# -*- coding: utf-8 -*-
import numpy as np
import random
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def Level_dataset(dataset, start, end):
    for i in range(start, end, 50):
        with open(str(i) + "-" + str((i+50)-1) + ".txt") as f:
            for j in range(50):
                wdata = f.readline().split(":")
                number_word = wdata[0].split() 
                if j < (50-1): #delete "\n"
                    dataset.append( [number_word[0], number_word[1], wdata[1][:-1]] )
                else: #last loop    
                    dataset.append( [number_word[0], number_word[1], wdata[1]] )
    return dataset 

level1 = [] #score level 5.5 point
level1 = Level_dataset(level1, 1001, 1500)
level1 = np.array(level1) 
#level3 = [] #score level 6.0 point
#level3 = Level_dataset(level3, 1501, 1550) 
#level3 = np.array(level3)   
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def main():
    select = input("1:Search word, 2:Create 10 random words: ")

    if int(select) == 1:
        #Search Word function
        word = input("Search Word: ")

        for i in range(0, 500):
            if level1[i][1] == str(word) :
                print(level1[i][0] + " " + level1[i][1] + ": " + level1[i][2])
            
    elif int(select) == 2:
        print("Level1")
        #output random word
        for i in range(20):
            number = random.randint(1001, 1500)#1001<=number<=1250
            for j in range(0, 500):
                if level1[j][0] == str(number) :
                    print(level1[j][0] + " " + level1[j][1] +  ": " + level1[j][2])
    else:
        print("No process")
    
#Function()
main()
    