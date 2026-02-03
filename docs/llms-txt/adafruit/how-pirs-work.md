# Source: https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/how-pirs-work.md

# PIR Motion Sensor

## How PIRs Work

PIR sensors are more complicated than many of the other sensors explained in these tutorials (like photocells, FSRs and tilt switches) because there are multiple variables that affect the sensors input and output. To begin explaining how a basic sensor works, we'll use this rather nice diagram

The passive infrared (PIR) sensor itself has two slots in it, each slot is made of a special material that is sensitive to IR. The lens used here is not really doing much and so we see that the two slots can 'see' out past some distance (basically the sensitivity of the sensor). When the sensor is idle, both slots detect the same amount of IR, the ambient amount radiated from the room or walls or outdoors. When a warm body like a human or animal passes by, it first intercepts one half of the PIR sensor, which causes a_&nbsp;positive differential_&nbsp;change between the two halves. When the warm body leaves the sensing area, the reverse happens, whereby the sensor generates a negative differential change. These change pulses are what is detected.

![](https://cdn-learn.adafruit.com/assets/assets/000/035/647/medium800/proximity_pir-diagram.png?1473477850)

## The PIR Sensor
The IR sensor itself is housed in a hermetically sealed metal can to improve noise/temperature/humidity immunity. There is a window made of IR-transmissive material (typically coated silicon since that is very easy to come by) that protects the sensing element. Behind the window are the two balanced sensors.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/512/medium800/proximity_pyrosensor.gif?1447975942)

_[Left image from Murata datasheet](http://learn.adafruit.com/system/assets/assets/000/010/137/original/pyroelectrics21e.pdf)_

![](https://cdn-learn.adafruit.com/assets/assets/000/000/513/medium800/proximity_pyrodiagram.gif?1447975952)

_[Image from RE200B datasheet](http://learn.adafruit.com/system/assets/assets/000/010/134/original/RE200B.pdf)_

You can see above the diagram showing the element window, the two pieces of sensing material

![](https://cdn-learn.adafruit.com/assets/assets/000/000/514/medium800/proximity_pirinternalschem.gif?1447975961)

_[Image from RE200B datasheet](http://learn.adafruit.com/system/assets/assets/000/010/134/original/RE200B.pdf)_

This image shows the internal schematic. There is actually a JFET inside (a type of transistor) which is very low-noise and buffers the extremely high impedence of the sensors into something a low-cost chip (like the BIS0001) can sense.

## Lenses

PIR sensors are rather generic and for the most part vary only in price and sensitivity. Most of the real magic happens with the optics. This is a pretty good idea for manufacturing: the PIR sensor and circuitry is fixed and costs a few dollars. The lens costs only a few cents and can change the breadth, range, sensing pattern, very easily.

In the diagram up top, the lens is just a piece of plastic, but that means that the detection area is just two rectangles. Usually we'd like to have a detection area that is much larger. To do that, we use [a simple lens](http://en.wikipedia.org/wiki/Lens_%28optics%29)&nbsp;such as those found in a camera: they condenses a large area (such as a landscape) into a small one (on film or a CCD sensor). For reasons that will be apparent soon, we would like to make the PIR lenses small and thin and moldable from cheap plastic, even though it may add distortion. For this reason the sensors are actually [Fresnel lenses](http://en.wikipedia.org/wiki/Fresnel_lens):

![](https://cdn-learn.adafruit.com/assets/assets/000/000/515/medium800/proximity_sensorsmagfresnel.gif?1447975970)

_[Image from Sensors Magazine](http://www.sensorsmag.com/articles/0403/35/main.shtml)_

The Fresnel lens condenses light, providing a larger range of IR to the sensor.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/516/medium800/proximity_linearfresnel.gif?1447975978)

_[Image from BHlens.com](http://www.bhlens.com/linear_fresnel_lens.aspx)_

![](https://cdn-learn.adafruit.com/assets/assets/000/000/517/medium800/proximity_pirfocal.gif?1447975987)

_[Image from Cypress appnote 2105](http://learn.adafruit.com/system/assets/assets/000/010/138/original/an2105.pdf)_

OK, so now we have a much larger range. However, remember that we actually have two sensors, and more importantly we dont want two really big sensing-area rectangles, but rather a scattering of multiple small areas. So what we do is split up the lens into multiple section, each section of which is a fresnel lens.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/518/medium800/proximity_frenelled.jpg?1396763705)

_Here you can see the multiple facet-sections_![](https://cdn-learn.adafruit.com/assets/assets/000/000/519/medium800/proximity_frenelling.jpg?1396763710)

_This macro shot shows the different Fresnel lenses in each facet!_

The different faceting and sub-lenses create a range of detection areas, interleaved with each other. That's why the lens centers in the facets above are 'inconsistent' - every other one points to a different half of the PIR sensing element

![](https://cdn-learn.adafruit.com/assets/assets/000/000/520/medium800/proximity_NL11NH.gif?1447975995)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/521/medium800/proximity_NL11NH-side.gif?1447976005)

_[Images from NL11NH datasheet](http://learn.adafruit.com/system/assets/assets/000/010/135/original/NL11NH.pdf)_

Here is another image, more qualitative but not as quantitative. (Note that the sensor in the Adafruit shop is 110° not 90°)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/522/medium800/proximity_rounddetectlens.gif?1447976014)

_[Image from IR-TEC](http://www.irtec.com/ms-360.htm)_

- [Previous Page](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/overview.md)
- [Next Page](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/connecting-to-a-pir.md)

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
