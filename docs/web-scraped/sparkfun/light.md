# Source: https://learn.sparkfun.com/tutorials/light

## Introduction

Manipulation of light is a very useful skill for any electronics tinkerer. From illumination to [distance sensing](https://www.sparkfun.com/distance_sensing), light bridges the electronic and the physical in myriad useful ways.

### Wavelength

The key defining feature of a beam of light is its **wavelength**. Light travels through space as a wave, and the distance between two wave peaks is the wavelength of that beam of light. In human terms, the wavelength is what determines the color of a light beam.

[![alt text](//cdn.sparkfun.com/assets/3/8/7/2/b/51153f6ece395f7b28000004.png)](//cdn.sparkfun.com/assets/3/8/7/2/b/51153f6ece395f7b28000004.png)

*Wavelength is usually denoted by the greek character **λ** (pronounced \"lamb-da\") (Image by Wikipedia user [dicklyon](http://en.wikipedia.org/wiki/User:Dicklyon)).*

Because nothing in physics can be simple, a light beam also behaves as a stream of particles, or **photons** (masochists can refer to [this article on the wave/particle duality of light](http://en.wikipedia.org/wiki/Wave%E2%80%93particle_duality)). Shorter wavelength light has more energy per photon.

### Intensity

The other characteristic of a beam of light is its intensity. [Radiant intensity](http://en.wikipedia.org/wiki/Radiant_intensity) is measured by the rate at which energy intersects the surface of the sphere bounded by that circle at the top of the ice cream cone, in watts per steradian. To understand this, imagine a sphere with a teeny, tiny star in the center. Light is spreading out from the star in all directions equally. Now, add an ice cream cone with its point in the center of the star, extending to the surface of the sphere. The angle at the bottom of the cone is one radian (there are 2π radians in a circle; one radian is approximately 57.3°). The area defined by this imaginary ice cream cone is called a [steradian](http://en.wikipedia.org/wiki/Steradian).

[![alt text](//cdn.sparkfun.com/assets/b/3/3/c/2/51154092ce395f6f3f000002.png)](//cdn.sparkfun.com/assets/b/3/3/c/2/51154092ce395f6f3f000002.png)

*Graphical depiction of a steradian. A beam of light\'s radiant intensity is described by the wattage of the light beam divided by this surface area (Image courtesy of [wikimedia commons](http://commons.wikimedia.org/wiki/File:Steradian.svg).)*

### Visible light versus invisible light

When we talk about light, we generally mean **visible** light\--the wonderful stuff of rainbows and sunshine. Light, however, spans a very, very wide range of wavelengths. This is referred to as the electromagnetic spectrum.

[![The electromagnetic spectrum](//cdn.sparkfun.com/r/600-600/assets/3/9/c/1/c/512bccd7ce395f4147000000.png)](//cdn.sparkfun.com/assets/3/9/c/1/c/512bccd7ce395f4147000000.png)

*The full spectrum of electromagnetic radiation. Visible light is a very small part! Image created by [Philip Ronan](http://commons.wikimedia.org/wiki/User:Sakurambo)).*

At one end, there are gamma rays and X-rays, which are nasty, high energy ionizing electromagnetic radiation that are fundamentally incompatible with life. At the other end, very low-frequency, long-wavelength radio waves carry information across vast distances, yielding glimpses into the very origins of the universe itself.

In this article, we\'ll be sticking to visible light and the areas closest to it: infrared and ultraviolet. From ultraviolet through far infrared, light behaves pretty similarly to what we\'re used to seeing with visible light: shadows are cast, lenses can focus it, it can be diffused by, say, a white sheet of paper, etc. Once you move out into the longer and shorter wavelengths, things start to get weird, and we\'ll reserve discussion of that for another lesson.

We\'re going to discuss light in three different groups: ultraviolet, visible, and infrared. Ultraviolet light is light which has a wavelength just slightly shorter than visible light; infrared, just slightly longer. Of the three groups, visible and infrared are somewhat more useful and common in electronics, and we\'ll give them correspondingly more time.

*Tutorial thumbnail courtesy [D-Kuru/Wikimedia Commons](http://commons.wikimedia.org/wiki/User_talk:D-Kuru).*

## Ultraviolet Light

[Ultraviolet light](http://en.wikipedia.org/wiki/Ultraviolet) is light between 10nm and 400nm, which places it between X-rays and visible light. Ultraviolet can be very harmful to life forms\--you\'re probably most familiar with its effects in the form of sunburn.

[![Ultraviolet spectrum](//cdn.sparkfun.com/r/600-600/assets/e/3/4/9/2/512bccd7ce395f5147000000.png)](//cdn.sparkfun.com/assets/e/3/4/9/2/512bccd7ce395f5147000000.png)

### Ultraviolet-A

UVA (315nm to 400nm wavelength) is the lowest energy band of ultraviolet light. It is nearly visible to humans, and many insects, and even some birds, can see into this light band. White fluorescent bulbs and white LEDs work by exposing a material to UVA light, which absorbs the UVA photons and emits photons in the visible spectrum, appearing white to us.

UVA is also often used to detect counterfeit documents; as a hedge against counterfeiting, many documents (passports, driver\'s licenses, and bank notes, to name a few) will include a watermark that glows under UVA radiation. Blacklight posters are another example of things which react to UVA light, and bleach, soap, and many biological materials will also glow when exposed to UVA.

[![alt text](//cdn.sparkfun.com/assets/3/5/b/f/b/5115424fce395f763d000001.jpg)](//cdn.sparkfun.com/assets/3/5/b/f/b/5115424fce395f763d000001.jpg)

*Anti-counterfeiting features in a US \$20 bill revealed by a [400nm UVA LED](https://www.sparkfun.com/products/8662).*

Most of the UVA light in a sunbeam reaches the earth\'s surface.

### Ultraviolet-B

UVB (280nm to 315nm) is a higher energy level light than UVA. It is found in sunlight, and is responsible not only for the skin damage that causes sunburn and skin cancer but also the synthesis of Vitamin D in the human body. It is also produced by welding torches; even brief exposure to the flare from a welding torch, and even at a reasonable distance, can cause serious eye damage if the viewer is not protected.

[![Welding torch flare](//cdn.sparkfun.com/r/400-400/assets/9/2/7/6/9/51155647ce395fe73d000003.jpg)](//cdn.sparkfun.com/assets/9/2/7/6/9/51155647ce395fe73d000003.jpg)

*Welding torches create a lot of UVB and UVC light. Welders must minimize exposure to avoid sunburn and eye damage ([Image](http://en.wikipedia.org/wiki/File:Pipefitter_welder_kutzo.jpg) courtesy wikipedia).*

UVB light is fairly well blocked by normal window glass; this is why hanging an arm out of an open car window can result in a sunburn affecting that arm only. [Richard Feynman](http://en.wikipedia.org/wiki/Feynman) (Nobel laureate and noted bongo musician) observed the Trinity nuclear test explosion using the windscreen of a pickup truck to protect himself from the ultraviolet radiation emitted by the blast.

Only about 10% of the UVB light emitted by the sun reaches earth\'s surface; the other 90% is absorbed by the atmosphere (primarily the ozone layer).

#### Ultraviolet-C

UVC ( 100nm to 280nm) tends to be the limit of the interesting UV light for us. Almost none of the sun\'s UVC reaches the earth\'s surface; the atmosphere does a very effective job of screening it away.

In the bad old days, before EEPROM memory and flash memory (which can be erased and rewritten electronically), the only non-volatile, non-magnetic means of electronic data storage was the EPROM. Once an EPROM was written, it could only be erased by being exposed to a strong source of UVC light for 20-30 minutes. For a hobbyist, that\'s a long time to wait to find out if the changes you made to your code fixed a bug!

[![UV-erasable microchip](//cdn.sparkfun.com/r/400-400/assets/e/c/f/7/8/51155935ce395ff771000001.jpg)](//cdn.sparkfun.com/assets/e/c/f/7/8/51155935ce395ff771000001.jpg)

*An old UV-erasable PIC16C765 microcontroller. The window over the die is made of quartz, because normal glass is not transparent to ultraviolet light.*

## Visible Light

Visible light is light in the range of (approximately) 380nm to 740nm. This can vary; some people\'s eyes will be able to detect light of lower or higher wavelengths than this, but in general, most humans\' eyes are sensitive to this region.

[![Visible spectrum of light](//cdn.sparkfun.com/r/600-600/assets/3/a/0/e/5/512bccd7ce395f4047000000.png)](//cdn.sparkfun.com/assets/3/a/0/e/5/512bccd7ce395f4047000000.png)

### The Human Eye

There are two peculiarities in the way the human eye perceives light: our eyes are sensitive to different wavelengths in different amounts, and our eyes perceive light intensity logarithmically rather than linearly.

#### Perception of Color

As you can see on this chart, our eyes pick up different wavelengths of light with different efficiency, mixing the perceived intensities to yield what we refer to as a \"color\". Furthermore, you can also see that at low light levels, our perception of color becomes skewed.

[![Luminosity curves for the human eye](//cdn.sparkfun.com/assets/6/d/3/6/c/51193819ce395f1a49000000.png)](//cdn.sparkfun.com/assets/6/d/3/6/c/51193819ce395f1a49000000.png)

*[Scotopic and photopic luminosity curves](http://en.wikipedia.org/wiki/Luminous_intensity) for the human eye. These curves show the perceived intensity of a light source by wavelength, assuming the [radiant intensity](http://en.wikipedia.org/wiki/Radiant_intensity) of the light sources are all equal.*

Because of this, a special unit of light intensity, the **candela**, was developed. The candela weights the intensity of a light source according to its color; a human eye will perceive a one-candela light source to be of similar brightness to another one-candela light source, regardless of wavelength. LED brightness is typically given in terms of millicandelas (mcd), and a great demonstration of the perceived intensity difference across colors can be seen when considering the intensity of an RGB LED such as [this one](https://www.sparkfun.com/products/105): 800mcd for the red, 4000mcd for the green, and 900mcd for the blue. I\'ve marked the wavelengths of those three colors (625nm, 520nm, and 467.5nm) on the chart below.

[![RGB LED marked on photopic curve](//cdn.sparkfun.com/r/600-600/assets/b/2/7/2/a/51155ce7ce395f523d000008.png)](//cdn.sparkfun.com/assets/b/2/7/2/a/51155ce7ce395f523d000008.png)

*The relative intensities of the blue, green, and red LEDs in a [tricolor LED](https://www.sparkfun.com/products/105) have been marked on this photopic curve. Compare the relative intensities (0.3 for the red, 0.7 for the green, and 0.15 for the blue) to the millicandela ratings for the three colors given by the LEDs datasheet (800mcd, 4000mcd, and 900mcd). The ratios aren\'t exact. While blue has a slightly higher mcd than red, blue is lower on the curve. The mcd rating for green is higher than both colors on the curve.*

The eye can be fooled into detecting wavelengths of light that are not present by mixing different wavelengths; it is by this principle which most color displays work. Only three colors (some form of red, green, and blue) are actually available; by mixing those three light colors at different intensities, the vast majority of natural colors can be simulated (at least, as far as our eyes are concerned).

[![Color mixing diagram](//cdn.sparkfun.com/r/600-600/assets/c/9/f/0/e/51155bb0ce395fe03f000002.png)](//cdn.sparkfun.com/assets/c/9/f/0/e/51155bb0ce395fe03f000002.png)

*Color mixing of red, green and blue light sources. By tweaking the light levels, a vast number of other light colors can be simulated.*

#### Perception of Intensity

We naturally tend to think of light as a linear phenomenon. Given two light sources, we may reasonably perceive one to be twice as bright as the other. We\'ve already seen how this can be affected by color; now let\'s consider the intensity of a light of a single color relative to our perception of it. The intensity of an LED varies linearly with the current being used to drive it.

[![LED current versus intensity](//cdn.sparkfun.com/r/600-600/assets/7/7/c/2/9/512bde8ece395ff642000000.png)](//cdn.sparkfun.com/assets/7/7/c/2/9/512bde8ece395ff642000000.png)

*Actual data gathered by pointing an LED at a photodiode and linearly increasing the LED drive current linearly from 0-25mA.*

Let\'s do a little experiment. If you have an Arduino, breadboard, resistor, LED, and a pushbutton, whip up this circuit, [download the code](//cdn.sparkfun.com/assets/a/f/2/9/5/51158420ce395fba23000000.ino), and throw the code onto the Arduino.

[![Fritzing Diagram of Simple LED Circuit and Arduino](//cdn.sparkfun.com/r/600-600/assets/1/4/b/8/6/511583f6ce395fd023000000.png)](//cdn.sparkfun.com/assets/1/4/b/8/6/511583f6ce395fd023000000.png)

This circuit is pretty simple: push the button once, and the LED will turn on. Push it and hold it, and the LED will start to get brighter. Release it, and the LED will stop getting brighter and the Arduino will print out over the serial port how much brighter the LED was when you stopped it getting brighter than it was when it started. Try to stop the LED when it is twice as bright as it was when it started.

Why is it so hard? The light output of an LED is linear, so doubling the current through the LED doubles the amount of light energy it is emitting. However, your eye does not respond in a linear fashion, it responds logarithmically. The reason for this is simple: our eyes need to provide us with useful information across a full range of lighting conditions, from starlight to daylight. On a cloudless night under a full moon, the light intensity is only 1/440,000th that of a sunny day, yet our eyes must function well at both of those extremes and everywhere in between! That makes judging a linear light source\'s relative brightness very difficult.

#### Color blindness

Color blindness is not, as the name would suggest, a simple inability to perceive color. There are in fact many varieties of color blindness; the most common, red-green color blindness, affects almost 10% of the male population to some degree.

Color blindness can be diagnosed by a [simple test](http://www.micro.magnet.fsu.edu/primer/java/humanvision/colorblindness/index.html), where the subject is asked to identify patterns or symbols created from dots of a different color against a background of similarly-sized dots.

[![Ishihara test plate](//cdn.sparkfun.com/assets/e/c/3/a/8/5119343ece395fc24b000000.png)](//cdn.sparkfun.com/assets/e/c/3/a/8/5119343ece395fc24b000000.png)

*Test plate from the Ishihara color blindness test. A person with normal color vision will see the number 74; color blind persons may see the number 21 or no number at all, depending on the type of deficiency present.*

As a kindness to those of us with color blindness, please try not to use color to convey information. Good examples of bad design include LEDs which change color to signify a condition (green means \"okay\", red means \"failure\"), maps using a range of colors to connect a numerical value to a region, and text colors other than white-on-black or black-on-white.

## Infrared Light

Infrared light is light with a longer wavelength than visible light, but a shorter wavelength than microwave. It has arbitrarily been chosen to start at 700nm and stop at 1mm (1,000,000nm), making it a far larger segment of the spectrum than ultraviolet or visible light. Something like 55% of the light energy reaching the earth\'s surface from the sun is infrared.

[![Infrared light spectrum](//cdn.sparkfun.com/r/600-600/assets/7/8/9/8/2/512bccd7ce395f4d47000000.png)](//cdn.sparkfun.com/assets/7/8/9/8/2/512bccd7ce395f4d47000000.png)

### Near-Infrared

**Near-infrared** is a region of great interest in electronics: this is the region within which infrared remote controls, object sensors, and distance detectors operate. It is just barely above the visible range, and is extremely easy to both create and detect with solid-state technologies.

[![IR Emitter/Detector Pair](//cdn.sparkfun.com/assets/5/4/e/5/3/5115878bce395fa020000000.jpg)](//cdn.sparkfun.com/assets/5/4/e/5/3/5115878bce395fa020000000.jpg)

*[SparkFun\'s matched infrared emitter/detector pair.](https://www.sparkfun.com/products/241) Inexpensive, but extremely susceptible to interference from both visible and infrared light in the environment.*

The near-infrared band extends up to 1400nm. Common emitter wavelengths are [850nm](https://www.sparkfun.com/products/9469) and [950nm](https://www.sparkfun.com/products/9349). There is a tremendous amount of near-infrared light surrounding us at all times; the potential for interference with infrared signaling and sensing is great. Most infrared signaling systems (such as [infrared remote controls](http://learn.sparkfun.com/tutorials/ir-remote-control) solve this by modulating the beam at a fixed frequency, rather than attempting to filter out light which is not of the desired wavelength.

[![alt text](//cdn.sparkfun.com/assets/2/4/9/6/7/51158873ce395ffa23000001.jpg)](//cdn.sparkfun.com/assets/2/4/9/6/7/51158873ce395ffa23000001.jpg)

*[Modulated IR receiver module](https://www.sparkfun.com/products/10266). This small IC looks for infrared light being pulsed at 38kHz and attempts to interpret it as a data signal.*

Near-infrared is well detected by digital cameras, too. So well detected, in fact, that most digital cameras have a physical filter to block out infrared wavelengths. This filter can be removed, allowing greater sensitivity in the infrared range. A simple filter which allows infrared light to pass but blocks visible light can be created out of 35mm film negatives; the tag end of the film roll which has no pictures on it is perfect for this.

[![IR image vs. Visible image](//cdn.sparkfun.com/assets/8/b/5/2/a/51158e1bce395fb220000006.jpg)](//cdn.sparkfun.com/assets/8/b/5/2/a/51158e1bce395fb220000006.jpg)

*Two pictures of the same scene. The image on the left was taken in a darkened room with a cheap webcam that has had its infrared filter removed and replaced by film negatives, and the image on the right was taken with a standard point-and-shoot camera.*

### Long-wavelength Infrared

Long-wavelength infrared is light in the 8000nm-15000nm range. This is the thermal imaging zone, where all of those amazing false-color images detailing the relative temperature of things come from.

[![False-color infrared image](//cdn.sparkfun.com/r/600-600/assets/8/c/5/2/1/511917bbce395fef32000000.jpg)](//cdn.sparkfun.com/assets/8/c/5/2/1/511917bbce395fef32000000.jpg)

*The same scene in the visible spectrum and the long-wavelength infrared. Notice that the plastic bag is opaque to visible light but nearly transparent to infrared (courtesy NASA Spitzer Infrared Telescope team).*

It\'s a common mistake for people to misunderstand the difference between near-infrared imaging and long-wave infrared imaging. Near-infrared imaging is pretty easy to achieve\--standard CMOS and CCD imaging chips can easily detect light in the near-infrared region. Long-wave IR requires special sensors, since the light beam has a wavelength 1000 times longer than near-IR. This requires a correspondingly larger geometry in the sensor elements.

[![Long-wave IR temp sensor](//cdn.sparkfun.com/assets/5/1/0/3/2/5119308cce395f2c39000000.jpg)](//cdn.sparkfun.com/assets/5/1/0/3/2/5119308cce395f2c39000000.jpg)

*A long-wave [IR temperature sensor](https://www.sparkfun.com/products/9570). The longer wavelength requires a larger sensing region than visible or near-IR applications.*

Another increasingly familiar use of this region is laser etching and cutting. Most laser cutters rely on a CO~2~ laser tubes to generate the laser beam at a wavelength of 10640nm.