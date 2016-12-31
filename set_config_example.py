import datetime
import shelve


config = shelve.open('config',writeback=True)
print config

config['onTriggerSpeed']=15
config['onLookbackMins']=60
config['pollingIntervalMins']=5
config['scheduledStartHour']=[8,17]
config['scheduledEndHour']=[10,19]
config['windpollminutes']=5
config['bomurl']='http://www.bom.gov.au/fwo/IDN60901/IDN60901.95757.json'
config['gmailid']='bob@gmail.com'  
config['gmailpw']='password123'
config.close()

