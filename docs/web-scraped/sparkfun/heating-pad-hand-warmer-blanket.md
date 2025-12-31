# Source: https://learn.sparkfun.com/tutorials/heating-pad-hand-warmer-blanket

## What Are Heating Pads Good For?

There are a lot of great projects you can use heating pads ([5x10cm](https://www.sparkfun.com/products/11288) and [5x15cm](https://www.sparkfun.com/products/11289)) in, ranging from warming gloves, slippers, a blanket, or anything you want to keep nice and warm. Got a [beard mask](hhttps://www.etsy.com/search?q=beard%20mask) you want to make toasty? Do beards need to be warmer? Not sure. Would it be a fun project? Definitely.

[![Heating Pad - 5x10cm](https://cdn.sparkfun.com/r/600-600/assets/parts/6/9/5/9/11288-01.jpg)](https://www.sparkfun.com/heating-pad-5x10cm.html)

### [Heating Pad - 5x10cm](https://www.sparkfun.com/heating-pad-5x10cm.html) 

[ COM-11288 ]

These DC powered heating pads are perfect for near-body heating applications. They get warm to the touch but not too hot as l...

[ [\$4.75] ]

[![Heating Pad - 5x15cm](https://cdn.sparkfun.com/r/600-600/assets/parts/6/9/6/0/11289-01.jpg)](https://www.sparkfun.com/heating-pad-5x15cm.html)

### [Heating Pad - 5x15cm](https://www.sparkfun.com/heating-pad-5x15cm.html) 

[ COM-11289 ]

These DC powered heating pads are perfect for near-body heating applications. They get warm to the touch but not too hot as l...

[ [\$5.95] ]

### What Parts Should You Consider Getting for Your Project?

You can go as simple as getting the appropriate power supply and a heating pad. One heating pad is rated for **5V**, and draws about **600mA**. If you want to add a form of logic or control to your circuit, such as interfacing with sensors, the easiest way is to add a microcontroller/development board to your project. You will also need some wire and transistor to control the heating pad if you are using a microcontroller. Check the wishlist in the next section for more details on the products used in this tutorial.

[] **Warning!** Please make sure to use the appropriate power requirements when operating this heating pad. We do not recommend this product for beginners.

### Tools

You will need sewing needles, a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Needle Set](https://cdn.sparkfun.com/r/140-140/assets/parts/4/8/7/5/10405-04b.jpg)](https://www.sparkfun.com/needle-set.html)

### [Needle Set](https://www.sparkfun.com/needle-set.html) 

[ TOL-10405 ]

This set of sewing needles is a must-have when stitching together your next e-textile project. Each envelope contains three 4...

[ [\$2.25] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

- [Basic Lilypad Tutorial](https://www.sparkfun.com/tutorials/313)
- [Beginning LilyPad Arduino](https://www.sparkfun.com/tutorials/312)
- [Planning a Wearable Electronics Project](https://learn.sparkfun.com/tutorials/planning-a-wearable-electronics-project)
- [LilyPad Basics:E-Sewing](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)
- [Transistors](https://learn.sparkfun.com/tutorials/transistors)

## DIY Project Idea: Hand Warmer Blanket

A blanket project with two heating pads to keep your hands warm when you are on the computer/notebook/tablet/phone/playing chess/all other activities.

### Required Materials

There are a lot of parts on this list that can be exchanged for alternate parts, or that aren\'t needed at all, depending on what type of setup you want. To follow along with this project, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

**Note:** If you do not want to sew or use conductive thread, exchange the Lilypad LEDs and Lilypad button for through-hole components and solder on a bigger protoboard instead.

You could use a 3.7 LiPo battery to power both the LilyPad USB board and the heating pads. Remember: You will still need a MOSFET, because having two heating pads will draw more current then the LilyPad pins can handle. This option is nice, since you can use the LilyPad to charge the LiPo battery when the heating pad isn\'t in use. The draw back to using a 3.7v LiPo battery is that the heating pads won\'t get as warm as they would with a 5v (or higher) power supply.

In this setup, we use the LilyPad USB, because you won\'t have to get an extra FTDI basic for an USB connection.

## Directions

The first step is to select your fabric. When picking a fabric, you want to consider the following:

- Is the pattern on the fabric going to work, or look out of place? If you are going Snuggie style, will you need to add extra fabric for the arms?
- On what level of awesome is the fabric you are selecting? Meaning, how fast are you going to get sick of looking at it?
- Is the fabric thick, cozy, and going to keep the rest of your body warm? Sheer, light fabrics don\'t help to keep you warm during the winter months.

In the video below, you\'ll see that you can get as weird as you want when customizing your blanket:

For the example in the video, extra fabric and button snaps were sewn on the back of the blanket for easy removal for washing.

[![Heating pad blanket with sewing snaps](//cdn.sparkfun.com/r/600-600/assets/b/b/b/3/9/514761face395fc95c000000.jpg)](//cdn.sparkfun.com/assets/b/b/b/3/9/514761face395fc95c000000.jpg)

If you don\'t have a sewing machine, or don\'t want to sew, you can do a No-Sew blanket and be creative when adding a pouch that holds your heating pads and circuit. [No-Sew blanket tutorials](http://www.instructables.com/tag/type-id/?q=no+sew+blanket&sort=none)

## Circuit

Here is a diagram of the circuit setup:

[![Circuit Heating Pads Arduino LEDs MOSFET](//cdn.sparkfun.com/r/600-600/assets/0/9/3/2/0/514761face395f055e000000.jpg)](//cdn.sparkfun.com/assets/0/9/3/2/0/514761face395f055e000000.jpg)

*Having a hard time seeing the circuit? Click the image for a closer look.*

**Note:** As you can see, the LilyPad LEDs and Lilypad Button were sewn into the fabric, but you can easily switch these for normal, through-hole LEDs, and a button soldered on a protoboard with the other soldered components.

[] **Warning!** Make sure to solder hook-up wire to your heating pad connections. DO NOT try to use conductive thread to connect the two heating pads.

## Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

    language:c
      /*

     Heating Pad Hand Warmer Blanket Code Example
      SparkFun Electronics, Pamela, 1/24/2013
      Beerware License

      Hardware Connections:
      -led1 = D9;
      -led2 = D10;
      -led3 = D11;
      -button = D2;
      -Mofset = D3;

      Usage: 
      Hit the switch to power, hit the button to adjust how warm the heating elements get, and three LEDs will indicate low, medium, and high levels. 
     */

    int btnPin = 2;
    boolean btnPressed = false;
    int fetPin = 3;
    int led1 = 9;
    int led2 = 10;
    int led3 = 11;
    int mode;

    void setup() 

    // the loop routine runs over and over again forever:
    void loop() 
    }

There you go! As with any DIY project, you should always customize and tweak what you want for maximum awesomeness.

[] **Warning:** Make sure when using heat pads, not to leave unattended!