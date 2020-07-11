# -*- coding: utf-8 -*-

from datetime import datetime
from pytz import timezone

class Real_time():
    def __init__(self): 
        self.Tokyo_time = None
        self.Berlin_time = None
        self.New_York_time = None
         
    def Get_Time(self):
        tzTYO = timezone("Asia/Tokyo")
        self.Tokyo_time = datetime.now(tzTYO).strftime("%m/%d %H:%M")
         
        tzBel = timezone("Europe/Berlin")
        self.Berlin_time = datetime.now(tzBel).strftime("%m/%d %H:%M")
         
        tzNYC = timezone("America/New_York")
        self.New_York_time = datetime.now(tzNYC).strftime("%m/%d %H:%M")

        #print("Tokyo/Japan : Berlin/Europe : NewYork/USA")
        #print(self.Tokyo_time, " ", self.Berlin_time, " ", self.New_York_time, "\n")
        
        return self.Tokyo_time, self.Berlin_time,  self.New_York_time

if __name__ == "__main__":
    world_time = Real_time()
    tokyo_time, berlin_time, newyork_time = world_time.Get_Time()
    print(berlin_time, tokyo_time, newyork_time)
         