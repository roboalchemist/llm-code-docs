# Source: https://learn.sparkfun.com/tutorials/choosing-an-arduino-for-your-project

## Introduction

## Are you just looking for specs between Arduino boards?

Check out our **[Arduino Comparison Guide](https://www.sparkfun.com/standard_arduino_comparison_guide)**! We\'ve compiled every Arduino development board we carry, so you can quickly compare them to find the perfect one for your needs.

[Take me there!](https://www.sparkfun.com/standard_arduino_comparison_guide)

![Arduino Comparison](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/arduino-comparison.jpg)

Let\'s face it, there are a a lot of different Arduino boards out there. How do you decide which one you need for your project? In this tutorial, we\'ll take a look at the diverse world of Arduino boards. We\'ll delve deeper into each board, examining the pros, cons, and example use-cases.

[![Smattering of Arduino Boards](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/0/Arduino-Smattering_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/0/Arduino-Smattering_1.jpg)

[Arduino](https://learn.sparkfun.com/tutorials/what-is-an-arduino) is an open-source electronics prototyping platform based on flexible, easy-to-use hardware and software. It\'s intended for artists, designers, hobbyists, and anyone interested in creating interactive objects or environments. Or more simply, you load on some code and it can read sensors, perform actions based on inputs from buttons, control motors, and accept [shields](https://learn.sparkfun.com/tutorials/arduino-shields) to further expand it\'s capabilities. Really, you can do almost anything.

All Arduino boards have one thing in common: they are programmed through the [Arduino IDE](http://arduino.cc/en/Main/Software). This is the software that allows you to write and upload code. Beyond that, there can be a lot of differences. The number of inputs and outputs (how many sensors, LEDs, and buttons you can use on a single board), speed, operating voltage, and form factor are just a few of the variables. Some boards are designed to be embedded and have no programming interface (hardware) which you would need to buy separately. Some can run directly from a 3.7V battery, others need at least 5V.

### Suggested Viewing

### Suggested Reading

If you don\'t know what Arduino is but found yourself here, you may want to start with our [What is an Arduino tutorial?](https://learn.sparkfun.com/tutorials/what-is-an-arduino).

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

You should also have a good understanding of the Arduino IDE. If you need help installing it, visit [this tutorial](https://learn.sparkfun.com/tutorials/installing-arduino-ide).

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

## Glossary of Terms

**Microcontroller (MCU):** The microcontroller is the heart (or, more appropriately, the brain) of the Arduino board. The Arduino development board is based on AVR microcontrollers of different types, each of which have different functions and features.

**Input Voltage:** This is the suggested input voltage range for the board. The board may be rated for a slightly higher maximum voltage, but this is the safe operating range. A handy thing to keep in mind is that many of the [Li-Po batteries that we carry](https://www.sparkfun.com/search/results?term=lithium&what=products) are 3.7V, meaning that any board with an input voltage including 3.7V can be powered directly from one of our Li-Po battery packs.

**System Voltage:** This is the system voltage of the board, i.e. the voltage at which the microcontroller is actually running. This is an important factor for shield-compatibility since the logic level is now 3.3V instead of 5V. You always want to be sure that whatever outside system with which you\'re trying to communicate is able to match the [logic level](https://learn.sparkfun.com/tutorials/logic-levels) of your controller.

**Clock Speed:** This is the operating frequency of the microcontroller and is related to the speed at which it can execute commands. Although there are rare exceptions, most ATmega microcontrollers running at 3V will be clocked at 8MHz, whereas most running at 5V will be clocked at 16MHz. The clock speed of the Arduino can be divided down for power savings with a few tricks if you know what you\'re doing.

**Digital I/O:** This is the number of digital input/output (I/O) pins that are broken out on the Arduino board. Each of these can be configured as either an input or an output. Some are capable of PWM, and some double as serial communication pins.

**Analog Inputs:** This is the number of [analog input](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion) pins that are available on the Arduino board. Analog pins are labeled \"A\" followed by their number, they allow you to read analog values using the analog-to-digital converter (ADC) in the ATMega chip. Analog inputs can also be configured as more digital I/O if you need it!

**PWM:** This is the number of digital I/O pins that are capable of producing a [Pulse-width modulation](https://learn.sparkfun.com/tutorials/pulse-width-modulation). (PWM) signal. A PWM signal is like an analog output; it allows your Arduino to \"fake\" an analog voltage between zero and the system voltage.

**UART:** This is the number of separate [serial communication](https://learn.sparkfun.com/tutorials/serial-communication) lines your Arduino board can support. On most Arduino boards, digital I/O pins 0&1 double as your serial send and receive pins and are shared with the serial programming port. Some Arduino boards have multiple UARTs and can support multiple serial ports at once. All Arduino boards have at least one UART for programming, but some aren\'t broken out to pins that are accessible.

**Flash Space:** This is the amount of program memory that the chip has available for your to store your sketch. Not all of this memory is available as a very small portion is taken up by the bootloader (usually between 0.5 and 2KB).

**Programming Interface:** This is how you hook up the Arduino board to your computer for programming. Some boards have a USB jack on-board so that all you need to do is plug them into a USB cable. Others have a header available so that you can plug in an [FTDI Basic breakout](https://www.sparkfun.com/search/results?term=ftdi+basic&what=products) or [FTDI Cable](https://www.sparkfun.com/search/results?term=ftdi+cable&what=products). Other boards, like the Mini, break out the serial pins for programming but aren\'t pin-compatible with the FTDI header. Any Arduino board that has a USB jack on-board also has some other hardware that enables the serial to USB conversion. Some boards, however, don\'t need additional hardware because their microcontrollers have built-in support for USB.

## ATmega328-Based Boards

**Note:** The ATmega328P is the updated version of the ATmega328 microcontroller but operates very similarly. It is important to note, however, that the 328P will consume less power than the 328 and that the two chips will have varying chip signatures. In general though, the functionality and programming of the two are comparable. We will be referring to the ATmega328p as the ATmega328 throughout this tutorial.

The ATmega328 (and the ATmega168 before that, and ATmega8 before that,\...) is a staple of the Arduino platform. 32kB of flash (program space), up to 23 I/Os \-- eight of which can be analog inputs \-- operating frequencies of up to 20 MHz. None of it\'s specifications are flashy, but this is still a *solid* 8-bit microcontroller. For many electronics projects, what the 328 provides is still more than enough.

The Arduino boards on this page all feature the ATmega328 as their main MCU brain. The microcontroller alone makes every board on this page nearly identical in terms of I/O count and memory. Their differences stem from things like programming interfaces, form factors, and operating voltages.

### The Main Event: Arduino Uno

The Arduino Uno is the \"stock\" Arduino. It\'s what we compare every, other, Arduino-compatible board to. If you\'re just getting into Arduino, **this is the board to start with**.

[![Arduino Uno - R3](https://cdn.sparkfun.com/r/600-600/assets/parts/6/3/4/3/11021-01.jpg)](https://www.sparkfun.com/arduino-uno-r3.html)

### [Arduino Uno - R3](https://www.sparkfun.com/arduino-uno-r3.html) 

[ DEV-11021 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$27.60] ]

[![Arduino Uno - R3 SMD](https://cdn.sparkfun.com/r/600-600/assets/parts/6/8/1/6/Arduino_Uno_R3-_1.jpg)](https://www.sparkfun.com/arduino-uno-r3-smd.html)

### [Arduino Uno - R3 SMD](https://www.sparkfun.com/arduino-uno-r3-smd.html) 

[ DEV-11224 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$26.30] ]

The Uno comes in two flavors, [through-hole](https://www.sparkfun.com/products/11021) and [SMD](https://www.sparkfun.com/products/11224), which use either a through-hole or surface-mount ATmega328. The through-hole version (pictured above) is nice because you can take the chip out and swap in a new one (in case the magic, blue smoke is released), but the SMD version has the potential to be more readily available (PTH chips are increasingly being phased out of existence).

The Arduino Uno can be powered through either the USB interface, or an external barrel jack. To connect it to a computer you\'ll need a [type-B-to-A USB cable](https://www.sparkfun.com/products/512) (like the USB connector on most printers).

### A Modification: RedBoard

One of the greatest things about Arduino is the fact that the entire project is open-source. The schematics, hardware design files, and source code are all freely available for viewing and modification. Released under a [Creative Commons Share Alike license](http://creativecommons.org/licenses/by-sa/3.0/), anyone is free to riff on the hardware design and produce their own version. That\'s how a product like the [RedBoard](https://www.sparkfun.com/products/13975) comes to be. It still looks and acts just like an Arduino Uno, but is slightly modified to make the board better-suited to certain purposes.

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

The RedBoard is nearly identical to the Uno, but there are a few key differences:

- **USB connector**: The Redboard uses the smaller mini-B connector, so you\'ll need a [mini-B-to-A USB cable](https://www.sparkfun.com/products/11301) to connect it to your computer.
- **USB-to-Serial Transciever**: The Arduino Uno uses an ATmega16U4 loaded with custom firmware to convert between USB and serial. The RedBoard uses the FTDI FT232RL. This difference is only really prevalent when **installing drivers** because each requires a different driver file.
- **SMD vs PTH**: The RedBoard is only offered in a SMD version, and it takes SMD a step further by making *every* component surface-mount. No sharp edges on the bottom of the board!
- **Color**: True to it\'s name, the RedBoard comes in ~~Ferrari~~ SparkFun red. It won\'t have any real influence on the operation of the Arduino, but it certainly affects the board\'s swag-factor.
- **Price**: Because we manufacture the board in-house, here in Boulder, CO, we can afford to keep the price-tag a tad lower.

Like the Uno, the RedBoard is great for beginners. On the whole, it should offer the same Arduino experience as an Uno might. For a deeper comparison between the RedBoard and Uno, check out our [RedBoard vs. Uno tutorial](https://learn.sparkfun.com/tutorials/redboard-vs-uno).

[](https://learn.sparkfun.com/tutorials/redboard-vs-uno)

### RedBoard vs. Uno 

August 6, 2013

In this tutorial we discuss the differences and similarities between the RedBoard and the Arduino Uno (SMD and PTH). The development platforms

### For the Pros

Arduino Pros are a scaled-down version of the Uno. There\'s still an ATmega328 on there, but removed are the connectors and USB-to-serial-converting circuitry. Basically, this is the bare-minimum an Arduino needs to still be an Arduino. As the name would imply, these boards are intended for use by more experienced Arduino-ers.

[![Arduino Pro 328 - 5V/16MHz](https://cdn.sparkfun.com/r/600-600/assets/parts/6/0/4/4/10915-01.jpg)](https://www.sparkfun.com/arduino-pro-328-5v-16mhz.html)

### [Arduino Pro 328 - 5V/16MHz](https://www.sparkfun.com/arduino-pro-328-5v-16mhz.html) 

[ DEV-10915 ]

It\'s blue! It\'s skinny! It\'s the Arduino Pro! SparkFun\'s minimal design approach to Arduino. This is a 5V Arduino running the...

**Retired**

[![Arduino Pro 328 - 3.3V/8MHz](https://cdn.sparkfun.com/r/600-600/assets/parts/6/0/4/3/10914-01.jpg)](https://www.sparkfun.com/arduino-pro-328-3-3v-8mhz.html)

### [Arduino Pro 328 - 3.3V/8MHz](https://www.sparkfun.com/arduino-pro-328-3-3v-8mhz.html) 

[ DEV-10914 ]

It\'s blue! It\'s skinny! It\'s the Arduino Pro! SparkFun\'s minimal design approach to Arduino. This is a 3.3V Arduino running t...

[ [\$18.50] ]

You\'ll need more than just a USB cable to program an Arduino Pro; an external board is required to convert USB from your computer to [serial](https://learn.sparkfun.com/tutorials/serial-communication) that the Arduino understands. There are various boards and cables that can accomplish this task, we recommend the [FTDI Basic Breakout](https://www.sparkfun.com/products/9716).

[![FTDI Basic](https://cdn.sparkfun.com/r/300-300/assets/b/7/4/0/e/522e223b757b7f33538b4568.png)](https://cdn.sparkfun.com/assets/b/7/4/0/e/522e223b757b7f33538b4568.png)

This board mates up to the 6-pin, right-angle connector on the edge of the board. When you\'re done programming and ready to stick the board into a project, just unplug the FTDI Basic.

The smaller form factor and absence of connectors means this board can be more **custom-tailored** to fit into a project. You can solder wires or connectors directly onto the pins you need. Then again, it has the same pin footprint as the Uno, so it\'s still [shield](https://learn.sparkfun.com/tutorials/arduino-shields) compatible.

The Pros come in two varieties: [5V/16MHz](https://www.sparkfun.com/products/10915) and [3.3V/8MHz](https://www.sparkfun.com/products/10914). The 5V/16MHz board runs at the same voltage and speed as the Arduino Uno. The 3.3V/8MHz board is unique, though, because it can operate at a lower voltage. A lower operating voltage makes the board easier to power with batteries ([LiPos](https://www.sparkfun.com/search/results?term=lithium) specifically), but it also means the clock speed has to be turned down. The 3.3V/8MHz board runs at half the speed a regular Arduino Uno\...but 8MHz is still pretty darn fast for many applications. You can still turn an LED on and off more than a million times per second!

Of course, if this board is still to big, you can shrink it down even further\...

#### Pro Mini\'s

The Mini boards pack all of the remaining punch of the Arduino Pro into a much smaller footprint. Every pin is still broken out (actually, *more* pins are broken out), they\'re just in a very different footprint.

[![Arduino Pro Mini 328 - 5V/16MHz](https://cdn.sparkfun.com/r/600-600/assets/parts/6/5/3/9/11113-01b.jpg)](https://www.sparkfun.com/arduino-pro-mini-328-5v-16mhz.html)

### [Arduino Pro Mini 328 - 5V/16MHz](https://www.sparkfun.com/arduino-pro-mini-328-5v-16mhz.html) 

[ DEV-11113 ]

SparkFun\'s minimal design approach to Arduino. This is a 5V Arduino running the 16MHz bootloader.

[ [\$11.25] ]

[![Arduino Pro Mini 328 - 3.3V/8MHz](https://cdn.sparkfun.com/r/600-600/assets/parts/6/5/4/0/11114-01.jpg)](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html)

### [Arduino Pro Mini 328 - 3.3V/8MHz](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html) 

[ DEV-11114 ]

SparkFun\'s minimal design approach to Arduino. This is a 3.3V Arduino running the 8MHz bootloader.

[ [\$11.25] ]

*An Arduino Pro Mini attached to an FTDI Basic, which provides power and uploads code.*

Obviously, these boards aren\'t shield-compatible, but they are [breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)-compatible. You can solder male headers into the Pros, and straddle it across the breadboard\'s middle strip. The small form-factor also makes them very conducive to embedding into projects (like in the [H2O pH Probe](https://www.sparkfun.com/news/1305)).

Like the regular Pro boards, these are offered in [5V/16MHz](https://www.sparkfun.com/products/11113) and [3.3V/8MHz](https://www.sparkfun.com/products/11114) varieties. And you still have to program them with an FTDI Basic.

### Etcetera

#### Arduino Fio

And, the [Arduino Fio](https://www.sparkfun.com/products/10116) too. This board wires up the ATmega328 to an XBee (or XBee-compatible) wireless transceiver, so your Arduino can communicate wirelessly with other devices.

[![Arduino Fio](https://cdn.sparkfun.com/r/600-600/assets/parts/4/3/6/9/10116-01.jpg)](https://www.sparkfun.com/arduino-fio.html)

### [Arduino Fio](https://www.sparkfun.com/arduino-fio.html) 

[ DEV-10116 ]

The Arduino Funnel I/O (Fio) is a board designed by Shigeru Kobayashi, based on the original design from \[LilyPad\](http://www...

[\$30.95] [ [\$10.83] ]

#### ATmega328P with Arduino Optiboot

What do you get when you take the SparkFun RedBoard or the Arduino Uno and strip away everything but the microcontoller? The ATmega328P with Optiboot is what you get, offering the functionality of the RedBoard and Uno in a much smaller package. For reference when placing the Arduino on a breadboard or a project, we labeled the pins with a sticker!

[![ATmega328 with Arduino Optiboot (Uno)](https://cdn.sparkfun.com/r/600-600/assets/parts/5/0/7/6/10524-01.jpg)](https://www.sparkfun.com/atmega328-with-arduino-optiboot-uno.html)

### [ATmega328 with Arduino Optiboot (Uno)](https://www.sparkfun.com/atmega328-with-arduino-optiboot-uno.html) 

[ DEV-10524 ]

The name says it all on this one. An ATmega328P in DIP package, pre-loaded with the Arduino Optiboot (Uno 16MHz) Bootloader. ...

[ [\$6.50] ]

The Optiboot (Arduino Bootloader) allows for Arduino code to be uploaded to the microcontroller without the RedBoard or the Uno. This comes in handy when you want the functionality of a basic board but need to save some space. To upload code from the Arduino IDE to the ATmega328P you will need a 5V power supply, a serial UART circuitry, and a 16MHz crystal. Once that is taken care of, you\'ll be all set to tackle your next project!

#### RedStick

Have you ever wanted a RedBoard that could fit in your pocket protector? Well fret no more! The RedStick has many of the same features you\'re used to with ATmega328 boards, now in fun size!

[![SparkFun RedStick](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/2/5/8/13741-01.jpg)](https://www.sparkfun.com/products/13741)

### [SparkFun RedStick](https://www.sparkfun.com/products/13741) 

[ DEV-13741 ]

In 2015 we developed the BadgerStick as a fun and interactive way for people to learn about soldering and engage with SparkFu...

**Retired**

Despite it\'s small size, the board still has 14 digital I/O pins with 6 PMW pins, 8 analog inputs, UART, SPI, I2C, and external interrupts. Running at 5V/16MHz, the board can be powered either through the USB plug, single celled LiPo battery, or even 2x AA batteries. The onboard boost converter allows the board to be powered with an input range between **2 to 6 volts**. With a built-in FTDI and USB end, simply connect the board directly to a computer\'s USB port to reprogram! (No external FTDI board or USB cable required!)

#### RedBot Mainboard

The RedBot Mainboard is meant for simple, fast development for robotic controls. It is an all in one board that includes an XBee header, pre-programmed Optiboot (Uno) bootloader, numerous pins for sensor integration, TB6612FNG dual DC motor driver, power switch, and a motor disable switch so that pesky robot doesn\'t keep trying to run off while you\'re tinkering. While designed specifically for the Magician and Shadow chassis, the servo and sensor capabilities can be applied to many robotic projects.

[![SparkFun RedBot Mainboard](https://cdn.sparkfun.com/r/600-600/assets/parts/8/7/3/4/12097-01.jpg)](https://www.sparkfun.com/sparkfun-redbot-mainboard.html)

### [SparkFun RedBot Mainboard](https://www.sparkfun.com/sparkfun-redbot-mainboard.html) 

[ ROB-12097 ]

The SparkFun RedBot Mainboard is a robotic development platform that works with the Arduino IDE.

[ [\$36.95] ]

Like many standard ATmega328P boards, the RedBot operates at 5V, has an operating frequency of 16Hz, and has a flash memory of 32kB. Pin-wise it comes with two 1x3 female header for motors, four 2x3 male headers for servos, and two 2x3 male headers sensor ports. Because the board is a motor driver-Arduino combo with all these headers and connectors, the need to stack multiple shields is eliminated while customization is increased.

#### OpenScale

If you\'re working on a project and want to record the temperature or measure the weight of a static load, then the OpenScale is the perfect board for you. Designed for data collection, the OpenScale utilizes screw terminals to connect to temperature sensors and load cells. The board comes with a built-in HX711 load cell amplifier and FTDI.

[![SparkFun OpenScale](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/4/6/5/13261-01.jpg)](https://www.sparkfun.com/sparkfun-openscale.html)

### [SparkFun OpenScale](https://www.sparkfun.com/sparkfun-openscale.html) 

[ SEN-13261 ]

The SparkFun OpenScale is a simple-to-use, open source solution for measuring weight and temperature. It has the ability to r...

[ [\$40.26] ]

When it comes to recording the data, you will have plenty of options. You can simply connect the OpenScale to your computer using your USB port. You can also connect a datalogger (like the OpenLog) or communicate with a Bluetooth transmitter using the serial UART port. The board operates at 5V/16MHz.

Another great benefit of the OpenScale is that it\'s open source. To upload code to the OpenScale, simply use the Arudino IDE. The board comes with a bootloader compatible with the Arduino Uno, so get coding!

#### OpenLog

The SparkFun OpenLog is an open source datalogger that works over a simple serial UART connction. While it\'s smaller than the Arduino Pro Mini, there are not as many pins broken out for easy access on the PCB. The board includes a microSD card socket that handles up to 32GB to store all the serial data that your project generates for scientific or debugging purposes.

[![SparkFun OpenLog](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/2/0/2/13712-SparkFun_OpenLog-01.jpg)](https://www.sparkfun.com/sparkfun-openlog.html)

### [SparkFun OpenLog](https://www.sparkfun.com/sparkfun-openlog.html) 

[ DEV-13712 ]

The SparkFun OpenLog can store, or \"log\", huge amounts of serial data and act as a black box of sorts.

[ [\$17.50] ]

The board operates at 3.3V and requires a 3.3V FTDI to program

#### MicroView

The MicroView combines the ATmega328P with a 64x48 pixel OLED to display sensor data, email, pin status, and more. The MicroView also has a full-featured Arduino library to make programming the module easy. The board includes 12 digital I/O pins (3 of which provide PWM output and 6 analog input pins).

[![SparkFun MicroView - OLED Arduino Module](https://cdn.sparkfun.com/r/600-600/assets/parts/9/8/4/5/12923-01.jpg)](https://www.sparkfun.com/sparkfun-microview-oled-arduino-module.html)

### [SparkFun MicroView - OLED Arduino Module](https://www.sparkfun.com/sparkfun-microview-oled-arduino-module.html) 

[ DEV-12923 ]

The MicroView is the first chip-sized Arduino compatible module that lets you see what your Arduino is thinking using a built...

[ [\$47.95] ]

The MicroView operates at 5V/16MHz and requires a 5V FTDI or the MicroView USB Programmer to upload code.

------------------------------------------------------------------------

The list could go on and on. If you see a board with that recurring, six-pin, serial header, and an ATmega328 doing all of the processing, its specifications probably aren\'t all that different from an Arduino Pro.

## ATmega32U4-Based Boards

The next step in the Arduino evolutionary chain was merging the USB-to-Serial programming part of the board onto the main MCU. That meant we had to leave the ATmega328 behind \-- because it doesn\'t natively support USB \-- in favor of the ATmega32U4. Aside from the additional USB support, the 32U4 is largely similar to the 328. Both are 8-bit AVRs with 32kB of flash memory, 22-ish I/O lines, ADCs, UARTs, timers, etc.

These ATmega32U4 boards often have the benefit of being **cheaper** than the ATmega328-based boards \-- there\'s one less costly [IC](https://learn.sparkfun.com/tutorials/integrated-circuits) to put on there. They can also do things regular Arduino boards can\'t, like emulate a USB keyboard/mouse. On the downside, they can be less reliable, and more difficult to use.

### Arduino Leonardo

The [Leonardo](https://www.sparkfun.com/products/11286) is the patriarch of all ATmega32U4 Arduino boards. It shares the same form factor and I/O placement (analog, PWM, I^2^C pins in the same place) as the Arduino Uno, so it remains shield compatible.

[ ![Arduino Leonardo with Headers](https://cdn.sparkfun.com/r/600-600/assets/parts/6/9/5/3/11286-01a.jpg) ]

### Arduino Leonardo with Headers 

[ DEV-11286 ]

Arduino is an open-source physical computing platform based on a simple i/o board and a development environment that implemen...

**Retired**

Differences between the Leonardo and the Uno? Aside from the new microcontroller, and lack of a second USB-to-Serial-converting IC, there\'s not many. The USB connector is different, the Leonardo connects to a computer via a [micro-B USB cable](https://www.sparkfun.com/products/10215). The [driver installation process](http://arduino.cc/en/Guide/ArduinoLeonardoMicro?from=Guide.ArduinoLeonardo) is also a bit more involved \-- sometimes it can take a little extra fidgeting to get the board installed on your computer.

### Pro Micro

Just as the Pro Mini took the guts of the Arduino Uno and shrunk them down, the Pro Micro works as a miniature version of the Leonardo. Unlike the Pro Mini, the Pro Micro doesn\'t require an external board to upload a sketch \-- the 32U4 takes care of everything!

[![Pro Micro - 5V/16MHz](https://cdn.sparkfun.com/r/600-600/assets/parts/9/3/2/6/12640-01a.jpg)](https://www.sparkfun.com/pro-micro-5v-16mhz.html)

### [Pro Micro - 5V/16MHz](https://www.sparkfun.com/pro-micro-5v-16mhz.html) 

[ DEV-12640 ]

Here at SparkFun, we refuse to leave \'good enough\' alone. That\'s why we\'re adding to our line-up of Arduino-compatible microc...

[ [\$22.50] ]

[![Pro Micro - 3.3V/8MHz](https://cdn.sparkfun.com/r/600-600/assets/parts/9/2/4/9/12587-01b.jpg)](https://www.sparkfun.com/pro-micro-3-3v-8mhz.html)

### [Pro Micro - 3.3V/8MHz](https://www.sparkfun.com/pro-micro-3-3v-8mhz.html) 

[ DEV-12587 ]

Here at SparkFun, we refuse to leave \'good enough\' alone. That\'s why we\'re adding to our line-up of Arduino-compatible microc...

[ [\$21.50] ]

The Pro Micro comes in the standard [5V/16MHz](https://www.sparkfun.com/products/11098) operating range or a more unique [3.3V/8MHz](https://www.sparkfun.com/products/10999) variant.

Pro Micros are among the more complicated Arduino boards to get up and running. There are [extra steps](http://www.sparkfun.com/tutorials/338) required to enable them in your Arduino environment, and a misstep can (at least temporarily) \"brick\" the Pro Micro. These boards are a good choice if you\'re an advanced Arduino-er and have a small USB-oriented project in mind ([a mini USB keyboard/mouse?](https://www.sparkfun.com/tutorials/337)).

### More Variants!

#### FioV3

There are plenty of other riffs on the Leonardo design as well. There\'s the [Fio v3](https://www.sparkfun.com/products/11520), for any Arduino Leonardo project you might want to add an XBee to.

[![Fio v3 - ATmega32U4](https://cdn.sparkfun.com/r/600-600/assets/parts/7/4/4/0/11520-01.jpg)](https://www.sparkfun.com/fio-v3-atmega32u4.html)

### [Fio v3 - ATmega32U4](https://www.sparkfun.com/fio-v3-atmega32u4.html) 

[ DEV-11520 ]

The Fio v3 is a new spin on the Arduino Fio hardware powered by the ATmega32U4.Not only is it small and LiPo-ready, it\'s a ve...

**Retired**

### QDuino Mini

Or the [Qduino Mini](https://www.sparkfun.com/products/13614) which adds a LiPo charger and battery fuel gauge, and two RGB LEDs (one for status and another that is user programmable!). The board was designed by Quin at the age of 14 and manufactured at SparkFun.

[![Qduino Mini - Arduino Dev Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/9/8/7/13614-01b.jpg)](https://www.sparkfun.com/qduino-mini-arduino-dev-board.html)

### [Qduino Mini - Arduino Dev Board](https://www.sparkfun.com/qduino-mini-arduino-dev-board.html) 

[ DEV-13614 ]

The Qduino Mini is a tiny, Arduino-compatible board with a battery connector and charger built-in as well as a fuel gauge tha...

[ [\$35.95] ]

#### Bare Conductive Touch Board

Then there is the Bare Conductive touch board. Basically it is a Arduino Leonardo designed to turn almost any material or surface into a sensor. The board comes with a built-in capacitive touch sensor, a MP3 decoder IC, microSD card socket, and LiPo charge IC to create light switches, musical instruments, custom interactive surfaces.

[![Bare Conductive Touch Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/5/5/4/13298-02.jpg)](https://www.sparkfun.com/bare-conductive-touch-board.html)

### [Bare Conductive Touch Board](https://www.sparkfun.com/bare-conductive-touch-board.html) 

[ DEV-13298 ]

The Touch Board from Bare Conductive is an easy-to-use Arduino@Heart board that gives you the ability to turn almost any mate...

**Retired**

## Wearable Arduinos

The e-textiles segment of the Arduino market is ruled by LilyPads. These are identifiable as unique purple, flowery-looking, circular boards. The pins on LilyPads are called \"petals\", they have bigger holes and copper filled to the edge of the board. These are designed so [conductive thread](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing) can be sewn through the holes, and make electrical contact with the exposed copper on the petal.

[![LilyPad sewn into fabric](https://cdn.sparkfun.com/r/600-600/assets/a/4/a/f/f/5228cce1757b7f2c568b4568.JPG)](https://cdn.sparkfun.com/assets/a/4/a/f/f/5228cce1757b7f2c568b4568.JPG)

LilyPads are great for e-textiles \-- projects which combine electronics and fabric wizardy. For a detailed explanation of these boards, check out this tutorial.

[](https://learn.sparkfun.com/tutorials/choosing-a-lilypad-arduino-for-your-project)

### Choosing a LilyPad Arduino for Your Project 

October 27, 2015

Not sure which LilyPad Arduino is right for you? We\'ll discuss the features of each and help you decide.

## More Power!

Need some extra \"beef\" in your Arduino? Need more I/O pins, or a faster processor? That\'s where Arduino\'s like the Mega or the Due come into the picture.

### Arduino Mega: The Souped Up Uno

The [Arduino Mega](https://www.sparkfun.com/products/11061) is what you might get if you packed four Arduino Uno\'s into one board. There are **54 I/O pins**, instead of the 14 an Uno gives you. That\'s a whole lot of extra LEDs! Instead of one hardware serial port, there are four. And the Mega sports a whopping **256 kB of flash** program space. Not to mention 16 analog inputs, and 14 PWM outputs. The Mega just has more of everything.

[![Arduino Mega 2560 R3](https://cdn.sparkfun.com/r/600-600/assets/parts/6/4/3/3/11061-01.jpg)](https://www.sparkfun.com/arduino-mega-2560-r3.html)

### [Arduino Mega 2560 R3](https://www.sparkfun.com/arduino-mega-2560-r3.html) 

[ DEV-11061 ]

Arduino is an open-source physical computing platform based on a simple i/o board and a development environment that implemen...

[ [\$48.40] ]

The brain of the Mega is an ATmega2560, a fully souped up ATmega328. Aside from the massive processor overhaul, the Mega still shares a lot in common with the Arduino Uno. There\'s a secondary IC on-board (an ATmega16U2) to convert USB-to-serial to allow USB programming. It runs at the same speed \-- 16 MHz. All of the pins are broken out in a way that keeps the board shield-compatible. Because of these similarities, the Mega is a good option for Arduino beginners and experts alike.

If your Arduino project is hitting a wall because you don\'t have enough I/O, or if you\'re running out of program space, consider stepping up to the Mega.

### Arduino Due: Arduino Harder

You thought the Mega was powerful? The [Arduino Due](https://www.sparkfun.com/products/11589) is a revolutionary take on the Arduino platform. It sports an entirely different processor architecture \-- ARM instead of AVR. It\'s a 32-bit processor, clocks in at 84 MHz, and has native USB support.

[![Arduino Due](https://cdn.sparkfun.com/r/600-600/assets/parts/7/5/9/2/11589-01d.jpg)](https://www.sparkfun.com/products/11589)

### [Arduino Due](https://www.sparkfun.com/products/11589) 

[ DEV-11589 ]

The Due is Arduino\'s first ARM-based Arduino development board. This board is based on a powerful 32bit CortexM3 ARM microcon...

**Retired**

This thing sports many unique features that other boards don\'t have. Stuff like:

- Two **digital-to-analog converters** (DACs), which allow the board to output true analog values (instead of PWM). This means you can play audio out it!
- **USB on-the-go (OTG)** capability allows the Due to act as both a USB device and a host. So you can hook up other USB devices \-- like flash drives, WiFi modules, or phones \-- *to* the Due.
- **Direct Memory Access** (DMA) allows the microcontroller to offload memory-access tasks, so it can perform other operations at the same time.

There are also some new things to watch out for. The Due\'s processor \-- an ATSAM3X8E \-- can\'t work at 5V, so the board only runs at **3.3V** This means it may not be compatible with all shields.

The Due has some amazing functionality, but it\'s also a more **advanced** board. It\'s not recommended for beginners, but if you have a project that might take advantage of the Due\'s unique characteristics, check it out!

### Teensy

The Teensy line is a collection of microcontrollers from PJRC, based around several different powerful ICs. There is an option to use a Teensy with Arduino IDE if you install the Teensyduino add-on.

#### Teensy++2.0

The 8-bit Teensy++ 2.0 runs at 5V/16MHz and breaks out all of the I/O available on the AT90USB1286 to breadboard friendly 0.1\" spaced headers. The development board has 127kB of flash memory available for programming. There 46 digital I/O pins available with 8 analog inputs and 9 PWM outputs.

[![Teensy++ 2.0](https://cdn.sparkfun.com/r/600-600/assets/parts/8/0/2/5/11781-01.jpg)](https://www.sparkfun.com/products/11781)

### [Teensy++ 2.0](https://www.sparkfun.com/products/11781) 

[ DEV-11781 ]

The Teensy++ 2.0 breaks out all of the IO available on the AT90USB1286 to breadboard-friendly 0.1\" spaced headers so you can ...

**Retired**

To program, you would simply install the Teensyduino add-on for the Arduino IDE and upload via USB.

#### Teensy LC

The 32-bit Teensy LC runs at 3.3V/48MHz (with the exception of pin 17 which can output 5V for addressable LED strips). This board also makes the I/O available to breadboard friendly 0.1\' spaced headers. The development board has 62kB of flash memory available for programming. There are 27 I/O pins available with 13 analog inputs, and 10 PWM pins.

[![Teensy LC](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/5/7/1/13305-01.jpg)](https://www.sparkfun.com/products/13305)

### [Teensy LC](https://www.sparkfun.com/products/13305) 

[ DEV-13305 ]

The Teensy LC is a 32 bit microcontroller board that provides you with an uncomplicated option to get started with Teensy wit...

**Retired**

To program, you would simply install the Teensyduino add-on for the Arduino IDE and upload via USB.

#### Teensy 3.2

The 32-bit Teensy LC runs at 3.3V/72MHz but the I/O pins are 5V tolerant. This board also makes the I/O available to breadboard friendly 0.1\' spaced headers. The development board has 256kB of flash memory available for programming. There are 34 I/O pins available with 21 analog inputs, and 12 PWM pins.

[![Teensy 3.2](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/2/4/9/13736-01.jpg)](https://www.sparkfun.com/products/13736)

### [Teensy 3.2](https://www.sparkfun.com/products/13736) 

[ DEV-13736 ]

The Teensy 3.2 is a breadboard-friendly development board with loads of features in a, well, teensy package.

**Retired**

To program, you would simply install the Teensyduino add-on for the Arduino IDE and upload via USB.

### Arduino MKR Vidor 4000

The MKR Vidor 4000 is the first ever Arduino based on an FPGA chip with a SAMD21 microcontroller. It includes a WiFi, BLE, MIPI camera connector, micro HDMI, mini PCI express connector, I2C connector, LiPo Connector, and USB port. The board can perform high-speed digital audio and video processing.

[ ![Arduino MKR Vidor 4000](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/1/4/6/14870-Arduino_MKR_Vidor_4000-01.jpg) ]

### Arduino MKR Vidor 4000 

[ DEV-14870 ]

The Arduino MKR Vidor 4000 is highly configurable and powerful, and it can perform high-speed digital audio and video process...

**Retired**

The board operates at 3.3V and can be programmed with a USB cable.

## Internet of Things!

### SparkFun ESP8266 Thing

The ESP8266 Thing is a low cost microcontroller with built-in WiFi. By default, the board comes with a trace antenna but you could also connect an external antenna to the u.FL connector. The board breaks out the ESP8266 pins for development and includes a LiPo charge IC. Perfect for connecting your thing to the cloud. Best of all, there is an ESP8266 board add-on so that it can be used with the popular Arduino IDE.

[![SparkFun ESP8266 Thing](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/4/0/0/13231-01.jpg)](https://www.sparkfun.com/sparkfun-esp8266-thing.html)

### [SparkFun ESP8266 Thing](https://www.sparkfun.com/sparkfun-esp8266-thing.html) 

[ WRL-13231 ]

The SparkFun ESP8266 Thing is a breakout and development board for the ESP8266 WiFi SoC -- a leading platform for IoT or WiF...

[ [\$19.95] ]

While there are not as many I/O pins as the Arduino Uno (it has 11 I/O pins), it has a clock speed of **80MHz**, **512kB** of flash memory, and all pins can output a PWM at about 1kHz. You will need a 3.3V FTDI and cable to upload code to the board. Since the chip is **3.3V**, a logic level converter is required to connect any device higher than the system voltage. The board does not come populated with headers.

### SparkFun ESP8266 Thing Development Board

The ESP8266 Thing development board is basically the same as the original ESP8266 Thing. One difference is that there is no JST connector and LiPo charge circuit. Also, the development board comes populated with an FTDI to upload code and there is an option to include headers.

[![SparkFun ESP8266 Thing - Dev Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/1/9/7/13711-01.jpg)](https://www.sparkfun.com/sparkfun-esp8266-thing-dev-board.html)

### [SparkFun ESP8266 Thing - Dev Board](https://www.sparkfun.com/sparkfun-esp8266-thing-dev-board.html) 

[ WRL-13711 ]

The SparkFun ESP8266 Thing Dev Board is a development board that has been solely designed around the ESP8266, with an integra...

[ [\$19.95] ]

[![SparkFun ESP8266 Thing - Dev Board (with Headers)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/3/8/6/13804-01.jpg)](https://www.sparkfun.com/sparkfun-esp8266-thing-dev-board-with-headers.html)

### [SparkFun ESP8266 Thing - Dev Board (with Headers)](https://www.sparkfun.com/sparkfun-esp8266-thing-dev-board-with-headers.html) 

[ WRL-13804 ]

The SparkFun ESP8266 Thing Dev Board with Headers is a dev board that has been designed around the ESP8266, with an integrate...

[ [\$20.25] ]

### SparkFun Blynk Board (ESP8266)

Looking for an app with your ESP8266? The Blynk board was designed for mobile phones and includes the popular ESP8266. With the Blynk app, you can start building projects with the graphical interface by dragging and dropping widgets to control or monitor your thing!

[![SparkFun Blynk Board - ESP8266](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/3/6/4/13794-01a.jpg)](https://www.sparkfun.com/sparkfun-blynk-board-esp8266.html)

### [SparkFun Blynk Board - ESP8266](https://www.sparkfun.com/sparkfun-blynk-board-esp8266.html) 

[ WRL-13794 ]

The SparkFun Blynk Board is specially designed to work with the 'widgets' within the Blynk mobile app to create your next...

**Retired**

While the board was built for the Blynk app, the default firmware can be modified in the Arduino IDE. The board includes built-in trace antenna, FTDI, an addressable WS2812 RGB LED, Si7021 temperature and humidity sensor, and an analog-to-digital converter. The board does not come populated with headers. However, there is an option to use connect using alligator clips or the polarized connectors.

#### Arduino Ethernet

There are innumerable Arduino-compatible boards out there which make use of the ATmega328. Many, like the Arduino Pros, require an FTDI Basic to receive code, but they add on extra hardware to make them unique. The [Arduino Ethernet](https://www.sparkfun.com/products/11229), where the Arduino Uno and an [Ethernet Shield](https://www.sparkfun.com/products/9026) are smashed onto a single board, is a good example of this.

[![Arduino Ethernet w/o PoE](https://cdn.sparkfun.com/r/600-600/assets/parts/6/8/2/3/11229-01a.jpg)](https://www.sparkfun.com/products/11229)

### [Arduino Ethernet w/o PoE](https://www.sparkfun.com/products/11229) 

[ DEV-11229 ]

So you want your Arduino to surf the web but you don\'t have room for the Arduino board plus the Ethernet Shield. What do you ...

**Retired**

Pins 10, 11, 12 and 13 are reserved for interfacing with the Ethernet module and should not be used otherwise. This reduces the number of available pins to 9, with 4 available as PWM outputs. Operating voltage is **5V**; recommended input voltage range is **7-12V**. There\'s also an on-board microSD card reader for extra storage space!

### Arduino Industrial 101

The Arduino Industrial 101 is essentially a stripped down version of the Arduino Yún with an even smaller footprint than both the Yún and the Uno R3. It has an ATmega32u4 microcontroller integrated into the baseboard and the Atheros AR9331 microprocessor supports the LininoOS embedded Linux operating system. With almost half the board taken up by a module sporting a U.FL connector, not only does this board run Linux but it also operates over Wi-Fi!

[![Arduino Industrial 101](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/0/3/3/14134-01.jpg)](https://www.sparkfun.com/products/14134)

### [Arduino Industrial 101](https://www.sparkfun.com/products/14134) 

[ DEV-14134 ]

The Arduino Industrial 101 is a WiFi evaluation board for the Arduino 101 LGA module based on a MIPS Linux processor. With th...

**Retired**

There are 3 GPIOs (2 of which can be used as PWM Outputs), 4 Analog Inputs, 1 Ethernet signal on pin headers (no standard ethernet port!) and a built-in DC/DC converter. While the ATmega32u4 operates at 5V, the AR9331 and associated pins that are broken out operate at 3.3V. An on-board regulator provides the 3.3VDC supply for the AR9331 but be mindful of your connections. It is recommended to power the board via the micro-USB connection with 5VDC.

It has 16MB of flash memory which comes preloaded with the Linino OS; which allows you real-world connectivity to Linux hosted applications. By making a local connection and pointing your browser at the Industrial 101's configuration panel (default *192.168.240.1*), you can choose your Wi-Fi network and then use PuTTY or terminal to access the Linino OS command line.

You can upload your code either online or offline. With a built in CDC, no FTDI breakout is required for uploading code. This board does not come pre-populated with its headers so you\'ll need to do some soldering but it is absolutely worth it for your IoT projects!