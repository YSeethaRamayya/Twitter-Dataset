import tweepy #https://github.com/tweepy/tweepy
import csv


#Twitter API credentials
consumer_key ="XXXXXXXXXX"
consumer_secret ="XXXXXXXXXX"
access_key ="XXXXXXXXXX"
access_secret ="XXXXXXXXXX"

def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    alltweets = []
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    #key=api.followers_ids(screen_name =screen_name)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1        
    #retw=api.retweets(id)
    #retw.wait_on_rate_limit
    #print(retw.new_tweets)
    while len(new_tweets) > 0:
        #retweets=[]
        print("getting tweets before %s" % (oldest))
        new_tweets = api.user_timeline(screen_name =screen_name,count=200,max_id=891035114838294528,include_rts=True)
        alltweets.extend(new_tweets)
        #oldest = alltweets[-1].id -1
        print( "...%s tweets downloaded so far" % (len(alltweets)))
        outtweets = [[tweet.id_str, tweet.created_at,tweet.retweet_count,tweet.favorite_count,tweet.text.encode("utf-8")] for tweet in alltweets]
        with open('%s_tweets.csv' % screen_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["id","created_at","retweets","favorites","text"])
            writer.writerows(outtweets)
        pass
        
if __name__ == '__main__':
    get_all_tweets("HPV vaccine side effects")
