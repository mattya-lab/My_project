# -*- coding: utf-8 -*-
import sqlite3 #record database ver 0.5.2 (pip install records==0.5.2)

class Database():
    def __init__(self, news_data):
        self.store_news = news_data
        self.store_data = []
        self.dbfile = None
        self.connection = None
        self.link = None
        self.nowtime = None
        self.now = None
        
    def create_table(self, nowtime):
        self.nowtime = nowtime
        now = str(nowtime.year)+"-"+str(nowtime.month)+"-"+str(nowtime.day)
        self.now = now
        #self.connection = sqlite3.connect("G:\\マイドライブ\\NewsDisplay\\database_file\\"+now+".db")
        self.connection = sqlite3.connect("G:\\マイドライブ\\NewsDisplay\\database_file\\Test.db")
        self.dbfile = self.connection.cursor()
        self.dbfile.execute("CREATE TABLE IF NOT EXISTS Japan (datetime, topic);")
        
    def store_news_topic(self): #Store_news    
        for topic in range( len(self.store_news) ):
            self.store_data.append([self.now, self.store_news[topic]])
            
        self.dbfile.executemany("INSERT INTO japan VALUES(?, ?);", self.store_data)
        self.connection.commit()
        self.connection.close()
        
    def check_topic(self):
        
        for row in self.dbfile.execute("SELECT * FROM Japan"):
            print( row )   
        #self.connection.commit()
        #self.connection.close()

