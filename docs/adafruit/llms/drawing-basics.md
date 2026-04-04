# Source: https://learn.adafruit.com/pi-video-output-using-pygame/drawing-basics.md

# Pi Video Output Using pygame

## Drawing Basics

# The Screen Object
While the pygame API and documentation is quite clear (see the [pygame.draw](http://www.pygame.org/docs/ref/draw.html "Link: http://www.pygame.org/docs/ref/draw.html")&nbsp;documentation, for example), most of the pygame drawing operations take place on a **screen** , which is rendered on a specific [display](http://www.pygame.org/docs/ref/display.html "Link: http://www.pygame.org/docs/ref/display.html").  
  
The way that the code we entered in the previous page works is it initializes the display in the **\_\_init\_\_** function, and it then allows us to access a field named ' **screen**', where all of the actual drawing and graphics work is done in pygame (you pass a reference to this screen to most drawing functions).  
  
You can see how this works by looking at the 'test' function we added and called:```
# Fill the screen with red (255, 0, 0)
red = (255, 0, 0)
self.screen.fill(red)
# Update the display
pygame.display.update()
```

This code references the 'screen' provided in the class (self.screen since we're referencing it from inside the class), and calls the fill method. &nbsp;Once we are done all of our drawing, we tell pygame to update the entire display to take into account these changes, which is done with:

```
pygame.display.update()
```

This is actually an important point about pygame:

Info: 

This is both an intentional and an intelligent choice. &nbsp;By doing all of your drawing code at once,and only updating the screen when the drawing is complete, you can benefit from something called double-buffering, which makes all of your drawing appear instant, rather than seeing controls get rendered one at a time in a sequential, sluggish-feeling way.

# Accessing the Screen
Since we made a wrapper class called pyscope which takes care of the low-level framebuffer initialisation, etc., how do you access the screen object from outside the class? &nbsp;It's easy ... any time you want to do any drawing, you just need to access the screen as follows:```
# Create an instance of the PyScope class
scope = pyscope()
# Fill the screen with yellow
scope.screen.fill((255, 255, 0))
# Update the display
pygame.display.update()

# Wait 10 seconds
time.sleep(10)
```

You can test this out by placing it at the bottom of your file with no indents, and you should see a yellow screen for ten seconds when you run it.

- [Previous Page](https://learn.adafruit.com/pi-video-output-using-pygame/pointing-pygame-to-the-framebuffer.md)
- [Next Page](https://learn.adafruit.com/pi-video-output-using-pygame/pygame-drawing-functions.md)

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
