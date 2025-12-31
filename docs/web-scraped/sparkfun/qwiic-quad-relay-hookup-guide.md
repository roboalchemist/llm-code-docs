# Source: https://learn.sparkfun.com/tutorials/qwiic-quad-relay-hookup-guide

## Introduction

[SparkFun\'s Qwiic Quad Relay](https://www.sparkfun.com/products/16566) is a product designed for switching not one but **four high powered devices** from your Arduino or other low powered microcontroller using I^2^C. It has four [relays](https://www.sparkfun.com/products/100) rated up to 5 Amps per channel at 250VAC or 30VDC that are controlled by an ATtiny84A. Each channel has its own blue stat LED, silk for easy identification, and screw terminals for easy connection. The product is *Qwiic* enabled allowing you to easily integrate the Quad Relay with other products in the [Qwiic environment](https://www.sparkfun.com/qwiic), which means no solder neccessary!

[![SparkFun Qwiic Quad Relay](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/4/4/9/16566-SparkFun_Quad_Relay__Qwiic_-01a.jpg)](https://www.sparkfun.com/sparkfun-qwiic-quad-relay.html)

### [SparkFun Qwiic Quad Relay](https://www.sparkfun.com/sparkfun-qwiic-quad-relay.html) 

[ COM-16566 ]

The SparkFun Qwiic Quad Relay is a unique power accessory board, used for switching 4 high powered devices from your Arduino ...

**Retired**

⚡ **Before we begin!** There are a number of safety precautions included in the product, but that can not account for human inexperience and error. This product and the example below interacts with **HIGH** AC voltage and so is intended for people experienced around, and knowledgeable about **HIGH** AC voltage. If that\'s not quite your jam, then take a look at our [IoT Power Relay](https://www.sparkfun.com/products/14236)! It\'s not I^2^C but the IoT Power Relay contains shielding to prevent accidental shock.

### Required Materials

For the example under **Hardware Assembly**, I used the following materials to control a load (i.e. a lamp). You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Jumper Wires - Connected 6\" (M/M, 20 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/6/1/3/12795-00.jpg)](https://www.sparkfun.com/jumper-wires-connected-6-m-m-20-pack.html)

### [Jumper Wires - Connected 6\" (M/M, 20 pack)](https://www.sparkfun.com/jumper-wires-connected-6-m-m-20-pack.html) 

[ PRT-12795 ]

These are 6\" long jumper wires with male connectors on both ends. Use these to jumper from any female header on any board, to...

[ [\$2.95] ]

[![Tactile Button Assortment](https://cdn.sparkfun.com/r/140-140/assets/parts/4/7/0/5/10302-01.jpg)](https://www.sparkfun.com/tactile-button-assortment.html)

### [Tactile Button Assortment](https://www.sparkfun.com/tactile-button-assortment.html) 

[ COM-10302 ]

This is a simple 12-pack of momentary, multicolor buttons, great for all sorts of projects!

[ [\$5.95] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/5/TOL-15312-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html)

### [Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html) 

[ TOL-15312 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA Barrel Jack wall power supply manufactured specifically for S...

[ [\$9.50] ]

[![Breadboard - Mini Modular (Red)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/6/2/7/12044-01.jpg)](https://www.sparkfun.com/breadboard-mini-modular-red.html)

### [Breadboard - Mini Modular (Red)](https://www.sparkfun.com/breadboard-mini-modular-red.html) 

[ PRT-12044 ]

This red Mini Breadboard is a great way to prototype your small projects! With 170 tie points there\'s just enough room to bui...

[ [\$4.50] ]

### Additional Options

You could also use our 9 volt wall adapter if that suits your fancy and we have a number of Qwiic cable sizes to fit your needs.

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Wall Adapter Power Supply - 9VDC 650mA](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/5/00298-01a.jpg)](https://www.sparkfun.com/products/298)

### [Wall Adapter Power Supply - 9VDC 650mA](https://www.sparkfun.com/products/298) 

[ TOL-00298 ]

High quality switching \'wall wart\' AC to DC 9V 650mA wall power supply manufactured specifically for Spark Fun Electronics. T...

**Retired**

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

**Retired**

[![Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/4/14428-Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/products/14428)

### [Qwiic Cable - 200mm](https://www.sparkfun.com/products/14428) 

[ PRT-14428 ]

This is a 200mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/5/14429-Qwiic_Cable_-_500mm-01.jpg)](https://www.sparkfun.com/products/14429)

### [Qwiic Cable - 500mm](https://www.sparkfun.com/products/14429) 

[ PRT-14429 ]

This is a 500mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

### Tools

You will need a flush cutter and wire stripper to remove the sheath and insulation from a cable. A Phillips head screwdriver will be required to connect the load\'s to a screw terminal.

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

[![Flush Cutters - Xcelite](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/3/6/14782-Flush_Cutters_-_Xcelite-02.jpg)](https://www.sparkfun.com/products/14782)

### [Flush Cutters - Xcelite](https://www.sparkfun.com/products/14782) 

[ TOL-14782 ]

These are simple flush cutters from Excelite that give you a way to cut leads very cleanly and close to the solder joint.

**Retired**

[![Self-Adjusting Wire Strippers](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/1/4/8/14872-Self-Adjusting_Wire_Strippers-04.jpg)](https://www.sparkfun.com/products/14872)

### [Self-Adjusting Wire Strippers](https://www.sparkfun.com/products/14872) 

[ TOL-14872 ]

The Self-Adjusting Wire Stripper can take a wire, placed in the head of the tool, compress the handles, and you will have a p...

**Retired**

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Overview

**Revision Changes:** This guide is for the Qwiic Quad Relay [v2.0 \[ COM-16566 \]](https://www.sparkfun.com/products/16566) and [v1.0 \[ COM-15102 \]](https://www.sparkfun.com/products/15102). There are some improvements to the design for reliability but overall, they should function the same. below is a list of changes for v2.0.\
\

- Included a normally open jumper for the power LED.
- Switching regulator in place of a linear regulator.
  - The switching regulator is much more efficient; no external cooling needed when powering four relays at once.
- Improved circuitry around the relays.
  - An issue where relays on certain boards in v1.0 didn\'t switch completely when actuated has been resolved.

The image on the left is v2.0 while the right is v1.0. You\'ll notice that the circuit to regulate the voltage by the barrel jacks are different. If you flip over either version, you will find the board\'s version number just under the relay labeled as `4`.\
\

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![v2.0](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/16566-SparkFun_Quad_Relay__Qwiic_-04a.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/16566-SparkFun_Quad_Relay__Qwiic_-04a.jpg)   [![v1.0](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/15102-SparkFun_Qwiic_Quad_Relay-05a.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/15102-SparkFun_Qwiic_Quad_Relay-05a.jpg)
  *v2.0*                                                                                                                                                                                                        *v1.0*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Power

**Heads up!** The circuit to regulate the voltage is different in v2.0. The maximum voltage is now 12V.

There are two separate power systems on the Quad Relay: a 5V system that powers the relays and a 3.3V system that powers the on board ATtiny84A and interfaces with a microcontroller through the four pin header or Qwiic connector.

The on board barrel jack takes a power source in a range of **7-12V**. It regulates the voltage and supplies power to the 5V power system of the relays. If your wall adapter or power source is at 5 volts like our [5V/2A Wall adapter](https://www.sparkfun.com/products/12889) then you can close the jumper on the underside of the product labeled **5V Wall Adapter** (see **Jumpers** section below), and this will allow you to sidestep the on board regulator to power the 5V system directly. If you decide to go with a higher voltage wall adapter, be cognizant that the voltage regulator will start to heat up. With all the relay channels turned on the Quad Relay will pull \~250mA of current and at 9 Volts, that\'s 2.25 Watts of power (mathematical!). Over time the regulator will get hot, but will remain functional. I suggest that if you expect to have all relay channels on for extended periods of time, that you go with a 5V power supply.

[![Input Power Barrel Jack](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/16566-SparkFun_Quad_Relay_Qwiic_Power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/16566-SparkFun_Quad_Relay_Qwiic_Power.jpg)

To provide 3.3V to the on board ATtiny84A you can use the plated through hole labeled **3V3** on the four pin header. Alternatively, you can plug a Qwiic connector into one of the two Qwiic connectors.

[![PTH Pins and Qwiic Connectors for Power](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/16566-SparkFun_Quad_Relay_Qwiic_Power_Alternative.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/16566-SparkFun_Quad_Relay_Qwiic_Power_Alternative.jpg)

### Relays

There are four single pole, double throw [JZC-11F relays](https://www.sparkfun.com/products/100) on the Qwiic Quad Relay. Each relay is capable of 5 Amps at 250VAC or 30VDC. These relays have an associated **blue screw pin terminals** that are aligned in order from left to right.

[![Relays](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/16566-SparkFun_Quad_Relays.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/16566-SparkFun_Quad_Relays.jpg)

### LEDs

There is a red power LED labeled **PWR** that indicates power from the barrel jack. There is also a blue stat LED for each relay labeled with their respective number **1-4**. Whenever a relay is activated (i.e. when COM is connected to NO), the respective LED will light up.

[![Relays and Screw Terminals](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/16566-SparkFun_Quad_Relay_Qwiic_Status_LEDs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/16566-SparkFun_Quad_Relay_Qwiic_Status_LEDs.jpg)

### Jumpers

There are three jumpers on the underside of the Qwiic Quad Relay.

- LED - The first jumper is for the power LED. [Close the jumper](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces) to eanble the power LED.
- ADDR - The second is the address jumper that changes the default I^2^C address from **0x6D** to **0x6C**.
- BYP - The thirdis the jumper labeled **5V Wall Adapter Jumper**. If you intend to use a wall adapter or other power source that is below 7-15V than you can close this jumper to side step the on board voltage regulator, and provide 5V directly to the 5V power system.

[![Jumper Pads](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/16566-SparkFun_Quad_Relay_Qwiic_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/16566-SparkFun_Quad_Relay_Qwiic_Jumpers.jpg)

**Note:** In v1.0, there were only two jumpers on the back of the board. With v2.0, there is now an additional jumper for the power LED.

### Qwiic Connectors

The Qwiic connectors allow you to integrate easily into our [Qwiic environment](www.sparkfun.com/qwiic) and allows you to prototype *without* the need for soldering! The 3.3V provided by the Qwiic connector will power the on board ATtiny84A. If you do not power the 3.3V power system this way, you can still provide power through the four pin header.

[![Qwiic Connectors](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/Qwiic_connectors_nw.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/Qwiic_connectors_nw.jpg)

### Board Dimensions

The board size is 3.25\"x 1.85\". There are 5x mounting holes on the board, four of which are on each corner of the board. The fifth mounting hole near the upper left of the board is included should you decide to attach a Qwiic enabled device using the 1.0\"x1.0\" sized board.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/9/8/a/7/d/Qwiic_Quad_Relay_Board_Dimensions.png)](https://cdn.sparkfun.com/assets/9/8/a/7/d/Qwiic_Quad_Relay_Board_Dimensions.png)

### Safety Considerations

This product is designed to switch high power AC or DC and so has some inherent dangers. We\'ve done our best to implement safety features directly into the design. To begin, the copper ground pour for the ATtiny84A circuitry is restricted to an area apart from the relays. In regards to the microcontroller, there are opto-isolators that isolate the 3.3V power system that it utilizes from the 5V power system of the relays. Next, the common pin of the relays have an air gap surrounding the pin on three sides to prevent any high voltage arcing. Finally, the traces on the relays are extra wide to handle the high amperage carrying potential of the relays.

## Hardware Assembly

### Introduction to Relays

Let\'s walk through how to setup the relay to switch on a lamp or other device, but let\'s begin with a short introduction into relays. A relay is a [**switch**](https://learn.sparkfun.com/tutorials/switch-basics). However, unlike most switches, within the relay\'s housing there is also a switching mechanism that is *isolated* from the switch. This is the relay\'s defining feature because this separation between switching mechanism and switch, as well as the switching mechanism\'s low-power requirements, allows for low-power microcontrollers to activate the switching mechanism without interfacing with whatever is getting \"switched\". Shmow-zow!

We have three channels per relay broken out to blue screw pin terminals. The channels are labeled for their function. One is considered *normally open* or **NO**, the next channel is *common* or **COM**, and the final is *normally closed* or **NC**. The names explain the state of the channel with relation to the switch at rest. The *normally closed* channel is where the switch sits before the switching mechanism has been activated and conversely the *normally open* channel is where the switch would sit after. The *common* channel is, as the name implies, what the other two channels have in common. This is known as a single pole, double throw switch (**SPDT**). The image below helps to illustrate this characteristic of our particular relay.

[![SPDT Switch ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/9/single_pole_double_throw_with_text.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/single_pole_double_throw_with_text.jpg)

When the switching mechanism is activated the thicker bar in the image above that connects *normally closed* to *common* flips over to connect *normally open* and *common*.

### Assembly

Onto the assembly. First, I\'m using a [BlackBoard](https://www.sparkfun.com/products/14669) for it\'s [Qwiic](https://www.sparkfun.com/qwiic) capabilities and it\'s powered via micro-USB. I have a button plugged into a breadboard, straddling the gap in the center, and jumper wires connecting it to pin 2 and GND on the blackboard.

[![BlackBoard with Button and Qwiic Cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/9/Quad_Relay_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/Quad_Relay_Hookup_Guide-03.jpg)

On the tail end is a Qwiic connector leading to the Quad Relay.

⚡ **Warning!** Make sure the lamp is **not** plugged into the wall as you cut into the wire in the following section.

Let\'s take a quick look at the lamp wire, before we look at the Quad Relay. Our goal here is to sever one of the two lamp wires, and plug the two ends of the cut wire into the relay which will reconnect the wire when we activate the switching mechanism. First, I\'ve cut one of the two wires as shown to create a break in the connection.

[![Cutting Cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/9/cutting_wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/cutting_wires.jpg)

I then peeled the wire apart and [stripped the two ends](https://learn.sparkfun.com/tutorials/working-with-wire#stranded-vs-solid).

[![Strip Wire Ends](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/9/cut_wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/cut_wires.jpg)

We\'ll put one end of our wire in the **COM** channel, and the other we\'ll have to decide upon. For this project we want our switch to act intuitively: when you activate the switching mechanism, the light switches on. There could be a case where you want the switching mechanism activated as its \"rest\" state. Since we\'re going with a more normal approach we\'ll cut our wire and place one end in *common* and the other in the *normally open* channel. Now when we activate the switching mechanism, the severed wire will be reconnected when the switch flips to the *normally open* channel connecting it and the *common* channel.

For the quad relay, I\'m powering the 5V system (the relays), with a [5V Wall Adapter](https://www.sparkfun.com/products/12889), and the **5V Wall Adapter** jumper closed underneath. The Qwiic cable from the black board is providing power to the 3.3V system as seen at the top of the picture below, and we have the lamp cable plugged into and the screw terminals tightened down on channels **COM** and **NO**.

[![Connection on Qwiic Quad Relay Side](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/9/relay_wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/relay_wires.jpg)

⚡ **Warning!** Make sure that your wires connecting to the wall outlet are secure and are rated to handle the current! Please be careful when handling the contacts when the cable is plugged into a wall outlet. **Touching the contacts while powered could result in injury.**\
\
Looking for information about safety and insulation? Check out the notes about [Safety and Insulation from our Beefcake Relay Control Kit](https://learn.sparkfun.com/tutorials/beefcake-relay-control-hookup-guide/saftey-and-insulation).

Now that our hardware is all set up, let\'s take a look at the code that turns the lamp on. Remember to not touch the relay\'s contacts when the system is powered.

## Arduino Library

We\'ve written a library to make it even easier to get started with the SparkFun Qwiic Quad Relay. The library will give you the full functionality of the Qwiic Quad Relay without the hub bub of the I²C data transactions. You can click the link below to download the file or navigate through the Arduino Library Manager by searching **SparkFun Qwiic Relay**. You can also go the [Github page](https://github.com/sparkfun/SparkFun_Qwiic_Relay_Arduino_Library) and get it directly.

[SparkFun Qwiic Relay Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_Relay_Arduino_Library/archive/master.zip)

This library also works with our [Qwiic Single Relay board](https://www.sparkfun.com/products/15102). If you only need one relay then go check it out!

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Library Functions Overview

The list below outlines all of the functions of the Qwiic Relay Arduino Library designed to work with the Qwiic Quad Relay along with short descriptions of what they do. The examples cover nearly all of the functions so take a look at those for demonstrations on how to integrate them into your own code.

- `bool begin(TwoWire &wirePort = Wire);` - Initialize the Qwiic Relay on the I^2^C bus
- `float singleRelayVersion();` - Returns the version number of the relay
- `void turnRelayOn(uint8_t relay);` - Turn the given relay on. Valid inputs for `relay` are 1 through 4. For example, `turnRelayOn(1);` will toggle the first relay.
- `void turnRelayOff(uint8_t relay);` - Turn the selected relay off. Similar to the above function, select values between 1 and 4 to turn the chosen relay off.
- `void toggleRelay(uint8_relay)` - Toggles the selected relay to the opposite state. The function first checks the status of the relay and is toggled to either `on` or `off` depending on what the status check returns.
- `void turnAllRelaysOn();` - Turns all relays on the board on.
- `void turnAllRelaysOff();` - Turns all relays on the board off.
- `void toggleAllRelays();` - Toggles all relays on the board to the opposite state of the relay status check.
- `uint8_t getState(uint8_t relay);` - Returns the status of the selected relay. Returns `1` if on or `0` if off. Just like with previous functions, valid inputs for `relay` are 1 through 4.
- `bool changeAddress(uint8_t newAddress);` - Changes the I^2^C address of the Qwiic Relay. The new address is written to the memory location in EEPROM that determines the address. Valid `newAddress` values can be between **0x07** and **0x78**.

## Example Code

### Example 4 - Relay Control using Buttons

This is the code used for the lamp example below. Unzip and open up example four under **\...** \> **SparkFun Qwiic_Relay_Arduino Library-master** \> **Example Code** \> **Example4_Quad_Relay_Buttons** to follow along. Starting at the top, we have `#include`-ed the path to the library\'s header file as well as to Arduino\'s I²C library: `Wire.h`. To use the functions in the SparkFun Qwiic Relay Library we create a version of it, and name it `quadRelay`. You\'ll notice that in parentheses we have given it the board\'s address. If you have changed it or closed the address jumper, than change the `RELAY_ADDR` to your address.

    language:c
    #include <Wire.h>
    #include "SparkFun_Qwiic_Relay.h"

    #define RELAY_ADDR 0x6D

    Qwiic_Relay quadRelay(RELAY_ADDR);

Next we setup three buttons: yellow, red, and blue on three pins: 2, 3, and 4.

    language:c
    const int yellow_btn = 2;
    const int red_btn    = 3;
    const int blue_btn   = 4;

First we check that we can communicate correctly with the Quad Relay with the `quadRelay.begin()` function call. If there are some connection issues we\'ll find out about them here. Notice that his won\'t stop our code from running so keep an eye out for an error message. Next we use pullup resistors on our buttons to put them into a known **HIGH** state.

    language:c
    void setup()
    

Finally in the loop the buttons are constantly being checked for a button press. For example, if the blue button is pressed then relay number one turns on. The small 400ms delay is there for debounce. Without it each of our casual presses would be read a couple hundred times before we finally took our finger off of the button.

    language:c
    void loop()
    

        // Button two turns on relay two....
      if(digitalRead(blue_btn) == LOW)

      // Button three turns off relay one and two...
      if(digitalRead(red_btn) == LOW)

    }

Now let\'s upload some code via the Arudino IDE. Before uploading, be sure to remove power to the load when uploading to safely handle the relay. Then connect the Arduino to your computer to upload. Select the board (in this case the **Arduino/Genuino Uno**) and COM port that your Arduino has enumerated to. Click the upload button. When the code has finished uploading, place the Arduino and relay on a non-conductive surface to test. Remember to not touch the relay\'s contacts when the system is powered.

## Let There Be Light!

After we load up the code, and press the button we should see the relay one LED light up.

[![Qwiic Quad Relay Powered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/9/relay_wires_on.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/relay_wires_on.jpg)

If your relay LED is on and the lamp doesn\'t turn on, make sure you have the lamp turned on. We\'ll let the relay handle turning it off and on from now on. Now if all is correctly assembled:

[![Quad Relay in Action](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/Quad_Relay.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/9/Quad_Relay.gif)

Algebraic!!

**Note:** Did you notice that there were more examples in the **Example Code** folder? If you need, there is an example using interupts (i.e. **Example3_Quad_Relay_Interrupts**) if you need your [Arduino to stop whatever it is processing](https://learn.sparkfun.com/tutorials/processor-interrupts-with-arduino) to toggle the relays.

**Heads up!** The circuit used in this tutorial is a temporary connection so you will need to secure the circuit and place the relay in an enclosure. For more ideas, check out some of the projects in resources and going further.