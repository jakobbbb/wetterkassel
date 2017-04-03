# This is the configuration file for WetterKassel

class config:
    # empty config structure
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
