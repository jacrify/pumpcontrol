/* 

Protocol:

PC sends a string containing 2 values, comma separated, terminated by a \n

Value 1: Switch on or off (char)
	If '0', switch off
	If '1', do a little dance.
	or switch on

Value 2: Pulse Length in milliseconds (string)
	Receiving as input as it's easier to change script code than load this onto arduino later

Arduino sends three bytes back on completion:
'ok\n'

*/


int onPin=12;
int offPin=11;

int onSerial=1;
int offSerial=0;


void setup() {
  // initialize serial:
  Serial.begin(9600);
  pinMode(onPin, OUTPUT);
  pinMode(offPin, OUTPUT);
}

void loop() {
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
	int pulseTime=100;
	int onOff=0;
  if (Serial.available()) {
    // get the next two bytes:
    onOff = Serial.parseInt(); 
		pulseTime =  Serial.parseInt();
		
		if (Serial.read() == '\n') {
		}
		int pin=offPin; //default to off in case pc side programmer is an idiot
		if (onOff == 1) {
			pin=onPin;
		}
		
		digitalWrite(pin, HIGH);
		delay(pulseTime );						
		digitalWrite(pin, LOW);

		Serial.println("ok");

		//Serial.println(onOff);

		//Serial.println(pulseTime);
  }
}


