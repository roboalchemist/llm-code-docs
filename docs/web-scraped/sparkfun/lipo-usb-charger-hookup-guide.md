# Source: https://learn.sparkfun.com/tutorials/lipo-usb-charger-hookup-guide

## Introduction

We love LiPo batteries! They pack a walloping, power-supplying punch in a tiny, flat package. And, they\'re incredibly easy to recharge, when that time comes. If you\'re looking to make your project mobile and easily rechargeable, we can\'t recommend this pairing enough: an [850 mAh LiPo battery](https://www.sparkfun.com/products/341) and an embeddable [USB LiPo charger](https://www.sparkfun.com/products/12711).

[![SparkFun USB LiPoly Charger - Single Cell](https://cdn.sparkfun.com/r/600-600/assets/parts/9/4/5/6/12711-01.jpg)](https://www.sparkfun.com/sparkfun-usb-lipoly-charger-single-cell.html)

### [SparkFun USB LiPoly Charger - Single Cell](https://www.sparkfun.com/sparkfun-usb-lipoly-charger-single-cell.html) 

[ PRT-12711 ]

If you need to charge LiPo batteries, this simple charger will do just that, and do it fast! The SparkFun USB LiPo Charger is...

[ [\$18.50] ]

This tutorial will explain how to use the [USB LiPo Charger](https://www.sparkfun.com/products/12711) with any of our [single-cell LiPo batteries](https://www.sparkfun.com/search/results?term=lithium+polymer+3.7V). We\'ll focus on the [LiPo Charger and Battery Retail kit](https://www.sparkfun.com/products/12722), but this information can be applied to that charger and any compatible battery.

### Required Materials

- [USB LiPo Charger](https://www.sparkfun.com/products/12711)
- A [single-cell LiPo battery](https://www.sparkfun.com/search/results?term=lithium+polymer+3.7V)
  - The charger can be made to work with batteries of any capacity, including [40mAh](https://www.sparkfun.com/products/11316), [110mAh](https://www.sparkfun.com/products/731), [400mAh](https://www.sparkfun.com/products/10718), [850mAh](https://www.sparkfun.com/products/341), [1000mAh](https://www.sparkfun.com/products/339), [2000mAh](https://www.sparkfun.com/products/8483), and the [6000mAh fatpack](https://www.sparkfun.com/products/8484).
- A **5V power source**, options include:
  - A computer USB port with attached [mini-B USB cable](https://www.sparkfun.com/products/11301)
  - A [USB Wall Adapter](https://www.sparkfun.com/products/11456) and mini-B cable
  - A [5V Wallwart Supply](https://www.sparkfun.com/products/8269)

### Suggested Reading

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

## Inputs and Outputs

On this page, we\'ll dissect the USB charger, examining all of the inputs, outputs, and specifications of the board.

[![Single Cell LiPoly Charger Annotated ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/4/charger-annotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/4/charger-annotated.png)

### Charger Input \-- Power Supply

First, you\'ll need something to supply power to the charger, so it can regulate power to the battery. Connect your power supply to one of these two inputs: a **barrel jack** (5.5mm outer diameter, 2.1mm center pole, center-positive) or a **mini-B USB** connector.

Your power **supply voltage** should be **between 4.75 and 6V**. A 5V USB supply \-- from a [mini-B cable](https://www.sparkfun.com/products/11301) connected to either a computer USB port or [wall adapter](https://www.sparkfun.com/products/11456) \-- makes for a perfect power source. Or, if you want to use the barrel jack input, we recommend the [5V wall adapter](https://www.sparkfun.com/products/8269).

[![USB adapter](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/2/2/4/usb-wall.jpg)](https://www.sparkfun.com/products/11456) [![5V wallwart](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/2/2/4/5v-wall.jpg)](https://www.sparkfun.com/products/8269)

The **current requirements** of the supply will depend on how you\'ve [set the charge current](https://learn.sparkfun.com/tutorials/lipo-usb-charger-hookup-guide/setting-the-charge-current) on the board. By default, the charge current is set to **500mA**, so make sure your supply can handle that. Computer and laptop USB ports are most suspect here; 500mA is the defined max a port can supply, and oftentimes they\'re set to have an even lower output than that (e.g. 100mA).

You can safely attach both a 5V wall-wart and USB supply to the board. There is some protection ([diodes!](https://learn.sparkfun.com/tutorials/diodes)) on-board to prevent reverse current. The higher-voltage supply will source power to the chip.

**Warning:** While the chip can take up to 6V for the maximum voltage, it can only take 1500mA for the max current. If you use the [6V/2A power supply](https://www.sparkfun.com/products/14158) as the power supply, then you are very likely to burn the chip out on the board. If you need a wall adapter with a barrel jack, then we recommend the [5V/2A power supply](https://www.sparkfun.com/products/12889).

### Charger Output \-- Single-Cell LiPo Battery

Once you\'ve connected a power supply to your charger, the next step is to connect a battery. This board will only charge a very specific battery, make sure it meets these requirements:

- **Single-Cell Batteries Only** \-- Your LiPo should have a nominal voltage output of about 3.7V, and get up to around 4.2V at a full charge. That means single-cell LiPo\'s only. If you have a [multi-cell battery](https://www.sparkfun.com/products/11855) \-- something with a nominal voltage of 7.4V or more \-- this isn\'t the charger for you.

[![Battery connected to charger](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/4/LiPo_USB_Charger_tutorial_pics-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/4/LiPo_USB_Charger_tutorial_pics-01.jpg)

- **Battery Chemistry** \-- The charger will only work with **Lithium-Polymer or Lithium-Ion** batteries.
- **Capacity Considerations** \-- To avoid explosions (which are only very briefly fun), you shouldn\'t charge these LiPos at a current over 1C. That means a 500mAh battery shouldn\'t be given a charge current over 500mA, a 100mAh shouldn\'t be charged higher than 100mA. This board is designed to charge at 500mA out-of-the-box, but it\'s easy enough to change that rate. See the next page if your battery\'s capacity is under 500mAh.

All of our compatible batteries are terminated with a white **JST connector**, which you can plug directly into the mating black connector next to the *BATT IN→* label. If your battery is terminated with some, weird, non-JST connector, you can also use the **un-populated 0.1\"-pitch header** directly behind the JST connector. Wires or other connectors can be [soldered](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) to this header, if desired.

### System Output

The LiPo USB Charger is designed to be easily **embeddable inside a project**. The *←SYS OUT* connector allows you to connect your battery output to the remaining parts of your project.

[![Using the System Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/4/LiPo_USB_Charger_tutorial_pics-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/4/LiPo_USB_Charger_tutorial_pics-02.jpg)

*You can use the \"SYS OUT\" header to power a [3.3V Arduino Pro](https://www.sparkfun.com/products/10914). All while leaving your battery connected to the charger.*

As with the battery connection, you can use either the JST connector or the nearby 0.1\"-pitch header to connect your project.

The *SYS OUT* output will connect your project directly to your battery. That means the battery supply voltage (somewhere between 3.6 and 4.2V) will power your project. Make sure you regulate that as necessary.

### [][Charge Status LED](https://learn.sparkfun.com/tutorials/lipo-usb-charger-hookup-guide#charge_LED)

The on-board red *Charging* LED can be used to get an indication of the **charge status** of your battery.

  Charge State      LED status
  ----------------- -------------------------------------------
  No Battery        Floating (should be OFF, but may flicker)
  Shutdown          Floating (should be OFF, but may flicker)
  Charging          ON
  Charge Complete   OFF

\

If you want to add your own, larger LED, there\'s an unpopulated footprint where you can solder either a [3mm](https://www.sparkfun.com/categories/171) or [5mm](https://www.sparkfun.com/categories/172) LED in the tiny (but bright!) red LED\'s stead. Make sure you get the [polarity](https://learn.sparkfun.com/tutorials/polarity) right, though.

## Setting the Charge Current

Before you plug a battery into the charger, you should be aware of your **battery\'s capacity** and the **charge current** supplied by the charger. To be safe[\*](#protection), you should keep the charge current **at or below 1C** of your battery. That means you should charge your 850mAh battery at 850mA or less, and a 100mAh battery at 100mA or less.

The charge current controls **how fast your battery will charge**. If you have a 1000mAh battery, charging at 1000mA will fully charge that battery in 1 hour. Charging it at 500mA will mean a full charge takes twice as long \-- 2 hours. So more charge current is better\...as long as it doesn\'t exceed your battery\'s specifications.

The featured component on the LiPo USB Charger board \-- an [MCP73831](http://cdn.sparkfun.com/datasheets/Components/General%20IC/33244_SPCN.pdf) \-- has a **programmable charge current** feature. It can be set to deliver anywhere **between 15mA and 500mA** to a battery. To program that value, a resistor is connected from the *PROG* pin to ground. There are already two resistors on-board, which can set the charge current to either 500mA and 100mA. A small jumper is used to select between those. You can also add your own resistor, to set a custom charge current.

### Jumper-Selecting

Next to the charge-status LED there are three bare pads that form a **two-way jumper**. The center pad connects to the MCP73831\'s *PROG* pin, and the outer two pads connect to a pair of resistors. The labels next to those outer pads indicate the charge current that they set.

[![Jumper location highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/4/jumper-location.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/4/jumper-location.png)

If you look *really* closely at that jumper, you may see a small trace connecting the middle pad to the *500mA*-labeled outer pad. As such, this board is **configured to deliver a 500mA current by default**.

To change the charge current to 100mA, you\'ll need to **cut that small trace** between the pads (a [hobby knife](https://www.sparkfun.com/products/9200) is recommended), and apply a solder blob to connect the *100mA*-labeled pin to the center pad.

### Custom Charge Current

If neither 100mA or 500mA will work for you, there is an unpopulated resistor footprint to allow you to set a custom charge current.

[![Resistor plugged into board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/4/resistor-charge-current.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/4/resistor-charge-current.png)

Before adding the resistor, **disconnect both jumpers** discussed in the section above. Then use this equation to select your resistor:

[![\\I\_ = \\frac}\\;\\; \\mathrm\\;\\; R\_ = \\frac}](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/4/equation-charge-current.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/4/equation-charge-current.gif)

For example, if you want to charge a [400mAh battery](https://www.sparkfun.com/products/10718) at exactly 400mA, solder in a 2.5kΩ resistor (you may have to series a [2.2k and 330](https://www.sparkfun.com/products/10969)).

------------------------------------------------------------------------

[\*] Most batteries include **over-current protection** \-- implemented on the little circuit board under the yellow tape \-- which will keep the battery from blowing up if you supply too much current. But it\'s best to not rely on that circuit: you\'ll save power and your sanity.