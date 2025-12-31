# Source: https://learn.sparkfun.com/tutorials/qwiic-mp3-trigger-hookup-guide

## Introduction

Sometimes you just need to play an MP3 file. Whether it\'s a sound track as you enter the room or a pirate cackling when a dollar [gets donated](https://github.com/nseidle/Money_Vacuum) to the kid\'s museum. The [Qwiic MP3 Trigger](https://www.sparkfun.com/products/15165) takes care of all the necessary bits, all you need to do is send a simple I^2^C command and listen.

[![SparkFun Qwiic MP3 Trigger](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/6/3/1/15165-SparkFun_Qwiic_MP3_Trigger-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-mp3-trigger-dev-19030.html)

### [SparkFun Qwiic MP3 Trigger](https://www.sparkfun.com/sparkfun-qwiic-mp3-trigger-dev-19030.html) 

[ DEV-19030 ]

The SparkFun Qwiic MP3 Trigger takes care of all the necessary requirements for playing sound files, all you need to do is se...

**Retired**

### Required Materials

The Qwiic MP3 Trigger does need a few additional items for you to get started, shown below. However, you may already have a few of these items, so feel free to modify your cart as necessary.

[![Hamburger Mini Speaker](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/3/1/14023-01.jpg)](https://www.sparkfun.com/hamburger-mini-speaker.html)

### [Hamburger Mini Speaker](https://www.sparkfun.com/hamburger-mini-speaker.html) 

[ COM-14023 ]

This will be a treat for your ears! The Hamburger Mini Speaker is a 3W economical speaker option for any project needing stan...

[ [\$7.95] ]

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![USB Wall Charger - 5V, 1A (Black)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/3/1/0/11456-USB_Wall_Charger_-_5V__1A__Black_-01.jpg)](https://www.sparkfun.com/usb-wall-charger-5v-1a-black.html)

### [USB Wall Charger - 5V, 1A (Black)](https://www.sparkfun.com/usb-wall-charger-5v-1a-black.html) 

[ TOL-11456 ]

USB is being implemented as a power connection standard more and more these days, but you don\'t always have a computer on han...

[ [\$5.95] ]

[![microSD Card - 1GB (Class 4)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/7/0/15107-microSD_Card_-_1GB__Class_4_-01.jpg)](https://www.sparkfun.com/microsd-card-1gb-class-4.html)

### [microSD Card - 1GB (Class 4)](https://www.sparkfun.com/microsd-card-1gb-class-4.html) 

[ COM-15107 ]

For the times when all you need is a basic SD card this is the card for you. 1GB capacity is plenty to store MP3s or log envi...

[ [\$5.50] ]

**Note:** If you want to add hardware connections for the triggers, you will probably some [soldering equipment](https://www.sparkfun.com/categories/49), [hook-up wire](https://www.sparkfun.com/search/results?term=hook-up+wire), and some [momentary buttons](https://www.sparkfun.com/categories/313). Additionally, if you wish to interface with the board using a microcontroller, you should also grab a [RedBoard Qwiic](https://www.sparkfun.com/products/15123) and some [Qwiic cables](https://www.sparkfun.com/products/15081).

### Suggested Reading

If you're unfamiliar with switches, jumper pads, or I^2^C be sure to checkout some of these foundational tutorials.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/button-and-switch-basics)

### Button and Switch Basics 

A tutorial on electronics\' most overlooked and underappreciated component: the switch! Here we explain the difference between momentary and maintained switches and what all those acronyms (NO, NC, SPDT, SPST, \...) stand for.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

The Qwiic Keypad utilizes the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the **Logic Levels** and **I^2^C** tutorials (above) before using it. Click on the banner above to learn more about our [Qwiic products](https://www.sparkfun.com/categories/399).

## Hardware Overview

### Electrical Characteristics

The Qwiic MP3 Trigger is designed to operate at **3.3V** and must not be powered above **3.6V** as this is the maximum operating voltage of microSD cards. The **5V** power from the USB C connector tied to a robust AP2112 3.3V voltage regulator that can source up to **600mA** for the board. Otherwise, the board can also be powered through the Qwiic connector.

#### Maximum Operating Voltages

All I/O pins are **5V** tolerant but the board must but powered at **3.3V**.

#### Recommended Operating Voltages

All I/O pins are designed to function at **3.3V**. The board consumes **35mA** at 3.3V in standby and can consume over **400mA** when driving at **8 Ohm** speaker at max volume.

**Note:** The Qwiic MP3 Trigger can be powered through either the USB C cable or the Qwiic connector when used in conjunction with the [RedBoard Qwiic](https://www.sparkfun.com/products/15123). However, when using the Qwiic connection make sure that the **3.3V** line can source enough current for the amplifier.

### MP3 and ATtiny84

At the heart of the Qwiic MP3 Trigger is the [WT2003S MP3 decoder IC](https://cdn.sparkfun.com/assets/7/c/0/c/6/WT2003S-16S_Chip_V1.03.pdf). This IC reads MP3s from the microSD card and will automatically mount the SD card as a jump drive if USB is detected. The [ATtiny84A](https://cdn.sparkfun.com/datasheets/Widgets/doc8006.pdf) receives I^2^C commands and controls the MP3 decoder.

[![WT2003S IC and ATtiny84A IC](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_ATtiny84A_WT2003S.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_ATtiny84A_WT2003S.jpg)

### SD and USB

The SparkFun Qwiic MP3 Trigger works with 512MB to 32GB cards formatted in FAT32. We recommend the [SparkFun 1GB MicroSD Card](https://www.sparkfun.com/products/15107) because it's a good mix of low-cost and good performance for MP3 playing. Up to 255 songs can be loaded onto Qwiic MP3 Trigger.

[![The USB C and microSD connectors on the SparkFun Qwiic MP3 Trigger](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_USB_microSD.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_USB_microSD.jpg)

The easiest way to add and remove MP3s to the Qwiic MP3 Trigger is to attach a USB C cable. This will enumerate the microSD card as a jump drive making it extremely easy to access the files on the card. Alternatively, if you don't want to use USB, you can eject the microSD card and read/write to it using a normal [USB SD adapter](https://www.sparkfun.com/products/13004).

**Troubleshooting Tip:** While USB is connected to a computer, MP3 playing is disabled. However, as long as D+/D- are not connected, you can power the board over USB from a [USB wall adapter](https://www.sparkfun.com/products/11456) or power bank and still use the Qwiic MP3 Trigger normally.

**Note:** If you are moving just a few MP3 files, the USB C cable will work perfectly fine. However, if you need to move large amounts of data to the SD card, we suggest a normal [USB SD adapter](https://www.sparkfun.com/products/13004). The write speed to the SD card through a USB C cable is slower than a few MBs per second.

### Qwiic Connectors

The Qwiic MP3 Trigger from SparkFun includes two Qwiic connectors to make daisy chaining this music player with a large variety of I^2^C devices. Checkout [Qwiic](https://www.sparkfun.com/qwiic) for your next project.

[![Highlighted I2C port and Qwiic connectors](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_I2C_Ports_2_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_I2C_Ports_2_.jpg)

The I^2^C pins broken out on the board are tied directly to the Qwiic connectors.

### Audio Amplifier

The speaker is boosted by a **Class-D mono amplifier** capable of outputting up to **1.4W**. What does 1.4W mean? It\'s incredibly loud; great for making sure your mech effects are heard on the \*con floor (i.e. \_Comic\_ - con, \_Def\_ - con, etc.) and wonderful for annoying your officemates. Both outputs have volume controlled by the `SET_VOLUME` command and is selectable between 32 levels. Additionally, there are PTH holes beside both connectors if a soldered connection is preferred.

[![Class D Amplifier on SparkFun Qwiic MP3 Trigger](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Class_D_Amp_2_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Class_D_Amp_2_.jpg)

**Note:** The volume can be adjusted in software using the **SET_VOLUME** `0x07` command (see *Command Set* section). The volume setting is saved to NVM (non-volatile memory) and loaded at power on.

### Audio Outputs

A standard 3.5mm audio jack is provided making it easy to play your tunes over headphones or amplified desktop speakers like our [Hamburger Speaker](https://www.sparkfun.com/products/14023) or any other amplifier.

[![3.5mm audio jack and poke-home connectors](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Audio_Connectors_2_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Audio_Connectors_2_.jpg)

A poke-home connector labeled **Speaker** is also provided in parallel to the 3.5mm jack. This is a friction fit type connector; simply push stranded or solid core wire (**22AWG** or larger) into the hole and the connector will grip the wire.

To use an [external speaker](https://www.sparkfun.com/products/9151), solder two wires onto the speaker and insert the wires into the poke home connector.

[![Inserting tinned speaker wires into the Qwiic MP3 Trigger](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/5/9/Qwiic_MP3_Trigger_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/Qwiic_MP3_Trigger_Tutorial-01.jpg)

*Wire inserted into the poke home connector.*

To remove, push *down* on the tab with a ballpoint pen and gently pull on the wire.

[![Using pen to remove wire from poke home connector](https://cdn.sparkfun.com/r/400-6400/assets/learn_tutorials/8/5/9/Qwiic_MP3_Trigger_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/Qwiic_MP3_Trigger_Tutorial-03.jpg)

*Using pen to remove wire from poke home connector.*

### Jumpers

The Qwiic MP3 Trigger has three jumpers shown below:

[![Three jumpers on the SparkFun Qwiic MP3 Trigger](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Jumpers.jpg)

The default 7-bit I^2^C address of the Qwiic MP3 Trigger is `0x37`. The **ADR** jumper is open be default and can be closed with solder to force the device's I^2^C address to `0x36`. This is handy if you need to have two Triggers on the same bus. If you need more than two devices on the bus, or if these addresses conflict with another I^2^C device the address can be changed in software. Please see the [Command Set](https://learn.sparkfun.com/tutorials/qwiic-mp3-trigger-hookup-guide#command-set).

**Troubleshooting Tip:** Closing the **ADR** jumper forces the device to I^2^C address 0x36 regardless what the user may have set via the SET_ADDRESS command.

Cutting the **I^2^C** jumper will remove the 2.2k Ohm resistors from the I^2^C bus. If you have many devices on your I^2^C bus you may want to remove these jumpers. Not sure how to cut a jumper? [Read here!](https://learn.sparkfun.com/tutorials/how-to-work-w-jumper-pads-and-pcb-traces/cutting-a-trace-between-jumper-pads)

The **INT** jumper is located below the SparkFun logo and connects a 10K pull-up resistor to the INT pin. If you have multiple, open-drain, interrupt pins connected together you may want to remove this pull-up to better control the pull-up resistance.

### I/O Pins

There are several I/O pins broken out on the board, which are described in the table below.

[![Pins on the Qwiic MP3 Player](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Pins_2_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Pins_2_.jpg)

  Pin Name      Type           Description
  ------------- -------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  RST           Input          Active low. Pull this pin low to reset the ATtiny84A, effectively resetting the Qwiic MP3 Trigger.
  INT           Output         Active low. Goes low when track is finished playing. Goes high again when CLEAR_INTERRUPTS command is issued.
  SCL           Input          Serial clock line of I^2^C interface. Qwiic MP3 Trigger does implement clock stretching and will hold the clock line low if it is unable to receive additional I^2^C data.
  SDA           Input/Output   Serial data line of I^2^C interface.
  3.3V          Power          Qwiic MP3 Trigger can be powered from **2.8V** to **3.3V**. Anything greater than **3.6V** will damage the microSD card.
  GND           Power          The ground pin.
  Trigger 1-4   Input          When a trigger pin is pulled to ground, the corresponding T00X.mp3 file is played. Pins can be combined to play T001 to T010. Pins are 5V tolerant.

#### Triggers

There are four trigger pins at the top of the board. When pulled low these pins begin playing whatever file is named `T001.mp3` to `T010.mp3`. For example, if you attach a momentary button to **Pin 3** and **GND**, when you press that button the `T003.mp3` file will immediately be played. This allows you to start playing sound effects with the touch of a button without *any* programming!

[![Four trigger pins at the top of Qwiic MP3 Trigger](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Trigger_Pins_2_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Trigger_Pins_2_.jpg)

##### [Single Trigger]

For a basic triggered setup, load four files named *T001.mp3*, *T002.mp3*, *T003.mp3*, and *T004.mp3* on the microSD card. Use a wire or button to connect a trigger pin to ground and the associated track will begin playing. Once you have the setup working, use any [momentary button](https://www.sparkfun.com/categories/313) to allow a user to cause an MP3 to start playing.

##### [Using Multiple Triggers]

By pulling multiple pins down simultaneously the four triggers can play up to ten tracks: T001 to T010. When a trigger pin is detected the pin values are added together. For example, pulling pins **2** and **4** low at the same time will play track `T006.mp3` as will pulling pins **1**, **2**, and **3** low at the same time.

**Note:**

- The trigger pins are constantly monitored and any change in pins will immediately cause the new track to begin playing.
- Indefinitely holding a pin low will cause the same track to play again. This allows for looping sound effects.

#### Interrupt Pin

The Qwiic MP3 Trigger has an **INT pin** which is configured as an open-drain pin with an on board 10K Ohm pull-up.

[![INT pin and jumper](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_INT_Jumper_2_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_INT_Jumper_2_.jpg)

The **INT pin** will go low when a track has stopped playing. Once the **CLEAR_INTERRUPTS** `0x0D` command has been received, the **INT pin** will become high-impedance and will return to a high level.

If you have multiple devices with bussed interrupt pins you may want to cut the **INT jumper** to remove the 10K pull-up resistor.

## Qwiic MP3 Trigger Library

**Note:** This section assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

The SparkFun Qwiic MP3 Trigger Arduino library demonstrates how to control all the features of the Qwiic MP3 Trigger. We recommend downloading the SparkFun library through the Arduino library manager by searching \'**SparkFun MP3 Trigger**\'. Alternatively you can grab the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_Qwiic_MP3_Trigger_Arduino_Library):

[SparkFun Qwiic MP3 Trigger Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_MP3_Trigger_Arduino_Library/archive/master.zip)

Once you have the library installed checkout the various examples.

- **Example1:** Play the first MP3 track on the microSD card.
- **Example2:** Play the next track on the microSD card.
- **Example3:** Play a particular file. For example `mp3.playFile(3);` will play F003.mp3.
- **Example4:** Stop and pause tracks.
- **Example5:** Kitchen sink example showing setting of volume, equalizer, get song name, get song count, get firmware version, etc.
- **Example6:** Change the I^2^C address of the MP3 Trigger. Allows multiple Triggers to live on the same I^2^C bus.
- **Example7:** Shows how to start the library using a different Wire port (for example Wire1).
- **Example8:** Demonstrates how to check for the end-of-song interrupt and begin playing the song again.

## Command Set

The SparkFun Qwiic MP3 Trigger library takes care of all these commands for you. However, if you want to implement your own interface, the following commands are available (see list below). The Qwiic MP3 Trigger uses standard I^2^C communication to receive commands and send responses. By default, the ***unshifted* I^2^C address** of the Qwiic MP3 Trigger is `0x37`. The **write** byte is `0x6E` and the **read** byte is `0x6F`.

Here is an example I^2^C transaction showing how to set the volume level to 10:

[![Logic trace showing 0x6E 0x07 0x0A](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Set_Volume.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Set_Volume.jpg)

Here is an example I^2^C transaction showing how to read the device ID (0x39):

[![Logic trace showing 0x6E 0x10 0x6F 0x39](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Read_ID.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Read_ID.jpg)

The following commands are available:

- **STOP** `0x00` - Stops any currently playing track
- **PLAY_TRACK** `0x01 [TRACKNUMBER]` - Play a given track number. For example 0x01 0x0A will play the 10th MP3 file in the root directory.
- **PLAY_FILENUMBER** `0x02 [FILENUMBER]` - Play a file \# from the root directory. For example 0x02 0x03 will play F003.mp3.
- **PAUSE** `0x03` - Pause if playing, or starting playing if paused
- **PLAY_NEXT** `0x04` - Play the next file (next track) located in the root directory
- **PLAY_PREVIOUS** `0x05` - Play the previous file (previous track) located in the root directory
- **SET_EQ** `0x06 [EQ_SETTING]` - Set the equalization level to one of 6 settings: 0 = Normal, 1 = Pop, 2 = Rock, 3 = Jazz, 4 = Classical, 5 = Bass. Setting is stored to NVM and is loaded at each power-on.
- **SET_VOLUME** `0x07 [VOLUME_LEVEL]` - Set volume level to one of 32 settings: 0 = Off, 31 = Max volume. Setting is stored to NVM and is loaded at each power-on.
- **GET_SONG_COUNT** `0x08` - Returns one byte representing the number of MP3s found on the microSD card. 255 max. Note: Song count is established at power-on. After loading files on the SD card via USB be sure to power-cycle the board to update this value.
- **GET_SONG_NAME** `0x09` - Returns the first 8 characters of the file currently being played. Once the command is issued the MP3 Trigger must be given 50ms to acquire the song name before it can be queried with an I^2^C read.
- **GET_PLAY_STATUS** `0x0A` - Returns a byte indicating MP3 player status. 0 = OK, 1 = Fail, 2 = No such file, 5 = SD Error.
- **GET_CARD_STATUS** `0x0B` - Returns a byte indicating card status. 0 = OK, 5 = SD Error. Once the command is issued the MP3 Trigger must be given 50ms to acquire the card status before it can be queried with an I^2^C read.
- **GET_VERSION** `0x0C` - Returns two bytes indicating Major and Minor firmware version.
- **CLEAR_INTERRUPTS** `0x0D` - Clears the interrupt bit.
- **GET_VOLUME** `0x0E` - Returns byte that represents the volume level.
- **GET_EQ** `0x0F` - Returns byte that represents the EQ setting.
- **GET_ID** `0x10` - Returns 0x39. Useful for testing if a device at a given I^2^C address is indeed an MP3 Trigger.
- **SET_ADDRESS** `0xC7 [NEW_ADDRESS]` - Sets the I^2^C address of Qwiic MP3 Trigger. For example `0x6E 0xC7 0x21` will change the MP3 Trigger at I^2^C address 0x37 to address 0x21. In this example `0x6E` is device address `0x37` with write bit set to 1. Valid addresses are 0x08 to 0x77 inclusive. Setting is stored to NVM and is loaded at each power-on.

### Command Que

The ATtiny84A receives commands over I^2^C. It then records the I^2^C commands into a command que. The que is sent FIFO over serial to the WT2003S at **9600bps**. The WT2003S then requires an undetermined amount of time to respond. This means that commands are not instantaneously executed by the Qwiic MP3 Trigger and some commands may require a certain amount of time to before the Qwiic MP3 Trigger has loaded a valid response.

[![I2C traces showing how to read a song name](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Get_Song_Name2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/SparkFun_Qwiic_MP3_Trigger_-_Get_Song_Name2.jpg)

*An Example GET_SONG_NAME. Do you know the answer?*

For example, `GET_SONG_NAME` can be issued by the master microcontroller to the Qwiic MP3 Trigger. The QMP3 then transmits a serial command to the WT2003S. After a certain amount of time (unfortunately there are no max times defined by the [WT2003S datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/WT2003S-16S_Chip_V1.03.pdf)) the WT2003S will respond via serial. This can take **15 to 40ms**. At that time, the song name will be loaded onto the Qwiic MP3 Trigger and can be read over I^2^C by the master microcontroller.

In order to avoid clock stretching by the Qwiic MP3 Trigger and tying up the I^2^C bus, the Qwiic MP3 Trigger will release the bus after every command is received. Therefore, it is up to the user to wait the minimum **50ms** between the `WRITE GET_SONG_NAME` and the `READ` I^2^C commands.

### Power Up Time

The MP3 decoder IC on the Qwiic MP3 Trigger is the WT2003S. It requires approximately **1500ms** after power on to mount the SD card. Normally, the Qwiic MP3 Trigger is powered while the user writes and re-writes sketches so the user does not notice this boot time. The boot time only comes into effect when user initially powers their project. The main controller (such as an Uno) needs to wait up to **2 seconds** before giving up communicating with the Qwiic MP3 Trigger. The SparkFun Qwiic MP3 Trigger library takes care of the **2 second wait** but if you're writing your own implementation then consider the following example code:

    language:c
    if (isConnected() == false)
    
    return (true); //We're all setup!

### Maximum Song Count

Up to 255 songs can be loaded onto Qwiic MP3 Trigger and triggered through the command interface.

## Example 1: Play Track 1

The Qwiic MP3 Trigger can be used both as a standalone board or with the Qwiic connect system. In this case, we will be using the [RedBoard Qwiic](https://www.sparkfun.com/products/15123) as the microcontroller in the Qwiic system.

For both options, make sure to load an MP3 file labeled `T001.mp3` onto the MicroSD card.

**Heads up!** Make sure to follow the same format to label each track when including more than one audio file. Otherwise, you associated audio file will not begin playing with the trigger pin. For example, if you were including a second track, make sure to label it as `T002.mp3` to associate it with **Trigger Pin 2**.

### Standalone: Using Trigger 1

By default the firmware installed on the ATtiny84 allows you to play tracks using the triggers. For more details, see the *Triggers* section of the **Hardware Overview**. Simply plug in the SD card, power the Qwiic MP3 Trigger, and short the **Trigger Pin 1** to **GND**. Everytime you short both pins, `T001.mp3` will play.

[![Using trigger pins](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/Example_1_GIF.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/Example_1.jpg)

*Triggering the first track to play by shorting **Trigger 1** with a pair tweezers. **Click** on image for a closer view of the hardware setup.*

### Arduino Library: Using RedBoard Qwiic

Plug in the SD card into the MP3 Trigger. Then, connect the Qwiic MP3 Trigger to the [RedBoard Qwiic](https://www.sparkfun.com/products/15123) using a [Qwiic cable](https://www.sparkfun.com/products/15081).

[![Triggering with a RedBoard](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/Example_2_GIF.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/9/Example_2.jpg)

*Triggering the first track to play through the Qwiic connection. **Click** on image for a closer view of the hardware setup.*

Upload `Example1-PlaySong.ino` using the Arduino IDE to the RedBoard Qwiic. Once uploaded, the RedBoard will check for the Qwiic MP3 Trigger, set the volume to 10 and then play `T001.mp3`. Pressing the **RESET** button on the RedBoard will run the sketch again.