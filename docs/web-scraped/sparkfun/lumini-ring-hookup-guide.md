# Source: https://learn.sparkfun.com/tutorials/lumini-ring-hookup-guide

## Introduction

The LuMini rings ([3 inch](https://www.sparkfun.com/products/14965), [2 inch](https://www.sparkfun.com/products/14966), [1 inch](https://www.sparkfun.com/products/14967)) are a great way to add a ring of light to just about anything.

[![SparkFun LuMini LED Ring - 1 Inch (20 x APA102-2020)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/6/3/14967-SparkFun_LuMini_LED_Ring_-_1_Inch__APA102-2020_-01.jpg)](https://www.sparkfun.com/sparkfun-lumini-led-ring-1-inch-20-x-apa102-2020.html)

### [SparkFun LuMini LED Ring - 1 Inch (20 x APA102-2020)](https://www.sparkfun.com/sparkfun-lumini-led-ring-1-inch-20-x-apa102-2020.html) 

[ COM-14967 ]

The one inch version of the SparkFun LuMini LED Ring, packed with 20 individually addressable LEDS, each capable of producing...

[ [\$11.95] ]

[![SparkFun LuMini LED Ring - 2 Inch (40 x APA102-2020)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/6/1/14966-SparkFun_LuMini_LED_Ring_-_2_Inch__APA102-2020_-01.jpg)](https://www.sparkfun.com/sparkfun-lumini-led-ring-2-inch-40-x-apa102-2020.html)

### [SparkFun LuMini LED Ring - 2 Inch (40 x APA102-2020)](https://www.sparkfun.com/sparkfun-lumini-led-ring-2-inch-40-x-apa102-2020.html) 

[ COM-14966 ]

The two inch version of the SparkFun LuMini LED Ring, packed with 40 individually addressable LEDS, each capable of producing...

[ [\$18.95] ]

[![SparkFun LuMini LED Ring - 3 Inch (60 x APA102-2020)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/5/8/14965-SparkFun_LuMini_LED_Ring_-_3_Inch__APA102-2020_-01.jpg)](https://www.sparkfun.com/sparkfun-lumini-led-ring-3-inch-60-x-apa102-2020.html)

### [SparkFun LuMini LED Ring - 3 Inch (60 x APA102-2020)](https://www.sparkfun.com/sparkfun-lumini-led-ring-3-inch-60-x-apa102-2020.html) 

[ COM-14965 ]

The three inch version of the SparkFun LuMini LED Ring, packed with 60 individually addressable LEDS, each capable of produci...

**Retired**

The LuMini line uses the same LED used on our [Lumenati](https://www.sparkfun.com/categories/405) boards, the [APA102](https://www.sparkfun.com/categories/tags/apa102), just in a smaller, 2.0x2.0 mm package. This allows for incredibly tight pixel densities, and thus, a more continuous ring of color. While the LuMini Rings come in different sizes, they all operate in a similar fashion.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Size of a APA102-2020 Package](https://cdn.sparkfun.com/r/300-300/assets/parts/1/2/7/7/8/14608-SMD_LED_-_RGB_APA102-2020__Pack_of_10_-04.jpg)](https://www.sparkfun.com/products/14608)   [![APA102, 5050 Package](https://cdn.sparkfun.com/r/300-300/assets/parts/1/3/1/3/8/14863-SMD_LED_-_RGB_APA102C-5050__Pack_of_10_-03.jpg)](https://www.sparkfun.com/products/14863)
  *Size of a APA102, 2020 Package*                                                                                                                                                             *Size of a APA102, 5050 Package*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Heads up!** The LiMini Rings and Matrix has a different footprint compared to the individual APA102-2020s that are sold in packs of 10 (i.e. COM-14608).

In this tutorial, we\'ll go over how to connect the LuMini rings up to more LuMini rings as well as other APA102 based products. We\'ll check out how to map out a ring of lights in software so we can get a little more creative with circular animations. We\'ll go over some things to consider as you string more and more lights together, and we\'ll also go over some neat lighting patterns to get you away from that standard rainbow pattern (if you have 16 million colors why would you use 255).

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

#### Choosing a Microcontroller

You\'ll need a microcontroller to control everything, however, there\'s a few things to consider when picking one out for the purpose of controlling a whole ton of LED\'s. The first thing is that, although they don\'t have to operate at a specific timing, APA102 LED\'s can transmit data *really, really fast* for LED\'s, like 20 MHz fast. So you should use a microcontroller fast enough to take advantage of this fact. Another thing to consider when you start getting into higher LED counts is the amount of RAM taken up by the LED frame. Each LED takes up 3 bytes of space in RAM, which doesn\'t sound like a lot, but if you\'re controlling 5000 LED\'s, well, you might need something with a bit more RAM than your traditional RedBoard. The below chart outlines the amount of LED\'s where you may start running into memory issues. Keep in mind that these are very generous estimates and will decrease depending on what other global variables are declared.

  **Microcontroller**      **Max LED\'s**   **Clock Speed**
  ------------------------ ---------------- -----------------------------
  SparkFun RedBoard        600              16 MHz
  Arduino Mega 2560        2600             16 MHz
  Pro Micro                700              16 MHz
  SparkFun ESP8266 Thing   27,000           160 MHz
  SparkFun ESP32 Thing     97,000           160 MHz or 240 MHz
  Teensy 3.6               87,000           180 MHz (240 MHz Overclock)

It\'s pretty easy to choose the ESP or Teensy when it comes to stuff like this, as you\'ve got a ton of overhead in clock cycles to run wacky calculations for animations. However, if your project isn\'t all about lights, and you\'re just tossing a LuMini Ring on a project as an indicator, less powerful microcontrollers will suffice. Here are a few [microcontrollers listed from the catalog](https://www.sparkfun.com/categories/300). Depending on the development board, you may need to solder [headers based on your personal preference](https://www.sparkfun.com/categories/381).

[![Pro Micro - 5V/16MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/9/3/2/6/12640-01a.jpg)](https://www.sparkfun.com/pro-micro-5v-16mhz.html)

### [Pro Micro - 5V/16MHz](https://www.sparkfun.com/pro-micro-5v-16mhz.html) 

[ DEV-12640 ]

Here at SparkFun, we refuse to leave \'good enough\' alone. That\'s why we\'re adding to our line-up of Arduino-compatible microc...

[ [\$22.50] ]

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![SparkFun ESP32 Thing](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/5/6/4/13907-01.jpg)](https://www.sparkfun.com/sparkfun-esp32-thing.html)

### [SparkFun ESP32 Thing](https://www.sparkfun.com/sparkfun-esp32-thing.html) 

[ DEV-13907 ]

The SparkFun ESP32 Thing is a comprehensive development platform for Espressif's ESP32, their super-charged version of the ...

[ [\$30.85] ]

[![Arduino Mega 2560 R3](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/3/3/11061-01.jpg)](https://www.sparkfun.com/arduino-mega-2560-r3.html)

### [Arduino Mega 2560 R3](https://www.sparkfun.com/arduino-mega-2560-r3.html) 

[ DEV-11061 ]

Arduino is an open-source physical computing platform based on a simple i/o board and a development environment that implemen...

[ [\$48.40] ]

[![SparkFun ESP8266 Thing - Dev Board (with Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/8/6/13804-01.jpg)](https://www.sparkfun.com/sparkfun-esp8266-thing-dev-board-with-headers.html)

### [SparkFun ESP8266 Thing - Dev Board (with Headers)](https://www.sparkfun.com/sparkfun-esp8266-thing-dev-board-with-headers.html) 

[ WRL-13804 ]

The SparkFun ESP8266 Thing Dev Board with Headers is a dev board that has been designed around the ESP8266, with an integrate...

[ [\$20.25] ]

[![Teensy 3.6 (Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/8/14058-01.jpg)](https://www.sparkfun.com/products/14058)

### [Teensy 3.6 (Headers)](https://www.sparkfun.com/products/14058) 

[ DEV-14058 ]

The Teensy 3.6 is larger, faster and capable of more complex projects, especially with its onboard micro SD card port, ARM Co...

**Retired**

[![SparkFun Thing Plus - ESP32 WROOM](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/9/4/14689-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/products/14689)

### [SparkFun Thing Plus - ESP32 WROOM](https://www.sparkfun.com/products/14689) 

[ WRL-14689 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

**Retired**

#### Selecting a Power Supply

In most cases, your LED installation is gonna pull more than your board can handle (Depending on brightness and animation, anywhere from 100-250 LED\'s can be too much for your board\'s voltage regulator to handle) so you should snag a sweet 5V power supply that\'s got enough wattage in the cottage for all of your LED\'s. Here are a few [5V power supplies listed in our catalog](https://www.sparkfun.com/categories/307). Just make sure to get the appropriate cable and adapter when connecting to your power hungry LEDs.

[![Wall Adapter Power Supply - 5V DC 2A (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/1/12889-01.jpg)](https://www.sparkfun.com/products/12889)

### [Wall Adapter Power Supply - 5V DC 2A (Barrel Jack)](https://www.sparkfun.com/products/12889) 

[ TOL-12889 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA Barrel Jack wall power supply manufactured specifically for S...

**Retired**

[![Mean Well Switching Power Supply - 5VDC, 20A](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/9/7/0/14098-01.jpg)](https://www.sparkfun.com/products/14098)

### [Mean Well Switching Power Supply - 5VDC, 20A](https://www.sparkfun.com/products/14098) 

[ TOL-14098 ]

This is a 100W single output switching power supply from Mean Well. This power supply is extremely reliable and able to outpu...

**Retired**

[![Mean Well LED Switching Power Supply - 5VDC, 5A](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/6/3/14601-Mean_Well_LED_Switching_Power_Supply_5V_25W-01.jpg)](https://www.sparkfun.com/products/14601)

### [Mean Well LED Switching Power Supply - 5VDC, 5A](https://www.sparkfun.com/products/14601) 

[ TOL-14601 ]

This is a 40W single output switching power supply from Mean Well that has been specifically designed to be with LED applicat...

**Retired**

You can either estimate the necessary size of your power supply by taking the amount of LED\'s and multiplying by 60 mA (0.06 A) which is the amount of current it takes to run an LED at full white. This calculation will give you the maximum amount of power your LED\'s could draw, but most of the time, this is a gross overestimate of the amount of power you\'ll actually end up consuming. Instead of calculating, I usually like to test my completed installation on a [benchtop power supply](https://www.sparkfun.com/products/9291) using the brightest animation it\'ll be running, and then add 20 or 30 percent to give myself a little wiggle room if I want to turn the brightness up in the future.

[![Power Supply - 80W DC Switching Mode](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/1/6/09291-1.jpg)](https://www.sparkfun.com/products/9291)

### [Power Supply - 80W DC Switching Mode](https://www.sparkfun.com/products/9291) 

[ TOL-09291 ]

This is an 80W 3-in-1 (3 output ranges) Switching DC Power Supply. Gives a regulated 0-36VDC @ 2.2A, 80W max output. Takes a ...

**Retired**

### Tools

You will need a wire stripper, wire, soldering iron, solder, [general soldering accessories](https://www.sparkfun.com/categories/49). Tweezers are optional if you are soldering the surface mount decoupling capacitor to the back of the board.

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![Tweezers - Curved (ESD Safe)](https://cdn.sparkfun.com/r/140-140/assets/parts/5/2/4/5/10602-01.jpg)](https://www.sparkfun.com/tweezers-curved-esd-safe.html)

### [Tweezers - Curved (ESD Safe)](https://www.sparkfun.com/tweezers-curved-esd-safe.html) 

[ TOL-10602 ]

You can tell by our large assortment of tweezers that we here at SparkFun are way into picking up tiny things. To make sure w...

[ [\$4.75] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

[![Wire Strippers - 20-30AWG](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/0/1/14763-Wire_Strippers_-_758PL0066-03.jpg)](https://www.sparkfun.com/products/14763)

### [Wire Strippers - 20-30AWG](https://www.sparkfun.com/products/14763) 

[ TOL-14763 ]

These are high grade wire strippers from Techni-Tool with a curved grip making them an affordable option if you need to remov...

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/light)

### Light 

Light is a useful tool for the electrical engineer. Understanding how light relates to electronics is a fundamental skill for many projects.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

[](https://learn.sparkfun.com/tutorials/electric-power)

### Electric Power 

An overview of electric power, the rate of energy transfer. We\'ll talk definition of power, watts, equations, and power ratings. 1.21 gigawatts of tutorial fun!

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

## Hardware Overview

### I/O Pins

The LuMini rings are powered and controlled using a few pads on the back of each board. Each board has a set of pads for **5V** and ground, a set of pads for data and clock input, and a set of pads for data and clock output. These pads are outlined in the below image.

[![I/O Pads](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/1/pads.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/1/pads.png)

*I/O Pads*

### Decoupling Capacitor Pads

In larger installations you may need to add a decoupling capacitor between power and ground to prevent voltage dips when turning on a whole bunch of LED\'s simultaneously. The spot to add this optional capacitor is outlined below.

[![Capacitor Pads](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/1/cap.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/1/cap.png)

*Capacitor Pads*

We\'d recommend the surface mount [4.7 µF capacitor](https://www.sparkfun.com/products/15169) that is shown below. If you\'ve never done surface mount soldering before, this part might be a little tricky, but check out our [SMD tips and tricks](https://www.sparkfun.com/news/2233) on doing just that.

[![Capacitor 4.7uF - SMD (Strip of 10)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/5/6/2/15169-Capacitor_4.7uF_SMD__strip_of_10_-01.jpg)](https://www.sparkfun.com/products/15169)

### [Capacitor 4.7uF - SMD (Strip of 10)](https://www.sparkfun.com/products/15169) 

[ COM-15169 ]

This is 10 pack of tiny 4.7µF SMD decoupling capacitors. Each of these caps offers a DC voltage rating of 16V and a capacita...

**Retired**

### LED Numbers

Looking at the back of each ring, you\'ll also see some numbers. Since the ring acts like a string of LEDs, these numbers correspond to the LED number in the string. Note that, like the led array, we index at LED 0, so calling `leds[5]` will correspond to the LED on the opposite side of the **5** labeling.

[![LED Numbers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/1/nums.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/1/nums.png)

*LED Numbers*

[] **Warning!** We\'ve found that setting the global brightness using the FastLED Library to `32` is good for testing, as it\'s a little easier on the eyes. However, turning the brightness up all the way and leaving all LED\'s on white will result in damage to your ring! Be careful to make sure your animations don\'t run too hot, and if they do, you can always lower the brightness.

## Hardware Assembly

### Soldering to the LuMini Rings

[Soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) wires to the pads on the LuMini rings is pretty simple. The trick is simply to pre-solder both the pad and [stripped wire](https://learn.sparkfun.com/tutorials/working-with-wire#how-to-strip-a-wire) before attempting to solder the two together. Then, press the wire onto the pad and solder away! Check out the below GIF if you\'re a little confused.

[![Soldering](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/1/SparkFun_LuMini_LED_Ring_1.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/1/SparkFun_LuMini_LED_Ring_1.gif)

*Soldering to the LuMini Ring*

### Choosing Pins

The APA102 LED is controlled on an SPI-like protocol, so it\'s generally good practice to connect **`CI`** to **`SCLK`** on your microcontroller, and connect **`DI`** to **`MOSI`**. However, This setup isn\'t required, and you can connect data and clock up to most pins on your microcontroller. Go ahead and determine which pins you will use, and solder your Data (**`DI`**) and Clock (**`CI`**) lines into your microcontroller.

Now that we know how to solder to these pads, we can start making a chain of LuMini rings, or even chain them to other APA102 based products. To do this, all we\'ll need to do is solder **`CO`** and **`DO`** of one ring to the **`CI`** and **`DI`** of the next ring. The below image has the output of a 1 inch ring connected to the input of a 3 inch ring.

[![Chained Rings](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/1/SparkFun_LuMini_LED_Ring-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/1/SparkFun_LuMini_LED_Ring-03.jpg)

*Chained Rings*

## Software Installation

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

We\'ll be leveraging the ever popular **FastLED** library to control our LuMini rings. You can obtain these libraries through the Arduino Library Manager. Search for **FastLED** to install the latest version. If you prefer downloading the libraries manually, you can also grap them from the [GitHub Repository](https://github.com/FastLED/FastLED):

[DOWNLOAD THE FASTLED LIBRARY (ZIP)](https://github.com/FastLED/FastLED/archive/master.zip)

## Light It Up

SparkFun has also written some example code specific to the rings to get you started. These example sketches can be found in the [LuMini 3-Inch GitHub Repo under Firmware](https://github.com/sparkfun/LuMini_3_Inch/tree/master/Firmware). To download, click on the button below.

[DOWNLOAD THE EXAMPLE SKETCHES (ZIP)](https://github.com/sparkfun/LuMini_3_Inch/archive/master.zip)

Make sure to adjust the pin definition depending on how you connected the LEDs to your microcontroller.

### Example 1 \-\-- Ring Test

Glen Larson invented the Larson Scanner as an LED effect for the TV series [Knight Rider](https://en.wikipedia.org/wiki/Knight_Rider_(1982_TV_series)). In this example, we\'ll reproduce it, only we\'ll add in some color for good measure. The Larson Scanner is a great and colorful way to test all of your LEDs on your ring. We\'ll first begin by creating an object for our ring. Simply uncomment the proper number of LED\'s for your ring of choice. For these examples, we\'ll be using the 3 inch ring.

    language:c
    #include <FastLED.h>

    // How many leds in your strip? Uncomment the corresponding line
    #define NUM_LEDS 60 //3 Inch
    //#define NUM_LEDS 40 //2 Inch
    //#define NUM_LEDS 20 //1 Inch

    // The LuMini rings need two data pins connected
    #define DATA_PIN 16
    #define CLOCK_PIN 17

    // Define the array of leds
    CRGB ring[NUM_LEDS];

We\'ll then initialize a ring using the `.addLeds` function below. Notice the **BGR** in this statement, this is the color order, sometimes, the manufacturer will change the order in which the received data is put into the PWM registers, so you\'ll have to change your color order to match. The particular chipset we\'re using is **`BGR`**, but this could change in the future. We\'ll also set the global brightness to `32`.

    language:c
    void setup() 

[] **Warning!** We\'ve found that setting the global brightness using the FastLED Library to `32` is good for testing, as it\'s a little easier on the eyes. However, turning the brightness up all the way and leaving all LED\'s on white will result in damage to your ring! Be careful to make sure your animations don\'t run too hot, and if they do, you can always lower the brightness.

Our animation is then contained in the `fadeAll()` function, which loops through every LED and fades it to a percentage of it\'s previous brightness. Our `loop()` then set\'s an LED to a hue, increments the hue, and then shows our LEDs. After this, we use the `fadeAll()` function to fade our LED\'s down so they don\'t all end up being on.

    lanuage:c
    void fadeAll() 
    }

    void loop() 
    }

Your code should look like the GIF below if you\'ve hooked everything up right. If thing\'s aren\'t quite what you\'d expect, double check your wiring.

[![Example 1 Output](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/1/SparkFun_LuMini_LED_Ring_A.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/1/SparkFun_LuMini_LED_Ring_A.gif)

*Example 1 Output*

### Example 2 \-\-- RGB Color Picker

In this second example, we\'ll use the serial terminal to control the color displayed by the ring. We initialize everything in the same way. We then listen for data on the serial port, parsing integers that are sent from the serial terminal on your desktop and putting them in the corresponding color (red, green or blue). The code to accomplish this is shown below.

    language:c
    #include <FastLED.h>

    // How many leds in your strip?
    #define NUM_LEDS 60 //3 Inch
    //#define NUM_LEDS 40 //2 Inch
    //#define NUM_LEDS 20 //1 Inch

    //Data and Clock Pins
    #define DATA_PIN 16
    #define CLOCK_PIN 17

    CRGB color;
    char colorToEdit;

    // Define the array of leds
    CRGB ring[NUM_LEDS];

    void setup() 

    void loop()
    
        //Display our current color data
        Serial.print("Red Value: ");
        Serial.println(color[0]);
        Serial.print("Green Value: ");
        Serial.println(color[1]);
        Serial.print("Blue Value: ");
        Serial.println(color[2]);
        Serial.println();
        for (int i = 0; i < NUM_LEDS; i++)
        
      }
    }

Go ahead and upload this code, then open your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) to **115200**. It should be displaying the current color value (R:0, G:0, B:0), if not.

[![RGB Color Picker](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/1/EX2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/1/EX2.PNG)

Changing the value of a color is done be sending the letter of the color (R, G, or B) followed by a value between 0 and 255. For instance, turning **red** to half brightness would be achieved by sending **`R127`**. Play around and look for your favorite color.

### Example 3 \-\-- HSV Color Picker

The third example is very similar to the first in that we are picking colors using the serial terminal. However, in this example, we are working with an [HSV color space.](https://en.wikipedia.org/wiki/HSL_and_HSV) This sketch works mostly the same as the previous one, only we send `h`, `s` or `v` instead of `r`, `g` or `b`. Upload the below code and play around in search of your favorite color.

    language:c
    #include <FastLED.h>

    // How many leds in your strip?
    #define NUM_LEDS 60 //3 Inch
    //#define NUM_LEDS 40 //2 Inch
    //#define NUM_LEDS 20 //1 Inch

    //Data and Clock Pins
    #define DATA_PIN 16
    #define CLOCK_PIN 17

    CHSV color = CHSV(0, 255, 255);
    char colorToEdit;

    // Define the array of leds
    CRGB ring[NUM_LEDS];

    void setup() 

    void loop()
    
        //Display our current color data
        Serial.print("Hue: ");
        Serial.println(color.hue);
        Serial.print("Saturation: ");
        Serial.println(color.sat);
        Serial.print("Value: ");
        Serial.println(color.val);
        Serial.println();

        for (int i = 0; i < NUM_LEDS; i++)
        
      }
    }

Once again, play around to try and find your favorite color. I find that HSV is a much more intuitive space to work in than RGB space.

### Example 4 \-\-- Angle Assignment

In this example, we\'ll assign the LED\'s in our circle to the angles of the [unit circle](https://en.wikipedia.org/wiki/Unit_circle) so we won\'t have to think about which LED corresponds to which angle. We\'re also going to use 0-255 instead of 0-360, as this makes more sense from a computer standpoint. For example, the LED\'s at 90° would be accessed by calling `ringMap[64]`. This is accomplished using the `populateMap()` function, which populates the `uint8_t ringMap[255]` object. The `populateMap()` function is shown below and gets called in our `setup()` loop.

    language:c
    #include <FastLED.h>

    // How many leds in your strip?
    #define NUM_LEDS 60 //3 Inch
    //#define NUM_LEDS 40 //2 Inch
    //#define NUM_LEDS 20 //1 Inch

    //Data and Clock Pins
    #define DATA_PIN 16
    #define CLOCK_PIN 17

    // Define the array of leds
    CRGB ring[NUM_LEDS];
    uint8_t ringMap[255];
    uint8_t rotation = 0;

    float angleRangePerLED = 256.0 / NUM_LEDS; //A single LED will take up a space this many degrees wide.

    void populateMap () //we map LED's to a 360 degree circle where 360 == 255
    
      }
    }

    void fadeAll(uint8_t scale = 250)
    
    }

    void setup()
    

In our loop, we\'ll map each angle of the circle to a hue, then we\'ll light up 3 pixels, each separated by 120° We do this by lighting an LED at a starting angle 0, then add 120° which corresponds to 85.333 ((120/360)\*255 = 85.333) and light the LED at this angle. We repeat the same process to light the final LED. Each angle is matched to a hue, so we should see the same colors in each position.

    language:c
    void loop()
    
      FastLED.show();
      rotation++;
      fadeAll(248);
      delay(5);
    }

Notice how `ringMap[angle]` is called within `ring`, as it will return the LED number at that angle. Uploading this code should look similar to the below GIF

[![Example 4 Output](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/1/SparkFun_LuMini_LED_Ring_B.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/1/SparkFun_LuMini_LED_Ring_B.gif)

*Example 4 Output*

### Example 5 \-\-- Using Gradients

In this final example, we\'ll leverage FastLED\'s palette object (**`CRGBPalette16`**) to create and visualize a color palette on our ring. We have much the same initialization as our previous examples, only this time we also initialize a `CRGBPalette16` object which will be full of colors along with a `TBlendType` which will tell us whether or not to blend the colors together or not. This can be either `LINEARBLEND` or `NOBLEND`. To populate this gradient, we use examples 2 and 3 to find the colors we want to put into our gradient. The gradient included is a bunch of colors created in HSV space, but you can easily change to RGB space if you prefer. You can also use any of the preset palettes by uncommenting the line that sets it equal to `currentPalette`.

    language:c
    TBlendType    currentBlending = LINEARBLEND;
    CRGBPalette16 currentPalette = ;

    //currentPalette = RainbowColors_p;
    //currentPalette = RainbowStripeColors_p;
    //currentPalette = OceanColors_p;
    //currentPalette = CloudColors_p;
    //currentPalette = LavaColors_p;
    //currentPalette = ForestColors_;
    //currentPalette = PartyColors_p;

We then use the `ColorFromPalette` function to put the colors from our gradient onto our LED ring. Notice how we use the angle functions once again to map each part of the gradient to an angle.

    language:c
    void loop() 
      FastLED.show();
      rotation++;
      delay(20);
    }

Play around with the colors in your palette until you\'re satisfied. If all is hooked up correctly your ring should look something like the below GIF.

[![Example 5 Output](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/1/SparkFun_LuMini_LED_Ring_C.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/1/SparkFun_LuMini_LED_Ring_C.gif)

*Example 5 Output*

### Additional Examples

There are quite a few additional examples contained in the FastLED library. While they aren\'t made specifically for the rings, they can still show you some useful features in the FastLED library, and may give you some ideas for some animations of your own.

[GitHub: FastLED \> Examples](https://github.com/FastLED/FastLED/tree/master/examples)

If the FastLED library is installed, they can be found from the Arduino IDE menu by opening up **File** -\> **Examples** -\> **Examples From Custom Libraries** -\> **FastLED** .