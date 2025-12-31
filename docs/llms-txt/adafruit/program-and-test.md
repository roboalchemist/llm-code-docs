# Source: https://learn.adafruit.com/biometric-security-box/program-and-test.md

# Biometric Lock Box

## Program and Test

## Download Fingerprint and Keypad&nbsp;Libraries

- Download the [Adafruit Fingerprint Sensor Library](https://github.com/adafruit/Adafruit-Fingerprint-Sensor-Library) and install it according to the instructions in readme.txt.  
- Download the Keypad Library and install according to the instructions [here](http://playground.arduino.cc/Code/Keypad).

## Enroll Fingers

- Load the "enroll" example into the Arduino IDE.  
- Change the mySerial pin definitions to:&nbsp;"SoftwareSerial mySerial(13, 12);"  
- Follow the [tutorial for enrolling fingerprints](http://learn.adafruit.com/adafruit-optical-fingerprint-sensor/enrolling-with-arduino "Link: http://learn.adafruit.com/adafruit-optical-fingerprint-sensor/enrolling-with-arduino").

## Load code  

- Load the Biometric Box sketch at the bottom of this page.  
- Edit the "secretCode" string to define your passcode.  
- Compile and upload the sketch.  

## Test the Latch Operation

- Power on the box - the led on the power switch should flash a few times, then start to&nbsp;'breathe'.  
- Enter your passcode - the fingerprint sensor should turn on and glow red.  
- Place your finger on the sensor and you should hear the solenoid click.

```
/*************************************************** 
  Biometric Box Sketch for the optical Fingerprint sensor
  This sketch implements a two-level security scheme requiring the
  user to enter a passcode via the keypad before scanning a fingerprint
  for access.

  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!

  Written by Bill Earl for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/
#include &lt;Keypad.h&gt;
#include &lt;Adafruit_Fingerprint.h&gt;
#include &lt;SoftwareSerial.h&gt;

// Define the states for the lock state machine
#define LOCKED 2
#define PASSWORD_OK 1
#define UNLOCKED 0

// State Variables:   Initialize to the locked state
int LockState = LOCKED;
long StartTime = 0;
int position = 0;

// Define your password key sequence here
char* secretCode = "1423";

// Keypad key matrix:
const byte rows = 4; 
const byte cols = 3; 
char keys[rows][cols] = 
{
   {'1','2','3'},
   {'4','5','6'},
   {'7','8','9'},
   {'*','0','#'}
};

// Keypad pin definitions
byte rowPins[rows] = {2, 3, 4, 5}; 
byte colPins[cols] = {6, 7, 8};  

// Instantiate the keypad
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, rows, cols);

// More pin definitions:
int LedPin = 10;
int SolenoidPin = 11;

// Define a Fingerprint sensor on pins 12 &amp; 13
int getFingerprintIDez();
SoftwareSerial mySerial(13, 12);
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&amp;mySerial);


void setup()                    
{
   pinMode(LedPin, OUTPUT);
   pinMode(SolenoidPin, OUTPUT);
   
   // Flash hello
   for (int i = 0; i &lt; 3; i++)
   {
     digitalWrite(LedPin, HIGH);
     delay(100);
     digitalWrite(LedPin, LOW);
     delay(100);
   }
   
   // Initialize state and communicatins
   setLockState(LOCKED); 
   Serial.begin(9600); 
   finger.begin(57600);

   // Connect to the sensor
   if (finger.verifyPassword()) 
   {
      Serial.println("Found fingerprint sensor!");
   } 
   else 
   {
      Serial.println("Did not find fingerprint sensor :(");
      while (1);
   }
}


void loop()                    
{
   // Run the state machine:
   
   // Locked State - Monitor keypad for valid Password code entry
   if (LockState == LOCKED)
   {
      char key = keypad.getKey();

      if (key == '*' || key == '#')
      {
         position = 0;
         setLockState(LOCKED);
      }
      if (key != 0)
      {
         if (key == secretCode[position])  // Valid key in Password sequence
         {
            Serial.print("Matched ");   
            Serial.print(key);   
            Serial.print("-at-");   
            Serial.println(position);   
            position ++;
         }
         else  // Invalid key - start all over again
         {
            Serial.println("Invalid Code!");   
            position = 0;
         }
      }

      // Let the LED 'breathe' while we wait
      analogWrite(LedPin, sin((millis() % 3142) / 1000.0) * 255);

      if (position == 4)  // Password successfully entered - advance state
      {
         setLockState(PASSWORD_OK);
         position = 0;
      }
      delay(100);
   }

   // PASSWORD_OK state - Now wait for a valid fingerprint reading
   else if (LockState == PASSWORD_OK)
   { 
      if (getFingerprintIDez() != -1)
      {
         setLockState(UNLOCKED); // Valid fingerprint - advance state to UNLOCKED
      }
      if (millis () - StartTime &gt; 5000) 
      {
         setLockState (LOCKED); // Time-out - go back to the LOCKED state
      }
   }

   // UNLOCKED state - hold the solenoid open for a limited time
   else if (LockState == UNLOCKED)
   { 
      for (int i = 0; i &lt; 30; i++)
      {
         // Flash the led to indicate the lock is open
         digitalWrite(LedPin, LOW);
         delay(50);
         digitalWrite(LedPin, HIGH);
         delay(50);
      }
      setLockState (LOCKED);  // Time-out - go back to the locked state.
   }
}



// returns -1 if failed, otherwise returns ID #
int getFingerprintIDez() 
{
   uint8_t p = finger.getImage();
   if (p != FINGERPRINT_OK)  return -1;

   p = finger.image2Tz();
   if (p != FINGERPRINT_OK)  return -1;

   p = finger.fingerFastSearch();
   if (p != FINGERPRINT_OK)  return -1;

   // found a match!
   Serial.print("Found ID #"); Serial.print(finger.fingerID); 
   Serial.print(" with confidence of "); Serial.println(finger.confidence);
   return finger.fingerID; 
}


// Set the state and the time of the state change
void setLockState(int state)
{
   LockState = state;
   StartTime = millis ();
   if (state == LOCKED)
   {
      Serial.println("Locked!");
      digitalWrite(LedPin, HIGH);
      digitalWrite(SolenoidPin, LOW);  
   }

   else if (state == PASSWORD_OK)
   {
      Serial.println("PASSWORD_OK!");
      digitalWrite(LedPin, LOW);  
   }    
   else if (state == UNLOCKED)
   {
      Serial.println("Unlocked!");
      digitalWrite(LedPin, LOW);
      digitalWrite(SolenoidPin, HIGH);      
   }
}
```

- [Previous Page](https://learn.adafruit.com/biometric-security-box/assembly.md)
- [Next Page](https://learn.adafruit.com/biometric-security-box/final-assembly.md)

## Featured Products

### Panel Mount 2.1mm DC barrel jack

[Panel Mount 2.1mm DC barrel jack](https://www.adafruit.com/product/610)
This power jack is designed to easily attach to a panel up to 8mm thick (0.315" or 5/16") and fit 2.1mm power plugs snugly and securely. Perfect for adding a power connector to your project enclosure. We like this jack in particular for its long body (so you can use it on thicker...

In Stock
[Buy Now](https://www.adafruit.com/product/610)
[Related Guides to the Product](https://learn.adafruit.com/products/610/guides)
### Rugged Metal On/Off Switch with Green LED Ring

[Rugged Metal On/Off Switch with Green LED Ring](https://www.adafruit.com/product/482)
These chrome-plated metal buttons are rugged and look real good while doing it! Simply drill a 16mm hole into any material up to 1/2" thick and you can fit these in place, there's even a rubber gasket to keep water out of the enclosure. On the front of the button is a flat metal...

In Stock
[Buy Now](https://www.adafruit.com/product/482)
[Related Guides to the Product](https://learn.adafruit.com/products/482/guides)
### Adafruit MENTA - Mint Tin Arduino Compatible Kit with Mint Tin

[Adafruit MENTA - Mint Tin Arduino Compatible Kit with Mint Tin](https://www.adafruit.com/product/795)
Introducing the MENTA, a portable minty Arduino-compatible project that fits into a common mint tin. We took our super popular Boarduino series, and wrapped it with a prototyping area into a rounded PCB that slots directly into an Altoids-sized metal tin. We included everything you expect to...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/795)
[Related Guides to the Product](https://learn.adafruit.com/products/795/guides)
### N-channel power MOSFET

[N-channel power MOSFET](https://www.adafruit.com/product/355)
When you need to switch a lot of power, N-channel MOSFETs are best for the job. These FETs can switch over 60A and 30V and are TO-220 packages so they fit nicely into any breadboard or perfboard. Heat sinking is easy with TO-220's, but because of the very low Rds(on) of down to 0.009 ohms...

In Stock
[Buy Now](https://www.adafruit.com/product/355)
[Related Guides to the Product](https://learn.adafruit.com/products/355/guides)
### Small  Push-Pull Solenoid - 12VDC

[Small  Push-Pull Solenoid - 12VDC](https://www.adafruit.com/product/412)
Solenoids are basically electromagnets: they are made of a big coil of copper wire with an armature (a slug of metal) in the middle. When the coil is energized, the slug is pulled into the center of the coil. This makes the solenoid able to pull (from one end) or push (from the other)  
<br...></br...>

In Stock
[Buy Now](https://www.adafruit.com/product/412)
[Related Guides to the Product](https://learn.adafruit.com/products/412/guides)
### Membrane 3x4 Matrix Keypad + extras

[Membrane 3x4 Matrix Keypad + extras](https://www.adafruit.com/product/419)
Punch in your secret key into this numeric matrix keypad. This keypad has 12 buttons, arranged in a telephone-line 3x4 grid. It's made of a thin, flexible membrane material with an adhesive backing (just remove the paper) so you can attach it to nearly anything. The keys are connected into...

In Stock
[Buy Now](https://www.adafruit.com/product/419)
[Related Guides to the Product](https://learn.adafruit.com/products/419/guides)
### Fingerprint sensor

[Fingerprint sensor](https://www.adafruit.com/product/751)
Secure your project with biometrics - this all-in-one optical fingerprint sensor will make adding fingerprint detection and verification super simple. These modules are typically used in safes - there's a high powered DSP chip that does the image rendering, calculation, feature-finding and...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/751)
[Related Guides to the Product](https://learn.adafruit.com/products/751/guides)

## Related Guides

- [Reebok CheckLight Teardown](https://learn.adafruit.com/reebok-checklight-teardown.md)
- [Muse Headset Teardown](https://learn.adafruit.com/muse-headset-teardown.md)
- [Whistle Dog Activity Monitor Teardown](https://learn.adafruit.com/whistle-dog-activity-monitor-teardown.md)
- [Control Electronics with your Brain using NextMind](https://learn.adafruit.com/control-electronics-with-your-brain-using-nextmind.md)
- [Your Pulse Displayed with NeoPixels](https://learn.adafruit.com/pulse-sensor-displayed-with-neopixels.md)
- [Circuit Playground Bluefruit BLE Heart Rate Pendant with CircuitPython](https://learn.adafruit.com/ble-heart-rate-display-pendant.md)
- [Meditation Trainer](https://learn.adafruit.com/heart-rate-variability-sensor.md)
- [Myo Armband Teardown](https://learn.adafruit.com/myo-armband-teardown.md)
- [LED Breath Stats Mask](https://learn.adafruit.com/led-breath-stats-mask.md)
- [Adafruit MPRLS Ported Pressure Sensor Breakout](https://learn.adafruit.com/adafruit-mprls-ported-pressure-sensor-breakout.md)
- [Pulse Room](https://learn.adafruit.com/pulse-room.md)
- [Getting Started with MyoWare Muscle Sensor](https://learn.adafruit.com/getting-started-with-myoware-muscle-sensor.md)
- [Setting up an Open Speech Recording Website](https://learn.adafruit.com/setting-up-an-open-speech-recording-website.md)
- [Adafruit Optical Fingerprint Sensor](https://learn.adafruit.com/adafruit-optical-fingerprint-sensor.md)
- [Pulse Oximeter Wireless Data Logger](https://learn.adafruit.com/pulse-oximeter-wireless-data-logger.md)
