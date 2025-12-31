# Source: https://learn.sparkfun.com/tutorials/wireless-arduino-programming-with-electric-imp

## Getting Started

[![Imp Arduino Bootloader Screen](https://cdn.sparkfun.com/assets/3/9/0/a/f/52f7ecd6ce395fcd7f8b4567.png)](https://cdn.sparkfun.com/assets/3/9/0/a/f/52f7ecd6ce395fcd7f8b4567.png)

*Loading a new sketch via wireless*

This tutorial will show you how to use an Electric Imp to repogram an Arduino from a webpage. Yep, you read that right. Now you can reprogram an Arduino (and an Imp) from anywhere in the world!

[![Picture of imp stack without yellow wire](https://cdn.sparkfun.com/r/600-600/assets/9/7/a/c/f/52f654e2ce395f327c8b4567.jpg)](https://cdn.sparkfun.com/assets/9/7/a/c/f/52f654e2ce395f327c8b4567.jpg)

*The Electric Imp before modification for bootloading*

The Electric Imp is a powerful device that allows you to connect to the internet relatively easily. For a lot of my Imp projects, I use an Arduino to handle the interface between the various bits of hardware. While reprogramming the Imp is extremely easy via their web-based IDE, reprogramming an Arduino is much more tedious and requires plugging in a computer and downloading new code. Why not use the Imp\'s wireless connection to push new Arduino sketches as well?

If you\'ve ever installed an Arduino into a place that required a scissor lift, in a water tight enclosure, on the top of a building, or into a paper-mache piñata, you understand how problematic it can be to fix that bug you never imagined. With a few bits of hardware you can have an Arduino attached firmly to the Internet of things as well as making the Imp+Arduino a heck of a lot easier to reprogram.

*What in the world is Tomatoless Boots?* Sorry. It\'s a joke first told by [Rob Faludi](http://www.faludi.com/):

    Wireless is a pointless way to describe wireless. It only describes what wireless is not, not what it is. 
    For example, it also has no tomatoes, so we might as well call it 'tomatoless'.

And since it\'s a bootloader of sorts, we decided (against good judgement) to call it [Tomatoless Boots](https://github.com/sparkfun/Tomatoless_Boots). Zomg thank you Aron Steg for writing the [original Imp code](http://forums.electricimp.com/discussion/comment/7904). We took his code and [made a few improvements](https://github.com/sparkfun/Tomatoless_Boots) to dramatically improve the bootload time and to get it to work with general Arduinos.

### Required Materials

Parts you\'ll need:

\

Along with the above parts, you\'ll need the following tools.

- [Exacto Knife](https://www.sparkfun.com/products/9200)
- [Soldering iron](https://www.sparkfun.com/products/10707) and a [bit of wire](https://www.sparkfun.com/products/11367)
- Local Wifi access

This reprogramming-over-wifi trick only works with ATmega328 based Arduinos with a serial bootloader such as the [Arduino Uno](https://www.sparkfun.com/products/11021), [Fio](https://www.sparkfun.com/products/10116), [LilyPad](https://www.sparkfun.com/products/10274), [Pro](https://www.sparkfun.com/products/10915), [Pro Mini](https://www.sparkfun.com/products/11113), and [RedBoard](https://www.sparkfun.com/products/11575). This tutorial will *not* work with the [Due](https://www.sparkfun.com/products/11589), [Leonardo](https://www.sparkfun.com/products/11286), [Micro](http://arduino.cc/en/Main/arduinoBoardMicro), [Galileo](https://www.sparkfun.com/products/12720), or [Teensy](https://www.sparkfun.com/products/12646). There are probably some really good ways of getting these other boards to bootload over wifi but their bootloaders are different enough that this tutorial doesn\'t attempt to cover them.

### Suggested Reading

Other tutorials you may want to brush up on before diving into this one:

- [Getting Started with the Electric Imp](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide)
- [How to use a multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)
- [How to install and solder Arduino Headers](https://learn.sparkfun.com/tutorials/arduino-shields/installing-headers-preparation)

## Bootloading 101

Now for a bit of history and bootloader basics:

[![Optiboot logo](https://cdn.sparkfun.com/assets/0/e/0/b/b/52f7e536ce395f09508b4567.png)](https://cdn.sparkfun.com/assets/0/e/0/b/b/52f7e536ce395f09508b4567.png)

*The [Optiboot](https://code.google.com/p/optiboot/) Logo*

There have been lots of serial bootloaders written throughout the years for lots of different microcontrollers. I wrote one for the [PIC ages ago](https://www.sparkfun.com/tutorials/69) and one to [wirelessly bootload Arduinos over XBee](https://www.sparkfun.com/tutorials/122) as well. The Arduino originally used the STK500 bootloader written by Atmel(see [app note AVR061](http://www.atmel.com/Images/doc2525.pdf)) that was then updated by Peter Knight and Bill Westfield to become the shrunk down [Optiboot](https://code.google.com/p/optiboot/). Optiboot and a handful of similar bootloaders are what are installed on every ATmega328 based Arduino today.

The serial bootloader is activated each time the ATmega328/Arduino is powered up or reset. For a brief period of time (about 500ms), the microcontroller will listen for a special set of characters. If it hears nothing from the computer, then the ATmega will exit the bootloader and begin to run the user\'s code that resides in flash memory. However, if the microcontroller hears those special characters, then it will know that a new program needs to be downloaded and begins to wait for a [HEX file](http://en.wikipedia.org/wiki/Intel_HEX) to be sent. Normally this communication is done while connected to a computer (via a [USB to serial connection](https://www.sparkfun.com/products/9716)), but anything capable of attaching to the serial port on the Arduino has the option to reprogram it. The Imp can talk serial with ease, and the fact that it connects to the world wide web so easily makes it a good choice for wirelessly bootloading your board.

## Hardware Connections

[![Bare Imp Shield](https://cdn.sparkfun.com/assets/7/d/2/7/5/52f7e69bce395f8e038b4567.png)](https://cdn.sparkfun.com/assets/7/d/2/7/5/52f7e69bce395f8e038b4567.png)

*Imp Shield with no headers*

The very first step is to solder the Arduino headers to the Imp shield. For more information about how to do this, checkout this [tutorial](https://learn.sparkfun.com/tutorials/arduino-shields/installing-headers-preparation).

[![Electric Imp Shield Schematic](https://cdn.sparkfun.com/r/600-600/assets/9/f/1/8/1/52f6619bce395f816c8b4568.jpg)](https://cdn.sparkfun.com/assets/9/f/1/8/1/52f6619bce395f816c8b4568.jpg)

*[Schematic](http://cdn.sparkfun.com/datasheets/Dev/Arduino/Shields/electric-imp-shield-v11.pdf) for the Imp Shield*

Next, we need to re-route the Imp\'s UART to the Arduino\'s serial pins (0 and 1). By default the [Imp Shield](https://www.sparkfun.com/products/11401) connects the Imp\'s serial port (pins 5 and 7) to Arduino\'s pins 8 and 9.

[![Solder pads on Imp Shield](https://cdn.sparkfun.com/r/600-600/assets/a/f/d/a/1/52f654e4ce395fe67c8b4567.jpg)](https://cdn.sparkfun.com/assets/a/f/d/a/1/52f654e4ce395fe67c8b4567.jpg)

*The TX and RX pads with default trace*

Luckily, the genius behind the Imp shield design had the foresight to make it easy to switch pins ([Jim](https://github.com/jimblom) is awesome). On the back of the shield, you\'ll find two jumpers labeled RX and TX. In the image above, you should see a small trace connecting the TX and RX pins of the Imp to the right pads labeled 8 and 9.

[![Cut solder pads](https://cdn.sparkfun.com/r/600-600/assets/5/6/e/c/1/52f654e2ce395fd5648b4567.jpg)](https://cdn.sparkfun.com/assets/5/6/e/c/1/52f654e2ce395fd5648b4567.jpg)

*Default trace has been cut*

Carefully use an [exacto knife](https://www.sparkfun.com/products/9200) to cut the default trace. If you\'ve never cut a trace before don\'t worry - it\'s easy! Just take your time. Cutting a trace is less like cutting through metal and more like scoring tile or scraping ice off your windshield; it takes a few passes. Once you\'ve cut the traces, use a [multimeter](https://www.sparkfun.com/products/9141) to do a [continuity test](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter/continuity) to verify that you have indeed severed the connection between the center pad and the pad to the right.

[![Pads soldered together](https://cdn.sparkfun.com/r/600-600/assets/3/e/4/3/b/52f654e4ce395f1e0e8b4568.jpg)](https://cdn.sparkfun.com/assets/3/e/4/3/b/52f654e4ce395f1e0e8b4568.jpg)

*New connections jumpered*

Next, add some solder and jumper the center pads to their matching left pad. The Imp should now be wired directly to the Arduino\'s serial port.

[![Jumper wire from P1 to RST](https://cdn.sparkfun.com/r/600-600/assets/a/e/8/7/b/52f654e4ce395fdb5a8b4568.jpg)](https://cdn.sparkfun.com/assets/a/e/8/7/b/52f654e4ce395fdb5a8b4568.jpg)

*Jumper wire added*

The final hardware modification is a jumper from P1 of the Imp to RST on the shield. This will allow the Imp to reset the Arduino whenever it pulls the P1 pin low.

[![Full stack with jumper in place](https://cdn.sparkfun.com/r/600-600/assets/3/f/4/5/a/52f654e2ce395fc2688b4567.jpg)](https://cdn.sparkfun.com/assets/3/f/4/5/a/52f654e2ce395fc2688b4567.jpg)

*Full stack with jumper in place*

Once you\'ve soldered the jumpers and single wire, add the Imp shield to your Arduino and connect a USB cable. Assuming you have [commissioned your Imp](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/all#blinkup) to your local wifi, the Imp should power up, blink red, then blink green as it attaches to the Internet.

------------------------------------------------------------------------

Now why did I tell you to take your time cutting the default traces? Because I made a big mistake when cutting the default TX trace. Have a second look:

[![Cut trace](https://cdn.sparkfun.com/r/600-600/assets/5/6/e/c/1/52f654e2ce395fd5648b4567.jpg)](https://cdn.sparkfun.com/assets/5/6/e/c/1/52f654e2ce395fd5648b4567.jpg)

Don\'t see the problem? How about now:

[![A bad cut trace](https://cdn.sparkfun.com/r/600-600/assets/a/8/8/f/f/Bad_Cut_Trace.png)](https://cdn.sparkfun.com/assets/a/8/8/f/f/Bad_Cut_Trace.png)

*Uh oh\...*

I was going too fast, the cut I made was too long, and I ended up cutting the TX trace to the Imp. When I attached everything to my Imp bootloading failed to work; everything was timing out because the Imp never heard a response from the Arduino (because the TX trace was cut). Luckily, I had a second functioning setup, so I tested my code on that. Everything worked, so I knew it must be a hardware problem with the board I was using for this tutorial. After a few minutes of scratching my head I used a multimeter to start probing for continuity. Once I discovered TX was not connected I tracked down this bad cut.

[![Green wire fix](https://cdn.sparkfun.com/r/600-600/assets/5/7/a/c/f/52f66aacce395f86698b4567.jpg)](https://cdn.sparkfun.com/assets/5/7/a/c/f/52f66aacce395f86698b4567.jpg)

*Green wire fix*

With some 30AWG [wire wrap wire](https://www.sparkfun.com/products/8186) and some [hemostats](https://www.sparkfun.com/products/8555), the trace was quickly repaired, and the board started working as expected.

Take extra time when cutting traces so as to not cut beyond or knick nearby traces.

## Software Connections

We are going to assume that you have already [commissioned your Imp](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/all#blinkup) and gotten it onto your local wifi. [Log in](https://ide.electricimp.com/signin) to your Electric Imp account and open the Imp IDE. Here is the code you\'ll need to load code into the Agent:

*Above is the code for the Imp Agent*

And here is the code you\'ll need to load into the Imp Device:

*Above is the code for the Imp Device*

Once you\'ve successfully loaded both bits of code, find the [agent link](https://cdn.sparkfun.com/assets/9/2/2/5/4/52f67273ce395fa4668b456c.jpg) at the top of the page. Open another browser tab, and navigate to the agent link. You should be presented with a simple HTML page:

[![Imp Bootloading Page](https://cdn.sparkfun.com/assets/3/9/0/a/f/52f7ecd6ce395fcd7f8b4567.png)](https://cdn.sparkfun.com/assets/3/9/0/a/f/52f7ecd6ce395fcd7f8b4567.png)

*Get ready\... Go!*

From here you can select the hex file you would like to send to your Arduino. The HEX file is found after compiling your sketch in the Arduino IDE. We\'ll tell you how to get these HEX files in the next section. For now, use these two:

- [Blink-1Hz.hex](https://cdn.sparkfun.com/assets/b/1/c/9/7/52f65a13ce395f2c6c8b4569.hex)
- [Blink-Fast.hex](https://cdn.sparkfun.com/assets/3/0/2/c/d/52f65a13ce395fc46f8b456a.hex)

Download these HEX files to your local computer. Select the `Blink-1Hz.hex` from the \'Choose File\' button, then \'Send\' the file to the Arduino. After a few seconds, your Arduino should be bootloaded with the new program! The LED should be blinking once per second. Now select the Blink-Fast hex file, and upload it. The LED should now be blinking four times per second.

[![Output log in Imp IDE](https://cdn.sparkfun.com/r/600-600/assets/3/1/8/5/e/52f673aece395f9e618b456a.jpg)](https://cdn.sparkfun.com/assets/3/1/8/5/e/52f673aece395f9e618b456a.jpg)

*Watch the output in the IDE*

The Imp will provide various bits debug information as well during booloading. If you run into issues, be sure to check the output from the Imp IDE.

## Getting HEX

By default, Arduino outputs the HEX file of your sketch to a rather hard to find, hidden, temporary folder such as `C:\Users\Cylon\AppData\Local\Temp\build7734646579940080062.tmp\Blink.cpp.hex`. Here\'s a trick to make change the output folder of Arduino to an easier to find `C:\HEXFiles\Blink.cpp.hex`.

[![Arduino Preferences Menu](https://cdn.sparkfun.com/assets/c/6/b/6/6/52f654dbce395f0c198b4568.jpg)](https://cdn.sparkfun.com/assets/c/6/b/6/6/52f654dbce395f0c198b4568.jpg)

Open Arduino, and click on File-\>Preferences. This will show you where the `preferences.txt` file is stored. If you move your cursor to this area of the window, the directory will turn blue, and if you click on it, you will open the directory that contains the `preferences.txt` file. You **must close** Arduino before editing this file. Every time Arduino closes, it will overwrite the preferences file with the current settings. If you edit the preferences file while Arduino is open all your changes will be lost.

[![Arduino properties file](https://cdn.sparkfun.com/r/600-600/assets/f/f/4/0/f/52f7bc1ece395fc2298b4567.png)](https://cdn.sparkfun.com/assets/f/f/4/0/f/52f7bc1ece395fc2298b4567.png)

With Arduino closed, open the `preferences.txt`. Add a line:

    build.path=C:\Arduino-Output\

Or the equivalent path for your OS. Any path *without spaces* is valid. I enjoy pointing both my Arduino sketch folder and output folder to a dropbox folder so that I can share libraries and HEX files between computers. You will need to avoid spaces in your build.path otherwise you may see this error:

    C:\Program Files (x86)\Arduino\hardware\tools\avr\bin\avr-ar: unable to rename 'core.a'; reason: File exists

For example: `build.path=C:\Arduino HEX Files\` does not work because of the spaces.

Once you have a path in place, save the changes, and close the file. Reopen Arduino, and open a sketch of your choice (use the Examples-\>Digital-\>Blink if you have no other sketches). Hit the Verify button to compile the sketch.

[![HEX File in list](https://cdn.sparkfun.com/assets/1/a/7/d/4/52f7bfd1ce395faf2f8b4567.png)](https://cdn.sparkfun.com/assets/1/a/7/d/4/52f7bfd1ce395faf2f8b4567.png)

*There\'s the HEX file!*

Now, navigate to the build.path folder. You should see a bunch of files including one with a `.hex` extension. This is the file that needs to be selected and sent via the Electric Imp bootloader.