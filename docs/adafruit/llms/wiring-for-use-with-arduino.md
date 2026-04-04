# Source: https://learn.adafruit.com/adafruit-optical-fingerprint-sensor/wiring-for-use-with-arduino.md

# Adafruit Optical Fingerprint Sensor

## Wiring for use with Arduino

Once you've tested the sensor, you can now use it within a sketch to verify a fingerprint. We'll need to rewire the sensor. Disconnect the green and white wires and plug the green wire into digital **2** and the white wire to digital **3**. (For ESP8266 use **4** & **5** , for devices with Hardware UART use **0** & **1** )

Danger: 

If your [fingerprint sensor has individual socket wires (its this one)](https://www.adafruit.com/product/4690) then use the following wire setup:

- Red Wire to 3.3V
- Yellow wire is Serial TX
- White wire is Serial RX
- Black wire is ground

![biometric_4690-02.jpg](https://cdn-learn.adafruit.com/assets/assets/000/099/199/medium640/biometric_4690-02.jpg?1612321199)

![biometric_4690-00.jpg](https://cdn-learn.adafruit.com/assets/assets/000/099/201/medium640/biometric_4690-00.jpg?1612321417)

If your cable has a single slim connector on the end and has different color wires:

- The first wire from the left should be the black wire ground
- then the two data pins: Serial RX is the white wire
- Serial TX is the green wire
- Then the red power wire (3 or 5V)

You'll have to cut, strip and solder the wires.

![biometric_wiring.jpg](https://cdn-learn.adafruit.com/assets/assets/000/049/718/medium640/biometric_wiring.jpg?1514501575)

![biometric_751-04.jpg](https://cdn-learn.adafruit.com/assets/assets/000/099/200/medium640/biometric_751-04.jpg?1612321302)

If your sensor is an older one and has all the same-color wires, The first wire from the left is ground, then the two data pins, then power. You'll have to cut, strip and solder the wires.

&nbsp;

RX is the same as the White wire  
TX is&nbsp;the same as the Green wire

![biometric_file.png](https://cdn-learn.adafruit.com/assets/assets/000/048/438/medium640/biometric_file.png?1511588931)

On the "rugged" fingerprint sensor:

- Red wire is connected to 3.3V for power
- Black wire is connected to ground
- Yellow to Microcontroller RX (data _in_ to microcontroller)
- Green to Microcontroller TX (data _out_ from microcontroller)

![biometric_4651-00.jpg](https://cdn-learn.adafruit.com/assets/assets/000/109/720/medium640/biometric_4651-00.jpg?1647394791)

On the 'slim' fingerprint sensor

- Black to GND
- Yellow to Microcontroller TX (data _out_ from microcontroller)
- Green to Microcontroller RX (data _in_ from microcontroller)
- Red to 3.3V VIN

![biometric_4750-01.jpg](https://cdn-learn.adafruit.com/assets/assets/000/109/721/medium640/biometric_4750-01.jpg?1647395108)

# Arduino UNO & Compatible Wiring

This example sketch uses pins **2** and **3** for software serial (on ATmega328P type boards by default) - Not all boards support Software Serial on all pins so check board documentation! For example on ESP8266 we used **4** & **5**

You can power the sensor from **3.3V** or **5V** - some sensors require 3.3V, see above!

Warning: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/509/medium800/biometric_ardwiring.jpeg?1396783921)

# Hardware Serial Wiring

If you have a device with hardware serial, you should use that instead. Often this is pins #0 and #1

![](https://cdn-learn.adafruit.com/assets/assets/000/048/436/medium800/biometric_hwseri.png?1511584080)

Next, you'll need to install [the Adafruit Fingerprint sensor library (also available from github)](https://github.com/adafruit/Adafruit-Fingerprint-Sensor-Library).

Open up the Arduino Library Manager:

![](https://cdn-learn.adafruit.com/assets/assets/000/048/434/medium800/biometric_managelib.png?1511582708)

Type in **Fingerprint** until you see the **Adafruit Fingerprint library** show up!

![](https://cdn-learn.adafruit.com/assets/assets/000/048/435/medium800/biometric_fingerlib.png?1511582738)

Click Install! That's it. Now you should be able to select the **File→Examples→Adafruit\_Fingerprint→fingerprint** example sketch.

# Soft & Hard Serial

By default the sketch uses software serial (Arduino UNO & compatibles). If you are using a device with Hardware Serial, e.g does not have a USB-Serial converter chip, use that instead! Usually those are on pins 0 & 1

```
// On Leonardo/Micro or others with hardware serial, use those! #0 is green wire, #1 is white
// uncomment this line:
#define mySerial Serial1

// For UNO and others without hardware serial, we must use software serial...
// pin #2 is IN from sensor (GREEN wire)
// pin #3 is OUT from arduino  (WHITE wire)
// comment these two lines if using hardware serial
//#include &lt;SoftwareSerial.h&gt;
//SoftwareSerial mySerial(2, 3);
```

If necessary, uncomment/comment lines for hardware serial support

# Upload

Upload it to your Arduino as usual. Open up the serial monitor at 9600 baud and when prompted place your finger against the sensor that was already enrolled.  
  
You should see the following:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/510/medium800/biometric_arduinosearch.gif?1448059690)

Info: 

The 'confidence' is a score number (from 0 to 255) that indicates how good of a match the print is, higher is better. Note that if it matches at all, that means the sensor is pretty confident so you don't have to pay attention to the confidence number unless it makes sense for high security applications.

Of course you have to have **enrolled** a fingerprint first! If you did this using the Windows program, that's good to go. If you have not yet, you should at least have gotten a `Found fingerprint sensor!` printout. You can go ahead to the next step to enroll fingerprints.

If you get `Did not find fingerprint sensor :(` check your wiring, maybe swap the RX and TX wire as that's a common issue  
  
If you want to have a more detailed report, change the **loop()**&nbsp;to run **getFingerprintID()** instead of **getFingerprintIDez()** - that will give you a detailed report of exactly what the sensor is detecting at each point of the search process.

- [Previous Page](https://learn.adafruit.com/adafruit-optical-fingerprint-sensor/searching-with-the-software.md)
- [Next Page](https://learn.adafruit.com/adafruit-optical-fingerprint-sensor/enrolling-with-arduino.md)

## Featured Products

### Fingerprint sensor

[Fingerprint sensor](https://www.adafruit.com/product/751)
Secure your project with biometrics - this all-in-one optical fingerprint sensor will make adding fingerprint detection and verification super simple. These modules are typically used in safes - there's a high powered DSP chip that does the image rendering, calculation, feature-finding and...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/751)
[Related Guides to the Product](https://learn.adafruit.com/products/751/guides)
### Rugged Panel Mount Fingerprint Sensor with Bi-Color LED Ring

[Rugged Panel Mount Fingerprint Sensor with Bi-Color LED Ring](https://www.adafruit.com/product/4651)
Secure your project with biometrics - this all-in-one optical fingerprint sensor will make adding fingerprint detection and verification super simple. It even has an LED ring built around the detection pad, which can be set to red, blue or purple (as well as some fading/blinking effects) for a...

In Stock
[Buy Now](https://www.adafruit.com/product/4651)
[Related Guides to the Product](https://learn.adafruit.com/products/4651/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)

## Related Guides

- [A REST API for Arduino & the CC3000 WiFi Chip](https://learn.adafruit.com/a-rest-api-for-arduino-and-the-cc3000-wifi-chip.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [Adafruit 4-Channel ADC Breakouts](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts.md)
- [Collin's Lab: MIDI](https://learn.adafruit.com/collins-lab-midi.md)
- [Adafruit PN532 RFID/NFC Breakout and Shield](https://learn.adafruit.com/adafruit-pn532-rfid-nfc.md)
- [Adafruit AirLift Shield - ESP32 WiFi Co-Processor](https://learn.adafruit.com/adafruit-airlift-shield-esp32-wifi-co-processor.md)
- [8BitBox](https://learn.adafruit.com/8bitbox.md)
- [Geofencing with the FONA 808 & Adafruit IO](https://learn.adafruit.com/geofencing-with-the-fona-808-and-adafruit-io.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [Photocells](https://learn.adafruit.com/photocells.md)
- [Automatic Monitor Color Temperature Adjustment](https://learn.adafruit.com/automatic-monitor-color-temperature-adjustment.md)
- [Arduino Lesson 15. DC Motor Reversing](https://learn.adafruit.com/adafruit-arduino-lesson-15-dc-motor-reversing.md)
- [Adafruit 1.14" 240x135 Color TFT Breakout LCD Display](https://learn.adafruit.com/adafruit-1-14-240x135-color-tft-breakout.md)
- [How to Find Hidden COM Ports](https://learn.adafruit.com/how-to-find-hidden-com-ports.md)
- [Low Power Coin Cell Voltage Logger](https://learn.adafruit.com/low-power-coin-cell-voltage-logger.md)
