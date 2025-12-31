# Source: https://learn.sparkfun.com/tutorials/touch-potentiometer-hookup-guide

## Introduction 

The [Touch Potentiometer](https://www.sparkfun.com/products/13144), or Touch Pot for short, is an intelligent, linear capacitive touch sensor that implements potentiometer functionality with 256 positions. It can operate as a peripheral to a computer, embedded microcontroller or in a stand-alone capacity. The Touch Potentiometer provides both a dual-channel analog and PWM output for direct control of other circuitry. Configurable analog and PWM transfer functions support a wide variety of applications.

[![SparkFun Touch Potentiometer](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/2/1/8/13144-02.jpg)](https://www.sparkfun.com/products/13144)

### [SparkFun Touch Potentiometer](https://www.sparkfun.com/products/13144) 

[ PRT-13144 ]

The SparkFun Touch Potentiometer, or Touch Pot for short, is an intelligent linear capacitive touch sensor that implements po...

**Retired**

**Note:** This product is a collaboration with [danjuliodesigns](http://danjuliodesigns.com/products/touch_pot/touch_pot.html). A portion of each sales goes back to them for product support and continued development.

------------------------------------------------------------------------

### Recommended Materials

This tutorial will go over numerous examples of how to us the Touch Potentiometer. The materials needed to follow along with each example will be listed at the beginning of that example\'s section.

### Suggested Reading/Viewing

First and foremost, Dan Julio of danjuliodesigns has written an amazing user manual for the Touch Potentiometer. Most of the information you need to know about the Touch Pot can be found in that document including maximum power ratings, dimensional drawing, and very detailed operational instructions. You can download the manual via the link below or you can always grab the most up-to-date version from [his website](http://danjuliodesigns.com/products/touch_pot/touch_pot.html).

[Touch Potentiometer User Manual](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/touch_pot_sf_1_4.pdf)

To better understand the Touch Potentiometer and how it functions, it will help to have a good understanding of the following concepts. If there\'s any you are unfamiliar with, visit the corresponding tutorial first, then head on back.

- [Resistors](https://learn.sparkfun.com/tutorials/resistors) - The section on [potentiometers](https://learn.sparkfun.com/tutorials/resistors/types-of-resistors#pot) is of particular interest.
- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication) - The Touch Pot uses Serial Communication to talk to the utility used to configure the board.
- [I2C](https://learn.sparkfun.com/tutorials/i2c) - The Touch Pot uses I2C Communication to communicate with embedded microcontrollers or with other Touch Pots on the bus.
- [Pulse-width Modulation](https://learn.sparkfun.com/tutorials/pulse-width-modulation) - The Touch Pot has a PWM output for interfacing with lighting systems or other controllers that accept PWM inputs.
- [Hexadecimal](https://learn.sparkfun.com/tutorials/hexadecimal) and [Binary](https://learn.sparkfun.com/tutorials/binary) are used a lot when diving in to the operation of the Touch pot.
- The Touch Pot relies on [Capacitive Sensing](http://en.wikipedia.org/wiki/Capacitive_sensing) to detect changes to its current setting. Check out the video below for a detailed breakdown of how Cap Sensing works and different methods of detecting cap sense.

## Board Overview

There are several different ways to interface to the Touch Potentiometer. This section will briefly cover each of these methods. Most of this information can be found in the [user manual](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/touch_pot_sf_1_4.pdf).

[![Board Overview](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Overview.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Overview.png)

### Digital I/O

The Touch Potentiometer Digital IO connections consist of the VIN and Ground power signals for the micro-controller and digital portion of the AD5262, a TTL-level serial interface, an I^2^C interface, and the PWM output. The Touch Potentiometer communicates to a host device using TTL-level serial interface or an I^2^C interface. Both interfaces are active simultaneously. The serial interface operates at 9600 baud. The I^2^C interfaces is a 7-bit slave with a maximum clock rate of 100 kHz. It does not support General Call or 10-bit addressing.

  Pin Label   Function
  ----------- -------------------------------
  GND         Ground
  VIN         +5-12 Volt power input
  SDA         I^2^C SDA (Data)
  SCL         I^2^C SCL (Clock)
  RX          Serial TTL RX Input
  TX          Serial TTL TX Output
  PWM         Pulse-width Modulation Output

#### Power

The Touch Pot has a 5V LDO voltage regulator (Vreg) to allow the board to be powered from external sources that are larger than 5V (great for lighting and audio systems that require 9-12V). The VIN pin can be powered with **any voltage between 4.6-12V**. The datasheet for the Vreg can be found [here](http://www.micrel.com/_PDF/mic5205.pdf).

**Important Note about Power Supplies**\
\
The capacitive sensors may be adversely affected by electrical noise. They are sensitive to 50 and 60-Hz energy that may be coupled through power supplies with inadequate line filtering or configurations with a ground loop (for example, a system that has a DC power supply and is also connected to a computer with its own power supply). It may be necessary to include an AC line filter in front of some cheap switch-mode power supplies to eliminate ground loop conditions.

#### Serial Communication

A computer with a USB interface and terminal emulator program can access the Touch Potentiometer using the [serial interface](https://learn.sparkfun.com/tutorials/serial-communication) connected to a USB-to-serial device like a [FTDI Basic Breakout Board](https://www.sparkfun.com/products/9716) or a micro-controller like the [5V Pro Micro](https://www.sparkfun.com/products/12640) that has both a USB interface with Communications Device Class (CDC) support and a serial port. The Touch Potentiometer serial interface operates at 5V logic levels with a data rate of 9600 baud, eight data bits, no parity and one stop bit (8N1).

### I^2^C Communication

The Touch Pot communicates over [I^2^C](https://learn.sparkfun.com/tutorials/i2c) just as any other I^2^C sensor would. It supports 7-bit addressing and a maximum transfer rate of 100 kHz. It may be connected to a 5V Arduino I^2^C peripheral (A4/A5) directly. Level translators should be used for 3.3V Arduino boards (or other 3.3V micro-controllers). The Touch Potentiometer activates weak pull-ups on its I^2^C signals, so pull-up resistors are not necessary for short connections (a few inches). Pull-up resistor values of 4.7kΩ to 10kΩ may be used.

The **default I^2^C address is 0x08**. There are **64 available I2C addresses**. The Touch Pot uses two consecutive I2C addresses, which is why only 64 are available. Details on changing that address in the utility app and on the fly will discussed later in the tutorial.

#### Pulse-width Modulation

The PWM output generates a signal with a duty-cycle that is proportional to the current Touch Potentiometer value. A value of zero results in a PWM output of 0% duty cycle (off). A value of 255 (full-scale) results in a PWM output of nearly 100% duty cycle (on).

### Analog I/O

The Touch Potentiometer Analog IO signals consist of the \[AD5262\] wiper and wiper power supply signals. The AD5262 supports two separate digital 20kΩ potentiometers, each with two terminals and a wiper connection. They have their own power supply connections allowing the voltage levels on the potentiometers to exceed the +5 volt logic power supply (see important note below).

Pin Label

Function

A1, A2

A Terminals for potentiometer 1 and 2

W1, W2

Wiper Terminals for potentiometer 1 and 2

B1, B2

B Terminals for potentiometer 1 and 2

V+

Positive Power Supply. Connected at the factory to the 5V logic signal by jumper J1. With J1 removed this may be connected to a positive voltage up to 15V. Note the sum of \|V-\| + \|V+\| must be 15V or less.

V-

Negative Power Supply. Connected at the factory to ground by jumper J2. With J2 removed this may be connected to a negative voltage down to -5V. Note the sum of \|V-\| + \|V+\| must be 15V or less.

**Current Limitations:** The maximum amount of current allowed through the A or B to W pins is 5mA continuous, 20 mA intermittent.

**Important Notes about V+ and V-**\
\
Care must be taken with V+ and V- to prevent damage to the ICs on the Touch Potentiometer.\
\
1. V+ and V- must always be connected to power and should be powered before or at the same time voltages appear on the A, B and W signals and 5V input.\
\
2. By default, V+ is connected to 5V with jumper J1 and V- is connected to ground with jumper J2. Voltages on the A, B and W signals should not exceed the range of 0 - 5V with these jumpers installed. Remove these jumpers by removing the solder blob if a different power supply will be connected to V+ and/or V-.\
\
3. The maximum voltage potential between V- and V+ is 15 volts. V- maximum is -5V. V+ maximum is 15V.\
\
4. Electrical noise on V- and V+ may be coupled into the signal passing through the potentiometer. A power supply connected to V- and V+ may require additional filtering to eliminate this noise.

### Calibration/Configuration Button

The Touch Pot has a button located on the backside that allows the user to change both the I^2^C address on the fly as well as calibrate the capacitive touch sensor on the fly. As indicated by the silkscreen near the button, three rapid, successive presses will enter I^2^C address change mode, and four presses will start the calibration process. The presses have to be complete within 2 seconds, or they are ignored

## Touch Pot Utility App

Dan Julio has created a desktop application that communicates with the Touch Pot over a serial connection. From this utility app you can change configuration settings, alter LED behavior, calibrate the capacitive touch sensor, view current readings in jabber mode, and much more.

You can [download the utility](http://www.danjuliodesigns.com/products/touch_pot/touch_pot/tputil.html), known as **tputil**, from danjuliodesigns.com. Versions for Windows, Mac and Linux are all available.

In order to communicate between the Touch Pot and tputil, you\'ll need to create a serial connection. The easiest way to do this is to solder some headers onto the Touch Pot. You\'ll need some form of TTL-to-USB converter such as our [USB to TTL Serial Cable](https://www.sparkfun.com/products/12977) or something like an [FTDI Basic](https://www.sparkfun.com/products/9716) with some [male-to-female jumper wires](https://www.sparkfun.com/products/9140).

Make your connections as follows:

  TTL-to_USB Device   Touch Potentiometer
  ------------------- ---------------------
  GND                 GND
  VCC                 VIN
  TX                  RX
  RX                  TX

[![USB to TTL Cable in action](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-12.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-12.jpg)

*Touch Potentiometer connected to computer via a USB to TTL Serial Cable. (Note: the logic levels on this cable are 3.3V but work well enough.)*

Once the Touch Pot is connected, open the tputil. Select the correct [serial port](https://learn.sparkfun.com/tutorials/terminal-basics/basic-terminology-), and click connect. Once connected, you can alter a variety of settings for the Touch Pot.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Screen_Shot_2015-10-22_at_2.40.33_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Screen_Shot_2015-10-22_at_2.40.33_PM.png)

Checking the Jabber check box will display the current value of the senor. Sliding your finger along the sensor will change this value in real time. Other setting such as LED behavior can be altered here. The PWM output can be set to linear or non-linear for lighting systems. The analog output can be set to Log instead of Linear for audio systems.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/utility2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/utility2.png)

The Configure tab offers lots of options such as calibration of the cap sense, factory reset, changing the I^2^C address, and getting the current EEPROM and sensor values.

More details about the functionality that the utility app provides access to can be found under the [Operation section](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/touch_pot_sf_1_4.pdf#page=21) of the User Manual.

## Example 1: PWM Lighting Controller

This example will demonstrate how to use the PWM output on the Touch Potentiometer to control an LED lighting system.

Many LED lighting systems use constant current power supplies, such as our [PicoBuck](https://www.sparkfun.com/products/11850) and [FemtoBuck](https://www.sparkfun.com/products/12937) LED Drivers. These drivers usually have a PWM input, allowing you to fade the LEDs on or off. The best part: there is no programming necessary.

### Hardware Hookup

Before making any connections, you\'ll need to decide how you want your lighting system to behave. The PicoBuck has three, independently-controlled channels capable of handling PWM signals, whereas the FemtoBuck has only one channel and one PWM input. For this example, all three inputs on a PicoBuck were tied together so that all three channels would fade in unison. You can leave each channel separate, which is great for RGB color blending systems, but you\'ll need a Touch Pot for each individual channel in that scenario or a way to switch between channels.

The Touch Pot works best as a lighting dimmer control when the PWM output set to **Non-linear**. This can be accomplished in the tputil app mentioned in the previous section.

Connecting the Touch Pot to the PicoBuck only requires two wires. Ground needs to connect to ground on the opposite board. The PWM output pin on the Touch Pot connects to the three input pins on the PicoBuck (IN1, IN2, and IN3) that are tied together, as mentioned above.

[![Touch Pot and PicoBuck](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-11.jpg)

Here is a wiring diagram showing how this would look with a FemtoBuck. The same would apply to the PicoBuck; just tie the three PWM pins together.

[![Touch Potentiometer with the Pico Buck and High Power LEDs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/8/TouchPotPicoBuckFritzing.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/TouchPotPicoBuckFritzing.png)

*Note: You could also power the Touch Pot with the 12V supply, since it has the 5V LDO regulator on it. However, if you\'re powering you\'re LEDs with more than 12V, you\'ll need the secondary 5V-12V supply for the Touch Pot.*

Last, you\'ll need to power both the Touch Pot and the Constant Current Driver. The Driver will accept voltages up to 36V, but **12V** will be more common. You will also need to power the Touch Pot with **5V**. You can use two separate power supplies, such as a [5V](https://www.sparkfun.com/products/12889) and [12V](https://www.sparkfun.com/products/9442) wall adapter, or you can find a dual-voltage supply. We offer a [12V/5V power supply (TOL-15664)](https://www.sparkfun.com/products/15664). For a more robust lighting system, you can also get a decent power supply such as a [Meanwell](https://www.sparkfun.com/categories/tags/mean-well). Just make sure to connect the circuit appropriate voltages.

**Warning!** Depending on the manufacturer, dual-voltage power supplies can lack proper filtering and tends to wreak havoc on the Touch Potentiometer. We saw this with our previous [12V/5V power supply (TOL-11296)](https://www.sparkfun.com/products/retired/11296). However, we **DO NOT** recommend using the older power supply with the Touch Potentiometer.

Once everything is connected, you should be able to apply power to the Touch Pot and the LED Driver. Everything should power on, and the Touch Pot should start in the \'off\' position. Run your finger along the capacitive touch strip, and watch the LEDs fade on and off.

[![LEDs on Actobotics Channel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-10.jpg)

You can read more about the PWM capabilities of the [Touch Pot in the user manual on page 15](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/touch_pot_sf_1_4.pdf#page=15).

[Capacitive Touch Potentiometer User Manual (pg 15)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/touch_pot_sf_1_4.pdf#page=15)

## Example 2: Analog Volume Controller

The next example will show how to use the Analog Potentiometer functionality of the Touch Pot to control both the left and right volume for an audio amplifier. This example will be using the [SparkFun Audio Amplifier Kit](https://www.sparkfun.com/products/9612). The same hookup could be used with the [SparkFun Mono Audio Amp Breakout](https://www.sparkfun.com/products/11044) as well.

### Hardware Hookup

If you have not done so already, you\'ll need to [build the Audio Amp Kit](http://cdn.sparkfun.com/datasheets/Kits/SFE03-0010-KitCard-AudioAmp-ReadersSpreads_03.pdf). Be sure to **omit the two PTH Potentiometers** included in the kit.

The analog transfer function of the Touch Pot can be set to **Logarithmic** for a more realistic volume control **Non-linear**. This can be accomplished in the tputil app mentioned previously.

Next, connect the Analog Potentiometer pins on the Touch Pot to the Audio Amp pins where the PTH potentiometers would have been. There are two channel, each consisting of an A, W and B. We\'ll consider A as \'+\', W as Wiper and B as \'-\'. One the PCB, these inputs map like this:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/AudioAmpTouchPot.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/AudioAmpTouchPot.png)

Here is a look at the underside of the connections.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-06.jpg)

And from the top\...

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-04.jpg)

Once both volume channels are connected, we\'ll need to provide power to the Amp and the Touch Pot. Since the Touch Pot has a 5V LDO voltage regulator, we can use the same power supply to power both the Amp and the Touch Pot. A supply between the range of 9V-12V should be used to power both. Power routed from the input can be seen in the image below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-05.jpg)

Last, you\'ll need to connect some wires for audio in and audio out. This can be achieved several different ways. The speakers can be attached directly to the amp, or an audio output cable can be attached, as was the case in our example. You can use an [audio input cable](https://www.sparkfun.com/products/11580) on the input side. This allows for phones, MP3 players and other 3.5mm jack-type devices to play music through this setup.

With everything connected, apply power. You should see the Amp and the Touch Pot power on. Connect a speaker and an audio source, play some tunes and use the Touch Pot to control the volume!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-03.jpg)

*Complete Audio setup.*

You can read more about the analog output capabilities in the [User Manual](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/touch_pot_sf_1_4.pdf#page=20).

## Example 3: Interfacing with Microcontrollers 

The first two examples showed how you can use the Touch Pot right out of the box, no programming necessary. This example will show you how to connect the Touch Pot to a microcontroller. It will also cover how to add more than one Touch Pot to an I^2^C bus. For an example of interfacing the Touch Pot to a computer over serial, visit the [User Manual](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/touch_pot_sf_1_4.pdf#page=16)

### Hardware Hookup

This example uses a [Pro Micro 5V](https://www.sparkfun.com/products/12640) to communicate with the Touch Pot over I^2^C. The connections between the two are as follows:

[![Fritzing Image](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/8/ProMicroTouchPot.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/ProMicroTouchPot.png)

You should end up with something that looks like this:

[![Pro MIcro Touch Pot Powered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-01.jpg)

*Note: The white and blue wires are connected to the serial interface to allow the Pro Micro to talk to the tputil as well using a different sketch, [tp_test_sketch](http://danjuliodesigns.com/products/touch_pot/assets/tp_test_sketch.zip), found on [danjuliodesign.com](http://danjuliodesigns.com/products/touch_pot/touch_pot.html).*

If you have not used a Pro Micro before, you should visit the [Hookup Guide](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide). In particular, you\'ll need to install some additional drivers and add the board definitions for the Pro Micro to the Arduino IDE. The Hookup guide covers this for both [Windows](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide#installing-windows) and [Mac and Linux](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide#installing-mac--linux) users. Alternatively, you could use any microcontroller that has I^2^C and Serial communications.

Once the Pro Micro is setup in the Arduino IDE, select the correct board (Pro Micro) and serial port.

[![board selection](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Pro_MIcro.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Pro_MIcro.png)

Then, upload the following code to the Pro Micro:

    language:c
    /*
     * Simple Touch Potentiometer Example with Arduino
     *
     * Reads the pot value and controls the brightness of the Arduino LED on
     * Digital Pin 13.  Also logs new values to the serial port.  Utilizes
     * both the direct and indirect command interface forms.
     *
     * Assumes Touch Pot is at I2C Address 8
     *
     * Released into the public domain by Dan Julio.  This software is supplied on an as-is 
     * basis and no warranty as to its suitability for any particular purpose is either made
     * or implied.  danjuliodesigns, LLC. will not accept any claim for damages howsoever
     * arising as a result of use or failure of this software.
     */
    #include "Wire.h"

    int i2cAddr = 8; // Direct access at i2cAddr, indirect registers at i2cAddr+1

    uint8_t prevValue;
    uint8_t curValue;

    void setup() 

    void loop() 
    }

    // Write a Touch Potentiometer register
    void WriteTpReg(uint8_t addr, uint8_t data) 

    // Get the Touch Potentiometer value
    uint8_t ReadTpValue()  else 
    }

    // Read a Touch Potentiometer register
    uint8_t ReadTpReg(uint8_t addr)  else 
    }

Once that is uploaded, open your favorite [Serial Terminal](https://learn.sparkfun.com/tutorials/terminal-basics) at 115200 baud. As you slide your finger along the capacitive touch strip ion the Touch Pot, you should see the current PWM value print out on the terminal.

[![Serial Terminal Print out](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/ProMicroScreen.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/ProMicroScreen.png)

### Multiple Touch Potentiometers

Building on this same example, we can add a second Touch Pot to the I^2^C bus. You can use the SMD pads found on the back of the Touch Pot to solder a second Touch Pot to the first.

[![2 Touch Pots](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-09.jpg)

In order for this to work, you\'ll need to change the I^2^C address on one of the Touch Pots. This can be accomplished through the TP Utility app, or it can be changed on the fly by pressing the button on the back of the Touch Pot three times.

You will see the all the LEDs on the Touch Pot blink three times, indicating you are in address change mode. As you slide your finger along the sensor, the LEDs will change. They are telling you the address in [binary](https://learn.sparkfun.com/tutorials/binary). Holding the Touch Pot sideways, with the PTH holes on the left, you will see every combination of numbers between 0b01 and 0b64.

You can repeat this process adding up to 64 Touch Pots on a single I^2^C bus.

More information on interfacing to microcontrollers through the I^2^C port can be found in the [User Manual](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/8/touch_pot_sf_1_4.pdf#page=17).