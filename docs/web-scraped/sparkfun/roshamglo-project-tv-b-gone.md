# Source: https://learn.sparkfun.com/tutorials/roshamglo-project-tv-b-gone

## Introduction

In addition to playing some infrared (IR) Rock-Paper-Scissors, you can use your [Roshamglo badge](https://www.sparkfun.com/products/14130) for a number of fun activities, including sending IR commands to your TV (well, almost any TV, really).

[![SparkFun Roshamglo Badge Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/0/2/7/14130-05.jpg)](https://www.sparkfun.com/products/14130)

### [SparkFun Roshamglo Badge Kit](https://www.sparkfun.com/products/14130) 

[ KIT-14130 ]

The SparkFun Roshamglo is the new and fun way to play Rock-Paper-Scissors with your friends! The board uses the ATtiny84, and...

**Retired**

A few years ago, [Mitch Altman](https://en.wikipedia.org/wiki/Mitch_Altman) designed an ATtiny85-based IR remote, known as [TV-B-Gone](http://www.tvbgone.com/)^®^, that transmits the power code of popular televisions over the course of about a minute. Since then, several people have contributed to the open source code of TV-B-Gone, including [Limor Fried](https://en.wikipedia.org/wiki/Limor_Fried) and [Ken Shirriff](https://github.com/shirriff), who created an [Arduino port of the program](https://github.com/shirriff/Arduino-TV-B-Gone).

**Note:** TV-B-Gone works by transmitting the \"Power On/Off\" signal in over 100 TV encoding schemes. It works for about 80% of the most popular manufacturers (e.g., Panasonic, Sony, RCA, Toshiba), but there is no support for some newer TV manufacturers (e.g., Insignia, Affinity).

### Required Materials

You will need a [Roshamglo badge](https://www.sparkfun.com/products/14130) and, optionally, a resistor between 47Ω and 1kΩ. We recommend the [Resistor Kit](https://www.sparkfun.com/products/10969), as it has several different resistor options to play with.

#### Tools

If you plan to add a resistor to your Roshamglo badge to increase the IR range, you will need a [soldering iron](https://www.sparkfun.com/products/9507) and [solder](https://www.sparkfun.com/search/results?term=solder).

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/ir-communication)

### IR Communication 

This tutorial explains how common infrared (IR) communication works, as well as shows you how to set up a simple IR transmitter and receiver with an Arduino.

[](https://learn.sparkfun.com/tutorials/hack-your-roshamglo-badge)

### Hack Your Roshamglo Badge 

Learn how to customize and program your Roshamglo badge.

[](https://learn.sparkfun.com/tutorials/roshamglo-hookup-guide)

### Roshamglo Hookup Guide 

This tutorial provides everything you need to know to get started with the Roshamglo badge.

## Hardware Assembly (Optional)

In its default state, the Roshamglo badge has an IR transmission range of about 5 feet. This was done by design to prevent people from bouncing signals off other people and interrupting Rock-Paper-Scissors games.

However, 5 feet is a little short for being able to control a TV from across the room. You don\'t need to upgrade the hardware, but if you do, you can easily shoot TV beams from 40+ feet away.

First, choose a resistor value you want to use to upgrade your badge\'s range. Something between 47Ω (40+ feet range) and 1kΩ (around 10 feet) will work the best. Note that the resistor will be in parallel with the 1.5kΩ resistor that\'s already on the board. To help you decide what to choose, here are some common resistor values that should work:

  Resistor   Current Through LED   Predicted Range
  ---------- --------------------- -----------------
  47Ω        37mA                  40 feet
  100Ω       18mA                  20 feet
  220Ω       9mA                   12 feet
  330Ω       6mA                   10 feet
  470Ω       5mA                   8 feet
  1kΩ        3mA                   6 feet
  Open       1mA                   5 feet

**Note:** If you want the maximum range, just use a **47Ω resistor**. You could get away with a smaller resistor, and therefore more current, but keep in mind the IR LED is rated for a maximum of 70mA. Things could get hot.

In the corner of the Roshamglo board, by the USB connector, you will see two holes situated diagonally toward the center of the board with the label `R_Ext`.

[![Resistor holes on Roshamglo](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/7/Roshamglo_TV_be_gone_Tutorial-01_highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo_TV_be_gone_Tutorial-01_highlight.jpg)

Solder your chosen resistor into those holes. We recommend bending the resistor\'s leads so that the resistor folds nicely onto the board and does not touch other components.

[![Extra resistor added to Roshamglo](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/7/Roshamglo_TV_be_gone_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo_TV_be_gone_Tutorial-02.jpg)

*Resistor bent between components*

## Programming

Before we load the TV-B-Gone code onto the Roshamglo badge, we\'ll need to install Arduino and the Roshamglo board definitions. Follow the instructions in the tutorial below to make sure you can send new programs to your Roshamglo board.

[](https://learn.sparkfun.com/tutorials/hack-your-roshamglo-badge)

### Hack Your Roshamglo Badge 

March 12, 2017

Learn how to customize and program your Roshamglo badge.

**Note:** We are using a version of the TV-B-Gone software that has been modified to work on Roshamglo. A few of the TV codes have been removed in order to make it fit into the 6k of program memory available on the badge\'s microcontroller.

Download the [Roshamglo Project Repository](https://github.com/sparkfun/Roshamglo) as a .zip file:

[Download the Roshamglo Project](https://github.com/sparkfun/Roshamglo/archive/master.zip)

Unzip it. Open the Arduino IDE and select **File \> Open**. Navigate to **\\/Firmware/Examples/Roshamglo-TV-B-Gone**. Open the **Roshamglo-TV-B-Gone.ino** file.

[![Roshamglo TV-B-Gone Arduino code](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo-TV-B-Gone_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo-TV-B-Gone_01.png)

By default, the Roshamglo-TV-B-Gone code supports North American IR codes. To change them to support European Union codes, click on the **main.h** tab and change

    language:c
    #define REGION NA

to

    language:c
    #define REGION EU

[![Changing TV-B-Gone to support European Union IR codes](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo-TV-B-Gone_06.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo-TV-B-Gone_06.png)

Select **Tools \> Board \> Roshamglo**.

[![Programming Roshamglo badge with TV-B-Gone firmware](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/7/Roshamglo-TV-B-Gone_02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo-TV-B-Gone_02.png)

Click the **Upload** button.

[![Uploading the firmware from Arduino](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo-TV-B-Gone_03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo-TV-B-Gone_03.png)

Wait for **Uploading** to appear at the bottom of the Arduino window.

[![Waiting for Roshamglo badge in Arduino](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo-TV-B-Gone_04.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo-TV-B-Gone_04.png)

At this point, make sure your Roshamglo badge is **OFF**, and press and hold the **Down** button on the Roshamglo badge (hold the five-way switch toward the *SparkFun* logo). While holding the **Down** button, insert the badge into an available USB slot on your computer.

[![Putting Roshamglo into bootloader mode](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/7/Hacking_the_Roshamglo_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Hacking_the_Roshamglo_Tutorial-01.jpg)

The program should be uploaded from Arduino. You should see a *Done Uploading* message appear.

[![Finished uploading TV-B-Gone firmware to Roshamglo from Arduino](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo-TV-B-Gone_05.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo-TV-B-Gone_05.png)

**Note:** If you get an error message while uploading, it could be caused by a variety of reasons. The way we\'re uploading programs to Roshamglo is actually hacked together, as we\'re [emulating USB](https://www.obdev.at/products/vusb/index.html) on the badge, which many computers do not like. Here are some things to try if you do get an error:

- Try a different USB port
- Unplug other USB devices
- Close other programs that might be running
- Reinstall the [Roshamglo USB driver](https://learn.sparkfun.com/tutorials/hack-your-roshamglo-badge#install-usb-driver)
- Try a different computer

## Try It Out

Turn on your Roshamglo badge. If North American IR codes were chosen (default), the green LED will blink three times. If EU codes were chosen, the green LED will blink six times.

Find a nearby TV, aim the USB connector toward it and press down on the center button of the five-way switch. The green LED should begin to flash intermittently, which indicates that the IR codes are being sent. You can let go of the button at this point; the codes will continue to be sent. Note that it could take up to 72 seconds for all the codes to be transmitted; keep pointing the badge at your target.

[![Turn off a TV with your Roshamglo badge](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/7/Roshamglo_TV_be_gone_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/7/Roshamglo_TV_be_gone_Tutorial-04.jpg)

With any luck, the TV should turn off (or perhaps on, as the IR codes for on and off are the same for many TVs).

**Note:** The beam width on Roshamglo\'s IR LED is fairly narrow. You may have to point it directly at the TV\'s IR receiver.

If you would like to cancel the 72 seconds of code transmission, you can either press the *RESET* button or turn the badge off using the side switch.