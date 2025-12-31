# Source: https://learn.sparkfun.com/tutorials/microsd-sniffer-hookup-guide

## Introduction

The [microSD Sniffer](https://www.sparkfun.com/products/9419) is a useful tool for hacking or debugging circuits with microSD functionality.

[![microSD Sniffer](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/6/angledSnifferCrop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/6/angledSniffer.jpg)

The Sniffer allows you to see the SPI signals passing back and forth from your microSD card to your microcontroller or project.

### Covered in This Tutorial

This tutorial will show you how to setup the sniffer as well as how to use it to \"sniff\" the data transmitted to and received from a microSD card.

### Materials Required

To follow along with this tutorial, we recommend you have access to the following materials.

You will also need a project that has a microSD slot involved. We will be using the microSD Shield and Redboard.

[![SparkFun microSD Shield](https://cdn.sparkfun.com/r/140-140/assets/parts/9/5/2/8/12761-05.jpg)](https://www.sparkfun.com/sparkfun-microsd-shield.html)

### [SparkFun microSD Shield](https://www.sparkfun.com/sparkfun-microsd-shield.html) 

[ DEV-12761 ]

Running out of memory space in your Arduino project? The SparkFun microSD Shield equips your Arduino with mass-storage capabi...

[ [\$17.95] ]

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/9/5/1/8/12757-01.jpg)](https://www.sparkfun.com/products/12757)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/products/12757) 

[ DEV-12757 ]

At SparkFun we use many Arduinos and we\'re always looking for the simplest, most stable one. Each board is a bit different an...

**Retired**

You will also need some kind of logic analyzer. You can use anything like the following:

[![USB Oscilloscope - MSO-19](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/5/8/09263-4.jpg)](https://www.sparkfun.com/products/9263)

### [USB Oscilloscope - MSO-19](https://www.sparkfun.com/products/9263) 

[ TOL-09263 ]

Need to do some debugging? Who doesn\'t? But do you really want to be weighed down with a logic analyzer, a pattern generator ...

**Retired**

[![USB Oscilloscope - MSO-28](https://cdn.sparkfun.com/r/140-140/assets/parts/6/8/0/9/11219-01a.jpg)](https://www.sparkfun.com/products/11219)

### [USB Oscilloscope - MSO-28](https://www.sparkfun.com/products/11219) 

[ TOL-11219 ]

Who needs a whole bag full of instruments just to do some debugging? Why can\'t your logic analyzer and your DSO be the same b...

**Retired**

[![Logic 4 - USB Logic Analyzer](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/3/2/9/13195-03.jpg)](https://www.sparkfun.com/products/13195)

### [Logic 4 - USB Logic Analyzer](https://www.sparkfun.com/products/13195) 

[ TOL-13195 ]

This is the Logic 4, a powerful logic analyzer in a very small anodized aluminum package from \[Saleae Logic\](https://www.sale...

**Retired**

[![Logic Pro 8 - USB Logic Analyzer](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/3/3/0/13196-03.jpg)](https://www.sparkfun.com/logic-pro-8-usb-logic-analyzer.html)

### [Logic Pro 8 - USB Logic Analyzer](https://www.sparkfun.com/logic-pro-8-usb-logic-analyzer.html) 

[ TOL-13196 ]

Do you need big logic analysis in a small package? That\'s exactly what the Logic Pro 8 brings you. The Logic Pro 8 is a 8-cha...

**Retired**

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend reviewing them before beginning to work with the microSD Sniffer.

- [Serial Peripheral Interface](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)
- [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels)
- [SD Cards and Writing Images](https://learn.sparkfun.com/tutorials/sd-cards-and-writing-images)
- [MicroSD Shield Hookup Guide](https://learn.sparkfun.com/tutorials/microsd-shield-and-sd-breakout-hookup-guide)

## Hardware Overview

Hardware wise, the microSD Sniffer is pretty simple and straight-forward! There\'s only 3 main parts you need to be aware of.

[![Front of Sniffer](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/6/FrontViewLabeled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/6/FrontViewLabeled.jpg)

*Front view of the microSD Sniffer.*

#### 1. Headers

The pins of the SD card are broken out for a standard 0.1-inch row of header holes. This allows you to solder headers onto the board and connect into a breadboard for prototyping. Alternatively, you can also just connect IC hooks on these holes and use a logic analyzer or oscilloscope to monitor the traffic across the SPI bus.

#### 2. microSD Socket

This is your standard microSD socket. It fits microSD cards. Hurray simplicity!

#### 3. microSD Insert

[![Back of Sniffer](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/6/backViewLabeled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/6/backViewLabeled.jpg)

*Back view of the microSD Sniffer.*

These are the actual connection pins for the microSD Sniffer. You will plug these into your circuit in place of where you would normally plug in a microSD card. Notice how they look exactly like the bottom of your microSD card?

## Hardware Hookup

### Assembly

We\'ll be using the microSD Sniffer to see the SPI traffic between the microSD shield and the microSD card. If you aren\'t sure how to set up the microSD shield, please review our tutorial [here](https://learn.sparkfun.com/tutorials/microsd-shield-and-sd-breakout-hookup-guide).

Insert the microSD card into the microSD Sniffer socket, and plug the end of the microSD Sniffer into the socket on the microSD shield.

Everything is now ready to go, but we still need something to actually watch the traffic. For this, we will be using the Logic 4 - USB Logic Analyzer. You can use whatever analyzer you have around, but you will need one with 8 channels.

Pair one channel from the analyzer to one header on the microSD Sniffer. Repeat this until all of your headers have been connected to the analyzer. Keep in mind that your analyzer may have a dedicated `GND` line or other dedicated channels, so make sure you match any of those up if that\'s the case.

[![General Circuit Hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/6/Micro_SD_Sniffer_Hook_Up_Guide.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/6/Micro_SD_Sniffer_Hook_Up_Guide.jpg)

*Everything is connected and ready to go!*

Once everything is connected, it\'s time to power it all up and watch the SPI traffic!

## Functionality

### Visualization

We can now view the data on the SPI bus with the logic analyzer. In our example, the Redboard is running the `Examples>SD>Datalogger.ino` sketch included by default in the Arduino IDE.

Open up the logic analyzer software, and configure it for your set up. In our example, we\'ve labeled each channel with the corresponding pin name on the microSD Sniffer.

The analyzer collects 1 million samples at 8MHz. Once it has collected data, you should see something similar to the following.

[![Default Reading](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/6/8MHz1MSamples.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/6/8MHz1MSamples.png)

*Initial Display of Readings*

We can see there is definitely something occuring on several of the lines, but it\'s still not clear what. If we look at our time scale, the range shown is 0ms to \~35ms. We can zoom in on a smaller time scale to get more detail about the communication occurring.

[![ZoomedIn](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/6/ZoomedIn.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/6/ZoomedIn.png)

*There is much more readable data at the smaller timeframe of 100us displayed.*

Looking at our data, we can see something is not quite right \-- according to the VCC line, there\'s no power going to our system! While the issue in this case was only due to a loose connection between the IC hook on the analyzer and the Sniffer, you could dig deeper into each signal to debug your circuit if there is a problem. If we fix the loose connection, the data looks better, showing a `HIGH` signal on `VCC`.

[![VCC Fixed](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/6/DebuggingVCC.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/6/DebuggingVCC.png)

Again, this is a very simplified example, but you could use the Sniffer to verify the clock signal to your card, or to see if there are actual data signals being sent to the microSD card.