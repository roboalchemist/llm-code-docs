# Source: https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player

## Introduction

The [LilyPad MP3 Player](https://www.sparkfun.com/products/11013) is an amazing little board that contains almost everything you need to play audio files. You just need to add a Lipo battery, speakers, and a micro-SD card with your audio files on it.

[![LilyPad MP3](https://cdn.sparkfun.com/r/600-600/assets/parts/6/2/9/8/11013-01a.jpg)](https://www.sparkfun.com/lilypad-mp3.html)

### [LilyPad MP3](https://www.sparkfun.com/lilypad-mp3.html) 

[ DEV-11013 ]

The LilyPad MP3 Player is your all-in-one audio solution, containing an Arduino-compatible microcontroller, MP3 (and many oth...

[ [\$56.50] ]

You can use the LilyPad MP3 Player to create all kinds of noisy projects; your imagination is the only limit!

[![LilyPad MP3 Player Connected](https://cdn.sparkfun.com/assets/9/7/b/6/5/518a939dce395fce37000000.jpg)](https://cdn.sparkfun.com/assets/9/7/b/6/5/518a939dce395fce37000000.jpg)

Before diving in, you should familiarize yourself with any of the following topics that will be covered in this tutorial, if you are not comfortable with them already.

- [How to install an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [Battery Technologies](https://learn.sparkfun.com/tutorials/battery-technologies)
- [Sewing with Conductive Thread](https://learn.sparkfun.com/tutorials/sewing-with-conductive-thread)
- [Using GitHub](https://learn.sparkfun.com/tutorials/using-github)

## Getting to Know the LilyPad MP3 Player

[![LilyPad MP3 Player](https://cdn.sparkfun.com/images/products/1/1/0/1/3/11013-01.jpg)](https://cdn.sparkfun.com/images/products/1/1/0/1/3/11013-01.jpg)

The LilyPad MP3 Player comes with preinstalled software called [**\"Trigger\"**](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/getting-started-with-the-default-trigger-sketch) that will play specific files when the input pins are grounded. You can also add an optional rotary encoder and load the [**\"Player\"**](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/getting-started-with-the-player-sketch) software to turn the board into a \"real\" audio player, or even [write your own software](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/writing-your-own-code) using the free Arduino programming environment.

### Anatomy of the LilyPad MP3 Player:

[![LilyPad MP3 Player connectors](https://cdn.sparkfun.com/assets/a/d/2/5/b/51785c42ce395f7110000003.png)](https://cdn.sparkfun.com/assets/a/d/2/5/b/51785c42ce395f7110000003.png)

Let\'s start with the connectors. You will normally power the board with a single-cell (3.7V) Lipo battery, which plugs into the two-pin **\"JST\" battery connector**. There is a **stereo headphone jack** that you can use to connect the board to a pair of headphones if desired. Connecting headphones will disable the speakers, but [you can change this behavior if you wish.](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/hardware-details#headphonejumper) (If you\'d like to connect the board to an external amplifier, see the special note [here.](#externalamplifier)) You can plug a 5V FTDI board or cable into the 6-pin **5V FTDI header**, to both recharge an attached Lipo battery and to reprogram the board if desired (see [this note](#ftdipower) about powering the board from USB). And finally, there is a **micro-SD card socket** into which you\'ll insert a micro-SD memory card containing the audio files you want to play.

[![LilyPad MP3 Player power switch and LEDs](https://cdn.sparkfun.com/assets/f/c/9/1/3/5178504fce395f1e10000000.png)](https://cdn.sparkfun.com/assets/f/c/9/1/3/5178504fce395f1e10000000.png)

The board contains a **power switch** that is used to turn the board on and off. There are also two LEDs; a **red power LED** that will light up when the board is powered on, and a **yellow charge LED**. The charge LED will light up when the battery is being charged, and go out when it is full. (It is also normal for the charge LED to turn on if no battery is attached.) You can charge the battery while the board is on or off, but the battery will charge faster if the board is off.

[![LilyPad MP3 Player I/O pins](https://cdn.sparkfun.com/assets/4/b/c/b/9/517859dfce395f530e000001.png)](https://cdn.sparkfun.com/assets/4/b/c/b/9/517859dfce395f530e000001.png)

The LilyPad MP3 Player has **twelve \"pins\"** (they\'re really holes, but they connect to pins on the microcontroller) that you\'ll use to connect to the outside world. For each pin, we\'ve provided both **\"sew taps\"** (large holes you can loop conductive thread around to use it in fabric projects), and standard **headers** (smaller holes that you can solder wires or [header pins](https://www.sparkfun.com/products/116) to if you wish).

Five of the pins are set up to be **triggers**, which you can use with the default software to trigger playback of specific audio files. (We\'ll learn more about this on the next page, [\"Using the default trigger sketch\"](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/getting-started-with-the-default-trigger-sketch).) Typically you\'ll connect triggers to switches that activate the playback of various audio files. Many of the triggers also have alternate functions, such as serial ports, that you can use to communicate with other devices in more complex projects. The alternate functions are listed in the table below.

You\'ll also use the pins to connect to external **speakers**. The LilyPad MP3 Player includes a stereo (two channel, left and right) amplifier that supports speakers between 4 and 8 ohms. Each speaker has two terminals, labeled \"+\" and \"-\". Normally you\'ll connect two speakers to the board, but you can also use just one speaker if you wish, or connect multiple speakers in series or parallel. Just don\'t connect the speaker pins to anything but a speaker or [transducer](https://www.sparkfun.com/search/results?term=surface+transducer&what=products).

Here is a table of the pins and their functions:

  ----------------- ----------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **pin name**      **function**                  **notes**
  VIN               Raw voltage in (3.5V to 6V)   If you don\'t want to connect a Lipo battery, you can use this pin to power the board from an external supply. If you want to also charge an attached Lipo battery, this input should be between 4.5V and 6V. You can read more about your options for powering the board [here](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/hardware-details#power).
  3.3V              Regulated 3.3V in or out      If you already have a regulated 3.3V supply, you can use this pin to power the board. (Powering the board through this pin will not charge the battery.) You can also pull 3.3V power out of this pin if you need it somewhere else.
  GND               Ground (0V)                   Use as a power ground, and also for the return side of your trigger switches (see the diagram [here](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/building-the-board-into-your-project)).
  T1                Trigger 1                     General purpose I/O pin (Arduino pin A0). You\'ll usually connect this through a switch to ground. Can also be used as an analog input.
  T2                Trigger 2 / SDA               General purpose I/O pin (Arduino pin A4). You\'ll usually connect this through a switch to ground. Can also be used as SDA (serial data) in an I2C (\"wire\" library) connection (4.7K pullup included), or an analog input if the pullup is disabled.
  T3                Trigger 3 / SCL               General purpose I/O pin (Arduino pin A5). You\'ll usually connect this through a switch to ground. Can also be used as SCL (serial clock) in an I2C (\"wire\" library) connection (4.7K pullup included), or an analog input [if the pullup is disabled](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/hardware-details#pullupdisable).
  T4                Trigger 4 / TX                General purpose I/O pin (Arduino pin D1). You\'ll usually connect this through a switch to ground. Can also be used as TX (transmit) in a serial connection. Do not permanently pull this pin low or reprogramming and serial monitoring will be disabled.
  T5                Trigger 5 / RX                General purpose I/O pin (Arduino pin D0). You\'ll usually connect this through a switch to ground. Can also be used as RX (receive) in a serial connection. Do not permanently pull this pin low or reprogramming and serial monitoring will be disabled.
  Right Speaker +   Right Speaker +               Connect to the right speaker + terminal. Only connect to a speaker or other coil-based transducer. Do not short to power, ground, or any other signal.
  Right Speaker -   Right Speaker -               Connect to the right speaker - terminal. Only connect to a speaker or other coil-based transducer. Do not short to power, ground, or any other signal.
  Left Speaker +    Left Speaker +                Connect to the left speaker + terminal. Only connect to a speaker or other coil-based transducer. Do not short to power, ground, or any other signal.
  Left Speaker -    Left Speaker -                Connect to the left speaker - terminal. Only connect to a speaker or other coil-based transducer. Do not short to power, ground, or any other signal.
  ----------------- ----------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You may have noticed the unused footprint in the middle of the board. That is there to allow you to add an optional **RGB rotary encoder** if you wish. You won\'t need it to run the preinstalled \"Trigger\" software, but if you want to turn the LilyPad MP3 Player into a true audio player, the rotary encoder provides a simple user interface to switch tracks and change the volume. See the [\"Getting started with the player sketch\"](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/getting-started-with-the-player-sketch) page for more information.

[![LilyPad MP3 Player hardware](https://cdn.sparkfun.com/assets/5/1/d/b/8/5178650ece395f2d0d000000.png)](https://cdn.sparkfun.com/assets/5/1/d/b/8/5178650ece395f2d0d000000.png)

In case you\'re interested in the hardware on the board, there is an **ATmega 328p microprocessor**, running Arduino software that pulls data from audio files on the micro-SD card and feeds that data to the **VS1053B audio-decoding chip**. The VS1053B transforms the digital audio data back into analog audio signals. The audio signals are sent to the headphone jack and a **TPA2016D2 stereo amplifier**, which boosts the audio signal for the speakers. We also threw in a **MCP73831 Lipo battery charger** to make it easy to recharge the battery from the FTDI port. Neat, huh?

### Tips on speaker selection

The TPA2016D2 stereo amplifier on the LilyPad MP3 Player is capable of driving about a watt of power into each channel. This doesn\'t sound like much, but it can produce surprising volume from a large speaker.

In general, larger speakers will sound better than small ones, so use the largest ones that your project will accommodate. Don\'t worry that the speaker is marked \"20 watts\" or higher; that is just the maximum power that the speaker is designed to handle. We\'ve had great results with recycled automotive and PC speakers, and even large cabinet speakers.

If your project requires a small speaker, remember that any small speaker will sound much better if it has an enclosed cavity behind it. You can do this with a project enclosure, recycled food containers, etc. Use your imagination!

### Some important things to know:

- Always turn the LilyPad MP3 Player off before inserting or removing the micro-SD card. This will prevent corruption of the data on the card.

- []The 5V FTDI port is provided to charge an attached Lipo battery, and provide a way to reprogram the board. It will power the board if no audio is playing, but will not provide enough power to drive the speakers (the board will reset while playing). In general, the best way to power the LilyPad MP3 Player is with a Lipo battery. If you\'d like to use an external supply, see the instructions [here](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/hardware-details#power), and if you *really* want to run the board from FTDI power [you can hack it to do so.](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/hardware-details#ftdihack)

- To recharge an attached Lipo battery, plug a [5V FTDI Basic](https://www.sparkfun.com/products/9716) or [cable](https://www.sparkfun.com/products/9718) into the 6-pin FTDI connector. Match up the direction of your FTDI board or cable with the \"GRN\" and \"BLK\" markings on either side of the connector. The yellow \"Charge\" light will turn on while the battery is charging and turn off when it\'s fully charged. It\'s normal for the charge light to turn on if no battery is attached. The charge rate is set to 500mA, which means that a 1000mAh battery will charge in about two hours. If you\'d like to change the charge rate, see the instructions [here](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/hardware-details#chargerate).

- []The LilyPad MP3 Player\'s headphone jack is safe for headphones, but don\'t connect it to an external amplifier unless you\'re using a battery to power the LilyPad. (The fine print is that if the audio ground is shorted to the power ground, the audio decoder chip will be damaged).

- The VS1053B chip understands a large variety of audio file formats, but we\'ll occasionally run into one it can\'t play back (it will quietly skip it). See the list of formats and bitrates it understands [here](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/supported-audio-formats). If you do run into a file it has problems with, you can often fix the problem by translating the file into a different format using the audio software of your choice.

- The LilyPad MP3 Player is washable, but because conductive thread connections can be fragile, we recommend washing your project as little as possible. Please hand-wash, and be sure to remove the Lipo battery and micro-SD card before washing. Because water can get into lots of little crevices, allow everything to air-dry for several days before powering it up again.

**With that out of the way, let\'s start playing audio!**

## Getting Started with the Default \"Trigger\" Sketch

The LilyPad MP3 Player comes with a preinstalled sketch (Arduino programs are called sketches) called **\"Trigger\"**. This sketch will wait for one of the five trigger inputs to be grounded and will then play the corresponding audio file from the micro-SD card. You can sew the LilyPad MP3 Player into your project and use \"soft switches\" to trigger any sound you want. Best of all, since this sketch comes preinstalled on every LilyPad MP3 Player, you can use it right out of the box, with no programming necessary. Let\'s get started!

### Required Materials

- A [single-cell (3.7V) Lipo battery](https://www.sparkfun.com/search/results?term=polymer+lithium+ion+battery&what=products) (500mAh or above recommended. You can use smaller ones if you reduce the charge rate, see the instructions [here](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/hardware-details#chargerate)).

- A [5V FTDI Breakout](https://www.sparkfun.com/products/9716) or [cable](https://www.sparkfun.com/products/9718) (to recharge the battery and reprogram the board if desired).

- One or two 4 or 8-ohm [speakers](https://www.sparkfun.com/search/results?term=speaker&what=products), [surface transducers](https://www.sparkfun.com/search/results?term=surface+transducer&what=products), or headphones with a 1/8\" stereo jack. If you want to connect the LilyPad MP3 Player to an amplifier, see this [note](#externalamplifier).

- [Conductive thread and sewing supplies](https://www.sparkfun.com/search/results?term=conductive+thread&what=products), or [hook-up wire](https://www.sparkfun.com/search/results?term=hook-up+wire&what=products) and [soldering tools](https://www.sparkfun.com/products/11101). (**TIP:** [alligator cables](https://www.sparkfun.com/products/11037) are a great way to quickly test out circuits and programming before committing to needle and thread!)

- A [micro-SD card](https://www.sparkfun.com/products/11609).

- Some audio files you\'d like to play. The LilyPad MP3 Player can play many audio formats, you can see the whole list [here](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/supported-audio-formats).

### Instructions

1.  Put up to five audio files onto the micro-SD card. Usually this is done by putting the card into a reader attached to your computer and copying audio files to it. The LilyPad MP3 Player will play a number of audio formats including MP3, WAV, WMA, AAC, MID, etc.

2.  Rename the audio files on the micro-SD card so that the first character of each filename is the number \"1\" to \"5\", corresponding to the trigger that you want to play that file. You don\'t need to change anything else about the filename.

3.  Turn off the LilyPad MP3 Player and plug your micro-SD card into the socket. Push it in until it clicks; if you release it, it will stay seated. To remove it, push again until it clicks, and it will pop out when you release it.

    ::: 
    [![MicroSD Card inserted into socket](https://cdn.sparkfun.com/assets/b/a/1/c/4/517ae754ce395ffc48000001.png)](https://cdn.sparkfun.com/assets/b/a/1/c/4/517ae754ce395ffc48000001.png)
    :::

4.  Connect a headphone to the headphone jack, **or** connect speakers to the left and right speaker terminals. *(Note that when anything is plugged into the headphone jack, the speakers are disabled. [This behavior can be changed if desired](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/hardware-details#headphonejumper)).*

    ::: 
    [![Speakers](https://cdn.sparkfun.com/assets/e/6/2/3/7/517ae77fce395f0949000000.png)](https://cdn.sparkfun.com/assets/e/6/2/3/7/517ae77fce395f0949000000.png)
    :::

5.  Plug a 3.7V single-cell Lipo battery into the JST connector. Note that a FTDI USB connection will not provide enough power to run the board, so a battery or other external power source is required.

    ::: 
    [![LiPo Battery](https://cdn.sparkfun.com/assets/1/a/b/4/4/517ae451ce395fbe48000000.png)](https://cdn.sparkfun.com/assets/1/a/b/4/4/517ae451ce395fbe48000000.png)
    :::

6.  Move the power switch to ON. The red LED should light up.

7.  Wait a few seconds for the software to start up. Now, momentarily, connect the ground sew tap (marked GND) to one of the trigger terminals (marked T1 through T5). The audio file associated with that terminal should play through the speakers / headphone. If you don\'t hear anything, see the [troubleshooting page](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/troubleshooting).

    ::: 
    [![Triggering a Pin](https://cdn.sparkfun.com/assets/4/8/2/1/3/517ae947ce395fef48000000.png)](https://cdn.sparkfun.com/assets/4/8/2/1/3/517ae947ce395fef48000000.png)
    :::

8.  To charge the battery or reprogram the board, connect a 5 volt FTDI board to the FTDI header. The yellow LED will light up while the battery is charging, and go out when it\'s full. To reprogram the board, see the instructions [here](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/writing-your-own-code).

9.  Have fun!

Now that you know how the trigger sketch works, [it\'s time to think about what you\'ll do with it.](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/building-the-board-into-your-project)

### Tips

The Trigger sketch has several software settings within it that control whether triggers can restart an already playing clip, send debugging information to the serial monitor window, etc. You can easily change these settings if desired, or make any other changes you wish to the sketch, by using the free Arduino programming environment. See the [programming page](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/writing-your-own-code) for more information.

## Building the Board into Your Project

Now that you know how it works, it\'s time to think about building the board into your dream project. The LilyPad MP3 Player is equally at home with conductive thread or soldered wire connections, so you can use it in \"soft\" or more traditional projects.

If this is your first time doing a fabric project, take a look at our [Beginning LilyPad Arduino tutorial](https://www.sparkfun.com/tutorials/312). It will give you an overview of the techniques you\'ll use working with LilyPad components and sewing with conductive thread.

### Triggers

Electrically, we\'ll be connecting each trigger to a momentary switch, with the opposite side of the switch connected to ground. Because the switch is normally open, the trigger pin will be disconnected from ground and will \"float\" to a \"high\" state (3.3V) because of a pull-up resistor on the board.

[![Connecting the triggers](https://cdn.sparkfun.com/assets/3/7/0/7/c/5179c78fce395f540a000000.png)](https://cdn.sparkfun.com/assets/3/7/0/7/c/5179c78fce395f540a000000.png)

When you activate a switch, the trigger will be connected to ground, which is \"low\" or 0V. The software knows that when a trigger is low, it\'s time to play the proper audio file.

Note that the very low voltages the LilyPad MP3 Player uses are **completely safe**. You can touch anything on the board without fear of damaging yourself or the board.

### Switches

You can certainly use hardware switches if you wish. If you\'re doing a fabric project, you may want to use a **soft switch**. A soft switch acts just like its hardware cousin, but it is made with conductive thread or fabric. The conductive areas are normally separated, but when you press / brush against / twist / fold the switch, the conductive surfaces touch each other and conduct electricity. There are lots of ways to make soft switches, and because this field is so new there is lots of room for new ideas. Invent someting amazing! [Here\'s one example](https://www.sparkfun.com/tutorials/306) where SparkFun engineer Dia made a soft switch that looks like a flower that you brush against to activate.

Because there are five triggers, you can have up to five soft switches. You\'ll run each trigger to one side of a switch. The other side of each soft switch will be connected to ground. You can run one ground line to all the switches.

### Speakers

The only other lines you need to run are to the speakers. Remember that these lines should only be attached to real speakers or other coil-based transducers; if you need an analog audio output, use the headphone jack. As the speakers use more current than the switches, you should make the speaker connections a bit beefier than the others. Be careful not to short the speaker lines together or to any other connection, and be careful about loose threads at the \"Left Speaker -\" connection which is close to the 5V FTDI header.

[![Triggers and speakers - everything you need](https://cdn.sparkfun.com/assets/3/e/a/5/f/5179c78fce395f110b000000.png)](https://cdn.sparkfun.com/assets/3/e/a/5/f/5179c78fce395f110b000000.png)

### Battery

To keep the battery from flopping around and possibly breaking its wires, we recommend sewing a little pocket to hold it snugly. Don\'t sew it in permanently; you may need to remove it for washing or replacement. Speaking of which\...

### Washing

The LilyPad MP3 Player is washable, but because conductive thread connections can be fragile, we recommend washing your project as little as possible. Please hand-wash, and be sure to remove the Lipo battery and micro-SD card before washing. Because water can get into lots of little crevices, allow everything to air-dry for several days before powering it up again.

## Getting Started with the \"Player\" Sketch

The \"Player\" sketch is *not* preprogrammed onto the LilyPad MP3 Player, but you can easily install it using the free Arduino IDE. It is included with the LilyPad MP3 software that you can download from the [GitHub page](https://github.com/sparkfun/LilyPad_MP3_Player/tree/master/Arduino/LilyPad%20MP3%20Player).

The Player sketch turns the LilyPad MP3 Player into a \"real\" audio player, allowing you to easily switch between tracks and change the volume. The user interface is a [rotary encoder](https://www.sparkfun.com/products/10982) (a knob with a built-in pushbutton) available separately from SparkFun.com that you can solder onto the LilyPad MP3 Player board.

*If you plan on using the player sketch and rotary encoder, be sure to install the rotary encoder **before** sewing the LilyPad MP3 Player into your project. This because you\'ll need access to the back of the board to install the encoder.*

### Required Materials

- [RGB Rotary Encoder](https://www.sparkfun.com/products/10982)

- [Clear Plastic Knob](https://www.sparkfun.com/products/10597) *(Optional)*

- Soldering tools *([soldering tools](https://www.sparkfun.com/products/11101) (i.e. soldering iron, solder, safety glasses, etc.))*

- A [single-cell (3.7V) Lipo battery](https://www.sparkfun.com/search/results?term=polymer+lithium+ion+battery&what=products) (500mAh or above recommended. You can use smaller ones if you reduce the charge rate, see the instructions [here](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/hardware-details#chargerate)).

- A [5V FTDI BOB](https://www.sparkfun.com/products/9716) or [cable](https://www.sparkfun.com/products/9718) (to recharge the battery and reprogram the board if desired).

- One or two 4 or 8-ohm [speakers](https://www.sparkfun.com/search/results?term=speaker&what=products), [surface transducers](https://www.sparkfun.com/search/results?term=surface+transducer&what=products) or headphones with a 1/8\" stereo jack. If you want to connect the LilyPad MP3 Player to an amplifier, see this [note](#externalamplifier).

- [Conductive thread and sewing supplies](https://www.sparkfun.com/search/results?term=conductive+thread&what=products), or [hook-up wire](https://www.sparkfun.com/search/results?term=hook-up+wire&what=products) and [soldering tools](https://www.sparkfun.com/products/11101). *(**TIP:** [alligator cables](https://www.sparkfun.com/products/11037) are a great way to quickly test out circuits and programming before committing to needle and thread!)*

- A [micro-SD card](https://www.sparkfun.com/products/11609).

- Some audio files you\'d like to play. The LilyPad MP3 Player can play many audio formats, you can see the whole list [here](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/supported-audio-formats).

[![alt text](https://cdn.sparkfun.com/assets/b/a/5/2/0/5182f412ce395f7832000000.jpg)](https://cdn.sparkfun.com/assets/b/a/5/2/0/5182f412ce395f7832000000.jpg)

### Instructions

1.  Install the rotary encoder.

    - Insert the Rotary Encoder\'s pins into the holes in the center of the LilyPad MP3 Player. Note that it goes into the \"top\" side of the board (the side with the silkscreen that indicates where the encoder goes).

    ::: 
    [![Inserting Rotary Encoder into Board](https://cdn.sparkfun.com/assets/0/6/7/c/e/5182f412ce395fe231000000.jpg)](https://cdn.sparkfun.com/assets/0/6/7/c/e/5182f412ce395fe231000000.jpg)
    :::

    - Flip the board over, and solder the encoder\'s pins to the board.

    ::: 
    [![Solder Encoder Pins](https://cdn.sparkfun.com/assets/e/c/f/6/1/5182f40dce395f6d32000001.jpg)](https://cdn.sparkfun.com/assets/e/c/f/6/1/5182f40dce395f6d32000001.jpg)
    :::

    - *Optional*: place the knob onto the rotary encoder shaft. That\'s it!

    ::: 
    [![Rotary Encoder with Knob](https://cdn.sparkfun.com/assets/9/1/b/a/2/5182f413ce395fd932000003.jpg)](https://cdn.sparkfun.com/assets/9/1/b/a/2/5182f413ce395fd932000003.jpg)
    :::

2.  Install the Arduino software.

    - If you haven\'t, download and install the free Arduino IDE (Integrated Deveopment Environment) available from [www.arduino.cc](www.arduino.cc). Follow the instructions there for your type of computer and operating system.

    - Plug your FTDI board or cable into your computer. The drivers should install automatically. If they don\'t, see the instructions at [www.arduino.cc](www.arduino.cc) for your computer and operating system.

3.  Install the LilyPad MP3 Player libraries.

    - Download the latest LilyPad MP3 Player software from the [product page](https://www.sparkfun.com/products/11013) at SparkFun.com.

    - Open the archive, and drag the contents of the \"Arduino\" folder into your personal Arduino sketches directory (this is usually called \"Arduino\" and will be in your documents folder). This will install a \"libraries\" folder with several new libraries, and a \"LilyPad MP3 Player\" folder with example code.

    - If it\'s running, restart the Arduino IDE.

4.  Upload the \"Player\" sketch.

    - Connect a Lipo battery (or other power source) to the LilyPad MP3 Player.

    - Connect your 5V FTDI board or cable to the LilyPad MP3 Player. (The yellow \"charge\" LED may light up, that\'s fine.)

    - Turn on the LilyPad MP3 Player\'s power switch. The red LED should light up.

    - Start the Arduino IDE, and load the \"Player\" sketch from the \"LilyPad MP3 Player\" folder.

    - From the IDE\'s \"Tools/Board\" menu, select \"Arduino Pro or Pro Mini (3.3V/8MHz) w/ATmega 328\"

    - From the IDE\'s \"Tools/Serial Port\" menu, select the port that your FTDI board or cable is using. This is usually the highest number; you can be sure if you unplug the FTDI and the number disappears.

    - Upload the \"Player\" sketch to the LilyPad MP3 Player. If you have compilation problems, double-check that the required libraries were installed correctly from step 3 above.

    - Once the code is loaded and running, the RGB LED on the rotary encoder will blink if there is no micro-SD card installed. This is normal.

5.  Place the audio files of your choice on a micro-SD card.

    - The LilyPad MP3 Player understands a wide variety of [audio types](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/supported-audio-formats). The filenames can be anything as long as they use one of the standard file extensions (MP3, WAV, AAC, MID, etc.).

    - The only limit to the number of audio tracks you can have on your SD card is its storage capacity.

6.  Turn off the LilyPad MP3 Player, and plug your micro-SD card into the socket.

    - Push it in until it clicks; if you release it, it will stay seated. To remove it, push again until it clicks, and it will pop out when you release it.

7.  Connect a headphone to the headphone jack, or connect speakers to the left and right speaker terminals. (Note that when anything is plugged into the headphone jack, the speaker terminals are disabled. This behavior can be [changed if desired](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/hardware-details#headphonejumpers).

    - **TIP:** [alligator cables](https://www.sparkfun.com/products/11037) are a great way to quickly test out circuits and programming before committing to needle and thread!\
      \

8.  Plug a 3.7V single-cell Lipo battery into the JST connector. Note that a FTDI USB connection will not provide enough power to run the board, so a battery or other external power source is required.

9.  Turn the power switch ON. The red LED should light up, and after a few seconds, the rotary encoder will turn red, indicating the player is in \"track\" mode. (If the rotary encoder blinks, there was a startup problem, see the [troubleshooting page](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/troubleshooting) for help.)

    ::: 
    [![LiPo Battery Inserted](https://cdn.sparkfun.com/assets/5/a/5/b/f/51834a39ce395fe731000000.png)](https://cdn.sparkfun.com/assets/5/a/5/b/f/51834a39ce395fe731000000.png)
    :::

10. Play music! Here\'s how:

    - At any time, to start and stop playback, **briefly** press the rotary encoder button. When a track has finished playing, the next track will automatically start.

    - To switch between \"track\" and \"volume\" modes, **hold the rotary encoder button down for one second** until the color changes. Red = track mode, green = volume mode.

    - In track mode, you can turn the knob forwards or backwards to change tracks (one track per \"click\" of the knob). If you\'re currently playing, turning the knob will stop the current track, switch to the next / previous one, and start the new track. If you\'re not playing, the player will silently keep track of how many clicks you\'ve made. If you click more than the number of tracks on the card, it will loop around to the beginning.

    - In volume mode, you can turn the knob forwards or backwards to change the volume.

11. To charge the battery or reprogram the board, connect a 5 volt FTDI board or cable to the FTDI header. The yellow LED will light up while the battery is charging and go out when it\'s full.

12. Have fun!

## Hardware Details and Hacking Tips

### []Power options and hacks

You can power the LilyPad MP3 Player in several ways:

#### Lipo battery

The easiest option is to use a Lipo (Lithium-Polymer) battery. SparkFun carries these in [several sizes](https://www.sparkfun.com/search/results?term=lithium+polymer+battery&what=products), which translates into different run times.

It is recommended that you use a Lipo battery of at least 500mAh, to match the default 500mA rate of the built-in Lipo charger (this is also the maximum current available from most USB ports). SparkFun Lipo batteries have a maximum charge rate of 1C, which means you shouldn\'t charge them faster than one hour. 500mA will charge a 500mAh battery in one hour, a 1000mAh battery in two hours, etc. A battery smaller than 500mAh would charge in less than one hour, which could cause the battery to overheat and possibly be damaged.

#### Unregulated 3.7V to 6V source

If you have an external 3.7V to 6V source, you have two options:

If you want to use your power source to recharge an attached Lipo battery, you can attach it to the \"VIN\" sew tap. Note that to recharge a battery the voltage must be greater than 4.5V (but still less than 6V).

If you want to use your power source to run the LilyPad MP3 Player directly (without a battery), connect it to the JST battery connector or the headers directly behind it. SparkFun carries [pigtails](https://www.sparkfun.com/products/8670) (a connector with bare wires) that match this connector. Note that if you connect a 5V FTDI to the board, a maximum of 4.2V will appear at this connector as the charger attempts to charge the missing battery.

#### Regulated 3.3V source

If you have an external regulated 3.3V source, you can use it by connecting it to the 3.3V sew tap. Note that this will not charge an attached Lipo battery. You can also pull regulated 3.3V out of this sew tap to power other items in your project.

#### Current requirements[]

Because the amplifier chip can pull quite a bit of power at full volume, ensure that any external supply you use can supply up to a few hundred mA. With lower volume levels, you can get away with 50-100mA.

#### []Changing the charge rate

If you would like to use a battery smaller than 500mAh, you can do so by soldering a new charge-rate resistor to the board. A through-hole footprint is provided in the white box marked R1 near the power switch.

You will need a through-hole resistor of the proper resistance. The formula to use is R = 1000/amps. For the given 500mA charge rate, the provided resistor is 1000/0.5 amps, or 2000 ohms. For a 110mAh battery, the resistor would be 1000/0.4 or 9090 ohms. (There is no standard 9090-ohm resistor, so use the next larger standard size which would be 10k.)

Before soldering on the new resistor, remove the existing surface-mount resistor within the white box. You can remove it by carefully heating it up with a soldering iron and nudging it off the pads when the solder softens.

#### Hacking for FTDI power

We said earlier that you can\'t power the LilyPad MP3 Player solely from a 5V FTDI board or cable. This is because the FTDI connector is used to charge the battery, and the limited current isn\'t enough to run the whole system including the amplifier (which can draw quite a bit of power).

However, you *can* modify the board to allow it to be powered via FTDI. Note that if you do this, you\'ll be bypassing the charge circuitry, so you won\'t be able to connect a Lipo battery to the board. If you\'d rather run the board from an FTDI than a battery, here\'s how to modify the board.

***NOTE: once you make this modification, do not connect a Lipo battery to the board. This modification sends 5V to the battery connector, which would overcharge an attached battery. Damage or fire may result.***

To modify the board for power from the 5V FTDI header, solder a jumper wire between the VIN sew tap (you can use the small header hole directly behind it) and the \"+\" header on the JST battery connector. This sends 5V from the FTDI connector to the power input of the board, bypassing the charge circuitry that limits the current. Once you do this, you\'ll be able to power the board from the FTDI connector. Did we mention not to connect a Lipo battery to the board after you make this modification?

### Solder jumpers

There are several solder jumpers on the board that you can use to alter its behavior. You probably won\'t need them, but they\'re there if you\'re ambitious.

#### I2C pullups (SJ1 and SJ2)[]

The TPA2016D2 amplifier chip has an I2C (\"wire\" library) interface that can be used to alter various settings on the chip. This interface is connected to the ATmega328 and is also sent to trigger 2 and trigger 3 in case you want to use external I2C sensors such as accelerometers, gyroscopes, etc.

In the example sketches, the I2C interface is normally disabled and generally shouldn\'t interfere with the use of trigger 2 or trigger 3. However, if you\'d like to absolutely separate trigger 2 and trigger 3 from the amplifier chip and 4.7K pullup resistors, you can do so by cutting SJ1 and SJ2.

These jumpers are normally connected (there\'s a thin trace running between the pads). If you want to sever the I2C connection to the amplifier, carefully cut the traces between the pads using a hobby knife. If you\'d like to restore the connection later, use a blob of solder to reconnect the two pads.

#### Serial MIDI connection (SJ3)

SJ3 (on the bottom of the board) can be used to connect the serial RX line (trigger 5) to the serial RX pin of the VS1053B audio decoder chip. This will let you send serial MIDI data directly from trigger 5 to the audio decoder.

**Please note** that without changing this jumper, you can still play MIDI files from the SD card just like any other audio file. This jumper is only useful if you have an external MIDI source such as a keyboard that you might want to connect directly to the LilyPad MP3 Player.

#### Headphone jack speaker cutoff (SJ4 and SJ5)[]

Normally, when you plug headphones into the jack, the audio signal to the amplifier chip and speakers will be interrupted by switches built into the jack. If you would rather have audio go to both the headphone jack and amplifier, you can close solder jacks SJ4 and SJ5 on the bottom of the board.

### Even more headers

If you need more I/O than the five trigger pins, and you\'re not going to be using a rotary encoder, you can take advantage of the unused rotary encoder connections in the center of the board. The following diagram shows the location of these pins and their functions. Feel free to use them in your project:

[![alt text](https://cdn.sparkfun.com/assets/1/6/5/b/2/519d68dfce395fbf43000000.png)](https://cdn.sparkfun.com/assets/1/6/5/b/2/519d68dfce395fbf43000000.png)

In addition to the rotary encoder header, there are several additional pins available on the six-pin ISP (In-System Programming) connector. This connector is normally used to perform bare-metal programming of the ATmega microprocessor (such as replacing the bootloader) using a compatible ISP [programmer](https://www.sparkfun.com/products/9825). You can use these pins for your own purposes, but **be aware** that the SPI interface (the MOSI, MISO and SCK pins) is already heavily used by the playback software to move data from the micro-SD card to the VS1053B chip.

But all is not lost! If you want to use the SPI interface for other purposes, such as driving an addressable LED string, you can do so if you\'re careful. Bill Porter\'s MP3 Player library will let you use the SPI pins *between audio transfers*, as long as you\'re quick about it and release the SPI port in time for the next data transfer to take place. (If you don\'t, the VS1053B will run out of buffered data and \"starve\", causing a gap or glitch in the playback.) See Bill\'s [documentation](http://www.billporter.info/2012/01/28/sparkfun-mp3-shield-arduino-library/) for instructions on how to do this, and have fun!

## Troubleshooting

If you don\'t hear anything, hopefully the following list will help you find the problem.

### Serial debugging

A big troubleshooting tip for almost any issue, is that both the \"Trigger\" and \"Player\" sketches have an option in the code to send debugging output to the serial port. When this is turned on (\"true\"), text messages will be output to the serial port describing what the board is doing at any given time, as well as any problems it finds. Serial debugging is turned on by default in the \"Player\" sketch. To turn on serial debugging in the \"Trigger\" sketch, follow these steps:

    * Open the "Trigger" sketch in the Arduino IDE (see the programming page for more information)
    * There will be a line near the top that says "debugging = false"
    * Change "false" to "true"
    * Upload the modified sketch
    * In the IDE, turn on the Serial Monitor window
    * Set the baud rate to 9600
    * The board will reset and status messages should appear in the Serial Monitor window

The information printed to the window will give you a lot of visibility into what\'s going on within the board. NOTE that when using serial debugging in the \"Trigger\" sketch, triggers 4 and 5 are deactivated (since those pins are used for serial input and output).

### Problems with the SD card:

- Did you remember to plug your micro-SD card into the LilyPad MP3 Player? (We do it too.)

- If the LilyPad MP3 Player has a problem starting up, it will output blink codes through the rotary encoder LED. If you don\'t have the rotary encoder installed, you can temporarily stick a normal LED into the five-pin row of holes in the middle of the board (use the two end holes, and put the longer lead towards the SparkFun logo). One blink = SD card problem. More blinks = MP3 decoder problem. See the comments in the sketch for more information.

- If you\'re using the default \"Trigger\" sketch, ensure that your filenames have a \'1\' to \'5\' as the first character.

- If you\'re using the \"Player\" sketch, ensure that your filenames have one of the following extensions: \"MP3\", \"WAV\", \"MID\", \"MP4\", \"WMA\", \"FLA\", \"OGG\", \"AAC\". Note that the VS1053 itself does not care what the filename is (you can use any of those on any file); the sketch just checks the extension to avoid sending non-audio data to the chip in case there are other files on the SD card.

- Ensure that your files are supported audio formats and bitrates. See the [supported audio formats page](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/supported-audio-formats) more information.

- If your file format isn\'t supported, you can often load that file into an audio editor program, and re-save it as a supported file type.

### Problems with the triggers:

- Try using an alligator cable or jumper wire to manually bridge the ground-trigger connection. This will help you determine whether the problem is in the board or in your switch.

- If you have serial debugging turned on in the sketch, triggers 4 and 5 will be disabled (these triggers are also used for the TX and RX lines).

### Problems with the speakers:

- Plug in headphones and see if you can hear any sound that way.

- Note that when you plug in headphones, the speakers will be disabled. [You can change this behavior if you wish.](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/hardware-details#headphonejumper)

- Try using alligator cables to connect directly from the LilyPad MP3 Player to your speakers.

- If you\'re writing your own code, ensure you don\'t have the amplifier disabled using the shutdown signal (EN_GPIO1, which is on A2). This signal should be HIGH to activate the amplifier.

- Note that this amplifier chip has a feature that slowly ramps up the volume when it\'s first turned on.

### Power problems:

- Do you have a power source connected, and is the power switch turned on? (The red power LED should be on).

- If playback starts but stops in the middle, ensure you\'re using a fully-charged battery.

- Remember that the 5V FTDI will power the board enough to program it, but not enough to drive the speakers. You must use a Lipo battery or other external power source.

- The battery charge chip (located between the 3.3V pin and the right speaker + pin) will get warm while charging a battery, especially if the battery is empty. This is normal. It will cool down as the battery is filled.

### Pause before playing?

- A customer called us with a strange problem: their LilyPad MP3 Player was playing audio files, but only after a long pause. The same files played normally on a PC. After looking at their files, we realized that the files contained an image of the album cover as part of the metadata. Since this data is at the beginning of the file, the VS1053 chip had to read through (and ignore) all the image data before getting to the actual audio data. Loading the audio files into Audacity and saving them back out without the metadata fixed the problem.

### Still having problems?

If you still can\'t get it working, please contact our [Technical Support Department](https://www.sparkfun.com/static/technical_assistance), who will be happy to help you out.

## Supported Audio Formats

The VS1053B audio decoding chip built into the LilyPad MP3 Player understands a wide variety of audio file formats. Occasionally you\'ll run into something it can\'t play; in that case you can often load it into the audio-editing software of your choice and \"save as\" a different format.

Below is a summary of the audio formats that the VS1053B understands, along with the common filename extensions for those formats. Note that the \"player\" sketch checks each file to ensure that it has one of these extensions: MP3, WAV, // MID (MIDI), MP4, WMA, AAC, FLA, OGG, but this is solely to avoid sending non-audio data to the VS1053B from other files that may be on your micro-SD card. The chip itself doesn\'t care about the extension. If you\'re using the player sketch, you can always rename your audio files to *any* of the above extensions.

This is only a summary. For much more detail see the [VS1053B datasheet](http://www.sparkfun.com/datasheets/Components/SMD/vs1053.pdf).

**MPEG layer III (.MP3)**

    language:bash
    Two channels max
    Sample rates: 8 through 48 kHz
    Bitrates: 32 through 320 kbit/s
    Variable bit rate (VBR) supported
    Layer I and II also supported with additional setup, see the VS1053B datasheet for more information.

**Ogg Vorbis (.OGG)**

    language:bash
    Two channels max
    Window size: 64 - 4096 samples
    Sample rate: 48 kHz max
    Bitrate: 500 kbit/s max

**AAC (.AAC .MP4 .M4A)**

    language:bash
    Two channels max
    Sample rates from 8 kHz to 96 kHz (rates > 48 kHz are downsampled to 48 kHz)
    Bitrates to 576 kbit/s
    ATDS (streaming) format recommended

**WMA (.WMA)**

    language:bash
    Two channels max
    Sample rates from 8 kHz to 48 kHz
    Bitrates from 5 kbits/s to 192 kbits/s
    Variable bit rate (VBR) supported

**WAV (.WAV)**

    language:bash
    Two channels max

    PCM format
        8 or 16 bits, sample rates < 48 kHz

    IMA_ADPCM format
        Sample rates < 48 kHz

    MPEG LAYER 3 format
        Same as MP3 modes

**MIDI (.MID)**

    language:bash
    General MIDI and SP-MIDI format 0
        Format 1 and 2 files must be converted to format 0

    Maximum polyphony: 64
    Actual polyphony: 19-31 notes at 3.5X clock

    Two instrument banks:
        GM1 (instruments)
        GM2 (percussion)

## Writing Your Own Code

The LilyPad MP3 Player uses the same pinout as SparkFun\'s [MP3 Player Shield](https://www.sparkfun.com/products/10628) and should run the same code without modification.

The LilyPad MP3 Player is Arduino-compatible. It uses the same bootloader as SparkFun\'s \"Pro\" and \"Pro Mini\" series of boards. Tto select the correct board from the Arduino IDE, go to the \"Tools/Board\" menu, and select \"Arduino Pro or Pro Mini (3.3V/8MHz) w/ATmega 328\".

We made it this way to support Bill Porter\'s excellent [MP3 Player Library](http://www.billporter.info/2012/01/28/sparkfun-mp3-shield-arduino-library/), which takes care of most of the hard work involved in playing audio files. If you look at the example code we provide, you\'ll find this library at its core.

The best way to write new code is to start with one of the existing examples. For example, we modified the stock code to play a prank on \"According To\" Pete Dokter where we looped the \"It\'s A Small World\" song over and over, while very slowly increasing the volume. We\'ve included this code is in the examples directory.

You can download the LilyPad MP3 Player code from the [github repository](https://github.com/sparkfun/LilyPad_MP3_Player). Clicking the \"ZIP\" button on that page will download the latest version. You could also install a github client and clone the repostitory to your local machine.

Within the archive, you\'ll find the [\"Trigger\"](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/getting-started-with-the-default-trigger-sketch) and [\"Player\"](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player/getting-started-with-the-player-sketch) sketches, as well as example programs showing off different features of the board, such as the use of the rotary encoder. All of the code is fully-commented and completely free for you to use and modify.

If you\'d like to bypass the Arduino environment and program the ATMega328 directly, you can do that as well. There is an unpopulated 6-pin ISP header on the board. You can use this header to program the board using an Atmel ISP programmer such as SparkFun\'s [Pocket Programmer](https://www.sparkfun.com/products/9825).

***We\'d like to extend huge thanks to Bill Porter and Michael Flaga for their hard work on the [MP3 Player Library](http://www.billporter.info/2012/01/28/sparkfun-mp3-shield-arduino-library/).***