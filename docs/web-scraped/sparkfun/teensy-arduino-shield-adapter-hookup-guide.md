# Source: https://learn.sparkfun.com/tutorials/teensy-arduino-shield-adapter-hookup-guide

## Introduction

**Note:** This shield has been updated to v1.1. The only difference in the revision is a single jumper to isolate the V~cc~ power from 5V. Just in case users accidentally connect 5V to the ISP pins (the Teensy is a 3.3V board).

The [Teensy Arduino Shield Adapter](https://www.sparkfun.com/products/13288) is a useful tool for upgrading existing projects to a more powerful controller. If you have an Arduino shield you\'d love to use, but prefer working with the Teensy, then this product is just what you need!

[![Teensy Adapter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/FinalAssembly.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/FinalAssembly.jpg)

### Required Materials

To follow along with this tutorial, we recommend you have access to the following materials.

As this adapter was originally designed for the Teensy 3.1, we recommend using either the Teensy 3.1 or 3.2. However, th footprint is compatible with the Teensy LC (*not all of the features available on the adapter are compatible with the LC\... see **Teensy Compatibility** section*).

[![Teensy 3.1](https://cdn.sparkfun.com/r/140-140/assets/parts/9/3/3/8/12646-01a.jpg)](https://www.sparkfun.com/products/12646)

### [Teensy 3.1](https://www.sparkfun.com/products/12646) 

[ DEV-12646 ]

The Teensy 3.1 is a breadboard-friendly development board with loads of features in a, well, teensy package.

**Retired**

[![Teensy LC](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/7/1/13305-01.jpg)](https://www.sparkfun.com/products/13305)

### [Teensy LC](https://www.sparkfun.com/products/13305) 

[ DEV-13305 ]

The Teensy LC is a 32 bit microcontroller board that provides you with an uncomplicated option to get started with Teensy wit...

**Retired**

[![Teensy 3.2](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/4/9/13736-01.jpg)](https://www.sparkfun.com/products/13736)

### [Teensy 3.2](https://www.sparkfun.com/products/13736) 

[ DEV-13736 ]

The Teensy 3.2 is a breadboard-friendly development board with loads of features in a, well, teensy package.

**Retired**

In addition to the Teensy, you will need a micro-[USB cable](https://www.sparkfun.com/categories/71) (examples below):

[![USB Micro-B Cable - 6\"](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/4/3/0/13244-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6.html)

### [USB Micro-B Cable - 6\"](https://www.sparkfun.com/usb-micro-b-cable-6.html) 

[ CAB-13244 ]

This is a USB 2.0 type A to Micro-B 5-pin black cable. You know, the mini-B connector that usually comes with cell phones, Ca...

[ [\$2.50] ]

[![Reversible USB A to Reversible Micro-B Cable - 0.8m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/7/15428-Reversible_USB_A_to_Reversible_Micro-B_Cable_-_0.8m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-reversible-micro-b-cable-0-8m.html)

### [Reversible USB A to Reversible Micro-B Cable - 0.8m](https://www.sparkfun.com/reversible-usb-a-to-reversible-micro-b-cable-0-8m.html) 

[ CAB-15428 ]

These 0.8m cables have minor, yet genius modifications that allow both ends to be plugged into their ports regardless of thei...

[ [\$5.50] ]

[![Reversible USB A to Reversible Micro-B Cable - 0.3m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/8/15429-Reversible_USB_A_to_Reversible_Micro-B_Cable_-_0.3m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-reversible-micro-b-cable-0-3m.html)

### [Reversible USB A to Reversible Micro-B Cable - 0.3m](https://www.sparkfun.com/reversible-usb-a-to-reversible-micro-b-cable-0-3m.html) 

[ CAB-15429 ]

These 0.3m cables have minor, yet genius modifications that allow both ends to be plugged into their ports regardless of thei...

[ [\$4.50] ]

[![SparkFun Rugged microB Cable - 1m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/1/14742-USB_micro-B_Braided_Cable_-_3_Foot-01.jpg)](https://www.sparkfun.com/products/14742)

### [SparkFun Rugged microB Cable - 1m](https://www.sparkfun.com/products/14742) 

[ CAB-14742 ]

Is your laptop covered in stickers that hide the dents? Do you put your equipment through its paces? The SparkFun 1 meter Rug...

**Retired**

To assemble the adapter shield, you will need some [soldering equipment](https://www.sparkfun.com/categories/49) (examples below):

[![Solder - 1/4lb Spool (0.032\") Special Blend](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/9/3/10243-Solder_-_1_4lb_Spool__0.032___Special_Blend-01.jpg)](https://www.sparkfun.com/solder-1-4lb-spool-0-032-special-blend.html)

### [Solder - 1/4lb Spool (0.032\") Special Blend](https://www.sparkfun.com/solder-1-4lb-spool-0-032-special-blend.html) 

[ TOL-10243 ]

We don\'t want to hype this solder TOO much, but this could possibly be the best solder in the world. There, we\'ve said it. Th...

[ [\$28.50] ]

[![SparkFun Safety Glasses](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/0/8/11046-SparkFun_Safety_Glasses-02.jpg)](https://www.sparkfun.com/sparkfun-safety-glasses.html)

### [SparkFun Safety Glasses](https://www.sparkfun.com/sparkfun-safety-glasses.html) 

[ SWG-11046 ]

With these SparkFun Safety Glasses you\'ll have a pair of lightweight, economical, and stylish lenses to protect your precious...

[ [\$5.10] ]

[![Electronic Snippers](https://cdn.sparkfun.com/r/140-140/assets/parts/4/9/3/5/10447-Electronic_Snippers-04.jpg)](https://www.sparkfun.com/products/10447)

### [Electronic Snippers](https://www.sparkfun.com/products/10447) 

[ TOL-10447 ]

While our small diagonal cutters are great for hobby use, sometimes you need something with a little more bite. These electro...

**Retired**

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

[![Solder Wick #2 25ft. - TechSpray](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/9/4/08775-01-L.jpg)](https://www.sparkfun.com/solder-wick-2-25ft-techspray.html)

### [Solder Wick #2 25ft. - TechSpray](https://www.sparkfun.com/solder-wick-2-25ft-techspray.html) 

[ TOL-08775 ]

Solder wick, coffee, and paper towels keep SparkFun running. You can steal someone\'s diagonal cutters for a minute, but you\'d...

**Retired**

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/8/3/14681-SparkFun_Beginner_Tool_Kit.jpg)](https://www.sparkfun.com/products/14681)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/products/14681) 

[ TOL-14681 ]

This assortment of tools is great for those of you who need a solid set of tools to start your workbench on the right foot!

**Retired**

### Suggested Reading

If you aren\'t familiar with the following concepts, please review them before beginning to work with the Teensy Arduino Shield Adapter.

- [Getting Started with the Teensy](https://learn.sparkfun.com/tutorials/getting-started-with-the-teensy)
- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [How to Power Your Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project)
- [Battery Technologies](https://learn.sparkfun.com/tutorials/battery-technologies)
- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering)
- [Working with Wire](https://learn.sparkfun.com/tutorials/working-with-wire)
- [Arduino Shields](https://learn.sparkfun.com/tutorials/arduino-shields-v2)

## Hardware Overview

There are several features on the Teensy Adapter Shield to be aware of. While this shield provides basic Arduino compatibility with a standard shield, there\'s a few other fun features to check out.

**Note:** This shield has been updated to v1.1. The only difference in the revision is a single jumper to isolate the V~cc~ power from 5V. Just in case users accidentally connect 5V to the ISP pins (the Teensy is a 3.3V board).

The jumper pad and markings are shown below:

### [Version 1.0](https://www.sparkfun.com/products/13288)

![no jumper pad on v10 board](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/v10_jumper_pad.jpg)\
*No jumper pad.*\
\
![designated marking for v10 board](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/v10_marking.jpg)\
*Version 1.0 marking.*

### [Version 1.1](https://www.sparkfun.com/products/15716)

![jumper pad on v11 board](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/v11_jumper_pad.jpg)\
*With jumper pad.*\
\
![designated marking for v11 board](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/v11_marking.jpg)\
*Version 1.1 marking.*

### Teensy Compatibility

The adapter design interfaces with all features of the [Teensy 3.1](https://www.sparkfun.com/products/12646) and [Teensy 3.2](https://www.sparkfun.com/products/13736), but the adapter fits the [Teensy LC](https://www.sparkfun.com/products/13305) footprint as well. Not all of the features available on the adapter are compatible with the LC due to the microcontroller\'s limitations. Please check the datasheets to ensure functionality for your project to determine the best Teensy for your use case.

This adapter is not compatible with the [Teensy 4.0](https://www.sparkfun.com/products/15583) due to the differences in the pin layout.

### Real Time Clock Battery

[![RTC Battery Clip](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/RTCconnector.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/RTCconnector.JPG)

The battery holder included for the shield allows the users to install this into a project and run the RTC (Real Time Clock) on the Teensy as a time keeping option. The included coin cell battery outputs 3V and will power the RTC in case of system power loss to maintain accurate time.

**This feature does not work with the Teensy LC.**

### JST Power Connector

[![JST Connector](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/jst.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/jst.JPG)

This connector breaks out the 3.3V power line from the Teensy. You can power external devices off of this using a [JST jumper wire](https://www.sparkfun.com/products/9914), or you can solder wires directly to this connection instead.

This header can also be used as a power input to both the Teensy and the Arduino footprint and is **not** regulated down. The voltage supplied on the connector must be 3.3V.

**You must cut the VIN/VUSB jumper on the bottom of the Teensy if you intend to power the Teensy via this connection and use USB for communication/programming.**

### Barrel Jack

[![Barrel Jack](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/barreljack.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/barreljack.JPG)

The barrel jack allows the user to power the Teensy and Shield combo using a wall adapter or any power supply with a male barrel jack. This voltage can be anywhere from 4-12V, and is regulated to 5V for powering the Teensy. This power supply connects directly to VRAW on the Arduino shield footprint and is not regulated down. Please read the datasheet for any shields you intend to connect to via the adapter shield.

**You must cut the VIN/VUSB jumper on the bottom of the Teensy if you intend to power the Teensy via this connection and use USB for communication/programming.**

### I^2^C Jumpers

[![I2C Jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/i2cjumpers.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/i2cjumpers.JPG)

The two solder jumpers included on the adapter allow the user to configure the I^2^C lines on the board. The adapter ships with the jumpers closed by default, connecting the `SDA` and `SCL` pins of the Teensy to pins `A4` and `A5` on the Arduino footprint respectively. If you have an Arduino Leonardo-compatible shield, you can swap this jumper to isolate the SDA and SCL lines on the same-named pins, and access `A6` and `A7` of the Teensy on `A4` and `A5` of the Arduino footprint. `A4` and `A5` of the Teensy will still connect to the Arduino footprint `SDA` and `SCL`.

### ICSP Header

[![ICSP Header](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/ICSPHeader.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/ICSPHeader.JPG)

The ICSP header breaks out the SPI pins for Leonardo-compatible shields. You can also use this header to reprogram the Teensy if you have an AVR programmer.

**Warning!** If you are using a 5V shield that connects over the ICSP/ISP pins, **do not** connect ISP pin 2 on the adapter to your shield. This will short 3.3V and 5V together and could damage your Teensy.

#### Power Isolation Jumper

[![Power Isolation Jumper](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/v11_jumper_pad.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/v11_jumper_pad.jpg)

If you are using the updated v1.1 adapter, there is a power isolation jumper marked `J4`, next to the ICSP/ISP pins. This jumper by default is open and is used to isolate V~cc~ of the adapter board from the ISP pins. This is used to prevent users from accidentally frying their boards when providing 5V power instead of the 3.3V that the Teensy is rated for.

### Additional Analog Pins

[![Analog Headers](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/AnalogHeaders.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/AnalogHeaders.JPG)

Just because you\'re using the Teensy with an Arduino shield doesn\'t mean you want to lose the extra features of the Teensy! We\'ve broken out additional analog pins 8-11 from the Teensy to a 6-pin header, along with `AREF` and `GND`. These pins don\'t interact with the Arduino shields at all, and are simply a bonus for external sensors or inputs if desired.

### DAC Pin Header

[![DAC Header](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/DACheader.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/DACheader.JPG)

One of the other great features of the Teensy is the onboard Digital-to-Analog converter. We\'ve broken this pin out to the board\'s edge, along with the `PROG` pin, and two corresponding `GND` pins.

On the [Teensy LC](https://www.sparkfun.com/products/13305), pin A12 is used instead of A14 (*as marked on shield*).

## Hardware Assembly

So you\'ve got a bag of parts and are ready to get your Teensy interfaced with your Arduino shields. It\'s time to bust out that soldering iron!

We\'re going to solder the adapter together in order of smallest profile to largest. This will help make it easier to reach all the soldering points with the iron, as well as make it easier to line all the items up properly.

**Battery Holder**

[![Battery Holder](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/BatteryClip_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/BatteryClip_1.jpg)

First, insert the [battery holder](https://www.sparkfun.com/products/7948) and ensure it is sitting flush on the board. Flip the adapter over, and solder the connectors. Keep in mind that the battery clip is all metal and will conduct heat, so don\'t burn yourself!

Because the battery clip will endure a lot of strain on battery insertion or removal, you want to make sure you fully connect the pins to the board. Make sure your solder points look nice and filled in, like this:

[![Battery Connectors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/BatteryClipBottom.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/BatteryClipBottom.jpg)

**Capacitor**

The next component to solder is the [capacitor](https://www.sparkfun.com/products/523). The cap is [polarized](https://learn.sparkfun.com/tutorials/polarity), so make sure you insert it correctly into the board. The negative side of the cap should be inserted closest to the barrel jack footprint.

Once you insert the cap, bend the legs out a bit to hold the capacitor flush against the board while you solder it.

[![Capacitor Sitting Flush](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/CapacitorFlush.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/CapacitorFlush.jpg)

Once you\'ve soldered the capacitor legs, clip any excess leg.

[![Clipped capacitor legs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/CapacitorSoldered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/CapacitorSoldered.jpg)

**JST Connector**

Next, insert the [JST connector](https://www.sparkfun.com/products/9749). This part tends to need a bit of a push to insert fully into the board, so make sure you get it sitting flush before soldering. Make sure the opening on the connector sits along the board edge and isn\'t inserted backwards.

[![JST Connector Inserted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/JSTinserted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/JSTinserted.jpg)

**Voltage Regulator**

The [voltage regulator](https://www.sparkfun.com/products/107) does tend to be a bear to insert properly, so take your time with this step. First insert the regulator legs into the board. Make sure the regulator is inserted in the correct orientation, with the metal tab towards the ICSP header on the board and the plastic body casing closest to the JST connector.

[![Voltage Regulator Orientation](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/VRegInsertion.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/VRegInsertion.jpg)

*Proper orientation of voltage regulator from the side view.*

Once you\'ve verified the regulator is oriented correctly, but before soldering, bend the regulator down towards the PCB. The mounting hole on the regulator should match up with the mounting hole on the PCB.

Solder the regulator legs and clip any excess. This part does regulate the project voltage, so make sure to get a good solder connection on all the pins and ensure there are no jumpers or clippings that could short the board.

[![Regulator Leg clipped](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/RegulatorLegClip.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/RegulatorLegClip.jpg)

**Female Headers for Teensy**

At this point, you will need to determine how you want your adapter shield to interface with your Teensy and your Arduino shields. The steps shown are our recommended method of interfacing everything, but you can customize this. Please check our tutorial on [Getting Started with the Teensy](https://learn.sparkfun.com/tutorials/getting-started-with-the-teensy) to see other possible configurations.

Take the [female headers](https://www.sparkfun.com/products/115) from your kit, and cut them down into individual strips to fit in the Teensy footprint. Plug in the headers, and verify that they line up well. You may also need to use one of the [6-pin female headers](https://www.sparkfun.com/products/11894) on the short edge of the Teensy footprint.

[![Gap in Headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/ProperlyAlignedHeaders.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/ProperlyAlignedHeaders.jpg)

If you have gaps between the headers like shown above, you may need to file down the edges of the connectors to get everything to fit compactly. Start soldering the header rows one at a time. To help keep them straight as you solder, we recommend tacking the first and last solder points first.

[![Tacked Headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/BottomShieldTeensyHeadersTacked.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/BottomShieldTeensyHeadersTacked.jpg)

*Notice the first and last headers are tacked down.*

This allows you to easily fix any poorly inserted or angled headers that may occur.

[![Misaligned headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/MisalignedHeaders.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/MisalignedHeaders.jpg)

*These headers will never do!*

If you have decided to solder all of the Teensy pins, you will also need to solder in the inner row of headers on the shield.

[![Second row headers to solder](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/ModifiedHeadersTeensy.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/ModifiedHeadersTeensy.jpg)

**Shield Headers**

Next, solder on the [10-pin](https://www.sparkfun.com/products/11896), [8-pin](https://www.sparkfun.com/products/11895), and [6-pin headers](https://www.sparkfun.com/products/11894) onto the Adapter board. To make sure you line these headers up properly, we recommend using a pre-soldered shield as a soldering jig to hold the adapter headers in place.

[![Stacked headers for soldering](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/LineUpHeaders.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/LineUpHeaders.jpg)

*Pre-soldered shield used as a soldering jig to keep the headers lined up.*

Keep in mind that you may need to add on the [stackable headers](https://www.sparkfun.com/products/11417) from your kit onto your board in order to provide enough clearance between the Teensy and the shield you use.

**Barrel Jack**

The final part to solder is the [barrel jack](https://www.sparkfun.com/products/119). Notice that when you insert it, the through holes are much larger than the standard headers.

[![Barrel jack pins bare](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/BarrelJackInserted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/BarrelJackInserted.jpg)

Because of the large plated through holes, you will need more solder and heat to properly connect these and fill them in (just like on that battery clip!). Be patient, and take it slow, to ensure you don\'t burn the PCB or any traces.

That\'s it! Your adapter should now be soldered and ready to go.

[![Teensy Adapter Completed Top](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/CompletedAdapterTop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/CompletedAdapterTop.jpg)

*All pieces inserted and soldered!*

[![Teensy Adapter Soldered Bottom](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/CompletedAdapterBottom.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/CompletedAdapterBottom.jpg)

*Teensy Adapter successfully soldered!*

**Teensy Headers**

Now that your adapter is completed, you can use this as a soldering jig to connect the [male headers](https://www.sparkfun.com/products/116) to your Teensy. Break the strip into smaller parts, and insert them into the pre-soldered headers on the adapter. Plug the Teensy on top, and solder away!

[![Teensy Headers stacked](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/Teensy_Arduino_Shield_Adapter_Tutorial-20.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/Teensy_Arduino_Shield_Adapter_Tutorial-20.jpg)

**Crystal**

**Note:** This step is optional and only necessary if you intend to use the RTC feature on the Teensy 3.1 or 3.2.

If you intend to use the RTC on the Teensy 3.1 or Teensy 3.2, you will need to solder the [crystal](https://www.sparkfun.com/products/540) onto the Teensy. You can solder it via the bottom or the top, but keep in mind you should insert it where it is least likely to get knocked or short the body of the crystal onto other components.

[![Crystal on Teensy Bottom](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/Crystal_bottom.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/Crystal_bottom.jpg)

*Double check that the crystal won\'t short on any pins before soldering!*

### Plug it all in

Once everything is soldered properly, it\'s time to put your boards together. If you did not solder the Teensy directly to the adapter, plug the Teensy into the adapter, and insert whichever shield you\'ve chosen to connect.

Plug in your Teensy via USB, upload your code, and you\'re good to go!

[![Teensy System](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/4/TeensyAdapterStacked.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/4/TeensyAdapterStacked.jpg)

*Final Adapter assembly with the [Electric Imp Shield](https://www.sparkfun.com/products/12887) stacked on top.*

**Remember!** If you intend to use an external power supply, you must cut the jumper on the bottom of the Teensy to prevent shorting VUSB and VIN.

Don\'t forget to plug in your [coin-cell battery](https://www.sparkfun.com/products/337), if you intend to use the RTC. This **does not** work with the Teensy LC.

## Programming

Because this board is simply an adapter, there is no special programming required to start working with the adapter. You will, however, need to program the Teensy for any Arduino shield with which you\'d like to work.

When programming your Teensy, remember to select the proper board from the Arduino IDE drop down, and select the proper serial port and baud rate.

Please review our tutorial on [Getting Started with the Teensy](https://learn.sparkfun.com/tutorials/getting-started-with-the-teensy), for more information on programming the Teensy in either the Arduino IDE or in a C compiler.

Don\'t forget to verify and update your pin definitions in your shield code if you intend on using `A6` or `A7` in place of `SDA` or `SCL`.