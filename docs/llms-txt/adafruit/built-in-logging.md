# Source: https://learn.adafruit.com/adafruit-ultimate-gps/built-in-logging.md

# Adafruit Ultimate GPS

## Built In Logging

One of the nice things about the MTK3339 is the built in data-logger. This basic data-logging capability can store date, time, latitude, longitude and altitude data into a 64K flash chip inside. Its not a high resolution logger - it only logs once every 15 seconds when there is a fix - but for 99% of projects that want to track location, this can be a great low power way to log data - no SD card or other EEPROM required! It can store up to 16 hours of data.

The GPS module does require a microcontroller to 'kick start' the logger by requesting it to start. If power is lost it will require another 'kick' to start. If you already have some data in the FLASH, a new trace will be created (so you wont lose old data) and if you run out of space it will simply halt and not overwrite old data. Despite this annoyance, its still a very nice extra and we have some library support to help you use it

For more details check out the [LOCUS (built-in-datalogging system) user guide](http://www.adafruit.com/datasheets/GTop%20LOCUS%20Library%20User%20Manual-v13.pdf)

First, we should try getting the logger to run.Open up the **File→Examples→Adafruit\_GPS→locus\_start** sketch. This will demonstrate how to start the logger (called LOCUS)

The key part is here:

```
Serial.print("STARTING LOGGING....");
  if (GPS.LOCUS_StartLogger())
    Serial.println(" STARTED!");
  else
    Serial.println(" no response :(");
  delay(1000);
```

You should start the logger and then check the response:![](https://cdn-learn.adafruit.com/assets/assets/000/001/387/medium800/gps_logstart.gif?1447864284)

# Logging Status  

  
Once you've seen that the GPS is OK with logging, you can load up the status sketch which will also give you more data. Upload&nbsp; **File→Examples→Adafruit\_GPS→locus\_status** ![](https://cdn-learn.adafruit.com/assets/assets/000/001/388/medium800/gps_LOCUS-status.gif?1447864285)

This output gives you some more information. the first entry is the Log #. This is how many log traces are in the memory. Every time you start and save data, a new log is made. Full Stop means that once the logger has run out of memory it will stop. Next the output indicates that we are logging only during fix data and at set intervals, with an interval delay of 15 seconds. We are not logging based on distance or speed. The current status is LOGGING (active), there's also the number of records we've stored. Each record is a timestamped location. We log once every 15 seconds, you can see the records increment from 344 to 345 here. Lastly, we can see how much of the internal flash storage is used, only 4% at this point

In real use, you'll probably want to start the loggging and then have your microcontroller go to sleep to reserve power, waking up once in a while to check up on the logging status.

# Downloading Data  

Finally, once we're done logging we need to extract the data. To do this we need to first get the raw data out of the FLASH and then decode the sentences. Upload **File→Examples→Adafruit\_GPS→locus\_dump&nbsp;** to the Arduino and open up the serial monitor

Danger: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/389/medium800/gps_logdump.gif?1447864285)

Copy and paste all the text after the —-'s (starting with **$PMTKLOX,0,86\*67** and ending with **$PMTK001,622,3\*36** ) [then paste it into the box located on this page](http://learn.adafruit.com/custom/ultimate-gps-parser)

OR

[you can try this python tool that don has kindly donated](https://github.com/don/locus) to the community!

# Using the GPS Tool

If you are having difficulty with the Arduino/javascript tool, you can also try using the GPS tool. The tool runs only under Windows but it is very powerful.  
  
Connect the GPS module to an Arduino [(connected with the Direct Wiring example)](http://learn.adafruit.com/adafruit-ultimate-gps/direct-computer-wiring) , FTDI adapter or other TTL converter and download the [GPS Tool](../../../../adafruit-ultimate-gps/downloads) - connect to the GPS via the COM port of the Arduino/FTDI/TTL cable. You can then query, dump and delete the log memory

- [Previous Page](https://learn.adafruit.com/adafruit-ultimate-gps/circuitpython-datalogging.md)
- [Next Page](https://learn.adafruit.com/adafruit-ultimate-gps/resources.md)

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
