import speedtest
import datetime
import pymongo
from pymongo import MongoClient

# Set up the DataBase Connection
client = MongoClient()
db = client.SpeedTest

currentDT = datetime.datetime.now()

def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    # There is a lot more data in the res, I extracted the current data we were looking for.
    return res["download"]/1000000,res["upload"]/1000000, res["ping"], res['timestamp']

def post_mongo():
    d, u, p, t = test()
    post = {
    'localTime' : currentDT,
    'download' : d,
    'upload' : u,
    'ping' : p,
    'timeStamp' : t
    }
    posts = db.FromSwitch
    post_id = posts.insert_one(post).inserted_id
    

if __name__ == '__main__':
    post_mongo() 