# Source: https://learn.sparkfun.com/tutorials/qwiic-twist-hookup-guide

## Introduction

Sometimes you just need a volume knob. The [Qwiic Twist](https://www.sparkfun.com/products/15083) is a digital RGB encoder, also known as a continuously rotating knob that is read and controlled over I^2^C.

[![SparkFun Qwiic Twist - RGB Rotary Encoder Breakout](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/4/3/3/15083-SparkFun_Qwiic_Twist_-_RGB_Rotary_Encoder_Breakout-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-twist-rgb-rotary-encoder-breakout.html)

### [SparkFun Qwiic Twist - RGB Rotary Encoder Breakout](https://www.sparkfun.com/sparkfun-qwiic-twist-rgb-rotary-encoder-breakout.html) 

[ DEV-15083 ]

The SparkFun Qwiic Twist is a digital RGB rotary encoder breakout that is also able to connect to our Qwiic Connect System.

[ [\$25.50] ]

What does that mean? Send the command `twist.getCount()` and you'll get the number of steps the user has twisted the knob. For example, 312 or -23 depending on the direction and amount the user and turned the knob. The Twist takes care of all the various interrupts, switches, PWM\'ing of LEDs and presents all those features over an easy-to-use I^2^C interface. The Qwiic Twist was designed to get rid of the large mass of wires that are needed to implement an RGB encoder in a breadboard. Now you can get encoder position with something as twist.getCount(); and your microcontroller can keep focused on other more important tasks.

The Qwiic Twist has an indent type encoder which gives the user a great \'clicky\' feel as they turn. The Qwiic Twist also has an RGB LED and a built-in button. We've written an Arduino library to make controlling these features as easy as:

    language:c
    twist.setColor(255, 0, 0); //Red
    if(twist.isPressed() == true) Serial.println(“Pressed!”);

And finally, the I^2^C address of Qwiic Twist is software configurable which means you can hookup over 100 Twists on a single I^2^C bus!

[![Four SparkFun Qwiic Twists connected](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/6/Qwiic_Twist_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic_Twist_Hookup_Guide-01.jpg)

### Required Materials

To follow along with this hookup guide, you will need one of the following Qwiic shields with an Arduino. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![SparkFun Qwiic Shield for Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/3/14352-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html)

### [SparkFun Qwiic Shield for Arduino](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html) 

[ DEV-14352 ]

The SparkFun Qwiic Shield is an easy-to-assemble board that provides a simple way to incorporate the Qwiic Connect System wit...

[ [\$7.75] ]

**Note:** Originally, a BlackBoard was used in the tutorial. If you are looking to reduce the cost and avoid soldering headers to the Qwiic shield, try taking a look at the RedBoard Qwiic. It is essentially a RedBoard with Qwiic connector.\
\

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

You will also need a Qwiic cable to connect the shield to your Twist, choose a length that suits your needs. The Qwiic to breadboard cable is good if you want to easily plug the Qwiic Twist into a 3.3V platform such as [Teensy](https://www.sparkfun.com/categories/267).

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - Breadboard Jumper (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/1/14425-Qwiic_Cable_-_Breadboard_Jumper__4-pin_-01.jpg)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html)

### [Qwiic Cable - Breadboard Jumper (4-pin)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html) 

[ PRT-14425 ]

This is a jumper adapter cable that comes pre-terminated with a female Qwiic JST connector on one end and a breadboard hookup...

**Retired**

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

**Retired**

[![Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/4/14428-Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/products/14428)

### [Qwiic Cable - 200mm](https://www.sparkfun.com/products/14428) 

[ PRT-14428 ]

This is a 200mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/5/14429-Qwiic_Cable_-_500mm-01.jpg)](https://www.sparkfun.com/products/14429)

### [Qwiic Cable - 500mm](https://www.sparkfun.com/products/14429) 

[ PRT-14429 ]

This is a 500mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

### Tools

The Qwiic Twist is designed to be easily connected to a [Qwiic bus](https://www.sparkfun.com/qwiic) without soldering. But if you choose to connect to the I^2^C pins directly you may need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

Additionally, we've got a great video on how the inner workings of encoders work and why they're important.

## Hardware Overview

The RGB encoder is a 24 indent encoder. You'll *feel* 24 clicks when turning one 360 degree rotation.

[![The RGB encoder on the Qwiic Twist](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/SparkFun-Qwiic-Twist.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/SparkFun-Qwiic-Twist.jpg)

The encoder works best with the [Clear Plastic Knob](https://www.sparkfun.com/products/10597) but is compatible with any knob with a 6mm knurled hole. The encoder output is filtered through a series of resistors, capacitors, and error checked in software to be sure the accurate number of ticks is being output.

[![Qwiic Twist with Clear Knob lit up purple](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic_Twist_PurpleKnob.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic_Twist_PurpleKnob.jpg)

The encoder has an RGB LED built into it. To get the full light effect we recommend a clear knob but depending on your setup you may also be able to get a 'backlit' effect with an opaque knob. The RGB LEDs are pulse-width-modulated and controlled via software (and backed by non-volatile memory) so you can tell the Qwiic Twist to go to any color you want and it will be that color now and even after the Twist is power cycled (it remembers the last color setting).

The encoder has a built-in momentary button. This is useful for selecting menu items and getting general feedback from the user.

### Qwiic I^2^C Pins

[![Qwiic Twist connected to a BlackBoard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/6/Qwiic_Twist_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic_Twist_Hookup_Guide-02.jpg)

The Qwiic Twist is best used with the Qwiic system. Simply plug a [Qwiic Cable](https://www.sparkfun.com/products/14426) into the Twist and start talking to it.

[![I2C pins on the Qwiic Twist highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/SparkFun-Qwiic-Twist-I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/SparkFun-Qwiic-Twist-I2C.jpg)

Alternatively you can solder to the I^2^C pins on the board.

[] **Heads Up!** The Qwiic Twist is designed to operate at **3.3V** so please don't drive it at **5V**. Your I^2^C pins, however, can be **5V** logic.

### RST and INT

The reset pin is an active low input. When pulled low Qwiic Twist will be held in reset.

[![RST and INT pins on the digital RGB encoder highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic-Twist-ADR-INT-2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic-Twist-ADR-INT-2.jpg)

The INT pin is active low and is open drain output. The interrupt pin will go low when any of the follow events happen:

- The user presses the button is pressed or released.
- The user has turned the knob and no movement has been detected for a certain amount of time. This amount of time is called the *turnInterruptTimeout* and is 250ms by default. This means that once the user has stopped turning the knob for 250ms the interrupt will fire. This is helpful when the user is doing lots of knob changes. The Qwiic Twist won\'t fire the interrupt until the user has stopped fidgeting. The turnInterruptTimeout is software configurable from 1ms to 65000ms (65 seconds).

The INT pin is open drain and is pulled up through a 10k resistor but if you want to connect multiple Twists and share the interrupt pins among many Twists then you can optionally cut the jumper to remove the 10k pull up on each Twist board.

### Jumpers

The ADR jumper is normally open and controls the I^2^C address of the device. By default the Qwiic Twist 7-bit unshifted address is `0x3F`. If the jumper is closed with solder, the address will become `0x3E`.

[![Address jumper of the Qwiic Twist](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic-Twist-Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic-Twist-Jumpers.jpg)

The Twist is unique in that it can have any address assigned to it between 0x08 and 0x77. This means over 100 Twists can be connected on a single bus!

**Note:** If the ADR jumper is closed then Qwiic Twist will resort to address `0x3E` regardless of what address may have been configured via software commands. This is a safety mechanism in case the Twist gets set to an unknown address.

The INT jumper is a normally closed jumper; there is a small trace connecting the two pads. This jumper connects the INT pin on the ATtiny84 through a 10k resistor to **3.3V**. Cutting the small trace disconnects the 10k resistor from the INT pin on the ATtiny84.

[![Qwiic INT jumper closed with trace](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic-Twist-Jumpers-INTHighlightedFixed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic-Twist-Jumpers-INTHighlightedFixed.jpg)

The INT pin on Qwiic Twist is *open drain*, meaning the pin will actively go low when an interrupt occurs but will then float when there is no interrupt. This *open drain* type of setup is handy if you have multiple devices sharing a single interrupt line. For advanced applications (such as many many Twists all sharing the same INT pin) you may want to [cut this jumper](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces) on each Twist to remove the 10k pull ups. **For general use you can leave this jumper unmodified.**

The Qwiic Twist has built-in 2.2k pull-up resistors on the SDA and SCL lines. These are needed for normal I^2^C communication. The I^2^C jumper has two small traces connecting the pull-ups to 3.3V. **For general use you can leave this jumper unmodified.** If you have many (over 7) devices on the I^2^C bus, each with their own pull up resistors, then you may want to [cut the I^2^C jumpers](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces) to disconnect the 2.2k resistors on each Qwiic board.

## Qwiic Twist Arduino Library

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

We've written an easy to use Arduino library that covers the gamut of features on the Qwiic Twist. The easiest way to install the library is by searching **SparkFun Twist** within the Arduino library manager. We've even got a tutorial on [installing an Arduino library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library/all) if you need it. You can also manually install the [Qwiic Twist library](https://github.com/sparkfun/SparkFun_Qwiic_Twist_Arduino_Library) by downloading a zip:

[Download the SparkFun Qwiic Twist Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_Twist_Arduino_Library/archive/master.zip)

- **Example 1** - Basic reading of the encoder value
- **Example 2** - Set the Knob Color
- **Example 3** - Displaying Crazy Colors on Knob
- **Example 4** - Connect Colors: Change knob color from blue to red based on position
- **Example 5** - Reading Time Stamps
- **Example 6** - Display encoder difference since last reading
- **Example 7** - Set the encoder count value
- **Example 8** - Enabling and reading interrupts
- **Example 7** - Set the encoder count value
- **Example 9** - Change the I^2^C address
- **Example 10** - Advanced Wire settings

Below are the various functions that can be called from the library. Most of these functions are demonstrated in the examples so we recommend you go through each example first.

- **`boolean begin(TwoWire &wirePort, uint8_t deviceAddress);`**
- **`int16_t getCount();`** \-- Returns the number of indents the user has turned the knob
- **`boolean setCount(int16_t amount);`** \-- Set the number of indents to a given amount
- **`int16_t getDiff(boolean clearValue = true);`** \-- Returns the number of ticks since last check. Clears the difference once read.
- **`boolean isMoved();`** \-- Returns true if knob has been twisted
- **`boolean isPressed();`** \-- Return true if button is currently pressed.
- **`boolean isClicked();`** \-- Returns true if a click event has occurred. Event flag is then reset.
- **`uint16_t timeSinceLastMovement(boolean clearValue = true);`** \-- Returns the number of milliseconds since the last encoder movement. Clears value once read.
- **`uint16_t timeSinceLastPress(boolean clearValue = true);`** \-- Returns the number of milliseconds since the last button event (press and release). Clears value once read.

**Color** functions set the brightness of each LED.

- **`boolean setColor(uint8_t red, uint8_t green, uint8_t blue);`** \-- Sets the color of the encoder LEDs, 0-255
- **`boolean setRed(uint8_t);`** \-- Set the red LED, 0-255
- **`boolean setGreen(uint8_t);`** \-- Set the green LED, 0-255
- **`boolean setBlue(uint8_t);`** \-- Set the blue LED, 0-255
- **`uint8_t getRed();`** \-- Get current value
- **`uint8_t getGreen();`** \-- Get current value
- **`uint8_t getBlue();`** \-- Get current value

**Connect** functions set the relation between each color and the twisting of the knob. These functions connect the LED so it changes \[amount\] with each encoder tick without the master intervening. Negative numbers are allowed (so LED gets brighter the more you turn the encoder down).

- **`boolean connectColor(int16_t red, int16_t green, int16_t blue);`** \-- Connect all colors in one command
- **`boolean connectRed(int16_t);`** \-- Connect individual colors
- **`boolean connectGreen(int16_t);`** \-- Connect individual colors
- **`boolean connectBlue(int16_t);`** \-- Connect individual colors
- **`int16_t getRedConnect();`** \-- Get the connect value for each color
- **`int16_t getGreenConnect();`**
- **`int16_t getBlueConnect();`**

**General** functions get and set various aspects of the Twist.

- **`uint16_t getIntTimeout();`** \-- Get number of milliseconds that must elapse between end of knob turning and interrupt firing
- **`boolean setIntTimeout(uint16_t timeout);`** \-- Set number of milliseconds that elapse between end of knob turning and interrupt firing
- **`void clearInterrupts();`** \-- Clears the moved and button interrupts as well as the pressed and clicked event bits
- **`boolean isConnected();`** \-- Returns true if sensor is detected
- **`uint16_t getVersion();`** \-- Returns a two byte firmware version
- **`void changeAddress(uint8_t newAddress);`** \-- Change the I^2^C address to newAddress

## Register Map

If you'd like to use a platform other than Arduino you can easily control Qwiic Twist by accessing the following set of registers:

[![The Qwiic Twist set of registers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/6/Qwiic_Twist_Register_Map_-_Endianness_Fixed_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic_Twist_Register_Map_-_Endianness_Fixed_.jpg)

*You can also download the [PDF](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic_Twist_Register_Map_-_Fixed_Endianness.pdf).*

The Qwiic Twist behaves as a normal I^2^C peripheral. First write the address of the register you would like to read or write, then follow that I^2^C command with a Read to read the given register or a Write and a data byte to write to a register. The register address pointer is auto-incrementing so you can read and write multiple registers at a time.

## Connecting Colors

One of the more advanced (but really handy) features of Qwiic Twist is the ability to connect the color control to the knob movement. What this means is that you can have the red LED brightness increase or decrease as the user turns the knob without sending commands to the Qwiic Twist. This greatly increases the responsiveness of the knob illumination and dramatically reduces I^2^C traffic.

[![Qwiic Twist changing color by just twisting](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic_Twist-Color-Connect.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/6/Qwiic_Twist-Color-Connect.gif)

In the above photo we have connected blue to increase brightness by 10 for every tick increment, and connected red to -10 per tick. The color changes automatically without the need for intervention from the I^2^C master. The color connect values are stored in the Qwiic Twist and will be loaded after each power-on.

See **[Example4](https://github.com/sparkfun/SparkFun_Qwiic_Twist_Arduino_Library/blob/master/examples/Example4_ConnectColors/Example4_ConnectColors.ino)** of the SparkFun library for a full demonstration.