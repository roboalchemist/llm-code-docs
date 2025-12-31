# Source: https://learn.sparkfun.com/tutorials/electronic-e-craft-terrarium

## Introduction

### Introduction

People put plants (both plastic and real) in terrariums to create small, concentrated natural environments. What makes these terrariums interesting to me is that the glass enclosure isolates the ordinary objects from the real world and frames the objects for people to take a closer look. For this project, I included electronic components into a terrarium for people to appreciate the aesthetic aspects of technology. Also, I also wanted to express that technology is alive in another way.

In this tutorial, I will be creating an interactive, electronic terrarium. When the edge of the terrarium is touched, the lights start to breathe, and a leaf appears in the sand. To see the terrarium in action, check out the video below.

ReplaceMeOpen

ReplaceMeClose

*[Electronic Terrarium](https://vimeo.com/149788225) from [Kehui Liu](https://vimeo.com/carrielkh) on [Vimeo](https://vimeo.com).*

### Materials Required

You will need the following materials to follow along with this project.

You will need one of the following to program the ATtiny.

[![Tiny AVR Programmer](https://cdn.sparkfun.com/r/140-140/assets/parts/8/1/1/1/11801-01.jpg)](https://www.sparkfun.com/tiny-avr-programmer.html)

### [Tiny AVR Programmer](https://www.sparkfun.com/tiny-avr-programmer.html) 

[ PGM-11801 ]

The ATtiny45 and 85 are a couple of really cool little MCUs but did you know you can program them in Arduino? That\'s right, n...

[ [\$18.95] ]

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/9/5/1/8/12757-01.jpg)](https://www.sparkfun.com/products/12757)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/products/12757) 

[ DEV-12757 ]

At SparkFun we use many Arduinos and we\'re always looking for the simplest, most stable one. Each board is a bit different an...

**Retired**

Additionally, you will need the following materials:

- An ATtiny Microcontroller - This project uses the [ATtiny45](http://www.mouser.com/ProductDetail/Atmel/ATtiny45-20PU/?qs=8jWQYweyg6MLwoQA%2FmRFwg%3D%3D&gclid=CL-AmomLvMoCFZY0aQodQuMPbA). You could also use the [ATtiny85](ATtiny).
- [TIP120 Transistor](http://www.mouser.com/ProductDetail/STMicroelectronics/TIP120/?qs=ljbEvF4DwOPl3O93r6IAPg%3D%3D&gclid=CIOMhNeNk8oCFQ8zaQodDZwH7Q)
- Paint
- Sand
- Fabric
- Crimp Beads
- Glass Vase

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend reading over them before proceeding.

- [Light-Emitting Diodes](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
- [How to Solder - Through Hole](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering)
- [What Is Electricity?](https://learn.sparkfun.com/tutorials/what-is-electricity)

## Arduino Code

Before we begin building this project, we need to first program the ATtiny, because we will be soldering directly to its legs, making it much more difficult to reprogram afterwards. If you would like to not solder directly to your ATtiny so as to be able to reprogram it or to reuse it in a later project, you can use a [DIP Socket](https://www.sparkfun.com/products/7937) as well, soldering all the parts to it and then inserting the ATtiny into it.

Program the code onto the ATtiny using the Arduino or ISP Programmer shown above. If you have never programmed an ATtiny using the Arduino IDE before, [have a look at this tutorial](http://highlowtech.org/?p=1695) about how to work with ATtiny. Alternatively, if you are using the TinyAVR Programmer, [take a look at this tutorial](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide/).

You will also need to add the [Capacitive Sensor library](http://playground.arduino.cc/Main/CapacitiveSensor?from=Main.CapSense) to your Arduino IDE in order to compile the sketch. This can be added using the [Library Manger](https://learn.sparkfun.com/tutorials/installing-an-arduino-library#using-the-library-manager).

[![Capacitive Sensor Library](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/5/InstallCapacitiveSensorLibrary.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/5/InstallCapacitiveSensorLibrary.JPG)

Copy and paste the code from below.

    language:c

    /*Electronic Terrarium
    Code by Kehui Liu
    December 2015
    From the Performative Sculpture class of Parsons DT
    Project tutorial available here: https://learn.sparkfun.com/tutorials/electronic-terrarium
    Released under the MIT License (https://opensource.org/licenses/MIT)
    */

    #include <CapacitiveSensor.h>

    CapacitiveSensor cs_3_4=CapacitiveSensor(3, 4);
    int heat = 0;
    int led = 1;
    long total;
    void setup()

    void loop()
            for(int i = 0; i<255;i++)
        }else
        delay(300);
    }

## Assembly

### Dye the Sand

[![Sand Coloring Materials](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/5/sand1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/5/sand1.jpg)

Mix thermochromic pigment with regular paint. Add the mixture to the sand and let dry. The color of thermochromic dye will fade when heated.

[![Coated Sand](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/5/sand2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/5/sand2.jpg)

*Thermochromatically covered sand.*

Mixing and matching paints and thermochromatic pigment will result in different colors of the sand in a neutral state. Remember that the color will fade the base paint color when heated.

### Sew the Flexinol

Draw a shape of your choice on a piece of fabric that you\'d like to display once heated. Sew the Flexinol onto the fabric. Seal the two end with [crimp beads](https://www.google.com/search?q=crimp+beads&ie=utf-8&oe=utf-8#q=crimp+beads&tbm=shop).

[![Flexinol leaf](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/5/leaf.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/5/leaf.jpg)

To test the result, cover the shape in a small amount of sand. Using a 9v battery, hook one end of the Flexinol to the positive (+) terminal and the other end to the negative (-) terminal. You should see the sand change color on top of the Flexinol shape.

### Tape the Vase

Use copper tape to outline your desired touching point. You will also need a spot on the copper tape to solder to your ATtiny.

[![Vase with copper tape](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/5/vase.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/5/vase.jpg)

### Solder Everything Together

Connect your circuit together. Use the image below as a guide.

[![Connected Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/5/parts.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/5/parts2.png)

*Please note that pin 1 of the ATtiny is the upper-left pin in the image.*

### Put Everything Into the Vase

Arrange the parts as you like. Gluing some components to the side of the enclosure may be necessary. Last, add the sand, and leave a thin layer on the heating part.

[![Parts in Vase](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/5/CompleteTerrarium.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/5/CompleteTerrarium.jpg)

### Connect the Batteries and Done!

Insert the CR2032 battery into the holder. Make sure the positive (+) side of the battery is facing out.

[![CR2032 Battery Inserted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/5/battery1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/5/battery1.jpg)

Finally, connect your 9V battery to the system.

[![9V Battery Inserted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/5/battery2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/5/battery2.jpg)

Now, when the edge is touched, you should see the image light up in the sand!