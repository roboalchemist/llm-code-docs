# Source: https://learn.sparkfun.com/tutorials/metawatch-teardown-and-arduino-hookup

## Introduction

The MetaWatches and BlueSMiRFs used in this tutorial have been retired from our catalog. This tutorial is available for reference if you still need access to the concepts, methods, hardware connections, and example code.\
\
We do have the [BlueSMIRF V2 with headers](https://www.sparkfun.com/products/23287) and the [BlueSMiRF V2 PTH version](https://www.sparkfun.com/products/24113) available if you are interested in using a BlueSMiRF V2 to stream UART data in your project!

The MetaWatch is a new open-source entry into the latest \"Smart Watch\" craze. It\'s a digital watch with a microprocessor and Bluetooth controller built in. It can interface with your smartphone to display stuff like weather forecasts, emails alerts, meeting notifications, or what music is playing (oh, and the time and date too).

SparkFun has a Developer\'s Kit of the MetaWatch in [black](https://www.sparkfun.com/products/12005) and [white](https://www.sparkfun.com/products/12004), which includes the watch, a programmer/charging clip, and a license to use TI\'s [Code Composer Studio](http://www.ti.com/tool/ccstudio).

[![MetaWatch strapped to a hand](https://cdn.sparkfun.com/r/400-400/assets/b/8/1/5/8/520bdb88757b7f3433d102a0.jpg)](https://www.sparkfun.com/products/12005)

The MetaWatch\'s standard use case is certainly very cool. Having notifications, weather, and music updates visible on your wrist is another step towards the future! But what else can we do with this hackable little device? In this tutorial, we\'ll go over some basics of the MetaWatch. Then we\'ll tear it down, and look at its guts! Then we\'ll put it back together and try to control it with\...what else\...an Arduino.

[![A look ahead at Arduino hookup and teardown](https://cdn.sparkfun.com/r/600-600/assets/4/1/0/8/6/520be03c757b7f53078f4015.png)](https://cdn.sparkfun.com/assets/4/1/0/8/6/520be03c757b7f53078f4015.png)

### Required Materials

The Arduino portion of this tutorial will combine an Arduino board with a Bluetooth module.

- The **Arduino Board** can be any Arduino-compatible board \-- [RedBoard](https://www.sparkfun.com/products/11575), [Uno](https://www.sparkfun.com/products/11021), [Pro Mini](https://www.sparkfun.com/products/11113) etc.
- The [BlueSMiRF Silver](https://www.sparkfun.com/products/10269) is used to serve as a bluetooth interface between Arduino and MetaWatch.
- You\'ll also need to **solder wires or headers** to the BlueSMiRF in order to get it connected to the Arduino.

Of course, you\'ll also need a MetaWatch in the style/color of your preference ([White FRAME](https://www.sparkfun.com/products/12004) or [Black FRAME](https://www.sparkfun.com/products/12005)).

### Suggested Reading

If you\'re only interested in checking out the MetaWatch use tips, or teardown, please go right ahead. If you want to control it with an Arduino/BlueSMiRF combo, consider reading some of these tutorials before proceeding:

- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)
- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication)
- [BlueSMiRF Hookup Guide](https://learn.sparkfun.com/tutorials/using-the-bluesmirf)
- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

## Use Tips

Before tearing your watch down, or connecting an Arduino to it, we\'d recommend you check out what it can do when interfaced to your phone. There are **apps** available for both [Android](https://play.google.com/store/apps/details?id=com.metawatch.mwm&hl=en) and [iOS](https://itunes.apple.com/us/app/metawatch-manager-for-ios/id557219641?mt=8) phones.

Play with it. Get a feel for how it functions. Notice how there are four \"Idle mode\" pages you can cycle through. Check it all out!

Playing with the watch might spawn a new project idea. Whether you want to write your own phone app, customize the watch\'s firmware, or connect a different Bluetooth device to it, we\'d encourage everyone to discover a new, cool way to interact with the watch.

### Charging, Connecting the Developer Clip

The Developer Clip is included to serve two purposes: charging and reprogramming. It takes a bit of aiming, but the clip is easy to attach to the watch.

[![Developer clip attached](https://cdn.sparkfun.com/assets/5/8/4/8/3/520ce27b757b7fc776b3f173.jpg)](https://cdn.sparkfun.com/assets/5/8/4/8/3/520ce27b757b7fc776b3f173.jpg)

The clip uses a [Spy-Bi-Wire](http://en.wikipedia.org/wiki/Spy-Bi-Wire) JTAG interface to communicate with the watch\'s MSP430 microcontroller. If you get really into the embedded firmware development side of the MetaWatch, this\'ll be what you use to upload and debug a program. For more more info on using the Developer Clip as a JTAG interface, check out the [JTAG Reflashing documentation](http://www.metawatch.org/assets/images/developers/MetaWatch_JTAG_Reflash_NoIDE_1.0.pdf).

### Button Labels and Gestures

The watch has six buttons, labeled A-F. A is the top-right button (at two o\'clock), and they increment clockwise around the watch.

[![Buttons labeled](https://cdn.sparkfun.com/assets/8/9/4/f/8/520d34f2757b7f76708b4567.png)](https://cdn.sparkfun.com/assets/8/9/4/f/8/520d34f2757b7f76708b4567.png)

The standard button uses are:

- A: Press to close out of most views.
- B: Cycle Idle mode pages
- C: Call up settings view. Turn on/off bluetooth radio, backlight, seconds display, invert display, etc.
- D: Show info display. Shows charge level, firmware version, bluetooth address, and other stats.
- E: Music display (phone-dependant)
- F: Backlight

On top of that, you can **reset** the watch by holding down the middle buttons (B and E) down for a few seconds. Alternatively, holding F does the same thing.

## Teardown

The designers of the MetaWatch made it super-easy to open it up. All you\'ll need is a small 1.4mm flat-head screwdriver, and an equally small #0-or-so Phillips-head. These screwdrivers should be present in most [screwdriver sets](https://www.sparkfun.com/products/10865). The first set of screws \-- flatheads \-- are on the four corners of the back of the watch.

[![Back view of watch](https://cdn.sparkfun.com/r/600-600/assets/8/9/9/7/7/520bbac2757b7ffa066e17cc.jpg)](https://cdn.sparkfun.com/assets/8/9/9/7/7/520bbac2757b7ffa066e17cc.jpg)

Loosening those screws, and removing the back reveals the watch\'s power source: a 20mm 3.7V **Li-Ion coin cell battery** (a smaller version of [this](https://www.sparkfun.com/products/10319)). The other big, visible, circular component is a **vibration motor**. You can also see four spring connectors for the JTAG interface.

[![Back plate removed](https://cdn.sparkfun.com/r/600-600/assets/2/3/3/4/8/520bbb39757b7f27089ef3fb.jpg)](https://cdn.sparkfun.com/assets/2/3/3/4/8/520bbb39757b7f27089ef3fb.jpg)

The guts of the watch are tied to the watch frame by four small Phillips screws. Loosening those screws allows you to (gently) remove the entire LCD/PCB assembly from the frame (you may have to pry it up with the flathead):

[![Watch guts removed from frame](https://cdn.sparkfun.com/r/600-600/assets/5/d/5/3/2/520bbbe6757b7f7e07cce255.jpg)](https://cdn.sparkfun.com/assets/5/d/5/3/2/520bbbe6757b7f7e07cce255.jpg)

### Examining the Guts

The MetaWatch\'s LCD is a 96x96 pixel, reflective, always-on display. We didn\'t get a picture of the back, but the part number is printed there. It\'s a [Sharp LS013B4DN01](http://www.sharpmemorylcd.com/resources/LS013B4DN01_Pre_Spec.pdf). Looks like it\'s got a simple [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)-like interface. Neat!

[![PCB guts](https://cdn.sparkfun.com/r/600-600/assets/0/4/6/6/b/520bbe68757b7f540aed6918.jpg)](https://cdn.sparkfun.com/assets/0/4/6/6/b/520bbe68757b7f540aed6918.jpg)

You can gently lift the display off the main PCB. The display and PCB are connected together using a [zebra connector](http://en.wikipedia.org/wiki/Elastomeric_connector), so they just have to be lined up and pressed together to interface. The PCB is very thin \-- 0.6mm.

[![Top of board](https://cdn.sparkfun.com/r/600-600/assets/b/f/1/7/f/520bc3cb757b7fa4070639df.jpg)](https://cdn.sparkfun.com/assets/b/f/1/7/f/520bc3cb757b7fa4070639df.jpg)

The main processor is the BGA-packaged version of the [MSP430F5438A](http://www.ti.com/product/msp430f5438a). Ultra-low power, 256KB flash, 16KB RAM, 87 I/O. Sweet chip! Low power too. The small chip labeled KXTF9 to the right of the MSP430 is a [Kionix accelerometer](http://www.kionix.com/sites/default/files/KXTF9%20Product%20Brief.pdf). The blue-ish, reflective chip above the MSP430 is a [CC2560 Bluetooth controller](http://www.ti.com/product/cc2560). Those are the most heavy-lifting ICs on the watch. There\'s also a chip antenna (top-left), backlight LED (top-middle), and light sensor (top-right). We also notice an unpopulated IC package \-- intriging.

Let\'s flip it over:

[![Back of board](https://cdn.sparkfun.com/r/600-600/assets/b/f/4/9/a/520bd95f757b7f7607f5cd32.jpg)](https://cdn.sparkfun.com/assets/b/f/4/9/a/520bd95f757b7f7607f5cd32.jpg)

Looks like most of the interesting stuff was on the top side. On the back, there\'s what looks like a Microchip [Serial EEPROM](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en532354), maybe some voltage regulator circuitry, and a wealth of test points. Meh.

And that\'s about it. The watch is really easy to take apart, and put back together (and it still works!). It seems very hackable, and it shows off a few chips which may be useful for other projects.

[![Complete teardown](https://cdn.sparkfun.com/r/600-600/assets/e/7/0/2/6/520bdaf4757b7f20338c9678.jpg)](https://cdn.sparkfun.com/assets/e/7/0/2/6/520bdaf4757b7f20338c9678.jpg)

------------------------------------------------------------------------

Next we\'ll have a look at controlling the watch via Bluetooth, using its published API.

## Connecting Arduino (Hardware)

I wanted to take the watch\'s published bluetooth API for a test drive. But instead of writing a phone app for it, I wanted to use something a little more familiar. Arduino! I\'m not sure how useful it\'ll be in the long run (part of the watch\'s allure is it\'s connected to a phone, which is connected to the Internet), but it\'s a fun exercise in controlling a cool, consumer-product-looking device with an Arduino.

### Connecting Bluetooth

You\'ll need a Bluetooth module to interface between the Arduino and MetaWatch. The MetaWatch\'s CC2560 Bluetooth module is a dual-mode, so it supports serial port profile (SPP) as well as Bluetooth 4.0 (BLE). We\'ll stick to using our go-to SPP Bluetooth module, the [BlueSMiRF Silver](https://www.sparkfun.com/products/10269) (the [Mate](https://www.sparkfun.com/products/10393) should also work).

[![Bluesmirf connected to Arduino](https://cdn.sparkfun.com/r/600-600/assets/5/0/d/3/9/520bb9f0757b7f930ca6616a.jpg)](https://cdn.sparkfun.com/assets/5/0/d/3/9/520bb9f0757b7f930ca6616a.jpg)

The BlueSMiRF interfaces to an Arduino via a [serial interface](https://learn.sparkfun.com/tutorials/serial-communication). On the next page, in the Firmware section, we\'ll use the [Software Serial Arduino library](http://arduino.cc/en/Reference/SoftwareSerial) to set up our serial interface (keeping the hardware interface free for Serial Monitor debugging).

Connecting the BlueSMiRF to the Arduino is about as simple as it gets: four wires. Two wires for power \-- 5V and GND \-- and two wires are for the two serial lines.

[![BlueSMiRF-Arduino fritzing/schematic](https://cdn.sparkfun.com/r/600-600/assets/3/7/7/5/6/520c0c87757b7ffa67e3ab4d.png)](https://cdn.sparkfun.com/assets/3/7/7/5/6/520c0c87757b7ffa67e3ab4d.png)

Note: If pins 10 and 11 don\'t work for your project, you can swap those pins to any SoftwareSerial-enabled pin. You\'ll need to change a couple values in the library if you do so.

## Connecting Arduino (Firmware)

### Download the SFE_MetaWatch Library

We wrote a simple library to interface from Arduino to BlueSMiRF to MetaWatch. Click [here](https://cdn.sparkfun.com/assets/f/a/a/9/7/520d38e7757b7f2d708b4568.zip) to download the library (or visit the [GitHub repo](https://github.com/sparkfun/MetaWatch_Library) to help contribute!). If you need help installing it, check out our [How to Install an Arduino Library tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library).

The library includes a couple pieces of example code, we\'ll be discussing the **SFE_MetaWatch_Menu.ino** example in this tutorial. You can go to *File \> Examples \> SFE_MetaWatch \> SFE_MetaWatch_Menu* within Arduino to open it.

A few things on the library:

- It assumes you have a BlueSMiRF Silver (based on the [RN-42 bluetooth module](https://www.sparkfun.com/products/10253)) connected as shown in the Hardware portion of this guide (Arduino pins 10 and 11).
- It defines a class called `SFE_MetaWatch`, which has a range of member functions you can call to interact with the watch.
- It does its best to automatically connect to the watch, but sometimes this\'ll need to be done manually from the Serial Monitor (see the directions below).

### Connecting BlueSMiRF to MetaWatch

The toughest part of all of this is getting the BlueSMiRF connected to the MetaWatch. Before uploading, make sure you set the `btBaudRate` variable near the top of the sketch to the baud rate of your BlueSMiRF (115200 is the module\'s default). Then set the `metaWatchAddress` variable to the 12-digit HEX address of your watch (press button D (bottom-left), the address is the xxxx-xxxx-xxxx formatted number at the bottom).

After uploading the code, **open up the serial monitor** (set at 9600 bps). When the code first starts, you can enter *k* (case-sensitive) to attempt to connect between BlueSMiRF and watch. If it succeeds, the BlueSMiRF\'s green, \"Connect\" LED should turn on.

If the connect fails, you\'ll enter into echo mode. Here, anything you send to the Serial Monitor will be relayed to the BlueSMiRF. If you\'re in echo mode, follow these steps to connect:

1.  Make sure **No line ending** is selected in the Serial Monitor.
2.  Enter command mode by sending *\$\$\$*. The BlueSMiRF\'s stat LED should blink very fast to show that it\'s in command mode. If it doesn\'t double-check that the `btBaudRate` variable is correctly set.
3.  Switch the line-ending drop down in the Serial Monitor to **Newline**.
4.  Type *C,* and click \"Send\". should be the 12-digit HEX string (0-9, A-F) matching the watch\'s BT address.
5.  The BlueSMiRF should respond \"TRYING\", and in a few seconds the BlueSMiRF\'s green connected LED should illuminate.

[![Animated GIF of connect process](https://cdn.sparkfun.com/assets/d/6/3/e/d/520c0f2b757b7f07601942a5.gif)](https://cdn.sparkfun.com/assets/d/6/3/e/d/520c0f2b757b7f07601942a5.gif)

If it still doesn\'t connect after you see \"TRYING\", double-check the `metaWatchAddress` variable. Also make sure both devices are in range of each other. If all else fails, restoring factory default values to the BlueSMiRF may be a last resort.

### Using the Library

Once connected, you can play around with the menu choices to adjust stuff on the watch. You should definitely try out setting up the clock widgets (send *w*), setting the time (send *t*, then HHMMSS), vibrating (*v*), and controlling the backlight (*l* for off, *L* for on). For more information on what\'s going on, check out the comments in the code.

There are a few parts of the code to highlight:

### Include the Library and Create a Watch Variable

These two pieces of code are required. Include the library near the top of your sketch. Then, sometime before `setup()` create an SFE_MetaWatch instance (we called it `watch`), which you\'ll refer to through the rest of the sketch. The two parameters for this constructor are the Watch\'s BT address, and the baud rate of your BlueSMiRF module.

    language:c

    #include <SFE_MetaWatch.h>
    ...
    SFE_MetaWatch watch(metaWatchAddress, btBaudRate);

### Begin and Connect

The `begin()` function should be called before you do anything else with the watch.

The `connect()` function will attempt to connect the BlueSMiRF to the MetaWatch. If successful, it should return a 1. If it fails it will either return a negative number.

    language:c
    watch.begin();
    ...
    if (watch.connect() < 0) // If connect fails, enter echo mode to manually connect
    

If you\'re having trouble connecting, the `echoMode()` function is a handy tool to try to communicate directly between the Serial Monitor and BlueSMiRF.

### Useful Watch Control Functions

The library can be used to control the watch\'s vibration motor, backlight, and the display. You can also read from the watch\'s light sensor, accelerometer, and battery gauge. And of course, since it is a watch, you can set the real-time clock\'s (RTC) hours, minutes, seconds, and date variables.

Here are a few handy functions to interface with the watch.

#### Set the RTC

The `setTime(year, month, date, day, hours, minutes, seconds)` function should be used to set the watch\'s clock. Each parameter is required. `year` and `month` are pretty self-explanatory, as are `hours`, `minutes` and `seconds`. `Date` is the date of the month (e.g. August **15**). `day` is the day of the week, and it should be a value between 0 and 6 (Sunday is 0, Saturday is 6).

#### Draw on the Display

The watch has four different idle pages you can play with, and cycle through by pressing the B button (middle-right). Eventually, we\'ll get to writing a sprite drawing function on the display, but for now here are some functions you can play with:

The display can be **cleared** completely black or white using the `clear(x)` function. If `x` is 0 it\'ll make the screen white, and if it\'s 1 the screen will black-out.

Pre-defined **widgets** can be drawn on the screen using the `setWidget(msgTotal, msgIndex, widgIDSet[], numWidg)` function. Most of these widgets are clock-related. You can draw full-screen clocks, quarter-screen and half-screen. The widgets aren\'t super-well documented in the API, so it takes some guess-and-check to find out which widget ID does what. The example code throws all four of the full-screen clock widgets on the screen. Check out the code and comments to see how it does that.

Before sending the `setWidget()` function, make sure to send the `watch.fullScreen(0)` command. That tells the watch that the Arduino will be drawing on the full screen of the watch.

After either the `clear()` or `setWidget()` commands, you need to send the `watch.update()` message, which tells the watch to draw what we\'ve been putting in its buffer.

    language:c
    watch.fullScreen(1); // Two options here are 0 for 2/3rd screen or 1 for full-screen
    watch.setWidget(1, 0, fullClockWidget, 4);
    watch.update(0, 0, 96, 0, 1, 0); // Update display to make it happen.
    Serial.println("Widgets updated");

Those four lines, for example, will get your watch to draw four clock full-page clock widgets on four different pages.

#### Vibrate

You can control the watch\'s vibration motor using the `vibrate(timeOn, timeOff, numCycles)` function. `timeOn` determines how many milliseconds the watch vibrates, `timeOff` determines how many milliseconds to *not* vibrate, and `numCycles` tells the watch how many times to repeat that process.

The example, `vibrate(100, 100, 5)` will vibrate 100ms, then stop for 100ms, and repeat five times.

#### Reset

If your watch goes crazy, or gets into an unknown state, the `reset()` function will start you over. After sending `reset()` you\'ll need to re-connect to the watch.

------------------------------------------------------------------------

If you\'d like to contribute to the SFE_MetaWatch library, or add some example code of your own, check out the [GitHub repository](https://github.com/sparkfun/MetaWatch_Library).