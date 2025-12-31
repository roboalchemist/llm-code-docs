# Source: https://learn.sparkfun.com/tutorials/xbee-wifi-hookup-guide

## Introduction

Digi\'s XBee WiFi modules are a nifty, all-in-one solution to get your project connected to a wireless network and up into the \\Cloud\\\<\\wavy hands\>. These modules may look just like \"normal\" XBee\'s \-- they\'re even the same size and pinout \-- but they\'re built to seamlessly connect to 802.11b/g/n networks.

[![XBee WiFi with Whip Antenna](https://cdn.sparkfun.com/assets/8/5/c/f/e/528e6965757b7f2f628b456c.png)](https://www.sparkfun.com/products/12571)

*An [XBee WiFi Module with Whip Antenna](https://www.sparkfun.com/products/12571). They\'re also offered with [PCB antennas](https://www.sparkfun.com/products/12568) and [RPSMA](https://www.sparkfun.com/products/12569) and [U.FL](https://www.sparkfun.com/products/12570) connector options.*

Aside from talking over a different wireless standard, these modules work just like any XBee. You can set them up using XCTU (which also helps get it connected to a network). You can toggle I/O pins, read analog and digital inputs, and set the module to sleep. They can operate completely on their own, without the need for an external controlling microcontroller. That said, if you want to hook up an Arduino, or another processor, it can be easily done through the serial port.

You can use these modules just as you would any other XBee \-- to set up a **local wireless serial gateway**. One XBee WiFi module can easily talk to another, as long as it has the local IP address of the other.

But these modules have another, more unique application: to make **Internet-of-Things** projects super-easy. Using the [Etherios(TM) Device Cloud](http://www.etherios.com/products/devicecloud/) service, you can quickly get them connected to the Cloud, where they can publish data and receive commands as well.

### Covered in This Tutorial

In this tutorial we\'ll provide a [quick overview](https://learn.sparkfun.com/tutorials/xbee-wifi-hookup-guide/an-overview) of the XBee WiFi modules. We\'ll then go over some examples. We\'ll show you [how to use XCTU](https://learn.sparkfun.com/tutorials/xbee-wifi-hookup-guide/using-x-ctu) to connect them to a nearby wireless network \-- including setting the SSID and encryption protocols.

In the last example, we\'ll show you how to [connect the XBee WiFi up to the Device Cloud](https://learn.sparkfun.com/tutorials/xbee-wifi-hookup-guide/to-the-cloud). This allows you to control the XBee through a web app loaded up in your web browser. You could control your XBee from across the sea (or from the table across your room).

#### Required Materials

To follow along with this tutorial, you\'ll need the following items:

- An XBee WiFi Module
  - If you want to set up a local wireless serial gateway, you\'ll need more than one.
- Either a [USB Explorer](https://www.sparkfun.com/products/8687), [Explorer Dongle](https://www.sparkfun.com/products/9819), or a [Serial Explorer](https://www.sparkfun.com/products/9111).
  - These boards exist as a \"translator\" between the XCTU software on your computer, and the XBee WiFi module.
- To follow along with the last example, we recommend (all of these are **optional**, or you might have some comparable components):
  - A [Breadboard](https://www.sparkfun.com/products/12002)
  - [XBee Breakout Board](https://www.sparkfun.com/products/8276) with [headers](https://www.sparkfun.com/products/8272) attached
  - [LED](https://www.sparkfun.com/categories/172) (we like [blue](https://www.sparkfun.com/products/529))
  - [Potentiometer](https://www.sparkfun.com/products/9806)
  - [SPDT Switch](https://www.sparkfun.com/products/102)
  - [Momentary Push-Button](https://www.sparkfun.com/products/97)

### Suggested Reading

- [Exploring XBees and XCTU](https://learn.sparkfun.com/tutorials/retired---exploring-xbees-and-xctu) \-- This is a good XBee and XBee explorer primer. If anything, check out the Explorer overviews in this tutorial.
- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication) \-- XBees use serial to communicate and receive data. Having some basic knowledge of serial (baud rate, RX, TX, etc.) goes a long way.
- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) \-- On the last page of this tutorial we\'ll build a circuit on a breadboard to control the XBee WiFi from the cloud.
- [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels) \-- The maximum operating voltage of the XBee WiFi is 3.3V. Don\'t go attaching 5V controllers and sensors to it!

## An Overview

The XBee WiFi modules all share the same footprint and pinout as most \"normal\" XBees. They\'ve got 20 through-hole pins, each spaced by 2mm. The pin functions range from power input to GPIO to analog input to SPI. Here, from the [datasheet](http://ftp1.digi.com/support/documentation/90002180_G.pdf), is the table of pins and their function:

[![Pinout Table](https://cdn.sparkfun.com/r/600-600/assets/4/8/a/0/0/528e6c16757b7f7a5a8b4568.png)](https://cdn.sparkfun.com/assets/4/8/a/0/0/528e6c16757b7f7a5a8b4568.png)

*XBee WiFi Pinout table. Click to embiggen.*

XBee WiFi modules *can* be connected to another microcontroller via their serial port, but what makes them special is they\'ve got a whole host of I/O pins of their own. An XBee alone can toggle LEDs, or motors, or relays, and it can read digital or analog inputs as well. We\'ll take advantage of the XBee I/O capabilities in the [To the Cloud!](https://learn.sparkfun.com/tutorials/xbee-wifi-hookup-guide/to-the-cloud) page, connecting LEDs and buttons directly to the little WiFi module.

### Choosing an Antenna

There are a variety of XBee WiFi modules, each with their own antenna termination. Two of the module have **integrated antennas**: the [PCB antenna](https://www.sparkfun.com/products/12568) and [wire (whip) antenna](https://www.sparkfun.com/products/12571). These are the best choice if you\'re looking for cheap, but they\'ll also have less range.

[![XBee WiFi PCB Antenna](https://cdn.sparkfun.com/r/300-300/assets/f/f/e/2/5/528e6fa4757b7f5d518b4567.jpg)](https://www.sparkfun.com/products/12568)[![XBee WiFi Whip Antenna](https://cdn.sparkfun.com/r/300-300/assets/6/9/b/c/8/528e6fac757b7fef698b456e.jpg)](https://www.sparkfun.com/products/12571)

*XBee WiFi modules with PCB antenna (left) and whip antenna (right). No external antenna needed!*

If you need more range, consider going with the modules with a [U.FL connector](https://www.sparkfun.com/products/12570) or an [RPSMA connector](https://www.sparkfun.com/products/12569). Either of these will require an **compatible external 2.4GHz antenna**.

[![U.FL Antenna](https://cdn.sparkfun.com/r/300-300/assets/5/c/2/5/f/528e6fac757b7f8d548b4568.jpg)](https://www.sparkfun.com/products/12570)[![RPSMA antenna](https://cdn.sparkfun.com/r/300-300/assets/d/c/2/a/1/528e6fac757b7f98688b456e.jpg)](https://www.sparkfun.com/products/12569)

*XBee WiFi modules with a U.FL (left) and SMA (right) antenna connector.*

For the U.FL version, the [Adhesive 2.4GHz antennas](https://www.sparkfun.com/products/11320) make a nice, low-profile choice. For the SMA version, duck antennas ([large](https://www.sparkfun.com/products/558) and [regular](https://www.sparkfun.com/products/145)) make a nice, stylish choice.

### Choosing a Breakout Board

The easiest way to use these modules is to plug them into a mating breakout board. For the next pages of this tutorial, we recommend you get an **XBee Explorer**, which will let you communicate to the XBee from your computer. The Explorers come in [mini-B USB](https://www.sparkfun.com/products/8687), [USB Dongle](https://www.sparkfun.com/products/9819) and [RS-232 Serial](https://www.sparkfun.com/products/9111) (if you\'ve got an ancient computer with a serial port) versions. Any of the three will work!

[![XBee plugged into a USB explorer](https://cdn.sparkfun.com/assets/7/a/e/5/e/528e726b757b7fbb5e8b4575.png)](https://cdn.sparkfun.com/assets/7/a/e/5/e/528e726b757b7fbb5e8b4575.png)

As alternatives to the USB and Serial explorers, there are more simple XBee breakout boards. There\'s *the* [XBee Breakout Board](https://www.sparkfun.com/products/8276), which simply breaks out the 2mm-spaced XBee to a more breadboard-friendly 0.1\" pitch. Then there\'s the [XBee Explorer Regulated](https://www.sparkfun.com/products/11373), which breaks out the pins and has onboard voltage regulating to help mesh with the 3.3V XBee. Either of these are great for embedding into a project, but may be a little more difficult to interface with your computer.

------------------------------------------------------------------------

On the next few pages we\'ll show you how to use the XBee WiFi with XCTU and Digi\'s Cloud Service. This isn\'t the only way to use these modules, but it\'s the easiest to get them up-and-running quickly. If you follow along, you can very easily have an XBee communicating with the \"cloud\".

## Using XCTU

XCTU is Digi\'s XBee configuration software. It makes communicating with XBees very easy, and provides a nice interface to modify all of the module\'s settings. When using it with the XBee WiFi\'s, it even provides a WiFi network scanning and connection interface to make connecting to networks a breeze.

The current release of XCTU is available on [Digi\'s website](http://www.digi.com/support/productdetail?pid=3352&osvid=57&type=utilities), unfortunately it\'s only available for Windows. For Mac OS X users, there is a [beta version of XCTU 6.0.0 available](http://www.digi.com/blog/community/xctu-sneak-peek-sign-up/), which we\'ve tested and found to work flawlessly with the XBee WiFi\'s. (Windows users can check it out too, it\'s pretty slick.) Go ahead and **download XCTU** to follow along.

For this section we\'ll also assume you have an XBee connected to your computer via a [USB Explorer](https://www.sparkfun.com/products/8687) or something similar. The Explorer should have enumerated as a COM port on your computer. This is the port we\'ll use to communicate with the XBee.

### Connecting to a WiFi Network With XCTU

Before we can begin using the XBee WiFi, we need to set it up to connect to our WiFi network. This is a process made simple with XCTU. Follow the steps below:

1.  **Plug** your XBee into your XBee Explorer, and plug the Explorer into your computer.
    - If you haven\'t already installed drivers for your Explorer, you may need to do so. Check out our [How to Install FTDI Drivers tutorial](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) for help there.

2.  **Open XCTU**. It should open up on the \"PC Settings\" tab. On there, select your XBee Explorer\'s **COM port** and make sure the port settings are as below (9600 8-N-1).
    [![XCTU PC Settings tab](https://cdn.sparkfun.com/assets/2/a/c/1/5/528e7e33757b7fdf138b4568.png)](https://cdn.sparkfun.com/assets/2/a/c/1/5/528e7e33757b7fdf138b4568.png)*First, setup your COM port and make sure the settings are correct.*

3.  Hit **Test/Query** to make sure you can communicate with your XBee WiFi. You should get a response like:
    [![XBee Communication Successful](https://cdn.sparkfun.com/assets/b/9/2/d/e/528e7e32757b7f6f5d8b456d.png)](https://cdn.sparkfun.com/assets/b/9/2/d/e/528e7e32757b7f6f5d8b456d.png)*This is a good sign! Means we\'re communicating with the XBee.*

4.  Click over to the **\"Modem Configuration\"** tab. And click **\"Read\"** to display your XBee WiFi\'s stored settings.
    [![Modem configuration settings](https://cdn.sparkfun.com/assets/d/3/d/1/b/528e7e34757b7f0a678b4569.png)](https://cdn.sparkfun.com/assets/d/3/d/1/b/528e7e34757b7f0a678b4569.png)*A view of the XBee WiFi\'s default parameters.*

5.  Select **\"Active Scan\"** near the top of the scrolling window. Then click the **\"Scan\"** button\*\* that appears. This will open the network scan utility.

6.  Click the **\"Scan\"** button at the bottom of the scan window. If all goes well, your network should appear above. The \"Link Margin\" value represents the strength of the signal (bigger is better). And the \"Security\" value indicates the encryption mode of the network.
    [![Scan window](https://cdn.sparkfun.com/assets/1/6/f/7/f/528e7e32757b7fa5648b456a.png)](https://cdn.sparkfun.com/assets/1/6/f/7/f/528e7e32757b7fa5648b456a.png)*Select your network\'s SSID, enter a passkey if necessary, and click \"Select AP\".*

7.  **Select your network**. If it is encrypted, **enter your Security Key**. Then click **\"Select AP\"** (not \"Done\"!). XCTU will configure your XBee, and it\'ll try lease a DHCP address if your network is set up for it.

    - This step can take a while. Be patient. Hopefully, once connected, you\'ll see a window telling you the XBee connected to your network in \"x milliseconds\".

8.  After successfully connecting, click **\"Read\"** at the top of the window again. This will update all of the XBee\'s settings, including GW (the gateway IP), MK (the subnet mask), and **MY (the module\'s assigned IP)**. If these values all make sense, then congratulations, your XBee is connected to your WiFi network!
    [![IP settings](https://cdn.sparkfun.com/assets/8/1/8/4/9/528e7e35757b7f9c678b456f.png)](https://cdn.sparkfun.com/assets/8/1/8/4/9/528e7e35757b7f9c678b456f.png)*Our XBee WiFi module\'s IP address is 192.168.0.101.*

Yay! What now? There are a few directions you can go:

### Communicating with Other XBees

If you\'ve ever used XBees before, you probably think of them as easy-to-setup wireless transceivers. Two XBees, configured correctly, can seamlessly **pass data to each other from one serial port to another**. XBee WiFi\'s are no different!

Following that same set of steps, you can **set up a second XBee WiFi module** to also connect to your wireless network. It\'ll get a unique IP address (usually assigned via DHCP). Take note of that.

To setup two XBees to communicate to each other, you\'ll need to modify the DL \-- **Destination IP Address** \-- of each to the other XBee. You can open a second XCTU window, or configure each one at a time.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/d/1/b/f/4/528e8836757b7f5c5c8b4568.png)](https://cdn.sparkfun.com/assets/d/1/b/f/4/528e8836757b7f5c5c8b4568.png)

*Imagine two XBees connected to a computer, each with it\'s own USB explorer and XCTU window open. If you want to configure them to talk with each other, set the \"DL\" property of each, to the other\'s IP address.*

Then you can click over to the **Terminal tab** to type characters and have them sent from your computer, through one XBee, into the other XBee and out to a second terminal.

------------------------------------------------------------------------

Another optional application for these modules is to use them on the cloud. Digi\'s Device Cloud service makes this very easy. Click over to the next page to see an example setup.

## To the Cloud!

XBee WiFi\'s are built to enable simple communication with [Device Cloud by Etherios (TM)](http://www.etherios.com/products/devicecloud/). The Device Cloud service allows you to interface your XBee WiFi with the web, where you can control the I/O pins and read its status from the comfy confines of your web browser (anywhere in the world!).

Now, Device Cloud *is* a paid service, but it\'s pretty reasonably priced (down to \$0.50 per device per month). They also provide a **free 30 day trial** if you just want to try it out, which is what we\'ll do here.

### Setting up Device Cloud

To begin, we\'ll need to set up the Device Cloud to communicate with our XBee WiFi. Follow the steps below to set this up:

1.  Go to the [Device Cloud Login Page](https://login.etherios.com/login.do). Login or make an account if you don\'t already have one. If you\'re just looking to try it free, don\'t worry \-- you won\'t have to enter any payment info.
2.  In Device Cloud **click to the Device Management tab**.
3.  In the Device Management section, click the **Add Devices** button near the top. This is where we\'ll point our XBee WiFi module to our Device Cloud ID.
4.  There are two methods for adding your XBee. We recommend the manual method:
    - Make sure you\'re on the \"Manual\" half of the Add Device window.
    - Find your **XBee WiFi\'s MAC address**. This is listed in XCTU under the SL and SH (serial number low and high) entries. You\'ll need to concatenate the two values to get your MAC address.
      [![XBee MAC address](https://cdn.sparkfun.com/assets/0/8/e/7/5/528e944e757b7fd9488b4571.png)](https://cdn.sparkfun.com/assets/0/8/e/7/5/528e944e757b7fd9488b4571.png)*In XCTU, this is where you\'ll find the MAC address.*
    - Set the **drop down menu to MAC address**. Then type your XBee\'s address into the text box nearby. You may need to add a couple leading *0*\'s to make it 6-bytes long. Then **click Add**.
      [![Adding XBee MAC address](https://cdn.sparkfun.com/assets/1/9/0/2/7/528e94b6757b7f6c5d8b456f.png)](https://cdn.sparkfun.com/assets/1/9/0/2/7/528e94b6757b7f6c5d8b456f.png)
    - After some thumb-twiddling your XBee and its MAC address should appear in the list below. **Click OK**.
5.  Now you should have an entry for your XBee in Device Cloud now. **Right-click on the XBee and select Properties** (or select the XBee and click the \"Properties\" button above).

[![XBee property window](https://cdn.sparkfun.com/r/600-600/assets/2/4/0/e/4/528e96a9757b7fbf0c8b456c.png)](https://cdn.sparkfun.com/assets/2/4/0/e/4/528e96a9757b7fbf0c8b456c.png)

Here you can view and control just about everything as it relates to your XBee. You can set pins direction and value in the **Input and Output Settings tab**. Try setting a pin to \"Output High\", then click `Save`. The pins should have been driven to 3.3V, but how do you know? Time to whip a circuit together!

### Take an Circuit Assembly Break!

Here\'s the circuit we\'ll use to get the most of XBee\'s example cloud dashboard. You don\'t have to hook up every part, but we recommend at least trying the LED connected to pin 13.

[![XBee Cloud Breadboard Diagram](https://cdn.sparkfun.com/r/600-600/assets/f/4/4/6/9/528fa9c1757b7f0e2a8b4568.png)](https://cdn.sparkfun.com/assets/f/4/4/6/9/528fa9c1757b7f0e2a8b4568.png)

*The schematic and breadboard diagram for the cloud example. Click to embiggen!*

You\'ll still need to power the XBee WiFi module. It can remain in the XBee Explorer, or you can plug it into a separate [XBee Breakout Board](https://www.sparkfun.com/products/8276). Here\'s an image of our hookup using:

- [Half Breadboard](https://www.sparkfun.com/products/12002)
- [10k Trimpot with Knob](https://www.sparkfun.com/products/9806)
- [Mini Push Button](https://www.sparkfun.com/products/97)
- [Mini Power Switch](https://www.sparkfun.com/products/102)
- [5mm Super-Bright Blue LED](https://www.sparkfun.com/products/529)
- [5V/3.3V Breadboard Power Supply](https://www.sparkfun.com/products/10804) (set to 3.3V!)

[![Real Circuit](https://cdn.sparkfun.com/r/600-600/assets/b/4/4/2/c/528fb25d757b7f3e2a8b4567.png)](https://cdn.sparkfun.com/assets/b/4/4/2/c/528fb25d757b7f3e2a8b4567.png)

Now that we\'ve attached some buttons and LEDs, it\'s time to take it to the cloud!

### Setting Up XBee Dashboard

You can use Digi\'s [Example App](https://xbeewifi.herokuapp.com/) to test out your Device Cloud setup. Follow these steps to get up-and-running:

1.  Log in to the [XBee WiFi Cloud Kit](https://xbeewifi.herokuapp.com/#/login). Use the same login as the Device Cloud earlier.
2.  On the next page, under the \"Select a Device\" heading, you should see a dropdown menu with your XBee address already selected. Then just click \"Yes (recommended)\" to configure your XBee for this example.
    [![Setting up the XBee Cloud](https://cdn.sparkfun.com/r/600-600/assets/f/5/5/7/f/528fb620757b7faa298b4567.png)](https://cdn.sparkfun.com/assets/f/5/5/7/f/528fb620757b7faa298b4567.png)
3.  Choose a layout preset and then **Create Dashboard!** You should see something like this on the next screen.
    [![XBee Cloud Kit App](https://cdn.sparkfun.com/r/600-600/assets/7/4/d/3/7/528fb620757b7fdd2a8b4567.png)](https://cdn.sparkfun.com/assets/7/4/d/3/7/528fb620757b7fdd2a8b4567.png)

Play around with it! Try turning the LED on remotely. Then read some buttons and potentiometers. Pretty cool! Now ask a friend from across the ocean to do it. Even cooler!

If you want to build out your own app, all of the required code is viewable by clicking the `</>` button on a widget. It looks like everything\'s hosted on [Digi\'s GitHub page](https://github.com/digidotcom/xbeewificloudkit), which we\'re *huge* fans of.