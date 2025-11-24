# Source: https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/testing-a-pir.md

# PIR Motion Sensor

## Testing a PIR

![](https://cdn-learn.adafruit.com/assets/assets/000/000/536/medium800/proximity_pirtestsch.gif?1447976024)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/537/medium800/proximity_pirtestbb.gif?1447976032)

Now when the PIR detects motion, the output pin will go "high" to 3.3V and light up the LED!

Once you have the breadboard wired up, insert batteries and wait 30-60 seconds for the PIR to 'stabilize'. During that time the LED may blink a little. Wait until the LED is off and then move around in front of it, waving a hand, etc, to see the LED light up!

# Retriggering
There's a couple options you may have with your PIR. First up we'll explore the 'Retriggering' option.   
  
Once you have the LED blinking, look on the back of the PIR sensor and make sure that the jumper is placed in the **L** position as shown below.   
![](https://cdn-learn.adafruit.com/assets/assets/000/000/538/medium800/proximity_pirback.jpg?1396763855)

![](https://cdn-learn.adafruit.com/assets/assets/000/013/842/medium800/proximity_triggerlow.jpg?1390948837)

Now set up the testing board again. You may notice that when connecting up the PIR sensor as above, the LED does not stay on when moving in front of it but actually turns on and off every second or so. That is called "non-retriggering".![](https://cdn-learn.adafruit.com/assets/assets/000/000/539/medium800/proximity_non-retriggerable.gif?1447976040)

Now change the jumper so that it is in the **&nbsp;H&nbsp;** position. If you set up the test, you will notice that now the LED&nbsp;_does_&nbsp;stay on the entire time that something is moving. That is called "retriggering".

![](https://cdn-learn.adafruit.com/assets/assets/000/000/540/medium800/proximity_retriggerable.gif?1447976050)

(The graphs above are from the BISS0001 datasheet, they kinda suck)

For most applications, "retriggering" (jumper in H position as shown below) mode is a little nicer.

![](https://cdn-learn.adafruit.com/assets/assets/000/013/843/medium800/proximity_triggerhigh.jpg?1390948864)

If you need to connect the sensor to something edge-triggered, you'll want to set it to "non-retriggering" (jumper in L position).

# Changing sensitivity
  
The Adafruit PIR has a trimpot on the back for adjusting sensitivity. You can adjust this if your PIR is too sensitive or not sensitive enough - clockwise makes it more sensitive.  
![](https://cdn-learn.adafruit.com/assets/assets/000/013/845/medium800/proximity_189bottom_LRG.jpg?1390950175)

# Changing Pulse Time and Timeout Length
There are two 'timeouts' associated with the PIR sensor. One is the " **Tx**" timeout: how long the LED is lit after it detects movement - this is easy to adjust on Adafruit PIR's because there's a potentiometer.   
  
The second is the " **Ti**" timeout which is how long the LED is guaranteed to be off when there is no movement. This one is not _easily_ changed but if you're handy with a soldering iron it is within reason.

First, lets take a look at the BISS datasheet again

![](https://cdn-learn.adafruit.com/assets/assets/000/000/541/medium800/proximity_titx.gif?1447976058)

On Adafruit PIR sensors, there's a little trim potentiometer labeled **TIME.** This is a 1 Megaohm adjustable resistor which is added to a 10K series resistor. And **C6** is 0.01uF so

> **Tx = 24576 x (10K + Rtime) x 0.01uF**

If the Rtime potentiometer is turned all the way down counter-clockwise (to 0 ohms) then  

> **Tx = 24576 x (10K) x 0.01uF = 2.5** seconds (approx)

If the Rtime potentiometer is turned all the way up clockwise to 1 Megaohm then  

> **Tx = 24576 x (1010K) x 0.01uF = 250** seconds (approx)

If RTime is in the middle, that'd be about 120 seconds (two minutes) so you can tweak it as necessary. For example if you want motion from someone to turn on a fan for a minimum of 1 minute, set the Rtime potentiometer to about 1/4 the way around.   
# For older/other PIR sensors
  
If you have a PIR sensor from somewhere else that does not have a potentiometer adjust, you can trace out the adjustment resistors this way:  

![](https://cdn-learn.adafruit.com/assets/assets/000/000/542/medium800/proximity_pirtitx.gif?1447976069)

Determining R10 and R9 isnt too tough. Unfortunately this PIR sensor is mislabeled (it looks like they swapped R9 R17). You can trace the pins by looking at the BISS001 datasheet and figuring out what pins they are - R10 connects to pin 3 and R9 connects to pin 7. the capacitors are a little tougher to determine, but you can 'reverse engineer' them from timing the sensor and solving!

For example:

> **Tx is = 24576 \* R10 \* C6 = ~1.2 seconds**   
> **R10** = 4.7K and **C6** = 10nF

Likewise,

> **Ti = 24 \* R9 \* C7 = ~1.2 seconds**   
> **R9** = 470K and **C7** = 0.1uF

You can change the timing by swapping different resistors or capacitors. For a nice tutorial on this, see [Keith's PIR hacking page](http://www.neufeld.newton.ks.us/electronics/?p=208 "Link: http://www.neufeld.newton.ks.us/electronics/?p=208").

- [Previous Page](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/connecting-to-a-pir.md)
- [Next Page](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/using-a-pir-w-arduino.md)

## Primary Products

### PIR (motion) sensor

[PIR (motion) sensor](https://www.adafruit.com/product/189)
PIR sensors are used to detect motion from pets/humanoids from about 20 feet away (possibly works on zombies, not guaranteed). This one has an adjustable delay before firing (approx 2-4 seconds), adjustable sensitivity **and** we include a 1 foot (30 cm) cable with a socket so you...

In Stock
[Buy Now](https://www.adafruit.com/product/189)
[Related Guides to the Product](https://learn.adafruit.com/products/189/guides)

## Related Guides

- [PropMaker Jack O'Lantern](https://learn.adafruit.com/propmaker-jack-o-lantern.md)
- [No-Code WipperSnapper Summoning Horn](https://learn.adafruit.com/adafruit-io-wippersnapper-summoning-horn.md)
- [Capacitive Touch Holiday Light Control](https://learn.adafruit.com/capacitive-touch-holiday-light-control.md)
- [Raspberry Pi Video Synth with Blinka and Processing](https://learn.adafruit.com/raspberry-pi-video-synth-with-blinka-and-processing.md)
- [Magical Mistletoe](https://learn.adafruit.com/magical-mistletoe.md)
- [Proximity Based Lighting](https://learn.adafruit.com/proximity-based-lighting.md)
- [Calibrating Sensors](https://learn.adafruit.com/calibrating-sensors.md)
- [Fog Machine with Motion Sensor and Adafruit IO](https://learn.adafruit.com/fog-machine-remote-trigger.md)
- [Feather Freezer Door Alarm](https://learn.adafruit.com/feather-door-alarm.md)
- [Tombstone Prop-Maker RP2040](https://learn.adafruit.com/tombstone-prop-maker-rp2040.md)
- [Track a Turtle with WipperSnapper](https://learn.adafruit.com/track-a-turtle-with-wippersnapper.md)
- [Sitcom SFX Door Trigger](https://learn.adafruit.com/sitcom-sfx-door-trigger.md)
- [Tree with Animated Eyes and Motion Sensor](https://learn.adafruit.com/tree-ent-sculpture-with-animated-eyes.md)
- [MIDI Laser Harp with Time of Flight Distance Sensors](https://learn.adafruit.com/midi-laser-harp-time-of-flight-sensors.md)
- [LPC824 NeoPixel IR Distance Sensor](https://learn.adafruit.com/lpc824-neopixel-ir-distance-sensor.md)
