import tweepy
import time
import random
import schedule

consumer_key = ''
consumer_secret = ''
Access_key = ''
Access_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(Access_key, Access_secret)
# Twi Api
api = tweepy.API(auth)


links = [
    'https://www.youtube.com/watch?v=yVmm3FjXbm8&t=243s',
    'https://www.youtube.com/watch?v=fx7pW3kPXMg',
    'https://www.youtube.com/watch?v=PDFlqkm5-LQ&t=22s',
    'https://www.youtube.com/watch?v=hW6t1c46CsY&t=606s',
    'https://www.youtube.com/watch?v=HFHM8eWwjn0',
    'https://www.youtube.com/watch?v=-Fxy5pewRkU',
    'https://www.youtube.com/watch?v=aQXSErOBlqA'
]
hashtags = [
    '#programming',
    "#javascript",
    "#codeNewbies",
    "#frontEnd",
    "#100DaysOfCode",
    "#coding",
    "#reactjs",
    "#CodeNewbies",
    "#css",
    "#linux",
    "#webdev",
    "#python",
    "#nodejs",
    '#Denojs',
    "#techtwitter",
    '#vuejs',
    "#helpmecode",
    "#freecodecamp",
    "#nestjs"
]

search_words = ["#javascript",
                "#webdevelopment", "#angular", "#nestjs"
                "#techtwitter", "#techtwitter", "#100DaysOfCode",
                "#helpmecode", "#freecodecamp", "#CodeNewbies",
                "#linux", "#reactjs", "#nodejs"]
compliment = ["Amazing content", "Nice Video", "Great Learning Resource",
              "Check this Video Out", "Let Learn together", "Great Content",
              "Great Tutorial",
              "Nice Content"]


def retweetRandom():
    api.retweet(api.search(random.choice(search_words))[0].id_str)
    print("Retweeted Succefully")


def tweetRandom():
    tweet = random.choice(compliment) + '\n' + random.choice(links) + \
        '\n' + ' '.join(random.sample(hashtags, 7))
    api.update_status(tweet)

    print("Posted Succesfully")


schedule.every(120).minutes.do(tweetRandom)
schedule.every(15).minutes.do(retweetRandom)

print("Just Got Started")
while True:
    schedule.run_pending()
    time.sleep(1)
