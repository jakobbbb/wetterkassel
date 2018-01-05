import WetterKassel
from twitter.twitter_utils import calc_expected_status_length as st_len
import twitter.api
LIMIT = twitter.api.CHARACTER_LIMIT # 280 from 3.3.1 onwards

class tweetbuild:
    def __init__(self, data, tweettime):
        self.data = data # weather data
        self.tweettime = tweettime # 0 for todays weather, 1 for tomorrow
        self.tweettext = ""

    # appends string to tweettext while keeping length <= LIMIT
    def add(self, addition): 
        if (st_len((self.tweettext + addition).encode("utf-8")) <= LIMIT):
            self.tweettext += addition
            return True
        else:
            return False

    def build(self):
        if self.tweettime == 0:
             self.add("Heute: ")
        else:
            self.add("Morgen: ")
        self.add( u"%s\N{DEGREE SIGN}C bis %s\N{DEGREE SIGN}C. " % (round(self.data["temperatureMin"],1), round(self.data["temperatureMax"],1)))
        self.add( self.data["summary"].strip("."))
        self.add(" " + WetterKassel.weathericons.emoji(self.data["icon"]) + ". ")
        self.add("Wind: " + str(int(round(self.data["windSpeed"],0))) + "km/h. ")
        # use abbreviations if needed
        if not self.add("Luftfeuchtigkeit: " + str(int(round(self.data["humidity"]*100,0))) + "%. "):
            self.add("Luftf.: " + str(int(round(self.data["humidity"]*100,0))) + "%. ")
        if not self.add("Regenwahrscheinlichkeit: " + str(int(round(self.data["precipProbability"]*100,0))) + "%. "):
            self.add("Regenwahrsch.: " + str(int(round(self.data["precipProbability"]*100,0))) + "%. ")
        return self.tweettext
        
