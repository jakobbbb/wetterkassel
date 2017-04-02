import twitter
from WetterKassel import config

class twitterapi:
    def __init__(self):
        self.consumer_key = config.twitterapi.consumer_key
        self.consumer_secret = config.twitterapi.consumer_secret
        self.access_key = config.twitterapi.access_key
        self.access_secret = config.twitterapi.access_secret
        self.encoding = config.twitterapi.encoding

        self.api = twitter.Api(
            consumer_key=self.consumer_key, 
            consumer_secret=self.consumer_secret,
            access_token_key=self.access_key,
            access_token_secret=self.access_secret,
            input_encoding=self.encoding
            )

    def post(self, message):
        try:
            status = self.api.PostUpdate(message)
        except UnicodeDecodeError:
            print "[-] Unicode Decode Error!"
            sys.exit(2)
