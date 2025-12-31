# Source: https://learn.sparkfun.com/tutorials/lumidrive-hookup-guide

## Introduction

[LumiDrive](https://www.sparkfun.com/products/14779) is SparkFun\'s foray into all things Python on microcontrollers. Leveraging Adafruit\'s Circuit Python, we have created a product made for driving a strand of [APA102\'s](https://www.sparkfun.com/products/14015). We\'ve broken out a few analog and digital pins from the onboard SAMD21G-AU microcontroller so that you can implement external buttons, switches, and other whizzbangs to interact with the [LED](https://www.sparkfun.com/leds)s.

[![SparkFun LumiDrive LED Driver](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/0/3/0/14779-SparkFun_LumiDrive_LED_Driver-01.jpg)](https://www.sparkfun.com/sparkfun-lumidrive-led-driver.html)

### [SparkFun LumiDrive LED Driver](https://www.sparkfun.com/sparkfun-lumidrive-led-driver.html) 

[ DEV-14779 ]

With the SparkFun LumiDrive you will be able to control and personalize a whole strand of APA102s directly from the board its...

[ [\$25.50] ]

### Circuit Python

You can read the extensive documentation about Circuit Python [here](https://learn.adafruit.com/welcome-to-circuitpython/overview) on Adafruit\'s website, but let\'s review a short and sweet version. Circuit Python is Adafruit\'s version of [MicroPython](https://micropython.org/). What pray tell, is MicroPython? MicroPython is Python 3 for microcontrollers. MicroPython takes the power of the wildly popular Python [interpreted](https://en.wikipedia.org/wiki/Interpreted_language) language that is easy to use, easy to read, and powerful and makes it usable for microcontrollers. It feels familiar in the way you declare and use pins but unlike Arduino, you don\'t have to compile or upload your code. This is because your microcontroller acts like a USB drive when you plug it into your computer. The code simply lives as a file that you modify directly and when it\'s saved, it is automatically loaded. Algebraic! It\'s also compatible with the Python 3 you have on your computer so that you can develop seamlessly on your desktop! Why are we using Circuit Python? Circuit Python has the advantage of having many libraries built in by default that are catered toward entry-level hobbyists. In the case of the LumiDrive, we\'ll be utilizing the DotStar library, Adafruit\'s library for APA102 LEDs.

### Required Materials:

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![LED RGB Strip - Addressable, 1m (APA102)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/0/8/14015-01.jpg)](https://www.sparkfun.com/led-rgb-strip-addressable-1m-apa102.html)

### [LED RGB Strip - Addressable, 1m (APA102)](https://www.sparkfun.com/led-rgb-strip-addressable-1m-apa102.html) 

[ COM-14015 ]

These are addressable 1-meter-long 5V RGB LED strips that come packed with 60 APA102Cs. APA102 LEDs are very similar to WS281...

[\$17.50] [ [\$10.95] ]

We have many portable options to power your LEDs:

[![Lithium Ion Battery - 2Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/2/13855-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-2ah.html)

### [Lithium Ion Battery - 2Ah](https://www.sparkfun.com/lithium-ion-battery-2ah.html) 

[ PRT-13855 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 200...

[ [\$19.41] ]

[![Lithium Ion Battery - 6Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/3/13856-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-6ah.html)

### [Lithium Ion Battery - 6Ah](https://www.sparkfun.com/lithium-ion-battery-6ah.html) 

[ PRT-13856 ]

If you need some juice, this 6Ah Lithium Ion Battery is for you. These are very compact batteries based on Lithium Ion chemis...

[ [\$48.44] ]

[![Lithium Ion Battery - 1Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/0/1/13813-01.jpg)](https://www.sparkfun.com/products/13813)

### [Lithium Ion Battery - 1Ah](https://www.sparkfun.com/products/13813) 

[ PRT-13813 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1000 mAh!

**Retired**

I found this connector to be very helpful because it kept me from plugging and unplugging different strands of APA102\'s directly into the poke-home connectors.

[![LED Strip Pigtail Connector (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/2/1/14576-LED_Pigtail_connector_4_Pin_-01.jpg)](https://www.sparkfun.com/led-strip-pigtail-connector-4-pin.html)

### [LED Strip Pigtail Connector (4-pin)](https://www.sparkfun.com/led-strip-pigtail-connector-4-pin.html) 

[ CAB-14576 ]

These 4-pin JST-SM pigtail connectors mate perfectly with LED strips and other applications that require only two lines and a...

[ [\$1.95] ]

### Suggested Reading

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

[](https://learn.sparkfun.com/tutorials/mean-well-led-switching-power-supply-hookup-guide)

### Mean Well LED Switching Power Supply Hookup Guide 

In this tutorial, we will be connecting a Mean Well LED switching power supply to an addressable LED strip controlled by an Arduino.

[](https://learn.sparkfun.com/tutorials/lumini-ring-hookup-guide)

### LuMini Ring Hookup Guide 

The LuMini Rings (APA102-2020) are the highest resolution LED rings available.

## Hardware Overview

### Power

There are three options for power on the product: USB-C, Lithium Ion Battery, or Input. You can provide power in the range from **3.3V-6V**.

[![This picture highlights the power input of the board that includes the USB-C connector, Lipo Connector, and two pin header just next to the lipo connector.](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/Power_Input_Labelled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/Power_Input_Labelled.jpg)

#### USB-C

USB-C, aside from being reversible which is already awesome, has the capability of supplying more power than its predecessor. I was able to pull 2 AMPs from my computer on a 3.1 USB plug. Be cautious - I did this so that you don\'t have to! Every computer is different and I strongly advise that you don\'t do something so rash unless you are absolutely confident. Also keep in mind that different USB ports (2.0, 3.0, and 3.1) supply different levels of power. 3.1 is easy to identify because it has a blue tongue when you look into the port.

#### Lithium Ion Battery

We have many options in our catalog that will suit your various portable power needs. LumiDrive also comes with a charging circuit so you can charge your LiPo battery.

[![LiPo Battery Plugged in as well as USB-C Power](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/5/LiPoBattery.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/LiPoBattery.jpg)

#### Two Pin Input Headers

Last but not least is a 2 pin header labeled `INPUT` where you can supply your own power.

#### Current Draw

The table below lists the current draw for a strand of 55 LEDs at **full white** at half and full brightness. I\'ve also included current draw for the various included functions at varying LED amounts and brightness to help you make more educated decisions when purchasing or using your LEDs.

[] **Please Note:** The chart below was written for APA102 1m LED strip with the 5050 LEDs - if you are using any of the APA102 line with 2020s we do **not** recommend running at full brightness. We\'ve found that setting the global brightness to 32 is good for testing; turning the brightness up all the way and leaving all LED\'s on white will result in damage to your LEDs!

  \# of LEDs (Half Brightness)      Current Consumption (Amps)
  --------------------------------- ----------------------------
  1                                 0.070
  2                                 0.095
  3                                 0.120
  5                                 0.139
  10                                0.289
  20                                0.536
  30                                0.755
  35                                0.883
  40                                1.102
  50                                1.311
  \# of LEDs (Full Brightness)      Current Consumption (Amps)
  10                                0.520
  15                                0.737
  25                                1.328
  27                                1.426
  29                                1.523
  31                                1.618
  40                                2.018
  Function at 55 LEDs               Current Consumption (Amps)
  Slice Rainbow (0.25 Brightness)   0.336
  Slice Rainbow (0.50 Brightness)   0.600
  Rainbow Cycle (0.25 Brightness)   0.281
  Rainbow Cycle (0.50 Brightness)   0.500
                                    
  Function at 85 LEDs               Current Consumption (Amps)
  Slice Rainbow (0.25 Brightness)   0.500
  Slice Rainbow (0.50 Brightness)   0.890
  Rainbow Cycle (0.25 Brightness)   0.425
  Rainbow Cycle (0.50 Brightness)   0.727

### Input Output

There are four input/output pins broken out to the side of the product. There are two digital pins and two analog pins. These can be used to interact with your LED strand (or not) by attaching buttons, switches, light sensors, etc.

[![This picture shows the top side of the product with the usb-c connector facing up, highlighting the four lowest plated through holes as input and output pins.](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/DIgital_Analog_Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/DIgital_Analog_Pins.jpg)

### Buttons

There are two buttons on the product. The top button is a reset button which will reset the board on press. The second is a button attached to digital pin D6. You can use this in place of attaching a button to the board.

[![This picture shows the topside of the product with the USB-C connector facing up, and highlights the two buttons on the left side. The top being reset and the other D6.](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/Buttons.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/Buttons.jpg)

### LEDs

There are two LEDs on board. The top LED in the picture is a yellow charge LED that indicates that a LiPo battery is being charged. The second is a blue stat LED attached to pin D13.

[![This picture shows the topside of the product with the USB-C connector facing up, and highlights the two LEDs on the right side, one labeled Charge and the other LED.](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/LEDs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/LEDs.jpg)

### Poke-home Connectors

There are two Poke-home connectors at the bottom of the product.

[![This picture shows the topside of the product with the USB-C connector facing up, and highlights the two large side by side Poke-home connectors that allow for easily connecting of wires without soldering.](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/PokeHome_Connectors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/PokeHome_Connectors.jpg)

They are versatile and rather robust and allow you to plug in wire without the need for solder. They\'re labeled with the color of wire that is used in the strands of APA102 LEDs that we sell here at SparkFun but are not limited to just those. Just below that silk you\'ll notice the function of those lines are labeled as in the following chart.

  Pin      Description
  -------- --------------
  RED      VCC (3.3-5V)
  BLU      Clock
  GRN      Data
  YELLOW   Ground

## Hardware Assembly

**Note:** You can also use a ball point pen instead of a tweezer to push down on the poke-home connector.

Hardware assembly is straight forward. Let\'s start by plugging your LED strand into the poke-home connectors. Finer control can be achieved by using a pair of tweezers or the tip of a pen to press in the flap on the topside of the poke-home connector. Here we\'ve opted for tweezers since that\'s what we had handy.

[![Inserting the wire into the poke home clamp with the black flap pressed down by tweezers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/5/Poke-home_clamp.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/Poke-home_clamp.jpg)

When you press onto the black flap on the top of the poke-home connector, two metal wedges move laterally - to the sides of the product- inside the connector. Push your wire into the poke-home connector. When you release it, the two wedges will clamp down onto the wire. Give them a slight tug to make sure the wires are in there solid. You\'re ready to rock!

[![Wire inserted into poke home clamp and black flap no longer depressed](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/5/Poke-home_push.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/Poke-home_push.jpg)

Plug your LumiDrive into your computer with the USB-C connector. It should pop up automatically as a hard drive called **CIRCUITPY**. If it doesn\'t pop up automatically, unplug it and plug it back in. If that doesn\'t work, navigate to your files folder and look for ***CIRCUITPY*** on the left hand side and give it a click. At this point the blue stat LED on the LumiDrive should be blinking. From here you can open up that **CIRCUITPY** by clicking on it.

[![Drag and drop folder view](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/5/Main.py_Drag_and_Drop.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/Main.py_Drag_and_Drop.JPG)

*Having a hard time seeing? Click the image for a closer look.*

[] **Note!** You may or may not be wondering what all these files are on the CIRCUITPY drive? I have hidden files turned on on my computer. Files with preceding periods i.e. \".Trashes\" or \".metadata_never_index\" are necessary for MAC users. The boot_out.txt file tells you what version of Circuit Python is loaded onto your LumiDrive. Finally \"Main.py\" is where all the fun happens.

Let\'s move onto the example code.

## Python Example Code

Your LumiDrive should already come with the following Python code but in case something happens to it, than you can re-download the example code here:

[LumiDrive Main.py Example Code](https://github.com/sparkfun/SparkFun_LumiDrive_Example_Code)

**Heads up!** You can also upload Arduino code to the LumiDrive using the Arduino IDE. Just select **SparkFun SAMD21 Dev Breakout Board** under the board menu. If you don\'t have the SparkFun SAMD21 board definitions then check our [hookup guide](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/setting-up-arduino) for detailed instructions and [drivers (if you need them)](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/drivers-if-you-need-them).\
\
If you do want to go the Arduino route, you\'ll need to install the FastLED library. See our [LuMini Ring Hookup Guide](https://learn.sparkfun.com/tutorials/lumini-ring-hookup-guide#software-installation) for installation details and example code.\
\

[] Please note that once you upload Arduino code, you\'ll lose your Circuity Python Firmware. Don\'t panic! Just double tap the reset button on your LumiDrive and the board will pop up as **LUMIBOOT**. Now you can drag and drop the firmware below and voila!\
\

[Download LumiDrive Default Firmware (ZIP)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/lumidrive_firmware.zip)

Before we begin, let\'s talk about the options for loading and updating this code on your LumiDrive. One option is to move the file *main.py* onto your desktop and edit it with a [text editor](https://en.wikipedia.org/wiki/List_of_text_editors). When you\'re done with it, you can simply drag and drop it back into the **CIRCUITPY** drive. Circuit Python will recognize the change and automatically load the new code. The other option is to edit the file directly in the **CIRCUITPY** drive. This option is much more convenient and efficient, but requires a text editor that writes the file completely when it\'s saved. On Windows not all text editors exhibit the necessary behavior. Below is a list of good, not great, and not recommended text editors for editing files directly on LumiDrive (or any Circuit Python board). If you\'re using a Mac then you won\'t be running into any of these issues.

  GOOD                 GOOD only with ADD-ONS   NOT Recommended
  -------------------- ------------------------ -------------------
  MU                   PYCharm IDE              Notepad/Notepad++
  VIM                  Atom                     IDLE
  EMACS                Slick Edit               Nano
  Sublime Text                                  
  Visual Studio Code                            

My suggestion would be to use [MU](https://codewith.mu/) or [Sublime Text](https://www.sublimetext.com/). The first is more beginner friendly while the second is more light weight with some really nice features. If you\'re already familiar with VIM, EMACS, or Visual Studio Code then use those instead.

If you\'re attached to one of the *not recommended* editors then there is a way to get it to work. After you\'ve made changes to the main.py, if you eject the **CIRCUITPY** drive then it will force Windows to write the saves that you made.

Let\'s quickly talk about which files Circuit Python monitors for saves. Circuit Python looks for the following four files in this order and runs the first one it finds: **code.txt**, **code.py**, **main.txt**, and **main.py**. That\'s all of it, now onto the code.

At the top of the code we have a number of libraries that are necessary for our code.

    language:python
    import adafruit_dotstar # Our LED library
    import digitalio
    import board
    import math
    import time

Here\'s where you can start to modify the code to your particular LED strip. The `num_pixels` variable should reflect how many LEDs you have and `brightness` controls the brightness. We have 60 pixels in the example because it reflects the number of LEDs of our [1m length of APA102s](https://www.sparkfun.com/products/14015). Keep in mind as you set these that if you\'re powering through your computer, don\'t add too many too quickly. Otherwise you could potentially harm your computer. Below our two variables we create an instance of our library called pixels, and just below that we have some pre-defined colors.

    language:python
    # These two variables should be adjusted to reflect the number of LEDs you have
    # and how bright you want them.
    num_pixels = 60 
    brightness = 0.25

    # This creates the instance of the DoTStar library. 
    pixels = adafruit_dotstar.DotStar(board.SCK, board.MOSI, 
        num_pixels, brightness=brightness, auto_write=False)

    # Some standard colors. 
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 150, 0)
    ORANGE = (255, 40, 0)
    GREEN = (0, 255, 0)
    TEAL = (0, 255, 120)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (180, 0, 255)
    MAGENTA = (255, 0, 20)
    WHITE = (255, 255, 255)

    # A list of the ten colors. Use this if you want to cycle through the colors. 
    colorList = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA,
                        WHITE]

We have a number of functions to handle different LED behaviors. Each function has a little explanation commented just above it\'s definition.

    language:python
    # The travel function takes a color and the time between updating the color. It
    # will start at LED one on the strand and fill it with the give color until it
    # reaches the maximum number of pixels that are defined as "num_pixels".
    def travel(color, wait):
        num_pixels = len(pixels)
        for pos in range(num_pixels):
            pixels[pos] = color 
            pixels.show() 
            time.sleep(wait)

    # The travel_back function like the travel function takes a color and the time between 
    # updating the color. However it unlike the travel function, it will start at
    # the last LED and works its way to LED. Fill the LED with the given color.
    def travel_back(color, wait):
        num_pixels = len(pixels)
        for pos in range(num_pixels, 0, -1):
            pixels[pos] = color 
            pixels.show() 
            time.sleep(wait)

    # This function may give you an idea of other functions to create. Here we're
    # starting with green LEDs and then slowing filling the red color until we have
    # a yellow color.  
    def green_yellow_wheel(wait):
        for redColor in range(255):
            color = (redColor, 150, 0)
            pixels.fill(color)
            pixels.show()
            time.sleep(wait)

    # You can use this function to get a custom color value. 
    # value much in the form of a tuple, like the colors above. 
    def wheel(pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            return (0, 0, 0)
        if pos < 85:
            return (255 - pos * 3, pos * 3, 0)
        if pos < 170:
            pos -= 85
            return (0, 255 - pos * 3, pos * 3)
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

    # This function takes a color and a dely and fills the entire strand with that color. 
    # The delay is given in the case you use multiple color fills in a row.  
    def color_fill(color, wait):
        pixels.fill(color)
        pixels.show()
        time.sleep(wait)

    # Fills the strand with two alternating colors and cycles through the 10 colors 
    def slice_alternating(wait):

        num_pixels = len(pixels)

        pixels[::2] = [RED] * (num_pixels // 2)
        pixels.show()
        time.sleep(wait)
        pixels[1::2] = [ORANGE] * (num_pixels // 2)
        pixels.show()
        time.sleep(wait)
        pixels[::2] = [YELLOW] * (num_pixels // 2)
        pixels.show()
        time.sleep(wait)
        pixels[1::2] = [GREEN] * (num_pixels // 2)
        pixels.show()
        time.sleep(wait)
        pixels[::2] = [TEAL] * (num_pixels // 2)
        pixels.show()
        time.sleep(wait)
        pixels[1::2] = [CYAN] * (num_pixels // 2)
        pixels.show()
        time.sleep(wait)
        pixels[::2] = [BLUE] * (num_pixels // 2)
        pixels.show()
        time.sleep(wait)
        pixels[1::2] = [PURPLE] * (num_pixels // 2)
        pixels.show()
        time.sleep(wait)
        pixels[::2] = [MAGENTA] * (num_pixels // 2)
        pixels.show()
        time.sleep(wait)
        pixels[1::2] = [WHITE] * (num_pixels // 2)
        pixels.show()
        time.sleep(wait)

    # This function divides the given number of pixels and fills them as evenly as
    # possible with a rainbow pattern (RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE) 
    # which repeats every 6 LEDs.
    def slice_rainbow(wait):

        num_pixels = len(pixels)

        pixels[::6] = [RED] * math.ceil(num_pixels / 6)
        pixels.show()
        time.sleep(wait)
        pixels[1::6] = [ORANGE] * math.ceil((num_pixels - 1) / 6)
        pixels.show()
        time.sleep(wait)
        pixels[2::6] = [YELLOW] * math.ceil((num_pixels -2) / 6)
        pixels.show()
        time.sleep(wait)
        pixels[3::6] = [GREEN] * math.ceil((num_pixels-3) / 6)
        pixels.show()
        time.sleep(wait)
        pixels[4::6] = [BLUE] * math.ceil((num_pixels-4) / 6)
        pixels.show()
        time.sleep(wait)
        pixels[5::6] = [PURPLE] * math.ceil((num_pixels-5) / 6)
        pixels.show()
        time.sleep(wait)

    # This function makes a strand of LEDs look like a rainbow flag that travels
    # along the length of the strand. It is not infinitely contniuous and will stop
    # after any single LED has cycled through every color.  
    def rainbow_cycle(wait):
        num_pixels = len(pixels)
        for j in range(255):
            for i in range(num_pixels):
                rc_index = (i * 256 // num_pixels) + j
                pixels[i] = wheel(rc_index & 255)
            pixels.show()
            time.sleep(wait)

    print("Clearing LEDs.")
    color_fill(BLACK,0) 

Finally we have a while loop that is akin to `void loop` in Arduino. Right now we have the loop blinking our blue D13 stat LED.

    language:python
    #Ah trusty ol' blink. 
    while True: 
        led.value = True
        time.sleep(.5)
        led.value = False
        time.sleep(.5)

Instead, let\'s pick some functions from the functions above and type them in. I chose the following and gave the function its\' necessary parameter: a delay time.

    language:python
    while True: 
        rainbow_cycle(0)

After you\'ve modified the code, just hit save (assuming you have the correct text editor for saving directly on LumiDrive) and the code will automatically run. If all is well you should see the following:

[![LED strand example in the dark](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/5/Strand_dark.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/Strand_dark.jpg)

Algebraic!

Using the [3 inch LuMini ring](https://www.sparkfun.com/products/14965), and a couple other functions.

[] **Reminder:** This example sets the brightness at 25. If you are using any of the APA102 line with 2020s we do **not** recommend running at full brightness. Turning the brightness up all the way and leaving all LED\'s on white will result in damage to your LEDs!

[![LumiDrive Demo with Lumini Ring](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/LumiDrive_Demo.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/LumiDrive_Demo.gif)

[] **Heads up!** Updating the APA102s gets slower the longer the strand or the amount of LEDs you\'re driving. This is just the nature of working in Python instead of C. There\'s also some [known efficiency issues](https://github.com/adafruit/circuitpython/issues/884) with the DotStar library.

## Read-Evaluate-Print-Loop (REPL)

A note about the Read-Evaluate-Print-Loop, or the REPL. It\'s a language shell that allows you to interact with the LumiDrive in an Interactive Python environment. If you pull up your favorite [serial program](https://learn.sparkfun.com/tutorials/terminal-basics) and open it to the COM port of the LumiDrive you should see the following.

[![Terminal Window showing REPL](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/5/REPL.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/REPL.JPG)

*Having a hard time seeing? Click the image for a closer look.*

Main.py will be running an infinite blink loop fresh out of the box. Simply press **CTRL-C** to interrupt the code. Here you have an interactive python environment to play around in.! Here we can do some fun things like Math!

[![Terminal window showing math example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/5/REPL_MATH.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/REPL_MATH.JPG)

*Having a hard time seeing? Click the image for a closer look.*

More importantly we can see what libraries and pins are available to us in the version of Circuit Python that is loaded on your LumiDrive, using the `help(modules)` and `dir(board)` commands respectively.

[![Terminal window showing help modules and dir(board)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/5/REPL_USEFUL.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/5/REPL_USEFUL.JPG)

*Having a hard time seeing? Click the image for a closer look.*

If you look at the line that says `dir(board)`, just below are various pins that are available in Circuit Python but not all of them are physically broken out on the board. When you\'re done messing around in REPL and ready to run the code that is on your LumiDrive, you can press **CTRL-D** and that will initiate a soft reboot.