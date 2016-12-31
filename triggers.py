__author__ = 'john'
import datetime
import fetcher
import logging

logger = logging.getLogger('pump_control')

class ScheduledTrigger:
    def __init__(self):
        return


    def shouldBeOn(self,config,now):
        hour=now.hour
        for starthour,endhour in zip(config['scheduledStartHour'],config['scheduledEndHour']):
            print starthour,endhour
            if hour>=starthour:
                    if hour < endhour:
                        logger.info("In scheduled hour, pump should be on")
                        return True
        return False

#fetch wind speed every windpollminutes
class WindTrigger:
    def __init__(self,fetcher):
        self.fetcher=fetcher
        self.lastfetch=False
        self.max_speed=0



    def shouldBeOn(self,config,now):

        d = datetime.timedelta(minutes=config['windpollminutes'])


        if self.lastfetch==False or now >= d+self.lastfetch:
            logger.info("Fetching wind speed...")
            self.max_speed=self.fetcher.get_max_speed(config['onLookbackMins'], now)
            logger.info("Max windspeed in last period is %u" % self.max_speed)
            self.lastfetch=now

        if (self.max_speed >= config['onTriggerSpeed']):
	    logger.info("Speed is greater than trigger speed %u, pump should be on" % config['onTriggerSpeed'])
            return True
        
        return False

class ManualTrigger:
    def __init__(self):
        return

    def shouldBeOn(self,config,now):
        if not 'manualEndTime' in config:
            return False
        manualEndTime=config['manualEndTime']

        if now < manualEndTime:
            logger.info("Running in manual mode, pump should be on")
            return True
        return False

