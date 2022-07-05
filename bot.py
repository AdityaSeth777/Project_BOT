#first open cmd and type "pip install tweepy 3.7"
#then if doesn't work, type "pip3 install tweepy 3.7"
import tweepy

auth = tweepy.OAuthHandler("YOU_CONSUMER_KEY", "YOUR_CONSUMER_SECRET")
auth.set_access_token("YOUR_ACCESS_TOKEN", "YOUR_ACCESS_SECRET")
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
#replying against specific keyword i.e. #adibot
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
