# Source: https://learn.adafruit.com/2-2-tft-display/arduino-wiring.md

# Source: https://learn.adafruit.com/adafruit-ultimate-gps/arduino-wiring.md

# Adafruit Ultimate GPS

## Breakout Arduino Wiring

Once you've gotten the GPS module tested with direct wiring, we can go forward and wire it up to a microcontroller. We'll be using an Arduino but you can adapt our code to any other microcontroller that can receive TTL serial at 9600 baud.

## Software Serial Boards
For an Arduino compatible, or any board that does not have an extra `HardwareSerial` port, we'll use `SoftwareSerial`. The examples in the **Adafruit\_GPS Arduino** library use pin 8 for Serial RX and pin 7 for Serial TX _on the Arduino-compatible board_. The constructor call in the example sketches is `SoftwareSerial(8, 7);`.

Connect **VIN** to +5V (or whatever the logic level is of your board), **GND** &nbsp;to Ground,&nbsp; **RX** to digital 7 and&nbsp; **TX** to digital 8. Note that the Arduino-compatible **TX** is connected to the GPS **RX** , and the Arduino-compatible **RX** is connected to the GPS **TX**.

![adafruit_products_gps_ss_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/099/285/medium640/adafruit_products_gps_ss_bb.png?1612729070)

## Hardware Serial Boards
If you're using a board with hardware serial support, like this Feather M0, wire up **VIN** to 3.3V (since that is the logic level of the Feather M0), **GND** to ground, and **GPS RX** to Feather TX and **GPS TX** to Feather RX.

![adafruit_products_gps_hs_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/112/153/medium640/adafruit_products_gps_hs_bb.png?1654002549)

