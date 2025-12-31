# Source: https://learn.sparkfun.com/tutorials/non-addressable-rgb-led-strip-hookup-guide

## Introduction 

**Note:** This tutorial is to control the 12V non-addressable RGB LED strips. If you are using an addressable LED strip (i.e. [WS2812](https://learn.sparkfun.com/tutorials/ws2812-breakout-hookup-guide) or [APA102](https://learn.sparkfun.com/tutorials/apa102-addressable-led-hookup-guide)), you will need to use a different power supply and a micrcontroller to control the LEDs.

Add color to your projects with the non-addressable LED strips! These are perfect if you want to add uniform lighting for your props, car, fish tank, or perhaps under cabinet lighting in your home.

[![LED RGB Strip - Bare (1m)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/4/9/12021-01.jpg)](https://www.sparkfun.com/led-rgb-strip-bare-1m.html)

### [LED RGB Strip - Bare (1m)](https://www.sparkfun.com/led-rgb-strip-bare-1m.html) 

[ COM-12021 ]

These are bare non-addressable 1 meter long RGB LED strips that come packed with 60 5060 LEDs per meter. As these are bare LE...

[ [\$15.95] ]

[![LED RGB Strip - Bare (5m)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/5/0/12022.jpg)](https://www.sparkfun.com/products/12022)

### [LED RGB Strip - Bare (5m)](https://www.sparkfun.com/products/12022) 

[ COM-12022 ]

These are bare non-addressable 5 meter long RGB LED strips that come packed with 60 5060 LEDs per meter, that\'s 300 LEDs. As ...

**Retired**

[![LED RGB Strip - Sealed (1m)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/5/1/12023.jpg)](https://www.sparkfun.com/products/12023)

### [LED RGB Strip - Sealed (1m)](https://www.sparkfun.com/products/12023) 

[ COM-12023 ]

Gone are the days that you have to worry about silicone weather proofing splitting and breaking on you! These are sealed non-...

**Retired**

[![LED RGB Strip - Sealed (5m)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/5/2/12024-01.jpg)](https://www.sparkfun.com/products/12024)

### [LED RGB Strip - Sealed (5m)](https://www.sparkfun.com/products/12024) 

[ COM-12024 ]

Gone are the days that you have to worry about silicone water proofing splitting and breaking on you! These are sealed non-ad...

**Retired**

### Required Materials

To follow along with this tutorial, you will need the following materials. The partial wishlist on the left is for a basic connection with an Arduino. It does not include the potentiometer and buttons. The full wishlist on the right is for the full circuit for additional functionality. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

#### Microcontroller

To make the most out of your LED strip, you will need a microcontroller. The easiest would be to use the RedBoard Qwiic but you can use any Arduino microcontroller as long as it has a minimum of three PWM pins.

[![Arduino Pro Mini 328 - 3.3V/8MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/4/0/11114-01.jpg)](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html)

### [Arduino Pro Mini 328 - 3.3V/8MHz](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html) 

[ DEV-11114 ]

SparkFun\'s minimal design approach to Arduino. This is a 3.3V Arduino running the 8MHz bootloader.

[ [\$11.25] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

#### Power Supply

To power your LEDs, you will need a 12V power supply. The amount of current needed depends on the length and density of the LED strip. Below are a few options if you are powering the LEDs from a wall outlet in an installation. You could also use a 9V power supply. It may not be as bright but your LED strip will not be as hot.

[![Wall Adapter Power Supply - 12VDC, 600mA (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/6/TOL-15313-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-12vdc-600ma-barrel-jack.html)

### [Wall Adapter Power Supply - 12VDC, 600mA (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-12vdc-600ma-barrel-jack.html) 

[ TOL-15313 ]

This is a high quality AC to DC \'wall wart\' which produces a regulated output of 12VDC at up to 600mA.

[ [\$9.25] ]

[![SparkFun ATX Power Connector Breakout Kit - 12V/5V (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/5/0/15701-SparkFun_ATX_Power_Connector_Breakout_Kit_-_12V_5V__4-pin_-01.jpg)](https://www.sparkfun.com/products/15701)

### [SparkFun ATX Power Connector Breakout Kit - 12V/5V (4-pin)](https://www.sparkfun.com/products/15701) 

[ KIT-15701 ]

The ATX power connector breaks out the standard 4-pin computer peripheral port for you 12V & 5V devices from one wall adapter...

**Retired**

#### Wires and Connectors

The stranded wires from the non-addressable do not have a connector. For prototyping you could use alligator clips with male headers. However, it would be easier to use a polarized connector like the ones from the 4-wire pigtail connector to easily connect and disconnect from your controller.

[![Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/2/0/11375-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html)

### [Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html) 

[ PRT-11375 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of stranded wire in a cardboard dispens...

[ [\$23.95] ]

[![LED Strip Pigtail Connector (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/2/1/14576-LED_Pigtail_connector_4_Pin_-01.jpg)](https://www.sparkfun.com/led-strip-pigtail-connector-4-pin.html)

### [LED Strip Pigtail Connector (4-pin)](https://www.sparkfun.com/led-strip-pigtail-connector-4-pin.html) 

[ CAB-14576 ]

These 4-pin JST-SM pigtail connectors mate perfectly with LED strips and other applications that require only two lines and a...

[ [\$1.95] ]

[![Alligator Clip with Pigtail (10 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/6/5/14303-Alligator_Clip_with_Pigtail__10_Pack_-01.jpg)](https://www.sparkfun.com/alligator-clip-with-pigtail-10-pack.html)

### [Alligator Clip with Pigtail (10 Pack)](https://www.sparkfun.com/alligator-clip-with-pigtail-10-pack.html) 

[ CAB-14303 ]

This is a 10-pack of wires that are pre-terminated with an alligator clip on one end and a male header on the other.

[ [\$9.25] ]

#### Transistors

If you are using a microcontroller to control the strip, you will need transistors to control each channel. For small lengths, you could use NPN transistors. For longer lengths, you could use n-channel mosfets. Just make sure to get the associated resistors depending on your transistor.

[![Transistor - NPN, 60V 200mA (2N3904)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/9/00521-1.jpg)](https://www.sparkfun.com/transistor-npn-60v-200ma-2n3904.html)

### [Transistor - NPN, 60V 200mA (2N3904)](https://www.sparkfun.com/transistor-npn-60v-200ma-2n3904.html) 

[ COM-00521 ]

These are very common, high quality BJT NPN transistors made by ST Micro.

[ [\$0.55] ]

[![Transistor - NPN, 60V 4A (2N5192G) ](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/0/0/6/13951-Transistor_-_NPN__80V_4A__TO225AA_-01.jpg)](https://www.sparkfun.com/transistor-npn-60v-4a-2n5192g.html)

### [Transistor - NPN, 60V 4A (2N5192G) ](https://www.sparkfun.com/transistor-npn-60v-4a-2n5192g.html) 

[ COM-13951 ]

This is the 2N5192G, an NPN silicon transistor. This little transistor can help in your project by being used to help drive l...

[ [\$1.05] ]

[![N-Channel MOSFET 60V 30A](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/5/10213-01.jpg)](https://www.sparkfun.com/n-channel-mosfet-60v-30a.html)

### [N-Channel MOSFET 60V 30A](https://www.sparkfun.com/n-channel-mosfet-60v-30a.html) 

[ COM-10213 ]

This part is no longer available. The recommended replacement is \[here\](https://www.sparkfun.com/products/24144). If you\'v...

**Retired**

[![SparkFun MOSFET Power Control Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/9/8/9/2/12959-01.jpg)](https://www.sparkfun.com/sparkfun-mosfet-power-control-kit.html)

### [SparkFun MOSFET Power Control Kit](https://www.sparkfun.com/sparkfun-mosfet-power-control-kit.html) 

[ COM-12959 ]

This is the SparkFun MOSFET Power Control Kit, a breakout PTH soldering kit for for the \[RFP30N06LE\](http://www.sparkfun.com/...

**Retired**

### Input

For options to adjust the color and brightness of your LED strip, you could use the following with a microcontroller.

[![Trimpot 10K Ohm with Knob](https://cdn.sparkfun.com/r/140-140/assets/parts/3/8/2/3/09806-01.jpg)](https://www.sparkfun.com/trimpot-10k-ohm-with-knob.html)

### [Trimpot 10K Ohm with Knob](https://www.sparkfun.com/trimpot-10k-ohm-with-knob.html) 

[ COM-09806 ]

This 10K trimmable potentiometer has a small knob built right in and it\'s breadboard friendly to boot!

[ [\$1.25] ]

[![Multicolor Buttons - 4-pack](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/1/8/14460-01.jpg)](https://www.sparkfun.com/multicolor-buttons-4-pack.html)

### [Multicolor Buttons - 4-pack](https://www.sparkfun.com/multicolor-buttons-4-pack.html) 

[ PRT-14460 ]

This is a simple 4-pack of momentary, multicolor buttons, great for all sorts of projects! Unlike previous iterations of mult...

[ [\$1.95] ]

### Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49). You may also need some wire strippers if you are cutting and reusing parts of the strip.

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Wire Strippers - 22-30AWG](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/0/0/14762-Wire_Strippers-03.jpg)](https://www.sparkfun.com/products/14762)

### [Wire Strippers - 22-30AWG](https://www.sparkfun.com/products/14762) 

[ TOL-14762 ]

These are your basic, run-of-the-mill wire strippers from Techni-Tool with a comfortable grip making them an affordable optio...

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing. If you are looking to customize the control by programming a microcontroller, we recommend looking at the SparkFun Inventor\'s Kit for Arduino.

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

[](https://learn.sparkfun.com/tutorials/led-light-bar-hookup)

### LED Light Bar Hookup 

A quick overview of SparkFun\'s LED light bars, and some examples to show how to hook them up.

[](https://learn.sparkfun.com/tutorials/transistors)

### Transistors 

A crash course in bi-polar junction transistors. Learn how transistors work and in which circuits we use them.

[](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v41)

### SparkFun Inventor\'s Kit Experiment Guide - v4.1 

The SparkFun Inventor\'s Kit (SIK) Experiment Guide contains all of the information needed to build all five projects, encompassing 16 circuits, in the latest version of the kit, v4.1.2 and v4.1.

## Hardware Overview 

The non-addressable RGB LED strips are also referred to as analog LED strips. Each channel has three LEDs wired in series with a current limiting resistor. Each segment contains three common anode RGB LED ICs that are connected in parallel. These are used more on strips. While these operate at **12V**, they can also light up with **9V**.

[![Schematic of Analog RGB LED Strip](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Non-Addressable-Analog-RGB-LED-Strip_schematic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Non-Addressable-Analog-RGB-LED-Strip_schematic.jpg)

**Note:** For more information, check out this forum post in Stack Exchange!\
\

[Stack Exchange \| Electrical Engineering:\
Why are most RGB LED Strips Common Anode instead of Common Cathode?](https://electronics.stackexchange.com/questions/106810/why-are-most-rgb-led-strips-common-anode-instead-of-common-cathode)

## Hardware Hookup

We\'ll be using a common anode RGB LED strip. There are a few methods of lighting the LED strip:

- straight power
- 555 Timer
- pre-programmed controller box
- microcontroller/single board computer

Below are three of these methods. For the scope of this tutorial, we will be using the third circuit diagram.

### Hookup 1: Straight Power!

**⚡ Note:** While the LED strip is labeled 12V, a 9V power supply was used so that the LEDs were not overwhelmingly bright. At 9V, it also did not dissipate as much heat.

The simplest method of using non-addressable LEDs to illuminate your project is to add power to your LED strip. You will just need to make a connection between the female barrel jack adapter and the non-addressable LED strip. Simply insert the black wire connecting the \"**12V**\" pin to the \"**+**\" of the barrel jack adapter\'s screw terminal for power. Then insert the wire or your choice into the \"**-**\" screw terminal. In the following hookup, all channels were connected to ground to mix the color of white.

[![Fritzing Diagram for Adapter and LED Strip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/0/Non_Addressable_LED_Strip_Simple_bb_Fritzing.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/Non_Addressable_LED_Strip_Simple_bb_Fritzing.png)

*Click the image for a closer look.*

**Note:** When testing the non-addressable LED strip, the pin labeled \"G\" was actually blue and the \"B\" was actually green. Depending on the manufacturer, the label may vary. Try testing the LED strip out with a power supply to determine if the letter represents the color.

Depending on your project and color that you are illuminating, you will need to ground each respective channel. Here are some [basic colors](https://en.wikipedia.org/wiki/Additive_color) that you could mix by grounding different pins. The tradeoff is that you are limited to seven colors and will need to adjust the connection every time you need to change the color. For projects that do not require that many colors, this would be the best setup.

[![Basic Color Mixing](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/0/RGB_ColorMix.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/0/RGB_ColorMix.jpg)

**Note:** Instead of disconnecting and reconnecting each wire, try adding a [switch](https://learn.sparkfun.com/tutorials/switch-basics) between each channel to mix colors. Just make sure the switch is rated appropriately.

### Hookup 2: Preprogrammed Controller Box

For those that are interested in a preprogrammed controller to easily control the non-addressable LED strip with a controller, you could use the Mi-Light remote and controller box. You will simply need to connect power through the barrel jack and tighten the screws for each channel. The controller box includes an additional \"white\" channel for LED strips with that have an the color.

[![Mi-Light 4-Zone LED Remote Controller](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/9/2/0/14711-Mi-Light_4-Zone_LED_Remote_Controller-01.jpg)](https://www.sparkfun.com/products/14711)

### [Mi-Light 4-Zone LED Remote Controller](https://www.sparkfun.com/products/14711) 

[ COM-14711 ]

The Mi-Light Remote Control is a 2.4GHz RF LED accessory that can change the color and dim non-addressable LED strips attache...

**Retired**

[![Mi-Light RGBW LED Controller Box](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/9/1/9/14710-Mi-Light_4-Zone_LED_Controller_Box_-01.jpg)](https://www.sparkfun.com/products/14710)

### [Mi-Light RGBW LED Controller Box](https://www.sparkfun.com/products/14710) 

[ COM-14710 ]

The Mi-Light LED Controller Box is a 2.4GHz RF LED accessory that enables your non-addressable LED strips to change color, di...

**Retired**

For more information, check out the video below!

### Hookup 3: Microcontroller

For those that want a little bit more flexibility and control over the LEDs, you can use a microcontroller. We\'ll be using a RedBoard Qwiic with the ATmega328P. You can use different microcontollers (i.e. AVR, ARM, micro:bit, ESP8266, ESP32, etc.) or single board computer (i.e. Raspberry Pi) as long as it can output a PWM signal. You just need a [transistor](https://learn.sparkfun.com/tutorials/transistors#applications-i-switches) since the [logic level](https://learn.sparkfun.com/tutorials/logic-levels) is lower than the voltage of the LED strip and the pins are not able to source enough current. The code (i.e. MakeCode, Python, etc.) depends on the microcontroller or single board computer. For the scope of the tutorial, we will be using the Arduino language to control the LEDs.

**Heads up!** Single board computers like the Raspberry Pi are limited in the number of PWM pins. If you are using a single board computer, you would probably need a dedicated PWM chip or DAC to control all three channels of the RGB LED strip. You could also try to use software PWM on a Pi.

Typically for common anode RGB LED strips, you could use NPN BJTs or N-channel MOSFETs as a switch. N-channel mosfets usually can handle more power and they are more power efficient. Therefore, we\'ll be adding the load on the high side. Each color channel requires a transistor to switch. The hookup diagram for a basic connection is shown on the left. For additional functionality, you could add buttons and a potentiometer to control the LEDs. For testing purposes, we\'ll use a breadboard, jumper wires, and alligator clips to connect. You\'ll eventually want to solder the LED strip to header pins, a prototyping board, or splice a 4-pin pigtail connector for a secure connection when using it in an installation.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Basic Arduino Hookup w/ N-Channel MOSFETS](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/1/Arduino_Analog_RGB_LED_Strip_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Arduino_Analog_RGB_LED_Strip_Fritzing_bb.jpg)   [![Buttons and Potentiometers Added for Additional Functionality](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/1/Arduino_Analog_RGB_LED_Strip_Fritzing_Buttons_Pot_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Arduino_Analog_RGB_LED_Strip_Fritzing_Buttons_Pot_bb.jpg)
  *Basic Arduino Hookup w/ N Channel MOSFETS*                                                                                                                                                                                                                        *Buttons and Potentiometers Added for Additional Functionality*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Click image for a closer look*

**Note:** If you are using small lengths of the RGB LED strip, you can also use NPN transistors as long as you are not exceeding the maximum current rating for the transistor. The following diagrams in this note used NPN transistors had pins from the left that were arranged as CBE with respect to the flat side facing you.\
\

Click to See Circuit Using NPN Transistor

\

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Basic Arduino Hookup w/ NPN Transistor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/1/Arduino_Analog_RGB_LED_Strip_Fritzing_NPN_Transistor_bb-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Arduino_Analog_RGB_LED_Strip_Fritzing_NPN_Transistor_bb-1.jpg)   [![Buttons and Potentiometers Added for Additional Functionality](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/1/Arduino_Analog_RGB_LED_Strip_Fritzing_Buttons_Pot_NPN_Transistor_bb-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Arduino_Analog_RGB_LED_Strip_Fritzing_Buttons_Pot_NPN_Transistor_bb-1.jpg)
  *Basic Arduino Hookup w/ NPN Transistor*                                                                                                                                                                                                                                                          *Buttons and Potentiometers Added for Additional Functionality*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By using a PWM output from a microcontroller and transistor to adjust the brightness of each color channel individually, the RGB LED can display almost any color you choose! For simplicity, we\'ll limit the colors to twelve colors and white on an Arduino. The following values in the diagram will create the primary, secondary, and tertiary colors.

[![Primary, secondary, and teriary colors with Arduino](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/0/TertiaryColorWheel_Chart.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/0/TertiaryColorWheel_Chart.png)

When using long strands, it is recommended to have a separate power supply for the Arduino and LEDs. Your setup should look similar to the image below on a breadboard if you are using a [12V/5V, 2A power supply](https://learn.sparkfun.com/tutorials/12v5v-power-supply-hookup-guide) and a 5M LED strip. The setup is the same except VIN is disconnected on the 12V. The Arduino is using its own 5V power. When programming the Arduino, it is recommended to disconnect the 5V pin so that you do not have conflicting power sources.

[![12V/5V power supply and a USB cable connected to an Arduino and the Non-Addressable RGB LED Strip ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/1/Non-Addressable_RGB_LED_Strip_Breadboard_Arduino_2_Power_Sources.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Non-Addressable_RGB_LED_Strip_Breadboard_Arduino_2_Power_Sources.jpg)

After you are done programming, you can remove the USB cable and connect the 12V/5V power supply\'s 5V pin to the circuit.

[![12V/5V power supply connected to an Arduino and the Non-Addressable RGB LED Strip when powering the board Remotely in an Installation](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/1/Non-Addressable_RGB_LED_Strip_Breadboard_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Non-Addressable_RGB_LED_Strip_Breadboard_Arduino.jpg)

## Arduino Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

To follow along, check out the [GitHub repository](https://github.com/sparkfun/Non-Addressable_RGB_LED_Strip_Code). There are five examples in the repo. Two of which are simple examples to turn on a certain color based on the type of LED that you are using. We\'ll go over the other three examples.

[Download GitHub Code Repo (ZIP)](https://github.com/sparkfun/Non-Addressable_RGB_LED_Strip_Code/archive/master.zip)

The three examples from this GitHub Repo that we will go over are listed below. Click on one of the links below to jump to the example!

- [Custom Color Cycling](https://learn.sparkfun.com/tutorials/non-addressable-rgb-led-strip-hookup-guide#custom_color_cycling)
- [Fading](https://learn.sparkfun.com/tutorials/non-addressable-rgb-led-strip-hookup-guide#fading)
- [Full Demo](https://learn.sparkfun.com/tutorials/non-addressable-rgb-led-strip-hookup-guide#full_demo)\

**Note:** While the example code included in the tutorial was written for analog LED strips, this can also work for individual common anode LEDs, common cathode LEDs, and high power RGB LEDs as well!\
\

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Clear Common Anode RGB LED- 5mm](https://cdn.sparkfun.com/assets/home_page_posts/3/2/4/7/10820-03-L_RGB_Clear_Common_Anode_LED-5mm.jpg)](https://www.sparkfun.com/products/10820)   [![Diffused Common Cathode RGB LED- 10mm](https://cdn.sparkfun.com/assets/home_page_posts/3/2/4/7/11120-01a-LED_RGB_Diffused_Common_Cathode-10mm.jpg)](https://www.sparkfun.com/products/11120)   [![SMD Common Cathode RGB LED on a Sewable PCB](https://cdn.sparkfun.com/assets/home_page_posts/3/2/4/7/13735-LilyPad_Tri-Color_RGB_Common_Cathode_LED-01b.jpg)](https://www.sparkfun.com/products/13735)   [![High Power RGB LED on a PCB](https://cdn.sparkfun.com/assets/home_page_posts/3/2/4/7/15200-Triple_Output_High_Power_RGB_LED-01.jpg)](https://www.sparkfun.com/products/15200)
  *Clear Common Anode RGB LED- 5mm*                                                                                                                                                      *Diffused Common Cathode RGB LED- 10mm*                                                                                                                                                           *SMD Common Cathode RGB LED on a Sewable PCB*                                                                                                                                                               *High Power RGB LED on a PCB*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Just make sure to check the datasheet to verify that there are channels for each color and include the appropriate parts if you are connecting them to a microcontroller.

------------------------------------------------------------------------

### [][Example 1: Custom Color Cycling](#custom_color_cycling)

This code will cycle through 12 colors and white. This is useful to test to see if you wired the colors correctly or want to show a color. There are options to adjust the brightness, type of LED, and rate at which the colors cycle.

If you have not already, unzip the GitHub repo and open the example code called **Example1_RGB-CycleLED.ino**. The path of the example code will probably look similar to: **\... \\ Non-Addresssable_RGB_LED_Strip_Code \\ Firmware \\ Arduino \\ Example1_RGB-CycleLED**. You can also copy the code below and paste it into the Arduino IDE. Select the board (in this case the **Arduino/Genuino Uno**) and COM port that the board enumerated to. Then hit the upload button to upload to your Arduino.

    language:c
    /******************************************************************************
      Example1_RGB-CycleLED.ino

      Non-Addressable RGB LED Custom Color Cycle
      WRITTEN BY: Ho Yun "Bobby" Chan @ SparkFun Electronics
      DATE: November 4, 2019
      GITHUB REPO: https://github.com/sparkfun/Non-Addresssable_RGB_LED_Strip_Code
      DEVELOPMENT ENVIRONMENT SPECIFICS:
        Firmware developed using Arduino IDE v1.8.9

      ============================== DESCRIPTION ==============================
      Expand your color options using analogWrite() and a non-addressable RGB LED.
      This code will cycle through 12 colors and white. There are options to adjust
      the brightness, type of LED, and rate at which the colors cycle.

      This example code works with an individual common anode and common cathode
      RGB LED. If you have a transistor or constant current LED driver, you can
      also use it to control an RGB LED strip or a higher power RGB LED.
      We'll assume that you are using a common anode LEDs in the strip. For more
      information checkout our tutorial: https://learn.sparkfun.com/tutorials/731

      Notes: There are twelve rainbow colors (primary, secondary, tertiary).
      Unlike digitalWrite(), which can be only HIGH (on) or LOW (off),
      analogWrite() lets you smoothly change the brightness from 0 (off) to 255 (fully on).
      When analogWrite() is used with the RGB LED, you can create millions of colors!
      For simplicity, we'll use 12 rainbow colors and white.  We will be blinking
      between each color.

      In the analogWrite() functions:
        0 is off
        128 is halfway on (used for the tertiary colors)
        255 is full brightness.

      ========== TUTORIAL ==========
      Non-Addressable RGB LED Strip Hookup Guide
      https://learn.sparkfun.com/tutorials/731

      Transistors | Applictions I: Switches
      https://learn.sparkfun.com/tutorials/transistors/all#applications-i-switches

      ==================== PRODUCTS THAT USE THIS CODE ====================
        LED RGB Strip (1M Bare) - https://www.sparkfun.com/products/12021
        LED RGB Strip (1M Sealed) - https://www.sparkfun.com/products/12023
        LED RGB Strip (5B Bare) - https://www.sparkfun.com/products/12022
        LED RGB Strip (5M Sealed) - https://www.sparkfun.com/products/12024
        Triple Output High Power RGB LED - https://www.sparkfun.com/products/15200

        PicoBuck LED Driver - https://www.sparkfun.com/products/13705
        N-Channel MOSFET Power Control Kit - https://www.sparkfun.com/products/12959

      ==================== HARDWARE CONNECTIONS ====================
      The hardware connection depends on your hardware and setup. Below is one possible
      arrangement.

      RGB Common Anode LED Strip => BJT/MOSFET => Arduino PWM Pin
          R pin => transistor => 5
          G pin => transistor => 6
          B pin => transistor => 9
          - pin                  -

      LICENSE: This code is released under the MIT License (http://opensource.org/licenses/MIT)

      ******************************************************************************/

    //Debug mode, comment one of these lines out using a syntax
    //for a single line comment ("//"):
    //#define DEBUG 0     //0 = LEDs only
    #define DEBUG 1     //1 = LEDs w/ serial output

    // Define our LED pins to a PWM Pin
    #define redPin 5
    #define greenPin 6
    #define bluePin 9

    // Create integer variables for our LED color value
    int redValue = 0;
    int greenValue = 0;
    int blueValue = 0;

    //Create brightness variable
    //Ranging from 0.0-1.0:
    //  0.0 is off
    //  0.5 is 50%
    //  1.0 is fully on
    float brightnessLED = 0.1;

    //Create variables for type of LED and if it is used with a transistor
    boolean commonAnode = false;
    boolean commonCathode = true; //i.e.) When pin is HIGH, LED will also go HIGH without a transistor/PicoBuck

    // Note:
    //  Common Anode is `commonAnode`
    //  Common Cathode LED is `commonCathode`
    //  Common Anode RGB LED Strip with transistor is `!commonAnode`
    //  RGB High Power LED with PicoBuck is also  `!commonAnode`
    boolean rgbType = !commonAnode;

    int blinkRate = 1000; //in milliseconds

    void setup() //end setup()

    void loop()
    //end loop

    // ==================== CUSTOM FUNCTIONS DEFINED BELOW ====================
    void allOFF() 

    void redON() 

    void orangeON() 

    void yellowON() 

    void chartrueseON() 

    void greenON() 

    void springGreenON() 

    void cyanON() 

    void azureON() 

    void blueON() 

    void violetON() 

    void magentaON() 

    void roseON() 

    void whiteON() 

    void rgbCalc() 
      else 

      redValue = int(redValue * brightnessLED);
      greenValue = int(greenValue * brightnessLED);
      blueValue = int(blueValue * brightnessLED);
    }

    void rgbShow() 

Once the code has been uploaded, the RGB LED will cycle through each of the 12 colors, white, and then turn off. Each color has its own function. When the function is called, the custom color will have a certain analog value for red, green, and blue. Before displaying the color, the values are calculated depending on the type of LED being used (either a common cathode or common anode). By default, we are assuming that the strip uses common anode LEDs but we are using a transistor to control them so `rgbType` is set to `!commonAnode`. The color is further calculated based on the intensity of the LED. After calculating the LED color lights up whenever the function `rgbShow()` is called.

Open the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) set to **9600** baud to see the output as the color changes. Try adjusting the brightness or blink rate. If you are not seeing the correct color associated with the output, make sure to check your connections and ensure that the correct type of RGB LED is selected.

[![Custom Color Cycling](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Non-Addressable_RGB_LED_Strip_Custom_Color_Cycling.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Non-Addressable_RGB_LED_Strip_Custom_Color_Cycling.gif)

### [][Example 2: Fading](#fading)

This code will fade through 12 colors and white. There are options to adjust the brightness, type of LED, and rate at which the colors fade.

If you have not already, unzip the GitHub repo and open the example code called **Example2_RGB-FadeLED.ino**. The path of the example code will probably look similar to: **\...Non-Addresssable_RGB_LED_Strip_Code\\Firmware\\Arduino\\Example2_RGB-FadeLED.ino**. You can also copy the code below and paste it into the Arduino IDE. Select the board (in this case the **Arduino/Genuino Uno**) and COM port that the board enumerated to. Then hit the upload button to upload to your Arduino.

    language:c
    /******************************************************************************
      Example2_RGB-FadeLED.ino

      Non-Addressable RGB LED Custom Color Fade
      WRITTEN BY: Ho Yun "Bobby" Chan @ SparkFun Electronics
      DATE: November 4, 2019
      GITHUB REPO: https://github.com/sparkfun/Non-Addresssable_RGB_LED_Strip_Code
      DEVELOPMENT ENVIRONMENT SPECIFICS:
        Firmware developed using Arduino IDE v1.8.9

      ============================== DESCRIPTION ==============================
      Expand your color options using analogWrite() and a non-addressable RGB LED.
      This code will fade through 12 colors and white. There are options to adjust
      the brightness, type of LED, and rate at which the colors fade.

      This example code works with an individual common anode and common cathode
      RGB LED. If you have a transistor or constant current LED driver, you can
      also use it to control an RGB LED strip or a higher power RGB LED.
      We'll assume that you are using a common anode LEDs in the strip. For more
      information checkout our tutorial: https://learn.sparkfun.com/tutorials/731

      Notes: There are twelve rainbow colors (primary, secondary, tertiary).
      Unlike digitalWrite(), which can be only HIGH (on) or LOW (off),
      analogWrite() lets you smoothly change the brightness from 0 (off) to 255 (fully on).
      When analogWrite() is used with the RGB LED, you can create millions of colors!
      For simplicity, we'll use 12 rainbow colors and white.  We will be fading
      between each color.

      In the analogWrite() functions:
        0 is off
        128 is halfway on (used for the tertiary colors)
        255 is full brightness.

      ========== TUTORIAL ==========
      Non-Addressable RGB LED Strip Hookup Guide
      https://learn.sparkfun.com/tutorials/731

      Transistors | Applictions I: Switches
      https://learn.sparkfun.com/tutorials/transistors/all#applications-i-switches

      ==================== PRODUCTS THAT USE THIS CODE ====================
        LED RGB Strip (1M Bare) - https://www.sparkfun.com/products/12021
        LED RGB Strip (1M Sealed) - https://www.sparkfun.com/products/12023
        LED RGB Strip (5B Bare) - https://www.sparkfun.com/products/12022
        LED RGB Strip (5M Sealed) - https://www.sparkfun.com/products/12024
        Triple Output High Power RGB LED - https://www.sparkfun.com/products/15200

        PicoBuck LED Driver - https://www.sparkfun.com/products/13705
        N-Channel MOSFET Power Control Kit - https://www.sparkfun.com/products/12959

      ==================== HARDWARE CONNECTIONS ====================
      The hardware connection depends on your hardware and setup. Below is one possible
      arrangement.

      RGB Common Anode LED Strip => BJT/MOSFET => Arduino PWM Pin
          R pin => transistor => 5
          G pin => transistor => 6
          B pin => transistor => 9
          - pin                  -

      LICENSE: This code is released under the MIT License (http://opensource.org/licenses/MIT)

      ******************************************************************************/

    //Debug mode, comment one of these lines out using a syntax
    //for a single line comment ("//"):
    //#define DEBUG 0     //0 = LEDs only
    #define DEBUG 1     //1 = LEDs w/ serial output

    // Define our LED pins to a PWM Pin
    #define redPin 5
    #define greenPin 6
    #define bluePin 9

    // Create integer variables for our LED color value
    int redValue = 0;
    int greenValue = 0;
    int blueValue = 0;

    //Create brightness variable
    //Ranging from 0.0-1.0:
    //  0.0 is off
    //  0.5 is 50%
    //  1.0 is fully on
    float brightnessLED = 0.1;

    //Create variables for type of LED and if it is used with a transistor
    boolean commonAnode = false;
    boolean commonCathode = true;//i.e.) When pin is HIGH, LED will also go HIGH without a transistor/PicoBuck

    // Note:
    //  Common Anode is `commonAnode`
    //  Common Cathode LED is `commonCathode`
    //  Common Anode RGB LED Strip with transistor is `!commonAnode`
    //  RGB High Power LED with PicoBuck is also  `!commonAnode`
    boolean rgbType = !commonAnode;

    int colorMode = 1; //color mode to control LED color

    //Variables for fading LED
    int prevFadeVal = 0;
    int currentFadeVal = 0;
    boolean increasing = true;
    int fadeVal = 5; //value to step when increasing/decreasing, recommended to be 1 or 5, larger numbers will have problems lighting up
    int fadeMAX = 255; //maximum fade value
    int fadeMIN = 0;   //minimum fade value
    int fadeDelay = 30;//delay between each step

    void setup() //end setup()

    void loop()
    

          // takes x amount of steps if you do not set it to zero for certain brightness (i.e. takes 8 more steps to turn off for 0.1)
          //Serial.print("Red Value =");
          //Serial.println( int((currentFadeVal) * brightnessLED));

          //Serial.print("Green Value =");
          //Serial.println( int((currentFadeVal * 0.498) * brightnessLED));
          break;
        //========== END FADE ORANGE ==========

        case 3://FADE YELLOW
          redValue = currentFadeVal;
          greenValue = currentFadeVal;
          blueValue = 0;

          rgbCalc();
          break;
        //========== END FADE YELLOW ==========

        case 4://FADE CHARTRUESE
          redValue = currentFadeVal * 0.498; // 128/255 = ~0.498039
          greenValue = currentFadeVal;
          blueValue = 0;

          rgbCalc();

          if (greenValue > 0 && redValue == 0) 
          break;
        //========== END FADE CHARTRUESE ==========

        case 5://FADE GREEN
          redValue = 0;
          greenValue = currentFadeVal;
          blueValue = 0;

          rgbCalc();
          break;
        //========== END FADE GREEN ==========

        case 6://FADE SPRING GREEN
          redValue = 0;
          greenValue = currentFadeVal;
          blueValue = currentFadeVal * 0.498; // 128/255 = ~0.498039

          rgbCalc();

          if (greenValue > 0 && blueValue == 0) 
          break;
        //========== END FADE SPRING GREEN ==========

        case 7://FADE CYAN
          redValue = 0;
          greenValue = currentFadeVal;
          blueValue = currentFadeVal;

          rgbCalc();
          break;
        //========== END FADE CYAN ==========

        case 8://FADE AZURE
          redValue = 0;
          greenValue = currentFadeVal * 0.498; // 128/255 = ~0.498039
          blueValue = currentFadeVal;

          rgbCalc();

          if (blueValue > 0 && greenValue == 0) 
          break;
        //========== END FADE AZURE ==========

        case 9://FADE BLUE
          redValue = 0;
          greenValue = 0;
          blueValue = currentFadeVal;

          rgbCalc();
          break;
        //========== END FADE BLUE ==========

        case 10://FADE VIOLET
          redValue = currentFadeVal * 0.498;
          greenValue = 0;
          blueValue = currentFadeVal;

          rgbCalc();

          if (blueValue > 0 && redValue == 0) 
          break;
        //========== END FADE VIOLET ==========

        case 11://FADE MAGENTA
          redValue = currentFadeVal;
          greenValue = 0;
          blueValue = currentFadeVal;

          rgbCalc();
          break;
        //========== END FADE MAGENTA ==========

        case 12://FADE ROSE
          redValue = currentFadeVal;
          greenValue = 0;
          blueValue = currentFadeVal * 0.498;

          rgbCalc();

          if (redValue > 0 && blueValue == 0) 
          break;
        //========== END FADE ROSE ==========

        case 13://FADE WHITE
          redValue = currentFadeVal;
          greenValue = currentFadeVal;
          blueValue = currentFadeVal;

          rgbCalc();
          break;
        //========== END FADE WHITE ==========

        default:
          allOFF();
          rgbCalc();
          break;
      }

    #if DEBUG
      Serial.print("Color Fading = ");
      if (colorMode == 1) 
      else if (colorMode == 2) 
      else if (colorMode == 3) 
      else if (colorMode == 4) 
      else if (colorMode == 5) 
      else if (colorMode == 6) 
      else if (colorMode == 7) 
      else if (colorMode == 8) 
      else if (colorMode == 9) 
      else if (colorMode == 10) 
      else if (colorMode == 11) 
      else if (colorMode == 12) 
      else if (colorMode == 13) 
      else 
      Serial.print(" | Brightness % = ");
      Serial.print(brightnessLED * 100);
      Serial.print("%");

      Serial.print(" | Fade Val Before Calc= ");
      Serial.println(currentFadeVal);
    #endif

      rgbShow();
      delay(fadeDelay);

      if (increasing == true) 
      else 

      if (currentFadeVal > fadeMAX) 
      else if (currentFadeVal < fadeMIN) 
      }

      prevFadeVal = currentFadeVal;

    }//END LOOP

    // ==================== CUSTOM FUNCTIONS DEFINED BELOW ====================
    void allOFF() 

    void redON() 

    void orangeON() 

    void yellowON() 

    void chartrueseON() 

    void greenON() 

    void springGreenON() 

    void cyanON() 

    void azureON() 

    void blueON() 

    void violetON() 

    void magentaON() 

    void roseON() 

    void whiteON() 

    void rgbCalc() 
      else 

      redValue = int(redValue * brightnessLED);
      greenValue = int(greenValue * brightnessLED);
      blueValue = int(blueValue * brightnessLED);
    }

    void rgbShow() 

Once the code has been uploaded, you should see the colors fading in and out. Open the serial monitor at **9600** to see what color is fading and its respective fade value. Due to the calculations and serial output, the fading can appear to be slow. You may want to adjust the baud rate to a higher value like *115200*, adjust the fade delay, or turn off the debugging by defining `DEBUG` as `0`. Additionally, the LEDs may turn off if the fade value and brightness is too small. This is due to the minimum voltage required to turn on the LEDs. You should see something similar to the GIF below. The GIF repeats a small sample of the colors fading. You will see all of the colors cycling in your setup.

[![Custom Color Fading](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Non-Addressable_RGB_LED_Strip_Custom_Color_Fading.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Non-Addressable_RGB_LED_Strip_Custom_Color_Fading.gif)

### [][Example 3: Full Demo](#full_demo)

**Note:** This example uses the full circuit to control the LED using buttons and a potentiometer. By default, the potentiometer is commented out. Simply uncomment the code by removing the `//` in front of this line of code.\
\

``` c
  //brightnessLED = analogRead(knobPin) / 1023.0; //potentiometer for Brightness
```

If there isn\'t an analog input connected, the pin will be floating. As a result, the LED\'s brightness will fluctuate everytime the analog pin is read in the main `loop()`.

This code will turn on a color, blink, fade, or cycle through 12 colors depending on the button input. The color cycle used in this demo will fade between each of the 12 colors. There are options to adjust the brightness, type of LED, and rate at which the colors cycle. The RedBoard will only change the color and pattern after pressing the button again.

If you have not already, unzip the GitHub repo and open the example code called **Example3_RGB-FullDemoLED.ino**. The path of the example code will probably look similar to: **\...Non-Addresssable_RGB_LED_Strip_Code\\Firmware\\Arduino\\Example3_RGB-FullDemoLED**. You can also copy the code below and paste it into the Arduino IDE. Select the board (in this case the **Arduino/Genuino Uno**) and COM port that the board enumerated to. Then hit the upload button to upload to your Arduino.

    language:c
    /******************************************************************************
      Example3_RGB-FullDemoLED.ino

      Non-Addressable RGB LED Full Demo
      WRITTEN BY: Ho Yun "Bobby" Chan @ SparkFun Electronics
      DATE: November 4, 2019
      GITHUB REPO: https://github.com/sparkfun/Non-Addresssable_RGB_LED_Strip_Code
      DEVELOPMENT ENVIRONMENT SPECIFICS:
        Firmware developed using Arduino IDE v1.8.9

      ============================== DESCRIPTION ==============================
      Expand your color options using analogWrite() and a non-addressable RGB LED.
      This code will either turn on a color, blink, fade, or cycle through 12
      colors and white depending on the button input. There are options to adjust
      the brightness, type of LED, and rate at which the colors blink/fade/cycle.

      This example code works with an individual common anode and common cathode
      RGB LED. If you have a transistor or constant current LED driver, you can
      also use it to control an RGB LED strip or a higher power RGB LED.
      We'll assume that you are using a common anode LEDs in the strip. For more
      information checkout our tutorial: https://learn.sparkfun.com/tutorials/731

      Notes: There are twelve rainbow colors (primary, secondary, tertiary).
      Unlike digitalWrite(), which can be only HIGH (on) or LOW (off),
      analogWrite() lets you smoothly change the brightness from 0 (off) to 255 (fully on).
      When analogWrite() is used with the RGB LED, you can create millions of colors!
      For simplicity, we'll use 12 rainbow colors and white.

      In the analogWrite() functions:
        0 is off
        128 is halfway on (used for the tertiary colors)
        255 is full brightness.

      ========== TUTORIAL ==========
      Non-Addressable RGB LED Strip Hookup Guide
      https://learn.sparkfun.com/tutorials/731

      Transistors | Applictions I: Switches
      https://learn.sparkfun.com/tutorials/transistors/all#applications-i-switches

      ==================== PRODUCTS THAT USE THIS CODE ====================
        LED RGB Strip (1M Bare) - https://www.sparkfun.com/products/12021
        LED RGB Strip (1M Sealed) - https://www.sparkfun.com/products/12023
        LED RGB Strip (5B Bare) - https://www.sparkfun.com/products/12022
        LED RGB Strip (5M Sealed) - https://www.sparkfun.com/products/12024
        Triple Output High Power RGB LED - https://www.sparkfun.com/products/15200

        PicoBuck LED Driver - https://www.sparkfun.com/products/13705
        N-Channel MOSFET Power Control Kit - https://www.sparkfun.com/products/12959

      ==================== HARDWARE CONNECTIONS ====================
      The hardware connection depends on your hardware and setup. Below is one possible
      arrangement.

      RGB Common Anode LED Strip => BJT/MOSFET => Arduino PWM Pin
          R pin => transistor => 5
          G pin => transistor => 6
          B pin => transistor => 9
          - pin                  -

      LICENSE: This code is released under the MIT License (http://opensource.org/licenses/MIT)

      ******************************************************************************/

    //Debug mode, comment one of these lines out using a syntax
    //for a single line comment ("//"):
    //#define DEBUG 0     //0 = LEDs only
    #define DEBUG 1     //1 = LEDs w/ serial output

    // Define our LED pins to a PWM Pin
    #define redPin 5
    #define greenPin 6
    #define bluePin 9

    // Create integer variables for our LED color value
    int redValue = 0;
    int greenValue = 0;
    int blueValue = 0;

    // Define our Potentiometer to a Analog Pin for Brightness
    // This is needed if you use a Potentiometer
    #define knobPin A0

    //Create brightness variable
    //Ranging from 0.0-1.0:
    //  0.0 is off
    //  0.5 is 50%
    //  1.0 is fully on
    float brightnessLED = 0.1;

    //Create variables for type of LED and if it is used with a transistor
    boolean commonAnode = false;
    boolean commonCathode = true;//i.e.) When pin is HIGH, LED will also go HIGH without a transistor/PicoBuck

    // Note:
    //  Common Anode LED is `commonAnode`
    //  Common Cathode LED is `commonCathode`
    //  Common Anode RGB LED Strip with transistor is `!commonAnode`
    //  RGB High Power LED with PicoBuck is also  `!commonAnode`
    boolean rgbType = !commonAnode;

    //Variables to keep track of color and pattern
    int colorMode = 0; //color mode to control LED color
    int pattern = 0; //pattern to turn off, stay on, fade, blink

    //Variables for fading LED
    int prevFadeVal = 0;
    int currentFadeVal = 0;
    boolean increasing = true;
    int fadeVal = 5; //value to step when increasing/decreasing, recommended to be 1 or 5, larger numbers will have problems lighting up
    int fadeMAX = 255; //maximum fade value
    int fadeMIN = 0;   //minimum fade value
    int fadeDelay = 30;//delay between each step

    //Variables for blinking LED
    int blinkVal = 0;
    boolean blinkON = false;
    int counter = 0; //use as a "delay"
    int blinkRate = 750; //in milliseconds

    //Variables to transition between RGB in a rainbow
    int rainbowRedVal = 0;
    int rainbowGreenVal = 0;
    int rainbowBlueVal = 0;
    int rainbowTransitionVal = 0;
    int rainbowDelay = 5; //in milliseconds to transition between colors

    //Note: You'll want to not make `rainbowDelay` too long as this will
    //      cause delays with button presses

    //Button variables for color
    const int button1Pin = 2;
    boolean button1State = false;
    boolean prevbutton1State = false;
    boolean currentbutton1State = false;

    //Button variables for pattern
    const int button2Pin = 3;
    boolean button2State = false;
    boolean prevbutton2State = false;
    boolean currentbutton2State = false;

    void setup() 

      sequenceTest();//visually initialization
      allOFF(); //make sure to initialize LEDs with it turned off
      rgbCalc();//calculate for RGB type
      rgbShow(); //make sure to show it happening

      pinMode(button1Pin, INPUT_PULLUP); //use internal pullup resistor with button
      pinMode(button2Pin, INPUT_PULLUP); //use internal pullup resistor with button

    #if DEBUG
      Serial.begin(9600); //initialize Serial Monitor
      //while (!Serial); // Comment out to wait for serial port to connect to Serial Monitor. Option for native USB.
      Serial.println("Custom Color Mixing Demo w/ an RGB LED. Toggling the buttons will adjust the color and pattern.");
      Serial.println(" ");
      Serial.println("Note: Make sure to adjust the code for a common cathode or common anode.");
      Serial.println("Default is set to no color and off!");
      Serial.println(" ");
    #endif

    }//end setup()

    void loop()
    
          else if (colorMode == 2) 
          else if (colorMode == 3) 
          else if (colorMode == 4) 
          else if (colorMode == 5) 
          else if (colorMode == 6) 
          else if (colorMode == 7) 
          else if (colorMode == 8) 
          else if (colorMode == 9) 
          else if (colorMode == 10) 
          else if (colorMode == 11) 
          else if (colorMode == 12) 
          else if (colorMode == 13) 
          else 
    #endif

          //Cycle through colors when pressing buttons
          if (colorMode < 0 || colorMode > 13) 
        }
        else 
        prevbutton1State = currentbutton1State;//update button1 state
      }

      //button has not been pressed, it will be high
      else 

      //==================== END CHECK BUTTON FOR COLOR MODE ====================

      //==================== CHECK BUTTON FOR PATTERN ====================
      if (button2State == LOW) 
          else if (pattern == 2) 
          else if (pattern == 3) 
          else if (pattern == 4) 
          else 
    #endif

          if (pattern < 0 || pattern > 4) 
        }

        else 
        prevbutton2State = currentbutton2State; //update button2 state
      }

      //button has not been pressed, it will be high
      else 
      switch (pattern) 
      //==================== END CHECK BUTTON FOR PATTERN ====================

    }//end loop

    // ==================== CUSTOM FUNCTIONS DEFINED BELOW ====================
    void allOFF() 

    void redON() 

    void orangeON() 

    void yellowON() 

    void chartrueseON() 

    void greenON() 

    void springGreenON() 

    void cyanON() 

    void azureON() 

    void blueON() 

    void violetON() 

    void magentaON() 

    void roseON() 

    void whiteON() 

    //-------------------- sequenceTest() FUNCTION --------------------

    void sequenceTest() //-------------------- END sequenceTest() FUNCTION --------------------

    void rgbCalc() 
      else 

      redValue = int(redValue * brightnessLED);
      greenValue = int(greenValue * brightnessLED);
      blueValue = int(blueValue * brightnessLED);
    }

    void rgbShow() 

    //-------------------- patternON() FUNCTION --------------------

    void patternON() //end switch

      rgbShow();
    }//-------------------- end patternON() FUNCTION --------------------

    //-------------------- patternFade() FUNCTION --------------------
    void patternFade() 
          // takes x amount of steps if you do not set it to zero for certain brightness (i.e. takes 8 more steps to turn off for 0.1)
          //Serial.print("Red Value =");
          //Serial.println( int((currentFadeVal) * brightnessLED));

          //Serial.print("Green Value =");
          //Serial.println( int((currentFadeVal * 0.498) * brightnessLED));
          break;
        //========== END FADE ORANGE ==========

        case 3://FADE YELLOW
          redValue = currentFadeVal;
          greenValue = currentFadeVal;
          blueValue = 0;

          rgbCalc();
          break;
        //========== END FADE YELLOW ==========

        case 4://FADE CHARTRUESE
          redValue = currentFadeVal * 0.498; // 128/255 = ~0.498039
          greenValue = currentFadeVal;
          blueValue = 0;

          rgbCalc();

          if (greenValue > 0 && redValue == 0) 
          break;
        //========== END FADE CHARTRUESE ==========

        case 5://FADE GREEN
          redValue = 0;
          greenValue = currentFadeVal;
          blueValue = 0;

          rgbCalc();
          break;
        //========== END FADE GREEN ==========

        case 6://FADE SPRING GREEN
          redValue = 0;
          greenValue = currentFadeVal;
          blueValue = currentFadeVal * 0.498; // 128/255 = ~0.498039

          rgbCalc();

          if (greenValue > 0 && blueValue == 0) 
          break;
        //========== END FADE SPRING GREEN ==========

        case 7://FADE CYAN
          redValue = 0;
          greenValue = currentFadeVal;
          blueValue = currentFadeVal;

          rgbCalc();
          break;
        //========== END FADE CYAN ==========

        case 8://FADE AZURE
          redValue = 0;
          greenValue = currentFadeVal * 0.498; // 128/255 = ~0.498039
          blueValue = currentFadeVal;

          rgbCalc();
          if (blueValue > 0 && greenValue == 0) 
          break;
        //========== END FADE AZURE ==========

        case 9://FADE BLUE
          redValue = 0;
          greenValue = 0;
          blueValue = currentFadeVal;

          rgbCalc();
          break;
        //========== END FADE BLUE ==========

        case 10://FADE VIOLET
          redValue = currentFadeVal * 0.498;
          greenValue = 0;
          blueValue = currentFadeVal;

          rgbCalc();

          if (blueValue > 0 && redValue == 0) 
          break;
        //========== END FADE VIOLET ==========

        case 11://FADE MAGENTA
          redValue = currentFadeVal;
          greenValue = 0;
          blueValue = currentFadeVal;

          rgbCalc();
          break;
        //========== END FADE MAGENTA ==========

        case 12://FADE ROSE
          redValue = currentFadeVal;
          greenValue = 0;
          blueValue = currentFadeVal * 0.498;

          rgbCalc();

          if (redValue > 0 && blueValue == 0) 
          break;
        //========== END FADE ROSE ==========

        case 13://FADE WHITE
          redValue = currentFadeVal;
          greenValue = currentFadeVal;
          blueValue = currentFadeVal;

          rgbCalc();
          break;
        //========== END FADE WHITE ==========

        default:
          allOFF();
          rgbCalc();
          break;
      }

      rgbShow();
      delay(fadeDelay);

      if (increasing == true) 
      else 

      if (currentFadeVal > fadeMAX) 
      else if (currentFadeVal < fadeMIN) 

      prevFadeVal = currentFadeVal;
    }//-------------------- END patternFade() FUNCTION --------------------

    //-------------------- patternBlink() FUNCTION --------------------
    void patternBlink() 

      rgbShow();

      if (counter == blinkRate) 
        else 
        counter = 0;
      }
      else 
    }//-------------------- patternBlink() FUNCTION //--------------------

    //-------------------- patternRainbow() FUNCTION --------------------
    void patternRainbow() 
        }
        else if (rainbowTransitionVal == 1) 
        }
        else if (rainbowTransitionVal == 2) 
        }
        else if (rainbowTransitionVal == 3) 
        }
        else if (rainbowTransitionVal == 4) 
        }
        else if (rainbowTransitionVal == 5) 
        }
        else if (rainbowTransitionVal == 6) 
        }
      }//end check for commonCathode

      else 
        }
        else if (rainbowTransitionVal == 1) 
        }
        else if (rainbowTransitionVal == 2) 
        }
        else if (rainbowTransitionVal == 3) 
        }
        else if (rainbowTransitionVal == 4) 
        }
        else if (rainbowTransitionVal == 5) 
        }
        else if (rainbowTransitionVal == 6) 
        }
      }//end check for commonAnode

      redValue = int(rainbowRedVal * brightnessLED);
      greenValue = int(rainbowGreenVal * brightnessLED);
      blueValue = int(rainbowBlueVal * brightnessLED);

      // Note: the rainbow function calculates the function here so
      // we do not need to call the `rgbCalc()` function

      rgbShow();

      delay(rainbowDelay);
    }//-------------------- END patternRainbow() FUNCTION --------------------

    // ==================== END CUSTOM FUNCTIONS DEFINED ====================

Once the code has been uploaded, the demo will cycle through the defined colors. Pressing the buttons will cycle through the color or pattern. Opening the Arduino serial monitor at **9600** will show the current color mode or pattern after every button press.

[![Full Demo with Rainbow](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Non-Addressable_RGB_LED_Strip_Full_Demo_Rainbow.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Non-Addressable_RGB_LED_Strip_Full_Demo_Rainbow.gif)

## Modifying RGB LED Strip

Depending on your project, you may not need to use all 1M or 5M of the LED strip. You can cut off the excess and use it for other projects. Or you may need to separate the strip and extend the wires to illuminate other parts of your project. You may even need to inject power at a certain length. Let\'s go over how to cut, rewire, clean, and reseal a sealed LED strip.

**Note:** We will be modifying the LED strip using [male jumper wires](https://www.sparkfun.com/products/11709) to connect to a breadboard. To make it easier to disconnect and reconnect the strips to your system, you could use a [4-pin polarized connector](https://www.sparkfun.com/products/14576) and a 1M sealed strip. You can also [solder wire](https://www.sparkfun.com/products/11367).\
\

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![LED Strip Pigtail Connector (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/2/1/14576-LED_Pigtail_connector_4_Pin_-01.jpg)](https://www.sparkfun.com/led-strip-pigtail-connector-4-pin.html)

### [LED Strip Pigtail Connector (4-pin)](https://www.sparkfun.com/led-strip-pigtail-connector-4-pin.html) 

[ CAB-14576 ]

These 4-pin JST-SM pigtail connectors mate perfectly with LED strips and other applications that require only two lines and a...

[ [\$1.95] ]

[![Jumper Wires Premium 6\" M/M - 20 AWG (10 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/8/9/2/11709-01.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-20-awg-10-pack.html)

### [Jumper Wires Premium 6\" M/M - 20 AWG (10 Pack)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-20-awg-10-pack.html) 

[ PRT-11709 ]

Jumper wires are awesome. Just a little bit of stranded core wire with a nice solid pin connector on either end. They have th...

[ [\$7.75] ]

First, cut the LED strip at the center of the exposed pads using a [diagonal cutter](https://www.sparkfun.com/products/8794). The dot and dashed line in the image below is where you will need to perform the cut. Make sure to remove part of the silicone tube to access the LED strip\'s pads if you are using the sealed version.

[![Cut between the LED Strip\'s Pads](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/2/12023_1_Nonaddressable_RGBLEDStripcut.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/2/12023_1_Nonaddressable_RGBLEDStripcut.jpg)

Cut half of the premium jumper wires and [strip](https://learn.sparkfun.com/tutorials/working-with-wire) the insulation. Then [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the wires to each of the LED strip\'s pads.

[![Solder Wires to LED Strip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/2/SolderLEDStrip.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/2/SolderLEDStrip.jpg)

For a secure connection, you can braid the wires together to manage the connections. To braid your wires, twist a pair of wires in a counterclockwise pattern between your index finger and thumb using both hands. We\'ll be using the green and red wires that were soldered on.

[![Wire Management Braiding Counterclockwise 1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/2/WireManagementBraidingCounterclockwise_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/2/WireManagementBraidingCounterclockwise_1.jpg)

Then twist the other pair of wires in a counterclockwise pattern.

[![Wire Management Braiding Counterclockwise 2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/2/WireManagementBraidingCounterclockwise_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/2/WireManagementBraidingCounterclockwise_2.jpg)

Twist the pairs of wires in a clockwise pattern.

[![Wire Management Braiding Clockwise](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/2/WireManagementBraidingClockwise.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/2/WireManagementBraidingClockwise.jpg)

### Clean Solder Joints

If you were using water soluble flux, clean the solder joints with deionized water and a toothbrush. Dry the LED strips thoroughly using compressed air. Luckily, SparkFun has a [PCB cleaning room](https://learn.sparkfun.com/tutorials/electronics-assembly/washing). As an alternative, you could use [water from the sink and towels](https://www.sparkfun.com/news/1161). You can also use isopropyl alcohol.

[![Clean Solder Joints](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/2/CleanSolderJoints.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/2/CleanSolderJoints.jpg)

### Test LED Strips

Once dry, test the LED strips to ensure the colors are correct and the wires are connected to its respective pads. You can use a benchtop power supply set to output about 12V, a 12V wall adapter, or 9V battery to verify the connection. The image below shows all the channels turned on. Make sure to test each channel individually.

[![Testing LED Strip with Wiring](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/1/Analog-Non-Addressable-RGB_LED_Strip.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/1/Analog-Non-Addressable-RGB_LED_Strip.jpg)

### Secure w/ Hot Glue or Heat Shrink

Add hot glue to the terminals to secure the wires further. You can also use some heat shrink with hot glue as long as it does not cover the LED. The image below shows the wires being secured with hot glue. The LED strip was used with a silicone tube so additional hot glue was added to seal the exposed strip.

[![Hot Glue Terminals](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/2/WireManagementHotGlueTerminals.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/2/WireManagementHotGlueTerminals.jpg)

**Tip:** To smooth out the glue on the wires and LED strip, try using a little hot air from a [heat gun](https://www.sparkfun.com/products/10326) or [hot air rework station](https://www.sparkfun.com/products/14557).

## Large Installation

For large installation projects, there may be voltage drops depending on the:

- amount of LEDs connected
- length of LED strip used
- how bright the LEDs are set
- animation

You may notice LEDs not able to fully turn on after a certain length due to the voltage drop. This is due to the increased resistance as you move further away from the power supply. You may notice that not all the colors are turned on or the strip becomes dim. You can also [check the voltage after each meter using a multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter/measuring-voltage) to see if there are any voltage drops if you are not able to visually see the voltage drops. If you see voltage drops and the LED strip not properly turning on, you will need to inject power with the power supply between each LED strip\'s Vcc and GND after about 1, 2, or 5 meters.

Long lengths of LED strips can also pull a lot of current when fully turned on. If you are using a high amperage power supply with long lengths, make sure that there is enough air flow, a heat sink to dissipate the heat properly, and the [wires can support the amperage](https://learn.sparkfun.com/tutorials/working-with-wire/all#wire-thickness). You may want to lower the brightness setting.