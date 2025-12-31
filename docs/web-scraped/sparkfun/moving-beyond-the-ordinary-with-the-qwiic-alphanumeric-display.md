# Source: https://learn.sparkfun.com/tutorials/moving-beyond-the-ordinary-with-the-qwiic-alphanumeric-display

## Introduction

Sometimes you need a display that can not only share information, but also catch the attention of those passing by. LCDs are great at getting a good amount of information on a small screen, but they're not nearly as eye-catching as an LED. Our Qwiic Alphanumeric Displays combine the best of both worlds, offering the ability to share information, combined with the eye-catching pop of LEDs. In this tutorial, We'll show you how fast and simple it is to start displaying information on the SparkFun Alphanumeric Display, starting with the most basic, then looking at some more advanced examples.

[![SparkFun Qwiic Alphanumeric Display Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/9/2/6/19297-SparkFun_Qwiic_Alphanumeric_Sampler_Kit-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-alphanumeric-display-kit.html)

### [SparkFun Qwiic Alphanumeric Display Kit](https://www.sparkfun.com/sparkfun-qwiic-alphanumeric-display-kit.html) 

[ KIT-19297 ]

The SparkFun Qwiic Alphanumeric Display Kit comes with six different colored, 14-segment Qwiic displays. This is your all-in-...

**Retired**

## Required Hardware

For this tutorial, you'll only need the following components:

A Qwiic Alphanumeric Display, in the color of your choosing:

[White Qwiic Alphanumeric Display](https://www.sparkfun.com/products/18565)

[Red Qwiic Alphanumeric Display](https://www.sparkfun.com/products/16916)

[Blue Qwiic Alphanumeric Display](https://www.sparkfun.com/products/16917)

[Purple Qwiic Alphanumeric Display](https://www.sparkfun.com/products/16918)

[Pink Qwiic Alphanumeric Display](https://www.sparkfun.com/products/16919)

[Green Qwiic Alphanumeric Display](https://www.sparkfun.com/products/18566)

For the more advanced examples using multiple displays, you can mix and match from the individual options above, or pick up one of our kits containing multiple Qwiic Alphanumeric Displays:

[SparkFun Qwiic Alphanumeric Starter Kit - Red and White](https://www.sparkfun.com/products/18624)

[SparkFun Qwiic Alphanumeric Display Kit](https://www.sparkfun.com/products/19297)

And of course, you\'ll need a [microcontroller](https://www.sparkfun.com/search/results?term=Redboard) and some [Qwiic Cables](https://www.sparkfun.com/products/15081) to hook it all up.

**Note:** If you have a microcontroller that doesn\'t have a Qwiic connector, you can still easily connect your Qwiic board by utilizing our [Flexible Qwiic Cable Breadboard Jumper.](https://www.sparkfun.com/products/18566)

## Setting Up Your Alphanumeric Display

Thanks to our Qwiic system, setup could not be easier. Just follow these simple steps:

Connect one end of your Qwiic cable to the Qwiic connector on your microcontroller.

Connect the other end of your Qwiic cable to the Qwiic connector on your Alphanumeric Display.

Connect your USB-C cable to your microcontroller, then to your computer.

Feeling creative? You can change the order of these steps, and your setup will still work perfectly!

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/0/6/Alphanumeric_Hardware_Hookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/0/6/Alphanumeric_Hardware_Hookup.jpg)

## Installing the Required Libraries

You can install the SparkFun Qwiic Alphanumeric Display Library in either of a couple of different ways.

In the Arduino IDE, open the Library Manager (either by opening the panel of the left side of the app, or from the dropdown menu going to Sketch/Include Library/Manage Libraries). From there, search "SparkFun Qwiic Alphanumeric", and click the "Install" button.

Use the following link, download the .ZIP file, and either extract it and install it, or use the "Add .ZIP Library" option in the IDE.

[Download the Arduino Library](https://github.com/sparkfun/SparkFun_Alphanumeric_Display_Arduino_Library/archive/refs/heads/main.zip)

## The Basics

Let's start at the very beginning, a very good place to start. Once you've installed the library, you'll be able to access all of our example code. Navigate your way to File/Examples/SparkFun Qwiic Alphanumeric Display Arduino Library/Example_01_PrintString, open it and upload it to your microcontroller. If all goes as expected, your display should be showing the work "Milk" for all to see! (Why "Milk"? Eh, why not? It's four characters in length, shows the use of both uppercase and lowercase letters, and, well, I suppose our engineer likes milk!)

    /*****************************************************************************************
     * This example tests illuminating whole 4 letter strings on the 14-segment display.
     * 
     * Priyanka Makin @ SparkFun Electronics
     * Original Creation Date: February 3, 2020
     * 
     * SparkFun labored with love to create this code. Feel like supporting open source hardware?
     * Buy a board from SparkFun! https://www.sparkfun.com/products/16391
     * 
     * This code is Lemonadeware; if you see me (or any other SparkFun employee) at the 
     * local, and you've found our code helpful, please buy us a round!
     * 
     * Hardware Connections:
     * Attach Red Board to computer using micro-B USB cable.
     * Attach Qwiic Alphanumeric board to Red Board using Qwiic cable.
     * 
     * Distributed as-is; no warranty is given.
     ****************************************************************************************/
    #include <Wire.h>

    #include <SparkFun_Alphanumeric_Display.h> //Click here to get the library: http://librarymanager/All#SparkFun_Qwiic_Alphanumeric_Display by SparkFun
    HT16K33 display;

    void setup()
    
      Serial.println("Display acknowledged.");

      display.print("Milk");
    }

    void loop()
    

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/0/6/AlphanumericSingleMilk.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/0/6/AlphanumericSingleMilk.jpg)

\
If you feel like the bright lights of the Alphanumeric Display aren't enough to capture the attention of passersby, there's always the option of adding a little motion to your message. Our library has a built-in function, shiftLeft() (or shiftRight()), that slides your message across the displays. Run File/Examples/SparkFun Qwiic Alphanumeric Display Arduino Library/Example_09_ScrollingString to see it in action.

    /**************************************************************************************
     * This example tests scrolling functionality of alphanumeric displays.
     * 
     * Priyanka Makin @ SparkFun Electronics
     * Original Creation Date: February 26, 2020
     * 
     * SparkFun labored with love to create this code. Feel like supporting open source hardware?
     * Buy a board from SparkFun! https://www.sparkfun.com/products/16391
     * 
     * This code is Lemonadeware; if you see me (or any other SparkFun employee) at the
     * local, and you've found our code helpful, please buy us a round!
     * 
     * Hardware Connections:
     * Attach Red Board to computer using micro-B USB cable.
     * Attach Qwiic Alphanumeric board to Red Board using Qwiic cable. 
     *  Don't close any of the address jumpers so that it defaults to address 0x70.
     * Attach a second Alphanumeric display using Qwiic cable.
     *  Close address jumper A0 so that this display's address become 0x71.
     * 
     * Distributed as-is; no warranty is given.
     *****************************************************************************************/
    #include <Wire.h>

    #include <SparkFun_Alphanumeric_Display.h>  //Click here to get the library: http://librarymanager/All#SparkFun_Qwiic_Alphanumeric_Display by SparkFun
    HT16K33 display;

    void setup() 
      Serial.println("Displays acknowledged.");

      display.print("MILK");
      delay(500);
    }

    void loop() 
    

## Going Beyond the Basics

Our shift function is a fast and super-simple way to scroll text, but the length of the text is limited to four characters. (More if you're using multiple displays, but we'll talk about that a little later on.) So, what can you do if you want to scroll a text string that's longer than the number of display digits you have. We just need to get a little creative with our coding.

Example - Moving text the hard way Suppose I want to try the scrolling example, but I'm lactose intolerant. I want to scroll "soy milk", but my display is only four characters. For this, we can use a little creative manual character shifting. Take a look at the code below, and you'll see how the eight characters (I'm including the space between the two words) make their way past the four available spaces.

    /*******************************************************************************************
     * This demo shows how to manually scroll a word or words longer than four characters
     * across a digit alphanumeric display.
     * 
     * Rob Reynolds @ SparkFun Electronics
     * Original Creation Date: October 16, 2024
     * 
     * SparkFun labored with love to create this code. Feel like supporting open source hardware?
     * Buy a board from SparkFun! https://www.sparkfun.com/products/19297
     * 
     * This code is Beerware; if you see me (or any other SparkFun employee) at the 
     * local, and you've found our code helpful, please buy us a round!
     * 
     * Hardware Connections:
     * Attach Red Board to computer using micro-B USB cable.
     * Attach Qwiic Alphanumeric board to Red Board using Qwiic cable.
     * 
     * Distributed as-is; no warranty is given.
     *****************************************************************************************/
    #include <Wire.h>

    #include <SparkFun_Alphanumeric_Display.h>  //Click here to get the library: http://librarymanager/All#SparkFun_Qwiic_Alphanumeric_Display by SparkFun
    HT16K33 display;

    void setup()
    

      Serial.println("Display acknowledged.");
      delay(2000);

    }

    void loop()
    

Earlier, I mentioned the possibility of using multiple displays. This takes a little bit of work on the front end, but after that, using four displays is just as easy as using one.

On the rear of the display board, you'll find a pair of jumpers labeled A0 and A1. These jumpers will allow you to change the I2C address, giving you four options.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/0/6/I2C_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/0/6/I2C_Jumpers.jpg)

\
We've made linking and using multiple displays incredibly simple. There are just a couple of things you need to keep in mind. In your setup(), you will, as usual, check to make sure that your I2C peripheral (in this case your Alphanumeric Display) acknowledges, like this:

    if (display.begin() == false)

When using multiple displays, you simply verify that all of them acknowledge, like this:

     if (display.begin(0x70, 0x71, 0x72, 0x73) == false)

The big thing the remember here is that when daisy-chaining your displays, they do not need to be connected in numeric order. However, the order in which you verify them in your code must match their physical order, Therefore, if you are using four displays, each of a different color, once you've given each its own unique I2C address, you can place the colors in any order you want. Just make sure that you match their I2C address order with the order in which you verify them in your code, something like this:

    if (display.begin(0x73, 0x71, 0x70, 0x72) == false) // This is perfectly acceptable

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/0/6/Alphanumeric_Daisy_Chain.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/0/6/Alphanumeric_Daisy_Chain.jpg)

*^But\ why\ stop\ at\ just\ two\ Alphanumeric\ Displays?\ By\ changing\ the\ I2C\ addresses,\ you\ can\ daisy-chain\ up\ to\ four\ displays\ at\ once!^*

WARNING: TECHNICAL (BUT IMPORTANT) STUFF: When using multiple I2C devices all containing built-in pull up resistors, the parallel equivalent resistance will often create too strong of a pull up for the bus to operate. A good rule of thumb is, if you're using multiple I2C boards, you should disable all but one pair of pull up resistors. These pull up resistors can be removed by cutting the traces of the I2C jumpers, as highlighted in the image below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/0/6/Alphanumeric-Display_I2CJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/0/6/Alphanumeric-Display_I2CJumper.jpg)

*^When\ using\ multiple\ I2C\ devices,\ you\ may\ need\ to\ cut\ the\ trace\ for\ the\ I2C\ resistors\ on\ one\ of\ your\ boards.^*

## Going beyond the Expected

Sometimes it's fun to take something, completely ignore its intended use, and turn it on its head. Or at least, on its side. I found myself wondering if I could use these Alphanumeric Modules for Vertical display. Of course, if we had single character boards, it would be simple. But with four characters per board, stacking vertically becomes a bit more of a challenge. Luckily, as we learned in Example 02 Turn On One Segment, we can control each of the fourteen segments of each character individually. What that example doesn't show is that we can turn on multiple segments at once, allowing us to create any number of shapes. In its simplest form, you can think of the segments that make up the letter "U". If you turn the display on its end, those same segments will give you a low, wide, letter "C".

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/0/6/AlphaNumericSegmentLabels.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/0/6/AlphaNumericSegmentLabels.jpg)

The code below will give you an idea of what it takes to create vertical displays.

    /*******************************************************************************************
     * This example tests illuminating individual segments to create a vertical display of sorts.
     * We will also use characters that, when turned on their side, can pass for vertical displays.
     * ex using a Z as an N
     *
     * Pass in the segment
     * and digit you wish to illuminate to illuminateSegement().
     * 
     *
     * 
     * SparkFun labored with love to create this code. Feel like supporting open source hardware?
     * Buy a board from SparkFun! https://www.sparkfun.com/products/16391
     * 
     * This code is Beerware; if you see me (or any other SparkFun employee) at the 
     * local, and you've found our code helpful, please buy us a round!
     * 
     * Hardware Connections:
     * Attach Red Board to computer using micro-B USB cable.
     * Attach Qwiic Alphanumeric board to Red Board using Qwiic cable.
     * 
     * Distributed as-is; no warranty is given.
     *****************************************************************************************/
    #include <Wire.h>

    #include <SparkFun_Alphanumeric_Display.h>  //Click here to get the library: http://librarymanager/All#SparkFun_Qwiic_Alphanumeric_Display by SparkFun
    HT16K33 display;

    void setup()
    
      Serial.println("Display acknowledged.");
      display.clear();
      delay(1000);

    }

    void loop()
    

    void code()
    

    void name()
    

    void neon()
    

    void zone()
    

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/0/6/AlphanumericVertNEON.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/0/6/AlphanumericVertNEON.jpg)

*^Of\ course\ it\'s\ not\ neon,\ but\ if\ you\ dim\ the\ lights,\ and\ maybe\ squint\ a\ little,\ it\'s\ not\ a\ bad\ substitute.^*

\
And if you want to get really crazy, you can combine vertical and horizontal! Combining the display.illuminateSegment() calls with the display.printChar() calls (and making sure you assign each to their proper character number) will put you high and above all others with their simple horizontal alphanumeric displays.

\

    /**************************************************************************************
     * This example allows for both vertical and horizontal display of characters.
     * Keep in mind that they are not designed for vertical use, so some of the characters
     * are a little off. Hey, it's the best I could do!
     * 
     * Rob Reynolds @ SparkFun Electronics
     * Original Creation Date: November 11, 2024
     * 
     * SparkFun labored with love to create this code. Feel like supporting open source hardware?
     * Buy a board from SparkFun! https://www.sparkfun.com/products/19297
     * 
     * This code is Beerware; if you see me (or any other SparkFun employee) at the
     * local, and you've found our code helpful, please buy us a round!
     * 
     * Hardware Connections:
     * Attach Red Board to computer using micro-B USB cable.
     * Attach Qwiic Alphanumeric board to Red Board using Qwiic cable. 
     *  Don't close any of the address jumpers so that it defaults to address 0x70.
     * Attach a second Alphanumeric display using Qwiic cable.
     * Close address jumper A0 so that this display's address become 0x71.
     * Close the necessary jumpers (A0 and/or A1) to change the other displays I2C
     * addresses to 0x72 znd 0x73. See hoolup guide or tutorial for specifics.
     * 
     * Distributed as-is; no warranty is given.
     *****************************************************************************************/
    #include <Wire.h>

    #include <SparkFun_Alphanumeric_Display.h>  //Click here to get the library: http://librarymanager/All#SparkFun_Qwiic_Alphanumeric_Display by SparkFun
    HT16K33 display;

    void setup() 
      Serial.println("Displays acknowledged.");
      display.setBrightness(15);
      display.clear();

      //display.print("*BUY MOREDISPLAYS");
    }

    void loop() 
    

\

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/0/6/AlphanumericVertHorizDisplays.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/0/6/AlphanumericVertHorizDisplays.jpg)

*^We\ don\'t\ need\ more\ subliminal\ messaging,\ we\ need\ more\ Qwiic\ Alphanumeric\ Displays!^*