Next up, download the Adafruit GPS library. This library does a lot of the 'heavy lifting' required for receiving data from GPS modules, such as reading the streaming data in a background interrupt and auto-magically parsing it. [You can check the code by visiting the GitHub repository](https://github.com/adafruit/Adafruit-GPS-Library "Link: https://github.com/adafruit/Adafruit-GPS-Library")

To install, open the Arduino library manager

![](https://cdn-learn.adafruit.com/assets/assets/000/099/281/medium800/adafruit_products_image.png?1612726778)

Search for **Adafruit GPS** and click **Install**

![](https://cdn-learn.adafruit.com/assets/assets/000/099/282/medium800/adafruit_products_image.png?1612726876)

Library installation is a frequent stumbling block…if you need assistance, our [All About Arduino Libraries](../../../../adafruit-all-about-arduino-libraries-install-use)&nbsp;guide spells it out in detail!

## Arduino UNO or other SoftwareSerial boards

If your microcontrollers _doesn't_ have a Hardware Serial interface available - say you're using an Arduino UNO or compatible, load up the `SoftwareSerial_echotest` example:

![](https://cdn-learn.adafruit.com/assets/assets/000/099/283/medium800/adafruit_products_image.png?1612726964)

## Leonardo/M0/M4/ESP32 and other Hardware Serial Boards

If you have a board with a spare Hardware Serial interface (which many boards other than the original Arduino UNO compatibles have) - we recommend using that since hardware serial will always give less errors and better performance than software serial!

We assume you'll be using `Serial1` - check your board documentation to figure out which pins that is!

![](https://cdn-learn.adafruit.com/assets/assets/000/099/284/medium800/adafruit_products_image.png?1612727196)

## Upload and Check Output

Whichever version you decide to use, upload the sketch to the microcontroller. Then open up the serial monitor. This sketch simply reads data from the software serial or hardware serial port and outputs that to USB.

Open up the Arduino IDE Serial Console and make sure to set the Serial baud rate to **115200**

![](https://cdn-learn.adafruit.com/assets/assets/000/099/286/medium800/adafruit_products_image.png?1612729336)

You can configure the GPS output you see by commenting/uncommenting lines in the **setup()** procedure. For example, we can ask the GPS to send different sentences, and change how often it sends data. 10 Hz (10 times a second) is the max speed, and is a lot of data. You may not be able to output "all data" at that speed because the 9600 baud rate is not fast enough.

```
// You can adjust which sentences to have the module emit, below
 
  // uncomment this line to turn on RMC (recommended minimum) and GGA (fix data) including altitude
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  // uncomment this line to turn on only the "minimum recommended" data for high update rates!
  //GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCONLY);
  // uncomment this line to turn on all the available data - for 9600 baud you'll want 1 Hz rate
  //GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_ALLDATA);
 
  // Set the update rate
  // 1 Hz update rate
  //GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ);
  // 5 Hz update rate- for 9600 baud you'll have to set the output to RMC or RMCGGA only (see above)
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_5HZ);
  // 10 Hz update rate - for 9600 baud you'll have to set the output to RMC only (see above)
  //GPS.sendCommand(PMTK_SET_NMEA_UPDATE_10HZ);
```

In general, we find that most projects only need the RMC and GGA NMEA's so you don't need ALLDATA unless you have some need to know satellite locations.- [Previous Page](https://learn.adafruit.com/adafruit-ultimate-gps/direct-computer-wiring.md)
- [Next Page](https://learn.adafruit.com/adafruit-ultimate-gps/parsed-data-output.md)

## Featured Products

### Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates

[Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates](https://www.adafruit.com/product/746)
We carry a few different GPS modules here in the Adafruit shop, but none that satisfied our every desire - that's why we designed this little GPS breakout board. We believe this is the **Ultimate** GPS module, so we named it that. It's got everything you want and...

In Stock
[Buy Now](https://www.adafruit.com/product/746)
[Related Guides to the Product](https://learn.adafruit.com/products/746/guides)
### Adafruit Ultimate GPS GNSS with USB - 99 channel w/10 Hz updates

[Adafruit Ultimate GPS GNSS with USB - 99 channel w/10 Hz updates](https://www.adafruit.com/product/4279)
The Ultimate GPS module you know and love has a _glow-up_ to let it be easily used with any computer, not just microcontrollers! With the built-in USB-to-Serial converter, you can now plug-n-play the Ultimate GPS into your computer, laptop, embedded Linux computer, and more. Power and...

In Stock
[Buy Now](https://www.adafruit.com/product/4279)
[Related Guides to the Product](https://learn.adafruit.com/products/4279/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### GPS Antenna - External Active Antenna - 3-5V 28dB 5 Meter SMA

[GPS Antenna - External Active Antenna - 3-5V 28dB 5 Meter SMA](https://www.adafruit.com/product/960)
Give your Ultimate GPS V3 a boost with this external active antenna. This GPS antenna draws about 10mA and will give you an additional 28 dB of gain. It's got a 5 meter long cable so it will easily reach wherever you need it to. The antenna is magnetic so it will stick to the top of a car...

In Stock
[Buy Now](https://www.adafruit.com/product/960)
[Related Guides to the Product](https://learn.adafruit.com/products/960/guides)
### SMA to uFL/u.FL/IPX/IPEX RF Adapter Cable

[SMA to uFL/u.FL/IPX/IPEX RF Adapter Cable](https://www.adafruit.com/product/851)
This RF adapter cable is super handy for anyone doing RF work. Often times, small electronics save space by having a pick-and-placeable u.FL connector (also called uFL, IPEX, IPAX, IPX, MHF, and AM). But most antennas have SMA or RP-SMA connectors on them. This little cable will bridge the...

In Stock
[Buy Now](https://www.adafruit.com/product/851)
[Related Guides to the Product](https://learn.adafruit.com/products/851/guides)
### CR1220 12mm Diameter - 3V Lithium Coin Cell Battery

[CR1220 12mm Diameter - 3V Lithium Coin Cell Battery](https://www.adafruit.com/product/380)
These are the highest quality & capacity batteries, the same as shipped with the iCufflinks,&nbsp;iNecklace, Datalogging and GPS Shields, GPS HAT, etc. One battery per order (you'll want one battery per cufflink or pendant.)  
  
Brand may vary but all battery brands are verified...

In Stock
[Buy Now](https://www.adafruit.com/product/380)
[Related Guides to the Product](https://learn.adafruit.com/products/380/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)

## Related Guides

- [2.8" TFT Touch Shield](https://learn.adafruit.com/2-8-tft-touch-shield.md)
- [Adafruit 4-Channel ADC Breakouts](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts.md)
- [CircuitPython Libraries on Linux and the 96Boards DragonBoard 410c](https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-96boards-dragonboard-410c.md)
- [Arduino Lesson 3. RGB LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds.md)
- [Arduino Lesson 8. Analog Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-8-analog-inputs.md)
- [Let’s Put LEDs in Things!](https://learn.adafruit.com/lets-put-leds-in-things.md)
- [Bluetooth Controlled Motorized Camera Slider](https://learn.adafruit.com/bluetooth-motorized-camera-slider.md)
- [Adafruit VS1053 MP3/AAC/Ogg/MIDI/WAV Codec Breakout Tutorial](https://learn.adafruit.com/adafruit-vs1053-mp3-aac-ogg-midi-wav-play-and-record-codec-tutorial.md)
- [CircuitPython Libraries on Linux and the NVIDIA Jetson Nano](https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-nvidia-jetson-nano.md)
- [Adafruit Optical Fingerprint Sensor](https://learn.adafruit.com/adafruit-optical-fingerprint-sensor.md)
- [FTDI Friend](https://learn.adafruit.com/ftdi-friend.md)
- [IR Sensor](https://learn.adafruit.com/ir-sensor.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [A REST API for Arduino & the CC3000 WiFi Chip](https://learn.adafruit.com/a-rest-api-for-arduino-and-the-cc3000-wifi-chip.md)
- [Adafruit Proto Screw Shield](https://learn.adafruit.com/adafruit-proto-screw-shield.md)
