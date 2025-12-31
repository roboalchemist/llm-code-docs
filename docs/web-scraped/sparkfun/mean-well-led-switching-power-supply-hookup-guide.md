# Source: https://learn.sparkfun.com/tutorials/mean-well-led-switching-power-supply-hookup-guide

## Introduction

In this tutorial, we will be connecting a Mean Well LED switching power supply ([5V/25W](https://www.sparkfun.com/products/14601) or [5V/40W](https://www.sparkfun.com/products/14602)) to an addressable LED strip controlled by an Arduino.

[![Mean Well LED Switching Power Supply - 5VDC, 5A](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/7/6/3/14601-Mean_Well_LED_Switching_Power_Supply_5V_25W-01.jpg)](https://www.sparkfun.com/products/14601)

### [Mean Well LED Switching Power Supply - 5VDC, 5A](https://www.sparkfun.com/products/14601) 

[ TOL-14601 ]

This is a 40W single output switching power supply from Mean Well that has been specifically designed to be with LED applicat...

**Retired**

[![Mean Well LED Switching Power Supply - 5VDC, 8A](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/7/6/4/14602-Mean_Well_LED_Switching_Power_Supply_5V_40W_-01.jpg)](https://www.sparkfun.com/products/14602)

### [Mean Well LED Switching Power Supply - 5VDC, 8A](https://www.sparkfun.com/products/14602) 

[ TOL-14602 ]

This is a 40W single output switching power supply from Mean Well that has been specifically designed to be with LED applicat...

**Retired**

### Required Materials

To follow along with this tutorial, you will need the following materials with the Mean Well 5V power supply. This is assuming that you are using the wall adapter cable for 120VAC. For the load, we will be using an addressable LED strip. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![Terminal Block - 6 Position (15A, 600V)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/0/9/2/13061-01.jpg)](https://www.sparkfun.com/terminal-block-6-position-15a-600v.html)

### [Terminal Block - 6 Position (15A, 600V)](https://www.sparkfun.com/terminal-block-6-position-15a-600v.html) 

[ PRT-13061 ]

This 6 position screw terminal block provides a simple way to connect wires to a single connection point.

[ [\$3.10] ]

[![Terminal Block - 3 Position (15A, 600V)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/0/9/1/13060-01.jpg)](https://www.sparkfun.com/products/13060)

### [Terminal Block - 3 Position (15A, 600V)](https://www.sparkfun.com/products/13060) 

[ PRT-13060 ]

This 3 position screw terminal block provides a simple way to connect wires to a single connection point. These blocks allow ...

**Retired**

[![iPixel Wall Adapter Cable - Two Terminal (NA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/6/5/14603-iPixel_Wall_Adapter_Cable_-_Two_Prong__NA_-01.jpg)](https://www.sparkfun.com/products/14603)

### [iPixel Wall Adapter Cable - Two Terminal (NA)](https://www.sparkfun.com/products/14603) 

[ CAB-14603 ]

These Wall Adapter Cables from iPixel are terminated with a standard NA plug at one end and two insulated spade terminal conn...

**Retired**

[![Skinny LED RGB Strip - Addressable, 1m, 60LEDs (SK6812)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/5/7/14612-Skinny_LED_RGB_Strip_-_Addressable__1m__60LEDs__SK6812__-01.jpg)](https://www.sparkfun.com/products/14730)

### [Skinny LED RGB Strip - Addressable, 1m, 60LEDs (SK6812)](https://www.sparkfun.com/products/14730) 

[ COM-14730 ]

These are skinny addressable 1-meter-long 5V RGB LED strips that come packed with 60 SK6812s. SK6812 LEDs are very similar to...

**Retired**

### Suggested Tools

Depending on your setup, you may need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49). Otherwise, a screw terminal block and a screw driver is sufficient.

[![Digital Multimeter - Basic](https://cdn.sparkfun.com/r/140-140/assets/parts/9/9/0/7/12966-01.jpg)](https://www.sparkfun.com/digital-multimeter-basic.html)

### [Digital Multimeter - Basic](https://www.sparkfun.com/digital-multimeter-basic.html) 

[ TOL-12966 ]

The digital multimeter (DMM) is an essential tool in every electronic enthusiasts arsenal. The SparkFun Digital Multimeter, h...

[ [\$21.50] ]

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

You will also need:

- Electrical Tape
- Surge Protector

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/electric-power)

### Electric Power 

An overview of electric power, the rate of energy transfer. We\'ll talk definition of power, watts, equations, and power ratings. 1.21 gigawatts of tutorial fun!

[](https://learn.sparkfun.com/tutorials/ws2812-breakout-hookup-guide)

### WS2812 Breakout Hookup Guide 

How to create a pixel string with the WS2812 and WS2812B addressable LEDs!

[](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)

### How to Use a Multimeter 

Learn the basics of using a multimeter to measure continuity, voltage, resistance and current.

## Hardware Overview

**Heads up!** There are a few versions of the switching power supplies. We will be using the 5V series of the power supplies.

The Mean Well APV-35 and LPV-60 series power supplies were designed to power LEDs. They include wire pairs for the input (brown and blue) and output (red and black). The input voltage requires an AC power cable to be connected that is not included with the power supply. The APV-35-5 provides **5V with up to 5.0A**. The LPV-60-5 provides **5V with up to 8.0A**.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![APV-35 Series 5V/5A](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/14601-Mean_Well_LED_Switching_Power_Supply_5V_25W-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/14601-Mean_Well_LED_Switching_Power_Supply_5V_25W-02.jpg)   [![LPV-60 Series 5V/8A](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/14602-Mean_Well_LED_Switching_Power_Supply_5V_40W_-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/14602-Mean_Well_LED_Switching_Power_Supply_5V_40W_-02.jpg)
  *APV-35 Series*                                                                                                                                                                                                                                            *LPV-60 Series*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Pinout

  Mean Well Power Supply   Notes
  ------------------------ -----------------------------------------------------------------
  ACL *(Brown)*            Input AC Voltage, Live/Hot wire
  ACN *(Blue)*             Input AC Voltage, Neutral Wire, Wider Blade on Wall Outlet Side
  V+ *(Red)*               Output Voltage (DC)
  V- *(GND, Black)*        Output Ground (DC)

## Hardware Assembly

**Note:** The tutorial follows the [North American standard wiring](https://en.wikipedia.org/wiki/Electrical_wiring) at 120VAC for a [polarized cable](https://en.wikipedia.org/wiki/AC_power_plugs_and_sockets#North_American_and_IEC_60906-2). If you are unsure about the standard wiring color in your region, please consult a certified electrician to connect to the AC input voltage side.

### Hookup Table

The following is the hookup table for connecting a wall adapter cable to a Mean Well power supply and then to your load. Ensure that the cable is not connected to a wall outlet when making the following connections between the cable and Mean Well power supply!

  120VAC Outlet (North American Standard)   Mean Well Power Supply   Load (i.e. LED Strips)   Notes
  ----------------------------------------- ------------------------ ------------------------ -----------------------------------------------------------------
  LIVE/HOT Wire *(Black)*                   ACL *(Brown)*                                     Input AC Voltage, Live/Hot wire
  NEUTRAL Wire *(White)*                    ACN *(Blue)*                                      Input AC Voltage, Neutral Wire, Wider Blade on Wall Outlet Side
                                            V+ *(Red)*               5V                       Output Voltage (DC)
                                            V- *(GND, Black)*        GND                      Output Ground (DC)

### Connecting the AC Input Voltage w/ Screw Terminals

⚡ **Warning!** Make sure that your wires are secure and are rated to handle the current! Please be careful with the spade terminals when the cable is plugged into a wall outlet. **Touching the terminals while powered could result in injury.**

Before beginning, make sure the power cable is unplugged from the wall outlet. Carefully remove the plastic cover on the terminal block by wiggling it back and forth from the black housing.

[![Remove Plastic Cover](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Removing_Plastic_Cover_from_Terminal_Block.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Removing_Plastic_Cover_from_Terminal_Block.jpg)

Insert the hot wire\'s spade connector into a terminal block between the metal plates.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Insert Spade Connector Between Metal Plates](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Insert_Hot_Wire_Spade_Connector_Between_Metal_Square_Nuts_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Insert_Hot_Wire_Spade_Connector_Between_Metal_Square_Nuts_1.jpg)   [![Inserted Spade Connector Between Metal Plates](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Insert_Hot_Wire_Spade_Connector_Between_Metal_Square_Nuts_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Insert_Hot_Wire_Spade_Connector_Between_Metal_Square_Nuts_2.jpg)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tighten the screw. Pull wire gently to see if it is secure.

[![Tighten Screws on Terminal Blocks](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Tighten_Screw_Screw_Terminal.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Tighten_Screw_Screw_Terminal.jpg)

Repeat for the neutral wire\'s spade connector.

[![Insert Mean Well Power Supply\'s Neutral Wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Repeat_for_Neutral_Wire.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Repeat_for_Neutral_Wire.jpg)

Connect the hot wire to the Mean Well\'s hot wire by inserting the wire between the metal plates and tightening the screw.

[![Insert Mean Well Power Supply\'s Hot Wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Connect_Mean_Well_Hot_Wire_to_Other_Side.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Connect_Mean_Well_Hot_Wire_to_Other_Side.jpg)

Remember to pull the wire gently to see if the connection is secure.

[![Pull Wire to Check If Secure](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Pull_Wire_to_Verify_Secure_Wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Pull_Wire_to_Verify_Secure_Wires.jpg)

Repeat for the input neutral wire.

[![Repeat for Neutral Wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Connect_Mean_Well_Neutral_Wire.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Connect_Mean_Well_Neutral_Wire.jpg)

### Connecting the DC Output Voltage w/ Screw Terminals

Connect your Mean Well power supply\'s output ground wire to one side of the terminal block.

[![Connect DC Output Ground](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Connect_DC_Ground.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Connect_DC_Ground.jpg)

Connect the output voltage\'s wire to another screw terminal.

[![Connect DC Output Voltage](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Connect_DC_Voltage.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Connect_DC_Voltage.jpg)

Connect your load wires to the other side of the Mean Well output voltage.

[![Connect Load](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Connect_Load_Wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Connect_Load_Wires.jpg)

### Other Methods of Connecting to the Mean Well Power Supply

You can also splice the wires or use spade connectors depending on your preference. If you decide to connect with a [spade connector](https://www.sparkfun.com/products/14407), make sure that you are using the correct tool to [properly crimp the connection](https://learn.sparkfun.com/tutorials/working-with-wire#how-to-crimp-an-electrical-connector). Needle nose pliers may not provide sufficient force to clamp the spade connector against the wires. Ensure that the power cable is unplugged from the wall outlet.

[![Connect Spade Connectors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Connect_Spade_Connectors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Connect_Spade_Connectors.jpg)

Remember to insulate your connections with electrical tape or heat shrink so that the connections are not exposed.

[![Insulate Wires for VAC](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Insulate_Exposed_Spade_Connectors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Insulate_Exposed_Spade_Connectors.jpg)

Once connected, make sure to test it out with a multimeter and surge protector before installing.

### Testing the Output

Let\'s test the power supply using a multimeter to see if we connected everything properly! To safely test, we will be using alligator clips, probes, and a breadboard to measure the output voltage to see if we get our expected voltage. If you are confident in your connections, you can also connect a multimeter\'s alligator clips directly to the output. Insert the two prong cable into a surge protector that is turned OFF. When ready, flip the switch on your surge protector to the ON position to provide power.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Testing the APV-35 Series Output voltage](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Test_with_Multimeter.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Test_with_Multimeter.jpg)   [![Testing the LPV-60 Series Output Voltage](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Power_Up_and_Test_Mean_Well_Power_Supply.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Power_Up_and_Test_Mean_Well_Power_Supply.jpg)
  *Testing the APV-35 Series Output Voltage*                                                                                                                                                                                *Testing the LPV-60 Series Output Voltage*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you are measuring a voltage that is close to your Mean Well power supply\'s output voltage rating, you are good to go!

### Adding a Load

Remove power and connect your load to the output. In this case, I decided to power an addressable LED strip using an Arduino and custom built shield.

[![Adding an LED Strip as a Load](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Mean_Well_with_Addressable_LED_Strip_and_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Mean_Well_with_Addressable_LED_Strip_and_Arduino.jpg)

[![Powered LED Strip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Mean_Well_with_Addressable_LED_Strip_and_Arduino_In_Dark_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Mean_Well_with_Addressable_LED_Strip_and_Arduino_In_Dark_1.jpg)

For safety and installation, make sure to add electrical tape around the exposed input voltage side and mount the electronics securely in an [enclosure](https://www.sparkfun.com/products/11366).

[![Big Red Box - Enclosure](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/7/11366-01.jpg)](https://www.sparkfun.com/big-red-box-enclosure.html)

### [Big Red Box - Enclosure](https://www.sparkfun.com/big-red-box-enclosure.html) 

[ PRT-11366 ]

This is the Big Red Box! These beefy, bright red, flanged, plastic enclosures will give your widget the protection (and atten...

[ [\$10.95] ]

### [][Power Large Loads and Daisy Chained LED Strips](#daisychain)

When daisy chaining your addressable LED strips, there may be a voltage drop depending on the:

- amount of LEDs connected
- length of LED strip
- how bright the LEDs are set
- animation

Below is an image of addressable LED strips daisy chained together and controlled by Arduino. The Arduino was programmed to turn on all the LEDs at full brightness using one 5V/25W power supply as an extreme case.

[![Daisy Chained LED Strips](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Power_Supply_with_Daisy_Chained_Addressable_LED_Strips.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Power_Supply_with_Daisy_Chained_Addressable_LED_Strips.jpg)

As you can see from the image below, the LEDs are not able to fully turn on after a certain length due to the voltage drop. This is due to the increased resistance as you move further away from the power supply. You may notice that not all the colors are turned on or the strip becomes dim. You can also [check the voltage after each meter using a multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter/measuring-voltage) to see if there are any voltage drops if you are not able to visually see the voltage drops.

[![Voltage Drops with Daisy Chained LED Strips with RGB Colors Turnned on at Full Brightness](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Brown_Out_with_Addressable_LED_Strips.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Brown_Out_with_Addressable_LED_Strips.jpg)

**Warning:** Turning on all the LEDs at full brightness is an extreme case. Higher density LED strips may not be able to handle the power and dissipate heat properly. It is recommended to use a lower brightness setting.

If you see voltage drops and the LED strip not properly turning on, you will need to connect the Mean Well\'s output between each LED strip\'s Vcc and GND after about 1, 2, or 5 meters. Your circuit may look similar to this setup if you daisy chain the LED strip and inject power between each cable.

[![Daisy Chained LED Strips](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Large-Installation-Addressable-LEDs-WS2812-APA-Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Large-Installation-Addressable-LEDs-WS2812-APA-Fritzing_bb.jpg)

*Click image for a closer view.*

Once connected, your power supply should have a connection between each LED strip.

[![Power Injection Between LED Strips](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Power_Supply__between_Daisy_Chained_Addressable_LED_Strips.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Power_Supply__between_Daisy_Chained_Addressable_LED_Strips.jpg)

**Warning:** Make sure to use appropriate wire gauges that can handle the current. The example shown here was a temporary setup for testing. When using the LED strips for permanent installations, you will want to avoid using a breadboard and thin wires to power a large amount of LEDs.

As you can see from the image below, the LEDs throughout the strip are able to fully turn on when connecting power between each LED strip.

[![LEDs Fully Turned On at Full Brightness as Expected](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Power_Supply__between_Daisy_Chained_Addressable_LED_Strips_Lit_Up_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Power_Supply__between_Daisy_Chained_Addressable_LED_Strips_Lit_Up_1.jpg)

Again, turning on all the LEDs at full brightness is an extreme case. You may be able get away with injecting power after more than a few meters if your setup uses a lower brightness setting and sequencing the LEDs.

[![LED Strips with Lower Brightness and Animated](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Power_Supply__between_Daisy_Chained_Addressable_LED_Strips_Lit_Up_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Power_Supply__between_Daisy_Chained_Addressable_LED_Strips_Lit_Up_2.jpg)

⚡ **Using More Than One Power Supply Unit?** If you are using more than one power supply for larger installations, it is recommended to disconnect the Vcc wire between each section\'s JST cable so that they are not conflicting. The data line(s) for data and ground for reference will still be connected.\
\

[![Daisy Chained LED Strip Powered with Multiple Power Supplies](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/7/9/Large-Installation-2-Addressable-LEDs-WS2812-APA-Multiple-Power-Supplies-Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Large-Installation-2-Addressable-LEDs-WS2812-APA-Multiple-Power-Supplies-Fritzing_bb.jpg)

\

*Click on image for closer view.*

⚡ **Need More Power?** You could also use a beefier power supply like the Mean Well 5V/20A with an adapter cable for your region.\
\

[![Adam Tech Wall Adapter Cable - Three Terminal (NA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/9/5/7/14092-01.jpg)](https://www.sparkfun.com/products/14092)

### [Adam Tech Wall Adapter Cable - Three Terminal (NA)](https://www.sparkfun.com/products/14092) 

[ CAB-14092 ]

These Adam Tech Wall Adapter Cables are terminated with a standard North American (NEMA 5\--15P) plug at one end and three ins...

**Retired**

[![Adam Tech Wall Adapter Cable - Three Terminal (EU)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/9/5/8/14093-01.jpg)](https://www.sparkfun.com/adam-tech-wall-adapter-cable-three-terminal-eu.html)

### [Adam Tech Wall Adapter Cable - Three Terminal (EU)](https://www.sparkfun.com/adam-tech-wall-adapter-cable-three-terminal-eu.html) 

[ CAB-14093 ]

These Adam Tech Wall Adapter Cables are terminated with a standard European (CEE 7/7) plug at one end and three insulated spa...

[\$4.95] [ [\$2.95] ]

[![Mean Well Switching Power Supply - 5VDC, 20A](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/9/7/0/14098-01.jpg)](https://www.sparkfun.com/products/14098)

### [Mean Well Switching Power Supply - 5VDC, 20A](https://www.sparkfun.com/products/14098) 

[ TOL-14098 ]

This is a 100W single output switching power supply from Mean Well. This power supply is extremely reliable and able to outpu...

**Retired**