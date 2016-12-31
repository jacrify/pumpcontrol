import os.path


# from datetime import datetime, date, time
import logging
import datetime
import shelve
from time import sleep
import sys

import gmail
import fetcher
import pump
import triggers
import web_server
import BaseHTTPServer
import threading

logger = ''



def load_config():
    config = shelve.open('config')
    klist = list(config.keys())
    copy = {};
    for key in klist:
        copy[key] = config[key]
    config.close()
    return copy




def setup_logger():
    global logger
    logger = logging.getLogger('pump_control')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('/var/log/pump.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)


config={}
try:
    setup_logger()
    server_address = ('', 8888)
    serv = BaseHTTPServer.HTTPServer(server_address, web_server.httpServHandler)
    t=threading.Thread(target=serv.serve_forever)
    t.daemon=True
    t.start()


    sleeptime = 1
    running = False

    config = load_config()
    logger.info("Config loaded")


    fetcher = fetcher.Fetcher(config['bomurl'])


    w=triggers.WindTrigger(fetcher)
    s=triggers.ScheduledTrigger()
    m=triggers.ManualTrigger()

    triggers=[m,s,w]

    while (True):

        now = datetime.datetime.now()
        config = load_config()
        logger.info("Config loaded")

        trigger=False
        for t in triggers:
            if t.shouldBeOn(config,now):
                trigger=True
		break

        if running:
            if not trigger:
                #turn off
                logger.info("Turning pump off")
                pump.turn_off()
		gmail.send_mail("Pump off","",config)
                running = False

        else:
            if trigger:

                #turn on
                logger.info("Turning pump on")
                pump.turn_on()
		gmail.send_mail("Pump on","",config)
                running = True


        logger.info("Sleeping for %u seconds" % ( (sleeptime * 60) ))
        sleep((sleeptime * 60) )


except Exception as ex:  #push errors via pushbullet, then sleep for a while in the hope they'll get fixed.

    e = str(ex)
    logger.exception(ex)
    gmail.send_mail("Poolpump: fatal error, check logs",e,config)
    sys.exit(0)



