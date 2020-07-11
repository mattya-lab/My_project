# -*- coding: utf-8 -*-

import requests
import datetime
from bs4 import BeautifulSoup 
from database import Database


class news_scrape():
    def __init__(self):
        self.url = None
        self.bbc = None
        self.japan_economy = None
        self.tokyo_economy = []
        
    def BBC_Scrape(self):
        self.url = requests.get("https://www.bbc.co.uk/news")
        self.bbc = []

        soup = BeautifulSoup(self.url.text, 'html.parser')
        headlines = soup.select(".gs-c-promo-heading__title")

        cnt = 0
        for headline in headlines :
            if cnt == 0:
                cnt += 1              
            elif cnt >= 10 + 1:
                break          
            else:
                print( str(cnt) + ": " + headline.get_text() )
                self.bbc.append( headline.get_text() )
                cnt += 1
        #print( self.bbc[1] )
        return self.bbc
        
    def Japan_Economy_Scrape(self):
        self.url = requests.get("https://www.nikkei.com/")
        self.japan_economy = []
        
        soup = BeautifulSoup(self.url.text, 'html.parser')
        headlines = soup.find_all("a", attrs={"class":"k-card__block-link"})
        
        for i in range( len(headlines) ):
            headlines[i] = headlines[i].contents[0].text 
            self.japan_economy.append( headlines[i] )
        
        #To Database module ( line 48 - 52)      
        Japan_economy_news_db = Database( self.japan_economy )
        nowtime = datetime.datetime.now()
        Japan_economy_news_db.create_table( nowtime )
        Japan_economy_news_db.store_news_topic()
        #Japan_economy_news_db.check_topic()
        
        for i in range(10):
            print(str(i+1) + ": " + headlines[i])
            self.tokyo_economy.append( headlines[i] )
            
        #print( self.tokyo_economy )
        return self.japan_economy
    
if __name__ == "__main__":
    top_news = news_scrape()
    BBC_top_news = top_news.BBC_Scrape()
    Japan_Economy_top_news = top_news.Japan_Economy_Scrape()
    