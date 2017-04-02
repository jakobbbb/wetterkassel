from WetterKassel import config
import requests

class weatherapi:
    def __init__(self):
        pass
       
    def url(self):
        url = "https://api.darksky.net/forecast/" #base url
        url += config.weatherapi.key
        url += "/" + config.weatherapi.lat + "," + config.weatherapi.lon + "/?"
        for param, value in config.weatherapi.params.iteritems():
            url += "&%s=%s" % (param, value)
        return url

    def getdata(self, dummy=False):
        if not dummy:
            r = requests.get(self.url())
            return r.json()
        else: # for testing, to avoid having to fetch actual data
            from json import loads
            with open("WetterKassel/dummy/dummydata.json", "r") as f:
                return loads(f.read())



class weathericons:
    @staticmethod
    def emoji(icon):
        emojis = {
            "clear-day" : u"\U00002600",
            "clear-night" : u"\U00002600",
            "rain" : u"\U00002614",
            "snow" : u"\U00002744",
            "wind" : u"\U0001F4A8",
            "fog" : u"\U0001F301",
            "cloudy" : u"\U00002601",
            "partly-cloudy-day" : u"\U000026C5",
            "partly-cloudy-night" : u"\U000026C5"
        }
        if icon in emojis.keys():
            return emojis[icon]
        else:
            return ""
