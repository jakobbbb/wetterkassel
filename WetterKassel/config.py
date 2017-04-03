# This is the configuration file for WetterKassel
# Add your keys here and rename this file to 'config.py'

class config:
    # (mostly) empty default config
    config = {
        "weatherapi" : {
            "key" : "",
            "lat" : "51.31",
            "lon" : "9.48",
            "params" : {
                "lang": "de",
                "units" : "ca",
                "exclude" : "minutely,hourly",
                },
            },
        "twitterapi" : {
            "consumer_key" : "",
            "consumer_secret" : "",
            "access_key" : "",
            "access_secret" : "",
            "encoding" : "utf-8",
            },
        }
