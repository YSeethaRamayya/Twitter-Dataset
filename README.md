# Twitter-Dataset

I have used tweepy API to pull tweets for a particular topic

there are several methods in tweepy API to import data from twitter

User_timeline: this method get data from the user timeline that we want. This works only when user follows particular user otherwise this method returns the tweets that were tweeted by this user.

Search: This method is used to get data from the twitter whether or not user follows the other user. This method also work's fine when we enter the text and it gets the tweets that matches the particular text.

User_timeline method gets tweets upto only 3217 where as search method gets tweets until rate limit exception is generated.

There is a cursor method if we need to iterate through out the whole twitter.

there are some other methods that I didn't used in this API.

