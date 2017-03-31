import WetterKassel
from time import time
from sys import argv , stderr, exit

def main():
    if len(argv) != 2:
        print >> stderr, "[-] Wrong amount of arguments supplied." 
        exit(1)
    if argv[1] == "morning":
        tweettime = 0 # current day
    elif argv[1] == "evening":
        tweettime = 1 #next day
    else: 
        print >> stderr, "[-] Wrong argument(s) supplied." 
        exit(1)
        
    wapi = WetterKassel.weatherapi()
    data = wapi.getdata(dummy=False) # get json weather data
    print "[+][%s] Got Weather Data" % str(time())
    daydata = data["daily"]["data"][tweettime]
    tweetbuilder = WetterKassel.tweetbuild(data=daydata, tweettime=tweettime)
    tweet = tweetbuilder.build()
    print "[+][%s] Built Tweet" % str(time())
    tapi = WetterKassel.twitterapi()
    tapi.post(tweet.encode("utf-8")) # encode to fix issue under linux
    print "[+][%s] Sent Tweet" % str(time())
if __name__ == "__main__":
    main()
