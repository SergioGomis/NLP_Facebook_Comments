import pymongo
from config import dbURL

client = pymongo.MongoClient(dbURL)


class MongoObject():
    def __init__(self):
        self.mydb = client.get_default_database()
        self.tweets1Collection = self.mydb['jobs']
        self.tweets2Collection = self.mydb['proptech']
        self.tweets3Collection = self.mydb['covid']


    def addTweet(self,tweet):
        
        x = self.tweets1Collection.insert_one(tweet)
        return x

    def addTweetPT(self,tweet):
        
        x = self.tweets2Collection.insert_one(tweet)
        return x
    
    def addTweetCV(self,tweet):
        
        x = self.tweets3Collection.insert_one(tweet)
        return x