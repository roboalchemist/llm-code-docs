# Source: https://learn.adafruit.com/pi-video-output-using-pygame.md

# Pi Video Output Using pygame

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/002/324/medium800/raspberry_pi_graticule.jpg?1396781737)

http://www.youtube.com/watch?v=Yj0gxhUTqbw&amp;feature=youtu.be

One of the biggest advantages of the Raspberry Pi as a development platform is the easy access you have to a lot of mature, well-designed&nbsp;SW stacks and libraries, making it relatively trivial to perform tasks that would be very complex or time-consuming to implement&nbsp;on deeply embedded mcu-based systems.  
  
One of the areas where this is particularly true is with graphics and user interfaces. &nbsp;The HW requirements are fairly high to be able to work with large displays (larger than say 320x240 pixels), and even if you can meet the timing requirements -- a 7" 800x480 display probably&nbsp;requires ~40MHz for the pixel clock -- there are very few open source or inexpensive graphics frameworks out there to render the kinds of modern UIs people expect today.  
  
The Pi is really stands out here since it's trivial to render complex UIs, taking advantage of modern features like Unicode text and&nbsp;complex scripts, and being able to use different fonts without having to worry about memory and rendering time (it can take a couple hundred KB of SRAM to render a TTF on an embedded system, and the libraries to interpret them are both large and complex), etc.&nbsp;You can also easily display the graphics on any inexpensive composite television or HDMI monitor, which is amazing for a $35 board ... more than the cost of many LCDs!  
  
