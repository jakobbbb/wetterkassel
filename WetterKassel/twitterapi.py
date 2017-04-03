import twitter
from WetterKassel import config

class twitterapi:
    def __init__(self):
        self.config = config.config["twitterapi"]
        self.consumer_key = self.config["consumer_key"]
        self.consumer_secret = self.config["consumer_secret"]
        self.access_key = self.config["access_key"]
        self.access_secret = self.config["access_secret"]
        self.encoding = self.config["encoding"]

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
            print >> stderr, "[-] Unicode Decode Error!"
            sys.exit(2)
