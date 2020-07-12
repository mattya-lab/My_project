# -*- coding: utf-8 -*-

import requests
import numpy as np
import datetime
from bs4 import BeautifulSoup

class Train_time():
    def __init__(self):
        self.url = None
        self.date = None
        self.schedule = None
        self.hour = []  #kyounbashi
        self.hour2 = [] #shijounawate
        self.min = []
        self.color = None # (kyoubashi) color array
        self.color2 = None # (shijounawate) color array
        self.kyoubashi = None
        self.shijounawate = None
           
    
    def Scheduling(self, hour, color):
        #print(hour)
        #print(self.min)
        
        #print(type(color[10]))
        x = y = last_nowtime = 0
        hour = list( hour )
        color = list( color )
        self.min = list(self.min)
        mintime = np.zeros( (len(hour), 20), dtype = (int))
        color_min = np.zeros( (len(hour), 20), dtype = (int))
        
        
        for i in range( len(self.min) ):
            color_nowmin = int(color[i], 16)
            if color_nowmin == 0:
                color_nowmin = 1
            elif color_nowmin == 32768:
                color_nowmin = 2
            else : #color_nowmin == 16750848:
                color_nowmin = 3
                
            
            if i == 0:
                mintime[x][y] = self.min[i]
                color_min[x][y] = color_nowmin
            else:
                if last_nowtime < int( self.min[i] ):
                    #print(str(last_nowtime)+"<"+str(self.min[i]))
                    y += 1
                    mintime[x][y] = self.min[i]
                    color_min[x][y] = color_nowmin
                else: 
                    #print(str(last_nowtime)+">"+str(self.min[i]))
                    #print(self.min[i])
                    x += 1
                    y = 0
                    mintime[x][y] = self.min[i]
                    color_min[x][y] = color_nowmin
                                                   
            last_nowtime = int( self.min[i] )
            
        #print(mintime)
        #print(color_min)
        return mintime, color_min

    def Get_arriving_time(self): 
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        #print(soup)
        # Get train arriving information train  
        hour = soup.find_all("th", attrs={"class", "hour"})
        #print(hour)
        
        for i in range( len(hour) ):
            hour[i] = hour[i].get_text()
        #print(hour)
      
        self.min = soup.find_all("font", attrs = {"class", "min"})
        color = []
        #print(self.min)
        
        for i in range( len(self.min) ):
            minute = str( self.min[i] )
            color.append( minute[32:38] )
            self.min[i] = self.min[i].get_text()
                     
        mintime, color_min = self.Scheduling(hour, color)

        return mintime, hour, color_min
       
    def Scrape(self):
        self.date = datetime.datetime.now()

        month = self.date.month
        if month < 10:
            month = "0" + str(month)
                   
        day = self.date.day
        if day < 10:
            day = "0" + str(day)
        
        #URL page is 'JRおでかけネット'
        self.url =  "https://mydia.jr-odekake.net/cgi-bin/mydia.cgi?MODE=11&FUNC=0&EKI=住道&SENK=学研都市線&DIR=京橋・北新地・尼崎方面&DDIV=&CDAY=&DITD=2892067001100%2c2892067001400&COMPANY_CODE=4&DATE="            
        self.url = self.url+str(self.date.year)+str(month)+str(day)
        #print(self.url)
        #Suminodu station to Kyobasi, Amagasaki station
        self.kyoubashi, self.hour, self.color = self.Get_arriving_time()


        self.url =  "https://mydia.jr-odekake.net/cgi-bin/mydia.cgi?MODE=11&FUNC=0&EKI=住道&SENK=学研都市線&DIR=四条畷・松井山手方面&DDIV=&CDAY=&DITD=2892067002100%2c2892067002400&COMPANY_CODE=4&DATE="
        self.url = self.url+str(self.date.year)+str(month)+str(day)
        
        #Shijounawate, Doushisyamae station
        self.shijounawate, self.hour2, self.color2 = self.Get_arriving_time()

        
if __name__ == "__main__":
    traintime = Train_time()
    traintime.Scrape()