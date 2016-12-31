This is a bunch of bad python that controls my pool pump via an arduino hacked onto a consumer remote controlled mains plug.

It has three main functions:

-  It polls the local weather station to get the current wind speed, and turns on when the wind is high (so that leaves landing in the pool get skimmed out)
-  It runs a few hours a day on a schedule
-  It turns on when request via a web interface- I have this hooked up to android and tasker so I get voice control
-  It sends emails (via gmail) whenever it turns on or off so I can keep track of it


To get it to go you need to :

1. Build the arduino interface
2. Copy to a linux box with python (I run it on a [Kodi](https://kodi.tv/) box, which a a fairly restrictive execution environment)
3. Find a weather feed close to you. I'm using the Aussie BOM feeds (json) from [here](http://www.bom.gov.au/catalogue/data-feeds.shtml#obs-ind) , but if you're not in aus you'll need to write some parsing code.
4. Set up a one time gmail password for notificationsm, or disable notifcations in the code
5. Edit set_config.py to reflect the above and other settings.
6. Run set_config.py (once off)
7. Run run.sh to start the daemon (put in your startup)


![Overview]({{ site.baseurl }}/assets/umllet overview.jpg)


To get the PC to control my pool pump, I had a couple of problems:

My pool pump is 20m from my house.

I didn't want to mess with mains power (I don't enjoy electrocution)


I looked at off the shelf arduino solutions for controlling mains power, but ended up buying a set of [Watts Clever Easy Off Sockets and Remote](http://www.aussietradesupplies.com.au/catalogue/energy_saving/watts_clever_easy_off_remote_control_socket_4_pack_remote_was_7495_now_5500).


![Watts Clever]({{ site.baseurl }}/assets/wattsClever.png)


I disassembled the remote, and using a breadboard, wired the arduino outputs to "push" the buttons on the remote. I also powered the remote off the arduino power. I only wired up one set of on/off switches but you could use this same technique to control 3 different power sockets.

The breadboard circuit to hook the arduino to the remote is pretty simple- some transistors and a couple of resistors to act as [voltage dividers](https://en.wikipedia.org/wiki/Voltage_divider) to drop the voltage to the right level.The whole design, including parts manifest, is available as a [Fritzing](http://fritzing.org/home/) file for download [here]({{ site.baseurl }}/assets/pumpControl.fzz)
. Overall it looks something like this:


![Breadboard]({{ site.baseurl }}/assets/breadboardDesign.jpg)


![Schematic]({{ site.baseurl }}/assets/schematic.jpg)


The "finished product", which plugs into my PC,  looks like this:

![arduino1]({{ site.baseurl }}/assets/arduinoPhoto1.jpg)

![arduino2]({{ site.baseurl }}/assets/arduinoPhoto2.jpg)

![arduino3]({{ site.baseurl }}/assets/arduinoPhoto3.jpg)




This system works best if you have a very good skimmer in your pool. I use the [poolskim](http://www.poolskim.com/) which is amazing.

![Poolskim]({{ site.baseurl }}/assets/poolskim_good_2.jpg)



The code that runs on the arduino is available in the PoolPumpSerial folder with the github code.

If you want voice control from Android, you need [Tasker](https://tasker.dinglisch.net/) and [Autovoice](https://joaoapps.com/autovoice/). Then import the tasker project in the anroid folder, and modify the IP address of the web server.


Warning: this code is not at all secure, especially the web interface.



