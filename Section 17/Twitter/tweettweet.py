import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(300)

#Follow back bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    followe.follow()     



search_string = 'Python'
numberoftweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberoftweets):
    try:
        tweet.favorite()
        print(f'I liked a tweet that says {tweet}')
    except tweepy.TweepError as e:
        print(e.reason)    
    except StopIteration:
        break    
                  