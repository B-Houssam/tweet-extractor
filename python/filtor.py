from json.decoder import JSONDecodeError
import regex as re
import pickle
import json
import pandas as pd
from textblob import TextBlob
from twitter_client import *
from Matweet import Tweet
from os import error, listdir
from os.path import isfile, join
import os 
import datetime as dt

def filter(path,parent):
    rpath = os.getcwd()+"/python/corp/data2.0/" + parent
    try:
        os.mkdir(rpath)
    except OSError as e:
        print('parent exist')
    file = open(path,"r")
    dirs = file.read().splitlines()
    file.close()
    for d in dirs:
        try:
            os.mkdir(os.path.join(rpath,d))
        except OSError as error:
            print("file already exist skipping ahead")
        finally:
            print("going to the next file")

def groupor():
    rpath = os.getcwd()+"/python/corp/data/"
    cpath = os.getcwd()+"/python/corp/data2.0/companies/"
    spath = os.getcwd()+"/python/corp/data2.0/smartphones/"
    lpath = os.getcwd()+"/python/corp/data2.0/laptops/"
    corp = [f for f in listdir(os.getcwd()+'/python/corp/data/')]
    companies = [f for f in listdir(cpath)]
    smartphones = [f for f in listdir(spath)]
    laptops = [f for f in listdir(lpath)]
    for c in corp :
        tweetArray = []
        entity = c.split("-")[0]
        if entity in companies:
            with open(cpath+entity+"/"+c,"wb") as w:
                with open(rpath+c,"r",encoding="utf-8") as read:
                    try:
                        data = json.load(read)
                    except JSONDecodeError as e:
                        print(c +" is the one causing error")
                for tweet in data["tweets"]:
                    tempo = Tweet(tweet["id"],tweet["text"],str(tweet["created_at"]),tweet["retweet_count"],tweet["favorite_count"],tweet["lang"],tweet["user_id"],tweet["coordinates"],tweet["geo"])
                    tweetArray.append(tempo)
                w.write(json.dumps({'tweets':[o.dump() for o in tweetArray]},indent=4,ensure_ascii=False).encode("utf8"))


        elif entity in smartphones:
            with open(spath+entity+"/"+c,"wb") as w:
                with open(rpath+c,"r",encoding="utf-8") as read:
                    try:
                        data = json.load(read)
                    except JSONDecodeError as e:
                        print(c +" is the one causing error")
                for tweet in data["tweets"]:
                    tempo = Tweet(tweet["id"],tweet["text"],str(tweet["created_at"]),tweet["retweet_count"],tweet["favorite_count"],tweet["lang"],tweet["user_id"],tweet["coordinates"],tweet["geo"])
                    tweetArray.append(tempo)
                w.write(json.dumps({'tweets':[o.dump() for o in tweetArray]},indent=4,ensure_ascii=False).encode("utf8"))
        elif entity in laptops:
            with open(lpath+entity+"/"+c,"wb") as w:
                with open(rpath+c,"r",encoding="utf-8") as read:
                    try:
                        data = json.load(read)
                    except JSONDecodeError as e:
                        print(c +" is the one causing error")
                for tweet in data["tweets"]:
                    tempo = Tweet(tweet["id"],tweet["text"],str(tweet["created_at"]),tweet["retweet_count"],tweet["favorite_count"],tweet["lang"],tweet["user_id"],tweet["coordinates"],tweet["geo"])
                    tweetArray.append(tempo)
                w.write(json.dumps({'tweets':[o.dump() for o in tweetArray]},indent=4,ensure_ascii=False).encode("utf8"))

if __name__ == '__main__':
    #filter(os.getcwd()+'/python/corp/assets/companies.txt','companies')
    groupor()
    