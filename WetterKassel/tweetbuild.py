import WetterKassel
from twitter.twitter_utils import calc_expected_status_length as st_len

class tweetbuild:
    def __init__(self, data, tweettime):
        self.data = data
        self.tweettime = tweettime
        self.tweettext = ""
    
    def add(self, addition):
        if (st_len((self.tweettext + addition).encode("utf-8")) <= 140):
            self.tweettext += addition
            return True
        else:
            return False

    def build(self):
        #return "Tweet!"
        if self.tweettime == 0:
             self.add("Heute: ")
        else:
            self.add("Morgen: ")
        self.add( u"%s\N{DEGREE SIGN}C bis %s\N{DEGREE SIGN}C. " % (round(self.data["temperatureMin"],1), round(self.data["temperatureMax"],1)))
        self.add( self.data["summary"].strip("."))
        self.add(" " + WetterKassel.weathericons.emoji(self.data["icon"]) + ". ")
        self.add("Wind: " + str(int(round(self.data["windSpeed"],0))) + "km/h. ")
        if not self.add("Luftfeuchtigkeit: " + str(int(round(self.data["humidity"]*100,0))) + "%. "):
            self.add("Luftf.: " + str(int(round(self.data["humidity"]*100,0))) + "%. ")
        if not self.add("Regenwahrscheinlichkeit: " + str(int(round(self.data["precipProbability"]*100,0))) + "%. "):
            self.add("Regenwahrsch.: " + str(int(round(self.data["precipProbability"]*100,0))) + "%. ")
        return self.tweettext
        
