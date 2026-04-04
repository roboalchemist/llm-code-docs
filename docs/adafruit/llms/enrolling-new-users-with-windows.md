# Source: https://learn.adafruit.com/adafruit-optical-fingerprint-sensor/enrolling-new-users-with-windows.md

# Adafruit Optical Fingerprint Sensor

## Enrolling New Users with Windows

The easiest way to enroll a new fingerprint is to use the Windows software. The interface/test software is unfortunately windows-only and the fingerprint image preview section only seems to work with these sensors:

### Basic Fingerprint Sensor With Socket Header Cable

[Basic Fingerprint Sensor With Socket Header Cable](https://www.adafruit.com/product/4690)
Secure your project with biometrics - this all-in-one optical fingerprint sensor will make adding fingerprint detection and verification super simple. It's easy to use and more affordable than ever!

These modules are typically used in safes - there's a high powered DSP chip that...

In Stock
[Buy Now](https://www.adafruit.com/product/4690)
[Related Guides to the Product](https://learn.adafruit.com/products/4690/guides)
![Fingerprint sensor with detection lens and socket cable](https://cdn-shop.adafruit.com/640x480/4690-02.jpg)

_but_ you only need to use it once to enroll, to get the fingerprint you want stored in the module.  
  
First up, you'll want to connect the sensor to the computer via a USB-serial converter. The easiest way to do this is to connect it directly to the USB/Serial converter in the Arduino. To do this, you'll need to upload a 'blank sketch' this one works well for "traditional" Arduinos, like the Uno and the Mega:

https://github.com/adafruit/Adafruit-Fingerprint-Sensor-Library/blob/master/examples/blank/blank.ino

Danger: 

If you're using a Leonardo, Micro, Yun, Zero, or other native-USB device like ATSAMD21 or ATmega32U4-based controller, use the Leo\_passthru sketch instead of the "blank" sketch.

https://github.com/adafruit/Adafruit-Fingerprint-Sensor-Library/blob/master/examples/Leo_passthru/Leo_passthru.ino

Wire up the sensor as described in the sketch comments **after** uploading the sketch. Since the sensor wires are so thin and short, we stripped the wire a bit and melted some solder on so it made better contact but you may want to solder the wires to header or similar if you're not getting good contact. When you plug in the power, you may see the LED blink to indicate the sensor is working.

[Check the Arduino wiring page for the different wire colors for each kind of sensor](https://learn.adafruit.com/admin/guides/143/editor/767)

You'll connect to the hardware RX / TX pins on the microcontroller:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/500/medium800/biometric_passthru.jpeg?1396783829)

Start up the SFGDemo software and click **Open Device** from the bottom left corner. Select the **COM port** used by the Arduino.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/501/medium800/biometric_opendevice.gif?1448059730)

And press OK when done. You should see the following, with a blue success message and some device statistics in the bottom corner. You can change the baud rate in the bottom left hand corner, as well as the "security level" (how sensitive it is) but we suggest leaving those alone until you have everything running and you want to experiment. They should default to 57600 baud and security level 3 so set them if they're wrong

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/502/medium800/biometric_opened.gif?1448059724)

Lets enroll a new finger! Click the **Preview** checkbox and press the **Enroll** button next to it ( **Con Enroll** means 'Continuous' enroll, which you may want to do if you have many fingers to enroll). When the box comes up, enter in the ID # you want to use. You can use up to 162 ID numbers.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/503/medium800/biometric_enrolladdr.gif?1448059718)

The software will ask you to press the finger to the sensor![](https://cdn-learn.adafruit.com/assets/assets/000/002/504/medium800/biometric_fingerrequest.gif?1448059713)

You can then see a preview (if you cliecked the preview checkbox) of the fingerprint.![](https://cdn-learn.adafruit.com/assets/assets/000/002/505/medium800/biometric_fingerpreview.gif?1448059708)

You will then have to repeat the process, to get a second clean print. Use the same finger!  
  
On success you will get a notice.  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/506/medium800/biometric_enrollsuccess.gif?1448059703)

If there's a problem such as a bad print or image, you'll have to do it again.- [Previous Page](https://learn.adafruit.com/adafruit-optical-fingerprint-sensor/enrolling-vs-searching.md)
- [Next Page](https://learn.adafruit.com/adafruit-optical-fingerprint-sensor/searching-with-the-software.md)

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
