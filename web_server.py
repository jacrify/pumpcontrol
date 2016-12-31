import BaseHTTPServer, cgi
import os
import sys

import datetime
import shelve
import sys
import threading
import logging

logger = logging.getLogger('pump_control')

def run_manual(hours,minutes):
    config = shelve.open('config',writeback=True)

    #to be run with two args when pump needs to run for an hour or so.
    #first arg is hours, second is minutes. Update config to run manually.
    now = datetime.datetime.now()
    t=datetime.timedelta(hours=hours,minutes=minutes)
    end=now+t
    config['manualEndTime']=end
    config.close()
    logger.info("Manual run written to config")



class httpServHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path.find('?') != -1:
         self.path, self.query_string = self.path.split('?', 1)
        else:
            self.query_string = ''



        #expect the following:
        #manual?hours=h
        #manual?minutes=m

        if self.path.find('manual') != -1:
            if self.query_string.find('hours') != -1:
                hours=self.query_string.split("=")[1]
                hours=int(hours)
                run_manual(hours,0)
            else:
                if self.query_string.find('minutes') != -1:
                    minutes=self.query_string.split("=")[1]
                    minutes=int(minutes)
                    run_manual(0,minutes)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.globals = dict(cgi.parse_qsl(self.query_string))




