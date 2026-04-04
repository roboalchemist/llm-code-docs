# Source: https://learn.adafruit.com/pi-video-output-using-pygame/pygame-drawing-functions.md

# Pi Video Output Using pygame

## Pygame Drawing Functions

Pygame includes a fairly rich collection of drawing objects and functions, making it easy to draw basic shapes, render text, display images, etc. &nbsp;The best way to learn the API is to start exploring it, look at examples on the web, and [read the documentation](http://www.pygame.org/docs/ "Link: http://www.pygame.org/docs/"), but the following sets of functions are probably the most useful if you're just getting started:

- [pygame.draw](http://www.pygame.org/docs/ref/draw.html "Link: http://www.pygame.org/docs/ref/draw.html") (basic drawing primitives)
- [pygame.font](http://www.pygame.org/docs/ref/font.html "Link: http://www.pygame.org/docs/ref/font.html") (text rendering)
- [pygame.image](http://www.pygame.org/docs/ref/image.html) (load and display .gifs, .jpgs, .pngs, etc.)

  
# Drawing a&nbsp;Graticule
As an example, we'll use some basic drawing primitives to render something resembling a graticule on an oscilloscope. &nbsp;Add the following function to your pyscope class (with proper indentation to align with the rest of the class):```
    def drawGraticule(self):
        "Renders an empty graticule"
        # The graticule is divided into 10 columns x 8 rows
        # Each cell is 50x40 pixels large, with 5 subdivisions per
        # cell, meaning 10x8 pixels each.  Subdivision lines are
        # displayed on the central X and Y axis
        # Active area = 10,30 to 510,350 (500x320 pixels)
        borderColor = (255, 255, 255)
        lineColor = (64, 64, 64)
        subDividerColor = (128, 128, 128)
        # Outer border: 2 pixels wide
        pygame.draw.rect(self.screen, borderColor, (8,28,504,324), 2)
        # Horizontal lines (40 pixels apart)
        for i in range(0, 7):
            y = 70+i*40
            pygame.draw.line(self.screen, lineColor, (10, y), (510, y))
        # Vertical lines (50 pixels apart)
        for i in range(0, 9):
            x = 60+i*50
            pygame.draw.line(self.screen, lineColor, (x, 30), (x, 350))
        # Vertical sub-divisions (8 pixels apart)
        for i in range(1, 40):
            y = 30+i*8
            pygame.draw.line(self.screen, subDividerColor, (258, y), (262, y))
        # Horizontal sub-divisions (10 pixels apart)
        for i in range(1, 50):
            x = 10+i*10
            pygame.draw.line(self.screen, subDividerColor, (x, 188), (x, 192))

```

This will draw a 500x320 pixel graticule, with an outer 2 pixel border, and divisions for 10 columns, and 8 rows. &nbsp;You can render the graticule with the following code at the bottom of your class:

```
# Create an instance of the PyScope class
scope = pyscope()
# Add  the graticule
scope.drawGraticule()
# Update the display
pygame.display.update()

# Wait 10 seconds
time.sleep(10)
```

That you give you something similar to the following (you may need to tweek the colors, etc., depending on the display you are using):

![](https://cdn-learn.adafruit.com/assets/assets/000/002/323/medium800/raspberry_pi_graticule.jpg?1396781726)

# Adding Text
Adding text is relatively straight-forward using the [pygame.font](http://www.pygame.org/docs/ref/font.html) functions/objects. &nbsp;If you wish to load specific fonts (you can load fonts from files, etc.) you should consult the documentation, but as a basic example of using the default system font you simply need to entering something similar to the following code:```
# Create an instance of the PyScope class
scope = pyscope()

# Get a refernce to the system font, size 30
font = pygame.font.Font(None, 30)
# Render some white text (pyScope 0.1) onto text_surface
text_surface = font.render('pyScope (%s)' % "0.1", 
True, (255, 255, 255))  # White text
# Blit the text at 10, 0
scope.screen.blit(text_surface, (10, 0))
# Update the display
pygame.display.update()
          
# Wait 10 seconds
time.sleep(10)
```

Info: 

# Adding Images
It's just as easy to add images using the [pygame.image](http://www.pygame.org/docs/ref/image.html "Link: http://www.pygame.org/docs/ref/image.html") functions/objects.  
  
To test this out, upload an image via the WebIDE using the ' **Upload File**' button on the left-hand menu, and upload the following image:![](https://cdn-learn.adafruit.com/assets/assets/000/002/319/medium800/raspberry_pi_adafruit_logo.gif?1396781698)

Select the appropriate image with the popup file dialogue ...

![](https://cdn-learn.adafruit.com/assets/assets/000/002/321/medium800/raspberry_pi_uploadimage.jpg?1396781704)

...&nbsp;and the&nbsp;image should show up in your file explorer with whatever name you gave it:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/320/medium800/raspberry_pi_imagefile.jpg?1396781699)

Now you simply need to reference the local file name with the following code:

```
# Create an instance of the PyScope class
scope = pyscope()

# Render the Adafruit logo at 10,360
logo = pygame.image.load('adafruit_logo.gif').convert()
scope.screen.blit(logo, (10, 10))
pygame.display.update()

# Wait 10 seconds
time.sleep(10)
```

# Wrapping it all Up + Animation
If you need to animate anything, the secret is simply to call 'pygame.display.update()' at the appropriate moment.  
  
An example using all of the above techniques can be seen in the following complete class that you can simply copy and paste into your pyscope.py file:```auto
import os
import pygame
import time
import random

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
                print('Driver: {0} failed.'.format(driver))
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

    def drawGraticule(self):
        "Renders an empty graticule"
        # The graticule is divided into 10 columns x 8 rows
        # Each cell is 50x40 pixels large, with 5 subdivisions per
        # cell, meaning 10x8 pixels each.  Subdivision lines are
        # displayed on the central X and Y axis
        # Active area = 10,30 to 510,350 (500x320 pixels)
        borderColor = (255, 255, 255)
        lineColor = (64, 64, 64)
        subDividerColor = (128, 128, 128)
        # Outer border: 2 pixels wide
        pygame.draw.rect(self.screen, borderColor, (8,28,504,324), 2)
        # Horizontal lines (40 pixels apart)
        for i in range(0, 7):
            y = 70+i*40
            pygame.draw.line(self.screen, lineColor, (10, y), (510, y))
        # Vertical lines (50 pixels apart)
        for i in range(0, 9):
            x = 60+i*50
            pygame.draw.line(self.screen, lineColor, (x, 30), (x, 350))
        # Vertical sub-divisions (8 pixels apart)
        for i in range(1, 40):
            y = 30+i*8
            pygame.draw.line(self.screen, subDividerColor, (258, y), (262, y))
        # Horizontal sub-divisions (10 pixels apart)
        for i in range(1, 50):
            x = 10+i*10
            pygame.draw.line(self.screen, subDividerColor, (x, 188), (x, 192))

    def test(self):
        "Test method to make sure the display is configured correctly"
        adcColor = (255, 255, 0)  # Yellow
        self.drawGraticule()
        # Render the Adafruit logo at 10,360
        logo = pygame.image.load('adafruit_logo.gif').convert()
        self.screen.blit(logo, (10, 335))
        # Get a font and use it render some text on a Surface.
        font = pygame.font.Font(None, 30)
        text_surface = font.render('pyScope (%s)' % "0.1",
            True, (255, 255, 255))  # White text
        # Blit the text at 10, 0
        self.screen.blit(text_surface, (10, 0))
        # Render some text with a background color
        text_surface = font.render('Channel 0',
            True, (0, 0, 0), (255, 255, 0)) # Black text with yellow BG
        # Blit the text
        self.screen.blit(text_surface, (540, 30))
        # Update the display
        pygame.display.update()
        # Random adc data
        yLast = 260
        for x in range(10, 509):
            y = random.randrange(30, 350, 2) # Even number from 30 to 350
            pygame.draw.line(self.screen, adcColor, (x, yLast), (x+1, y))
            yLast = y
            pygame.display.update()

# Create an instance of the PyScope class
scope = pyscope()
scope.test()
# Wait 10 seconds
time.sleep(10)
```

This should give you something similar to the following (depending on your display):

http://www.youtube.com/watch?v=Yj0gxhUTqbw&feature=youtu.be

- [Previous Page](https://learn.adafruit.com/pi-video-output-using-pygame/drawing-basics.md)

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
