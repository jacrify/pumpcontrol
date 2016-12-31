__author__ = 'john'
import json
import urllib2
import logging
import datetime


logger = logging.getLogger('pump_control')


class Datapoint:
    def __init__(self, time, speed, gust, direction):
        self.time = time
        self.speed = speed
        self.gust = gust
        self.direction = direction

    def __str__(self):
        timestring = self.time.strftime("%Y-%m-%dT%H:%M:%S")
        return "%s : Speed: %u Gust: %u Dir : %s " % (timestring, self.speed, self.gust, self.direction)

    def __repr__(self):
        return self.__str__()



def filter_by_time(elem, now, minutes_diff):
    delta = now - elem.time


    if delta.total_seconds() > (minutes_diff * 60):
        return False

    return True



class Fetcher:

    def __init__(self,url):
	self.url=url

    def get_json_from_url(self):
	#lucas heights : change this
	response = urllib2.urlopen(self.url,None,10)
	#response = urllib2.urlopen('http://www.bom.gov.au/fwo/IDN60901/IDN60901.95757.json',None,10)

	#sydney airport
	#response = urllib2.urlopen('http://www.bom.gov.au/fwo/IDN60901/IDN60901.94767.json',None,10)


	return json.load(response)


    def fetch_data(self,lookbackMins, now):
	data = self.get_json_from_url()
	outlist = []

	for datapoint in data['observations']['data']:
	    timestring = datapoint['local_date_time_full']
	    tuple_time = datetime.datetime.strptime(timestring, "%Y%m%d%H%M%S")
	    windspeedkm = datapoint['wind_spd_kmh']
	    windgustkm = datapoint['gust_kmh']
	    winddir = datapoint['wind_dir']
	    p = Datapoint(tuple_time, windspeedkm, windgustkm, winddir)
	    outlist.append(p)
        #print p.time




	outlist = sorted(outlist, key=lambda d: d.time)
	#print outlist

	# outlist= [elem for elem in outlist if filter_high_speed(elem)]

	now = datetime.datetime.now()

	outlist = [elem for elem in outlist if filter_by_time(elem, now, lookbackMins)]
	return outlist


    def get_max_speed(self,lookbackMins, now):
        try:
            points = self.fetch_data(lookbackMins, now)
        except:
            logger.exception("couldn't fetch data")
            return 0
        max=0
        for p in points:
                if p.speed > max:
                        max=p.speed
        return max

    def get_average_speed(self,lookbackMins, now):
        try:
            points = self.fetch_data(lookbackMins, now)
        except:
            logger.exception("couldn't fetch data")
            return 0
        if len(points)==0:
                return 0
        total=0
        for p in points:
                total+=p.speed
        return total/len(points)

