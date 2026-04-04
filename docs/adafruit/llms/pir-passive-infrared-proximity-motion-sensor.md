# Source: https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor.md

# PIR Motion Sensor

## Overview

PIR sensors allow you to sense motion, almost always used to detect whether a human has moved in or out of the sensors range. They are small, inexpensive, low-power, easy to use and don't wear out. For that reason they are commonly found in appliances and gadgets used in homes or businesses. They are often referred to as PIR, "Passive Infrared", "Pyroelectric", or "IR motion" sensors.![](https://cdn-learn.adafruit.com/assets/assets/000/000/503/medium800/proximity_pirsensor.jpg?1396763621)

PIRs are basically made of a&nbsp;[pyroelectric sensor](http://en.wikipedia.org/wiki/Pyroelectric)&nbsp;(which you can see below as the round metal can with a rectangular crystal in the center), which can detect levels of infrared radiation. Everything emits some low level radiation, and the hotter something is, the more radiation is emitted. The sensor in a motion detector is actually split in two halves. The reason for that is that we are looking to detect motion (change) not average IR levels. The two halves are wired up so that they cancel each other out. If one half sees more or less IR radiation than the other, the output will swing high or low.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/504/medium800/proximity_pirlens.jpg?1396763628)

Along with the pyroelectic sensor is a bunch of supporting circuitry, resistors and capacitors. It seems that most small hobbyist sensors use the [BISS0001 ("Micro Power PIR Motion Detector IC")](http://learn.adafruit.com/system/assets/assets/000/010/133/original/BISS0001.pdf), undoubtedly a very inexpensive chip. This chip takes the output of the sensor and does some minor processing on it to emit a digital output pulse from the analog sensor.  
  
Our older PIRs looked like this:

![](https://cdn-learn.adafruit.com/assets/assets/000/000/505/medium800/proximity_piranno.gif?1447975932)

Our new PIRs have more adjustable settings and have a header installed in the 3-pin ground/out/power pads

![](https://cdn-learn.adafruit.com/assets/assets/000/013/829/medium800/proximity_PIRbackLabeled.jpg?1390935476)

For many basic projects or products that need to detect when a person has left or entered the area, or has approached, PIR sensors are great. They are low power and low cost, pretty rugged, have a wide lens range, and are easy to interface with. Note that PIRs won't tell you how many people are around or how close they are to the sensor, the lens is often fixed to a certain sweep and distance (although it can be hacked somewhere) and they are also sometimes set off by housepets. Experimentation is key!## Some Basic Stats

These stats are for the PIR sensor in the Adafruit shop which is very much [like the Parallax one](http://www.parallax.com/Store/Sensors/ObjectDetection/tabid/176/ProductID/83/List/0/Default.aspx?SortField=ProductName,ProductName) . Nearly all PIRs will have slightly different specifications, although they all pretty much work the same. If there's a datasheet, you'll want to refer to it

- **Size:** Rectangular
- **Price:** [$10.00 at the Adafruit shop](http://www.adafruit.com/index.php?main_page=product_info&cPath=35&products_id=189)
- **Output:** Digital pulse high (3V) when triggered (motion detected) digital low when idle (no motion detected). Pulse lengths are determined by resistors and capacitors on the PCB and differ from sensor to sensor.
- **Sensitivity range:** up to 20 feet (6 meters) 110° x 70° detection range
- **Power supply:** 5V-12V input voltage for most modules (they have a 3.3V regulator), but 5V is ideal in case the regulator has different specs
- **[BIS0001 Datasheet](http://learn.adafruit.com/system/assets/assets/000/010/133/original/BISS0001.pdf)** (the decoder chip used)
- **[RE200B datasheet](http://learn.adafruit.com/system/assets/assets/000/010/134/original/RE200B.pdf)** (most likely the PIR sensing element used)
- **[NL11NH datasheet](http://learn.adafruit.com/system/assets/assets/000/010/135/original/NL11NH.pdf)** (equivalent lens used)
- **[Parallax Datasheet on their version of the sensor](http://learn.adafruit.com/system/assets/assets/000/010/136/original/PIRSensor-V1.2.pdf "Link: http://learn.adafruit.com/system/assets/assets/000/010/136/original/PIRSensor-V1.2.pdf")**

More links!

- [A great page on PIR sensors from GLOLAB \\](http://www.glolab.com/pirparts/infrared.html "Link: http://www.glolab.com/pirparts/infrared.html")

- [Next Page](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/how-pirs-work.md)

## Primary Products

### PIR (motion) sensor

[PIR (motion) sensor](https://www.adafruit.com/product/189)
PIR sensors are used to detect motion from pets/humanoids from about 20 feet away (possibly works on zombies, not guaranteed). This one has an adjustable delay before firing (approx 2-4 seconds), adjustable sensitivity **and** we include a 1 foot (30 cm) cable with a socket so you...

In Stock
[Buy Now](https://www.adafruit.com/product/189)
[Related Guides to the Product](https://learn.adafruit.com/products/189/guides)

## Related Guides

- [HalloWing All-Seeing Skull](https://learn.adafruit.com/hallowing-all-seeing-skull.md)
- [Magical Mistletoe](https://learn.adafruit.com/magical-mistletoe.md)
- [Screaming Cauldron](https://learn.adafruit.com/screaming-cauldron.md)
- [IoT Bird Feeder with Camera](https://learn.adafruit.com/iot-window-bird-feeder-with-camera.md)
- [No-Code WipperSnapper Summoning Horn](https://learn.adafruit.com/adafruit-io-wippersnapper-summoning-horn.md)
- [Motion Controlled Matrix Bed Clock](https://learn.adafruit.com/motion-controlled-matrix-bed-clock.md)
- [Adafruit VCNL4020 Proximity and Light Sensor](https://learn.adafruit.com/adafruit-vcnl4020-proximity-and-light-sensor.md)
- [Fog Machine with Motion Sensor and Adafruit IO](https://learn.adafruit.com/fog-machine-remote-trigger.md)
- [Feather Freezer Door Alarm](https://learn.adafruit.com/feather-door-alarm.md)
- [MIDI Laser Harp with Time of Flight Distance Sensors](https://learn.adafruit.com/midi-laser-harp-time-of-flight-sensors.md)
- [Using Adafruit IO Actions to Make an IoT Door Detector](https://learn.adafruit.com/using-adafruit-io-actions-to-make-an-iot-door-detector.md)
- [Quadcopter Spray Can Mod](https://learn.adafruit.com/quadcopter-spray-can-mod.md)
- [Adafruit VCNL4040 Proximity Sensor](https://learn.adafruit.com/adafruit-vcnl4040-proximity-sensor.md)
- [Using ItsaSNAP for HomeKit PIR Motion Detection](https://learn.adafruit.com/itsasnap-homekit-pir-motion-detection.md)
- [No-Code Room Occupancy Status ](https://learn.adafruit.com/no-code-room-occupancy-status.md)
