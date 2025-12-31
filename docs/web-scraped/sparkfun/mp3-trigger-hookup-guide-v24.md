# Source: https://learn.sparkfun.com/tutorials/mp3-trigger-hookup-guide-v24

## Introduction 

The [MP3 Trigger](https://www.sparkfun.com/products/13720) is a versatile, low-cost, low-power embedded audio unit that plays MP3 tracks directly from a FAT32 or FAT16 formatted microSD flash card to a stereo 1/8" (3.5mm) headphone output jack, supporting up to 192kbps stereo playback. The board has 18 external input pins that when pulled to ground, trigger pre-selected MP3 tracks, and a full-duplex serial control port that provides real-time volume control as well remote triggering for up to 255 tracks. There is also an on-board navigation switch for local access and playback of all MP3 tracks on the flash card.

[![MP3 Trigger](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/2/2/7/13720-01.jpg)](https://www.sparkfun.com/mp3-trigger.html)

### [MP3 Trigger](https://www.sparkfun.com/mp3-trigger.html) 

[ WIG-13720 ]

The MP3 Trigger board is built to make MP3 sound integration easier than ever.

[ [\$60.50] ]

The heart of the MP3 Trigger board is the Cypress PSoC CY8C29466-24SXI microcontroller which serves up MP3 data to a VLSI VS1063 audio codec IC. This version also supports an optional initialization file that can be used to set the serial port baud rate as well as to reprogram any of the 18 trigger inputs to alternate functions, including random and sequential track selection, transport controls and even volume up/down. Each conventional trigger can be set to either allow immediate restarts, or to lock out restarts if audio is playing. Also, a new trigger filename convention provides greater flexibility in naming your MP3 tracks and makes file management easier.

This version of the MP3 Trigger includes firmware that supports the use of an initialization file on the microSD card that can be used to change the serial baud rate, as well as to repurpose any of the 18 trigger inputs to alternate functions, such as random and sequential triggers, navigation controls and even volume controls. In addition, a restart lockout option can be used to prevent any trigger from starting a track if audio is already playing. Using these features, custom applications can often be implemented without the use of a separate microcontroller.

### Suggested Materials

To get started with your MP3 Trigger, you\'ll need a few items not included. To begin, you\'ll need an [microSD card](https://www.sparkfun.com/products/14832) on which to store your .mp3 files. A simple way to power the MP3 Trigger while you\'re familiarizing yourself with it is to use a [9V wall adapter](https://www.sparkfun.com/products/15314). If you intend on using your MP3 Trigger with another serial device, you need an [FTDI Basic](https://www.sparkfun.com/products/9716?_ga=1.172539360.273388466.1418147030) or other serial connection. Last, you will need something though which to play audio. You may use headphones, a 3.5mm-to-3.5mm audio cable to connect to an external audio source, or one of our [3.5mm Audio pigtails](https://www.sparkfun.com/products/11580) to wire your MP3 Trigger to the output you desire.

[![SparkFun FTDI Basic Breakout - 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/3/6/2/9/09716-SparkFun_FTDI_Basic_Breakout_-_5V-01.jpg)](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-5v.html)

### [SparkFun FTDI Basic Breakout - 5V](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-5v.html) 

[ DEV-09716 ]

This is a basic breakout board for the FTDI FT232RL USB to serial IC. The pinout of this board matches the FTDI cable to work...

[ [\$19.51] ]

[![Wall Adapter Power Supply - 9VDC, 650mA (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/7/TOL-15314-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-9vdc-650ma-barrel-jack.html)

### [Wall Adapter Power Supply - 9VDC, 650mA (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-9vdc-650ma-barrel-jack.html) 

[ TOL-15314 ]

This is a high quality switching \'wall wart\' AC to DC 9V 650mA wall power supply manufactured specifically for SparkFun Elect...

[ [\$9.25] ]

[![microSD Card with Adapter - 32GB (Class 10)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/1/0/2/14832-microSD_Card_with_Adapter_-_32GB__Class_10_-02.jpg)](https://www.sparkfun.com/microsd-card-with-adapter-32gb-class-10.html)

### [microSD Card with Adapter - 32GB (Class 10)](https://www.sparkfun.com/microsd-card-with-adapter-32gb-class-10.html) 

[ COM-14832 ]

This is a class 10 32GB microSD memory card, perfect for housing operating systems for single board computers and a multitude...

[\$26.95] [ [\$14.95] ]

[![Audio Cable TRRS - 18\" (pigtail)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/5/6/9/11580-01.jpg)](https://www.sparkfun.com/audio-cable-trrs-18-pigtail.html)

### [Audio Cable TRRS - 18\" (pigtail)](https://www.sparkfun.com/audio-cable-trrs-18-pigtail.html) 

[ CAB-11580 ]

TRRS connectors are the 3.5mm audio-style connectors that you see on some phones, MP3 players and development boards. TRRS st...

[ [\$1.95] ]

**Note:** The MP3 Trigger supports both SDSC (up to 2GB) and SDHC (up to 32GB) type microSD cards.

Make sure that you include some headers to connect to the PTH.

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/8/00553-03-L.jpg)](https://www.sparkfun.com/break-away-male-headers-right-angle.html)

### [Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-male-headers-right-angle.html) 

[ PRT-00553 ]

A row of right angle male headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custo...

[ [\$2.50] ]

### Tools

Depending on your setup, you may need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49) for a secure connection when using the plated through holes.

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

**Bundled Kits!** Check out the following tool kits with some of the soldering irons and accessories listed earlier!\
\

[![SparkFun Deluxe Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/8/1/2/7/11805-SparkFun_Deluxe_Tool_Kit.jpg)](https://www.sparkfun.com/products/11805)

### [SparkFun Deluxe Tool Kit](https://www.sparkfun.com/products/11805) 

[ TOL-11805 ]

This assortment of tools is great for those of you who have experience with tools but need a fresh set of new parts for your ...

**Retired**

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/8/3/14681-SparkFun_Beginner_Tool_Kit.jpg)](https://www.sparkfun.com/products/14681)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/products/14681) 

[ TOL-14681 ]

This assortment of tools is great for those of you who need a solid set of tools to start your workbench on the right foot!

**Retired**

### Suggested Reading

Before you begin working with the MP3 Trigger, you may find the following tutorials useful:

- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) - Soldering will be necessary to attach buttons and switches to the trigger inputs.
- [Working with Wire](https://learn.sparkfun.com/tutorials/working-with-wire) - You\'ll likely need to use some wire to attach those buttons and switches.
- [Switch Basics](https://learn.sparkfun.com/tutorials/switch-basics) - Learn about the numerous buttons and switches you can use to trigger your audio files.
- If you plan on using your MP3 Trigger with an Arduino or other microcontroller, you should have a good understanding of [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication), [Hexadecimal](https://learn.sparkfun.com/tutorials/hexadecimal), [ASCII](https://en.wikipedia.org/wiki/ASCII), and [Serial Terminals](https://learn.sparkfun.com/tutorials/terminal-basics).

## Board Overview

Here is a brief overview of the MP3 Trigger\'s specifications:

### Specifications

- **Input Voltage Range**: **4.5V to 12.0V DC**, or *regulated 3.3V* (jumper selectable)
- **Current Consumption**: Approximately 45mA idle, 85mA playing
- **Media**: SDSC and SDHC microSD cards
- **File system**: FAT32 and FAT16
- **Audio output**: Headphone stereo (1/8" stereo jack)
- **Trigger inputs**: **Logic level 3.3V--5.0V**, active low inputs, w/ internal pull-ups (connector provides individual grounds, allowing switches or jumpers to be connected directly to each trigger input)
- **Serial**: Full duplex, 8-bit, 38.4Kbaud (default, other baud rates supported via initialization file)

------------------------------------------------------------------------

The following will highlight the various hardware sections found on the MP3 Trigger.

### Power

The MP3 Trigger is designed to be powered a few different ways.

#### External Power via Barrel Jack

The first and most obvious power scheme is to apply external power to the barrel jack connector (5.5x2.1mm center positive). As the silkscreen next to the connector reads, you may power the MP3 Trigger through this jack with **4.5-12V DC**.

[![power option 1 with barrel jack](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-2-power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-2-power.jpg)

The solder jumper next to the barrel jack comes set to **VBUS by default**. Ensure that this jumper is always set to VBUS so long as you\'re powering the MP3 Trigger through that connector.

While power is applied to the barrel jack, you may use the USB/EXT switch as an ON/OFF switch to control the power to the MP3 Trigger. It should be powered while in the **EXT** position.

[![Switch Flipped to EXT](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/3/8/1/13720-04_mp3_trigger_external_power_switch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/13720-04_mp3_trigger_external_power_switch.jpg)

#### External Power via Through Holes

You can also solder power wires directly to the through-holes located on the backside of the board.

[![back holes](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-2-power-back.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-2-power-back.jpg)

#### FTDI Header via 5V Power Source

If you would like to integrate the MP3 Trigger into an existing system that uses 5V (like a USB port), you can power the MP3 Trigger through the FTDI header.

[![FTDI Port](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/3/8/1/mp3-5-FTDI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-5-FTDI.jpg)

You can apply the regulated power source directly to the VCC and GND pins, or you can solder some [right-angle headers](https://www.sparkfun.com/products/553) to the FTDI port and power with the appropriate [5V FTDI Basic Breakout](https://www.sparkfun.com/products/9716).

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Right-angle headers soldered on to the FTDI Port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/1/MP3_Trigger-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/MP3_Trigger-02.jpg)   [![Power with 5V FTDI](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/1/MP3_Trigger-01_5V_FTDI_Jumper_VBUS.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/MP3_Trigger-01_5V_FTDI_Jumper_VBUS.jpg)
  *Right-Angle Headers Soldered on FTDI Port*                                                                                                                                                                           *Power with 5V FTDI*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once connected, flip the switch to the **USB** side to power the board.

[![Switch Flipped to USB Side for Power from FTDI Header](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/3/8/1/13720-04_mp3_trigger_FTDI_power_switch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/13720-04_mp3_trigger_FTDI_power_switch.jpg)

If you intend on using the MP3 Trigger in conjunction with an Arduino or other microcontroller to communicate over the UART, you will do so through this port as well.

#### Why Use a 5V FTDI and Not a 3.3V FTDI?

You may not be able to power the MP3 Trigger with a 3.3V power source via the FTDI header despite it seeming logical that you could use a 3.3V FTDI on the \"5V FTDI\" header. The reasoning behind this is that certain versions of the [3.3V FTDI Basic](https://www.sparkfun.com/products/9873) uses the FTDI IC to regulate 5V down to 3.3V. If you are using this device to power the MP3 Trigger, you may exceed the current limitation of the 3.3V FTDI, leading to a potential brown-out on your device. Thus, we recommend using a [5V FTDI Basic](https://www.sparkfun.com/products/9716).

[![SparkFun FTDI Basic Breakout - 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/3/6/2/9/09716-SparkFun_FTDI_Basic_Breakout_-_5V-01.jpg)](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-5v.html)

### [SparkFun FTDI Basic Breakout - 5V](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-5v.html) 

[ DEV-09716 ]

This is a basic breakout board for the FTDI FT232RL USB to serial IC. The pinout of this board matches the FTDI cable to work...

[ [\$19.51] ]

#### FTDI Header via Regulated 3.3V Power Source

**Note:** SparkFun released a High-Current 3.3V FTDI Basic, known as the [Beefy 3](https://www.sparkfun.com/products/13746). Using this 3.3V FTDI with the MP3 Trigger is acceptable as it can provide enough current for it to operate.\
\

[![SparkFun Beefy 3 - FTDI Basic Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/7/6/13746-01.jpg)](https://www.sparkfun.com/sparkfun-beefy-3-ftdi-basic-breakout.html)

### [SparkFun Beefy 3 - FTDI Basic Breakout](https://www.sparkfun.com/sparkfun-beefy-3-ftdi-basic-breakout.html) 

[ DEV-13746 ]

This is SparkFun Beefy 3 FTDI Basic Breakout for the FTDI FT231X USB to serial IC. The pinout of this board matches the FTDI ...

[ [\$18.95] ]

If you power the MP3 Trigger with a regulated 3.3V power source that is able to source enough current via FTDI header\'s VCC pin, you will need to clear the solder jumper and resolder it so that the 3.3V pad and center pad are connected before you can power the board.

[![Solder Jumper with 3.3V FTDI](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-10-jumper3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-10-jumper3.jpg)

[] **Warning:** Switching the jumper to the 3.3V side will bypass the voltage regulator. You may risk damaging the microSD card and the components on the board if the voltage is higher than 3.3V or not regulated.

Once connected with a regulated 3.3V power source on the FTDI header, flip the switch to the **USB** side to power the board.

[![Jumper on 3.3V Side with ](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/3/8/1/13720-04_mp3_trigger_FTDI_power_switch_3_3V_Jumper.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/13720-04_mp3_trigger_FTDI_power_switch_3_3V_Jumper.png)

### Power LED

Power is indicated by the red Power LED located in the upper-right corner.

[![power LED](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-2-power-LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-2-power-LED.jpg)

### Trigger Pins

The Trigger pins are what make the MP3 Trigger so easy to use. Each of the 18 triggers is broken out to a 0.1\" through-hole. Next to each trigger pin is a ground pin. By [shorting](https://learn.sparkfun.com/tutorials/what-is-a-circuit/all#short) a trigger pin to ground, you are activating that trigger and thus playing the audio file associated with that particular trigger. More information can be found in the Using the Trigger Inputs section.

[![triggers](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/3/8/1/mp3-6-Triggers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-6-Triggers.jpg)

### 1/8\" Stereo Headphone Jack and Audio Solder Jumpers

The MP3 Trigger has a 1/8\" (3.5mm) audio jack to connect your project to an amplifier and speakers or to headphones.

[![Audio Jack](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-7-audioJack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-7-audioJack.jpg)

*Audio jumpers configured for Line out*

You will only be able to have your MP3 Trigger configured to play audio as a line out or as headphones,\*\* but not both at the same time\*\*. By default, the MP3 Trigger comes configured to play over a line out to an external audio system. If you wish to use your MP3 Trigger with headphone instead, you\'ll need to clear the solder from **all three audio solder jumpers** and solder the center pads to the opposite pads.

A solder jumper cheat sheet is conveniently printed in the silkscreen on the back of the MP3 Trigger to help you in altering the audio configuration.

[![jumper chart on back of MP3 trigger](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-4-jumperkey.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-4-jumperkey.jpg)

Once configured for headphones, the jumpers should look like this:

[![headphone jumper configuration](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-10-jumper4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-10-jumper4.jpg)

### Navigation Switch

The navigation switch allows you to cycle through and play/stop all the tracks located on your microSD card. More information on its operation can be found in the Basic Operation Section.

[![Nav Switch](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-8-switch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-8-switch.jpg)

### MicroSD Socket

The microSD socket is a simple push-to-insert/push-to-remove mechanism. The MP3 Trigger supports both **SDSC (up to 2GB)** and **SDHC (up to 32GB)** type microSD cards. More information on how the microSD card initializes can be found in the Basic Operation Section.

[![micro SD Socket](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-3-sdSocket.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-3-sdSocket.jpg)

## Basic Operation 

Simply drag and drop the desired MP3 files into the root directory of a FAT32 or FAT16 formatted microSD flash card using a PC.

The MP3 Trigger **does not support hot-swapping of the microSD Card**. While this won't damage anything, the microSD media is only initialized during power up. So whenever the card is changed or updated, be sure to power cycle the MP3 Trigger after installing the card.

When power is applied to the MP3 Trigger, the on-board (green) status LED indicates the state of the installed media as follows:

- 1 long blink - No formatted microSD media found.
- 1 long blink, followed by 1 short blink - microSD media found, no MP3 files located.
- Constant short blinks - Hardware problem with MP3 Decoder.
- 3 short blinks - microSD media found, at least 1 MP3 file located.

[![status LED](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-9-statusLED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/1/mp3-9-statusLED.jpg)

*Status LED*

As soon as the MP3 Trigger powers up with 3 short blinks, the on-board navigation switch can be used to play all of the tracks on the card, regardless of the filenames.

- Left - Plays the previous MP3 file in the directory
- Right -Plays the next MP3 file in the directory
- Center - Starts/Stops the current MP3 file

## Using the Trigger Inputs 

The MP3 Trigger provides 18 input pins (TRIG01 --TRIG18) that can be used to trigger specific MP3 tracks on the microSD card. MP3 tracks are associated with triggers by placing a 3-digit number (using leading 0s) at the beginning of the filename; **001 for TRIG01**, **002 for TRIG02** and so on. The rest of the filename can be anything. For example, the following are both valid names for TRIG14:

- "014TRACK.MP3"
- "014 Breaking Glass.mp3"

The trigger inputs are active low and pulled high internally. Therefore, they can be activated either by digital outputs from another microcontroller (such as an Arduino) or by a simple contact closure (switch) to ground. The inputs support voltage levels of either 5V or 3.3V.

The trigger inputs are made available on the even-numbered pins of a dual row connector, and all the opposing (odd-numbered) pins are ground, making it easy to wire individual switches or contact closures directly to the MP3 Trigger board.

Installing a 36-pin [dual-row header](https://www.sparkfun.com/products/12791) allows shunt jumpers to be installed on the trigger inputs to automatically sequence and loop tracks on power-up as follows.

When a triggered track reaches the end, the MP3 Trigger looks to see if any trigger inputs are active, and will automatically start another track if so. If only the same trigger is active, then that track will restart (loop). If other triggers are active, the MP3 Trigger will always start the next higher trigger track, wrapping back to 1 after 18.

This, combined with the fact that the MP3 Trigger will automatically start the lowest numbered active trigger on power up, means that by installing shunt jumpers on the trigger inputs, the MP3 Trigger can be set to automatically sequence and loop from 1 to 18 tracks on power up with no externally programming or control required. (Beginning with firmware version 2.40, installing a shunt jumper on a single sequential trigger will do the same thing.)

For example, if you wanted track 9 to play on startup, you\'d jumper trigger 9. If you wanted tracks 1 through 9 to play on startup, you have to have a jumper on all nine triggers.

Using the initialization file describe later in this document, triggers can be reprogrammed to start sequential or random tracks. For example, if a trigger is reprogrammed to be a random trigger, and that one trigger is shunted closed, then the MP3 Trigger will power up and continuously play tracks in a (pseudo) random order.

### Quiet Mode

The MP3 Trigger can be placed into Quiet Mode using the serial control port. In this mode, the trigger inputs will not start tracks but instead will cause serial messages to be sent upon activation. (See "MP3 Trigger Outgoing Message Summary" below.) This allows the trigger inputs to be decoupled from specific tracks, so that a PC or microcontroller can monitor the trigger inputs and then start any track or sequence of tracks via the serial control port.

Quiet Mode is off by default and is not preserved through a power cycle

## Serial Control Protocol 

The MP3 Trigger comes with a full duplex 3.3-5V serial TTL interface that allows for control of all the MP3 tracks (up to 256) on the microSD card as well as volume, and for monitoring input trigger activity. You can use an [FTDI Basic](https://www.sparkfun.com/products/9716) or connect to any serial interface that uses the format: **8-bits, 1-start, 1-stop, no parity, flow control = none**. The serial port baud rate **defaults to 38.4kbps (i.e. 38400 baud)**, but can be changed using the initialization file. All commands to the MP3 Trigger are 1 or 2 bytes in length.

1-byte commands are upper case ASCII characters. 2-byte commands start with an ASCII character. Those starting with an upper case character use an ASCII value ('0'--'9') as the second byte. (These commands can be typed on a keyboard.) 2-byte commands starting with a lower case character require a binary value (0 -- 255) as the second byte.

Bytes sent to the MP3 Trigger are not echoed. If echoing is required, set your terminal program to echo locally.

### Command Summary

Command: **Navigation -- Start/Stop**\
Number of bytes: 1\
Command byte: 'O'\
Data byte: none\
Comments: This command performs the same function as pushing the on-board nav switch center position. If the current track is playing, it stops. If the current track is stopped, it will restart from the beginning.

Command: **Navigation -- Forward**\
Number of bytes: 1\
Command byte: 'F'\
Data byte: none\
Comments: This command performs the same function as pushing the on-board nav switch right position. The next MP3 track in the directory will be started.

Command: **Navigation -- Reverse**\
Number of bytes: 1\
Command byte: 'R'\
Data byte: none\
Comments: This command performs the same function as pushing the on-board nav switch left position. The previous MP3 track in the directory will be started.

Command: **Trigger (ASCII)**\
Number of bytes: 2\
Command byte: 'T'\
Data byte: N = ASCII '1' through '9'\
Comments: If it exists, the track with the filename "00Nxxxx.MP3" will be started, where N is the data byte. xxxx can be any valid filename characters of any length.

Command: **Trigger (binary)**\
Number of bytes: 2\
Command byte: 't'\
Data byte: n = 1 to 255\
Comments: If it exists, the track with the filename "NNNxxxx.MP3" will be started, where NNN is the ASCII equivalent of the data byte \'n\' with leading 0s. xxxx can be any valid filename characters of any length.

Command: **Play (binary)**\
Number of bytes: 2\
Command byte: 'p'\
Data byte: n = 0 to 255\
Comments: If it exists, the nth track in the directory will be played. The total number of available tracks in the directory can be retrieved using Status Request command below.

**Note:** There are subtle differences when using the Play and Trigger commands. When sending the Play command (\'**p**\') with a data byte via the serial UART, the MP3 Trigger will begin playing files in the order that the track appears in the microSD card filesystem. For example, let\'s say you saved the following tracks in this order:\
\

- *\"009 SOMETHING.MP3\"*
- *\"005 START.MP3\"*
- *\"001 SPARK.MP3\"*
- *\"002 FUN.MP3\"*

\
You decide to send the [hex representation](https://learn.sparkfun.com/tutorials/hexadecimal) of the command byte and data byte. The Play command \'p\' as `0x160` with data byte \'1\' as `0x1` are sent to the MP3 trigger. The MP3 trigger will begin playing in the order that it was saved to the microSD card. As opposed to playing the track number associated with the number 1, it will begin playing *\"009 SOMETHING.MP3\"*. To play *\"001 SPARK.MP3\"*, you would need to send the play command as `0x160` with data byte \'3\' as `0x3` since it was the 3rd track to be saved in the directory.\
\
The Trigger command plays by the track based on the file name. Using the Trigger command \'**T**\' as `0x124` with data byte \'1\' as `0x61`, the board will play *\"001 SPARK.MP3\"*. Remember, the upper case ASCII character requires an [ASCII value](https://learn.sparkfun.com/tutorials/ascii#ascii-table) between \'1\' through \'9\' as the second data byte. Using the Trigger command \'**t**\' as `0x160` with data byte \'1\' as `0x1`, the board will play *\"001 SPARK.MP3\"*. As noted earlier, the lower case ASCII character requires a binary value between 0 to 255 as the second data byte.

Command: **Set Volume (binary)**\
Number of bytes: 2\
Command byte: 'v'\
Data byte: n = 0 to 255\
Comments: The VS1053 volume will be set to the value n. Per the VS1053 datasheet, maximum volume is 0x00, and values much above 0x40 are too low to be audible.

Command: **Status Request (ASCII)**\
Number of bytes: 2\
Command byte: 'S'\
Data byte: N = ASCII '0' through '1'\
Comments: If N = '0', the MP3 Trigger will respond with a version string. If N = '1', the MP3 Trigger will respond with the total number of tracks on the installed microSD card, in ASCII. Both responses will be preceded by the '=' character.

Command: **Quiet Mode (ASCII)**\
Number of bytes: 2\
Command byte: 'Q'\
Data byte: N = ASCII '0' or '1'\
Comments: If N='1', Quiet mode is turned on. If N='0', Quiet mode is turned off. Default state is off.

### MP3 Trigger Outgoing Message Summary

The MP3 Trigger sends the following ASCII messages:

- 'X': When the currently playing track finishes.
- 'x': When the currently playing track is cancelled by a new command.
- 'E': When a requested track doesn't exist (error).

In response to a Status Request Command, data byte = '0', the MP3 Trigger sends an 18-byte version string: e.g. "=MP3 Trigger v2.50". In response to a Status Request Command, data byte = '1', the MP3 Trigger sends the number of MP3 tracks on the currently installed microSD card: e.g. "=14".

In Quiet Mode only, when one or more trigger inputs are activated, the MP3 Trigger sends 'M' followed by a 3-byte bit mask indicating which triggers were activated:

- Data byte 0: TRIG01 through TRIG08
- Data byte 1: TRIG09 through TRIG16
- Data byte 2: TRIG17 and TRIG18

A value of 1 in a bit position indicates that the corresponding trigger input was activated.

## Initialization File

Version 2.40 firmware (and above) supports the use of an initialization file to change some of the operation parameters of the MP3 Trigger upon power up. This file is ASCII text only, and can be created and edited with any text editor such as Notepad. The initialization file must be named "MP3TRIGR.INI" and must, like all the mp3 files, be in the root directory. The file is optional. If it does not exist, then the MP3 Trigger defaults to normal operation at 38.4K baud and all triggers starting their respective tracks. Initialization file commands must begin with the "#" character and be followed by a space. The initialization file example on the following two pages is self-documented and describes the commands currently supported:

### Sample Initialization File

    #BAUD 38400
    #RAND 2
    #TRIG 01, 0, 0
    #TRIG 02, 0, 0
    #TRIG 03, 0, 0
    #TRIG 04, 0, 0
    #TRIG 05, 0, 0
    #TRIG 06, 0, 0
    #TRIG 07, 0, 0
    #TRIG 08, 0, 0
    #TRIG 09, 0, 0
    #TRIG 10, 0, 0
    #TRIG 11, 0, 0
    #TRIG 12, 0, 0
    #TRIG 13, 0, 0
    #TRIG 14, 0, 0
    #TRIG 15, 0, 0
    #TRIG 16, 0, 0
    #TRIG 17, 0, 0
    #TRIG 18, 0, 0
    ******************** ALL INIT COMMANDS ABOVE THIS LINE *********************
    This is a sample init file for the MP3 Trigger v2, firmware version 2.40.

    The init file is optional. If not present, the default parameters will be
    in effect: 38.4Kbaud, and all triggers will start their corresponding
    tracks with restart lockout disabled. If it is present, it must be named
    MP3TRIGR.INI and be located in the root directory.

    Only the first 512 bytes of the file are examined for commands, and the first
    occurrence of the '*' character is treated as the end of file by the parser.
    Comments are not allowed in the command section, but there is no restriction
    on the length of the comments that follow the first '*'.

    All commands must begin with the '#' character and be followed by a space,
    then the command parameters separated by commas. White space is ignored. All
    parameters are decimal numbers. Leading zeros are acceptable. See the above
    examples - which are redundant since they are all default values.

    The following commands are supported in firmware version 2.40:

    #BAUD N

        where N is one of the following: 2400, 9600, 19200, 31250 or 38400

    #RAND N

        where N is from 1 to 255

        The default behavior of the random trigger function is to play a random 
        track from all the MP3 files on the flash card. The #RAND function will
        exclude the first N tracks (in the directory) from the random trigger
        function. So if there are 18 MP3 files on the card and N=4, then the
        first 4 MP3 files will be excluded from the random trigger function.

    #TRIG N, F, L

        where: N is the trigger number (1-18)
        F is the trigger function type (see below)
        L is the restart lockout enable

        The defined trigger function types (F) are as follows:

        F = 0: Normal operation
        F = 1: Next (same as the forward Nav switch)
        F = 2: Random
        F = 3: Previous (same as the back Nav switch)
        F = 4: Start (restarts the current track)
        F = 5: Stop
        F = 6: Volume Up
        F = 7: Volume Down

        The restart lockout feature, if enabled, will prevent that trigger
        from working if audio is currently playing. Use this if you want
        to prevent restarts before the track has reached the end. This
        feature does not apply to function types 5-7.

        L = 0: Restart lockout disabled (default)
        L = 1: Restart lockout enabled

    You only need to include entries for triggers that are to be non-default.
    As an example, I use the following single-line init file to make trigger
    18 be a "Next" function, then hard-wire the trigger so that my MP3 Trigger
    powers up and loops continuously through all the tracks on the card.

    #TRIG 18, 1, 0

## Bootloader 

The MP3 Trigger has a resident bootloader that allows updating the firmware directly from the microSD card, alleviating the need for a hardware programmer. Because this bootloader is in located in protected sectors of the PSoC's flash memory, it cannot overwrite itself. The bootloader can always be run on power up, thus making it possible to recover from a bad firmware load.

**IMPORTANT NOTE:** Use of a hardware programmer, such as the Cypress MiniProg, to program the MP3 Trigger with anything other than the bootloader image will erase the bootloader. Don't do it!

### Using the Bootloader

To update the MP3 Trigger firmware, copy the new firmware hex file to a FAT16 or FAT32 formatted micro-SD card and rename the file to "MP3TRIGR.HEX". It doesn\'t matter if it\'s the only file on the microSD card or not - the bootloader will find it as long as it has this exact filename. Insert the microSD card into the MP3 Trigger with the power off. Hold down the center nav switch while turning on the power. Wait for the status LED to go solid, then power cycle the MP3 Trigger to run the new firmware.

### Bootloader Detailed Explanation

The bootloader is always entered whenever the board powers up. The first thing it does is look to see if the center nav switch is being held down. If not, it immediately vectors to the start of the firmware. Note that if you have previously loaded bad firmware, the board will simply halt or do whatever your bad code tells it to do -- possibly with no activity other than the power LED. This is normal if there\'s no good firmware loaded.

If the center nav switch is being held on power up, the bootloader searches the microSD card directory for a file named \"MP3TRIGR.HEX\". If there\'s no card installed, or the file doesn\'t exist on the card, it will blink the status LED very rapidly forever. If it finds and is able to open the file, it begins to program the PSoC Flash with the contents of the firmware file. The status LED will illuminate for each hex record programmed. If it successfully programs the entire file, the status LED will turn solid upon completion. You can then power cycle the MP3 Trigger and you will be running the new firmware (don\'t hold the nav switch down again or you will simply re-enter the bootloader.

If there\'s a flash memory programming error (or you pull the microSD card out before it finishes, for example) the status LED will indicate a bad programming cycle by blinking briefly at about 1 Hz (This looks very different than the blinking for programming records). You need to cycle the power again holding the nav switch to re-enter the bootloader.

The key is that the bootloader cannot over-write any p art of itself, no matter what\'s in the firmware image file. The worst thing that can happen is you load bad firmware and the board won\'t run. But you can always hold the nav switch down on power up and get into the bootloader to load new firmware.