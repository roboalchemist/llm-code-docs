# Source: https://learn.sparkfun.com/tutorials/sparkfun-5v1a-lipo-chargerbooster-hookup-guide

## Introduction

The [SparkFun 5V/1A LiPo Charger/Booster](https://www.sparkfun.com/products/14411) is a no nonsense circuit for generating an amp from a lipo, at 5 volts. It\'s low cost, has a simple booster circuit realizing the PAM2401 IC, and includes protection diodes so you can run multiple cells in series for extra kick. When a booster circuit is in operation, it draws more current than the lower the input voltage, so it\'s possible to violate the C rating of the battery. This circuit doesn\'t care, nor do I. If you\'re looking to coddle your LiPos, try the excellent [Battery Babysitter](https://www.sparkfun.com/products/13777). But if you need charge delivered somewhere *NOW*, this is the product for you.

[![SparkFun LiPo Charger/Booster - 5V/1A](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/4/3/2/14411-01.jpg)](https://www.sparkfun.com/sparkfun-lipo-charger-booster-5v-1a.html)

### [SparkFun LiPo Charger/Booster - 5V/1A](https://www.sparkfun.com/sparkfun-lipo-charger-booster-5v-1a.html) 

[ PRT-14411 ]

The SparkFun 5V/1A LiPo Charger/Booster is a no-nonsense circuit for generating one amp from a Lithium Polymer battery at 5V....

[ [\$18.50] ]

This guide shows how to use 1x charger/booster with 1x lipo to make a pack, and how to connect several packs together for greater current or voltage.

[![LiPo Charger/Booster](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-10.jpg)

### Required Materials

#### A Battery

You\'ll need a battery for each charger/booster you have. While really any LiPo will work, smaller batteries are easy to overload and don\'t supply much charge. It is recommended to use 1Ah batteries and larger, with the form factor most suited to our [1Ah cell](https://www.sparkfun.com/products/13813).

[![Lithium Ion Battery - 850mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/1/13854-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-850mah.html)

### [Lithium Ion Battery - 850mAh](https://www.sparkfun.com/lithium-ion-battery-850mah.html) 

[ PRT-13854 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 850...

[ [\$13.61] ]

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

*Recommended batteries for the 5V/1A charger booster.*

#### A Load

Any development board that runs from a USB supply is a great thing to power with the charger/booster. It provides a stable 5 volts, and can feed power hungry boards. Take a look in the [microcontrollers product category](https://www.sparkfun.com/categories/300), anything with a 5V input may need mobile power.

**Tip:** Many development boards regulate 5V USB power down to 3.3V for logic supply. This 3.3V rail often has a pin that can be used, giving you 5V and 3.3V to work with.

#### A Charger

Any old micro-B charger should do the trick, the circuit will consume up to 500mA so a computer\'s USB port is not recommended. You can even use the power pins to charge from a generic bench supply.

Here\'s some sources that can be used to connect to the on board micro-B USB connector:

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

With the addition of a [micro-B cable](https://www.sparkfun.com/products/10215/), the following USB supplies will work:

[![USB Wall Charger - 5V, 1A (Black)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/3/1/0/11456-USB_Wall_Charger_-_5V__1A__Black_-01.jpg)](https://www.sparkfun.com/usb-wall-charger-5v-1a-black.html)

### [USB Wall Charger - 5V, 1A (Black)](https://www.sparkfun.com/usb-wall-charger-5v-1a-black.html) 

[ TOL-11456 ]

USB is being implemented as a power connection standard more and more these days, but you don\'t always have a computer on han...

[ [\$5.95] ]

[![USB Wall Charger - 5V, 1A (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/8/0/14042-02.jpg)](https://www.sparkfun.com/products/14042)

### [USB Wall Charger - 5V, 1A (White)](https://www.sparkfun.com/products/14042) 

[ TOL-14042 ]

USB is being implemented as a power connection standard more and more these days. But you don't always have a computer on h...

**Retired**

Or if you\'re in the market for a larger generic supply, try these:

[![Power Supply - 80W DC Switching Mode](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/1/6/09291-1.jpg)](https://www.sparkfun.com/products/9291)

### [Power Supply - 80W DC Switching Mode](https://www.sparkfun.com/products/9291) 

[ TOL-09291 ]

This is an 80W 3-in-1 (3 output ranges) Switching DC Power Supply. Gives a regulated 0-36VDC @ 2.2A, 80W max output. Takes a ...

**Retired**

[![Mean Well Switching Power Supply - 5VDC, 20A](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/9/7/0/14098-01.jpg)](https://www.sparkfun.com/products/14098)

### [Mean Well Switching Power Supply - 5VDC, 20A](https://www.sparkfun.com/products/14098) 

[ TOL-14098 ]

This is a 100W single output switching power supply from Mean Well. This power supply is extremely reliable and able to outpu...

**Retired**

### Required Tools

You\'ll have to attach your load somehow! Make sure you\'ve got a few tools on hand.

- [Wire Strippers](https://www.sparkfun.com/products/12630)
- [Cutter](https://www.sparkfun.com/products/11952)
- [Hook-up Wires](https://www.sparkfun.com/products/11367)
- [Soldering Iron](https://www.sparkfun.com/categories/367)
- [Solder](https://www.sparkfun.com/categories/368)
- [Multimeter](https://www.sparkfun.com/categories/372)

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/electric-power)

### Electric Power 

An overview of electric power, the rate of energy transfer. We\'ll talk definition of power, watts, equations, and power ratings. 1.21 gigawatts of tutorial fun!

[](https://learn.sparkfun.com/tutorials/what-is-a-battery)

### What is a Battery? 

An overview of the inner workings of a battery and how it was invented.

## Hardware Overview

### Parts of the Board

The circuit is constructed by feeding an MCP73831 charge controller IC to the LiPo battery port, and to the input of a PAM2401 boost controller. Power always flows to the boost circuit, so an enable pin is provided to allow the booster to be shut down during charging if desired. Multiple connection types are provided for the battery, charge source, and switch to allow flexibility of application.

[![Board Layout 1](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/6/9/5/BoardLayout1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/BoardLayout1.png)

*Charger input, battery port, enable pin, and output pins of the 5V/1A Charger/Booster.*

The image below shows the location of the surface mount battery switch and external switch pins which are included to provide an additional option to control the output. Two LEDs are included to provide feedback on system status.

[![Board Layout 2](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/6/9/5/BoardLayout2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/BoardLayout2.png)

*Switch options and status LEDs provided for the 5V/1A Charger/Booster.*

### Functions

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Item                                Description
  ----------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Output Pins\                        Get **5V, 1A** out here! The \'OUT\' pins are labeled with polarity.\

  Battery Port                        Insert a LiPo battery here through the JST connector or solder directly to the PTH pins underneath the connector. These ins are labeled with polarity.

  Charger Input\                      Supply **5V, 500mA** here to charge. You can use a micro-B USB cable or solder directly to the PTH pins. These \'IN\" pins are labeled with polarity.\

  Battery Switch                      The on-board switch is a physical battery disconnect. When in the ON position, the battery is connected to the booster/charger. When flipped to the OFF position, the battery\'s positive lead is isolated from all electronics, and zero current will be drawn.\

  EXT SW Pins\                        These run parallel to on-board battery switch contacts. A higher current switch can be connected through these pins. If you\'re constantly drawing large currents or want a remote battery disconnect switch, connect it here.\

  EN Pin\                             The EN pin is enabled by default. This pin floats high and can be connected to ground to turn the output off. This is useful if your load circuit can\'t be put into low power mode for charging.\

  Charge LED\                         The charge LED indicates blue when the charger IC is attempting to charge the battery. It will turn off when the battery is fully charged. *Note: If current is being drawn while the battery is being charged, the charger may think the battery is never quite full and continue sourcing current.*\

  Boost LED\                          This LED indicates red when voltage is present on the output pins.\
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Charge Status LED

The on-board blue CHARGE LED can be used to get an indication of the charge status of your battery. Below is a table of other status indicators depending on the state of the charge IC.

  ------------------ -------------------------------------------
  **Charge State**   **LED status**
  No Battery         Floating (should be OFF, but may flicker)
  Shutdown           Floating (should be OFF, but may flicker)
  Charging           ON
  Charge Complete    OFF
  ------------------ -------------------------------------------

\

## Hardware Assembly

It\'s easy to get started on your bench. Simply plug the LiPo into the battery JST connector, charge with a micro-B USB supply, and solder your load to the output pins. This section shows some tips and alternate ways to configure the ports.

[![Connecting to the Charge and Battery Ports](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-01.jpg)

*(top) Without modification, the charger and battery can be plugged straight in. (bottom) Connections can be made to one or both of the battery/charger ports by way of soldering wires into the provided holes.*

### Covered Battery Pins

There are a pair of through-holes peeking out from underneath the JST connector. Here\'s how to safely remove the JST and apply battery leads directly. This also lowers the profile of the circuit board.

Make several small cuts to split the JST housing using a cutter. If you try and take the whole thing off at once, you risk pulling up the pads.

[![Cutting the JST Housing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-02.jpg)

*Splitting the top off the JST connector.*

With the top removed, the pins aren\'t captured in the housing anymore and they can be pulled off with the soldering iron one by one.

[![Remove JST Pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-03.jpg)

*Unsoldering the pins*

Alternatively, you can hot air the JST connector off, but it may melt in the process.

**Caution:** When working with a live battery where voltage is always present, don\'t cut both leads at the same time! This will short out the battery and damage the cutters. Work with each wire individually.

Cut and [strip part of the end of the wire](https://learn.sparkfun.com/tutorials/working-with-wire#stranded-vs-solid). Then [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the end to its respective through hole.

[![Soldering Ground Wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-04.jpg)

*Connecting the first wire*

[![Solder Second Wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-05.jpg)

*Connecting the second wire*

### Charge Source Pins

As with the JST port, you may wish to charge your lipos from a source other than a micro-B, such as a 5v barrel or bench supply. The USB port is difficult to remove without damage to the board, so leave it in and just use the \'+\' and \'-\' pins provided by soldering some hookup wire to the respective pins. To connect to a barrel jack easily, you could use a [female barrel jack adapter](https://www.sparkfun.com/products/10288).

**Heads up!** Never supply two power sources for charging at the same time!

[![Connecting to the Charge Source Through Hole Pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-06.jpg)

*The charger booster with a barrel jack attached.*

### External Switch Pins

The onboard switch is rated for 600mA. Using the full current output available, this rating will be violated. It won\'t have any immediate effect and is alright for peaky load with a nominal 500mA draw, but can lead to heat and corrosion depending on your application. If it\'s found to be a problem, solder a higher current switch (like the [SPST rocker switch](https://www.sparkfun.com/products/11138)) into the \'EXT SW\' pins.

[![High Current External Switch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-07.jpg)

*A high current capable panel switch is used to bypass the on-board switch.*

Using a high current switch, the two switches are now in parallel so either one can be used to energize the circuit. If using an external switch, be sure to leave the on-board switch in the OFF position.

Or you can jumper the external switch pins together and use the enable pin to switch power. Further details will be explained in the next section with the enable pin.

### Enable Pin

Another method to remove battery load is to use the enable pin on the PAM2401. It\'s pulled up with a resistor on the board, so leaving it floating will default to an enabled state. To disable, it can be connected to the neighboring ground pin. The pin consumes very little current so a light duty switch (like the [mountable slide switch](https://www.sparkfun.com/products/14330)) can be used.

[![Enable Pin with Switch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/5V_1Amp_Charger_Booster_Hookup_Guide-08.jpg)

*A small switch can be used to disable the booster.*

In this configuration, the onboard switch may not be necessary and can be bypassed by putting a jumper in the external switch holes. The battery won\'t be truly isolated though, and can drain over time. In the disable state, the current draw from the battery is about 6uA so it should take years to discharge.

Alternately, the pin can be driven by a logic source. The pin is 6V tolerant, with a logic-high threshold at 1/2 battery voltage, and a lower threshold of 0.2V.

## Charging a Battery

When a voltage is supplied to the charger, the MCP73831 charge IC comes alive and starts making decisions on how to regulate. First, it regulates current to 500mA until a certain voltage is reached, then it regulates voltage until current goes (close) to zero. When this happens, the charger IC shuts off.

[![MCP73831 Charge Current Regulation](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/chargecycle.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/chargecycle.png)

*As shown in the MCP73831 datasheet, charge current drops as battery voltage rises*

The charger IC is making decisions based on the battery voltage and output load, and can be tricked into an invalid mode. Follow these rules to get a reliable charge:

- Turn on the battery switch before connecting the charger.
- Consume no more than 20mA from the output terminals during charging.

**Using small batteries:** It\'s not recommended, but if you use sub amp-hour batteries you may find they don\'t charge correctly. By default, the board is set to charge at 500mA. 500mA is too much for them, so the protection circuits get in the way and creates a situation where the battery is dumping the input current rather than using it to charge. If you decide to go this route, swap RPROG with a 10K resistor to limit the charge circuit to 100mA. To calculate the programming resistor needed with the small batteries, you can use the following formula from the [datasheet](https://cdn.sparkfun.com/datasheets/Components/General%20IC/33244_SPCN.pdf):\
\

## Connecting a Load

Eager to get your 5V? Just connect up to the output terminals!

[![Output Pinst](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/outputterms.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/outputterms.jpg)

*Closeup of the output terminals are marked with polarity.*

But there\'s always more to know. An ideal booster circuit translates all input power to output power, so if the output is providing 5V @ 1A, or 5W, 5W must also be going *into* the booster. But if the input voltage is down to the battery lower limit of 3V, it will require 1.666A! With an efficiency of around 85%, it requires almost 2A on the input!

Here\'s a graph of the charger booster\'s measured performance:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/currentGraph.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/currentGraph.png)

*Input current (right scale) and output voltage (left scale), shown as a function of output load. Notice that the output voltage sags slightly, but is pretty well regulated, and that input current is always larger than output current for a booster circuit.*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/EfficiencyGraph.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/EfficiencyGraph.png)

*Input and output power is shown (left scale), as well as overall efficiency (right scale).*

## Using Multiple Charger Boosters

5V may be fine for microcontrollers, addressable LEDs, and servos, but with motors sometimes some extra kick is required. With electric motors, *speed is proportional to voltage*, and *torque is proportional to current*. So if we want robot acceleration we\'d want a high torque motor (low resistance), and if we want to go fast we\'ll need to supply a large voltage. This section shows how to use multiple boosters and what that means for the voltage levels.

The boosters have bypass diodes placed across their outputs. This means that if a negative voltage is presented to the output, it will conduct rather than apply negative voltage to the rails.

This allows the boosters to be placed in series to create voltages larger than 5, with a couple of caveats.

**Charging:** If one charger\'s ground is connected to the next charger\'s positive rail, the two grounds are at different voltages. If you are charging multiple cells, you can\'t connect all of them to the same source. **Use a separate isolated USB wall adapter for each charger when connected in series.**

**Running with one dead battery:** For each booster/charger that is not generating voltage in the stack, 0.5V will be subtracted from the sum of running boosters/chargers.

The following two diagrams show how two chargers in series interact. With both chargers on and supplying 5V, the output runs at 10V, and 1 amp is driven through the booster circuit (shown as an ideal supply).

[![Two Charger/Boosters in Series](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/bothon.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/bothon.png)

*Two active booster circuits working together to produce 10V*

When one booster stops producing voltage, it\'s still in the current loop and must pass the 1A that the other booster can provide. The protection diodes allow the current to slip by, but at the cost of a diode drop. For these B340A Schottky diodes, that\'s about 0.5V. The output voltage is now 4.5V.

[![Two Charger/Boosters in Series with One Booster On](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/onedead.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/onedead.png)

*Picture of boosters with one dead battery*

### Increasing Current

Life gets a little trickier if more current is needed. By supplying your own diodes and \"diode OR-ing\" the outputs, you can get increased current at the cost of a diode drop, or somewhere around 4.5V. You may get away with just connecting up the outputs but run the risk of back-feeding one output with the other.

**Diodes Required:** Each booster\'s output must be passed through a diode before connecting in parallel

**Output Voltage:** The voltage of the combined boosters will be at a diode drop below the output regulated voltage.

[![Two Charger/Boosters in Parallel with Diodes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/5/summingCurrent.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/5/summingCurrent.png)

*Two supplies in parallel can source more current, but external diodes are required.*