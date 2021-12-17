import tweepy
import random
import time
# store credential keys
import credential

# import credential
bearer = credential.BEARER
consumerkey = credential.CONSUMER_KEY
consumersecret = credential.CONSUMER_SECRET
access = credential.ACCESS_TOKEN
accesssecret = credential.ACCESS_SECRET

file_name = 'last_seen_id.txt'

# auth
client = tweepy.Client(bearer_token=bearer,
                        consumer_key=consumerkey, consumer_secret=consumersecret,
                        access_token=access, access_token_secret=accesssecret)

# Query with different keyword
query = '(self harm OR bunuh diri OR insomnia OR insecure OR cemas OR depresi OR stress OR burn out OR toxic OR bipolar OR gaslighting OR trauma OR hopeless OR kesepian OR abusive OR playing victim) -is:retweet lang:id'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# read reply from text
with open('mentalhealth.txt') as txt:
    line = txt.readlines()

def auto_reply():
    last_id = retrieve_last_seen_id(file_name)
    # search tweet with defined query
    tweets = client.search_recent_tweets(query=query, since_id=last_id, max_results=10)

    # iterate each tweet and reply
    for tweet in reversed(tweets.data):
        print(tweet.text)
        print(tweet.id)
        reply = line[random.randint(0, len(line) - 1)]
        create = client.create_tweet(text=reply ,in_reply_to_tweet_id=tweet.id)
        print(create)
        store_last_seen_id(tweet.id, file_name)
        time.sleep(random.randint(10, 20))

    print(len(tweets.data))

while True:
    auto_reply()
    time.sleep(600)