This tutorial will show you one way to get started drawing graphics on an external display using [pygame](http://www.pygame.org/news.html "Link: http://www.pygame.org/news.html") along with&nbsp;[Adafruit's WebIDE](http://learn.adafruit.com/webide/overview "Link: http://learn.adafruit.com/webide/overview"), and almost any&nbsp;external display ([several are available here](http://www.adafruit.com/category/105 "Link: http://www.adafruit.com/category/105")).

# What You'll Need

- A [Raspberry Pi Model B](http://www.adafruit.com/products/998 "Link: http://www.adafruit.com/products/998")&nbsp;
- [Occidentalis v0.2](http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2 "Link: http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2") or higher
- Some sort of external display (We're using a [7" NTSC/PAL TFT Display](http://adafruit.com/products/947))

# Development Tools
This tutorial uses&nbsp;Adafruit's&nbsp;[WebIDE](http://learn.adafruit.com/webide/overview). &nbsp;It's an&nbsp;ideal development environment to work&nbsp;with external displays, since you can display your debug output and keep the shell visible while the display contents are changed on the remote display, and easily upload files (images, fonts, etc.) to the Pi.&nbsp;   
  
You could also work via SSH, but as you'll see later in the tutorial this is less convenient since you'll need at least two sessions, it's more cumbersome to transfer files, and you'll probably find the text editor in the WebIDE more natural to use than vi or nano if you aren't already an experiences Linux user.  
  
If you're not&nbsp;already using WebIDE -- have a look at our easy to follow learning guides below:  

- [Occidentalis v0.2](http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2)
- [Raspberry Pi WebIDE](http://learn.adafruit.com/webide/overview)

- [Next Page](https://learn.adafruit.com/pi-video-output-using-pygame/getting-started.md)

## Featured Products

### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### NTSC/PAL (Television) TFT Display - 3.5" Diagonal

[NTSC/PAL (Television) TFT Display - 3.5" Diagonal](https://www.adafruit.com/product/913)
Yes, this is an adorable small television! The visible display measures only 3.5" (8.9cm) diagonal, the TFT comes with a NTSC/PAL driver board. The display is very easy to use - simply connect 6-12VDC to the red (+) and black (-) wires, then connect a composite video source to the RCA...

In Stock
[Buy Now](https://www.adafruit.com/product/913)
[Related Guides to the Product](https://learn.adafruit.com/products/913/guides)
### NTSC/PAL (Television) TFT Display - 2.0" Diagonal

[NTSC/PAL (Television) TFT Display - 2.0" Diagonal](https://www.adafruit.com/product/911)
Yes, this is an adorable miniature television! The visible display measures only 2" diagonal, the TFT comes with a NTSC/PAL driver board. The display is very easy to use - simply connect 6-12VDC to the red and black wires, then connect a composite video source to the RCA connector. Voila,...

In Stock
[Buy Now](https://www.adafruit.com/product/911)
[Related Guides to the Product](https://learn.adafruit.com/products/911/guides)
### NTSC/PAL (Television) TFT Display - 4.3" Diagonal

[NTSC/PAL (Television) TFT Display - 4.3" Diagonal](https://www.adafruit.com/product/946)
Yes, this is an adorable small television! The visible display measures only 4.3" (11cm) diagonal, the TFT comes with a NTSC/PAL driver board, enclosure and stand. The display is very easy to use - simply connect 12VDC to the 2.1mm center-positive DC jack (or use the cable and connect to...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/946)
[Related Guides to the Product](https://learn.adafruit.com/products/946/guides)
### NTSC/PAL (Television) TFT Display - 7" Diagonal

[NTSC/PAL (Television) TFT Display - 7" Diagonal](https://www.adafruit.com/product/947)
Yes, this is an adorable small television! The visible display measures only 7" (17.8cm) diagonal, the TFT comes with a NTSC/PAL driver board, enclosure and stand. The display is very easy to use - simply connect the included 12VDC adapter to the 2.1mm center-positive DC jack, then...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/947)
[Related Guides to the Product](https://learn.adafruit.com/products/947/guides)
### Raspberry Pi 1 Model B Starter Pack - Includes a Raspberry Pi

[Raspberry Pi 1 Model B Starter Pack - Includes a Raspberry Pi](https://www.adafruit.com/product/1014)
You want to get hacking with your Pi fast, right? Get everything you need to start with the Adafruit Starter Pack for Raspberry Pi. It's the perfect accompaniment to your new Pi, everything you need to boot up your Pi Model B and get going. **We pre-assemble the Cobbler for you, no...**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1014)
[Related Guides to the Product](https://learn.adafruit.com/products/1014/guides)
### NTSC/PAL (Television) TFT Display - 1.5" Diagonal

[NTSC/PAL (Television) TFT Display - 1.5" Diagonal](https://www.adafruit.com/product/910)
Yes, this is an adorable miniature television! The visible display measures only 1.5" diagonal, the TFT comes with a NTSC/PAL driver board. The display is very easy to use - simply connect 6-12VDC to the red and black wires, then connect a composite video source to the RCA connector....

In Stock
[Buy Now](https://www.adafruit.com/product/910)
[Related Guides to the Product](https://learn.adafruit.com/products/910/guides)

## Related Guides

- [Electronic Animated Eyes for ARM Microcontrollers](https://learn.adafruit.com/animated-electronic-eyes.md)
- [CircuitPython Day 2024 Countdown Clock](https://learn.adafruit.com/circuitpython-day-2024-countdown-clock.md)
- [Adafruit RP2350 22-pin FPC HSTX to DVI Adapter](https://learn.adafruit.com/adafruit-rp2350-22-pin-fpc-hstx-to-dvi-adapter.md)
- [Adafruit 3.5" 320x480 Color TFT Touchscreen Breakout](https://learn.adafruit.com/adafruit-3-5-color-320x480-tft-touchscreen-breakout.md)
- [AdaBox 018](https://learn.adafruit.com/adabox018.md)
- [Adafruit's Raspberry Pi Lesson 5. Using a Console Cable](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable.md)
- [Press Your Button for Raspberry Pi](https://learn.adafruit.com/press-your-button-for-raspberry-pi.md)
- [MONSTER M4SK Toon Hat](https://learn.adafruit.com/monster-mask-augmented-eyes-toon-hat.md)
- [Windows IoT Core Application Development: Headed Blinky](https://learn.adafruit.com/windows-iot-application-development-headed-blinky.md)
- [Cappy Monster M4sk with Animated Eyes](https://learn.adafruit.com/cappy-monster-m4sk.md)
- [Running TensorFlow Lite Object Recognition on the Raspberry Pi 4 or Pi 5](https://learn.adafruit.com/running-tensorflow-lite-on-the-raspberry-pi-4.md)
- [Pip-Boy 2040 Wrist-Mounted Prop](https://learn.adafruit.com/pip-boy-2040.md)
- [CustomEyesation: DIY Monster M4SK Graphics](https://learn.adafruit.com/customeyesation-diy-monster-m4sk-graphics.md)
- [Getting Started With Windows IoT Core on Raspberry Pi](https://learn.adafruit.com/getting-started-with-windows-iot-on-raspberry-pi.md)
- [Candy Bucket GIF Player Eyes](https://learn.adafruit.com/candy-bucket-gif-eyes.md)
