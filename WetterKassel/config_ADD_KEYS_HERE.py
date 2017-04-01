# This is the configuration file for WetterKassel
# Add your keys here and rename this file to 'config.py'

class config:
    class weatherapi:
        key = "Geheim" # ADD KEY HERE
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
        consumer_key = "Geheim" # ADD KEY HERE
        consumer_secret = "Geheim" # ADD KEY HERE
        access_key = "Geheim" # ADD KEY HERE
        access_secret = "Geheim" # ADD KEY HERE
        encoding = "utf-8"
