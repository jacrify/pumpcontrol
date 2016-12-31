__author__ = 'john'

import unittest
import datetime
import triggers

class MockFetcher:
    def __init__(self,maxspeed):
        self.maxspeed=maxspeed
        return

    def get_max_speed(self,lookbackMins, now):
        return self.maxspeed




class TestTriggers(unittest.TestCase):
    def test_scheduled_single(self):
        config={}
        config['scheduledStartHour']=[8]
        config['scheduledEndHour']=[10]

        s=triggers.ScheduledTrigger()

        now=datetime.datetime(2015,12,25,7,59,0)
        self.assertEqual(False,s.shouldBeOn(config,now))

        now=datetime.datetime(2015,12,25,8,00,0)
        self.assertEqual(True,s.shouldBeOn(config,now))

        now=datetime.datetime(2015,12,25,9,59,0)
        self.assertEqual(True,s.shouldBeOn(config,now))


        now=datetime.datetime(2015,12,25,10,0,0)
        self.assertEqual(False,s.shouldBeOn(config,now))


    def test_scheduled_multiple(self):
        config={}
        config['scheduledStartHour']=[8,10]
        config['scheduledEndHour']=[9,11]

        s=triggers.ScheduledTrigger()

        now=datetime.datetime(2015,12,25,7,59,0)
        self.assertEqual(False,s.shouldBeOn(config,now))

        now=datetime.datetime(2015,12,25,8,00,0)
        self.assertEqual(True,s.shouldBeOn(config,now))

        now=datetime.datetime(2015,12,25,8,59,0)
        self.assertEqual(True,s.shouldBeOn(config,now))


        now=datetime.datetime(2015,12,25,9,59,0)
        self.assertEqual(False,s.shouldBeOn(config,now))

        now=datetime.datetime(2015,12,25,10,0,0)
        self.assertEqual(True,s.shouldBeOn(config,now))

        now=datetime.datetime(2015,12,25,11,0,0)
        self.assertEqual(False,s.shouldBeOn(config,now))



    def test_manual(self):
        config={}

        config['manualEndTime']=datetime.datetime(2015,12,25,10,00,0)

        s=triggers.ManualTrigger()

        now=datetime.datetime(2014,12,25,7,59,0)
        self.assertEqual(True,s.shouldBeOn(config,now))

        now=datetime.datetime(2015,12,25,7,59,0)
        self.assertEqual(True,s.shouldBeOn(config,now))

        now=datetime.datetime(2015,12,25,8,00,0)
        self.assertEqual(True,s.shouldBeOn(config,now))

        now=datetime.datetime(2015,12,25,9,59,0)
        self.assertEqual(True,s.shouldBeOn(config,now))

        now=datetime.datetime(2015,12,25,10,0,0)
        self.assertEqual(False,s.shouldBeOn(config,now))

        now=datetime.datetime(2015,12,25,11,0,0)
        self.assertEqual(False,s.shouldBeOn(config,now))

        now=datetime.datetime(2016,12,25,11,0,0)
        self.assertEqual(False,s.shouldBeOn(config,now))

        config={}
        self.assertEqual(False,s.shouldBeOn(config,now))

    def test_wind_trigger(self):
        config={}

        config['windpollminutes']=15
        config['onLookbackMins']=60
        config['onTriggerSpeed']=10

        #will cause trigger
        f=MockFetcher(11)

        s=triggers.WindTrigger(f)


        now=datetime.datetime(2014,12,25,8,0,0)
        self.assertEqual(True,s.shouldBeOn(config,now))
        f.maxspeed=0
        #shouldn't trigger, as 15 minutes have not passed so new speed won't be checked.
        now=datetime.datetime(2014,12,25,8,14,0)
        self.assertEqual(True,s.shouldBeOn(config,now))


        now=datetime.datetime(2014,12,25,8,15,0)
        self.assertEqual(False,s.shouldBeOn(config,now))




if __name__ == '__main__':
    unittest.main()
