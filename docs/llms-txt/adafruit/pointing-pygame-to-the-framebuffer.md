# Source: https://learn.adafruit.com/pi-video-output-using-pygame/pointing-pygame-to-the-framebuffer.md

# Pi Video Output Using pygame

## Pointing Pygame to the Framebuffer

To render any sort of graphics from the console, we first need to point pygame to the underlying framebuffer used by Linux. &nbsp;This is probably the most error-prone operation, but the following code should handle this gracefully and report any errors if something does go wrong.  
  
Enter the following code into your new project, and save the file via the 'Save' button in the top-menu, or just enter CTRL+S:

```auto
import os
import pygame
import time

class pyscope:
    screen = None;

    def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679

        # Allow running from ssh
        os.putenv("DISPLAY", ":0")

        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print("I'm running under X display = {0}".format(disp_no))

        # Check which frame buffer drivers are available
        # Start with fbcon since directfb hangs with composite output
        drivers = ['x11', 'fbcon', 'directfb', 'svgalib']
        found = False
        for driver in drivers:
            # Make sure that SDL_VIDEODRIVER is set
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print("Driver: {0} failed.".format(driver))
                continue
            found = True
            break

        if not found:
            raise Exception('No suitable video driver found!')

        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print("Framebuffer size: %d x %d" % (size[0], size[1]))
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0, 0, 0))
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

    def test(self):
        # Fill the screen with red (255, 0, 0)
        red = (255, 0, 0)
        self.screen.fill(red)
        # Update the display
        pygame.display.update()

# Create an instance of the PyScope class
scope = pyscope()
scope.test()
time.sleep(10)
```

# Huh ... What is all this?
Don't worry if you don't understand every little bit of the code above. &nbsp;We've provided the code in a way that you simply need to create a new instance of the 'pyscope' class, and the low-level framebuffer implementation should be taken care of. &nbsp;How do you know it works? &nbsp;Let's try it out!  
  
There are three lines of code at the bottom that are important:```
# Create an instance of the PyScope class
scope = pyscope()
scope.test()
time.sleep(10)
```

The first line (after the comment) instantiates a new pyscope object named scope. &nbsp;As soon as this line is executed, the framebuffer will be configured, or any eventual error messages will be displayed if there were any problems.  
  
The second line simply calls a function named 'test' that is in the example code we entered earlier. &nbsp;This will simply fill the screen with the color red.  
  
The third line causes the program to sleep for 10 seconds before exiting. &nbsp;This is provided simply to give us a brief delay before the display returns to the shell, restoring whatever was displayed before this program was run.

# How Do I Run It?
If you've already run off and clicked the 'Run' button, you might have noticed the following error:![](https://cdn-learn.adafruit.com/assets/assets/000/002/317/medium800/raspberry_pi_WebIDERunError.jpg?1396781689)

You get this error because the application tries to access the framebuffer using first fbcon, then directfb if that fails and finally svgalib. &nbsp;They all fail for one important reason:

Warning: You may need root access to modify the framebuffer!

Future versions of the WebIDE will add the ability to run as root, but if you're running an older version that doesn't already include this functionality, there's an easy workaround. &nbsp;To give your program access to the framebuffer, simple click the Terminal icon at the top of the text editor, and from the shell that pops up enter:

```
sudo python pyscope.py
```

If all goes well, you should see something like the following in your terminal window:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/318/medium800/raspberry_pi_WebIDERun_good.jpg?1396781691)

And during 10 seconds, your display should look something like this:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/322/medium800/raspberry_pi__MG_0461.jpg?1396781717)

- [Previous Page](https://learn.adafruit.com/pi-video-output-using-pygame/getting-started.md)
- [Next Page](https://learn.adafruit.com/pi-video-output-using-pygame/drawing-basics.md)

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
