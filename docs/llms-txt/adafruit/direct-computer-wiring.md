# Source: https://learn.adafruit.com/adafruit-ultimate-gps/direct-computer-wiring.md

# Adafruit Ultimate GPS

## Direct Computer Wiring

GPS modules are great in that the moment you turn them on, they'll start spitting out data, and trying to get a 'fix' (location verification). Like pretty much every GPS in existence, the Adafruit Ultimate GPS uses TTL serial output to send data so the best way to first test the GPS is to wire it directly to the computer via the TTL serial to USB converter on an Arduino. You can also use an FTDI Friend or other TTL adapter but for this demonstration we'll use a classic Arduino.

Danger: This tutorial step won't work with a chip that has NATIVE USB - it's for an Arduino UNO compatible only. Go on to the next step, [Breakout Arduino Wiring](https://learn.adafruit.com/adafruit-ultimate-gps/arduino-wiring), but refer back here for this discussion of the GPS data!

First, load a "blank" sketch into the Arduino:

```
// this sketch will allow you to bypass the Atmega chip
// and connect the Ultimate GPS directly to the USB/Serial
// chip converter.
 
// Connect VIN to +5V
// Connect GND to Ground
// Connect GPS RX (data into GPS) to Digital 0
// Connect GPS TX (data out from GPS) to Digital 1
 
void setup() {}
void loop() {}
```

This is will free up the converter so you can directly wire and bypass the Arduino chip. Once you've uploaded this sketch, wire the GPS as follows. Your module may look slightly different, but as long as you are connecting to the right pin names, they all work identically for this part.

Note that TX on the Arduino is connected to TX on the Ultimate GPS, and similarly for RX. **This is not the usual wiring,** which would have TX\<-\>RX and RX\<-\>TX. It is wired this way because you are using the separate USB-serial converter on the Arduino board directly, by using the "blank" sketch above.

Danger: Use the wiring below **only** for the "blank" sketch above, with an Arduino Uno compatible only. For regular use, use the wiring shown on the [Breakout Arduino Wiring](https://learn.adafruit.com/adafruit-ultimate-gps/arduino-wiring) page.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/380/medium800/gps_directwire.jpeg?1396771648)

Now plug in the USB cable, and open up the serial monitor from the Arduino IDE and be sure to select&nbsp; **9600 baud** &nbsp;in the drop down. You should see text like the following:![](https://cdn-learn.adafruit.com/assets/assets/000/018/682/medium800/gps_nmea_data.png?1407363321)

This is the raw GPS "NMEA sentence" output from the module. There are a few different kinds of NMEA sentences, the most common ones people use are the&nbsp; **$GPRMC** &nbsp;( **G** lobal&nbsp; **P** ositioning&nbsp; **R** ecommended **M** inimum&nbsp; **C** oordinates or something like that) and the&nbsp; **$GPGGA** &nbsp;sentences. These two provide the time, date, latitude, longitude, altitude, estimated land speed, and fix type. Fix type indicates whether the GPS has locked onto the satellite data and received enough data to determine the location (2D fix) or location+altitude (3D fix).

[For more details about NMEA sentences and what data they contain, check out this site](http://aprs.gids.nl/nmea/)

If you look at the data in the above window, you can see that there are a lot of commas, with no data in between them. That's because this module is on my desk, indoors, and does not have a 'fix'. To get a fix, we need to put the module outside.

Danger: 

If you can get a really long USB cord (or attach a GPS antenna to the v3 modules) and stick the GPS out a window, so its pointing at the sky, eventually the GPS will get a fix and the window data will change over to transmit valid data like this:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/382/medium800/gps_fixed.gif?1447864280)

Look for the line that says&nbsp; **$GPRMC,194509.000,A,4042.6142,N,07400.4168,W,2.03,221.11,160412,,,A\*77** &nbsp;  
This line is called the RMC (Recommended Minimum) sentence and has pretty much all of the most useful data. Each chunk of data is separated by a comma.

The first part&nbsp; **194509.000** &nbsp;is the current time **GMT** (Greenwich Mean Time). The first two numbers **&nbsp;19&nbsp;** indicate the hour (1900h, otherwise known as 7pm) the next two are the minute, the next two are the seconds and finally the milliseconds. So the time when this screenshot was taken is 7:45 pm and 9 seconds. The GPS does not know what time zone you are in, or about "daylight savings" so you will have to do the calculation to turn GMT into your timezone

The second part is the 'status code', if it is a&nbsp; **V** &nbsp;that means the data is&nbsp; **V** oid (invalid). If it is an&nbsp; **A** &nbsp;that means its&nbsp; **A** ctive (the GPS could get a lock/fix)

The next 4 pieces of data are the geolocation data. According to the GPS, my location is **&nbsp;4042.6142,N**** &nbsp;**(Latitude 40 degrees, 42.6142 decimal minutes North) &&nbsp;**07400.4168,W**. (Longitude 74 degrees, 0.4168 decimal minutes West) To look at this location in Google maps, type&nbsp;**+40&nbsp; 42.6142', -74&nbsp; 00.4168'**&nbsp;into the&nbsp;[google maps search box](http://maps.google.com/)&nbsp;. Unfortunately gmaps requires you to use +/- instead of NSWE notation. N and E are positive, S and W are negative.

Danger: 

The next data is the ground speed in knots. We're going&nbsp; **2.03** &nbsp;knots

After that is the tracking angle, this is meant to approximate what 'compass' direction we're heading at based on our past travel

The one after that is&nbsp; **160412** &nbsp;which is the current date (16th of April, 2012).

Finally there is the&nbsp; **\*XX** &nbsp;data which is used as a data transfer checksum

Once you get a fix using your GPS module, verify your location with google maps (or some other mapping software). Remember that GPS is often only accurate to 5-10 meters and worse if you're indoors or surrounded by tall buildings.

- [Previous Page](https://learn.adafruit.com/adafruit-ultimate-gps/external-antenna.md)
- [Next Page](https://learn.adafruit.com/adafruit-ultimate-gps/arduino-wiring.md)

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

Out of Stock
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

- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
- [Ladyada's Learn Arduino - Lesson #2](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-2.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [Wireless Game Show Poppers for the Classroom!](https://learn.adafruit.com/wireless-game-show-poppers.md)
- [Wireless Gardening with Arduino + CC3000 WiFi Modules](https://learn.adafruit.com/wireless-gardening-arduino-cc3000-wifi-modules.md)
- [CircuitPython Essentials](https://learn.adafruit.com/circuitpython-essentials.md)
- [CircuitPython Libraries on Linux and ODROID C2](https://learn.adafruit.com/circuitpython-libaries-linux-odroid-c2.md)
- [2.2" TFT Display](https://learn.adafruit.com/2-2-tft-display.md)
- [RGB LED Matrix Basics](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix.md)
- [Halloween Pumpkin](https://learn.adafruit.com/halloween-pumpkin.md)
- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [Automatic Monitor Color Temperature Adjustment](https://learn.adafruit.com/automatic-monitor-color-temperature-adjustment.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [Skill Badge Requirements: Microcontrollers](https://learn.adafruit.com/skill-badge-requirements-microcontrollers.md)
- [RePaper eInk Development Board](https://learn.adafruit.com/repaper-eink-development-board.md)
