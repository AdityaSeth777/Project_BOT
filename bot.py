import tweepy


auth=tweepy.OAuthHandler("BvTJxZOOxPk6OdCR2FIPUYzp2", "OGosnGyCulRfJfPIcdbmSFVNyr0wulzGojk7olkNQTGStXlnHs")
auth.set_access_token("1543506499938398210-c8s6uvVK6Gc6vBktCJPyE4Nq7JQMJK", "SHgsQmkTjEWi3fYLO0zdwNcQdED69tWTQBwp3f5YoQxaw")
api = tweepy.API(auth)

# Tweet something
tweet = api.update_status("Bot of Aditya reporting now... !")
api.create_favorite(tweet.id)

FILE_NAME='last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read=open(FILE_NAME, 'r')
    last_seen_id=int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write=open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return
def reply ():
 tweets=api.mentions_timeline (read_last_seen(FILE_NAME), tweet_mode='extended')
 for tweet in reversed(tweets):
  if '#adibot' in tweet.full_text.lower():
    print (str(tweet.id)+'-'+tweet.full_text)
    api.update_status("@"+tweet.user.screen_name+"Auto reply and retweeting works ? Yes :)", tweet.id)
    #api.create_favourite(tweet.id)
    api.retweet(tweet.id)
    store_last_seen(FILE_NAME, tweet.id)

while True:
  reply ()
  time.sleep(2)
