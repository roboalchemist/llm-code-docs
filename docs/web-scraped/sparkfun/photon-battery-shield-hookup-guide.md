# Source: https://learn.sparkfun.com/tutorials/photon-battery-shield-hookup-guide

## Introduction

Free your [Photon](https://www.sparkfun.com/products/13774) from its USB cable by powering it through the [Photon Battery Shield](https://www.sparkfun.com/products/13626). The Battery Shield has everything your Photon needs to run off, charge, and monitor a LiPo battery.

[![Photon Battery Shield](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/angled.jpg)](https://www.sparkfun.com/products/13626)

The Shield features two unique IC\'s: an [MCP73831 charge controller](https://www.sparkfun.com/products/12711) and a [MAX17043 LiPo fuel gauge](https://www.sparkfun.com/products/10617). With them, you\'ll be able to charge your battery through USB and monitor its voltage and state-of-charge.

**Please Note:** All SparkFun shields for the Photon are also compatible with the [Core](https://store.particle.io/?product=spark-core) from Particle. The WKP, DAC and VBT pins on the Photon will be labeled A7, A6 and 3V3\*, respectively, on the Core, but will not alter the functionality of any of the Shields.

### Covered In This Tutorial

The purpose of this hookup guide is to familiarize you with the hardware and software of the Photon Battery Shield. It\'s split into the following sections:

- [Battery Shield Overview](https://learn.sparkfun.com/tutorials/photon-battery-shield-hookup-guide#battery-shield-overview) \-- A quick overview of the components and features of the Photon Battery Shield.
- [Using and Charging a LiPo Battery](https://learn.sparkfun.com/tutorials/photon-battery-shield-hookup-guide#using-and-charging-a-lipo-battery) \-- Some tips and tricks for running off, and charging a LiPo battery with the Shield.
- [Using the MAX17043 LiPo Fuel Gauge](https://learn.sparkfun.com/tutorials/photon-battery-shield-hookup-guide#using-the-max17043-lipo-fuel-gauge) \-- Example code \-- including a Particle library \-- demonstrating how to read the voltage and state-of-charge outputs, plus other features of the MAX17043 IC.

### Required Materials

The Photon Battery Shield equips your Photon with just about everything it should need to use a LiPo battery \-- it even includes headers! Of course you\'ll need the Battery Shield and a Photon.

[![SparkFun Photon Battery Shield](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/0/0/9/13626-01a.jpg)](https://www.sparkfun.com/sparkfun-photon-battery-shield.html)

### [SparkFun Photon Battery Shield](https://www.sparkfun.com/sparkfun-photon-battery-shield.html) 

[ DEV-13626 ]

The SparkFun Photon Battery Shield provides you with an easy way to power your Photon module with a Lithium Polymer (LiPo) ba...

**Retired**

[![Particle Photon (Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/2/8/13774-01.jpg)](https://www.sparkfun.com/products/13774)

### [Particle Photon (Headers)](https://www.sparkfun.com/products/13774) 

[ WRL-13774 ]

Particle\'s IoT (Internet of Things) hardware development board, the Photon, provides everything you need to build a connected...

**Retired**

The one thing the Battery Shield doesn\'t include is a battery. Our compatible LiPo batteries come in a variety of shapes and capacities \-- the larger the battery, the longer it will last. Any of the following will work:

[![Lithium Ion Battery - 6Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/3/13856-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-6ah.html)

### [Lithium Ion Battery - 6Ah](https://www.sparkfun.com/lithium-ion-battery-6ah.html) 

[ PRT-13856 ]

If you need some juice, this 6Ah Lithium Ion Battery is for you. These are very compact batteries based on Lithium Ion chemis...

[ [\$48.44] ]

[![Lithium Ion Battery - 850mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/7/00341-01b.jpg)](https://www.sparkfun.com/products/341)

### [Lithium Ion Battery - 850mAh](https://www.sparkfun.com/products/341) 

[ PRT-00341 ]

These are very slim, extremely light weight batteries based on the new Polymer Lithium Ion chemistry. This is the highest ene...

**Retired**

[![Lithium Ion Battery - 2000mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/2/Batt2AJST-01-L.jpg)](https://www.sparkfun.com/products/8483)

### [Lithium Ion Battery - 2000mAh](https://www.sparkfun.com/products/8483) 

[ PRT-08483 ]

These are very slim, extremely light weight batteries based on the new Polymer Lithium Ion chemistry. This is the highest ene...

**Retired**

[![Polymer Lithium Ion Battery - 400mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/5/5/5/7/10718-01d.jpg)](https://www.sparkfun.com/products/10718)

### [Polymer Lithium Ion Battery - 400mAh](https://www.sparkfun.com/products/10718) 

[ PRT-10718 ]

This is a very small, extremely light weight battery based on the new Polymer Lithium Ion chemistry. This is the highest ener...

**Retired**

If you want to use a battery of your own, just make sure it\'s a **single-cell** (3.7V nominal, \~4.2V max) lithium-polymer (LiPo) or lithium-ion (Li+). Optimally, choose one that is terminated with a [2-pin PH-series JST connector](https://www.sparkfun.com/products/9914), otherwise you may need to do some wire splicing.

If you don\'t already have one (or just want to stock up), you may also need a [Micro-B USB Cable](https://www.sparkfun.com/products/10215), which will come in handy when you need to recharge the battery. If you don\'t want to plug that cable into a computer, a [USB Wall Charger](https://www.sparkfun.com/products/12890) is useful to have on hand.

### Suggested Reading

Using the Photon Battery Shield doesn\'t require a whole lot of pre-existing knowledge. If you want to learn more about the foundational concepts in this tutorial, here are some guides we recommend:

- [How to Power a Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project) \-- Hopefully you\'ve already figured this out, since you\'re reading a Battery Shield tutorial. This tutorial does have an enlightening section on [battery power](https://learn.sparkfun.com/tutorials/how-to-power-a-project#remotemobile-power).
- [Battery Technologies](https://learn.sparkfun.com/tutorials/battery-technologies) \-- Specifically, check out the section on [Lithium Polymer batteries](https://learn.sparkfun.com/tutorials/battery-technologies#lithium-polymer).
- [How Lithium Polymer Batteries are Made](https://learn.sparkfun.com/tutorials/how-lithium-polymer-batteries-are-made) \-- Learn everything you always wanted to know about what goes on behind the scenes at a battery factory.
- [I^2^C Communication](https://learn.sparkfun.com/tutorials/i2c) \-- I^2^C is a popular low-level, two-wire communication standard. This is what we\'ll use to communicate with the MAX17043 fuel gauge IC.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/how-lithium-polymer-batteries-are-made)

### How Lithium Polymer Batteries are Made 

We got the opportunity to tour the Great Power Battery factory. Checkout how LiPos are made!

## Battery Shield Overview

Let\'s do a quick rundown of the Photon Battery Shield\'s hardware features. Here are some highlights of the board\'s main components:

[![Top of shield annotated](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/9/2/top-annotated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/top-annotated.jpg)

- **LiPo Connector (PH-Series JST)** \-- The battery goes here. This connector is polarized, so it\'ll only plug in the right way.
- **Photon Socket** \-- Each Photon comes pre-soldered with male headers, so all of our shields come pre-populated with female connectors on their top-side.
- **Photon Pin Breakouts** \-- Need more access to the Photon\'s I/O? These pin break-outs have that covered. These break outs are in the same place on each of our [Photon Shields](https://www.sparkfun.com/categories/278) \-- should you need to interface them together that way.
- **Photon Polarity Indicator** \-- Nothing\'s going to work if your Photon isn\'t plugged in correctly. These angled edges should match up to those on the Photon\'s PCB.
- **Charge LED Indicator** \-- This red LED will light up whenever the LiPo battery is being charged.

Flipping the Shield over reveals a few, less commonly-used features of the board:

[![Bottom of shield annotated](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/bottom-annotated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/bottom-annotated.jpg)

- **\"Stackable\" Male Pins** \-- Whether you want to plug the battery shield into more Photon shields, or use it in a breadboard, these male pins should do the job. If you don\'t need this feature, the pins can all be quickly beheaded by some [flush cutters](https://www.sparkfun.com/products/11952).
- **SMD Barrel Jack footprint** \-- This footprint allows you to add an [SMD Barrel Jack](https://www.sparkfun.com/products/12748) to the Battery Shield\'s underside. This\'ll allow you to charge the battery with a [5V Wall Adapter](https://www.sparkfun.com/products/12889), or even a [Small Solar Panel](https://www.sparkfun.com/products/7845). Just make sure your power source isn\'t higher than **5.5V**.
- **I^2^C Pull-up Resistor Enable/Disable** \-- The Photon Battery Shield includes a pair of 10kΩ pull-up resistors on the SDA and SCL lines (D0 and D1). If you\'ve got more I^2^C devices to connect, you may need to disable those. These jumpers are closed by default, but can be opened with a couple slices of a [hobby knife](https://www.sparkfun.com/products/9200).
- **Alert Interrupt Jumper** \-- The MAX17043 features a programmable interrupt output, which can fire whenever your battery gets below a set percentage of charge. This pin can be connected to the Photon\'s **D6 pin** by adding a blob of solder between these two pads. Note that this jumper is open by default, as other shields make use of D6.

## Using and Charging a LiPo Battery

Before plugging your battery in, grab your Photon, and plug it into the battery shield. Make sure you **line up the Photon\'s angled edges** with the matching white silkscreen on the shield. The Photon\'s USB connector should be pointing out the same direction as the black JST connector.

Next, grab your LiPo battery and mate its white JST connector with the black one on the shield. These connectors are polarized, so you can only plug it in the *right* way.

[![Photon running off a battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/9/2/battery-photon.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/battery-photon.jpg)

*Running your Photon off a LiPo is as simple as plugging in a battery and the Photon.*

If the battery had any charge, your Photon should turn on, and its RGB LED should begin being colorful. If it was already commissioned, your Photon should connect to your WiFi network. You can even load up the [Particle Build IDE](https://build.particle.io/build) and truly start loading code over-the-air.

### Charging the Battery through USB

Eventually your LiPo\'s power capacity will be drained, and it\'ll be time to charge it back up. To avoid any extra USB connectors, the Photon Battery Shield was designed to use the **Photon\'s USB connector** as a charge-source.

With the LiPo and Photon still connected to the Battery Shield, simply plug a Micro-B USB cable into your Photon (the other end of the USB cable can be plugged into a computer or USB wall adapter).

[![Charging a battery through USB](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/9/2/battery-photon-usb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/battery-photon-usb.jpg)

*To charge the LiPo, just plug a USB cable into the Photon\'s USB port.*

Once USB is attached, the red charge LED indicator should illuminate \-- it\'ll remain lit up until the battery is fully charged.

### (Optional) Charging the Battery through Barrel Jack

The Battery Shield provides additional options for charging your LiPo in an unpopulated barrel jack footprint. If you need to charge the LiPo sans-Photon, this may be the best option for you.

To add this feature, you\'ll need our [Surface-Mount Barrel Jack](https://www.sparkfun.com/products/12748), and some [soldering tools](https://www.sparkfun.com/categories/49). If you\'re a novice solderer, don\'t be scared off by the \"SMD\" soldering \-- these joints are about as easy as it gets. Check out or [soldering tutorial](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) for some guidance.

The barrel jack\'s input should face out towards the edge of the board. Make sure you solder all four pads:

[![SMD barrel jack soldered on bottom](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/9/2/battery-barrel-jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/battery-barrel-jack.jpg)

To charge a LiPo through this jack, you\'ll need a **5V power source** \-- our [5V Wall Adapter](https://www.sparkfun.com/products/12889) should do the trick. Or, if you really want to avoid wires, you can use our [small, 0.45W solar panel](https://www.sparkfun.com/products/7845), which will source up to 5V when it\'s nice and sunny.

[![Charging with barrel jack solar panel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/9/2/battery-barrel-solar.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/battery-barrel-solar.jpg)

------------------------------------------------------------------------

If you don\'t want to solder the barrel jack on, but still have a 5V power source available, you can supply that voltage to the \"VIN\" and \"GND\" pins on the shield\'s header. This is a more advanced charge technique, and only recommended for more experienced users.

## Using the MAX17043 LiPo Fuel Gauge

One of the most unique features of the Photon Battery Shield is the integrated MAX17043 LiPo fuel gauge. The MAX17043 sits between the battery and your Photon \-- it uses a calibrated ADC to measure the battery voltage. Comparing that measured voltage against their \"ModelGauge\" algorithm, the IC can produce a state-of-charge (SOC) estimate, to give you an idea of what percentage remains of the battery charge.

### Loading the SparkFunMAX17043 Library

The MAX17043 communicates over [I^2^C](https://learn.sparkfun.com/tutorials/i2c), so coding an interface between the Photon and the fuel gauge can be a little tricky. Luckily, we\'ve done the hard work for you! We\'ve written a Particle library for the MAX17043. You can load it up in the Particle IDE by going to the \"Libraries\" tab, and searching for **SparkFunMAX17043**.

[![MAX17403_Simple example in Particle Build](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/9/2/particle-build-max17043-2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/particle-build-max17043-2.png)

*Search the \"Libraries\" tab for \"SparkFunMAX17043\" to find the Fuel Gauge library.*

If you\'re using the desktop version of the IDE, Particle Dev, and still want to use the library, you can grab the latest version from our [GitHub repository](https://github.com/sparkfun/SparkFun_MAX17043_Particle_Library).

### Running the MAX17043_Simple Example

After finding the library, navigate to \"MAX17043_Simple.cpp\" and click **Use This Example** \-- the Build IDE will create a clone of this sketch in your \"Code\" tab.

You shouldn\'t have to change anything, just make sure your Photon is selected in the \"Devices\" tab, and click \"Flash\".

Once your Photon is running the code, there are two ways to view its data. One is to open a serial terminal (see our [Serial Terminal Basics tutorial](https://learn.sparkfun.com/tutorials/terminal-basics) if you need help with this). Find your Photon\'s serial port number (\"COM#\" on Windows \"/dev/tty.usbmodemXXXX\" on Mac) and set the baud rate to 9600. The battery\'s voltage, state-of-charge, and alert status will stream by.

[![Serial terminal output](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/serial-monitor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/serial-monitor.png)

*Using [TeraTerm](https://learn.sparkfun.com/tutorials/terminal-basics/tera-term-windows) to view the Photon\'s Serial.print debug output.*

Since USB is plugged in, the voltage and percentage should steadily increase as the battery charges.

Alternatively, if you want to monitor the battery *discharge*, you can use the Photon\'s Internet-connectivity to view the battery voltage and charge status. First, though, you\'ll need to identify your Photon\'s **device ID** as well as your account\'s **access token**. The device ID can be found in Particle Build by clicking the \'\>\' next to your device name.

[![Particle Device ID](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/particle-device-id.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/particle-device-id.png)

*Find your Device ID under the \"Devices\" tab, by clicking the carrot next to your Photon.*

Your access token can be found under the \"Settings\" tab.

[![Access Token](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/particle-access-token-2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/particle-access-token-2.png)

*Find your access token under the \"Settings\" tab.*

Armed with those long strings of hex characters, open a new browser tab and navigate to:

    https://api.particle.io/v1/devices/DEVICE_ID/voltage?access_token=ACCESS_TOKEN

Make sure to sub in the proper values for `DEVICE_ID` and `ACCESS_TOKEN`. If everything was entered correctly, you should see something like this:

[![Spark Variable JSON string](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/9/2/spark-variable-screenshot.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/spark-variable-screenshot.png)

*The Spark variable responds with a JSON string including a \"result\" key and value.*

Among the data in that JSON response is a \"result\" key, which shows the current voltage reading. You can also view the state-of-charge, and alert status by navigating to:

    https://api.particle.io/v1/devices/DEVICE_ID/soc?access_token=ACCESS_TOKEN

and

    https://api.particle.io/v1/devices/DEVICE_ID/alert?access_token=ACCESS_TOKEN

Yay [Spark Variables](http://docs.particle.io/photon/firmware/#spark-variable)!

### Using the SparkFunMAX17043 Library

The SparkFunMAX17043 library is simple. There\'s some initialization required. Make sure to include the library, and in your `setup()` call `lipo.begin()`.

    language:c
    #include "SparkFunMAX17043/SparkFunMAX17043.h" // Include the SparkFun MAX17043 library

    void setup()
    

Calling `lipo.quickStart()` will re-calibrate the MAX17043\'s ADC, and usually results in more accurate readings.

If you\'re using the library in Particle Build, make sure you go to the SPARKFUNMAX17043 library in the \"Libraries\" tab, select **INCLUDE IN APP**, and add it to your desired code file.

[![Include library in app](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/particle-include-in-app.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/2/particle-include-in-app.png)

*Any sketch using the SparkFunMAX17043 library needs to have it \"included\" first.*

#### Reading Voltage and SoC

Two functions are used to read the MAX17043\'s voltage and state-of-charge values:

    language:c
    // lipo.getVoltage() returns a voltage value (e.g. 3.93)
    voltage = lipo.getVoltage();
    // lipo.getSOC() returns the estimated state of charge (e.g. 79%)
    soc = lipo.getSOC();

Both functions return a `float` variable. `lipo.getVoltage()` should usually be between 0.0 and about 4.2. `lipo.getSOC()` should be somewhere between 0.0 and 100.0.

#### Using the Alert Interrupt

One of the MAX17043\'s nifty features is a programmable alert interrupt. You can tell it to trigger a flag whenever the state-of-charge falls below a certain threshold.

To set up the alert, use `lipo.setThreshold([percentage])`. For example:

    language:c
    lipo.setThreshold(15); // Set Alert threshold to 15%

\...will set the alert threshold to 15%.

The alert status can be read in both software and hardware. To get the alert status in software, call `lipo.getAlert()`. This function will return `0` if the alert is not triggered, and `1` if it is.

As mentioned in the Battery Shield Overview section, a jumper on the bottom of the board can optionally be closed to connect the MAX17043\'s alert pin to Photon pin D6. This alert is **active-low** \-- meaning it\'ll be HIGH when it\'s not triggered and LOW when the SoC has fallen below threshold.

Once an alert has been triggered, you\'ll need to clear it before it can fire again. That\'s what `lipo.clearAlert()` will do for you. Even if the SoC rises above the threshold, you\'ll still need to manually clear the alert.