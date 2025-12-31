# Source: https://learn.sparkfun.com/tutorials/hacker-in-residence-the-harmonic-skew-zoetrope

## Introduction

There are many things in our world that appear constant but are actually flickering at frequencies faster than we can easily perceive. Whether it's the rapid sequence video frames, the alternating current in our power outlets (and the resultant imperceptible blinking of our light fixtures), or even the compression and rarefaction of the air molecules that make up sound waves, these frequencies are all around us.

Sometimes the curtain is pulled back and we can see evidence of these frequencies. The [wagon wheel effect](http://en.wikipedia.org/wiki/Wagon-wheel_effect) is one such case. Sometimes, these artifacts are undesirable (like banding in video of a screen), but other times they are the underlying mechanic of a device's functionality (like a [zoetrope](http://en.wikipedia.org/wiki/Zoetrope)).

The Harmonic Skew Zoetrope uses moving subject matter and scanning lines of light to create the experience of visual distortion somewhat similar to [slit scan photography](http://en.wikipedia.org/wiki/Slit-scan_photography), but without the mediation of a screen.

-Hacker in Residence, [Jesse Harding](http://www.cosmicharding.com)

### Suggested Reading

- [Harmonics Wikipedia Entry](http://en.wikipedia.org/wiki/Harmonic)
- [Rolling Shutter Wikipedia Entry](http://en.wikipedia.org/wiki/Rolling_shutter)
- [Optics Wikipedia Entry](http://en.wikipedia.org/wiki/Optics)
- [Interferometry](http://en.wikipedia.org/wiki/Interferometry)

## Tools and Materials

Here is a list of the tools and materials used in this project. If you would like to replicate this project on your own, you may need to search for the right combination of materials.

- Motor
- Eccentric Roller
- Bearing
- Tension Springs
- Spinning Mirror (with motor)
- Laser Diode (with cylindrical lens)
- Adjustable Laser Diode Mount
- Power Supplies
- Speed Control (potentiometer or microcontroller)

## Hardware Assembly

Let\'s take a look at some of the parts that make up the Harmonic Skew Zoetrope. But first, a public service announcement\...

### Traveling with Electronic Components

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/0/TSAsmall.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/0/TSAsmall.JPG)

When you travel by plane with loose electronic components, be ready to answer any and all questions the TSA may have for you. Its best to keep that stuff at the top of your bag so that they don't have to rummage around when they inevitably search your stuff. Try to stay pleasant, and try to be descriptive but not overly technical.

### Eccentric Roller Assembly

The main motor is mounted with the shaft pointing up so that we can make an object oscillate in a horizontal plane. Mounted to the shaft of the motor is a piece of aluminum with the mounting hole off-center (essentially like a vibration motor). This piece of aluminum will roll inside the bore of a ball bearing, the outside of which will be mounted to a platform that will be kept from rotating by tension springs on the corners.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/0/tensionsmall.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/0/tensionsmall.JPG)

Depending on the size of motor and platform, a counterweight may be required to mitigate vibration.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/0/CASEYTEST.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/0/CASEYTEST.jpg)

*Testing the motor for current draw and vibration*

### Laser & Spinning Mirror Assembly

The cylindrical lens will bend the laser light in just one dimension, turning a point of light into a line of light. This allows us to scan the object so that the top and bottom of the object are illuminated at different points in time, but all points at the same height are illuminated at the same time.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/0/laser.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/0/laser.jpg)

I chose to use a dodecagonal mirror (12 sides) to reflect the laser light over approximately 60 degrees. More sides will decrease the amount of area over which the laser will scan. If the laser is scanning a larger area than the object, there will be more time that the object is not illuminated, which I wanted to avoid.

Here at SparkFun, we 3D printed a dodecagonal prism shape, hot glued mirrors onto each face, and attached it to a motor.

Once the spinning mirror is mounted, the laser can be mounted so that it is reflected toward the object. The adjustable mount allows you to fine tune this position. The closer you get the laser to the mirror, the larger the area illuminated by the scanning laser.

The speed of the oscillation of the object needs to be at or near a harmonic of the laser scan frequency (which is equal to 12 times the RPM of the motor, due to the number of sides). To match these frequencies, I used a potentiometer to vary the speed of the motor that spins the mirror, but you could also use an Arduino to read and control the speeds of both motors.

## Results 

IT WORKED!!! :)

I tested the Harmonic Skew Zoetrope with several objects: a piece of wood, a baby doll head, and finally a miniature skull.

The choice of a skull as the object to be distorted is a nod to Hans Holbein's painting from 1533, [The Ambassadors](http://en.wikipedia.org/wiki/The_Ambassadors_%28Holbein%29).

### THANK YOU!

I want to thank everyone at SparkFun for being so helpful, specifically Toni Klopfenstein, Evan Spitler, Casey Kuhns, Mike Grusin, Byron Jacquot, Jeff Branson, and Nathan Seidle! You guys were great!!!