# Source: https://learn.sparkfun.com/tutorials/connector-basics

## Introduction

Connectors are used to join subsections of circuits together. Usually, a connector is used where it may be desirable to disconnect the subsections at some future time: power inputs, peripheral connections, or boards which may need to be replaced.

### Covered in This Tutorial

In this tutorial we will go over:

- Basic connector terminology
- Categorize connectors into distinguishable categories
- Talk about the differences between connectors within those categories.
- Show how to identify polarized connectors
- Talk about which connectors are best suited for certain applications

### Suggested Reading

You may find these concepts useful before starting on this tutorial:

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/polarity)

### Polarity 

An introduction to polarity in electronic components. Discover what polarity is, which parts have it, and how to identify it.

## Connector Terminology

Before we get started discussing some commonly used connectors, let\'s explore the terminology used to describe connectors.

### Gender

**Gender** - The gender of a connector refers to whether it plugs in or is plugged into and is typically male or female, respectively (kids, ask your parents for a more thorough explanation). Unfortunately, there are cases where a connector may be referred to as \"male\" when it would appear to be female; in the examples section, we\'ll point a few of those out as we discuss individual component types and explain why that\'s the case.

[![Male and female 2.0mm PH series JST connectors](//cdn.sparkfun.com/assets/2/6/0/7/f/51141810ce395f4d7e000007.jpg)](//cdn.sparkfun.com/assets/2/6/0/7/f/51141810ce395f4d7e000007.jpg)

*Male (left) and female 2.0mm PH series JST connectors. In this case, gender is determined by the individual conductor.*

### Polarity

**Polarity** - Most connectors can only be connected in one orientation. This trait is called polarity, and connectors which have some means to prevent them being connected wrong are said to be **polarized**, or sometimes **keyed**.

[![North America wall plug](//cdn.sparkfun.com/r/400-400/assets/5/1/0/d/c/51154c1cce395f903d000001.jpg)](//cdn.sparkfun.com/assets/5/1/0/d/c/51154c1cce395f903d000001.jpg)

*A polarized North American wall plug. By having two different widths for the plug blades, the plug will only go into the outlet one way.*

### Contact

**Contact** - Contacts are the business portion of the connector. They are the metal parts which touch each other, forming an electrical connection. This is also where problems occur: the contacts can become soiled or oxidized, or the springiness required to hold the contacts together may fade with time.

[![ADH8066 mating connector](//cdn.sparkfun.com/assets/7/4/d/c/6/511414a4ce395f337e000007.jpg)](//cdn.sparkfun.com/assets/7/4/d/c/6/511414a4ce395f337e000007.jpg)

*The contacts on this connector are clearly visible.*

### Pitch

**Pitch** - Many connectors consist of an array of contacts in a repeated pattern. The pitch of the connector is the distance from the center of one contact to the center of the next. This is important, because there are many families of contacts which look very similar but may differ in pitch, making it difficult to know that you are purchasing the right mating connector.

[![.1\" pin header connector examples](//cdn.sparkfun.com/assets/b/c/9/7/1/5148c334ce395f8e55000000.jpg)](//cdn.sparkfun.com/assets/b/c/9/7/1/5148c334ce395f8e55000000.jpg)

*The pitch of the pins on the headers on a standard Arduino is .1\".*

### Mating Cycles

**Mating cycles** - Connectors have a finite life, and connecting and disconnecting them is what wears them out. Datasheets usually present that information in terms of **mating cycles**, and it varies widely from one technology to another. A USB connector may have a lifetime in the thousands or tens of thousands of cycles, while a board-to-board connector designed for use inside of consumer electronics may be limited to tens of cycles. It\'s important that you select a connector with a suitable life for the application.

### Mount

**Mount** - This one has the potential for being confusing. The term \"mount\" can refer to several things: how the connector is mounted in use (panel mount, free-hanging, board mount), what the angle of the connector is relative to its attachment (straight or right-angle), or how it is mechanically attached (solder tab, surface mount, through hole). We\'ll discuss this more in the examples section for each individual connector.

[![Comparison of different mounting methods for barrel-type connectors](//cdn.sparkfun.com/r/600-600/assets/b/5/4/1/6/51140d09ce395f697e000003.jpg)](//cdn.sparkfun.com/assets/b/5/4/1/6/51140d09ce395f697e000003.jpg)

*A comparison of three different methods of mounting the same barrel connector: (left to right) board mount, inline cable mount, and panel mount.*

### Strain Relief

**Strain relief** - When a connector mounts to a board or cable, the electrical connections tend to be somewhat fragile. It is typical to provide some kind of strain relief to transfer any forces acting on that connector to a more mechanically sound object than the fragile electrical connections. Again, there will be some good examples of this later on.

[![1/8\" Headphone jack showing strain relief](//cdn.sparkfun.com/assets/c/a/3/6/6/5113dc95ce395fe501000000.png)](//cdn.sparkfun.com/assets/c/a/3/6/6/5113dc95ce395fe501000000.png)

*This 1/8\" headphone jack comes with a strain relief \"boot\" slid over the cable to prevent forces on the cable from being transmitted directly to the electrical joints.*

## USB Connectors

**USB connectors** come in two flavors: host and peripheral. In the USB standard, there is a difference between the two, and the connectors on cables and devices reflect this. However, all USB connectors will have some things in common:

- **Polarization** - A USB connector can only nominally be inserted one way. It may be possible to force a connector in wrong, but that *will* result in damage to the device.
- **Four contacts** - All USB connectors have at least four contacts (although some may have five, and [USB 3.0+](http://en.wikipedia.org/wiki/USB_3.0) connectors have even more). These are for power, ground, and two data lines (D+ and D-). USB connectors are designed to transmit 5V, up to 500mA.
- **Shielding** - USB connectors are shielded, such that a metal shell which is not part of the electrical circuit is provided. This is important to keep the signal intact in environments with a lot of electrical \"noise\".
- **Robust power connection** - It\'s important for the power pins to make connection before the data lines, to avoid trying to power the device over the data lines. All USB connectors are designed with this in mind.
- **Molded strain relief** - All USB cables have plastic overmolding at the connector to prevent strain on the cable that could potentially damage the electrical connections.

[![Labeled image of USB extension cable](//cdn.sparkfun.com/assets/learn_tutorials/1/8/usb-features.jpg)](//cdn.sparkfun.com/assets/learn_tutorials/1/8/usb-features.jpg)

*A [USB extension cable](https://www.sparkfun.com/products/517), with some of the common features of USB connectors labeled.*

### USB-A Connectors

**USB-A female** is the standard \"host\" connector type. This is found on computers, hubs, or any device intended to have peripherals plugged into it. It is also possible to find extension cables with a female A connector and a male A connector on the other end.

[![USB-A ports on a laptop computer.](//cdn.sparkfun.com/r/600-600/assets/6/2/0/e/3/5113cf7fce395fb17e000000.JPG)](//cdn.sparkfun.com/assets/6/2/0/e/3/5113cf7fce395fb17e000000.JPG)

***Female USB-A** ports on the side of a laptop. The blue connector is USB 3.0 compliant.*

**USB-A male** is the standard \"peripheral\" connector type. Most USB cables will have one end terminating in a USB-A male connector, and many devices (such as keyboards and mice) will have a built-in cable terminated with a USB-A male connector. It\'s also possible to find USB-A male connectors that are board mountable, for devices like USB memory sticks.

[![USB-A male connector examples](//cdn.sparkfun.com/r/600-600/assets/2/a/f/d/4/51154e04ce395f6140000005.jpg)](//cdn.sparkfun.com/assets/2/a/f/d/4/51154e04ce395f6140000005.jpg)

*Two types of **Male USB-A** connectors, on a [SparkFun Cerberus cable](https://www.sparkfun.com/products/11515) and an [AVR Stick](https://www.sparkfun.com/products/9147) development board.*

### USB-B Connectors

**USB-B female** is a standard for peripheral devices. It\'s bulky, but robust, so in applications where size is not an issue, it\'s the preferred means for providing a removable connector for USB connectivity. It is usually a through-hole board mount connector, for maximum reliability, but there are panel-mount options for it as well.

[![USB-B connector on an Arduino Uno](//cdn.sparkfun.com/r/600-600/assets/5/3/d/3/b/5113e953ce395fbf7d000007.JPG)](//cdn.sparkfun.com/assets/5/3/d/3/b/5113e953ce395fbf7d000007.JPG)

*Arduino boards, including this [Uno](https://www.sparkfun.com/products/11224), have long used the female **USB-B** connector, due to its low cost and durability.*

**USB-B male** is almost exclusively found at the end of a cable. USB-B cables are ubiquitous and inexpensive, which also contributes to the popularity of the USB-B connection.

[![Male USB-B connector](//cdn.sparkfun.com/r/600-600/assets/f/7/4/a/7/51154e0ece395fee3f000002.jpg)](//cdn.sparkfun.com/assets/f/7/4/a/7/51154e0ece395fee3f000002.jpg)

*USB-B male* connector on the end of a [SparkFun Cerberus cable](https://www.sparkfun.com/products/11515).

### USB-Mini Connectors

The **USB-Mini** connection was the first standard attempt to reduce the size of the USB connector for smaller devices. USB-Mini female is typically found on smaller peripherals (MP3 players, older cellphones, small external hard drives), and is usually a surface mount connector, trading robustness for size. USB-Mini is slowly being phased out in favor of the USB-Micro connector.

[![USB-Mini female connector](//cdn.sparkfun.com/r/600-600/assets/8/e/e/9/0/51154e0ece395f0440000004.jpg)](//cdn.sparkfun.com/assets/8/e/e/9/0/51154e0ece395f0440000004.jpg)

***USB-Mini female** connector on a [Protosnap Pro Mini](https://www.sparkfun.com/products/10889).*

**USB-Mini male** is another cable-only connector. As with USB-B, it\'s extremely common, and cables can be found cheaply almost anywhere.

[![USB-Mini male connector](//cdn.sparkfun.com/r/600-600/assets/e/a/2/5/3/5113e5f8ce395faa7d000004.JPG)](//cdn.sparkfun.com/assets/e/a/2/5/3/5113e5f8ce395faa7d000004.JPG)

***USB-Mini male** connector on the end of a [SparkFun Cerberus cable](https://www.sparkfun.com/products/11515).*

### USB-Micro Connectors

**USB-Micro** is a fairly recent addition to the USB connector family. As with USB-Mini, the primary concern is size reduction, but USB-Micro adds a fifth pin for low-speed signalling, allowing it to be used in USB-OTG (On-the-go) applications where a device may want to operate as either a host or a peripheral depending on circumstances.

**USB-Micro female** is found on many newer peripherals, such as digital cameras and MP3 players. The adoption of USB-micro as a standard charge port for all new cellular phones and tablet computers means that chargers and data cables are becoming increasingly common, and USB-Micro is likely to supplant USB-Mini in the coming years as the small-factor USB connector of choice.

[![USB-Micro female connector](//cdn.sparkfun.com/r/600-600/assets/0/d/8/8/5/5113e6a5ce395f1c7e000000.JPG)](//cdn.sparkfun.com/assets/0/d/8/8/5/5113e6a5ce395f1c7e000000.JPG)

***USB-Micro female** connector on a [LilyPad Arduino USB](https://www.sparkfun.com/products/11190) board.*

**USB-Micro male** is also a cable-only connector. There are generally two types of cables with USB-Micro male ends: one for connecting a device with a USB-Micro port as a peripheral to a USB host device and one for adapting the USB-Micro female port to a USB-A female port, to be used in USB-OTG capable devices.

[![USB-Micro male connector](//cdn.sparkfun.com/r/600-600/assets/b/5/c/0/c/5113e63fce395ffe7d000000.JPG)](//cdn.sparkfun.com/assets/b/5/c/0/c/5113e63fce395ffe7d000000.JPG)

***USB-Micro male** connector on the [SparkFun Cerberus cable](https://www.sparkfun.com/products/11515).*

[![USB-A female to USB-Micro adapter](//cdn.sparkfun.com/assets/2/7/d/4/f/5113e730ce395f8d7e000000.jpg)](//cdn.sparkfun.com/assets/2/7/d/4/f/5113e730ce395f8d7e000000.jpg)

*[Adapter pigtail](https://www.sparkfun.com/products/11604) for using USB-OTG capable devices having only a USB-Micro port with standard USB peripherals. Note that not all devices supporting USB-OTG will work with this pigtail.*

### USB 3.0 micro-B Cable

**USB 3.0 micro-B cables** look similar to USB 2.0 micro-B connectors but they include additional pins for two differential pairs and a ground.

[![USB 3.0 Micro B male connector](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/9/5/0/14724-USB_3.0_Micro-B_Cable_-_1m-01.jpg)](https://cdn.sparkfun.com//assets/parts/1/2/9/5/0/14724-USB_3.0_Micro-B_Cable_-_1m-01.jpg)

*[USB 3.0 Type A to Micro-B Cable](https://www.sparkfun.com/products/14724)*

### USB 3.1 C Cable

**[USB C](https://en.wikipedia.org/wiki/USB-C)** packs 24 pins into the USB connector. Unlike the previous versions predecessors, this version is reversable! The design of the USB C cable also allows for current above 500mA for your power hungry devices.

[![USB 3.1 Type C connector](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-02.jpg)](https://cdn.sparkfun.com//assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-02.jpg)

*[USB 3.1 Cable A to C](https://www.sparkfun.com/products/14743)*

**Heads up!** Depending on the cable, not all of the pins are broken out for USB C. Some cables may be limited to the USB 2.0 specification with 4 pins as opposed to the full USB 3.1 specification. The [reversible USB A to C cables](https://www.sparkfun.com/products/15424) and [SuzyQable](https://www.sparkfun.com/products/14746) are a few examples. Depending on the USB port that is used, you may also be limited in the amount of current that can be provided to your device.

### Reversible USB

With the advancements in technology and manufacturing, USB connectors can be inserted either way! Below are examples of a reversible type A and type micro-b connector from the catalog.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Reversible Type A Connector End](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/15424-Reversible_USB_A_to_C_Cable_2m-04.jpg)](https://www.sparkfun.com/products/15424)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/15427-Reversible_USB_A_to_Reversible_Micro-B_Cable_2m-02.jpg)](https://www.sparkfun.com/products/15427)
  [![Reversible Type A Connector End](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/A_Reversible_USB_Cable.gif)](https://www.sparkfun.com/products/15424)                    [![Reversible Type Micro B Connector End](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/A_Reversible_Micro_B-Cable.gif)](https://www.sparkfun.com/products/15427)
  *[Reversible Type A Connector End](https://www.sparkfun.com/products/15424)*                                                                                                     *[Reversible Type Micro B Connector End](https://www.sparkfun.com/products/15427)*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

If you are looking for a USB connector or cable, check out our [USB Buying Guide](https://www.sparkfun.com/pages/USB_Guide) or [catalog](https://www.sparkfun.com/categories/386).

[![GPIB-USB Controller](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/4/00594-03-L.jpg)](https://www.sparkfun.com/gpib-usb-controller.html)

### [GPIB-USB Controller](https://www.sparkfun.com/gpib-usb-controller.html) 

[ BOB-00549 ]

The GPIB-USB Controller from Prologix is the easiest way to bridge the gap between modern computers and professional-grade te...

[ [\$319.95] ]

[![SparkFun USB-C Breakout - Horizontal](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/5/9/15100-SparkFun_USB-C_Breakout-01.jpg)](https://www.sparkfun.com/sparkfun-usb-c-breakout.html)

### [SparkFun USB-C Breakout - Horizontal](https://www.sparkfun.com/sparkfun-usb-c-breakout.html) 

[ BOB-15100 ]

The SparkFun USB-C Breakout supplies up to 3 times the power as previous USB board while breaking out each pin on the connect...

[ [\$4.95] ]

[![SparkFun USB Type A Female Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/9/4/4/0/12700-01.jpg)](https://www.sparkfun.com/sparkfun-usb-type-a-female-breakout.html)

### [SparkFun USB Type A Female Breakout](https://www.sparkfun.com/sparkfun-usb-type-a-female-breakout.html) 

[ BOB-12700 ]

This simple board breaks out a female USB type A connector\'s VCC, GND, D- and D+ pins to a 0.1\" pitch header. If you want to ...

[ [\$5.25] ]

[![USB-A Female to Type-C Male Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/7/0/0/21870-_PRT-_01.jpg)](https://www.sparkfun.com/usb-a-female-to-type-c-male-adapter.html)

### [USB-A Female to Type-C Male Adapter](https://www.sparkfun.com/usb-a-female-to-type-c-male-adapter.html) 

[ PRT-21870 ]

This Adapter allows you to run devices and cables with the classic USB Type A connector off a device or adapter with a USB Ty...

[ [\$4.95] ]

------------------------------------------------------------------------

## Audio Connectors

Another familiar connector group are those used for audio-visual applications\--RCA and phono. While these can\'t truly be considered to be of the same family, as the various USB connectors are, we\'ll consider both of them to be in the same vein.

### \"Phone\" Type Connectors

You\'ll probably immediately recognize the 1/8\" version of this connector as a the plug on the end of a pair of headphones. These connectors actually come in three common sizes: 1/4\" (6.35mm), 1/8\" (3.5mm), and 2.5mm. ¼\" size connectors find a lot of use in the professional audio and music community- most electric guitars and amplifiers have 1/4\" tip-sleeve (TS) jacks on them. 1/8\" tip-ring-sleeve (TRS) is very common as the connector for headphones or audio output signals on MP3 players or computers. Some cell phones will provide a 2.5mm tip-ring-ring-sleeve (TRRS) jack for connecting to headphones that also include a microphone for hands-free communications. Below are a few audio jacks that SparkFun carries in the catalog.

[![Audio Cable TRS - 1m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/5/5/8/18983-TRS_3.5mm_Cable-01.jpg)](https://www.sparkfun.com/audio-cable-trs-1m.html)

### [Audio Cable TRS - 1m](https://www.sparkfun.com/audio-cable-trs-1m.html) 

[ CAB-18983 ]

This cable has a standard TRS 3.5mm plug on both ends allowing for easy connections to any 3.5mm jack.

[ [\$2.75] ]

[![Audio Cable TRRS - 1ft](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/7/7/14163-01.jpg)](https://www.sparkfun.com/audio-cable-trrs-1ft.html)

### [Audio Cable TRRS - 1ft](https://www.sparkfun.com/audio-cable-trrs-1ft.html) 

[ CAB-14163 ]

This is a foot-long white audio cable that has been terminated with two TRRS connectors at each end. TRRS connectors are the ...

[ [\$2.25] ]

[![Audio Cable to Alligator Clips - 2.5mm](https://cdn.sparkfun.com/r/140-140/assets/parts/8/3/1/6/17983-2.5mm_Audio_Cable_to_Alligator_Clips_-_2.5mm-01.jpg)](https://www.sparkfun.com/audio-cable-to-alligator-clips-2-5mm.html)

### [Audio Cable to Alligator Clips - 2.5mm](https://www.sparkfun.com/audio-cable-to-alligator-clips-2-5mm.html) 

[ CAB-17983 ]

This is an Audio to Alligator Cable, an 8\" long 22 AWG wire with two alligator clips at one end and a 2.5mm mono plug at the ...

[\$0.95] [ [\$0.61] ]

[![Audio Adapter - 3.5 mm to 1/4\" Stereo](https://cdn.sparkfun.com/r/140-140/assets/parts/6/6/1/1/11150-01.jpg)](https://www.sparkfun.com/products/11150)

### [Audio Adapter - 3.5 mm to 1/4\" Stereo](https://www.sparkfun.com/products/11150) 

[ COM-11150 ]

This is your standard audio jack \"biggifier.\" Plug a 3.5mm cable into one side and now it will magically fit a 1/4\" jack. The...

**Retired**

[Click Here for More Audio Jacks](https://www.sparkfun.com/categories/342)

The common availability of these connectors and cables makes them a good candidate for general purpose connectivity applications\--for instance, long before USB, [Texas Instruments graphing calculators](http://en.wikipedia.org/wiki/TI-85) used a 2.5mm TRS connector for a serial programming connector. It should be remembered that tip-sleeve connector types are not designed for carrying power; during insertion, the tip and the sleeve can be momentarily shorted together, which may damage the power supply. The lack of shielding makes them poor candidates for high-speed data, but low speed serial data can be passed through these connectors.

[![1/8\" TRS phone plug](//cdn.sparkfun.com/assets/c/a/3/6/6/5113dc95ce395fe501000000.png)](//cdn.sparkfun.com/assets/c/a/3/6/6/5113dc95ce395fe501000000.png)

*[Headphone-type TRS phone plug, 1/8\"](https://www.sparkfun.com/products/11143). Typically, tip and ring will carry the stereo audio signals while sleeve will be connected to ground.*

[![1/8\" TS phone plug](//cdn.sparkfun.com/assets/9/a/9/8/3/51141b22ce395f657e000006.jpg)](//cdn.sparkfun.com/assets/9/a/9/8/3/51141b22ce395f657e000006.jpg)

*1/8\" phone plug. Note the lack of a ring contact on this connector.*

[![1/8\" board mount headphone jack](//cdn.sparkfun.com/assets/7/3/1/d/6/51141ba3ce395f337e000008.jpg)](//cdn.sparkfun.com/assets/7/3/1/d/6/51141ba3ce395f337e000008.jpg)

*[1/8\" board mount headphone jack](https://www.sparkfun.com/products/8032) with pins corresponding pin connections labeled. When no jack is inserted, an internal switch connects the tip and ring pins to the adjacent unmarked pins, allowing insertion detection.*

Below are a few audio sockets that SparkFun carries in the catalog.

[![SparkFun TRRS 3.5mm Jack Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/7/5/4/6/11570-01.jpg)](https://www.sparkfun.com/sparkfun-trrs-3-5mm-jack-breakout.html)

### [SparkFun TRRS 3.5mm Jack Breakout](https://www.sparkfun.com/sparkfun-trrs-3-5mm-jack-breakout.html) 

[ BOB-11570 ]

TRRS connectors are the audio-style connectors that you see on some phones, MP3 players and development boards. TRRS stands f...

[ [\$4.50] ]

[![Audio Jack 3.5mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/8/2/08032-Audio_Jack_3.5mm-01.jpg)](https://www.sparkfun.com/audio-jack-3-5mm.html)

### [Audio Jack 3.5mm](https://www.sparkfun.com/audio-jack-3-5mm.html) 

[ PRT-08032 ]

Low profile 3.5mm stereo audio jack.

[ [\$1.75] ]

[![Audio Jack - 1/4\" Stereo (right angle)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/6/0/5/11144-01.jpg)](https://www.sparkfun.com/audio-jack-1-4-stereo-right-angle.html)

### [Audio Jack - 1/4\" Stereo (right angle)](https://www.sparkfun.com/audio-jack-1-4-stereo-right-angle.html) 

[ COM-11144 ]

This is the kind of 1/4\" stereo jack you might find in home stereos and PA systems. Switched contacts allow you to detect whe...

[ [\$1.25] ]

[Click Here for More Audio Sockets](https://www.sparkfun.com/categories/388)

### RCA Connectors

Familiar as the home-stereo connector of choice for many decades, the RCA connector was introduced in the 1940s by RCA for home phonographs. It is slowly being supplanted by connections like HDMI in the audio-visual realm, but the ubiquity of the connectors and cables makes it a good candidate for home-built systems. It will be a long time before it is obsolete.

Female RCA connectors are usually found on devices, although it is possible to find extension or conversion cables with female jacks on them. Most RCA connectors are connected to one of four types of signals: component video (PAL or NTSC, depending on where the equipment was sold), composite video, stereo audio, or S/PDIF audio.

[![Female RCA plug, for video signals.](//cdn.sparkfun.com/assets/8/1/0/1/4/51141d1ace395fff7d000005.jpg)](//cdn.sparkfun.com/assets/8/1/0/1/4/51141d1ace395fff7d000005.jpg)

*[Female RCA connector](https://www.sparkfun.com/products/8631), for video signals. Typically, NTSC or PAL video signal connectors will be yellow.*

Male RCA connectors are usually found on cables.

[![Male RCA plugs](//cdn.sparkfun.com/assets/f/c/9/7/4/5113df13ce395f0f7e000000.jpg)](//cdn.sparkfun.com/assets/f/c/9/7/4/5113df13ce395f0f7e000000.jpg)

*[Male RCA plugs](https://www.sparkfun.com/products/8919). Red and white are usually for audio applications, with red denoting the \"right\" audio channel.*

## Power Connectors

While many connectors carry power in addition to data, some connectors are used specifically to provide power connections to devices. These vary widely by application and size, but we will only focus on some of the most common ones here.

### Barrel Connectors

Barrel connectors are typically found on low-cost consumer electronics which can be plugged into wall power via bulky [AC wall adaptors](https://www.sparkfun.com/products/8269?). Wall adaptors are widely available, in a variety of power ratings and voltages, making barrel connectors a common means for connecting power to small projects.

The female barrel connector, or \"jack\", can be purchased in several varieties: PCB mounted (surface mount or through hole), cable mount, or panel mount. Some of these connectors will have an additional contact that allows the application to detect whether a power supply is plugged into the barrel jack or not, thus allowing the device to bypass batteries and save battery life when running on external power.

[![Female barrel connector](//cdn.sparkfun.com/assets/a/6/c/e/3/51141da0ce395fe67e000005.jpg)](//cdn.sparkfun.com/assets/a/6/c/e/3/51141da0ce395fe67e000005.jpg)

*[Female barrel connector](https://www.sparkfun.com/products/119). When no plug is inserted, the \"insertion detection\" pin will be shorted to the \"sleeve\" pin.*

The male barrel connector, or \"plug\", is usually only found in a wire termination variety, although there are multiple methods of attaching the plug to the end of the wire. It\'s also possible to get plugs that come pre-attached to a cable.

[![Male barrel plug](//cdn.sparkfun.com/assets/e/b/d/c/3/51141dfdce395fe801000002.jpg)](//cdn.sparkfun.com/assets/e/b/d/c/3/51141dfdce395fe801000002.jpg)

*[Unattached male barrel plug](https://www.sparkfun.com/products/11476), for attachment to any power supply. Note that the sleeve connection is designed to be crimped onto the wire for extra strain relief.*

**Heads up!** There are [varying opinions on the gender](https://en.wikipedia.org/wiki/Coaxial_power_connector#Connector_construction_and_terminology) of the jack and plug for these low power coax connectors. Depending on where your get these connectors, the jack can be referred to \"male\" barrel connector due to the pin in the center and vice versa for the plug. Make sure to check out the product image and specs to find what you are looking for!

Barrel connectors provide only two connections, frequently referred to as \"pin\" or \"tip\" and \"sleeve\". When ordering, there are three differentiating characteristics of a barrel connection- inner diameter (the diameter of the pin inside the jack), outer diameter (the diameter of the sleeve on the outside of the plug), and polarity (whether the sleeve voltage is higher or lower than the tip voltage).

**Sleeve diameter** is most commonly either 5.5mm or 3.5mm.

**Pin diameter** is contingent upon sleeve diameter; a 5.5mm sleeve will have either a 2.5mm or 2.1mm pin. Unfortunately, this means that a plug designed for a 2.5mm pin will fit in a 2.1mm jack, but that the connection will be, at best, intermittent. 3.5mm sleeve plugs usually mate to a jack with a 1.3mm pin.

**Polarity** is the final aspect to consider; most often, the sleeve will be considered 0V and the tip will be a positive voltage relative to the sleeve. Many devices will have a small diagram indicating the polarity expected by the device; care should be taken to adhere to this, as an improper power supply may damage the device.

Plugs of both sleeve sizes are usually 9.5mm long, but longer and shorter ones do exist. All SparkFun products use a negative 5.5mm sleeve and a positive 2.1mm pin; we recommend sticking to that standard where possible, as it seems to be the most common flavor found in the wild.

[![Barrel connector polarity label](//cdn.sparkfun.com/r/600-600/assets/2/f/6/e/0/5113f704ce395ffc7d000000.png)](//cdn.sparkfun.com/assets/2/f/6/e/0/5113f704ce395ffc7d000000.png)

*Common polarity diagrams for AC adaptors with barrel plugs. Positive polarity (tip positive, sleeve 0V) is most common. Diagram courtesy Wikipedia user [Three-quarter-ten](http://commons.wikimedia.org/wiki/User:Three-quarter-ten).*

### \"Molex\" Connectors

Most computer hard drives, optical drives, and other internal peripherals get power through what is typically called a \"Molex\" connector. To be more accurate, it\'s a Molex series 8981 connector\--Molex is actually the name of the company which initially designed this connector back in the 1950s\--but common usage has denuded that fact somewhat.

Molex connectors are designed to carry a lot of current: up to 11A per pin. For projects where a lot of power may be needed\--a CNC machine, for instance, or a 3D printer- a very common method for powering the project is to use a desktop PC power supply and connecting the various system circuits through Molex connectors.

The Molex connector is one where the male/female terminology is a bit odd. The female connector is usually found on the end of a cable, and it slips inside of a plastic shell which surrounds the male pins on the male connector. Usually, the connectors are press-fit only, and very, very tight\--they are intended to be connected and disconnected only a few times and, as such, are a bad choice for systems where connections will frequently be changed.

[![Male Molex connector](//cdn.sparkfun.com/assets/5/d/e/d/6/51141ecdce395fba7d00000a.jpg)](//cdn.sparkfun.com/assets/5/d/e/d/6/51141ecdce395fba7d00000a.jpg)

*[Male Molex connector](https://www.sparkfun.com/products/15700). The gender of the pins inside the connector is what signifies the gender of the connector as a whole.*

[![Female Molex connector](//cdn.sparkfun.com/assets/f/d/5/f/2/51141ecdce395f547e000005.jpg)](//cdn.sparkfun.com/assets/f/d/5/f/2/51141ecdce395f547e000005.jpg)

*Female Molex connector on a [project power supply](https://www.sparkfun.com/products/15664).*

### IEC Connector

As with the Molex connector, this is a case where a generalized component name has come to be synonymous with a single, particular item. IEC connector usually refers to the power supply inlet which is commonly seen on desktop PC power supplies. Strictly speaking, that\'s an [IEC 60320-1](http://en.wikipedia.org/wiki/Iec_connector) C13 (female) and C14 (male) connector.

[![IEC 60320-1 C14 male connector](//cdn.sparkfun.com/assets/e/1/f/b/4/51141f68ce395fbf7d00000b.jpg)](//cdn.sparkfun.com/assets/e/1/f/b/4/51141f68ce395fbf7d00000b.jpg)

*C14 male IEC power inlet, on a [DC project power supply](https://www.sparkfun.com/products/11296). Note that, as with the Molex connector, the gender of the connector is defined by the pins within the hood.*

[![C13 female IEC power connector](//cdn.sparkfun.com/assets/9/6/1/7/0/51141f68ce395f7d7e00000c.jpg)](//cdn.sparkfun.com/assets/9/6/1/7/0/51141f68ce395f7d7e00000c.jpg)

*C13 female IEC power connector, on a fairly standard [AC power supply cable](https://www.sparkfun.com/products/14935). Cables with this end can be found all around the world, usually with the dominant local AC connector at the other end.*

IEC connectors are used almost exclusively for AC power input. The nice thing about using one on a project is that IEC-to-wall cables are extremely common *and* available with localized wall plugs for most international locations!

### JST Connector

At SparkFun, we frequently refer to \"2.0mm JST Connectors\". This is yet another generalization of a specific product- JST is a Japanese company which makes high-quality connectors, and our 2.0mm JST connector of choice is the PH series two-position polarized connector.

All of SparkFun\'s single-cell lithium-polymer ion batteries come standard with this type of JST connector, and many of our boards include this connector (or a footprint for it) as a power supply input. It has the advantage of being compact, durable, and difficult to connect backwards. Another feature, which can be an advantage or a disadvantage, depending on how you look at it, is that the JST connector is wicked hard to disconnect (although a [carefully applied diagonal cutter](http://cdn.sparkfun.com/assets/f/e/2/a/b/5114447cce395f7a7a000005.jpg) can be helpful!) once it\'s mated. While this makes it unlikely to fail during use, it also means that disconnecting the battery for charging can damage the battery connector.

[![2-Pin JST male connector on a LilyPad Arduino USB board](//cdn.sparkfun.com/assets/9/6/8/5/c/51142023ce395ff633000005.jpg)](//cdn.sparkfun.com/assets/9/6/8/5/c/51142023ce395ff633000005.jpg)

*2-Pin JST male connector on a [LilyPad Arduino USB](https://www.sparkfun.com/products/11190) board. Again, as with the Molex, the pins inside the hood determine the gender of the connector.*

[![Male and female 2-pin JST connectors](//cdn.sparkfun.com/assets/2/6/0/7/f/51141810ce395f4d7e000007.jpg)](//cdn.sparkfun.com/assets/2/6/0/7/f/51141810ce395f4d7e000007.jpg)

*[Male and female 2-pin JST connectors](https://www.sparkfun.com/products/9914).*

There are PH series connectors with more than two positions; SparkFun even sells them. However, our most frequent application is for the 2-position battery connection.

## SMA Antenna Connectors

Next up is the explanation of the confusing naming conventions for [SMA connectors](http://en.wikipedia.org/wiki/SMA_connector). If you would rather not understand why the convention is the way it is, you can just look at the 4 pictures and move on. Otherwise, have fun with the read!

[![SMA Connectors](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/SMA.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/SMA.jpg)

### RF Connector Conventions

SparkFun uses SMA-type connectors on a few boards that need a 50 Ohm impedance connection to an external antenna ([GPS](https://www.sparkfun.com/categories/17), [Bluetooth](https://www.sparkfun.com/categories/115), cellular, [Nordic](https://www.sparkfun.com/products/705), and [XBee](https://www.sparkfun.com/categories/111)). However, some of these boards use different genders and polarities of the SMA connector. Therefore, we need different antennas to match the specific gender or polarity of the RF connections.

There are 4 different types of SMA connectors using a combination of gender, which refers to the center pin and polarity, which refers to.....uh, this is where it gets confusing. [Wikipedia](http://en.wikipedia.org/wiki/SMA_connector#Reverse_polarity_SMA) tries to explain it. But from what I have found there was an original "old" design for SMA connectors.

### SMA Connectors

The original SMA design called for two compliant connectors:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![SMA Male](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/SMA_Male_Connector_End.jpg "SMA Male")](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/SMA_Male_Connector_End.jpg)   [![SMA Female](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/SMA_Female_Connector_End.jpg "SMA Female")](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/SMA_Female_Connector_End.jpg)

  ***SMA Male**\                                                                                                                                                                             ***SMA Female**\
  Center Pin, Inner Threads*                                                                                                                                                                 Center Hole, Outer Threads*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The above two connectors were designed to be used together, but there was a problem with this configuration and the FCC started moving towards Part 15 compliance. All this means is that all the SMA RF connectors are changing gender (center pin). Really annoying for those of us who need to mate an antenna to an RF device. The FCC gender change was instituted to prevent home users from damaging RF equipment (think home WiFi) when screwing on an antenna. If all antennas are female, there is no way to damage the center connector.

There is one consistency however; all antennas, cables or anything was being attached to a potential stationary object used an outer nut or inner thread design and all stationary devices used the outer thread design. This applies for all SparkFun products. All of our antennas are either SMA male or RP-SMA female. All of our boards are either SMA female or RP-SMA male.

### RP-SMA Connectors

The only thing that changed with the Part 15 compliance was the center pin, thus reversing the polarity of the connection and forming a "new" standard; the reversed polarized SMA (RP-SMA). The RP (reverse polarity) is named after its "thread gender" and has an opposite-gender pin.

The next two photos are considered reversed polarized (RP-SMA).

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![RP-SMA male](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/RP-SMA_Male_Connector_End.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/RP-SMA_Male_Connector_End.jpg)   [![RP-SMA Female](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/RP-SMA_Female_Connector_End.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/RP-SMA_Female_Connector_End.jpg)

  ***RP-SMA Male**\                                                                                                                                                                        ***RP-SMA Female**\
  Center Hole, "Male" Inner Threads*                                                                                                                                                       Center Pin, "Female" Outer Threads*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If the board does not have a u.FL connector to attach an external antenna, SparkFun RF boards and antennas will use a combination of the old (SMA) and new (RP-SMA):

- Cellular and GPS (900/1700/1800MHz and 1.57542GHz respectively) generally use the old convention: SMA male for the antennas and SMA female for the modules.

- Anything 2.4GHz (Bluetooth, ZigBee, WiFi, and Nordic) generally use the new convention: RP-SMA male on the antennas and RP-SMA female on the modules.

Really, you can ignore the gender descriptor. If you have a RP-SMA board or module, you need a RP-SMA antenna and so forth for SMA. Pretty simple, right?! Just make sure to match the antenna frequency with the your board.

And just in case if you happen to find the old and new mixing, we sell a [SMA male to RP-SMA male](https://www.sparkfun.com/products/9233) and a [RP-SMA female to RP-SMA male connector](https://www.sparkfun.com/products/9232) that will most combinations of antenna and connector to be mated.

[![RPSMA Male to SMA Female Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/0/5/09232-1.jpg)](https://www.sparkfun.com/rpsma-male-to-sma-female-adapter.html)

### [RPSMA Male to SMA Female Adapter](https://www.sparkfun.com/rpsma-male-to-sma-female-adapter.html) 

[ WRL-09232 ]

This is an adapter that converts an RP-SMA board to an SMA antenna. The adapter will connect to any of our 2.4GHz wireless bo...

[ [\$2.25] ]

[![SMA Male to RPSMA Male Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/0/6/09233-1.jpg)](https://www.sparkfun.com/sma-male-to-rpsma-male-adapter.html)

### [SMA Male to RPSMA Male Adapter](https://www.sparkfun.com/sma-male-to-rpsma-male-adapter.html) 

[ WRL-09233 ]

This is an inner thread (outer nut) adapter that will connect to any of our wireless boards or interface cables and allow you...

[ [\$2.25] ]

I hope you are not thoroughly confused!

------------------------------------------------------------------------

If you are looking for an RF connector or antenna, check out our [RF Connector Buying Guide](https://www.sparkfun.com/pages/RF_Conn_Guide) or [catalog](https://www.sparkfun.com/categories/78).

[![GNSS Multi-Band L1/L2/L5 Surveying Antenna - TNC (SPK6618H)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/5/9/7/SparkFun_GNSS_SPK6618H_Triband_Antenna_-_2-1.png)](https://www.sparkfun.com/gnss-multi-band-l1-l2-l5-surveying-antenna-tnc-spk6618h.html)

### [GNSS Multi-Band L1/L2/L5 Surveying Antenna - TNC (SPK6618H)](https://www.sparkfun.com/gnss-multi-band-l1-l2-l5-surveying-antenna-tnc-spk6618h.html) 

[ GPS-21801 ]

The SPK6618H is the latest advancement in GNSS antenna technology allowing tri-band (L1/L2/L5) reception for GPS, GLONASS, Ga...

[ [\$169.95] ]

[![GNSS Multi-Band L1/L2/L5 Helical Antenna (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/1/8/1/23847-Antenna-Feature.jpg)](https://www.sparkfun.com/gnss-multi-band-l1-l2-l5-helical-antenna-sma.html)

### [GNSS Multi-Band L1/L2/L5 Helical Antenna (SMA)](https://www.sparkfun.com/gnss-multi-band-l1-l2-l5-helical-antenna-sma.html) 

[ GPS-23847 ]

The SPK-6E antenna is a small, very light weight GNSS/GPS L1/L2/L5 multiband antenna for GPS, Galileo, and BeiDou constellati...

[ [\$119.95] ]

[![GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/1/1/15192-GNSS_Multi-band_Magnetic_Mount_Antenna_SMA_-_5m-01.jpg)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html)

### [GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html) 

[ GPS-15192 ]

The ANN-MB-00 GNSS multi-band antenna is extremely unique from other GNSS/GPS antennas in that it is designed to receive both...

[ [\$109.95] ]

[![GNSS Multi-Band L1/L2 Surveying Antenna - TNC (TOP106)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/7/4/17587-L1_L2_GNSS_antenna_TOP106-09-1.png)](https://www.sparkfun.com/gnss-multi-band-l1-l2-surveying-antenna-tnc-top106.html)

### [GNSS Multi-Band L1/L2 Surveying Antenna - TNC (TOP106)](https://www.sparkfun.com/gnss-multi-band-l1-l2-surveying-antenna-tnc-top106.html) 

[ GPS-17751 ]

The TOP106 from TOPGNSS is a certified GNSS/GPS surveying antenna capable of receiving the L1/L2 bands for GPS, GLONASS, Gali...

[ [\$199.95] ]

------------------------------------------------------------------------

## Pin Header Connectors

Pin header connectors comprise several different means of connection. Generally, one side is a series of pins which are soldered to a PCB, and they can either be at a right-angle to the PCB surface (usually called \"straight\") or parallel to the board\'s surface (confusingly referred to as \"right-angle\" pins). Such connectors come in a variety of pitches, and may have any number of individual rows of pins.

[![Right angle female header pin connector](//cdn.sparkfun.com/assets/7/4/e/2/f/511420f6ce395f157b000003.jpg)](//cdn.sparkfun.com/assets/7/4/e/2/f/511420f6ce395f157b000003.jpg)

*Right-angle female header pin connection on an [FTDI basic](https://www.sparkfun.com/products/9716) board.*

The most commonly seen pin headers are 0.1\" (2.54mm) single or double row connectors. This is a [standard breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all) compatible pitch. These come in [male](https://www.sparkfun.com/products/116) and [female](https://www.sparkfun.com/products/115) versions, and are the connectors used to connect Arduino boards and shields together. Users can easily connect jumper wires to breadboards.

[![0.1\" pin header connector examples](//cdn.sparkfun.com/assets/6/b/4/9/c/51142177ce395f9a7e000005.jpg)](//cdn.sparkfun.com/assets/6/b/4/9/c/51142177ce395f9a7e000005.jpg)

*0.1\" pin header connectors, male and female, on an Arduino Uno board.*

Other pitches are not uncommon; for instance, the [XBee wireless module](https://www.sparkfun.com/products/8664) uses a [2.0mm pitch](https://www.sparkfun.com/products/8272) version of the same connector. Below is a top view showing the SMD 2.00mm pitched female header soldered on the board. As you can see, the two rows of plated through holes for standard breadboard compatible headers next to the headers are spaced at 0.1\" (2.54mm) apart.

[![SMD 2.00mm Header next to 2.54mm PTHSMD 2.00mm Header next to 2.54mm PTH](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/11812-SparkFun_XBee_Explorer_USB-2_00mm-Header-B-2_54mm_PTH.jpg)](https://www.sparkfun.com/products/11812)

*[XBee Explorer USB](https://www.sparkfun.com/products/11812) with SMD 2.00mm pitch headers soldered on the board.*

A common variation on this part is a \"machine pin\" version. While the normal version is formed out of stamped and folded sheet metal, machine pin connectors are formed by tooling the metal into the desired shape. The result is a more robust connector, with a better joint and longer life, making it somewhat more expensive.

[![Female machine pin headers](//cdn.sparkfun.com/assets/d/4/8/d/a/5114022cce395f547e000003.jpg)](//cdn.sparkfun.com/assets/d/4/8/d/a/5114022cce395f547e000003.jpg)

*[Female machine pin headers](https://www.sparkfun.com/products/743). Note that these are designed to be snapped apart into smaller sections, while standard 0.1\" female header pin connectors are not. It\'s also important to note that not all non-machine pin header connectors will mate with the machine pin variety.*

Cables made to connect to these pin headers are usually one of two types: individual wires with **crimp** connectors on them or ribbon cables with **insulation displacement** connectors. These can simply be clamped onto the end of a ribbon cable, which creates a connection to each one of the conductors in the ribbon cable. Generally, cables are only available as female gender and expect a male pin to mate with.

[![Crimp connected header cable](//cdn.sparkfun.com/assets/c/d/6/9/4/511421f8ce395f687e000007.jpg)](//cdn.sparkfun.com/assets/c/d/6/9/4/511421f8ce395f687e000007.jpg)

*[Six-position crimp-type cable](https://www.sparkfun.com/products/10366). Each wire is individually stripped, a connector crimped to it, and then the connectors are inserted into the plastic frame.*

[![2x5 insulation displacement connectors on a ribbon cable](//cdn.sparkfun.com/assets/a/2/c/8/a/5114225fce395fe301000007.jpg)](//cdn.sparkfun.com/assets/a/2/c/8/a/5114225fce395fe301000007.jpg)

*[2x5 insulation displacement connectors (IDC) on a ribbon cable](https://www.sparkfun.com/products/8535). This type of cable can be quickly assembled because it does not require stripping of individual connectors. It also has polarizing tabs on each end, to prevent incorrect insertion in the mating board-side connector.*

Flexible circuits can also use solder tabs spaced with the standard 0.1\" pitch. These tabs are stapled through a flexible substrate in order to make contact with the semi-conductive material.

[![Solder Tabs Stabled through Flexible Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/Solder-Tab-Crimped-Force-Sensitive-Resistor.jpg)](https://learn.sparkfun.com/tutorials/force-sensitive-resistor-hookup-guide#hardware-assembly)

*Solder tab stapled on a flexible sensor.*

Depending on your project application and skill set, there are a few methods of connecting to the solder tabs. Users can insert the solder tabs into breadboards or solder directly to the pins However, the thin solder tabs can break over time when bent excessively and can become loose in a breadboard socket. Flexible sensors can also be sensitive to heat due to the semi-conductive material. As an alternative, the Amphenol FCI Clincher connectors were designed with thicker leads and breadboard compatible sockets for a more reliable connection.

[![Clincher Connectors Used with Flexible Circuits for a More Reliable Connection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/0/Flex_Force_Sensitive_SoftPot_Sensor_Clincher_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/0/Flex_Force_Sensitive_SoftPot_Sensor_Clincher_Connector.jpg)

*[Amphenol FCI Clincher connectors](https://www.sparkfun.com/categories/tags/clincher-connector) crimped on flexible sensors for a more reliable connection.*

## Temporary Connectors

### Screw Terminals

In some cases, it may be desirable to be able to connect bare, unterminated wire to a circuit. Screw terminals provide a good solution for this. They are also good for situations in which a connection should be capable of supporting multiple different connecting devices.

The downside of screw terminals is that they can come undone fairly easily, leaving a bare wire waving around in your circuit. A small dab of hot glue can address this without being too difficult to remove later.

Screw terminals are typically designed for a narrow range of wire gauges, and wires that are too small can be as big a problem as wires that are too big. SparkFun carries four types of screw terminal -- a 2.54mm (0.1\" breadboard standard), a 3.5mm, 5mm, and 10mm pitch version.

[![Screw Terminals 5mm Pitch (2-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/5/2PinScrewTerminal-01-L.jpg)](https://www.sparkfun.com/screw-terminals-5mm-pitch-2-pin.html)

### [Screw Terminals 5mm Pitch (2-Pin)](https://www.sparkfun.com/screw-terminals-5mm-pitch-2-pin.html) 

[ PRT-08432 ]

Screw Terminals with 5mm pitch pins. Comes in 2 or 3 positions and have the really cool feature of slide-locking together to ...

[ [\$1.10] ]

[![Screw Terminals 2.54mm Pitch (2-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/5/2/0/4/10571-01.jpg)](https://www.sparkfun.com/screw-terminals-2-54mm-pitch-2-pin.html)

### [Screw Terminals 2.54mm Pitch (2-Pin)](https://www.sparkfun.com/screw-terminals-2-54mm-pitch-2-pin.html) 

[ PRT-10571 ]

These are simple 2-position screw terminals with 2.54mm pitch pins. Rated up to 150V @ 6A, this terminal can accept 30 to 18A...

[ [\$0.95] ]

[![Screw Terminals 3.5mm Pitch (2-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/7/08084-01.jpg)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-2-pin.html)

### [Screw Terminals 3.5mm Pitch (2-Pin)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-2-pin.html) 

[ PRT-08084 ]

Screw Terminal 3.5mm pitch pins with slide-locking together to form any size you need. Rated up to 125V @ 6A, and can accept ...

[ [\$1.25] ]

[![Terminal Block - 3 Position (15A, 600V)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/0/9/1/13060-01.jpg)](https://www.sparkfun.com/products/13060)

### [Terminal Block - 3 Position (15A, 600V)](https://www.sparkfun.com/products/13060) 

[ PRT-13060 ]

This 3 position screw terminal block provides a simple way to connect wires to a single connection point. These blocks allow ...

**Retired**

[Click Here for More Screw Terminals](https://www.sparkfun.com/categories/383)

Most screw terminals are highly modular, and they can easily be extended at the same pitch by simply connecting two or more smaller sections together.

[![3.5mm screw terminals](//cdn.sparkfun.com/assets/d/6/c/4/a/511422cdce395feb01000003.jpg)](//cdn.sparkfun.com/assets/d/6/c/4/a/511422cdce395feb01000003.jpg)

[]

*[3.5mm pitch screw terminals](https://www.sparkfun.com/products/8235), showing the insertion point of the wire to be connected, the retention screw which holds the wire in place, and the modular connectors on the sides of the individual units allowing multiple pieces to be ganged together.*

### Spring Terminals

Alternatives to screw terminals include spring terminals (a.k.a. \"push-in\", \"cage-clamp\", or \"poke-home\" connectors). Spring terminals work in a similar fashion as screw terminals. However, instead of tightening a screw to make a connection with piece of wire, a spring clamps together pieces of metal together.

Spring terminals provide an alternative to screw terminals. They work [better in environments with a lot of vibrations (i.e. automotive applications)](https://electronics.stackexchange.com/questions/213996/is-a-screw-or-push-in-terminal-better-for-vibrating-environment) or when a wire expanding/contracting due to temperature cycling. Additionally, the tension is automatically adjusted to the wire gauge (assuming it is within the accepted wire thickness) as opposed to variances in tension when a user tightens the screw terminal. Below are a few spring terminal connectors that SparkFun carries in the catalog.

[![Spring Terminals - PCB Mount (4-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/4/08075-01.jpg)](https://www.sparkfun.com/spring-terminals-pcb-mount-4-pin.html)

### [Spring Terminals - PCB Mount (4-Pin)](https://www.sparkfun.com/spring-terminals-pcb-mount-4-pin.html) 

[ PRT-08075 ]

These are small spring terminals. Open the aperature with the small arm, insert the wire, release the arm and the wire is hel...

[ [\$1.95] ]

[![Spring Terminals - PCB Mount (2-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/2/08073-01.jpg)](https://www.sparkfun.com/spring-terminals-pcb-mount-2-pin.html)

### [Spring Terminals - PCB Mount (2-Pin)](https://www.sparkfun.com/spring-terminals-pcb-mount-2-pin.html) 

[ PRT-08073 ]

This is a good quick way to to interface to bare wires.

[ [\$1.75] ]

[![Spring Terminals - PCB Mount (3-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/3/08074-01.jpg)](https://www.sparkfun.com/spring-terminals-pcb-mount-3-pin.html)

### [Spring Terminals - PCB Mount (3-Pin)](https://www.sparkfun.com/spring-terminals-pcb-mount-3-pin.html) 

[ PRT-08074 ]

These are small spring terminals. Open the aperature with the small arm, insert the wire, release the arm and the wire is hel...

[ [\$1.95] ]

[![Spring Terminals - PCB Mount (6-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/6/spring-terminals.jpg)](https://www.sparkfun.com/products/8077)

### [Spring Terminals - PCB Mount (6-Pin)](https://www.sparkfun.com/products/8077) 

[ PRT-08077 ]

These are small spring terminals. Open the aperature with the small arm, insert the wire, release the arm and the wire is hel...

**Retired**

[![Speaker Terminal - 4 Spring](https://cdn.sparkfun.com/r/140-140/assets/parts/6/6/0/6/11145-01.jpg)](https://www.sparkfun.com/products/11145)

### [Speaker Terminal - 4 Spring](https://www.sparkfun.com/products/11145) 

[ COM-11145 ]

You may recognize these as the connectors that are commonly used for home stereo speakers. They happen to make good spring te...

**Retired**

Certain boards (like the [gamer:bit](https://www.sparkfun.com/products/14215), [LumiDrive](https://www.sparkfun.com/products/14779), and [Qwiic MP3 Trigger](https://www.sparkfun.com/products/15165) to name a few) are populated with a spring terminal for easy access to I/O pins. Those witth the poke-home connectors can pushed down on the tab using a ball-point pen or a [Phillips head screwdriver](https://www.sparkfun.com/products/9146).

[![Exp2_Step5bHookup \| closeup of a poke home being wiredup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/5/Exp2_Step5bHookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/5/Exp2_Step5bHookup.jpg)

*A ball-point pen pressing down on the tab of the [gamer:bit\'s poke-home connector](https://learn.sparkfun.com/tutorials/microarcade-kit-experiment-guide/experiment-2-button-reaction-timer) to connect a piece of wire.*

### Banana Connector

Most pieces of power test equipment (multimeters, power supplies) have a very simple connector called a \"banana jack\" on it. These mate to \"banana plugs\", crimped, sprung metal plugs, meant to make a single power connection. They are frequently available in a stackable configuration and can be easily connected to any type of wire. They are capable of carrying several amps of current and are inexpensive.

[![Banana plug](//cdn.sparkfun.com/assets/8/c/a/2/7/5114231ece395f7e7e000002.jpg)](//cdn.sparkfun.com/assets/8/c/a/2/7/5114231ece395f7e7e000002.jpg)

*[Stackable banana plug](https://www.sparkfun.com/products/507). Note that there are two different ways to plug in an additional banana plug.*

[![Variable power supply with banana plugs](//cdn.sparkfun.com/assets/9/5/6/0/3/5113f12fce395fc37e000000.jpg)](//cdn.sparkfun.com/assets/9/5/6/0/3/5113f12fce395fc37e000000.jpg)

*[Extech variable bench supply](https://www.sparkfun.com/products/9291) with banana jacks on the front.*

### Alligator Clip

Named for obvious reasons, alligator clips are good for test connections to posts or bare wires. They tend to be bulky, easily cause shorts to nearby bare metal, and have a reasonably poor grip that can be easily compromised. They are primarily used for low-cost connections during debugging.

[![Alligator clips](//cdn.sparkfun.com/assets/4/b/e/5/4/5114236dce395fa17e000006.jpg)](//cdn.sparkfun.com/assets/4/b/e/5/4/5114236dce395fa17e000006.jpg)

*A [\"third hand\" tool](https://www.sparkfun.com/products/9317), which uses alligator clips to hold work pieces, holding a [wire terminated with an alligator clip for electrical test](https://www.sparkfun.com/products/509). Note the plastic boot surrounding the alligator clip, to make it less likely to short to other connections.*

### IC Clip (or IC Hook)

For more delicate probing operations, there are a variety of IC clips on the market. These are sized to allow a user to clip them onto the pins of an IC without contacting adjacent pins; some of them are delicate enough to be clipped onto even fine-pitched SMD component legs. These smaller clips can be found on [logic analyzers](https://www.sparkfun.com/products/8938) as well as [test leads](https://www.sparkfun.com/products/501), which are great for prototyping or troubleshooting circuits.

[![Large IC clip](//cdn.sparkfun.com/assets/c/5/5/d/f/511423e4ce395fae7e000005.jpg)](//cdn.sparkfun.com/assets/c/5/5/d/f/511423e4ce395fae7e000005.jpg)

*A [large IC clip on the end of a wire](https://www.sparkfun.com/products/506). This clip is still small enough to be connected to a single leg on a through-hole chip without causing a problem for adjacent pins.*

## Other Connectors

### RJ-type Modular Connectors

**Registered jack** connectors are standard for telecommunications equipment into a local exchange. The names one normally hears associated with them (RJ45, RJ12, etc) are not necessarily correct, as the RJ designator is a based on a combination of the number of positions, the number of conductors actually present, and the wiring pattern. For example, while the ends of a standard ethernet cable are usually referred to as \"RJ45\", RJ45 actually implies not only an 8 position, 8 conductor modular jack, it also implies that it is wired for ethernet.

These modular connectors can be very useful, since they combine ready availability, multiple conductors, moderate flexibility, low cost, and moderate current carrying capacity. While not originally intended to deliver a great deal of power, these cables can be used to deliver data and a couple of hundred milliamps from one device to another. Care should be taken to ensure that jacks provided for applications like this are not connected to conventional ethernet ports, as damage will result.

[![8p8c \"RJ45\" style modular jack](//cdn.sparkfun.com/assets/9/b/6/b/4/51142492ce395f8301000005.jpg)](//cdn.sparkfun.com/assets/9/b/6/b/4/51142492ce395f8301000005.jpg)

*A standard 8p8c (8-position, 8-conductor) [\"RJ45\" modular jack](https://www.sparkfun.com/products/643). Be aware that if you intend to use this type of jack to pass DC signals and power, you must avoid using connectors with [built-in signal transformers](https://www.sparkfun.com/products/8534).*

### D-sub Type Connectors

Named for the shape of their shell, D-subminiature connectors are a classic standard in the computing world. There are four very common varieties of this connector: DA-15, DB-25, DE-15, and DE-9. The pin number indicates the number of connections provided, and the letter combination indicates the size of the shell. Thus, DE-15 and DE-9 have the same shell size, but a different number of connections.

[![Female board-mount DE9 connector](//cdn.sparkfun.com/assets/6/5/6/b/8/51142492ce395fe901000004.jpg)](//cdn.sparkfun.com/assets/6/5/6/b/8/51142492ce395fe901000004.jpg)

*[Female DE-9 board-mount connector](https://www.sparkfun.com/products/429). Gender is defined by the pins or sockets associated with each signal, not the connector as a whole, making this connector female despite the fact that it effectively inserts into the shell of the mating connector.*

DB-25 and DE-9 are the most useful to the hardware hacker; many desktop computers still include at least one DE-9 serial port, and often one DB-25 parallel port. Cables terminated with [DE-9](https://www.sparkfun.com/products/65?) and [DB-25](https://www.sparkfun.com/products/64?) connectors are widely available, too. As with the modular connector above, these can be used to provide power and point-to-point communications between two devices. Again, since the common usage of these cables does *not* include power transmission, it is very important that any repurposing of the cables be done cautiously, as a non-standard device plugged into a standard port can easily cause damage.