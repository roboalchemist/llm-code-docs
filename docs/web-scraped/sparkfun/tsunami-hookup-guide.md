# Source: https://learn.sparkfun.com/tutorials/tsunami-hookup-guide

## Introduction

**Note:** This tutorial was written for the Tsunami Super WAV Trigger v1.1. For users using v1.2, make sure to check out the [Tsunami Super WAV Trigger Hookup Guide](https://learn.sparkfun.com/tutorials/tsunami-super-wav-trigger-hookup-guide) .

Tsunami is the next-generation SparkFun polyphonic WAV file player.

[![Tsunami Super WAV Trigger](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/3/9/6/13810-01.jpg)](https://www.sparkfun.com/products/13810)

### [Tsunami Super WAV Trigger](https://www.sparkfun.com/products/13810) 

[ WIG-13810 ]

Based on a new generation ARM Cortex M7, the Tsunami extends polyphony to 32 mono or 18 stereo simultaneous uncompressed 44.1...

**Retired**

Tsunami is a bigger, better brother to the [WAV Trigger](https://www.sparkfun.com/products/13660). It starts with the same polyphonic WAV file playback engine, then adds a bunch of new features.

- First, Tsunami features eight analog outputs, which can be configured as either eight mono outputs or four stereo outputs.
  - In stereo mode, it can simultaneously play 18 stereo WAV files.
  - In mono mode, it can play back 32 mono WAV files.
  - Mono mode also offers a track synchronization option, which allows for playback of multichannel content, including quadrophonic, 5.1 and 7.1 surround formats.
- Tsunami also features a stereo audio input that can be mixed into any combination of the outputs.
- Each output provides independent, real-time volume control and pitch bend.
- WAV files can be independently mapped to outputs.
- Up to 4,096 WAV files can be indexed and played off a microSD card.
- Tracks can be triggered via three different interfaces.
  - There are 16 onboard inputs that can be tied to switches or logic-level devices.
  - The FTDI-compatible footprint allows serial control from a computer or microcontroller.
  - There are onboard MIDI input and output circuits \-\-- just add DIN-5 sockets.
- Tsunami offers low latency. Tracks typically start within 8 mSec of a trigger event.
- Detailed track control \-\-- tracks can start, pause, resume and stop, and loop seamlessly.
- Firmware can be easily loaded from the SD card, which facilitates switching between stereo and mono playback modes, as well as upgrading as new features are released.

Tsunami was developed in collaboration with [Robertsonics](http://robertsonics.com/). A portion of each sale goes back to them for product support and continued development.

This guide will show you how to start using Tsunami. We\'ll start by putting .WAV and configuration files on a microSD card, then pop it in Tsunami, then trigger sounds across multiple outputs.

### Required Materials

To follow along with this project tutorial, you will need the following materials:

#### Tools

You will also need a microSD card reader and a set of headphones or multimedia speakers.

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

- Robertsonics has a more detailed [Tsunami page](http://robertsonics.com/tsunami/). If this SparkFun guide doesn\'t have the information you\'re looking for, check there.
- Robertsonics also releases a cross-platform utility for generating Tsunami configuration files and new firmware files. All of these can be downloaded from Robertsonics\' [Tsunami downloads](http://robertsonics.com/tsunami-downloads/) page.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/button-and-switch-basics)

### Button and Switch Basics 

A tutorial on electronics\' most overlooked and underappreciated component: the switch! Here we explain the difference between momentary and maintained switches and what all those acronyms (NO, NC, SPDT, SPST, \...) stand for.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

[](https://learn.sparkfun.com/tutorials/midi-tutorial)

### MIDI Tutorial 

Understanding the Musical Instrument Digital Interface.

## Hardware Overview

The Tsunami board has the following features and interfaces.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/2/callouts.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/callouts.png)

*Major Tsunami Subsystems.*

- **MicroSD card slot.** We\'ve had the [best results](http://robertsonics.com/microsd-cards-for-audio/) with Class 4 and Class 10 cards.
- **Micro-B USB port** for power input.
- **Reset switch.** Used to reinitialize Tsunami, particularly after swapping the SD card.
- **3.3V FTDI-style serial interface**. Tsunami can be controlled using a PC, or an external microcontroller.
- **Atmel ATSAMS70N20 Cortex M7 microcontroller**. The brains of the whole operation!
- **0.1 inch header power input**. Connect an external supply of 5\--15 VDC here.
- **16 trigger inputs**. Used to control WAV file playback. Each has an adjacent ground pad to make connecting switches easier.
- **Stereo audio input**. Can be mixed to any combination of outputs.
- **Audio outputs**, configurable as four stereo outputs or eight mono outputs. Again, each output has an adjacent ground pad to facilitate wiring.
- **MIDI input and output ports**. Just add 5-pin DIN connectors for MIDI.

Each of these is described in more detail in the [Tsunami Online User Guide](http://robertsonics.com/tsunami-user-guide/).

### Tsunami Power Notes

#### Power Supply Requirements

Tsunami should be powered with between **5 and 15 VDC**. Tsunami is also rather power hungry: While playing WAV files, it draws about 200 mA.

Power can be applied two ways. For convenience, Tsunami can be powered by the USB micro-B connector, from a USB port, or a [micro-B terminated wall adapter](https://www.sparkfun.com/products/12890). Alternatively, Tsunami can be powered more directly using the 0.1 inch header power input.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/powering.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/powering.png)

*Powering Tsunami.*

#### Logic Levels

On Tsunami, the incoming voltage is regulated down to 3.3V for all of the onboard circuitry. The processor, codec and other circuitry are all powered from 3.3V.

Tsunami\'s digital interfaces operate at 3.3V and are not compatible with 5V logic. If you are connecting other devices to the FTDI header or trigger inputs, you need to be sure to use 3.3V devices, or a [voltage translator](https://www.sparkfun.com/products/11771) to bridge the gap.

The one exception to this is the opto-isolated MIDI input. Being opto-isolated, it is fully compatible with regular 5V MIDI circuitry.

## Tsunami Demonstration

To show how easy it is to use Tsunami, let\'s hook it up and play some sounds.

For this demo, we\'ll be using the firmware that comes preloaded when you purchase the board. This is the stereo version, which plays stereo WAV files and treats the adjacent outputs as pairs, numbered 1 through 4. Mono file playback is supported by a different firmware image.

## Prepare the SD Card

**Note:** For the best results, we recommend **Class 10** SD cards with a **FAT16** or **FAT32** file system format and a 32kB file allocation size. We recommend avoiding:\
\

- The [1GB SparkX SD Card](https://www.sparkfun.com/products/15107), from our catalog, since it isn\'t a Class 10 card and can lead to reliability issues.
- SD Cards with a capacity larger than 32GB, since it can be difficult to convert them to the **FAT16** or **FAT32** file system format with a 32kB file allocation size.

\
For more information on compatible SD cards, please check out the Robertsonics website:\
\

- [microSD Cards for Audio 2024](https://www.robertsonics.com/blog/microsd-cards-for-audio-2024)
- [microSD Cards for Audio](http://robertsonics.com/microsd-cards-for-audio/)

The contents of the microSD card are the key to Tsunami. To start this demonstration, we\'ll prepare a card with some prerecorded files.

First, a quick warning about formatting your uSD card. If you need to format your card, it is *very important* that you use the correct settings:

- File system must be FAT16 or FAT32
- File Allocation Size must be 32 kilobytes
- \"Quick format\" is usually okay
- Note, if you are using a \"brand new card\", then formatting may not be necessary. If you notice that your Tsunami is missing commands, making occasional strange buzzing sounds, and sometimes crashing, then your file allocation size may be incorrect.

[![alt text](https://cdn.sparkfun.com/r/500-500/assets/home_page_posts/2/6/9/6/format32.jpg)](https://cdn.sparkfun.com/assets/home_page_posts/2/6/9/6/format32.jpg)

*Formatting settings for Tsunami uSD card*

Next, download the demo files. Unzip the folder and put the files on the root directory of the card.

[Demo Tsunami Files (.ZIP)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/tsunami-demo-files.zip)

Before we put the card in Tsunami, let\'s quickly examine the files.

[![Files on the card](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/card-dir.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/card-dir.png)

*Files on the card*

Notice that there are two types of file: 16 WAV files, and one INI file.

### WAV Files

The WAV files are the audio content Tsunami will be playing back. These are 16 stereo WAV files, configured to play from the 16 trigger inputs.

#### Naming

The file names contain the trigger input mapping for the files. Each one starts with a three-digit number, which assigns it to the corresponding trigger input.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/trigger-to-file.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/trigger-to-file.png)

*File number to trigger mapping*

With 16 files, numbered 001 to 016, we\'ll be assigning a file to each of the trigger inputs.

#### WAV File Format

We should also take a moment to examine the file format. Tsunami plays WAV files recorded at 16-bit resolution, with a 44.1kHz sampling rate. Different firmware images allow for the playback of stereo or mono files.

Tsunami also requires that the file not contain any additional header information. Some audio recording programs, such as Pro Tools, write additional information at the start of the file. One easy way to remove unnecessary header information is by opening the file in [Audacity](http://www.audacityteam.org/) and exporting it as \"WAV (Microsoft) signed 16-bit PCM.\" As part of the export process, be sure to clear out any entries in the metadata dialog (title, artist, genre, etc.). The following video gives a brief demonstration of the Audacity export process.

*Exporting from Audacity to Tsunami.*

If you\'re curious about the header contents, Rail John Rogut has written the [Header Investigator](http://www.railjonrogut.com/HeaderInvestigator.htm) application, which can display Pro Tools region information and BWF time stamps. This extra data might be meaningful to DAW applications, but Tsunami doesn\'t use the information.

### .INI File

There is also an initialization file, `tsunami.ini`. Tsunami reads this file when it starts, to gather more details about how it should handle the trigger inputs. In this case, the triggers are constrained so that a file plays completely and can\'t be retriggered until it is done playing. This prevents stuttering when the trigger inputs aren\'t clean.

INI files are generated and edited using the [Tsunami Configurator](http://robertsonics.com/tsunami-downloads/) application. They are human readable ASCII text files. If you\'re curious about what\'s inside, you can open them in a text editor.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/2/config-util.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/config-util.png)

*Tsunami configurator*

If you want to map the triggered sounds to other outputs, you can select the output number in the \"Trigger Settings\" portion of the app.

You can find more information about the configurator utility in the [Tsunami user guide](http://robertsonics.com/tsunami-user-guide/#configurator).

## Install the Card

Now that we\'ve looked at the contents of the card, eject the card from your computer and put it in the slot on Tsunami.

## Connect Outputs

For this demo, we\'ll only be using the first stereo output, Output 1L and 1R.

To listen to that output, we\'ll make a temporary adapter using a [3.5mm TRRS breakout board](https://www.sparkfun.com/products/11570) and some [IC Hook test leads](https://www.sparkfun.com/products/501). We\'re using the IC Hooks so we don\'t have to solder them to the board, making a temporary connection for the sake of the example.

We cut three of the leads in half and soldered them to the `TIP`, `RING1` and `SLEEVE` pads of the breakout, using the following connection scheme. We didn\'t make any connection to the `RING2` pad.

Jumper Color

Breakout Connection

Tsunami Connection

Blue

TIP

Output 1L

Red

RING1

Output 1R

Green

SLEEVE

GND

The adapter cable looks like this.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/2/Tsunami_Super_Wav_Trigger_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/Tsunami_Super_Wav_Trigger_Hookup_Guide-02.jpg)

*Adapter cable*

With care, you can put the ends of the IC hooks through the 0.1\" pads on the PCB, connected as described in the table above.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/2/Tsunami_Super_Wav_Trigger_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/Tsunami_Super_Wav_Trigger_Hookup_Guide-03.jpg)

*Adapter cable in place*

Finally, connect your headphones, multimedia speakers, or other output device.

------------------------------------------------------------------------

## Connect Power

For this demo, we\'re simply powering Tsunami from the USB port on our computer.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/2/Tsunami_Super_Wav_Trigger_Hookup_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/Tsunami_Super_Wav_Trigger_Hookup_Guide-04.jpg)

*Test setup*

When you apply power, the board will initialize, and indicate readiness by blinking the status LED three times. From then on, the LED pulse every few seconds, indicating that the board is alive, and waiting to be triggered.

## Trigger Sounds

The simplest way to drive Tsunami is by shorting the trigger inputs to ground. By default, the trigger inputs use an internal pullup resistor, and recognize when they are grounded.

For this demo, we\'re going to use a short piece of wire to bridge trigger inputs to their corresponding ground pads. A more permanent application might use momentary switches, such as [cherry switches](https://www.sparkfun.com/products/13834), [tactile switches](https://www.sparkfun.com/products/97) or [microswitches](https://www.sparkfun.com/products/9414).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/2/Tsunami_Super_Wav_Trigger_Hookup_Guide-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/Tsunami_Super_Wav_Trigger_Hookup_Guide-05.jpg)

*Triggering a WAV file*

We\'ve bent the wire into a 0.1\" wide U-shape. We insert one end into a ground pad, and use the other to tap the trigger inputs.

## Eureka!

When the wire makes contact, you should hear a sound on the output. The files on the card simply recite the number of the trigger input.

The status LED also illuminates while files are playing.

## Further Experiments

Now that you\'ve got sound, there are a few other things you can try out.

### Other Trigger Modes

If your application doesn\'t have switches that can easily short the trigger inputs to ground, there are three methods to trigger sounds.

1.  Using an `*.INI` file, you can convert to trigger inputs to respond to 3.3V active-high logic pulses, which could be sent by a microcontroller or discrete logic.
2.  You can send MIDI note on and off commands to the MIDI port to trigger sounds.
3.  You can use the [Tsunami Serial Protocol](http://robertsonics.com/tsunami-user-guide/#serial-control) to trigger sounds on the FTDI-compatible serial port. You can connect to a computer using an FTDI [USB-to-serial converter](https://www.sparkfun.com/products/9873), or use the [Tsunami Arduino Library](https://github.com/robertsonics/Tsunami-Arduino-Serial-Library) on a microcontroller.

Tsunami responds on all of these interfaces simultaneously.

#### Connecting MIDI Input

For Tsunami to receive MIDI, all you need to do is add a [5-pin DIN](https://www.sparkfun.com/products/9536) socket. Simply connect pins 4 and 5 to the pads with corresponding labels.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/2/Tsunami_Super_Wav_Trigger_Hookup_Guide-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/Tsunami_Super_Wav_Trigger_Hookup_Guide-06.jpg)

*MIDI input connection.*

Keep in mind that the pins on a 5-pin DIN are out of order, but as a reminder, the numbers are usually embossed in the plastic of the connector.

Tsunami responds to MIDI note on and off, pitch bend, program change, and a number of continuous controller messages. By default it is in Omni-on mode, responding to messages on any channel, though the channel can be specifically assigned using the configuration file. More details about the MIDI implementation can be found in the [Tsunami user guide](http://robertsonics.com/tsunami-user-guide/#midi-implementation).

### More Outputs

To streamline this example, we\'ve limited it to the first stereo output \-- but of course, one of the best features of Tsunami is the multiple outputs. So let\'s take a look at a couple of ways to reassign WAV files to those outputs.

#### Trigger Output Mapping

The first method of assigning files to outputs is by editing the INI file. Using the Tsunami Configurator, you can assign files to outputs in the **\"Trigger Settings\"** section. Each trigger can be assigned to a different output.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/2/config-util-output-assig.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/config-util-output-assig.png)

*Tsunami output parameter.*

Of course, the INI file only covers the 16 trigger inputs.

#### MIDI Output Mapping

If you\'re using MIDI to trigger Tsunami, you can assign tracks to outputs using filenames. A fully specified file name begins with a number, followed by an underscore, a letter, and another number.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/filename.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/2/filename.png)

*Example Tsunami filename.*

- The `first number` (before the underscore) assign the file to one of the trigger inputs.
- The `underscore (_)` keeps the track number from running into the output field.
- The `letter` after the underscore, S or L, specifies **S**ingle-shot or **L** ooping playback.
- The `second number` (after the underscore) assigns the file to one of the four stereo outputs.
- The `filename` (remainder of the name) is not required, but might be useful to remind you what the contents of the file are.

For instance, file `001_S1beep.wav` will sound when trigger 1 is activated, and play on output 1. The trigger inputs are numbered `001` through `016`, and the stereo outputs are `1` through `4`. If you want to alter the mapping between files, trigger inputs, and audio outputs, you can simply change the numbers in the file names.

#### Serial Protocol Output Mapping

Finally, when you trigger sounds using the [serial control protocol](http://robertsonics.com/tsunami-user-guide/#serial-control), the output is specified as part of the trigger message.

Unlike the trigger input and MIDI track assignments, the mapping can be assigned on-the-fly as sounds are triggered.

### Mono Playback Firmware

In these examples, we\'ve been using the [stereo (dual-channel)](https://en.wikipedia.org/wiki/Stereophonic_sound) version of the Tsunami firmware. There is an alternate version of the firmware that plays [monophonic (single-channel)](https://en.wikipedia.org/wiki/Monaural) files. It nearly doubles the maximum polyphony, from 18 to 32 simultaneous files, and the outputs become 8 individually-assignable outputs. The mono version also has an option for starting a group of tracks at the same time, mapped to sequential outputs. This allows mono mode to play stereo, quadrophonic, and surround material.

You can get the mono mode firmware from Robertsonics [download page](http://robertsonics.com/tsunami-downloads/). It\'s easy to load from the micro SD card if you follow [these instructions](http://robertsonics.com/tsunami-user-guide/#updating-the-firmware).

If Tsunami gets a mapping number it doesn\'t understand (a mapping to output #9, for instance), it usually ignores it, and uses the default setting for that parameter (9 would become 1).