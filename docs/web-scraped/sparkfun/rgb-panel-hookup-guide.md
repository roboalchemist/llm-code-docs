# Source: https://learn.sparkfun.com/tutorials/rgb-panel-hookup-guide

## Introduction

Are you looking to add a *lot* of color to your project? These *massive* RGB [LED](https://www.sparkfun.com/leds) panels are an awesome place to start. You can create animations, games, or all sorts of other fun displays with them. Depending on the manufacturer, these panels can come in different sizes, LED pitch, and scan rates. Here are the ones that SparkFun currently carries in the catalog:

- 1024 pixels (3072 total LEDs!) [32x32 pixel](https://www.sparkfun.com/products/14646) panel with 1:16 scan rate measuring 7.5\"x7.5\"
- 2048 pixels (6144 total LEDs!) [32x64 pixel](https://www.sparkfun.com/products/14718) panel with 1:16 scan rate measuring 5x10\"

[![RGB LED Matrix Panel - 32x32](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/8/3/2/12584-RGB_LED_Panel_-_32x32-01.jpg)](https://www.sparkfun.com/rgb-led-matrix-panel-32x32.html)

### [RGB LED Matrix Panel - 32x32](https://www.sparkfun.com/rgb-led-matrix-panel-32x32.html) 

[ COM-14646 ]

These 32x32 RGB LED panels are an awesome place to start to add color to a project! You can create animations, games, or usef...

[ [\$48.50] ]

[![RGB LED Matrix Panel - 32x64](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/9/3/6/14718-RGB_LED_Matrix_Panel_-_32x64-01.jpg)](https://www.sparkfun.com/products/14718)

### [RGB LED Matrix Panel - 32x64](https://www.sparkfun.com/products/14718) 

[ COM-14718 ]

These 32x64 RGB LED panels are an awesome place to start to add color to a project! You can create animations, games, or usef...

**Retired**

**Warning:** Due to the limitations of the Arduino library used in this tutorial, a 64x64 RGB LED matrix panel will **not** work with a standard Arduino (Arduino Uno with Atmega328P, etc). You will need a Teensy, Raspberry Pi, FPGA, or a development board that has a higher processing speed and memory. Try looking at the [Resources and Going Further](https://learn.sparkfun.com/tutorials/rgb-panel-hookup-guide#resources--going-further) at the end of this tutorial for more information on alternatives to drive the 64x64 panels.\
\

[![RGB LED Matrix Panel - 64x64](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/9/2/14824-RGB_LED_Matrix_Panel_-_64x64-01.jpg)](https://www.sparkfun.com/products/14824)

### [RGB LED Matrix Panel - 64x64](https://www.sparkfun.com/products/14824) 

[ COM-14824 ]

These 64x64 RGB LED panels are an awesome place to start to add color to a project! You can create animations, games, or usef...

**Retired**

**Note:** The 16x32 version has been retired from our catalog, but we are keeping the information in the tutorial for reference.\
\

[![RGB LED Panel - 16x32](https://cdn.sparkfun.com/r/140-140/assets/parts/9/2/3/5/12583-01.jpg)](https://www.sparkfun.com/products/12583)

### [RGB LED Panel - 16x32](https://www.sparkfun.com/products/12583) 

[ COM-12583 ]

Are you looking to add a lot of color to your project? These large 32x16 RGB LED panels are an awesome place to start. You ca...

**Retired**

In this tutorial we\'ll show you just how, exactly, these panels operate. We\'ll dig into the hardware hookup and examine how to best power them. Then we\'ll work up a demo sketch and control them with Arduino.

[![LED Panels Lit Up](https://cdn.sparkfun.com/r/600-600/assets/5/3/7/d/f/52a9fe69757b7f96408b456a.jpg)](https://cdn.sparkfun.com/assets/5/3/7/d/f/52a9fe69757b7f96408b456a.jpg)

*A 16x32 RGB LED panel to the left, and a 32x32 panel to the right.*

### Required Materials

On top of either size panel, you\'ll also need:

- At least an [Arduino Uno](https://www.sparkfun.com/products/11021) (or [comparable ATmega328-based Arduino](https://www.sparkfun.com/products/11575)). These panels really stretch the Arduino to its limits. If you have an [Arduino Mega 2560](https://www.sparkfun.com/products/11061) you may want to whip that out instead. Any size higher than a 32x32 panel requires an Arduino Mega 2560 or faster microcontroller.
- Two packs of [male-to-male jumper wires](https://www.sparkfun.com/products/8431). You\'ll need around 16 to wire from the panel to your Arduino.
- A **5V power supply**. You\'ll need something that can source a high amount of current. A simple [5V (1A) wall adapter](https://www.sparkfun.com/products/11456) does work, at least in the short run, but you may want to step up to a higher capacity supply, like the [12V/5V (2A)](https://www.sparkfun.com/products/11296) or [5V/2A](https://www.sparkfun.com/products/12889) wall adapter.
- You\'ll also need some method to connect your power supply to the panel. The panel includes a 4-pin polarized connector and spade-terminated cable for its power supply. Check out the next page for help finding a power source and cable.

### Suggested Reading

Before following along with this tutorial, we recommend reading through these tutorials first:

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/shift-registers)

### Shift Registers 

An introduction to shift registers and potential uses.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

[](https://learn.sparkfun.com/tutorials/12v5v-power-supply-hookup-guide)

### 12V/5V Power Supply Hookup Guide 

In this tutorial, we will replace the 12V/5V (2A) power supply\'s molex connector with two male barrel jacks adapters.

## Powering the Panel

### Power Connector

[] **Warning!** **Don\'t use the 5V supply from your Arduino**. Those are only spec\'ed to supply about 800mA, and the Arduino\'s already eating into that capacity a bit.

These panels require a **regulated 3.3-5V** supply for power. And that supply needs to be able to source a good amount of current \-- **up to 2A in the worst case** (all pixels bright, hot, white). For a 32x64, one of these panels was pulling about *\~3.36A-3.43A without a heat sink* \-- **so about up to 4A worst case**. A 4-pin (2 for VCC, 2 for GND), 0.15\"-pitch polarized connector should be used to supply power to the panel. Depending on the manufacturer, the color and location of the power connector may be different.

[![Panel power connector](https://cdn.sparkfun.com/r/600-600/assets/6/f/d/9/9/52a9fe69757b7fbe5d8b4567.jpg)](https://cdn.sparkfun.com/assets/6/f/d/9/9/52a9fe69757b7fbe5d8b4567.jpg)

### Power Cable

Included with the panel is a dedicated cable for power. It\'s a 0.15\" pitch 4-pin polarized connector. The included cable is terminated with both a female polarized connector, and a pair of spade terminals.

[![Panel power cable](https://cdn.sparkfun.com/assets/f/3/0/f/9/52aa025d757b7f7f3c8b456a.png)](https://cdn.sparkfun.com/assets/f/3/0/f/9/52aa025d757b7f7f3c8b456a.png)

Here are a few methods we\'ve used to power the panel. If you are powering the Arduino with a different voltage, make sure to connect GND in order to have the same reference voltage.

#### Longer-Term: 12V/5V Power Supply [Breakout Board]

This is our recommended combo:

1.  A [12V/5V 2A Power Supply](https://www.sparkfun.com/products/15664), which should be enough to keep the display running. (Just don\'t hook up the 12V output to it!). *Note: If you are using an older 12V/5V power supply, you will need the three prong [IEC C13 Cable](https://www.sparkfun.com/products/11299) to connect AC power to the supply.*
2.  [Breakout Board](https://www.sparkfun.com/products/15035) with [Molex connector](https://www.sparkfun.com/products/15700) and [5mm screw terminals](https://www.sparkfun.com/products/8432) soldered. *Note: The spade connector for the panel\'s GND pin can be connected to both GND pins of the screw terminal. Just make sure to not connect it to the 12V or 5V side.*
3.  [Strip two pieces of wire](https://learn.sparkfun.com/tutorials/working-with-wire#how-to-strip-a-wire) and connect a [male DC barrel jack adapter](https://www.sparkfun.com/products/10287) with a [screwdriver](https://www.sparkfun.com/products/9146) to an Arduino\'s barrel jack for VIN. *Note: Most Arduinos should have a voltage regulator that can handle the input between 7-12V, just make sure to check out the specs on the development board before powering up.*

[![ATX Breakout Board Soldered with the 12V/5V\'s 4-Pin Connector Inserted](https://cdn.sparkfun.com//assets/parts/1/4/2/5/0/15701-SparkFun_ATX_Power_Connector_Breakout_Kit_-_12V_5V__4-pin_-02.jpg)]()

Your final connection should look similar to the closeup of the connection below with the LED panel\'s forked spade connector and wires inserted into the screw terminals.

[![Spade Connector and Wires Inserted into Screw Terminal](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/ATX_Power_Connections.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/ATX_Power_Connections.jpg)

#### Longer-Term: 12V/5V Power Supply [Splicing Wires]

You can also splice the wires using the following combinations:

1.  A [12V/5V 2A Power Supply](https://www.sparkfun.com/products/15664), which should be enough to keep the display running. (Just don\'t hook up the 12V output to it!). *Note: If you are using an older 12/5V power supply, you will need the three prong [IEC C13 Cable](https://www.sparkfun.com/products/11299) to connect AC power to the supply.*
2.  A [4-pin Molex Connector w/ Pigtail](https://www.sparkfun.com/products/11298) to interface the supply to panel.

[![12/V5V Power Supply, 3 Prong Cable, Molex Connector](https://cdn.sparkfun.com/r/600-600/assets/2/8/0/4/4/52aa044c757b7fbe418b456d.png)](https://cdn.sparkfun.com/assets/2/8/0/4/4/52aa044c757b7fbe418b456d.png)

*The ingredients for our power supply and cable.*

To begin, we snipped the spade connectors off of the panel power supply cable. And then [stripped](https://learn.sparkfun.com/tutorials/working-with-wire/how-to-strip-a-wire) the newly unterminated ends.

Then we [spliced](https://learn.sparkfun.com/tutorials/working-with-wire) the Molex pigtail to the LED panel\'s power cable by connecting the **red wires together**. Do the same for the black wires (make sure you use the black wire next to the red on the Molex pigtail). Make sure you are connecting to the 5V and GND pins and **NOT** the 12V pin. Before connecting to the RGB Matrix Panel, [test the connection with a multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter).

[![Splice covered in heat shrink](https://cdn.sparkfun.com/r/600-600/assets/d/a/1/6/2/52a9fe66757b7f772f8b4567.jpg)](https://cdn.sparkfun.com/assets/d/a/1/6/2/52a9fe66757b7f772f8b4567.jpg)

*Spliced Wires*

Finally, cover the splice with [heat shrink](https://www.sparkfun.com/products/9353) or [electrical tape](https://www.sparkfun.com/products/10689), and voila! That\'s a beautiful power cable.

[![Finished power supply cable splice](https://cdn.sparkfun.com/r/600-600/assets/b/e/a/7/e/52a9fe68757b7f473e8b4567.jpg)](https://cdn.sparkfun.com/assets/b/e/a/7/e/52a9fe68757b7f473e8b4567.jpg)

*Finished panel power supply cable.*

This is a nice, sturdy interface between the panel and a solid power supply. If you\'re looking for something easier, but less reliable check the below option.

#### Long-Term: Mean Well Switching Power Supply

For those that want to push the panels to the limit (i.e. setting the pixels on a 32x64 panel at full white at maximum capacity), combine:

1.  A [5VDC/20A Mean Well switching power supply -](https://www.sparkfun.com/products/14098) which is more than enough for your panel.
2.  A wall adapter cable ([North America](https://www.sparkfun.com/products/14092) or [European](https://www.sparkfun.com/products/14093) standard) depending on your country.

[![Mean Well Power Supply](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/14098-01_Meanwell_5V_20A_PowerSupply.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/14098-01_Meanwell_5V_20A_PowerSupply.jpg)

#### Short-Term: Barrel Jack

Grab a 5V wall adapter. Both been tested to work with the panels as well. At least in the short term.

- [5V/2A Wall Adapter](https://www.sparkfun.com/products/12889)
- [USB 5V/1A Wall Adapter](https://www.sparkfun.com/products/11456) (with [USB Barrel Jack Adapter](https://www.sparkfun.com/products/8639))

Use the power supply in conjunction with a [female barrel jack adapter](https://www.sparkfun.com/products/10288) and [screwdriver](https://www.sparkfun.com/products/9146) to get a quick and dirty connection between the spade and barrel jack.

[![Spade connected to barrel jack adapter](https://cdn.sparkfun.com/r/600-600/assets/d/3/1/8/7/52a9fe68757b7f74598b4567.jpg)](https://cdn.sparkfun.com/assets/d/3/1/8/7/52a9fe68757b7f74598b4567.jpg)

The final connection should look like the image below.

[![Wall adapter connected via barrel jack adapter](https://cdn.sparkfun.com/r/600-600/assets/a/a/7/a/5/52a9fe67757b7f71118b4567.jpg)](https://cdn.sparkfun.com/assets/a/a/7/a/5/52a9fe67757b7f71118b4567.jpg)

## Hardware Hookup

Before we can get into the code portion, there\'s quite a bit of wiring to do. The RGB panels have a pair of 16-pin (2x8) IDC connectors, and we need to wire up to most of those pins. Conveniently, both panels have the connector pins labeled (the unlabeled pins are ground). As we\'re hooking up to the panel, make sure you use the connector labeled ***Input***. The labeling may be slightly different depending on the manufacturer.

[![Connector labels on panel](https://cdn.sparkfun.com/r/600-600/assets/7/1/b/2/2/52a9fe69757b7f9a1f8b4567.jpg)](https://cdn.sparkfun.com/assets/7/1/b/2/2/52a9fe69757b7f9a1f8b4567.jpg)

*Connector labels on a 32x32 panel. 16x32 has the same layout, except that D is a no connect (NC) instead. 32x64 has the same layout but no labels.*

**Note to 16x32 Panel Users:** The 32x16 panel has the exact same pinout as the 32x32, except there is no \"D\" pin. Instead of \"D\", that pin (12 on the connector) is a no connect (NC), you can leave it alone.

**Labels on 32x64 and 16x32 Panel Users:** On top of that, some panels do not have labels on the connector pins \-- instead there is an **arrow (◄) indicating pin 1**, in the top-left corner of the connector (it\'s obscured by the frame, but visible if you peek in at the right angle). That pin 1 arrow indicator points to the \"R0\" pin, and the pinout follows that of the 32x32 panel from there. We have also seen panels come with their pins label **G1, G2, R1, R2, B1 & B2** instead of **G0, G1, R0, R1, B0 & B1**. The wiring will be the same for both cases by connecting to the connector on the left.\
\

[![](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/14718-RGB_LED_Matrix_Panel_-_32x64-03_noLabels.jpg "Panel without Labels")](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/14718-RGB_LED_Matrix_Panel_-_32x64-03_noLabels.jpg)

### Hookup Table

Here are the pin connections between LED panel connector and Arduino:

+-----------------+------------------------+---------------------------+--------------------+------------------------------------------+
| Panel Pin Label | Cable Connector Pin \# | Arduino Uno (Atmega328P)\ | Arduino Mega 2560\ | Notes                                    |
|                 |                        | Pin                       | Pin                |                                          |
+=================+========================+===========================+====================+==========================================+
| R0              | 1                      | 2                         | 24                 | Red Data\                                |
|                 |                        |                           |                    | *(columns 1-16)*                         |
+-----------------+------------------------+---------------------------+--------------------+------------------------------------------+
| G0              | 2                      | 3                         | 25                 | Green Data\                              |
|                 |                        |                           |                    | *(columns 1-16)*                         |
+-----------------+------------------------+---------------------------+--------------------+------------------------------------------+
| B0              | 3                      | 4                         | 26                 | Blue Data\                               |
|                 |                        |                           |                    | *(columns 1-16)*                         |
+-----------------+------------------------+---------------------------+--------------------+------------------------------------------+
| GND             | 4                      | GND                                            | Ground                                   |
+-----------------+------------------------+---------------------------+--------------------+------------------------------------------+
| R1              | 5                      | 5                         | 27                 | Red Data\                                |
|                 |                        |                           |                    | *(columns 17-32)*                        |
+-----------------+------------------------+---------------------------+--------------------+------------------------------------------+
| G1              | 6                      | 6                         | 28                 | Green Data\                              |
|                 |                        |                           |                    | *(columns 17-32)*                        |
+-----------------+------------------------+---------------------------+--------------------+------------------------------------------+
| B1              | 7                      | 7                         | 29                 | Blue Data\                               |
|                 |                        |                           |                    | *(columns 17-32)*                        |
+-----------------+------------------------+---------------------------+--------------------+------------------------------------------+
| GND             | 8                      | GND                                            | Ground                                   |
+-----------------+------------------------+------------------------------------------------+------------------------------------------+
| A               | 9                      | A0                                             | Demux Input A0                           |
+-----------------+------------------------+------------------------------------------------+------------------------------------------+
| B               | 10                     | A1                                             | Demux Input A1                           |
+-----------------+------------------------+------------------------------------------------+------------------------------------------+
| C               | 11                     | A2                                             | Demux Input A2                           |
+-----------------+------------------------+------------------------------------------------+------------------------------------------+
| D               | 12                     | A3                                             | Demux Input E1, E3 *(32x32 panels only)* |
+-----------------+------------------------+------------------------------------------------+------------------------------------------+
| CLK             | 13                     | 11                                             | LED Drivers\' Clock                      |
+-----------------+------------------------+------------------------------------------------+------------------------------------------+
| STB             | 14                     | 10                                             | LED Drivers\' Latch                      |
+-----------------+------------------------+------------------------------------------------+------------------------------------------+
| OE              | 15                     | 9                                              | LED Drivers\' Output Enable              |
+-----------------+------------------------+------------------------------------------------+------------------------------------------+
| GND             | 16                     | GND                                            | Ground                                   |
+-----------------+------------------------+------------------------------------------------+------------------------------------------+

For a more step-by-step approach, follow along below. We use [male-to-male premium jumper wires](https://www.sparkfun.com/products/8431) to wire between the included ribbon cable and our Arduino.

### Connect Data Pins: R0, B0, G0, R1, G1, and B1

These LED driver (shift register) data pins are hard-coded in the Arduino library and can\'t be moved. As listed in the table above, R0, G0, B0, R1, G1, and B1 go to the Arduino Uno\'s **pins 2 through 7** respectively. If you\'re wiring the panel up to an Arduino Mega, these pins should be connected to **pins 24-29** respectively.

For reference when wiring the pins, try looking down at the IDC connector with red wire on top. The cable connector\'s pin 1 is relative to the top right. If you look really closely at the molding, you may also arrow (◄) pointing to that pin. Also, note that the tab for polarity is on the right side on either end of the cable.

[![IDC Cable Connector Polarity.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/6/RGB_LED_Panel_Matrix_Tutorial_IDC_ConnectorPolarity.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/RGB_LED_Panel_Matrix_Tutorial_IDC_ConnectorPolarity.jpg)

*IDC Connector Highlighted w/ Arrow Pointing to Pin 1*

**Tip:** The **odd** numbered pins will be along the right side with the polarity marker and the tab. The pin holes on the left will be even numbered. Depending on the manufacturer, you may have received a black connector instead of a grey.

Once you decide what side to connect, start wiring pin 1 by connecting a red wire for R0. Then connect pin 2 by connecting a green wire for G0. After connecting pin 3 using a blue wire for B0, continue wiring the pins based on the hookup table.

[![Start Wiring](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/6/RGB_LED_Panel_Matrix_Tutorial_IDC_Polarity_Wiring.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/RGB_LED_Panel_Matrix_Tutorial_IDC_Polarity_Wiring.jpg)

To help keep track of what side you are connecting to, feel free to label your connections with a marker.

[![Label Your IDC Conenctor with a Marker](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/6/RGB_LED_Panel_Matrix_Tutorial_IDC_Connector_Label.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/RGB_LED_Panel_Matrix_Tutorial_IDC_Connector_Label.jpg)

### Connecting the Clock Pin

This is the last pin that has some restriction on where it can go \-- it must be connected to one of Arduino\'s **port B** pins. That means it must be either *8, 9, 10, 11, 12, or 13*. The example code has it defined as **pin 11** in the hookup table. Make sure to check your pin definition for the clock as it may vary with the code you are using.

### Connecting to A, B, C, (D for 32x32 users), OE, and STB Pins

These five (or six if you\'re using a 32x32 matrix) pins can be plugged in anywhere you may have space on your Arduino. Although, there\'s probably not a lot of room left\... We chose to stick A, B, and C in **pins A0, A1, and A2** respectively. OE connects to **pin 9**. STB to **pin 10**. And, if you\'re using a 32x32 matrix, D goes to **A3** as stated in the hookup table.

Feel free to swap those up if your application requires. Just make sure you switch it up in the example code too.

### Connecting to Ground(s) Pins

Last, but certainly not least (well, maybe, if we\'re talking about potential) is ground. There are three unlabeled pins on the connector which should all be tied to ground.

If you don\'t have anything else plugged into them, there should be three ground pins available on your Arduino. If you\'re struggling to find ground pins, though, you should be able to get away with only plugging one of the ground pins to your Arduino. Woo [color coded](http://en.wikipedia.org/wiki/Color_code) wires!

[![Cables connected from panel to Arduino](https://cdn.sparkfun.com/r/600-600/assets/b/f/d/0/3/52a9fe69757b7faa4c8b4567.jpg)](https://cdn.sparkfun.com/assets/b/f/d/0/3/52a9fe69757b7faa4c8b4567.jpg)

### Power

Once you are finished connecting the LED panel to an Arduino, add your 5V power supply to the panel\'s power connector. Don\'t forget to add power to your Arduino!

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/9/9/0/2/8/52a9fe69757b7fa6618b4569.jpg "16x32 Fully Connected to the RedBoard")](https://cdn.sparkfun.com/assets/9/9/0/2/8/52a9fe69757b7fa6618b4569.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/0/7/9/d/2/52a9fe6a757b7f96498b4567.jpg "32x32 Fully Connected to the Arduino Mega 2560")](https://cdn.sparkfun.com/assets/0/7/9/d/2/52a9fe6a757b7f96498b4567.jpg)
  *16x32 Fully Connected to the RedBoard*                                                                                                                                                                   *32x32 Fully Connected to the Arduino Mega 2560*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Connecting to 32x64 RGB LED Panels

For anyone connecting to the 32x64 RGB Panels, you will **need** to use an Arduino Mega 2560 with the library. Otherwise, the panels will not be able to display as expected due to the limitations of the library and the Arduino Uno.

To daisy chain two 32x32 RGB matrices together, connect another IDC cable from the output of the first panel to the input of the second panel. Then connect the second 4-pin polarized connector to the input power connector. After modifying the *test_shapes_32x64.ino*, the display will output as a 32x64 matrix as shown below.

[![Arduino Mega with two 32x32 RGB LED Matrices for an array of 32x64 ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/6/RGB_LED_Panel_Matrix_Tutorial_Two_32x32_Pitch5_ArduinoMega.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/RGB_LED_Panel_Matrix_Tutorial_Two_32x32_Pitch5_ArduinoMega.jpg)

**Heads up!** When daisy chaining the RGB LED matix panels, make sure that they have the same scan rate!

Here\'s an example with the 32x64 matrix with 4mm pitch.

[![Arduino Mega with 32x64 RGB LED Matrix](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/6/RGB_LED_Panel_Matrix_Tutorial_32x64_Pitch4_ArduinoMega.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/RGB_LED_Panel_Matrix_Tutorial_32x64_Pitch4_ArduinoMega.jpg)

When using an array higher than 32x64, another library would be a better option with a Teensy 3.0+, FPGA, or Raspberry Pi. You may need to level shift to convert 3.3V to 5V for the RGB LED panel to recognize the I/O signals. For more information, check out the links in the [Resources and Going Further](https://learn.sparkfun.com/tutorials/rgb-panel-hookup-guide/all#resources--going-further).

### Custom Shield Adapter

If you have a prototyping shield, try making a custom shield adapter for a more secure connection. Here\'s an example of using an [XBee shield](https://www.sparkfun.com/products/12847)\'s prototyping area with the connection specifically for the RGB LED panels. Follow the steps outlined above but [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the connection together.

[![Custom Shield Adapter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/6/RGB_LED_Panel_Matrix_Tutorial_32x32_Pitch5_Etch_a_Sketch_Custom_ProtoShield.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/RGB_LED_Panel_Matrix_Tutorial_32x32_Pitch5_Etch_a_Sketch_Custom_ProtoShield.jpg)

### Magnetic Mounts

Depending on the supplier, you may receive a set of magnetic mounts. Add it to the panel\'s mounting holes to stick on a fridge or metal wall! They also work great as a standoff. Just make sure to secure and insulate your wires to prevent any shorts if there is metal behind the panel.

[![Magnetic Mounts](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/1/6/6/12584-RGB_LED_Panel_magnetic_mounts.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/12584-RGB_LED_Panel_magnetic_mounts.jpg)

## Arduino Library Installation

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

[] **Compatibility:** The 16x32 works at a 1:8 scan rate. The 32x32 and 32x64 examples work with a 1:16 scan rate. Depending on the manufacturer, there may be different scan rates for the the LED Matrix Panels. Using different scan rates with the example code may cause unexpected behaviors.

Our example code is going to make use of Adafruit\'s most excellent **RGBMatrixPanel** library, which also requires their **AdafruitGFXLibrary**. You can obtain these libraries through the Arduino Library Manager by searching for those names. Or you can manually install them can by grabbing both of them \[[RGBMatrixPanel](https://github.com/adafruit/RGB-matrix-Panel) and [AdafruitGFXLibrary](https://github.com/adafruit/Adafruit-GFX-Library)\] from their GitHub repositories.

For your convenience, we packaged those libraries with the serial paint example code used in the tutorial:

[Serial Paint Example Code (ZIP)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/Libraries_Examples_RGB_Matrix_LED_Panels.zip)

### Library Examples

The **RGBMatrixPanel** library includes a number of fun examples to help show how the library can be used. They\'re awesome. Check them out under the **File\_ \> *Examples* \> \_RGBMatrixPanel** menu in Arduino. (Definitely check out the *Plasma_16x32 or Plasma_32x32* examples!). Make sure to adjust the code based on your hardware hookup. In this tutorial, we physically connected the clock pin to 11. Therefore, you need to adjust the defined CLK pin from

    language:c
    // If your 32x32 matrix has the SINGLE HEADER input,
    // use this pinout:
    #define CLK 8  // MUST be on PORTB! (Use pin 11 on Mega)
    #define OE  9
    #define LAT 10
    #define A   A0
    #define B   A1
    #define C   A2
    #define D   A3

to:

    language:c
    // If your 32x32 matrix has the SINGLE HEADER input,
    // use this pinout:
    #define CLK 11  // MUST be on PORTB! (Use pin 11 on Mega) <---CHANGE!
    #define OE  9
    #define LAT 10
    #define A   A0
    #define B   A1
    #define C   A2
    #define D   A3

**32x32 Examples for 32x64:** You can also use the \"**\...\_32x32.ino**\" examples in the **RGBmatrixPanel** library by adjusting the code for the 32x64 RGB matrix panels (i.e. **colorwheel_32x32**, **plasma_32x32**, etc). Just add the number \"`64`\" as a parameter when creating an instance of the RGBmatrixPanel class:\
\
`RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false, `**`64`**`);`

## Example Code

**Heads up!** This Arduino library and example used in this tutorial has been tested for 16x32 (w/ 1:8 scan rate), 32x32 (w/ 1:16 scan rate), and 32x64 (w/ 1:16 scan rate) panels. When using a larger matrix (such as the 64x64 RGB LED matrix panel), you will need a development board that has a higher processing speed and memory due to the limitations of the library used in this tutorial. Try looking at the [Resources and Going Further](https://learn.sparkfun.com/tutorials/rgb-panel-hookup-guide#resources--going-further) at the end of this tutorial for more information on alternatives to drive a larger matrix.

### Serial Paint

We wanted to write another fun sketch that provided an interactive way to explore with the panels and the Arduino library. What we came up with is a serial-controlled paint program. With this sketch, you can use the serial monitor (or, better yet, [another terminal program](https://learn.sparkfun.com/tutorials/terminal-basics)) to control a cursor and draw on the matrix.

Download and unzip the sketch included in the zipped libraries using the link below if you have not already.

[Serial Paint Example Code (ZIP)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/6/Libraries_Examples_RGB_Matrix_LED_Panels.zip)

#### • Selecting You LED Matrix Size

Before uploading, make sure the sketch is set up to work with your panel where it says:

    language:c
    /* - One of these should be commented out!
       - Also, make sure to adjust the saved image in the <bitmap.h> file.*/

    /* ========== For 32x64 LED panels: ==========
      You MUST use an Arduino Mega2560 with 32x64 size RGB Panel */
    //RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false, 64); // 32x64

    /* ========== For 32x32 LED panels: ========== */
    RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false); // 32x32

    /* ==========  For 32x16 LED panels: ========== */
    //RGBmatrixPanel matrix(A, B, C, CLK, LAT, OE, false); // 32x16

By default, the Serial Paint example uses the 32x32. If you are using 32x64, make sure to uncomment the following line by removing the \"`//`\"

    language:c
    //RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false, 64); // 32x64

Then comment out the following line by adding a \"`//`\" at the beginning of the line.

    language:c
    RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false); // 32x32

#### • Selecting the Saved Bitmap Image

Make sure to also uncomment/comment out the `bmp[]` array in the ***bitmap.h*** file by removing and adding \"`/*`\" and \"`*/`\" for your respective size.

#### • Upload!

Once you have adjusted the code to your screen, upload it to the Arduino! After upload, a single pixel should be blinking at the top left of the panel. It doesn\'t look like much, but that\'s a good sign.

### Using the Sketch

To control the program, open up your serial terminal to **9600 bps**. Try hitting sending `l` (lowercase \'L\') through the serial monitor, which should load the demo bitmap. You can send `E` (uppercase) to erase the screen.

The idea of this sketch is: move the cursor around to draw pixels, shapes, or text. Here are the commands made available by the sketch (they are case-sensitive):

- **Movement**: `w`, `a`, `s`, `d` (up, down, left, right)
- **Draw Pixel**: `Spacebar`
- **Erase Pixel**: `e`
- **Erase Screen**: `E`
- **Fill screen** with active color: `f`
- **Color Control:**
  - **Red value up**: `R` (values between 0 \[off\] and 7 \[most bright\])
  - **Red value down**: `r`
  - **Green up/down**: `G`/`g`
  - **Blue up/down**: `B`/`b`
  - **Copy color**: `z` (copies a color under the cursor)
- **Shape Drawing:**
  - **Line**: press `v` to place starting point. Then move cursor to endpoint and press `v` **again**.
  - **Rectangle**: press `x` or `X` to place first corner. Then move your cursor to where you want the diagonal corner. Then press either `x` for an **empty** box, or `X` for a **filled** box.
  - **Circle**: press `c` or `C` to place the *center* of the circle. Then move your cursor to where you want the outside edge of your circle to be. Then press `c` for an **empty** circle or `C` for a **filled** circle.
- **Text**: press `t` to go to text mode. Now **any characters** received will be displayed on the panel. It\'ll wrap around from one line to the next, but not from bottom to top. Press `` ` `` (above Tab / left of 1) to exit text mode.
- **Print**: press `p` to print an array of your drawing to the serial terminal. You can copy this, and put it back in your sketch if you want to load it again.
- **Load**: press `l` to load a pre-defined array from the sketch. The sketch includes a demo array, which was created from the print command. Follow this example to load your own drawings!

Give the paint sketch a try! See if you can make the next great ~~[Lite-Brite](https://cdn.sparkfun.com/assets/0/d/6/d/6/52a8a998757b7f4b638b456c.jpg)~~ LED Panel picture. If you make something neat, share it with us! Don\'t laugh. I drew that SFE flame one pixel at a time! Here are our creations:

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/2/f/e/e/3/52a9fe69757b7f1a038b4568.jpg)](https://cdn.sparkfun.com/assets/2/f/e/e/3/52a9fe69757b7f1a038b4568.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/e/c/3/0/9/52a9fe68757b7fc95d8b4567.jpg "32x32 panel image")](https://cdn.sparkfun.com/assets/e/c/3/0/9/52a9fe68757b7fc95d8b4567.jpg)
  *A drawing on the 16x32 panel.*                                                                                                                                   *An example drawing on the 32x32 panel.*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Try modifying the code to change the color and move around the matrix using potentiometers and buttons. You can see it in action in our [product showcase](http://www.youtube.com/watch?v=2KZR3rwEHg8&feature=youtu.be&t=3m18s):