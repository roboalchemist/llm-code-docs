# Source: https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/connecting-to-a-pir.md

# PIR Motion Sensor

## Connecting to a PIR

![](https://cdn-learn.adafruit.com/assets/assets/000/013/840/medium800/proximity_189_LRG.jpg?1390948374)

Most PIR modules have a 3-pin connection at the side or bottom. The pinout may vary between modules so triple-check the pinout! It's often silkscreened on right next to the connection (at least, ours is!) One pin will be ground, another will be signal and the final one will be power. Power is usually 3-5VDC input but may be as high as 12V. Sometimes larger modules don't have direct output and instead just operate a relay in which case there is ground, power and the two switch connections.

The output of some relays may be 'open collector' - that means it requires a pullup resistor. If you're not getting a variable output be sure to try attaching a 10K pullup between the signal and power pins.

An easy way of prototyping with PIR sensors is to connect it to a breadboard since the connection port is 0.1" spacing. Some PIRs come with header on them already, the one's from adafruit have a straight 3-pin header on them for connecting a cable

![](https://cdn-learn.adafruit.com/assets/assets/000/013/839/medium800/proximity_189bottom_LRG.jpg?1390948358)

For our PIR's the red cable is + voltage power, black cable is - ground power and yellow is the signal out. Just make sure you plug the cable in as shown above! If you get it backwards you won't damage the PIR but it won't work.

- [Previous Page](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/how-pirs-work.md)
- [Next Page](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/testing-a-pir.md)

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
