# Source: https://learn.sparkfun.com/tutorials/little-soundie-audio-player-hookup-guide

## Introduction

The [Little Soundie](https://www.sparkfun.com/products/14006) is a fun and easy-to-use audio playback device breaking out [VLSI](http://www.vlsi.fi/)\'s [VS1000D](http://www.vlsi.fi/fileadmin/datasheets/vs1000.pdf) audio codec. The Little Soundie can decode ogg vorbis (license free) and WAV type files.

[![SparkFun Little Soundie Audio Player](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/7/9/0/14006-SparkFun_Little_Soundie_Audio_Player-01.jpg)](https://www.sparkfun.com/sparkfun-little-soundie-audio-player.html)

### [SparkFun Little Soundie Audio Player](https://www.sparkfun.com/sparkfun-little-soundie-audio-player.html) 

[ DEV-14006 ]

The Little Soundie is a tiny audio playback device breaking out the VS1000D audio codec IC allowing this board the ability to...

**Retired**

No programming is required to get started but it will help to know binary. There are only a couple steps to set up your Little Soundie:

- Connect to your computer using a micro-USB cable
- Press the power/play button
- Format the disk when prompted
- Drag and drop your .ogg or .wav files

From here, audio playback is a matter of attaching a powered speaker and triggering the GPIO pins at 3.3V logic.

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

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

### Suggested Reading and Viewing

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/binary)

### Binary 

Binary is the numeral system of electronics and programming\...so it must be important to learn. But, what is binary? How does it translate to other numeral systems like decimal?

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

You may also want to check out this [Audacity Tutorial](https://www.youtube.com/watch?v=aCisC3sHneM) on YouTube.

## Hardware Overview

[![Little Soundie Audio Player](https://cdn.sparkfun.com/r/400-400/assets/parts/1/1/7/9/0/14006-SparkFun_Little_Soundie_Audio_Player-04.jpg)](https://cdn.sparkfun.com/assets/parts/1/1/7/9/0/14006-SparkFun_Little_Soundie_Audio_Player-04.jpg)

### Details:

- VIN **3.3V-5.5V**
- All IO **3.3V** logic with pull down resistors (**not 5V tolerant**)
- Plays audio stored on 4 megabit (Mb) SPI Flash
- Load audio on USB Mass Storage
- Uses high-performance license-free Ogg Vorbis decoder for compressed audio
- Also plays .WAV type files
- Customizable
- Line-Out stereo analog output with SNR\>90dB
- Supports variable bit-rate and sample rates
- 6 GPIO for triggering audio playback (Binary Coded)
- Programming free!

Connect a micro-USB cable from the Little Soundie to a computer and press the \"Power/Play\" button. You should now see a mass storage device that you will need to format before you can drag and drop your audio files into. You can name your files whatever you want to - the audio files are assigned a number based on the order you place them on your Little Soundie. The hardware maps a GPIO pin to a specific audio file number.

**Warning:** You cannot power the Little Soundie through USB unless you are transferring files to the mass storage device. When a USB is inserted, the Little Soundie boots into USB mass storage mode and no audio files will play. Make sure to eject the storage device and remove it safely to avoid data corruption.

### Power/Play Button

The Power/Play button is exactly what it says it is. This button needs to pressed once after connecting to a computer and needs to be pressed once it is in a project. This button turns on the VS1000D which then triggers all the internal voltage regulators. The \"PB\" (Power Button) pin has been broken out in case you want to trigger that interaction hands-free or remotely. If your project gets stuck in an unknown state, pressing and holding the button down for 5 seconds will reset the VS1000D.

[![Power Play button](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/5/7/6/Button.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/6/Button.jpg)

### Trigger Pins

The trigger pins can be found on the left side of the board. A momentary connection to 3.3V will trigger the audio to playback. Leaving the pin high will cause the file to play on repeat. This is great for leaving a cricket in someone\'s office! In the Audio Files section this is outlined more exhaustively but a HIGH signal on pin 00 will trigger file 1, on 00 and 01 will trigger file 3, and on 00, 02, and 03 will trigger file 13.

[![Trigger Pins](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/5/7/6/GPIO.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/6/GPIO.jpg)

### 3.5mm Jack

The Little Soundie comes equipped with a 3.5mm jack for attaching a powered speaker. If this does not work for your application the AC coupled left and right channels have been broken out so you can amplify the signals individually. We recommend using the [Noisy Cricket](https://www.sparkfun.com/products/14475) and a speaker or transducer but you can also use two [SparkFun Mono Audio Amp Breakout](https://www.sparkfun.com/products/11044). The 3.5mm jack is not for headphones.

[![3.5mm jack](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/5/7/6/Audio.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/6/Audio.jpg)

### VSIDE Pins

If you wanted to change any functionality of the Little Soundie you will need [VSIDE](http://www.vlsi.fi/en/support/software/vside.html). VSIDE is an IDE for VSDSP signal processor chips like the VS100D. There are several example projects you can build from or simply use. Programming is through UART so you\'ll only need to connect TX, RX, VCC, and GND. You can even use one of our FTDI breakout boards.

[![VSIDE Pins](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/5/7/6/VsSide.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/6/VsSide.jpg)

*You do not need to reprogram your Little Soundie. The VS1000D programming pins are broken out if you wish to update the firmware in VSIDE.*

## Assembly Tips 

Very minimal assembly is required to get started.

[![Breadboard, little soundie, two sets of male headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/6/Little_Soundie_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/6/Little_Soundie_Hookup_Guide-01.jpg)

To connect the Little Soundie\'s 6 I/O pins to external components, apply power, connect audio out, and use the VS1000D programming pins, you\'ll need to do some soldering. It is much easier to solder when the headers are placed in the breadboard.

[![Soldering on the breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/6/Little_Soundie_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/6/Little_Soundie_Hookup_Guide-02.jpg)

For a flat project like a birthday card or a wearable gauntlet I\'d recommend soldering the [right angle headers](https://www.sparkfun.com/products/12792) instead.

[![Little Soundie with right angle headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/6/Little_Soundie_Hookup_Guide-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/6/Little_Soundie_Hookup_Guide-05.jpg)

## Audio Files

You can trigger about 20 files (2-3 seconds sound bites each) from the SPI flash storage (USB mass storage). The total SPI flash size is **4 megabits (Mb)** (*approximately a **.5 megabyte (MB)***). OGG files take up much less space than .WAV so I recommend using OGG if more then 5-6 sound bites are to be used.

**Quick Note about using WAV:** The VS1000 developer library contains a simple WAV decoder, which is included in the firmware on the Little Soundie. Currently the WAV decoder supports 8-bit ulaw, 8-bit linear PCM, and 16-bit linear PCM formats.

Ogg Vorbis is an audio file format developed by [xiph](https://xiph.org/about/), an open source multi-media company.

> Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free, general-purpose compressed audio format for mid to high quality (8kHz-48.0kHz, 16+ bit, polyphonic) audio and music at fixed and variable bitrates from 16 to 128 kbps/channel. This places Vorbis in the same competitive class as audio representations such as MPEG-4 (AAC), and similar to, but higher performance than MPEG-1/2 audio layer 3, MPEG-4 audio (TwinVQ), WMA and PAC.

*Information courtesy of xiph.org*

There are sites out there that will do the conversion for you without having to open a program, like [this](https://audio.online-convert.com/convert-to-ogg) one.

[Audacity](https://manual.audacityteam.org/#tutorials) is a great open source resource for all things audio that also has fantastic documentation.

There are several sound effects sites such as [Zapsplat](https://www.zapsplat.com/sound-effect-packs/) and [Soundbible](http://soundbible.com). You can grab license-free sound bites from these locations and then convert to .OGG or .WAV using the methods listed above.

### Binary Coded Playback

To get the most out of your device and trigger more sounds than there are available pins, the firmware is set up to trigger pins based on a binary code. The binary associates an audio file with a specific set of pins held either high or low. While the pin combinations on Little Soundie can trigger up to 64 files, it is likely you will only be able to fit about 20 .OGG files on the device. In the binary column below, the number represents which pins on the Little Soundie are pulled high and which pins are held low. Pin 04 is the first digit and pin 00 is the last. Pin 05 is there in case you want to reprogram the VS1000D to change the playback functions.

File No.

Binary/IO Pin State

1

00001

2

00010

3

00011

4

00100

5

00101

\...

16

10000

17

10001

18

10010

19

10011

20

10100

\

## Hardware Example

The Little Soundie includes *almost* everything you\'ll need to add sound effects to your project. You\'ll need, a USB cable to connect to your computer, a power supply of 3.3V to 5.5V, and either a button, a switch, or anything that will set a pin HIGH at 3.3V logic.

For this project you will need the following the parts:

### Load Your Audio Clip

Load the sound clips you wish to use for this project. Simply connect the board to your computer through USB and press the power/play button, drag and drop your audio files, and safely remove the hardware via your computer (don\'t just unplug it). Remove the USB. You can not power your project from the USB port - this causes the VS1000D to boot into \"**USB, Mass Storage Device**\" mode.

### Power

Since you can power your project from 3.3V to 5.5V, I used a LiPo battery to power this project. Keep in mind that the I/O is not 5V tolerant.

### Buttons

The Little Soundie\'s GPIO pins are connected to GND through pull-down resistors. This makes the hardware wiring a bit easier. For each switch connected to a GPIO pin you\'ll need to connect one side of the switch to a GPIO pin on the Little Soundie and the other side to the 3.3V rail. When the button is pressed the file corresponding to the pin(s) sent HIGH will trigger playback of the audio file. With this set-up it may appear as though you can only trigger 5 files, but you can actually trigger 32. Since the GPIO are binary coded, pressing button 1 will correspond to the first file saved to the drive. If the first and third buttons are pressed at the same time the fifth file saved to the drive will play. Remember - the naming conventions of your audio files does not matter; what matters is the order in which they are loaded onto the USB drive.

### Hardware Hookup

For a clearer look at the wiring hookup, see the Fritzing diagram below.

**Warning:** Do not strip your lithium battery\'s JST connector. Please use M/M jumpers to connect your lithium battery to the breadboard!

[![Little Soundie Fritzing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/6/LittleSoundieFritzing-V2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/6/LittleSoundieFritzing-V2.jpg)

*Having a hard time seeing the circuit? Click the image for a closer look!*

Once your wiring is set up, plug in a powered speaker to the 3.5mm jack. Alternatively, you can use the left and right audio signals that are broken out on a [Mono Amp Breakout Board](https://www.sparkfun.com/products/11044) or use the [Noisy Cricket](https://www.sparkfun.com/products/14475).

[![Little Soundie Hooked up](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/6/Little_Soundie_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/6/Little_Soundie_Hookup_Guide-03.jpg)

When you are all set up and ready to hear some sounds press the power/play button and you should hear a little pop in the speaker. This lets you know the VS1000D is powered and ready to go.

This project is easily extensible by replacing the buttons with connections to a microcontrollers I/O. Hands-free, sensor-based, or remote controlled sound effects are just a Pro-Mini and Arduino sketch away!

## Troubleshooting

### Little Soundie Not Working?

Try pressing the reset button for 5 seconds. If that doesn\'t work you can reflash the VS1000D using [VSIDE](http://www.vlsi.fi/en/support/software/vside.html).

[VLSI Software Page for VSIDE](http://www.vlsi.fi/en/support/software/vside.html)