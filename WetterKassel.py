import WetterKassel
from time import time
from sys import argv , stderr, exit
from json import loads, dumps
from os import path

def main():
    if len(argv) != 2:
        print >> stderr, "[-] Wrong amount of arguments supplied." 
        exit(1)
    if argv[1] == "today":
        tweettime = 0 
    elif argv[1] == "tomorrow":
        tweettime = 1
    else: 
        print >> stderr, "[-] Wrong argument(s) supplied." 
        exit(1)

    # configuration
    configfile = "config.json"
    if path.isfile(configfile):
        with open(configfile, "r") as f:
            WetterKassel.config.config = loads(f.read())
    else:
        # generate empty config, exit
        print >> stderr, "[-] no config found, generating empty config"
        with open(configfile, "w+") as f:
            f.write(dumps(WetterKassel.config.config, sort_keys=True, indent=4))
        exit()

    # Get Data from Weather API
    wapi = WetterKassel.weatherapi()
    data = wapi.getdata(dummy=False) # get json weather data
    print "[+][%s] Got Weather Data" % str(time())

    # process data and build tweet
    daydata = data["daily"]["data"][tweettime]
    tweetbuilder = WetterKassel.tweetbuild(data=daydata, tweettime=tweettime)
    tweet = tweetbuilder.build()
    print "[+][%s] Built Tweet" % str(time())

    # post tweet
    tapi = WetterKassel.twitterapi()
    tapi.post(tweet.encode("utf-8")) # encode to fix issue under linux
    print "[+][%s] Sent Tweet" % str(time())
if __name__ == "__main__":
    main()
