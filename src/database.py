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
    
    def getTweetsCV(self,langu):

        query = self.tweets3Collection.find({"metadata.iso_language_code":langu},{"_id":0,"id":1,"created_at":1,"user.screen_name":1,"full_text":1})
        return query