import arduinoserial


#from datetime import datetime, date, time
from time import sleep
import logging



arduino_location="/dev/ttyACM0"
arduino_pulse_time=300 #milliseconds to pulse 433Mhz signal
arduino_quiet_time=3 # seconds to wait for arduino to be ready after connecting and sending   
arduino_between_retry_time=1 #seconds to wait between consecutive pulses
arduino_retry_times=10 #number of times to retry

def turn_on():
    trigger_pump(1)

def turn_off():
    trigger_pump(0)

def trigger_pump(state):
	arduino = arduinoserial.SerialPort(arduino_location, 9600)
	sleep(arduino_quiet_time) # wait for arduino to reboot :(
	
	times=arduino_retry_times

	while(times > 0) :
		arduino.write("%u,%u\n" % (state,arduino_pulse_time))
		#wait for pulse to finish, then some more
		sleep((arduino_pulse_time/1000)+arduino_quiet_time)
		response= arduino.read_until("\n").strip()
		
		if (response!="ok") :

			logging.info("Pump trigger failed")
			raise Exception("Pump trigger failed")
	
		#libary recognized cr as lf, ardunio ends line with cr/lf, so need to read twice to clear buffer
		response= arduino.read_until("\n").strip()
		sleep(arduino_between_retry_time)	
		times -= 1
	logging.info("Pump triggered OK")



