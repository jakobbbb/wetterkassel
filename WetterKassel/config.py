class config:
    class weatherapi:
        key = "" # ADD KEY HERE
        lat = "51.31"
        lon = "9.48"

# random coordinates for testing
#        from random import uniform as un
#        lat = str(un(-50,50))
#        lon = str(un(-50,50))


        params = { # optional, additional parameters
            "lang": "de",
            "units" : "ca",
            "exclude" : "minutely,hourly"
        }
    class twitterapi:
        consumer_key = "" # ADD KEY HERE
        consumer_secret = "" # ADD KEY HERE
        access_key = "" # ADD KEY HERE
        access_secret = "" # ADD KEY HERE
        encoding = "utf-8"
