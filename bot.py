import tweepy
import config
import maya
from maya import MayaInterval


from imagecreator import MakeImage


auth = tweepy.OAuthHandler(config.COMSUMER_KEY, config.COMSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
api = tweepy.API(auth)

def remaining_days():
    today = maya.now()
    enddate = maya.when('2017-09-15')
    interval = MayaInterval(start=today , end=enddate)
    return interval.timedelta.days

day = remaining_days()
image = image = MakeImage(day=day, dimension=[1000, 500], bgcolor='white', banner='images/banner.jpg')
api.update_with_media(image(), status="@%s" % 'pyconnigeria we are getting prepared')
print('done')