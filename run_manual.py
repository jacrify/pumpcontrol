import datetime
import shelve
import sys

config = shelve.open('config',writeback=True)
print config

#to be run with two args when pump needs to run for an hour or so.
#first arg is hours, second is minutes. Update config to run manually.
now = datetime.datetime.now()
t=datetime.timedelta(0,0,0,int(sys.argv[1].strip()),int(sys.argv[2].strip()),0)
end=now+t
config['manualEndTime']=end
config.close()

