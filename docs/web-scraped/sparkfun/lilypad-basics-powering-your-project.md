# Source: https://learn.sparkfun.com/tutorials/lilypad-basics-powering-your-project

## Introduction

In this guide, we will discuss options for powering your LilyPad projects (both e-sewing and Arduino-based), battery safety and care, and how to calculate and consider power constraints on your projects. Creating wearable and fabric projects have their own considerations and we\'ll also cover when it makes sense to switch from conductive thread connections to wired connections.

LilyPad projects are often wearable or portable, which means using a battery to take the final project on the go. However, there are a few options for powering your projects beyond just plugging in a battery. Read on for sections detailing different power sources and options available for working with the system.

[] **Warning:** The LilyPad ecosystem was designed to run on 3.3V, and most of the power boards you will find in the line will accommodate either a 3V CR2032 coin cell battery or 3.7V Lithium Polymer battery. Some LilyPad boards have voltage regulators on board and have more flexibility in the power source you use with them. Details on alternative power options are covered throughout the guide.

We\'ve compiled some tips for you, to help decide what power source to use, how long it will last on battery power, and other considerations. Knowing how much voltage your project needs, the total current draw of the LilyPad boards you are using in your project, and battery capacity will help you choose the best option for optimal operation.

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/electric-power)

### Electric Power 

An overview of electric power, the rate of energy transfer. We\'ll talk definition of power, watts, equations, and power ratings. 1.21 gigawatts of tutorial fun!

