# Source: https://learn.sparkfun.com/tutorials/building-large-led-installations

## Introduction 

While designing the layout for the new [SparkFun Emporium](http://blogs.denverpost.com/tech/2015/06/19/sparkfun-to-open-first-offline-store-host-driver-less-vehicle-race/17649/), I was given the opportunity to design a large LED art installation. I\'ve helped build LED installations [before](https://www.sparkfun.com/news/1561), but had never had the opportunity to design one from the ground up. Thus was born the *CandyBar*, a 46-foot LED bar consisting of 8 meters of addressable LED strips (480 LEDs total), all controlled via a [FadeCandy](https://www.sparkfun.com/products/12821) connected to a Raspberry Pi running the [FadeCandy server](https://github.com/scanlime/fadecandy/tree/master/server).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/1/Sales_Space_LED_Project_copy.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/1/Sales_Space_LED_Project_copy.jpg)

### Covered in this Tutorial

Controlling LEDs is one of the most fundamental tasks in embedded electronics, and it\'s often the \"Hello World\" for many beginners starting out on a new platform. However, LED-based projects add up quickly and can become complex very fast. This tutorial is intended to be a guideline for helping you design and build your own large-scale LED installation, while sharing some of the lessons learned from this build.

We\'ll go over the planning stage, pointing out considerations that will need to be taken as you design. This section will cover how you plan to control the LEDs, as well as power considerations. Next, we\'ll cover the build process. This section will cover how to build in stages for large projects, and how to make your installation transportable if need be. Last, we\'ll show the installation process and discuss the next steps to make your installation interactive.

### Materials Used

Here is a list of all the SparkFun parts used in this project.

Other parts used in this build include:

- [24V/250W Power Supply](http://www.mouser.com/ProductDetail/Mean-Well/SE-350-24/?qs=erfQA2AIGbWwfIN%2FyOBPyQ%3D%3D)
- [OctoController and Dual Driver PCBs](http://danjuliodesigns.com/projects/projects/isolated_driver_assets/hw_rev_2.zip) - Custom PCBs designed for LED installations (more info on these below).
- [OctoController parts](https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=e56103a576)
- [DualDriver parts](https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=548f365de5)
- [Coilcraft Inductor](http://www.coilcraft.com/forms/files/en/forms/sample_cart.cfm?action=request_sample&part_number=SER2915L-153KL&CFID=19931143&CFTOKEN=dc0801d000dbd44b-47E7C654-1016-FC16-794AF581B9D1F04D&jsessionid=8430b1e8a2dba07977be2235768239656832#) for each DualDriver board.
- Ethernet cables of varying length. I used a [3ft. cable](https://www.sparkfun.com/products/8915) from SparkFun, and [15ft.](https://www.amazon.com/gp/product/B00EUHRLF6/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1), [25ft.](https://www.amazon.com/gp/product/B001W28L2Y/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1), and [50ft.](https://www.amazon.com/gp/product/B001W26TIW/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1) cables from Amazon.

No two installations will ever be exactly the same. This list is just here for reference and suggestions. Your vision and budget may vary, resulting in certain parts being added or omitted.

### Suggested Reading

The [FadeCandy GitHub](https://github.com/scanlime/fadecandy) is definitely the place to start if you\'ve opted to use the FadeCandy in your project. There are tons and tons of examples showing how to control it through various means, from C++ and Python code to [Processing](https://processing.org/).

A lot was learned from my friend Dan Julio, who built a very impressive LED installation, [Luminescence](http://danjuliodesigns.com/personal/personal/personal/luminescence.html), for [The Dairy Center](https://tickets.thedairy.org/Online/default.asp) in Boulder, CO. His controller and driver PCBs were used in this design to ensure the installation would be robust and last as long as the space it\'s housed within. More information about these boards can be found on [his website](http://danjuliodesigns.com/projects/projects/isolated_driver.html).

This [FadeCandy LED Curtain tutorial](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy/overview) written by Phillip Burgess was also very helpful. Learning how to set up the FadeCandy Server with multiple FadeCandy devices or with an irregular number of LEDs requires altering the configuration file for the server. This tutorial helps clarify how to setup said configuration as well as offering lots of other great tips.

If you need to brush up on some more basic concepts, here are some that pertain to this tutorial.

- [Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) & [Electric Power](https://learn.sparkfun.com/tutorials/electric-power) - Together, these tutorials teach you how to calculate all the necessary power requirements your LEDs will require.
- [LED Basics](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds) - Learn about the finer details pertaining to light-emitting diodes.
- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) - There\'s lots to solder in any installation.
- [Working with Wire](https://learn.sparkfun.com/tutorials/working-with-wire) - Being a pro at wire splicing and soldering will make the build process much easier.
- [Getting Started with Raspberry Pi](https://learn.sparkfun.com/tutorials/setting-up-raspbian-and-doom) - If you\'ve never worked with the Pi or similar Single Board Computer before, you may want to check this out.

## Planning and Design Phase

The planning and design phase is by far the most important. A well-planned project usually results in an easier build process and execution. Here are some of the considerations you\'ll need to make as you plan out your installation:

### Addressable or Non-Addressable LEDs

This should be one of the first things you nail down. Led strips typically come in two flavors: addressable or non-addressable. Addressable LED strips, such as [this one](https://www.sparkfun.com/products/12025), are usually the go-to for many art installations. Each individual LED on the strip can be controlled independently of one another via a small microcontroller attached to each LED. Any installation you\'ve seen that is displaying images or patterns is most likely using addressable LEDs. The project covered in this guide uses addressable LEDs.

In contrast, there are [non-addressable LED strips](https://www.sparkfun.com/products/12021). These strips are generally cheaper, but they offer much less control. The entire strip can either be on or off, there is no individual LED control, and the entire strip can only be one color at a time. For installations that don\'t require the display of many different colors at once, this may be a better option. You could also use a number of these strips and control each strip independently, which would still give you many colors in one area.

Before diving in to the build, it\'s a good idea to test each strip individually to avoid complicated troubleshooting down the road. Also worth noting is that these strips can come in different densities, as in amount of LEDs per strip. Be aware of whether you\'re using strips with 60 LEDs per meter versus 64 LEDs per meter. This will come into play later on.

### Controlling the LEDs and Hardware Limitations

**Limitation on AVR-based Microcontrollers :** If you are just using an AVR-based microcontroller for large LED installations, there is a limitation with the number of WS2812s LEDs used. This is dependent on the microcontroller\'s memory and the size of the program. For an ATmega328P-based microcontroller (i.e. RedBoard Programmed with Arduino, Arduino Uno, Arduino Pro Mini, etc.), it can be up to \~300-400 LEDs. Check out Katerborg\'s note about using WS2812\'s with different Arduinos:\
\

[Katerborg: Powering Lots of LEDs from Arduino](http://www.eerkmans.nl/powering-lots-of-leds-from-arduino/)

\
If you want to get really crazy, [hackaday](https://hackaday.com/) demonstrates how to power 1000 NeoPixels with the Arduino's limited RAM.\
\

[Hackaday: Driving 1000 Neopixels With 1K Of Arduino RAM](http://hackaday.com/2014/05/19/driving-1000-neopixels-with-1k-of-arduino-ram/)

\

Or you can try to adapt the example code to your favorite microcontroller. Teensy development boards are an excellent choice when using a large number of WS2812 LEDs.

[![Teensy LC](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/7/1/13305-01.jpg)](https://www.sparkfun.com/products/13305)

### [Teensy LC](https://www.sparkfun.com/products/13305) 

[ DEV-13305 ]

The Teensy LC is a 32 bit microcontroller board that provides you with an uncomplicated option to get started with Teensy wit...

**Retired**

[![Teensy 3.5](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/5/14055-01.jpg)](https://www.sparkfun.com/products/14055)

### [Teensy 3.5](https://www.sparkfun.com/products/14055) 

[ DEV-14055 ]

The Teensy 3.5 is larger, faster and capable of more projects, especially with its onboard micro SD card port.

**Retired**

[![Teensy 3.6](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/7/14057-01.jpg)](https://www.sparkfun.com/products/14057)

### [Teensy 3.6](https://www.sparkfun.com/products/14057) 

[ DEV-14057 ]

The Teensy 3.6 is larger, faster and capable of more complex projects, especially with its onboard micro SD card port and upg...

**Retired**

**Note:** Depending on the amount of WS2812 LEDs that are being used with the Teensy, you may need to use the octows2811 adapter board:\
\

[PJRC: OctoWS2811 LED Library](https://www.pjrc.com/teensy/td_libs_OctoWS2811.html)

\

How do you want to control all these LEDs? One of the biggest factors when deciding this is figuring out how many LEDs you want your final installation to contain. Some LED controllers have limitations on how many LEDs they can control. For example, the FadeCandy can handle up to 512 LEDs each. If you have more than 512 LEDs, you\'ll need to add a second FadeCandy or use a different driver. More drivers means an added bit of complexity, as you\'ll need to keep track of the addresses of each one, as well as each LED\'s location.

Only one FadeCandy was used to control the 480 LEDs in the CandyBar. It lives atop the OctoController board from danjuliodesigns.com, and communicates to the Driver boards over varying lengths of Ethernet cables. The Ethernet cables provide both power and communication to each pair of LED strips through the DualDriver boards as well as [ESD](https://en.wikipedia.org/wiki/Electrostatic_discharge) protection.

### Power

This is one area that is often overlooked. A few LEDs draw very little power, but add up several hundred and you have one very power-hungry project. Not only that, but power must be distributed evenly to prevent some LEDs appearing brighter than others or putting off slightly different colors.

For the CandyBar, the same power scheme that Dan used in his [Luminescence project](http://danjuliodesigns.com/personal/personal/personal/luminescence.html) was used, scaled for my purposes: a single 24V/250W power supply, which then delivers 5V to each subsequent DualDriver board at up to 30 Watts per pair of LED strips (2x1 meter segments).

If you want to add more LEDs, you will need to add more power. Dan ended up using five of these supplies to power, one for each of the five FadeCandies controlling the 2300 LEDs in the sculpture.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/1/sys_control_lg.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/1/sys_control_lg.jpg)

*Image courtesy of [danjuliodesigns.com](http://danjuliodesigns.com/).*

You\'re not limited to these particular power supplies. If you have high-current 5V supplies, you can power the strips directly from them. Just be aware of how much current you\'re drawing from any power supply you use.

### Space and Environmental Conditions

How are you going to enclose this project? Is it going to be indoors or outdoors? Does it need to be sealed off from the elements? The answers to these questions can greatly affect how you build your project. If the LEDs need to be sealed up, heat may become an issue. If you\'re working indoors, you can save some money by not having to buy tons of weather proofing materials, or products that are already weatherproof.

Luckily for me, the location for the CandyBar had already been picked, and the idea to house the LEDs atop a long ledge covered in decorative molding had been decided before I was brought on to the project. Sometimes it\'s easier to design around a set of requirements rather than having free range to design as you see fit.

The CandyBar was built in pieces that could all be disassembled and reassembled atop the ledge. The plan was to use strips of [hardboard](https://en.wikipedia.org/wiki/Hardboard) cut into 8-foot segments. Hardboard is sturdy enough to house LED strips, but lightweight enough that it wouldn\'t put strain on the ledge.

I had 8 meters of LED strips to cover the 46-foot ledge. Adding more LEDs meant more power and another FadeCandy, but I wanted to keep this as simple as possible. I didn\'t have time to shop for different strips that have the LEDs more widely spaced apart, so I cut the strips into smaller sizes to even out the spacing between sections of LEDs. Each strip ended up getting cut in two, giving me 16 half-meter strips, and making the gaps between each much less noticeable.

As you\'re designing, just know that things may look good on paper, but you may have to improvise come build time.

## Construction 

It\'s wise not to start building until you have all the parts you think you\'ll need. As you build, you may find a need for parts you didn\'t think of during the design phase. Or, as in my case, you may find that you didn\'t get enough of a particular material.

The actual assembly and construction is my favorite part. It\'s very satisfying to watch your project come to life, piece by piece. In my case, I needed a very long space to work in. All the pieces of hardboard were placed in one long row, just as they would be in the final installment.

Each segment was marked where the LEDs would be attached and where the driver boards would go.

To attach the strips to the driver boards, the opposite ends of the strip that weren\'t needed were cut off and connected via screw terminals.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/1/driver.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/1/driver.jpg)

As planned, some of these connectors ended up near the end of the hardboard sections, making connecting and disconnecting a breeze. However, some of the segments did not line up with the hardboard. These strip segments were affixed with polarized connectors.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/1/Sales_Space_Project-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/1/Sales_Space_Project-02.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/1/Sales_Space_Project-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/1/Sales_Space_Project-03.jpg)

With everything marked and the LED strips prepped, it was time to adhere the strips and drivers to the hardboard with double-sided tape. Ribbon cable was used to connect the portions of LEDs that didn\'t need to be disassembled.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/1/Sales_Space_Project-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/1/Sales_Space_Project-01.jpg)

Once everything was soldered, it was time to test it all out. The FadeCandy server has a nice button to turn all the LEDs on or off for a quick test. With the solder connections all tested, the next task was to figure out the LED mapping.

## Setting Up the FadeCandy Server

If you\'ve opted to use the FadeCandy, this is a good time to set up the control portion of the project and begin testing your LED strips. This tutorial assumes that you already have you Pi set up and can ssh into it or have it attached to a monitor, keyboard and mouse.

Inside the examples folder of the [FadeCandy GitHub](https://github.com/scanlime/fadecandy), you\'ll find a [config folder](https://github.com/scanlime/fadecandy/tree/master/examples/config) that houses a few different config files for the server. With help from [this tutorial](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy/fadecandy-server-setup), the file below was created for mapping the layout of the CandyBar, which required accounting for the 60 LEDs per strip version I have, versus the 64 LEDs per strips that are set as the default in the file.

    ,

        "devices": [
            
        ]
    }

Another gotcha is that the mapping assumes you are creating an array of LED strips, like a display, and the CandyBar is just a line of LEDs. Thus every other strip was mapped backward, with strip one mapping from 0-59, and the following going from 119-60. You can account for this in software or in the server config file should your project also be linear in design. I ended up just accounting for it in software. The Python sketch below was great for a quick test.

    language:python
    #!/usr/bin/env python

    # Light each LED in sequence, and repeat.

    import opc, time

    numLEDs = 480
    client = opc.Client('fadecandy.local:7890')

    while True:
        for i in range(59, 0, -1):
            pixels = [ (0,0,0) ] * numLEDs
            pixels[i] = (255, 255, 255)
            client.put_pixels(pixels)
            time.sleep(0.01)
        for i in range(60, 119):
            pixels = [ (0,0,0) ] * numLEDs
            pixels[i] = (255, 255, 255)
            client.put_pixels(pixels)
            time.sleep(0.01)
        for i in range(179, 120, -1):
            pixels = [ (0,0,0) ] * numLEDs
            pixels[i] = (255, 255, 255)
            client.put_pixels(pixels)
            time.sleep(0.01)
        for i in range(180, 239):
            pixels = [ (0,0,0) ] * numLEDs
            pixels[i] = (255, 255, 255)
            client.put_pixels(pixels)
            time.sleep(0.01)
        for i in range(299, 240, -1):
            pixels = [ (0,0,0) ] * numLEDs
            pixels[i] = (255, 255, 255)
            client.put_pixels(pixels)
            time.sleep(0.01)
        for i in range(300, 359):
            pixels = [ (0,0,0) ] * numLEDs
            pixels[i] = (255, 255, 255)
            client.put_pixels(pixels)
            time.sleep(0.01)
        for i in range(419, 360, -1):
            pixels = [ (0,0,0) ] * numLEDs
            pixels[i] = (255, 255, 255)
            client.put_pixels(pixels)
            time.sleep(0.01)
        for i in range(420, 479):
            pixels = [ (0,0,0) ] * numLEDs
            pixels[i] = (255, 255, 255)
            client.put_pixels(pixels)
            time.sleep(0.01)

## Installation 

Once you have all the bits and pieces assembled, it\'s time to install them in their permanent (or temporary) resting place. A word of advice: high-up, long installations can be a pain to troubleshoot.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/1/Sales_Space_Project-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/1/Sales_Space_Project-04.jpg)

Each driver is connected and tested after installation.

**Heads up!** Be careful not to attach any of the Ethernet cables while the system is powered.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/1/Sales_Space_Project-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/1/Sales_Space_Project-06.jpg)

Each cable runs back to the controller board.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/1/Sales_Space_Project-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/1/Sales_Space_Project-05.jpg)

Power cables and an extra long mini-USB cable from the FadeCandy run from the controller board through the ledge, through a wall-mounted cable keeper and attach to the Raspberry Pi and power supply.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/1/2015-06-18_15.49.29.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/1/2015-06-18_15.49.29.jpg)

Here\'s a block diagram that shows what all the connections look like.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/1/diagram.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/1/diagram.png)

*Click for a larger view.*

Once you have everything installed, it\'s time to fire it up, and bask in the warming glow of your art.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/1/retailSpace.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/1/retailSpace.jpg)