This is a bunch of bad python that controls my pool pump via an arduino hacked onto a consumer remote controlled mains plug.

It has three main functions:
1) It polls the local weather station to get the current wind speed, and turns on when the wind is high (so that leaves landing in the pool get skimmed out)
2) It runs a few hours a day on a schedule
3) It turns on when request via a web interface- I have this hooked up to android and tasker so I get voice control


To get it to go you need to :
a) Build the arduino interface
b) Copy to a linux box with python (I run it on a Kodi box)
c) Find a weather feed close to you. I'm using the Aussie BOM feeds (json) from here: http://www.bom.gov.au/catalogue/data-feeds.shtml#obs-ind , but if you're not in aus you'll need to write some parsing code.
d) Set up a one time gmail password for notificationsm, or disable notifcations in the code
e) Edit set_config.py to reflect the above and other settings.
f) Run set_config.py (once off)
g) Run run.sh to start the daemon (put in your startup)

