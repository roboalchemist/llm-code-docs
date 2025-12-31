# Source: https://learn.sparkfun.com/tutorials/lilypad-safety-scarf

## Introduction 

[] Design and build time: 1 Day

In this project, we'll create a wearable safety scarf. The safety scarf is embedded with LilyPad Hardware and a ribbon of LEDs. It is designed for pedestrians to increase visibility when walking the streets at night. The LED ribbon is triggered when light is low, making the wearer more visible to vehicles, bikers, and other pedestrians.

[![safety scarf](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/IMG_5340sm.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/IMG_5340sm.jpg)

### Suggested Reading

Before you get started, take some time to familiarize yourself with the following:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

[](https://learn.sparkfun.com/tutorials/polarity)

### Polarity 

An introduction to polarity in electronic components. Discover what polarity is, which parts have it, and how to identify it.

[](https://learn.sparkfun.com/tutorials/insulation-techniques-for-e-textiles)

### Insulation Techniques for e-Textiles 

Learn a few different ways to protect your conductive thread and LilyPad components in your next wearables project.

[](https://learn.sparkfun.com/tutorials/planning-a-wearable-electronics-project)

### Planning a Wearable Electronics Project 

Tips and tricks for brainstorming and creating a wearables project.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

Learn how to use conductive thread with LilyPad components.

[](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-hookup-guide)

### LilyPad ProtoSnap Plus Hookup Guide 

The LilyPad ProtoSnap Plus is a sewable electronics prototyping board that you can use to learn circuits and programming with Arduino, then break apart to make an interactive fabric or wearable project.

[](https://learn.sparkfun.com/tutorials/getting-started-with-lilypad)

### Getting Started with LilyPad 

An introduction to the LilyPad ecosystem - a set of sewable electronic pieces designed to help you build soft, sewable, interactive e-textile projects.

In this project, we will also be following a free sewing pattern from Purl Soho which can be [found here](https://www.purlsoho.com/create/2014/03/06/corinnes-thread-cozy-sewn-cowl/).

## Materials and Tools

Let\'s go over all of the things you\'ll need to put your project together.

Learn more about e-sewing basic techniques [here](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing%22).

### You Will Also Need:

- Fabrics (according to your pattern)
- Hot Glue Gun
- Non-Conductive Thread
- Sewing Needles
- Pins
- Sewing Machine
- Scissors
- [Fray Check](https://www.walmart.com/ip/FRAY-CHECK-SEALANT/55211786)
- [Soldering Iron](https://www.sparkfun.com/categories/367) and [Solder](https://www.sparkfun.com/products/9163)
- [Wire Strippers](https://www.sparkfun.com/products/12630)
- [X-Acto Knife](https://www.sparkfun.com/products/9200)
- [Heat Gun](https://www.sparkfun.com/products/10326)
- [Heat Shrink](https://www.sparkfun.com/products/9353)
- White Felt
- Fabric Puff Paint
- [Iron-On Adhesive](http://www.joann.com/heat-n-bond-ultra-hold-iron-on-adhesive-17inx12in/1069806.html)
- [Silicone Flexible Wire](https://www.amazon.com/dp/B0713TCG72/ref=cm_sw_r_cp_ep_dp_zZYcAbHCA5A58)
- Clothing Iron

## Understanding Your Circuit

The LilyPad Safety Scarf is an example of a sewable embedded circuit. For this project, we will use a LilyPad USB Plus from the [LilyPad ProtoSnap Plus](https://www.sparkfun.com/products/14346) and [LilyPad Light Sensor](https://www.sparkfun.com/products/8464) (there is also one included on the ProtoSnap plus that can be used) as well as two [LED Ribbons](https://www.sparkfun.com/products/14139). This project will be powered with an [850 mAh LiPo battery](https://www.sparkfun.com/products/13854).

As expressed in the circuit diagram below, the sewable microcontroller is connected to a sewable light sensor via conductive thread. The light sensor has three connections, VCC, GND, and \'S\'. VCC and GND connect to \'+\' and \'-\', respectively. The \'S\' tab should be connected to pin A2 on the microcontroller.

The LED ribbon will be handled differently. While the ribbon itself can be sewn onto a garment, the electrical leads are not sewable - just traditional wires. Luckily, the LilyPad Sew tabs are also solder friendly. So in this instance, we will solder the LED lead\'s soft, flexible wire to the microcontroller. The datasheet for the LED ribbon indicates that the anode is copper colored (i.e. reddish brown) and the cathode is a silver color (i.e. metallic grey). Connect the anode to pin 11 on the LilyPad USB Plus and the cathode to the GND pin labeled \'-\'.

[![circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/LilyPadProtoSnapPlus_with_Symbols-03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/LilyPadProtoSnapPlus_with_Symbols-03.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

**Heads up!** This circuit does not have a current limiting resistor before the LED ribbon. While the circuit is functional, you may want to consider adding resistor or a transistor like the MOSFET power controller.\
\

[![SparkFun MOSFET Power Controller](https://cdn.sparkfun.com/r/140-140/assets/parts/6/7/9/7/11214-02.jpg)](https://www.sparkfun.com/sparkfun-mosfet-power-controller.html)

### [SparkFun MOSFET Power Controller](https://www.sparkfun.com/sparkfun-mosfet-power-controller.html) 

[ PRT-11214 ]

MOSFETs are awesome. They\'re like a switch that you flip electronically! This SparkFun MOSFET Power Controller makes it easy ...

[ [\$10.95] ]

If you are using the MOSFET power controller, the IN+ is the control pin (i.e. the LilyPad USB Plus\'s pin 11). IN- would be connected to GND. On the other side of the MOSFET power controller, you would be connecting power from the **+** pin to the LilyPad USB Plus\'s **+** pin. Then you would connect the MOSFET power controller\'s **-** pin to the LED\'s **+**. The LED\'s **-** pin would still be connected to ground on the LilyPad USB Plus\'s **-** pin.

## Software Installation 

### Arduino IDE

The LilyPad USB Plus is programmable via the Arduino IDE. If this is your first time using Arduino, please review our tutorial on installing the Arduino IDE.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

March 26, 2013

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

### LilyPad USB Plus and Board Add-On

If this is your first time working with the LilyPad ProtoSnap Plus, you will need to add the board through the boards manager to your program. Please visit the [LilyPad ProtoSnap Plus hookup guide](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-hookup-guide#setting-up-arduino) for detailed instructions on installing drivers and programming a LilyPad via the Arduino IDE.

**Heads up!** The correct selection in the boards manager is the LilyPad USB Plus. The LilyPad USB Arduino is an different version of this board and, if selected, will not upload correctly to the LilyPad USB Plus.

### Arduino Program

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

We have provided the code for this project below. Copy and paste it into your Arduino IDE and then upload it to your board. Make sure you have the correct board selected in the boards manager as well as the port under the port drop down.

    language:c
    //Melissa Felderman for SparkFun Electronics 2017

    //variable for sensor pin
    int sensorPin = A2;

    //variable for light value
    int lightValue;

    //variable for LEDPin
    int LEDPin = 11; 

    void setup()
    
        //if light is high, turn LEDs off
        else 

    }

[![programming](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-17.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-17.jpg)

## Putting It Together

### STEP 1:

Use an X-Acto Knife to cut the fabric around the LEDs back about one inch on one side of both of your LED ribbons.

[![step 1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-01.jpg)

### STEP 2:

This will cause the ribbon to fray at the end.

[![step 2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-02.jpg)

Pull back the wires and use a pair of scissors to cut off the frayed material. Make sure not to cut the LED\'s wires.

[![step 2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-03.jpg)

### STEP 3:

Apply Fray Check to the cut edge of each ribbon, and let it dry (\~15 minutes).

[![step 3](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-04.jpg)

### STEP 4:

[Strip](https://learn.sparkfun.com/tutorials/working-with-wire#how-to-strip-a-wire) the exposed wire of LED strip. Notice one lead has a copper tint and one does not. The copper tinted lead is the anode, or \'+\' lead. For more information about polarity and LEDs, visit our tutorials about [polarity](https://learn.sparkfun.com/tutorials/polarity) and [LEDs](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds).

[![step 4](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-05.jpg)

### STEP 5:

[Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the two LED ribbons together. This can be tricky with the LED ribbons since there is no room to add heat shrink and the frayed wires can easily become crossed. To battle this, I soldered my anodes first and left a little space between the two ribbons. Then, I insulated them with hot glue before soldering the cathodes together. Make sure to insulate the cathode side after soldering them together.

[![step 5](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-06.jpg)

### STEP 6:

Cut a small rectangle of white felt. Fold it over the ribbon to hide the solder connections we just made. Hot glue it in place.

[![step 6](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-07.jpg)

### STEP 7:

You should have one long LED ribbon now. Repeat steps 1-4 on only one end of the new long ribbon. Cut about two 4-5 inch pieces of flexible silicone wire, soldering one to the exposed anode and one to the exposed cathode.

[![step 7](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-10.jpg)

Insulate with heat shrink and then set aside for later.

[![step 7](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-11.jpg)

### STEP 8:

Cut your fabric according to the pattern. We used this lovely and easy to follow [free cowl pattern](https://www.purlsoho.com/create/2014/03/06/corinnes-thread-cozy-sewn-cowl/) by [Purl Soho](https://www.purlsoho.com/).

[![step 8](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-08.jpg)

### STEP 9:

Sew the lining pieces together. Then sew the outer pieces together, but stop before sewing the lining and the outer fabric together. Set the lining aside for later.

[![step 9](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-12.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-12.jpg)

### STEP 10:

Find the \"right side\" of the outer fabric. The right side is the side that will be facing the world when you wear the garment. Grab the LED ribbon, and pin it to the long edge of your outer fabric on the right side. The sew tab should be along the top edge of the fabric with the tube holding the LED strip pointing towards the center of the fabric as seen in the image below.

[![step 10](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-13.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-13.jpg)

### STEP 11:

When you reach the end of your fabric edge, cut the strip to the same length of the fabric.

[![step 11](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-14.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-14.jpg)

### STEP 12:

Add a touch of Fray Check to the edge of LED ribbon that you cut.

[![step 12](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-15.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-15.jpg)

### STEP 13:

Sew the LED ribbon down along the sew tab. Make sure to remove the pins as you go since this can break your sewing machine needle and cause problems with your stitch. When using a sewing machine, be careful to not sew into the LEDs and wires.

[![step 13](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-16.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-16.jpg)

### STEP 14:

Add a dab of hot glue to the bottom of your LilyPad Light Sensor and then place it on the right side of your fabric about an inch below the LED ribbon leads.

[![step 14](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-18.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-18.jpg)

[![step 14](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-19.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-19.jpg)

### STEP 15:

Flip the fabric over to the \"wrong side.\" The wrong side will be the inside of the cowl. Add some hot glue to the bottom of the LilyPad USB Plus and place it down about 1-2 inches below the light sensor (but on the opposite side!)

[![step 15](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-20.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-20.jpg)

[![step 15](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-21.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-21.jpg)

### STEP 16:

Using conductive thread, sew the light sensor to the microcontroller according to the circuit diagram.

[![step 16](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-22.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-22.jpg)

### STEP 17:

Strip the un-soldered side of both flexible silicone wires connected to the LED leads.

[![step 17](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-23.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-23.jpg)

### STEP 18:

Solder the anode (\'+\') lead connection to pin 11 on the LilyPad and the cathode (\'-\') lead to GND on the LilyPad.

[![step 18](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-24.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-24.jpg)

### STEP 19:

Cut a small hole directly above the USB cable connector. Make sure it is large enough to access that port from the opposite side of the fabric.

[![steo 19](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-26.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-26.jpg)

[![step 19](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-27.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-27.jpg)

### STEP 20:

Apply Fray Check around the cut edges of the hole. Make sure that the Fray Check does not get into the USB connector.

[![step 20](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-28.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-28.jpg)

### STEP 21:

Trim the excess conductive thread and test your circuit with a battery. Once everything is working, use some puff paint to insulate the traces on both the right and wrong side of the fabric.

[![step 21](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-29.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-29.jpg)

### STEP 22:

Place your battery on the iron-on adhesive and trace it.

[![step 22](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-30.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-30.jpg)

### STEP 23:

Draw a larger rectangle around the battery\'s trace and leave at least a half inch space between the lines.

[![step 23](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-31.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-31.jpg)

### STEP 24:

Cut along the edge of the larger rectangle, and then cut out the battery tracing as well.

[![step 24](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-32.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-32.jpg)

[![step 24](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-33.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-33.jpg)

### STEP 25:

With the paper side up, iron the iron-on adhesive to a scrap piece of fabric. Then cut the fabric along the edge of the adhesive.

[![step 25](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-34.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-34.jpg)

[![step 25](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-35.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-35.jpg)

### STEP 26:

Peel the paper backing off of the iron-on adhesive.

[![step 26](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-36.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-36.jpg)

### STEP 27:

Plug your battery into the LilyPad\'s JST connector.

[![step 27](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-37.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-37.jpg)

### STEP 28:

Place the piece of fabric with the iron-on adhesive over of the battery. Make sure that the adhesive side is facing down.

[![step 28](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-38.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-38.jpg)

### STEP 29:

Being extremely careful to not touch the battery, and iron over the fabric where there is adhesive in order to make a battery holder.

**CAUTION** Heat should never be applied to directly to the battery. Use extreme caution whith the iron around the battery. If your hand is less steady, make the area around the battery larger, so you have more room between the adhesive and the battery itself. As an alternative, you can also sew the battery holder down.

[![step 29](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-39.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-39.jpg)

### STEP 30:

Finish sewing the scarf according to the pattern.

[![step 30](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-40.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-40.jpg)

### STEP 31:

Use your finger to feel for the ON/OFF switch on the LilyPad and then cut a small hole in the lining fabric to expose it.

[![step 31](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-41.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-41.jpg)

### STEP 32:

Add some Fray Check around the edge of the hole, and let dry.

[![step 32](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/Safety_Scarf-44.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/Safety_Scarf-44.jpg)

### STEP 33:

Turn it on by flipping the switch and enjoy!

[![final product](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/IMG_5340sm.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/IMG_5340sm.jpg)

[![final product](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/IMG_5326sm__1_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/IMG_5326sm__1_.jpg)

[![final products](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/2/IMG_5335sm.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/2/IMG_5335sm.jpg)