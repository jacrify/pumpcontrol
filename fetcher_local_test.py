__author__ = 'john'
import datetime
from weather_fetch import fetcher


now=datetime.datetime.now()
max= fetcher.get_max_speed(60,now)
print("Max Speed: %s" % max)