[](https://learn.sparkfun.com/tutorials/what-is-a-battery)

### What is a Battery? 

An overview of the inner workings of a battery and how it was invented.

## Calculating Power Needs: Operating Voltage

Most LilyPad projects can operate easily on a **3.7V** rechargeable Lithium Polymer battery. The microcontroller or main sensor or component that each LilyPad board is built around has its particular operating voltage needs documented in its datasheet. You can find the datasheet for a product in the *Documents* tab of the catalog page on SparkFun.com.

[![SparkFun Product Page and the Documents Tab](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/8/Datasheet.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/8/Datasheet.png)

*Example of the documents tab for the [LilyPad Arduino USB - ATmega32U4 Board](https://www.sparkfun.com/products/12049).*

When reading the datasheet, look for **Operating Voltages** - the document will typically provide a minimum and maximum voltage range. If there is no datasheet attached to the product, you can also check the schematic.

If you don\'t give a board a large enough voltage, it may not operate correctly (you could see strange behavior in how code runs on a LilyPad Arduino, odd readings from sensors in the Serial Port, or dim LEDs). If you project is receiving voltage above its recommended range, you could potentially damage the board or reduce the operating time significantly. Make sure the power source you choose for your project is within the board\'s recommended range.

Here is a list of common LilyPad Boards and their needs. The middle column displays the regulated voltage on the board from the input voltage. If you choose a board that does not include a built-in regulator, you will need to pay close attention to your power source to make sure it is compatible with your project. The last column shows the input voltage that each board can take, notice that this can be above 3.3V, the suggested operating voltage of a LilyPad project.

  Board                                                                                                                       Voltage Regulation   Input Voltage
  --------------------------------------------------------------------------------------------------------------------------- -------------------- ---------------------------------
  [LilyTiny](https://www.sparkfun.com/products/11364)                                                                         No                   1.8V - 5.5V
  [LilyTwinkle](https://www.sparkfun.com/products/11364) / [LilyTwinkle ProtoSnap](https://www.sparkfun.com/products/11590)   No                   1.8V - 5.5V
  [LilyMini ProtoSnap](https://www.sparkfun.com/products/14063)                                                               3.3V                 1.62V - 3.63V, 5.0V through USB
  [LilyPad Arduino Simple](https://www.sparkfun.com/products/10274)                                                           No                   2.7V - 5.5V
  [LilyPad Arduino SimpleSnap](https://www.sparkfun.com/products/10941)                                                       3.3V                 2.7V - 5.5V
  [LilyPad Arduino USB - ATmega32U4 Board](https://www.sparkfun.com/products/12049)                                           3.3V                 2.7V - 5.5V
  [Lilypad USB Plus](https://www.sparkfun.com/products/14631)                                                                 3.3V                 1.8V - 5.5V
  [LilyPad Arduino 328 Main Board](https://www.sparkfun.com/products/13342)                                                   No                   2.7V - 5.5V
  [LilyPad XBee](https://www.sparkfun.com/products/12921)                                                                     3.3V                 1.8V - 9V
  [LilyPad Simblee BLE Board - RFD77101](https://www.sparkfun.com/products/13633)                                             3.3V                 1.8V -- 3.6V
  [LilyPad MP3](https://www.sparkfun.com/products/11013)                                                                      3.3V                 3.7V - 6V

[ ] **Some components in my project need more than 3.3V to operate, can I still use them with a LilyPad Arduino?**\
\
Most boards in the LilyPad system are designed to operate at the system voltage (3.3V), but if you are mixing and matching from other sewable or non-sewable product lines you may encounter a sensor or board that needs 5V. In this case, first try to find a 3.3V version of the board. If needed, you can hook up a [Bi-Directional Logic Level Converter](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide).

## Calculating Power Needs: Current Draw

In addition to checking the operating voltage of the LilyPad boards in your project, you\'ll also want to take a look at the current your project will draw compared to the current your microcontroller or battery source can provide.

The current draw of your project depends on the total number of LilyPad boards you have chosen to use in your project and applies to both LilyPad Arduino-controlled circuits and e-sewing projects. If your power supply or battery does not provide the current your project needs, the circuit may start acting in strange or unpredictable ways.

*As with voltage, you can check the datasheets of the individual LilyPad boards to estimate what your project will use.*

For projects using a LilyPad Arduino, check how much current each individual I/O (input/output) sew tab can provide - the amount of LilyPad boards, such as LEDs, will be limited by this number. For most LilyPad Arduinos this is 40mA per I/O sew tab.

*It\'s also better practice to round up and assume your circuit will need more current than to not provide enough current.*

If your project uses components that require a lot of current, like motors or large amounts of LEDs, you may need to readjust your power supply choice or even use a separate supply for the LilyPad Arduino and the current-hungry boards.

As you gain experience working with LilyPad boards, it will be easy to estimate the amount of current your project requires by looking at the boards\' datasheets and doing some math. You can also find out exactly how much current your project uses by measuring it with a [digital multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter/measuring-current) or variable DC power supply that has a readout for current.

#### Read World Example: LilyPad LEDs and LilyTiny

Let\'s explore an example of a frequently asked question about LilyPad projects: *How many LEDs can I connect to a LilyTiny (or LilyTwinkle) board?*

A typical **LilyPad LED** uses 20mA of current at full brightness. Multiply that by the number of LEDs you're using, add 10mA for the LilyPad that's running everything, and you'll have an estimate of your average current draw.

**Example:**\
\
A project with 10 LilyPad LEDs connected to a LilyTiny Board\
\

*20mA \* 10 + 10mA = 210mA*

*For more detailed information on working with LilyPad LEDs, take a look at our [Powering LilyPad LED Projects](https://learn.sparkfun.com/tutorials/powering-lilypad-led-projects).*

[](https://learn.sparkfun.com/tutorials/powering-lilypad-led-projects)

### Powering LilyPad LED Projects 

December 17, 2016

Learn how to calculate how many LEDs your LilyPad project can power and how long it will last.

## Considering Conductive Thread Resistance

Now that you\'ve done your calculations, there is another factor to consider: conductive thread resistance. Unlike copper wire, which has very little resistance, conductive thread\'s resistance will vary depending on the metal used to make the thread and the thickness of the thread. Many conductive threads list resistance in Ohms/Ft. The lower this number is, the better, because less resistance means more electricity can get through to the components used in your project.

You may expect your project to work perfectly, but the resistance of your connections over distance may cause some additional complications in your circuit.

[![Solid wire, stranded wire, and stainless steel conductive thread](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/1/WirevsThread.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/1/WirevsThread.jpg)

The basic electrical property [Ohm's Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law#ohms-law) states that running an electrical current through a material high in resistance causes the voltage to drop. The higher the current, the greater the voltage drop. This means that even though a [LiPo battery](https://www.sparkfun.com/products/13112) powering your LilyPad may put out 3.7 volts, by the time it gets through the thread to your components, it may drop to 3.0 volts or less. Many electrical components, such as LEDs, need a certain voltage to function properly. To minimize voltage drop, we\'ll need to decrease the resistance of the power connections. There are a few ways to do this:

- **Keep the length of the power connections as short as possible**. Because the resistance increases with length, if you reduce the length, you'll reduce the resistance.

- **Reduce the resistance of the thread itself**. Thicker thread has a lower resistance than thinner thread, and using multiple strands at a time reduces the resistance even further.

**Tip:**\
\
Use a non conductive thread to stitch bundled thread (either placed together or braided) to your base fabric. Leave enough open spaces in the stitching so you are able to stitch conductive thread to the larger thread bundle when connecting components. This video from e-textile expert Lynne Bruning shows this technique at around the 4:10 mark:\
\

### Conductive Thread Alternatives

For large projects that require thread to travel long distances, projects with a lot of power-hungry pieces such as a large amount of LilyPad Pixel Boards, or in spots where thread may break under stress, here are some alternatives that work well for wearables:

#### Conductive Ribbon

Specialty nylon ribbon with flexible stranded wire woven into it is a great alternative to conductive thread with low resistance. You will need to [solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) to the tinsel within the ribbon in order to use in a project.

[![Conductive Ribbon - 3-Conductor (1 yard)](https://cdn.sparkfun.com/r/140-140/assets/parts/4/4/7/7/10172-01.jpg)](https://www.sparkfun.com/products/10172)

### [Conductive Ribbon - 3-Conductor (1 yard)](https://www.sparkfun.com/products/10172) 

[ DEV-10172 ]

Here we have some conductive ribbon. Essentially, it\'s a fabric with 3 conductors woven into the ribbon. It measures roughly ...

**Retired**

#### Conductive Fabric Traces

You can create your own lower resistance traces using thin strips of conductive fabric. We recommend using iron-on adhesive to attach to fabric or ribbon, then using conductive thread to hand stitch components to the traces.

[![Conductive Fabric Used as Traces Between Components](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/5/Pixel_Ribbon.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/5/Pixel_Ribbon.png)

Don\'t forget to [insulate](https://learn.sparkfun.com/tutorials/insulation-techniques-for-e-textiles) the fabric traces as you would conductive thread.

#### Stranded Wire

Another alternative is to switch from conductive thread to traditional wire. Wire has a much lower resistance than thread, allowing you to use more LEDs than a conductive thread circuit. You'll have to switch from sewing to soldering, but it's easy to solder wires to the same sew tabs to which you would normally connect thread.

[![Ribbon Cable - 6 wire (15ft)](https://cdn.sparkfun.com/r/140-140/assets/parts/5/4/2/1/10646-02.jpg)](https://www.sparkfun.com/ribbon-cable-6-wire-15ft.html)

### [Ribbon Cable - 6 wire (15ft)](https://www.sparkfun.com/ribbon-cable-6-wire-15ft.html) 

[ CAB-10646 ]

Ribbon cable is really helpful in situations where you need to make a lot of connections without a big mess of wires. Nothing...

[ [\$4.50] ]

Wire is prone to breaking if it is flexed repeatedly. For wearable projects that require maximum flexibility, use stranded wire (not solid), and look for special silicone-jacketed wire that is extremely flexible. For projects that will be washed, water may wick into exposed stranded wire, becoming trapped and potentially corroding it over time. Apply a small dab of silicone sealant to the cut ends of the wire to prevent this from happening.

[] When soldering, be careful not to melt or burn nearby fabric. Elevate or insulate the back of the LilyPad board from any backing fabric before applying heat.

If you have never soldered before or worked with wire, we recommend visiting the following tutorials.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

Once you\'ve identified your project\'s power needs and considerations, it\'s time to move on to choosing a power source for your project.

## Power Options: Using a Built-In USB Connector

While working on programming a LilyPad Arduino project, you can use the power supplied by the USB cable connecting your LilyPad Arduino to your computer. Make sure the slide switch on the LilyPad Arduino is set to the ON position to upload code and power up your board while prototyping.

[![Built-In Power Switch in a LilyPad](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/TurnOnLilyPadSwitch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/TurnOnLilyPadSwitch.jpg)

This method works for LilyPad Arduinos with a built-in micro USB port and those with programming headers and [LilyPad FTDI Basic Breakout](https://www.sparkfun.com/products/10275).

LilyPad boards with a micro USB connector can be powered by 5V Lithium Ion battery packs such as the ones used in the [Spectacle](https://www.sparkfun.com/spectacle) line or for backups for cell phone charging.

[![Lithium Ion Battery Pack - 2.5Ah (USB)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/7/6/14367-Lithium_Ion_Battery_Pack__Power_Bank__-_2.5Ah__USB_-01a.jpg)](https://www.sparkfun.com/products/14367)

### [Lithium Ion Battery Pack - 2.5Ah (USB)](https://www.sparkfun.com/products/14367) 

[ PRT-14367 ]

We\'ve taken the classic, portable, rechargeable lithium ion battery pack and tweaked the design to make it amenable to low cu...

**Retired**

If your project is not portable or wearable (such as a wall hanging or permanent installation) you may choose to utilize a 5V wall adapter power supply for your project. Plugging into a dedicated power source will eliminate the need to constantly swap out or recharge batteries in your project.

[![Wall Adapter Power Supply - 5VDC, 2A (USB Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/4/TOL-15311-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-usb-micro-b.html)

### [Wall Adapter Power Supply - 5VDC, 2A (USB Micro-B)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-usb-micro-b.html) 

[ TOL-15311 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA USB Micro-B wall power supply manufactured specifically for S...

[ [\$9.50] ]

[![Wall Adapter Power Supply - 5.1V DC 2.5A (USB Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/2/8/13831-01a.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5-1v-dc-2-5a-usb-micro-b.html)

### [Wall Adapter Power Supply - 5.1V DC 2.5A (USB Micro-B)](https://www.sparkfun.com/wall-adapter-power-supply-5-1v-dc-2-5a-usb-micro-b.html) 

[ TOL-13831 ]

This is a high-quality switching \'wall wart\' AC to DC 5.1V 2,500mA USB Micro-B wall power supply manufactured specifically fo...

[ [\$13.95] ]

[ ] **I found a wall adapter or battery pack with a micro USB connector on it - can I use it to power my LilyPad project?**\
\
Micro USB does not necessarily mean the battery pack is right for your project. When sourcing battery packs outside the SparkFun catalog make sure to double check the labeling on the packaging and the product to verify it is a 5V supply.

The LilyPad Simple Power is a board that offers you some flexibility - it can accommodate a rechargeable battery or a micro USB cable attached to a wall adapter for LilyPad projects that do not have a built-in battery connector.

[![LilyPad Simple Power](https://cdn.sparkfun.com/r/140-140/assets/parts/8/3/2/4/11893-01a.jpg)](https://www.sparkfun.com/lilypad-simple-power.html)

### [LilyPad Simple Power](https://www.sparkfun.com/lilypad-simple-power.html) 

[ DEV-11893 ]

The LilyPad Simple Power is a simple e-textile board with a 500mA charge rate that lets you connect and charge a lipo battery...

[ [\$12.50] ]

## Power Options: Rechargeable Lithium Polymer Batteries

[ ] Only use 3.7V LiPo batteries connected to LilyPad JST ports. Do not use non-LiPo or other batteries in these JST ports, even if they have the same connector. The charging circuit could damage the battery. Always double check the orientation of the power and ground wires on the battery, depending on the manufacturer they may be reversed. All LiPo batteries carried by SparkFun have a standard configuration.

Many LilyPad products come equipped with a JST connector designed attach a 3.7V Lithium Polymer (LiPo) battery. These boards include a built-in battery charging circuit to recharge the LiPo when connected to a computer or wall wart via a USB connection.

[![LilyPad ProtoSnap Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/2/4/14346-01.jpg)](https://www.sparkfun.com/lilypad-protosnap-plus.html)

### [LilyPad ProtoSnap Plus](https://www.sparkfun.com/lilypad-protosnap-plus.html) 

[ DEV-14346 ]

The LilyPad ProtoSnap Plus is a sewable electronics prototyping board that you can use to explore circuits and programming, t...

[ [\$47.50] ]

[![LilyPad Arduino USB - ATmega32U4 Board](https://cdn.sparkfun.com/r/140-140/assets/parts/8/6/3/3/12049-LilyPad_Arduino_USB_-_ATmega32U4_Board-01.jpg)](https://www.sparkfun.com/lilypad-arduino-usb-atmega32u4-board.html)

### [LilyPad Arduino USB - ATmega32U4 Board](https://www.sparkfun.com/lilypad-arduino-usb-atmega32u4-board.html) 

[ DEV-12049 ]

LilyPad is a wearable e-textile technology designed to have large connecting pads to allow them to be sewn into clothing & co...

[ [\$31.95] ]

[![LilyPad MP3](https://cdn.sparkfun.com/r/140-140/assets/parts/6/2/9/8/11013-01a.jpg)](https://www.sparkfun.com/lilypad-mp3.html)

### [LilyPad MP3](https://www.sparkfun.com/lilypad-mp3.html) 

[ DEV-11013 ]

The LilyPad MP3 Player is your all-in-one audio solution, containing an Arduino-compatible microcontroller, MP3 (and many oth...

[ [\$56.50] ]

[![LilyPad Simple Power](https://cdn.sparkfun.com/r/140-140/assets/parts/8/3/2/4/11893-01a.jpg)](https://www.sparkfun.com/lilypad-simple-power.html)

### [LilyPad Simple Power](https://www.sparkfun.com/lilypad-simple-power.html) 

[ DEV-11893 ]

The LilyPad Simple Power is a simple e-textile board with a 500mA charge rate that lets you connect and charge a lipo battery...

[ [\$12.50] ]

[![LilyPad Arduino Simple Board](https://cdn.sparkfun.com/r/140-140/assets/parts/4/6/6/3/10274-01c.jpg)](https://www.sparkfun.com/products/10274)

### [LilyPad Arduino Simple Board](https://www.sparkfun.com/products/10274) 

[ DEV-10274 ]

This is the LilyPad Arduino Simple Board. It\'s controlled by an ATmega328 with the Arduino bootloader. It has fewer pins than...

**Retired**

[![LilyPad Simblee BLE Board - RFD77101](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/0/2/4/13633-01a.jpg)](https://www.sparkfun.com/products/13633)

### [LilyPad Simblee BLE Board - RFD77101](https://www.sparkfun.com/products/13633) 

[ DEV-13633 ]

The LilyPad Simblee BLE Board is a wearable development board that allows you to add mobile application functionality via Blu...

**Retired**

SparkFun carries a variety of 3.7V Lithium Polymer batteries that are compatible with the LilyPad system. The capacity of the battery will depend on the intended run time of your project, size constraints, and other factors.

[![Lithium Ion Battery - 110mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/0/13853-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-110mah.html)

### [Lithium Ion Battery - 110mAh](https://www.sparkfun.com/lithium-ion-battery-110mah.html) 

[ PRT-13853 ]

This is a very small, extremely light weight battery based on Lithium Ion chemistry. This is the highest energy density curre...

[ [\$7.53] ]

[![Lithium Ion Battery - 850mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/1/13854-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-850mah.html)

### [Lithium Ion Battery - 850mAh](https://www.sparkfun.com/lithium-ion-battery-850mah.html) 

[ PRT-13854 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 850...

[ [\$13.61] ]

[![Lithium Ion Battery - 400mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/5/8/13857-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-400mah.html)

### [Lithium Ion Battery - 400mAh](https://www.sparkfun.com/lithium-ion-battery-400mah.html) 

[ PRT-13851 ]

This is a very small, extremely lightweight battery based on Lithium Ion chemistry, with the highest energy density currently...

[ [\$7.98] ]

[![Lithium Ion Battery - 2Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/2/13855-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-2ah.html)

### [Lithium Ion Battery - 2Ah](https://www.sparkfun.com/lithium-ion-battery-2ah.html) 

[ PRT-13855 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 200...

[ [\$19.41] ]

[![Lithium Ion Battery - 6Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/3/13856-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-6ah.html)

### [Lithium Ion Battery - 6Ah](https://www.sparkfun.com/lithium-ion-battery-6ah.html) 

[ PRT-13856 ]

If you need some juice, this 6Ah Lithium Ion Battery is for you. These are very compact batteries based on Lithium Ion chemis...

[ [\$48.44] ]

[![Lithium Ion Battery - 1Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/0/1/13813-01.jpg)](https://www.sparkfun.com/products/13813)

### [Lithium Ion Battery - 1Ah](https://www.sparkfun.com/products/13813) 

[ PRT-13813 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1000 mAh!

**Retired**

[![E-Textiles Battery - 110mAh (2C Discharge)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/1/6/3/13112-02.jpg)](https://www.sparkfun.com/products/13112)

### [E-Textiles Battery - 110mAh (2C Discharge)](https://www.sparkfun.com/products/13112) 

[ PRT-13112 ]

This is a very small, extremely lightweight battery based on Polymer Lithium Ion chemistry. This is the highest energy densit...

**Retired**

### [] [Using a LiPo Battery and Battery Charging](#battery)

[ ] LilyPad projects are hand-washable, but **always remove the battery before washing your project** and air-dry your project for several days before replacing the battery.

Each LilyPad board with charging capabilities has a default charge rate. If this default charge current is set to **100mA**, so a 100mAh battery will recharge in one hour, a 1000mAh battery in 10 hours, etc. Since the board is set to charge at a rate of 100mA, we do not recommend connecting a lower capacity LiPo battery (i.e. 40mAh LiPo battery) to charge.

Most LilyPad products with an onboard charging circuit are set at 100mA, however, the [LilyPad MP3](https://www.sparkfun.com/products/11013) and [LilyPad Simple Power](https://www.sparkfun.com/products/11893) have a default charge rate of 500mA. If using a LiPo battery with capacity below the set charge rate, we recommend charging separately using a [SparkFun Adjustable LiPo Charger](https://www.sparkfun.com/products/14380).\
\

[![SparkFun Adjustable LiPo Charger](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/9/1/14380b-01.jpg)](https://www.sparkfun.com/sparkfun-adjustable-lipo-charger.html)

### [SparkFun Adjustable LiPo Charger](https://www.sparkfun.com/sparkfun-adjustable-lipo-charger.html) 

[ PRT-14380 ]

The SparkFun Adjustable LiPo Charger is a single-cell lithium polymer (LiPo) and lithium ion battery charger. Because it's ...

[ [\$13.95] ]

To recharge an attached battery, plug the board into a USB power source. While the battery is charging, the \"CHG\" LED will illuminate. When the battery is fully charged the LED will turn off.

[![Connecting a Battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/InsertBattery.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/InsertBattery.jpg)

*Inserting a LiPo battery into the JST port on a LilyPad ProtoSnap Plus*

It is safe to leave a LiPo battery attached to the board permanently, even with USB power applied. The battery will not be overcharged. We recommend you do not leave a charging battery unattended.

[ ] Always turn the LilyPad board off before inserting or removing a battery.

The battery connector can be a tight fit and difficult to remove; when disconnecting a battery never pull on the wires. Use a pair of needle nose pliers or cutters along the plastic to gently pull the plug out of the connector.

[![Remove LiPo Battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/PliersBattery_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/PliersBattery_1.jpg)

*Tip: there are two small \"nubs\" on the top of the plastic battery connector that can be shaved off with a hobby knife to make the battery easier to remove.*

[ ] **I found this cool battery pack with a JST connector on it - can I use it in my LilyPad project?**\
\
JST connectors are a common type of connector, just because a product has it does not mean it is LilyPad-compatible.When sourcing batteries outside the SparkFun catalog make sure to double check:\
\
    [] Is it 3.7V?\
    [] Is it a rechargeable Lithium Polymer/Lithium Ion battery?\
\

### [][LiPo Battery Safety and Care](#lipo_safety_care)

[ ] **Warning:** LiPo batteries can explode or catch fire if mishandled or damaged. They can become unstable and dangerous if punctured or exposed to high temperatures.

While LiPo batteries are a great option for providing rechargeable power to your project, they do have some safety considerations. This section will cover tips for safe handling and use of LiPos for your projects.

#### Storage

- Always store your batteries in and enclosure free of sharp objects. When installing a battery in your project, take care to keep it away from parts of your project that could pinch, poke, or strain the battery.

- Do not transport or store a LiPo battery with metal objects, such as hairpins, necklaces, or any other conductive object or material.

- Keep or store the battery in a cool and dry place/environment while installed in a project or in storage. If you are not planning to use your project for a long time, remove the battery and store it separately.

#### Keep Away from Heat and Moisture

- Keep your LiPo battery away from environments that will damage it. Do not immerse a LiPo battery in liquids. Remove the battery from your project if it needs to be washed.

- Do not use or store the battery near any source of heat. To secure a battery to your project, velcro is a temporary option or sew into a pouch or place in a plastic enclosure. Never iron or hot glue directly on or around a LiPo battery.

#### Strain Relief

One of the down sides to using these LiPo batteries is their fragile power connections. These type of batteries are manufactured for a permanent install in devices, and not being removed often as can sometimes happen with wearables. It can be easy to accidentally pull or break the power wires from the terminals on the safety circuit built into the battery.

You can provide strain relief to the wires by placing them to the side and securing with electrical tape - this will help with strain on the connection to the battery when pulling on them to remove.

[![Electrical tape around the wires of a LiPo for strain relief](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/8/TapedLipo.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/8/TapedLipo.jpg)

#### Inspect Battery Before Each Use

- Short circuits or damage to LiPo batteries may not always be noticeable - check the battery for puffiness, heat, or other changes. If the battery looks damaged, remove immediately.

- If the battery gives off an odor, generates heat, becomes discolored or deformed, or in any way appears abnormal during use, recharging, or storage, immediately remove it from your project or battery charger and stop using it. Make sure to dispose of your batteries properly - do not throw them in the trash! Contact your local e-waste disposal organization for details on how to discard batteries in your area.

## Power Options: Coin Cell Batteries

The LilyPad system includes boards that hold a single [3V CR2032 coin cell battery](https://www.sparkfun.com/products/338). These batteries are typically single use, but some rechargeable coin cell batteries may work in the holders.

[![Coin Cell Battery - 20mm (CR2032)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/338-Coin-Cell-Battery-20mm-Feature.jpg)](https://www.sparkfun.com/coin-cell-battery-20mm-cr2032.html)

### [Coin Cell Battery - 20mm (CR2032)](https://www.sparkfun.com/coin-cell-battery-20mm-cr2032.html) 

[ PRT-00338 ]

CR2032 Lithium metal 3V 250mAh button cell battery. Great for powering low power processors or blink an LED for weeks at a ti...

[ [\$2.25] ]

[ ] **The name of the battery CR2032 has some important information contained in it:**\
\

- C designates a lithium battery type
- R designates a ROUND (cylindrical) battery shape
- 20 specifies the package size (diameter) in mm
- 32 specifies the height in mm. Note this is 3.2 mm NOT 32mm

*In addition to confirming the voltage when selecting a battery (3V), pay special attention to the last two numbers of the part name as you may find batteries that appear to be compatible but are just slightly too large or small to fit into the LilyPad battery holders.*

The LilyPad product line includes a standalone battery holder with a switch that can be connected to a customized project, as well as built into the LilyMini board, and available in some ProtoSnap products. SparkFun also carries a non-LilyPad coin cell battery holder without sew tabs for projects that need a small footprint or for users who want to solder.

[![LilyPad Coin Cell Battery Holder - Switched - 20mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/5/1/7/13883-02.jpg)](https://www.sparkfun.com/lilypad-coin-cell-battery-holder-switched-20mm.html)

### [LilyPad Coin Cell Battery Holder - Switched - 20mm](https://www.sparkfun.com/lilypad-coin-cell-battery-holder-switched-20mm.html) 

[ DEV-13883 ]

Sure, your flashing, chip-tune playing T-shirt is really cool at the party\... but at some point you need to turn it off. And ...

[ [\$2.50] ]

[![LilyPad LilyMini ProtoSnap](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/9/0/5/14063-01.jpg)](https://www.sparkfun.com/lilypad-lilymini-protosnap.html)

### [LilyPad LilyMini ProtoSnap](https://www.sparkfun.com/lilypad-lilymini-protosnap.html) 

[ DEV-14063 ]

The LilyMini ProtoSnap is a great way to get started learning about creating interactive e-textile circuits before you start ...

[ [\$19.50] ]

[![Coin Cell Battery Holder - 20mm (Sewable)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/7/1/08822-03-L.jpg)](https://www.sparkfun.com/coin-cell-battery-holder-20mm-sewable.html)

### [Coin Cell Battery Holder - 20mm (Sewable)](https://www.sparkfun.com/coin-cell-battery-holder-20mm-sewable.html) 

[ DEV-08822 ]

This is a coin cell holder for the common CR2032 type battery. The holder has a neat pop-in, pop-out feature that makes chang...

[ [\$1.60] ]

[![LilyTwinkle ProtoSnap](https://cdn.sparkfun.com/r/140-140/assets/parts/7/5/9/3/11590-01.jpg)](https://www.sparkfun.com/lilytwinkle-protosnap.html)

### [LilyTwinkle ProtoSnap](https://www.sparkfun.com/lilytwinkle-protosnap.html) 

[ DEV-11590 ]

The ProtoSnap series is a new way to prototype your project without a breadboard. Everything is wired together on a single bo...

**Retired**

[ ] **Can I use two LilyPad battery holders in series or a two battery pack I found for my LilyPad project?**\
\
This depends on the LilyPad board you are powering. Two 3V batteries in series will supply 6V - some LilyPad boards do not have onboard regulation circuits and can be damaged by supplying them with more than 3V. For example, the LilyTiny and LilyTwinkle boards operate best between 2.4 and 5.5V. In these cases, a Lithium Ion/Lithium Polymer battery may be a better choice for your project.\
\
Check out the [Calculating Power Needs](https://learn.sparkfun.com/tutorials/lilypad-basics-powering-your-project#calculating-power-needs-operating-voltage) section for more tips on selecting the right battery for your project\'s unique needs.

### Battery Safety and Care

[ ] Lithium metal batteries can explode or catch fire if mishandled or damaged. They can become unstable and dangerous if punctured or exposed to high temperatures.

This section will cover tips for safe handling and use of coin cell batteries for your projects.

#### Storage

- Do not transport or store a coin cell battery with metal objects, such as hairpins, necklaces, or any other conductive object or material. Do not store loose coin cell batteries together - they can make contact with each other and short circuit and discharge.

- Keep or store the battery in a cool and dry place/environment while installed in a project or in storage. If you are not planning to use your project for a long time, remove the battery and store it separately.

#### Keep Away from Heat and Moisture

- Keep your coin cell battery away from environments that will damage it. Do not immerse a coin cell battery in liquids. Remove the battery from your project if it needs to be washed.

- Do not use or store the battery near any source of heat. To secure a battery to your project, use a specialty battery holder, sewn pouch, or place in a plastic enclosure. Never solder directly to a coin cell battery; if you need to solder one into a project, use a special battery holder or purchase a battery with solder tabs created for this purpose.

#### Inspect Battery Before Each Use

- Short circuits or damage to coin cell batteries may not always be noticeable - check the battery for puffiness, heat, or other changes. If the battery looks damaged, remove immediately.

- If the battery gives off an odor, generates heat, becomes discolored or deformed, or in any way appears abnormal during use, recharging, or storage, immediately remove it from your project or battery charger and stop using it. Make sure to dispose of your batteries properly - do not throw them in the trash! Contact your local e-waste disposal organization for details on how to discard batteries in your area.

## How Long Will My Project Run on Battery Power?

To figure out how long your project will run on battery power, you need to know two things:

- how much current your project uses
- the capacity of your battery

Battery capacity is given in **milliamp-hours** (mAh). This number tells you how many milli-amps (mA) a full battery can provide for one hour before it's empty. The [e-Textiles Battery](https://www.sparkfun.com/products/13112) that comes with most LilyPad Arduino kits has a 110mAh capacity. For many projects, especially ones with a large number of components such as LEDs, you will probably want to use a higher capacity battery for a longer run time.

To find out how long a battery will last, use this formula:\
\

**Hours = Battery mAh / Project mA**

Thus, an e-Textile battery will only power the project for approximately half an hour. Here\'s an instance where a larger capacity battery would make sense, if the project needs to operate for a long time, such as during an event or showcase. The trade-off is that a higher capacity battery is also physically larger \-- make sure to plan accordingly for proper battery storage/attachment on your project to reduce strain on the wires and fabric.

***Here are some typical runtimes for various SparkFun batteries and numbers of LilyPad LEDs/LilyPixels:***

**Number of LEDs**

1

2

5

10

20

Battery Name

Battery mAh

Hours of Operation

[Polymer Lithium Ion Battery - 40mAh](https://www.sparkfun.com/products/11316)

40

1.3

0.8

0.4

0.2

0.1

[E-Textiles Battery - 110mAh (2C Discharge)](https://www.sparkfun.com/products/13112)

110

3.7

2.2

1.0

0.5

0.3

[Coin Cell Battery - 20mm (CR2032) \*](https://www.sparkfun.com/products/338)

250

8.3

5.0

2.3

1.2

.61

[Polymer Lithium Ion Battery - 400mAh](https://www.sparkfun.com/products/10718)

400

13.3

8.0

3.6

1.9

1.0

[Polymer Lithium Ion Battery - 850mAh](https://www.sparkfun.com/products/341)

850

28.3

17.0

7.7

4.0

2.1

[Polymer Lithium Ion Battery - 1000mAh](https://www.sparkfun.com/products/339)

1000

33.3

20.0

9.1

4.8

2.4

[Polymer Lithium Ion Battery - 2000mAh](https://www.sparkfun.com/products/8483)

2000

66.7

40.0

18.2

9.5

4.9

[Polymer Lithium Ion Battery - 6Ah](https://www.sparkfun.com/products/8484)

6000

200.0

120.0

54.5

28.6

14.6

`*` Note: the Coin Cell Battery is non-rechargeable.

[] **Caution:** The other [batteries](https://www.sparkfun.com/categories/54) in our catalog are not created especially for e-Textiles. Use caution to avoid shorting out conductive thread traces when using alternative batteries.