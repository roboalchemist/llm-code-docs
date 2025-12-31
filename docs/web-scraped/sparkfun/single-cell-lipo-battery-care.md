# Source: https://learn.sparkfun.com/tutorials/single-cell-lipo-battery-care

## Introduction

**Note:** This tutorial was ported over from the [older LiPo Battery Care tutorial](https://www.sparkfun.com/tutorials/241). Tips from the [LilyPad Basics: Powering Your Project (Power Options: Rechargeable Lithium Polymer Batteries)](https://learn.sparkfun.com/tutorials/lilypad-basics-powering-your-project/power-options-rechargeable-lithium-polymer-batteries) were also added to this tutorial.

[Lithium-Ion Polymer (LiPo) batteries](https://www.sparkfun.com/categories/tags/lithium-polymer) are a favorite of ours. Very light weight and some of the highest energy densities available. We affectionately call this battery the \'car battery\' because it\'s huge. Not physically (it\'s 110 grams!) but because this 6Ah LiPo in capable of outputting 6 Amps over the period of one hour! This is a very large amount of power in our low-power embedded world. Please don\'t confuse this with a real car battery!

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/8484-Lithium_Ion_Battery_6Ah_JST_PH_Connector_small.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/8484-Lithium_Ion_Battery_6Ah_JST_PH_Connector_small.jpg)

*A [LiPo battery](https://www.sparkfun.com/products/13856) capable of producing 6 Amps for one hour!*

### Required Materials

To follow along with this tutorial, you will need the following materials at a minimum. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary. Below is a wishlist of the parts that you need to get started if you were to charge a LiPo battery and then remove the connector.

### Single Cell LiPo Chargers

There are a variety of development boards and breakout boards with a dedicated single cell LiPo battery charge circuit. Below are a [few examples from the SparkFun catalog that have the MCP73831](https://www.sparkfun.com/categories/tags/lipo-charger). The charge IC used and charge rate will depend on the design.

[![SparkFun IoT RedBoard - ESP32 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/8/0/0/ESP32_03.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html)

### [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html) 

[ WRL-19177 ]

The IoT RedBoard is an ESP32 WROOM-equipped development board that has everything you need in an Arduino Uno with extra perks...

[ [\$41.87] ]

[![SparkFun Adjustable LiPo Charger](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/9/1/14380b-01.jpg)](https://www.sparkfun.com/sparkfun-adjustable-lipo-charger.html)

### [SparkFun Adjustable LiPo Charger](https://www.sparkfun.com/sparkfun-adjustable-lipo-charger.html) 

[ PRT-14380 ]

The SparkFun Adjustable LiPo Charger is a single-cell lithium polymer (LiPo) and lithium ion battery charger. Because it's ...

[ [\$13.95] ]

[![SparkFun LiPo Charger Basic - Mini-USB](https://cdn.sparkfun.com/r/140-140/assets/parts/4/8/6/3/10401-SparkFun_LiPo_Charger_Basic_-_Mini-USB-02.jpg)](https://www.sparkfun.com/sparkfun-lipo-charger-basic-mini-usb.html)

### [SparkFun LiPo Charger Basic - Mini-USB](https://www.sparkfun.com/sparkfun-lipo-charger-basic-mini-usb.html) 

[ PRT-10401 ]

If you need to charge LiPo batteries, this simple charger will do just that. It is designed to charge single-cell Li-Ion or L...

[ [\$10.95] ]

[![SparkFun MicroMod Main Board - Single](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/5/7/7/20748-DEV_SparkFun_MicroMod_Main_Board_Single_v21-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-main-board-single.html)

### [SparkFun MicroMod Main Board - Single](https://www.sparkfun.com/sparkfun-micromod-main-board-single.html) 

[ DEV-20748 ]

The MicroMod Main Board is a specialized carrier board that allows you to interface a MicroMod Processor Board with a single ...

[ [\$18.50] ]

### Single Cell LiPo Battery

Of course, you will also need a single cell LiPo battery. Below are a few LiPo batteries to choose from in the [SparkFun catalog](https://www.sparkfun.com/categories/54).

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

[![Lithium Ion Battery - 1250mAh (IEC62133 Certified)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/6/0/6/17748-Lithium_Ion_Battery_-_1250_mAh__IEC62133_certified_-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-1250mah-iec62133-certified.html)

### [Lithium Ion Battery - 1250mAh (IEC62133 Certified)](https://www.sparkfun.com/lithium-ion-battery-1250mah-iec62133-certified.html) 

[ PRT-18286 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1250 mAh and is IE...

**Retired**

[![Lithium Ion Battery - 6Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/3/13856-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-6ah.html)

### [Lithium Ion Battery - 6Ah](https://www.sparkfun.com/lithium-ion-battery-6ah.html) 

[ PRT-13856 ]

If you need some juice, this 6Ah Lithium Ion Battery is for you. These are very compact batteries based on Lithium Ion chemis...

[ [\$48.44] ]

### Tools

Need some help removing the single cell LiPo battery from the JST connector? Try grabbing a needle nose plier or diagonal cutters. Or you can use a hobby knife to whittle down the JST-PH\'s locking tabs.

[![Needle Nose Pliers](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/3/3/08793-03-L.jpg)](https://www.sparkfun.com/needle-nose-pliers.html)

### [Needle Nose Pliers](https://www.sparkfun.com/needle-nose-pliers.html) 

[ TOL-08793 ]

Mini Pliers. These are great little pliers! A must have for any hobbyist or electrical engineer. Crucial for inserting device...

[ [\$3.60] ]

[![Diagonal Cutters](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/3/4/08794-03-L.jpg)](https://www.sparkfun.com/diagonal-cutters.html)

### [Diagonal Cutters](https://www.sparkfun.com/diagonal-cutters.html) 

[ TOL-08794 ]

Mini Diagonal Cutters. These are great little cutters! A must have for clipping leads and extra solder tails. 4\" long.

[ [\$3.75] ]

[![Hobby Knife](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/6/09200-Hobby_Knife-01.jpg)](https://www.sparkfun.com/hobby-knife.html)

### [Hobby Knife](https://www.sparkfun.com/hobby-knife.html) 

[ TOL-09200 ]

It\'s like an Xacto knife, only better. We use these extensively when working with PCBs. These small knives work well for cutt...

[ [\$3.75] ]

**Note:** If you decide to not use needle nose pliers, we recommend getting a low cost diagonal cutters instead of flush cutters. This will prevent users from damaging their nicer flush cutters when pulling the JST connector out.

### You May Also Need

For strain relief, you can use some electrical tape and scissors to secure the wires on the single cell LiPo battery. You may want a marker to label the battery.

- Electrical Tape
- Scissors
- Marker

### Suggested Reading

If you aren't familiar with the following concepts, we also recommend checking out a few of these tutorials before continuing

[](https://learn.sparkfun.com/tutorials/connector-basics)

### Connector Basics 

Connectors are a major source of confusion for people just beginning electronics. The number of different options, terms, and names of connectors can make selecting one, or finding the one you need, daunting. This article will help you get a jump on the world of connectors.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/how-lithium-polymer-batteries-are-made)

### How Lithium Polymer Batteries are Made 

We got the opportunity to tour the Great Power Battery factory. Checkout how LiPos are made!

[](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)

### How to Use a Multimeter 

Learn the basics of using a multimeter to measure continuity, voltage, resistance and current.

[](https://learn.sparkfun.com/tutorials/what-is-a-battery)

### What is a Battery? 

An overview of the inner workings of a battery and how it was invented.

## Charging LiPo Batteries, Safely

⚡ **Warning:** Never ever charge a LiPo with anything but a special LiPo charger! We recommend you do not leave a charging battery unattended.

Back in the old days, there were only two chargers available in SparkFun\'s catalog. The [standard charger based on the old MAX1555 IC](https://www.sparkfun.com/products/726) and our [faster charger based on the newer MCP73831 IC](https://www.sparkfun.com/products/10217). You will notice the MAX1555 and MCP73831 populated as a 5-pin IC as shown in the images below. The MAX1555 was great but its limited charging current (300mA) and diminishing market availability way back when pushed us towards creating chargers based on the MCP73831 (500mA per hour charging rate).

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/726-USB_Single_Cell_LiPoly_Charger_MAX1555.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/726-USB_Single_Cell_LiPoly_Charger_MAX1555.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/12711-USB_Single_Cell_LiPoly_Charger_MCP73831.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/12711-USB_Single_Cell_LiPoly_Charger_MCP73831.jpg)
  *Retired USB Single Cell LiPo Charger with MAX1555*                                                                                                                                                                     *USB Single Cell LiPo Charger with MCP73831*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You will notice the MCP73831 populated on select development boards and a variety of breakout boards with different USB connectors. Below are a few examples with the MCP73831 populated on different boards found in the [SparkFun catalog](https://www.sparkfun.com/categories/tags/lipo-charger).

[![SparkFun IoT RedBoard - ESP32 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/8/0/0/ESP32_03.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html)

### [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html) 

[ WRL-19177 ]

The IoT RedBoard is an ESP32 WROOM-equipped development board that has everything you need in an Arduino Uno with extra perks...

[ [\$41.87] ]

[![SparkFun Adjustable LiPo Charger](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/9/1/14380b-01.jpg)](https://www.sparkfun.com/sparkfun-adjustable-lipo-charger.html)

### [SparkFun Adjustable LiPo Charger](https://www.sparkfun.com/sparkfun-adjustable-lipo-charger.html) 

[ PRT-14380 ]

The SparkFun Adjustable LiPo Charger is a single-cell lithium polymer (LiPo) and lithium ion battery charger. Because it's ...

[ [\$13.95] ]

[![SparkFun LiPo Charger Basic - Mini-USB](https://cdn.sparkfun.com/r/140-140/assets/parts/4/8/6/3/10401-SparkFun_LiPo_Charger_Basic_-_Mini-USB-02.jpg)](https://www.sparkfun.com/sparkfun-lipo-charger-basic-mini-usb.html)

### [SparkFun LiPo Charger Basic - Mini-USB](https://www.sparkfun.com/sparkfun-lipo-charger-basic-mini-usb.html) 

[ PRT-10401 ]

If you need to charge LiPo batteries, this simple charger will do just that. It is designed to charge single-cell Li-Ion or L...

[ [\$10.95] ]

[![SparkFun MicroMod Main Board - Single](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/5/7/7/20748-DEV_SparkFun_MicroMod_Main_Board_Single_v21-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-main-board-single.html)

### [SparkFun MicroMod Main Board - Single](https://www.sparkfun.com/sparkfun-micromod-main-board-single.html) 

[ DEV-20748 ]

The MicroMod Main Board is a specialized carrier board that allows you to interface a MicroMod Processor Board with a single ...

[ [\$18.50] ]

Other notable LiPo chargers in the SparkFun catalog is the BQ24075 populated on the Battery Babysitter - LiPo Battery Manager, and LT3652 populated on the Sunny Buddy - MPPT Solar Charger. Both can be used to charge a single cell LiPo battery through USB or a solar panel, respectively.

[![SparkFun Battery Babysitter - LiPo Battery Manager](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/3/1/13777-01.jpg)](https://www.sparkfun.com/sparkfun-battery-babysitter-lipo-battery-manager.html)

### [SparkFun Battery Babysitter - LiPo Battery Manager](https://www.sparkfun.com/sparkfun-battery-babysitter-lipo-battery-manager.html) 

[ PRT-13777 ]

The SparkFun Battery Babysitter is an all-in-one single-cell Lithium Polymer (LiPo) battery manager. It's half battery char...

[ [\$23.95] ]

[![SparkFun Sunny Buddy - MPPT Solar Charger](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/7/2/12885-01.jpg)](https://www.sparkfun.com/sparkfun-sunny-buddy-mppt-solar-charger.html)

### [SparkFun Sunny Buddy - MPPT Solar Charger](https://www.sparkfun.com/sparkfun-sunny-buddy-mppt-solar-charger.html) 

[ PRT-12885 ]

This is the Sunny Buddy, a maximum power point tracking (MPPT) solar charger for single-cell LiPo batteries. This MPPT solar ...

[ [\$32.95] ]

### Recommended Charge Rate for Single Cell LiPo Batteries

To avoid explosions (which are only very briefly fun), you should not charge these LiPos at a current over the battery\'s capacity, typically 1C for fast charging. To be safe ^[\[1\]](https://learn.sparkfun.com/tutorials/single-cell-lipo-battery-care#note_1)^, you should keep the charge current at or below 1C of your battery as indicated in the datasheets.

What does this mean? Well, lets take a look at the datasheet for the [850mAh LiPo battery](https://www.sparkfun.com/products/13854). The image shown below highlights the recommended standard charge rate and maximum continuous charge current, where C is the capacity of the LiPo battery. For a standard charge rate of 0.2C, an 850mAh LiPo battery can be charged at a rate of 170mA. When charging at the maximum charge rate of 1C, an 850mAh LiPo battery can be charged at a rate of 850mA.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/850mAh_LiPo_Battery_Datasheet_Highlighted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/850mAh_LiPo_Battery_Datasheet_Highlighted.jpg)

*[Datasheet highlighted](http://cdn.sparkfun.com/datasheets/Prototyping/850mah-en-1.0ver.pdf) for the 850mAh LiPo Battery\'s Charge Rates*

What does this mean with the LiPo chargers available? Well, if you have an **500mAh single cell LiPo battery**, it should not be given a charge current over 500mA. You should use a charger that is able to charge the LiPo battery with a dedicated single cell LiPo charger **set at or below 500mA**. The minimum LiPo battery that SparkFun has available currently that is compatible at this rate that you can safely charge is 850mAh. Other larger single cell LiPo batteries can also be charged at this rate.

[![Lithium Ion Battery - 850mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/1/13854-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-850mah.html)

### [Lithium Ion Battery - 850mAh](https://www.sparkfun.com/lithium-ion-battery-850mah.html) 

[ PRT-13854 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 850...

[ [\$13.61] ]

[![Lithium Ion Battery - 1250mAh (IEC62133 Certified)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/6/0/6/17748-Lithium_Ion_Battery_-_1250_mAh__IEC62133_certified_-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-1250mah-iec62133-certified.html)

### [Lithium Ion Battery - 1250mAh (IEC62133 Certified)](https://www.sparkfun.com/lithium-ion-battery-1250mah-iec62133-certified.html) 

[ PRT-18286 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1250 mAh and is IE...

**Retired**

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

What about a **100mAh LiPo battery?** Yeah, those should not be charged higher than 100mA. Make sure to find a single cell LiPo charger that is **set at or below 100mA**. The minimum LiPo battery that SparkFun has available currently that is compatible at this rate that you can safely charge is 110mAh. Other larger single cell LiPo batteries (like the 400mAh shown below or any of the ones shown earlier) can also be charged at this rate.

[![Lithium Ion Battery - 110mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/0/13853-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-110mah.html)

### [Lithium Ion Battery - 110mAh](https://www.sparkfun.com/lithium-ion-battery-110mah.html) 

[ PRT-13853 ]

This is a very small, extremely light weight battery based on Lithium Ion chemistry. This is the highest energy density curre...

[ [\$7.53] ]

[![Lithium Ion Battery - 400mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/5/8/13857-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-400mah.html)

### [Lithium Ion Battery - 400mAh](https://www.sparkfun.com/lithium-ion-battery-400mah.html) 

[ PRT-13851 ]

This is a very small, extremely lightweight battery based on Lithium Ion chemistry, with the highest energy density currently...

[ [\$7.98] ]

Depending on the designer, the charge rate can be set to a default rate of either 500mA or 100mA. Certain boards can have a 3-way jumper, switches, and/or PTH footprint to solder a resistor to adjust the charge rate. Below is a schematic of the USB LiPoly Charger. As you can see, this particular board is set at a default rate of 500mA with a 3-way jumper. [Cutting the jumper](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all#cutting-a-trace-between-jumper-pads) and adding a solder blob between the center pad and the other jumper pad will set the charge rate to 100mA.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/USB_LiPo_Charger_Schematic_MCP73831_highlighted.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/USB_LiPo_Charger_Schematic_MCP73831_highlighted.JPG)

But what about that lone **40mAh LiPo Battery** in SparkFun\'s catalog?! If you look closely at the schematic shown earlier, there is also a footprint (not currently highlighted but it is connected to the same net) that allows users to solder a PTH resistor. This allows a user to set the charge rate to a value other than 500mA or 100mA. There\'s not that a lot of development boards and breakout boards that have the footprint available. Make sure to be careful when connecting a USB cable to those boards when a 40mAh battery is attached. You will want to remove the battery and connect the LiPo battery to a separate LiPo Charger that is **set at or below 40mA**.

[![Polymer Lithium Ion Battery - 40mAh (JST-PH)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/5/9/13857-01.jpg)](https://www.sparkfun.com/polymer-lithium-ion-battery-40mah.html)

### [Polymer Lithium Ion Battery - 40mAh (JST-PH)](https://www.sparkfun.com/polymer-lithium-ion-battery-40mah.html) 

[ PRT-13852 ]

This is an extremely tiny and light weight battery based on the new Polymer Lithium Ion chemistry.

[ [\$7.14] ]

To calculate the resistor needed on a board with the MCP73831, you can use the following formula from [its datasheet](https://cdn.sparkfun.com/datasheets/Components/General%20IC/33244_SPCN.pdf). Note that this equation is specific for the MCP73831 charge IC.

[![\\I\_ = \\frac}\\;\\; \\mathrm\\;\\; R\_ = \\frac}](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/4/equation-charge-current.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/4/equation-charge-current.gif)

We\'ll just skip ahead of the calculations and tell you that the value to charge at a rate of 40mA is\... 25kΩ! This is quite an odd number for a resistor value in SparkFun\'s catalog. You\'ll need to wire a few resistors wired in series and parallel to connect to the two PTHs (i.e. [10kΩ + 10kΩ + (10kΩ \|\| 10kΩ)](https://learn.sparkfun.com/tutorials/resistors) ). Or you could use resistor with a larger value like 47kΩ that is included in the [resistor kit](https://www.sparkfun.com/products/10969). However, the charge rate will be less: 21.28mA.

^[**\[1\]:**](https://learn.sparkfun.com/tutorials/single-cell-lipo-battery-care#note_1)\ Most\ batteries\ include\ over-current\ protection\ \--\ implemented\ on\ the\ little\ circuit\ board\ under\ the\ yellow\ tape\ \--\ which\ will\ keep\ the\ battery\ from\ blowing\ up\ if\ you\ supply\ too\ much\ current.\ But\ it\'s\ best\ to\ not\ rely\ on\ that\ circuit:\ you\'ll\ save\ power\ and\ your\ sanity.^

**Note:** For users using R/C LiPo batteries (i.e. more than one cell., make sure to use a dedicated LiPo battery balance charger to safely charge the LiPo batteries.\
\

[![Lithium Ion Battery - 1000mAh 7.4v](https://cdn.sparkfun.com/r/140-140/assets/parts/8/2/5/1/11855-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-1000mah-7-4v.html)

### [Lithium Ion Battery - 1000mAh 7.4v](https://www.sparkfun.com/lithium-ion-battery-1000mah-7-4v.html) 

[ PRT-11855 ]

This high discharge LiPo is a great way to power any R/C, robotic, or portable project. This is an excellent choice for anyth...

[ [\$16.95] ]

[![Lithium Ion Battery - 2200mAh 7.4v](https://cdn.sparkfun.com/r/140-140/assets/parts/8/2/5/2/11856-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-2200mah-7-4v.html)

### [Lithium Ion Battery - 2200mAh 7.4v](https://www.sparkfun.com/lithium-ion-battery-2200mah-7-4v.html) 

[ PRT-11856 ]

This high discharge LiPo is a great way to power any R/C, robotic, or portable project. This is an excellent choice for anyth...

**Retired**

[![SkyRC IMAX B6 V2 Professional Balance Charger / Discharger](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/7/0/2/16793-SkyRC_IMAX_B6_V2_Balance_Charger_-_Discharger-01.jpg)](https://www.sparkfun.com/skyrc-imax-b6-v2-professional-balance-charger-discharger.html)

### [SkyRC IMAX B6 V2 Professional Balance Charger / Discharger](https://www.sparkfun.com/skyrc-imax-b6-v2-professional-balance-charger-discharger.html) 

[ PRT-16793 ]

The SkyRC B6 V2 is a DC input high-performance, micro-processor controlled charge/discharge/DC/DC converter with battery mana...

**Retired**

## Types of LiPo Battery Packages

Depending on the manufacturer, there are different packages and connections for Lithium batteries. We will be going over how to connect and disconnect batteries with a JST-PH connector in this section. They will usually have a protection circuit under the yellow kapton tape, and a silver packaging (of course the exception is the [6Ah LiPo battery that is blue](https://www.sparkfun.com/products/13856)).

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com//assets/parts/1/7/6/0/6/17748-Lithium_Ion_Battery_-_1250_mAh__IEC62133_certified_-01.jpg)](https://www.sparkfun.com/products/18286)   [![](https://cdn.sparkfun.com//assets/parts/6/4/3/7/13251-01.jpg)](https://www.sparkfun.com/products/retired/13251)   [![](https://cdn.sparkfun.com//assets/parts/9/7/8/5/12895-01_1.jpg)](https://www.sparkfun.com/products/12895)   [![](https://cdn.sparkfun.com//assets/parts/4/7/2/6/10319-03a.jpg)](https://www.sparkfun.com/products/retired/10319)
  *[1250mAh LiPo battery with JST connector](https://www.sparkfun.com/products/18286)*                                                                                *[110mAh LiPo battery with Solder Tabs](https://www.sparkfun.com/products/retired/13251)*                             *[2600mAh Lithium Ion Battery 18650 Cell](https://www.sparkfun.com/products/12895)*                             *[24.5mm CR2450 Coin Cell Lithium Ion Battery](https://www.sparkfun.com/products/retired/10319)*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------

## JST-PH Connectors

Typically, single cell LiPo batteries are terminated with a two pin JST-PH female connector. These are [polarized connectors](https://learn.sparkfun.com/tutorials/connector-basics#power-connectors) with pin 1 as +VBATT (red wire) and pin 2 connected to ground (black wire). These mate with the two pin JST-PH male connector (shroud).

[![JST Male and Female Connector](https://cdn.sparkfun.com/assets/2/6/0/7/f/51141810ce395f4d7e000007.jpg)](https://cdn.sparkfun.com/assets/2/6/0/7/f/51141810ce395f4d7e000007.jpg)

⚡ **Danger:** Always double check the orientation of the power and ground wires on the battery, depending on the manufacturer they may be reversed!!! All single cell LiPo batteries in the yellow/silver packs carried by SparkFun and SparkFun original boards use this standard configuration.

### JST-PH Connector Locking Tabs

If you look closely at the JST female connector, there are two locking tabs on the top of the connector for a secure connection. However, this can make it hard for anyone that wants to unplug and replug the battery back into the board. After a few inserts and removals, the locking tabs on the JST connector will wear down slightly to the point that you will be able to remove the connector by hand.

[![closeup locking tabs highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/14299_JST_PH_Connector_Close_Up_Highlighted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/14299_JST_PH_Connector_Close_Up_Highlighted.jpg)

⚡ **Danger:** Certain ecosystems use a JST connector for power as well. One example is the micro:bit. Note that the input voltage for the connector is different: it is typically around 3V and is intended to be used with 2xAA batteries. The battery chemistry is different for the AA batteries (usually alkaline with a nominal voltage of about 1.5V). Make sure to not connect the LiPo battery directly to the micro:bit\'s JST connector unless you have a regulated voltage.\
\

[![](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/5/0/Removing_JST_from_MicroBit_2.jpg)](https://cdn.sparkfun.com//assets/learn_tutorials/8/5/0/Removing_JST_from_MicroBit_2.jpg)\
\
*Disconnecting JST Connectors on the micro:bit\
from the [Wireless Remote Control with micro:bit Tutorial](https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit/all%0A)*

## Connecting a LiPo Battery

Inserting the LiPo battery\'s JST connector into it\'s mating connector is a breeze. Simply hold the JST female connector with your index finger and thumb. Then hold board in a similar fashion using your other hand. Align the two JST connectors together. Insert the JST connector into the socket.

[![Inserting JST Connector to Boards](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Fingers_Wiggling-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Fingers_Wiggling-1.jpg)

## Disconnecting a LiPo Battery

Now disconnecting the LiPo battery is a different story. Earlier, we talked about some locking tabs on the side of the JST connector which can make it difficult to disconnect it from a female JST connector. Depending on the manufacturer, the material of the female JST connector can add an extra layer of difficulty if it is rigid. Below are a few options if you decide to disconnect the LiPo battery.

- Using Your Bare [Hands] Fingers!
- Needle Nose Pliers
- 3D Printed Battery Removal Tool
- Diagonal Cutters
- Shaving Off Locking Tabs

**Warning!** Make sure to not pull on the wires to disconnect. You may end up ripping the wires out from the connector.

#### 3D Printed JST Battery Removal Tool

You can use a specialized 3D printer tool dedicated to disconnecting LiPo batteries with a JST-PH connector. We highly recommend ordering the [SparkFun JST Battery Removal Tool](https://www.sparkfun.com/sparkfun-jst-battery-removal-tool.html) like the one below.

[![SparkFun JST Battery Removal Tool](https://cdn.sparkfun.com/r/600-600/assets/parts/2/9/5/3/0/27923-Sparkfun_JST_Battery_Removal_Tool-Feature.jpg)](https://www.sparkfun.com/sparkfun-jst-battery-removal-tool.html)

### [SparkFun JST Battery Removal Tool](https://www.sparkfun.com/sparkfun-jst-battery-removal-tool.html) 

[ TOL-27923 ]

The SparkFun JST battery removal tool is a tool to remove a standard 2-pin JST-PH connector (2mm pitch) from its housing! Eas...

[ [\$5.25] ]

**Note:** The JST battery removal tool is not intended to insert a JST female connector into the male connector.

Slide the tool between the JST female and male connector. You can slide the tool from the bottom or the top side as shown below.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![JST Battery Tool Inserted from Bottom](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/27923-SparkFun_JST_Battery_Removal_Tool_Insert_from_bottom.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/27923-SparkFun_JST_Battery_Removal_Tool_Insert_from_bottom.jpg)   [![JST Battery Tool Inserted from Top](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/27923-SparkFun_JST_Battery_Removal_Tool_Insert_from_top.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/27923-SparkFun_JST_Battery_Removal_Tool_Insert_from_top.jpg)
  *JST Battery Tool Inserted from Bottom*                                                                                                                                                                                                                                                                *JST Battery Tool Inserted from Top*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** This tool will work for most board designs with the [JST male connector](https://www.sparkfun.com/jst-right-angle-connector-smd-2-pin-black.html) populated on the edge of a board. Certain boards that have the JST male connector port facing toward the inside of the board may have components that will cause an obstruction when using the tool. Connectors that are populated close to the JST connector may also be another obstruction when using the tool.

In this case, we chose to slide the JST Battery Removal Tool from the bottom side. With your other hand, hold down the JST male connector. If necessary, place the wires through wire channel.

[![JST Battery Removal Tool Between JST Female and Male Connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/27923-SparkFun_JST_Battery_Removal_Tool_Pull_Connector_Away.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/27923-SparkFun_JST_Battery_Removal_Tool_Pull_Connector_Away.jpg)

Wiggle the JST female connector side to side while carefully pulling away the connector from the board.

[![LiPo Battery Disconnected](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/27923-SparkFun_JST_Battery_Removal_Tool_Battery_Disconnected.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/27923-SparkFun_JST_Battery_Removal_Tool_Battery_Disconnected.jpg)

**Note:** With the JST Battery Removal Tool, were also able to pull the connector directly away without needing to wiggle the connector side to side.

**Note:** You can also use the JST Battery Removal Tool to disconnect the battery packs used with micro:bits!\
\

[![JST Battery Removal Tool Used with micro:bit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/27923-SparkFun_JST_Battery_Removal_micro-bit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/27923-SparkFun_JST_Battery_Removal_micro-bit.jpg)

**Tip:** There\'s a small keyhole ring on the top of the JST Battery Removal Tool. You can find keychain rings at local hardware or craft stores. When attached, you can also use a small magnet to attach the tool to a metal shelf!\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/27923-SparkFun_JST_Battery_Removal_Tool_keychain_magnet_metal_shelf.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/27923-SparkFun_JST_Battery_Removal_Tool_keychain_magnet_metal_shelf.jpg)

**Note:** Feeling adventurous and have a 3D printer nearby? You can also [grab the 3D model from the GitHub repository](https://github.com/sparkfun/JST_Connector_Removal_Tool) and print the tool! You can also search online to find other designs similar to the JST battery removal tool as well. Keep in mind that you may need to modify the file and orient the print for your 3D printer in order to print properly.

#### Using Your Bare [Hands] Fingers!

You will need to carefully remove the connector out by pinching the sides of the JST female connector with your index finger and thumb. With your other hand, hold down the JST male connector.

[![Pinch JST Female Connector While Holding Down JST Male Connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Fingers_Wiggling-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Fingers_Wiggling-1.jpg)

Wiggle the JST female connector side to side while carefully pulling away the connector from the board.

[![Wiggle JST Female Connector Out](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Fingers_Wiggling-2_Arrows.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Fingers_Wiggling-2_Arrows.jpg)

The JST connector will slide out of the socket. Congratulations! You have successfully disconnected the LiPo battery from your board.

[![LiPo Battery Disconnected](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Fingers_Wiggling-3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Fingers_Wiggling-3.jpg)

#### Needle Nose Pliers

**Note:** Careful when using needle nose pliers! You will need to apply a certain amount of pressure to grip the connector. If you apply too much pressure, the connector may be damaged. Too little, and the needle nose pliers may slip and pinch the wires.

For those with long nails, you will want to use some needle nose pliers. We recommend using needle nose pliers with teeth like the one below:

[![Needle Nose Pliers](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/3/3/08793-03-L.jpg)](https://www.sparkfun.com/needle-nose-pliers.html)

### [Needle Nose Pliers](https://www.sparkfun.com/needle-nose-pliers.html) 

[ TOL-08793 ]

Mini Pliers. These are great little pliers! A must have for any hobbyist or electrical engineer. Crucial for inserting device...

[ [\$3.60] ]

Grip the sides of the JST female connector using the needle nose pliers in one hand. With your other hand, hold down the JST male connector.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Needle_Nose_Pliers_Wiggling-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Needle_Nose_Pliers_Wiggling-1.jpg)

Wiggle the JST female connector side to side while carefully pulling away the connector from the board. Using needle nose pliers will make it easier to remove but make sure to not angle the tool too much as the pins can be damaged if you angle the connector at an extreme angle.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Needle_Nose_Pliers_Wiggling-2_Arrows.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Needle_Nose_Pliers_Wiggling-2_Arrows.jpg)

The JST connector will slide out of the socket. Congratulations! You have successfully disconnected the LiPo battery from your board.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Needle_Nose_Pliers_Wiggling-3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Needle_Nose_Pliers_Wiggling-3.jpg)

**Note:** Are you skilled with a rotary tool? You can also make a custom plier like the ones explained in this [forum post JST XH connectors](https://www.eevblog.com/forum/projects/connector-puller-for-jst-xh-connectors/).

#### Diagonal Cutters

**Note:** Careful when using diagonal cutters! You will need to apply a certain amount of pressure to grip the connector. If you apply too much pressure, the connector may be damaged. Too little, and the diagonal cutters may slip and cut the wires.

Of course you could also use some diagonal cutters as well. Wire cutters have thin jaws that allow you to grip the head of the connector. However, there is a risk of cutting the wires if the diagonal cutters slip.

[![Diagonal Cutters](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/3/4/08794-03-L.jpg)](https://www.sparkfun.com/diagonal-cutters.html)

### [Diagonal Cutters](https://www.sparkfun.com/diagonal-cutters.html) 

[ TOL-08794 ]

Mini Diagonal Cutters. These are great little cutters! A must have for clipping leads and extra solder tails. 4\" long.

[ [\$3.75] ]

Depending on the design of the board, you may need to grip from the top or bottom of the JST connector. We\'ll show in the following images how to remove the connector from the bottom. Position the wire cutter between the between the JST female connector\'s flanges on the side and the JST male connector\'s socket. With your other hand, hold down the JST male connector. Don\'t go squeezing hard on the wire cutters either. They are simply there to grip the edge of the connector.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Diagonal_Cutters_Wiggling-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Diagonal_Cutters_Wiggling-1.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Diagonal_Cutters_Wiggling-2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Diagonal_Cutters_Wiggling-2.jpg)
  *Diagonal cutters holding JST connector from the top of a PCB*                                                                                                                                                                                                                            *Diagonal cutters holding JST connector from the bottom of a PCB*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** You can also use round nose pliers similar to the method used with diagonal cutters. However, they won\'t have the thin jaws like a diagonal cutter.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/PliersBattery_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/PliersBattery_1.jpg)

Use the edge of the PCB as a fulcrum point and lever out the connector. Pull the JST female connector away from the board by wiggling the connector sideways back and forth

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Diagonal_Cutters_Wiggling-3_Arrows.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Diagonal_Cutters_Wiggling-3_Arrows.jpg)

The JST connector will slide out of the socket. Congratulations! You have successfully disconnected the LiPo battery from your board.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Diagonal_Cutters_Wiggling-4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Remove_2-pin_JST-PH_Connector_LiPo_Battery_Diagonal_Cutters_Wiggling-4.jpg)

### Removing the Locking Tabs

Another option is to removing the locking tabs using a hobby knife. Cutting the tabs will make it easier to remove by hand. While it will not be as secure as it was before, we have found that it still holds pretty well in the JST male connector socket.

[![Hobby Knife](https://cdn.sparkfun.com/r/600-600/assets/parts/2/6/4/6/09200-Hobby_Knife-01.jpg)](https://www.sparkfun.com/hobby-knife.html)

### [Hobby Knife](https://www.sparkfun.com/hobby-knife.html) 

[ TOL-09200 ]

It\'s like an Xacto knife, only better. We use these extensively when working with PCBs. These small knives work well for cutt...

[ [\$3.75] ]

Pinch the sides of the JST female connector with your index finger and thumb. With the hobby knife, slice the locking tabs off each side of the JST female connector until it is flush with the top of the connector. There\'s not a lot of space to work with so make sure to not cut your fingers and angle the hobby knife away from your finger tips!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Hobby_Knife_JST-PH_Connector_Locking_Tabs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Hobby_Knife_JST-PH_Connector_Locking_Tabs.jpg)

The JST connector on the left shows the locking tabs intact. The JST connector on the right shows the locking tabs removed after. If the connector is still too tight, you can also cut down part of the fin (the slot between the two locking tabs) on the top of the connector as well.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/JST-PH_Connector_Comparison_Locking_Tabs_Removed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/JST-PH_Connector_Comparison_Locking_Tabs_Removed.jpg)

## How Much Power is Left?

You might be asking yourself, how much power is left in my LiPo battery? This is useful to ensure that you have enough charge to power your project or storing the LiPo battery.

### Multimeter

One way to check the voltage of a LiPo battery is [using a multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter/). You can set a multimeter to measure the voltage and connect to the terminals of the JST connector. Of course, you can also connect to the +VBATT and GND pins on a PCB if the battery is connected to a board as well. Just be careful not to accidentally create a short between the two terminals when measuring with the probes.

[![Measuring the voltage of a LiPo Battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/01_Multimeter_Tutorial-03.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/01_Multimeter_Tutorial-03.jpg)

*Using a Multimeter to test the voltage on a LiPo Battery.*

### LiPo Fuel Gauge

Another method is using a dedicated LiPo Fuel Gauge to output the voltage and charge remaining on a display. You are less likely to short the battery terminal pins using a LiPo Fuel Gauge (assuming that you are connecting a LiPo battery to the LiPo Fuel Gauge\'s JST connector or have it soldered to the PTH) compared to using a multimeter. Below are a few LiPo Fuel Gauges that you could use.

[](https://learn.sparkfun.com/tutorials/lipo-fuel-gauge-max1704x-hookup-guide)

### LiPo Fuel Gauge (MAX1704X) Hookup Guide 

February 23, 2023

Monitor your LiPo battery with the LiPo fuel gauge! In this tutorial, we will be using the MAX17043 and MAX17048 to monitor a single cell, LiPo battery over the Arduino Serial Monitor. We will also connect a display to view the output without the need to connect the microcontroller to a computer.

[](https://learn.sparkfun.com/tutorials/battery-babysitter-hookup-guide)

### Battery Babysitter Hookup Guide 

June 23, 2016

An introduction and getting started guide for the Battery Babysitter - a flexible LiPo battery charger and monitor.

## Reinforcing the Power Cables

One of the down sides to using these LiPo batteries is their fragile power connections between the wires and protection circuit. These type of batteries are manufactured for a permanent install in devices, and not being removed often as can sometimes happen with projects. For users prototyping or frequently removing the battery from boards without ON/OFF switches, it can be easy to accidentally pull or break the power wires from the terminals on the protection circuit built into the battery. Luckily for us, a little electrical tape goes a long way!

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/10689-02_elecrtical_tape.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/10689-02_elecrtical_tape.jpg)

The red and black wires on a LiPo will tend to wear out and break off if you swing the battery around too much. This fix is so simple, but we find that many people don\'t realize what a little stress-relief can do. You can provide strain relief to the wires by placing them to the side and securing with electrical tape - this will help with strain on the connection to the battery.

On your LiPo battery, fold the red and black wires to the side. With electrical tape, start in the middle of the battery and tape over the top. Use a little bit of tension on the tape as you go over the top of the battery. I use one and a half full wraps around the battery.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Strain_Relief_LiPo_Battery_Electrical_Tape-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Strain_Relief_LiPo_Battery_Electrical_Tape-1.jpg)

Cut the tape with wire cutters or knife to make a clean cut. Tearing the tape can leave ugly ripples in the electrical tape.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Strain_Relief_LiPo_Battery_Electrical_Tape_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Strain_Relief_LiPo_Battery_Electrical_Tape_2.jpg)

To make it even more secure, you can add another piece of tape across LiPo battery.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/Strain_Relief_LiPo_Battery_Electrical_Tape-3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/Strain_Relief_LiPo_Battery_Electrical_Tape-3.jpg)

This one or two wraps around the battery serve as a simple stress relief. All the mechanical stress is transferred to the tape instead of to the soldered terminals inside the top of the battery. Now when you use (or mis-use) the battery, you won\'t have to worry about breaking the red and black wires from the top of the battery!

## Labeling Batteries

We\'ve had a surprising collection of LiPos for various projects (they just seem to be replicating at this point!). A problem that came up was identifying the battery. What was I doing with this battery? What torture had I put it through? A Sharpie marker is perfect for marking your battery. A name such as \'heater\' or \'costume\' makes a world of difference. Dating the battery will let you know when you first used it. After a few years these batteries will start to lose some of their capacity. A date code helps to indicate that general health of a cell.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/4/5/BatteryCare-5_Labeling.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/BatteryCare-5_Labeling.jpg)

Remember, a protection circuit is usually built into yellow and silver pack that we sell. The protection circuit board is usually under the yellow Kapton tape where the wires are connected.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/13854-03_LiPo_Battery_Protection_Circuit_under_Yellow_Kapton_Tape.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/4/5/13854-03_LiPo_Battery_Protection_Circuit_under_Yellow_Kapton_Tape.jpg)

The protection circuit will prevent:

- over voltage (over charging)
- over current (the battery will turn off if there is a short in your system)
- under voltage (the battery will turn off before it runs down too low)

This protection circuit prevents most misuse of the battery and we have definitely misused some batteries. You can be re-assured the protection circuit will protect you and the battery.

## Battery Storage and Handling

[ ] **Warning:** LiPo batteries can explode or catch fire if mishandled or damaged. They can become unstable and dangerous if punctured or exposed to high temperatures.

While LiPo batteries are a great option for providing rechargeable power to your project, they do have some safety considerations. This section will cover a few tips for safe handling and use of LiPo batteries for your projects.

### Storage

- When not in use for long periods, it is recommended to discharge the LiPo battery to about 3.9V to 4.0V.

- Always store your batteries in an enclosure free of sharp objects. When installing a battery in your project, take care to keep it away from parts of your project that could pinch, poke, or strain the battery.

- Do not transport or store a LiPo battery with metal objects, such as hairpins, necklaces, or any other conductive object or material.

- Keep or store the battery in a cool and dry place/environment while installed in a project or in storage. If you are not planning to use your project for a long time, remove the battery and store it separately.

### Keep Away from Heat and Moisture

- Keep your LiPo battery away from environments that will damage it. Do not immerse a LiPo battery in liquids. Remove the battery from your project if it needs to be washed (such as e-textiles and wearable projects).

- Do not use or store the battery near any source of heat. To secure a battery to your project, velcro is a temporary option or sew into a pouch or place in a plastic enclosure. Never iron or hot glue directly on or around a LiPo battery.

### Inspect Battery Before Each Use

- Short circuits or damage to LiPo batteries may not always be noticeable - check the battery for puffiness, heat, or other changes. If the battery looks damaged, remove immediately.

- If the battery gives off an odor, generates heat, becomes discolored or deformed, or in any way appears abnormal during use, recharging, or storage, immediately remove it from your project or battery charger and stop using it. Make sure to dispose of your batteries properly - do not throw them in the trash! Contact your local e-waste disposal organization for details on how to discard batteries in your area.