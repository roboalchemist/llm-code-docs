# Source: https://learn.sparkfun.com/tutorials/qwiic-speaker-amp-tpa2016d2-hookup-guide

## Introduction

The [SparkFun Qwiic Speaker Amp](https://www.sparkfun.com/products/20690) includes the Texas Instruments TPA2016D2 stereo, filter-free class-D audio power amplifier. Its efficient class-D operation also means low heat and long battery life when driving 4Ω speakers at up to 2.8W in stereo, and 8Ω speakers at up to 1.7W in stereo. It won\'t shake a stadium but it will provide plenty of volume for your audio projects.

[![SparkFun Qwiic Speaker Amp](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/5/3/2/20690_DEV-_SparkFun_Qwiic_Speaker_Amp-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-speaker-amp.html)

### [SparkFun Qwiic Speaker Amp](https://www.sparkfun.com/sparkfun-qwiic-speaker-amp.html) 

[ DEV-20690 ]

The SparkFun Qwiic Speaker Amp includes the Texas Instruments TPA2016D2 class-D stereo audio amp.

[ [\$15.50] ]

**Note:** The [LilyPad MP3 Trigger](https://www.sparkfun.com/products/11013) uses the same TPA2016D2 for the amplifier! The Qwiic Speaker Amp was based of the designs off the LilyPad MP3 Trigger by Mike Grusin. The amplifier was connected to the I^2^C pins on the Arduino microcontroller as well but the [Arduino example code only used basic settings](https://github.com/sparkfun/LilyPad_MP3_Player/blob/master/Arduino/LilyPad%20MP3%20Player/Examples/Trigger_I2C/Trigger_I2C.ino).

### Required Materials

To follow along with this tutorial, you will need the following materials at a minimum. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Minimum Parts

At a minimum, you will need a cable and differential speaker with the Qwiic Speaker Amp. You will also need a power supply and some wires. This is assuming that you have a media player (i.e. smartphone, computer, or portable digital player) with a TRS audio output and the speakers have wires connected to the terminal.

[![DC Barrel Jack Adapter - Female](https://cdn.sparkfun.com/r/140-140/assets/parts/4/6/8/4/10288-02.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html)

### [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html) 

[ PRT-10288 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.75] ]

[![SparkFun Qwiic Speaker Amp](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/5/3/2/20690_DEV-_SparkFun_Qwiic_Speaker_Amp-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-speaker-amp.html)

### [SparkFun Qwiic Speaker Amp](https://www.sparkfun.com/sparkfun-qwiic-speaker-amp.html) 

[ DEV-20690 ]

The SparkFun Qwiic Speaker Amp includes the Texas Instruments TPA2016D2 class-D stereo audio amp.

[ [\$15.50] ]

[![Thin Speaker - 0.5W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/8/15350-Feature.jpg)](https://www.sparkfun.com/thin-speaker-0-5w.html)

### [Thin Speaker - 0.5W](https://www.sparkfun.com/thin-speaker-0-5w.html) 

[ COM-15350 ]

This 0.5W, 8Ohm speaker is only 40mm in diameter and just over 4mm thick, the same kind you might find in one of those \"talki...

[ [\$1.50] ]

[![Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/5/TOL-15312-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html)

### [Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html) 

[ TOL-15312 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA Barrel Jack wall power supply manufactured specifically for S...

[ [\$9.50] ]

[![Audio Cable TRS - 1m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/5/5/8/18983-TRS_3.5mm_Cable-01.jpg)](https://www.sparkfun.com/audio-cable-trs-1m.html)

### [Audio Cable TRS - 1m](https://www.sparkfun.com/audio-cable-trs-1m.html) 

[ CAB-18983 ]

This cable has a standard TRS 3.5mm plug on both ends allowing for easy connections to any 3.5mm jack.

[ [\$2.75] ]

[![Jumper Wires Premium 6in. M/M - 2 Pack (Red and Black)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/5/5/16662-Jumper_Wires_Premium_6in._M_M_Pack_of_2-_Red_and_Black-02.jpg)](https://www.sparkfun.com/jumper-wires-premium-6in-m-m-2-pack-red-and-black.html)

### [Jumper Wires Premium 6in. M/M - 2 Pack (Red and Black)](https://www.sparkfun.com/jumper-wires-premium-6in-m-m-2-pack-red-and-black.html) 

[ PRT-16662 ]

These red and black jumper wires can be used for pretty much everything including breadboards, Arduinos, and any 0.1in pitch ...

[ [\$1.25] ]

**Note:** Click below for a wishlist of the minimum parts.\
\

[Qwiic Speaker Amp Minimum Parts Wishlist](https://www.sparkfun.com/wish_lists/169349)

### Connecting with an Arduino

For users that want to configure the TPA2016D2 with the Arduino Library, you will need an Arduino microcontroller. We\'ll be using the RedBoard Plus with the ATmega328P. Make sure to add two speakers to your cart if you decide to have stereo output.

[![Flexible Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/4/5/17258-Flexible_Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-200mm.html)

### [Flexible Qwiic Cable - 200mm](https://www.sparkfun.com/flexible-qwiic-cable-200mm.html) 

[ PRT-17258 ]

This polarized I2C cable insulation is made from silicon making it more flexible than our original Qwiic cable particularly i...

[ [\$1.95] ]

[![SparkFun RedBoard Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/8/7/18158-SparkFun_RedBoard_Plus-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-plus.html)

### [SparkFun RedBoard Plus](https://www.sparkfun.com/sparkfun-redboard-plus.html) 

[ DEV-18158 ]

The RedBoard Plus is an Arduino-compatible development board that has everything you need in an Arduino Uno with extra perks ...

[ [\$29.50] ]

[![DC Barrel Jack Adapter - Female](https://cdn.sparkfun.com/r/140-140/assets/parts/4/6/8/4/10288-02.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html)

### [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html) 

[ PRT-10288 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.75] ]

[![SparkFun Qwiic Speaker Amp](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/5/3/2/20690_DEV-_SparkFun_Qwiic_Speaker_Amp-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-speaker-amp.html)

### [SparkFun Qwiic Speaker Amp](https://www.sparkfun.com/sparkfun-qwiic-speaker-amp.html) 

[ DEV-20690 ]

The SparkFun Qwiic Speaker Amp includes the Texas Instruments TPA2016D2 class-D stereo audio amp.

[ [\$15.50] ]

[![Thin Speaker - 0.5W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/8/15350-Feature.jpg)](https://www.sparkfun.com/thin-speaker-0-5w.html)

### [Thin Speaker - 0.5W](https://www.sparkfun.com/thin-speaker-0-5w.html) 

[ COM-15350 ]

This 0.5W, 8Ohm speaker is only 40mm in diameter and just over 4mm thick, the same kind you might find in one of those \"talki...

[ [\$1.50] ]

[![Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/5/TOL-15312-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html)

### [Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html) 

[ TOL-15312 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA Barrel Jack wall power supply manufactured specifically for S...

[ [\$9.50] ]

[![Reversible USB A to C Cable - 2m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/3/15424-Reversible_USB_A_to_C_Cable_-_2m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html)

### [Reversible USB A to C Cable - 2m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html) 

[ CAB-15424 ]

These 2m cables have minor modifications that allow them to be be plugged into their ports regardless of orientation on the U...

[ [\$10.50] ]

[![Audio Cable TRS - 1m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/5/5/8/18983-TRS_3.5mm_Cable-01.jpg)](https://www.sparkfun.com/audio-cable-trs-1m.html)

### [Audio Cable TRS - 1m](https://www.sparkfun.com/audio-cable-trs-1m.html) 

[ CAB-18983 ]

This cable has a standard TRS 3.5mm plug on both ends allowing for easy connections to any 3.5mm jack.

[ [\$2.75] ]

[![Jumper Wires Premium 6in. M/M - 2 Pack (Red and Black)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/5/5/16662-Jumper_Wires_Premium_6in._M_M_Pack_of_2-_Red_and_Black-02.jpg)](https://www.sparkfun.com/jumper-wires-premium-6in-m-m-2-pack-red-and-black.html)

### [Jumper Wires Premium 6in. M/M - 2 Pack (Red and Black)](https://www.sparkfun.com/jumper-wires-premium-6in-m-m-2-pack-red-and-black.html) 

[ PRT-16662 ]

These red and black jumper wires can be used for pretty much everything including breadboards, Arduinos, and any 0.1in pitch ...

[ [\$1.25] ]

**Note:** Click below for a wishlist when connecting an Arduino.\
\

[Qwiic Speaker Amp and Arduino Parts Wishlist](https://www.sparkfun.com/wish_lists/169350)

**Note:** Click below for the kit with the minimum parts to control the Qwiic Speaker Amp with an Artemis Nano. When using the Artemis Nano, make sure to [install the appropriate board definitions and select the correct board when uploading code](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide).\
\

[![SparkFun Qwiic Speaker Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/0/0/5/Kit_21230.jpg)](https://www.sparkfun.com/sparkfun-qwiic-speaker-kit.html)

### [SparkFun Qwiic Speaker Kit](https://www.sparkfun.com/sparkfun-qwiic-speaker-kit.html) 

[ KIT-21230 ]

The SparkFun Qwiic Speaker Kit provides you with just what you need to get started with the stereo audio via a simple Qwiic i...

**Retired**

### Accessories

There are many ways to connect to the Qwiic Speaker Amp. Below are a few accessories that you could use.

#### Speakers

Below are a few [speakers from the catalog](https://www.sparkfun.com/categories/344) that you could use as an output. You will want to choose differential speakers like the following listed below (not to be confused by the piezo buzzers). Note that some speakers may perform better than others at certain frequencies while others operate around a certain frequency range. Make sure to check out the speaker\'s datasheet when choosing a speaker.

[![Thin Speaker - 0.5W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/8/15350-Feature.jpg)](https://www.sparkfun.com/thin-speaker-0-5w.html)

### [Thin Speaker - 0.5W](https://www.sparkfun.com/thin-speaker-0-5w.html) 

[ COM-15350 ]

This 0.5W, 8Ohm speaker is only 40mm in diameter and just over 4mm thick, the same kind you might find in one of those \"talki...

[ [\$1.50] ]

[![Speaker - 0.5W (8 Ohm)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/7/0/09151-03-L.jpg)](https://www.sparkfun.com/speaker-0-5w-8-ohm.html)

### [Speaker - 0.5W (8 Ohm)](https://www.sparkfun.com/speaker-0-5w-8-ohm.html) 

[ COM-09151 ]

A small audio speaker that is ideal for radio and amplifier projects and is small enough to fit in robot projects.

[ [\$1.50] ]

[![Through-Hole Speaker](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/9/5/8/PRT-20660_01.jpg)](https://www.sparkfun.com/through-hole-speaker.html)

### [Through-Hole Speaker](https://www.sparkfun.com/through-hole-speaker.html) 

[ PRT-20660 ]

This is a small 15mm round speaker that operates around the audible 2kHz range.

[ [\$2.95] ]

[![Speaker - PCB Mount](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/0/4/11089-01.jpg)](https://www.sparkfun.com/speaker-pcb-mount.html)

### [Speaker - PCB Mount](https://www.sparkfun.com/speaker-pcb-mount.html) 

[ COM-11089 ]

This through-hole speaker is great for projects where you need something that sounds better than a piezo buzzer but don\'t hav...

**Retired**

Note that some speakers may be rated as a higher wattage (more than what the Qwiic Speaker Amp can output). Higher wattage speakers will still play sound but they won\'t be fully powered.

[![Surface Transducer - Large](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/7/0/4/19102-Surface_Transducer_-_Large-01.jpeg)](https://www.sparkfun.com/surface-transducer-large.html)

### [Surface Transducer - Large](https://www.sparkfun.com/surface-transducer-large.html) 

[ COM-19102 ]

Surface transducers give you the awesome power to turn almost any surface into a speaker.

[ [\$37.95] ]

[![Wide Frequency Range Speaker - 3in. (Polypropylene Cone)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/7/6/5/COM-18379_01.jpg)](https://www.sparkfun.com/wide-frequency-range-speaker-3in-polypropylene-cone.html)

### [Wide Frequency Range Speaker - 3in. (Polypropylene Cone)](https://www.sparkfun.com/wide-frequency-range-speaker-3in-polypropylene-cone.html) 

[ COM-18379 ]

This speaker is an excellent choice for compact applications requiring high fidelity music, or high intelligibility voice/com...

[\$11.95] [ [\$6.95] ]

#### Connectors, Wires, and Cables

For users connecting from a media player, you will need a TRS cable. Users can also make their own and wire the connection up with the TRS audio plug.

[![Audio Cable TRS - 1m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/5/5/8/18983-TRS_3.5mm_Cable-01.jpg)](https://www.sparkfun.com/audio-cable-trs-1m.html)

### [Audio Cable TRS - 1m](https://www.sparkfun.com/audio-cable-trs-1m.html) 

[ CAB-18983 ]

This cable has a standard TRS 3.5mm plug on both ends allowing for easy connections to any 3.5mm jack.

[ [\$2.75] ]

[![TRS Audio Plug - 3.5mm (Metal)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/0/9/15438-TRRS_Audio_Plug_3.5mm-02.jpg)](https://www.sparkfun.com/products/15438)

### [TRS Audio Plug - 3.5mm (Metal)](https://www.sparkfun.com/products/15438) 

[ COM-15438 ]

Plug (two conductors and a ground) & shroud to hack or repair or add a three-conductor audio jack into your project.

**Retired**

Depending on the connection, you will need jumper wire for the power, audio input, and/or speaker output. Below are a few [wires from the catalog](https://www.sparkfun.com/categories/141). Note that other wire might be too thick and may not fit the screw terminals. If the terminals on the speaker are big enough, you could also use spade quick disconnects as well.

[![Alligator Clip with Pigtail (4 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/3/2/6/13191-01.jpg)](https://www.sparkfun.com/alligator-clip-with-pigtail-4-pack.html)

### [Alligator Clip with Pigtail (4 Pack)](https://www.sparkfun.com/alligator-clip-with-pigtail-4-pack.html) 

[ CAB-13191 ]

This is a 4 pack of wires that are pre-terminated with an alligator clip on one end and a hookup pigtail on the other. Alliga...

[ [\$4.75] ]

[![Quick Disconnects - Female 1/4\" (Pack of 5)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/1/0/14407-01.jpg)](https://www.sparkfun.com/quick-disconnects-female-1-4-pack-of-5.html)

### [Quick Disconnects - Female 1/4\" (Pack of 5)](https://www.sparkfun.com/quick-disconnects-female-1-4-pack-of-5.html) 

[ PRT-14407 ]

Sometimes referred to as \"spade connectors,\" these quick disconnects are really useful as power connectors in prototyping or ...

[ [\$0.60] ]

[![Hook-up Stranded Wire - Black (22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/3/4/08867-01.jpg)](https://www.sparkfun.com/hook-up-stranded-wire-black-22-awg.html)

### [Hook-up Stranded Wire - Black (22 AWG)](https://www.sparkfun.com/hook-up-stranded-wire-black-22-awg.html) 

[ PRT-08867 ]

Standard 22 AWG stranded black wire. Use this for soldering wire or any project in which you need flexible wire. Stranded wir...

[ [\$3.75] ]

[![Hook-up Stranded Wire - Red (22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/3/2/08865-01.jpg)](https://www.sparkfun.com/hook-up-stranded-wire-red-22-awg.html)

### [Hook-up Stranded Wire - Red (22 AWG)](https://www.sparkfun.com/hook-up-stranded-wire-red-22-awg.html) 

[ PRT-08865 ]

Standard 22 AWG stranded red wire. Use this for soldering wire or any project in which you need flexible wire. Comes in small...

[ [\$3.75] ]

[![Hook-up Wire 2-Conductor - Clear (22AWG-7x30, Stranded, 25ft)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/7/9/1/PRT-18382_01.jpg)](https://www.sparkfun.com/hook-up-wire-2-conductor-clear-22awg-7x30-stranded-25ft.html)

### [Hook-up Wire 2-Conductor - Clear (22AWG-7x30, Stranded, 25ft)](https://www.sparkfun.com/hook-up-wire-2-conductor-clear-22awg-7x30-stranded-25ft.html) 

[ PRT-18382 ]

Great for general connections between projects (low or high current applications).

[ [\$6.25] ]

[![Jumper Wires Premium 6in. M/M - 2 Pack (Red and Black)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/5/5/16662-Jumper_Wires_Premium_6in._M_M_Pack_of_2-_Red_and_Black-02.jpg)](https://www.sparkfun.com/jumper-wires-premium-6in-m-m-2-pack-red-and-black.html)

### [Jumper Wires Premium 6in. M/M - 2 Pack (Red and Black)](https://www.sparkfun.com/jumper-wires-premium-6in-m-m-2-pack-red-and-black.html) 

[ PRT-16662 ]

These red and black jumper wires can be used for pretty much everything including breadboards, Arduinos, and any 0.1in pitch ...

[ [\$1.25] ]

[![Spade Connector Wire - 3ft, Female (2 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/8/0/14166-03.jpg)](https://www.sparkfun.com/spade-connector-wire-3ft-female-2-pack.html)

### [Spade Connector Wire - 3ft, Female (2 Pack)](https://www.sparkfun.com/spade-connector-wire-3ft-female-2-pack.html) 

[ CAB-14166 ]

These simple 24AWG wires are terminated with a female insulated spade connector at one end and a braided wire lead at the oth...

[ [\$2.50] ]

For those that want to take advantage of Qwiic-enabled devices, you\'ll want to grab a Qwiic cable.

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

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

[![Qwiic Cable - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/5/14429-Qwiic_Cable_-_500mm-01.jpg)](https://www.sparkfun.com/products/14429)

### [Qwiic Cable - 500mm](https://www.sparkfun.com/products/14429) 

[ PRT-14429 ]

This is a 500mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

#### Power

To power the board, you could use a separate power supply for the Qwiic Audio Amp. For installations, you could use a 5V wall wart and a barrel jack adapter. For portable applications, you could use a LiPo battery and boost converter for a constant voltage input.

[![DC Barrel Jack Adapter - Female](https://cdn.sparkfun.com/r/140-140/assets/parts/4/6/8/4/10288-02.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html)

### [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html) 

[ PRT-10288 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.75] ]

[![Lithium Ion Battery - 1250mAh (IEC62133 Certified)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/6/0/6/17748-Lithium_Ion_Battery_-_1250_mAh__IEC62133_certified_-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-1250mah-iec62133-certified.html)

### [Lithium Ion Battery - 1250mAh (IEC62133 Certified)](https://www.sparkfun.com/lithium-ion-battery-1250mah-iec62133-certified.html) 

[ PRT-18286 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1250 mAh and is IE...

**Retired**

[![Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/5/TOL-15312-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html)

### [Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html) 

[ TOL-15312 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA Barrel Jack wall power supply manufactured specifically for S...

[ [\$9.50] ]

[![SparkFun LiPo Charger/Booster - 5V/1A](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/3/2/14411-01.jpg)](https://www.sparkfun.com/sparkfun-lipo-charger-booster-5v-1a.html)

### [SparkFun LiPo Charger/Booster - 5V/1A](https://www.sparkfun.com/sparkfun-lipo-charger-booster-5v-1a.html) 

[ PRT-14411 ]

The SparkFun 5V/1A LiPo Charger/Booster is a no-nonsense circuit for generating one amp from a Lithium Polymer battery at 5V....

[ [\$18.50] ]

### Tools

To secure the wires in the screw terminals, you will need the pocket screwdriver set. Note that some [screwdriver flat heads might be too large](https://www.sparkfun.com/products/9146) to drive the screws. The pocket screwdriver set includes a drive bit that is compatible with the screw terminals that are soldered on the Qwiic Speaker Amp. There is also another drive bit that you could use to secure wire to the barrel jack adapter as well.

[![Pocket Screwdriver Set](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/3/12891-01.jpg)](https://www.sparkfun.com/pocket-screwdriver-set.html)

### [Pocket Screwdriver Set](https://www.sparkfun.com/pocket-screwdriver-set.html) 

[ TOL-12891 ]

What should every hacker have available to them? That\'s right, a screwdriver (you have to get into those cases somehow). What...

[ [\$5.50] ]

You may need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49) when soldering wires to the speakers or to modify the jumpers.

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

[![Hobby Knife](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/6/09200-Hobby_Knife-01.jpg)](https://www.sparkfun.com/hobby-knife.html)

### [Hobby Knife](https://www.sparkfun.com/hobby-knife.html) 

[ TOL-09200 ]

It\'s like an Xacto knife, only better. We use these extensively when working with PCBs. These small knives work well for cutt...

[ [\$3.75] ]

[![Wire Strippers - 20-30AWG](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/6/6/15220_-_Wire_Strippers_-_20-30AWG.jpg)](https://www.sparkfun.com/products/15220)

### [Wire Strippers - 20-30AWG](https://www.sparkfun.com/products/15220) 

[ TOL-15220 ]

These are higher grade wire strippers from Jonard Industries with a comfortable, curved grip making them an affordable option...

**Retired**

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

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic) if you decide to take advantage of the Qwiic connector.

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/redboard-plus-hookup-guide)

### RedBoard Plus Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Plus. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

## Hardware Overview

In this section, we will highlight the hardware and pins that are broken out on the Qwiic Speaker Amp (TPA2016D2). For more information on the amplifier, check out our [Resources and Going Further](https://learn.sparkfun.com/tutorials/qwiic-speaker-amp-tpa2016d2-hookup-guide#resources-and-going-further).

[![TPA2016D2 Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_IC.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_IC.jpg)

### Amplifier to Amplifier [(Comparision of a few of SparkFun Audio Amps)]

What distinguishes this audio amplifier from others is that it features volume control (i.e. gain), Dynamic Range Compression (DRC), Automatic Gain Control (AGC), enable/disable amplifier, and its ability to be configured through software via I^2^C. Its efficient class-D operation also means low heat and long battery life when driving 4Ω speakers at up to 2.8W in stereo, and 8Ω speakers at up to 1.7W in stereo. This is quite a bit more power than the [mono amplifier (TPA2005D1)](https://www.sparkfun.com/products/11044) or [Noisy Cricket stereo amplifier (LM4853)](https://www.sparkfun.com/products/14475). It won\'t shake a stadium but it will provide plenty of volume for your audio projects.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/parts/2/0/5/3/2/20690_DEV-_SparkFun_Qwiic_Speaker_Amp-_01.jpg "Qwiic Speaker Amp (TPA2016D2), release date September 2022")](https://www.sparkfun.com/products/20690)   [![Noisy Cricket Stereo Amplifier (LM4853)](https://cdn.sparkfun.com//assets/parts/1/2/5/2/0/14475-SparkFun_Noisy_Cricket_Stereo_Amplifier_-_1.5W-01.jpg "Noisy Cricket Stereo Amplifier (LM4853), SparkFun release date April 2018")](https://www.sparkfun.com/products/14475)   [![Mono Amplifier (TPA2005D1)](https://cdn.sparkfun.com//assets/parts/6/4/0/0/11044-01a.jpg "Mono Amplifier (TPA2005D1), SparkFun release date March 2012")](https://www.sparkfun.com/products/11044)

  *Qwiic Speaker Amp\                                                                                                                                                                                          *Noisy Cricket Stereo Amp\                                                                                                                                                                                                                                                        *Mono Amp\
  (TPA2016D2)\                                                                                                                                                                                                 (LM4853)\                                                                                                                                                                                                                                                                         (TPA2005D1)\
  \[ [DEV-20690](https://www.sparkfun.com/products/20690) \]*                                                                                                                                                  \[ [DEV-14475](https://www.sparkfun.com/products/14475) \]*                                                                                                                                                                                                                       \[ [BOB-11044](https://www.sparkfun.com/products/11044) \]*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The DRC and AGC is unique compared to other audio amplifiers. This is a powerful feature that allows you to \"even out\" the loud and quiet sections from your audio input. It also allows you to maximize the volume of your speakers. By fine-tuning the settings, you can get the most volume to prevent distortion of the audio signal. Using the DRC, AGC, and/or the limiter alone allows you to protect your speakers from getting damaged by extremely loud playback. We\'ve written an extensive Arduino Library (shown later in this tutorial) that allows you to easily control all of the amplifier\'s features from simple gain control to advanced AGC. Note that you will need to send the configuration to the TPA2016D2 upon every power cycle.

### Power

There are two ways to power the board:

- Screw Terminal
- Qwiic Cable

⚡ **Danger:** Make sure to only apply power through either the screw terminal or Qwiic cable. You can damage Qwiic-enabled boards that are daisy chained to the Qwiic Speaker Amp if there is a solder jumper on JP1 and you apply power to VIN.

#### Power [Screw Terminals]

The Qwiic Speaker Amp requires an input voltage between **2.5V** and **5.5V**. You can insert wires through the two pin screw terminal labeled as **VIN** and **GND**. Using a higher voltage closer to the recommended input voltage will drive the speakers better and provide a louder sound.

[![Power Pins](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Speaker_Power_Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Speaker_Power_Pins.jpg)

#### Power [Qwiic Cable]

You can also provide power through the Qwiic Connector. This will provide 3.3V for the amplifier. Simply insert a Qwiic cable between your development board and the Qwiic Speaker Amp.

[![Qwiic Connector Power Input](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Speaker_Qwiic_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Speaker_Qwiic_Connector.jpg)

If you are powering the board through the Qwiic connector, make sure to add a solder jumper on **JP1**.

[![JP1](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_JP1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_JP1.jpg)

[] **Warning:** For users powering the Qwiic Speaker Amp through the Qwiic cable, the development board\'s 3.3V voltage regulator might not be able to fully power the Qwiic Speaker Amp, your microcontroller, and Qwiic-enabled device that is daisy chained.

### Thermal Dissipation

While the TPA2016D2 includes thermal protection, the exposed copper pour directly below the IC on the bottom of the board is added to the design for better thermal dissipation.

[![Ground Pour](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Copper_Pour.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Copper_Pour.jpg)

### I^2^C and Qwiic

To communicate with the amplifier, you will need an I^2^C bus. The Qwiic system makes it easy to connect the TPA2016D2 to your projects via the Qwiic connector. You can add a Qwiic cable between the amplifier and development board to configure the TPA2016D2. The I^2^C address of the TPA2016D2 is **0x58** (unshifted). There are two 2.2kΩ pull-up resistors connected to the SDA and SCL lines.

[![Qwiic Connector](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Speaker_Qwiic_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Speaker_Qwiic_Connector.jpg)

### Audio Input

There are two ways to provide an audio signal for the Qwiic Speaker Amp.

- 3.5mm TRS Connector
- Screw Terminals

#### Audio Input [3.5mm TRS Connector]

One method of providing an audio signal is through the 3.5mm TRS connector (labeled as **INPUT**). This is if you have a media player with a 3.5mm TRS connector as well. The tip is connected to the left audio input, the ring is connected to the right audio input, and the sleeve is connected to ground.

[![Audio In - 3.5mm audio jack Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Speaker_3.5mm_TRS_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Speaker_3.5mm_TRS_Connector.jpg)

#### Audio Input [Screw Terminals]

The other method is to connect an audio signal to the audio in left (**AUD IN**, **L**) and right (**AUD IN**, **R**) pins that are broken out on the screw terminals. Just make sure to connect ground.

[![Audio In - Screw Terminals Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Audio_Input_Screw_Terminal.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Audio_Input_Screw_Terminal.jpg)

### Shutdown

We broke out the shutdown pin (labeled as **[SHDN]**) by the audio input pins. This pin is active low. Connecting this pin with a wire to the ground pin will manually shutdown the Qwiic Speaker Amp.

[![Shutdown Pins](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Shutdown.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Shutdown.jpg)

### Speaker Output

The board includes differential stereo outputs for a left and right speaker. Below are some specifications from the datasheet that show what you may expect from each channel based on the speaker\'s impedance and voltage input.

- 1.7W per Channel into 8Ω at 5V
- 750mW per Channel into 8Ω at 3.6V
- 2.8W per Channel into 4Ω at 5V
- 1.5W per Channel into 4Ω at 3.6V

For an analog input on the left (**AUD IN**, **L**), make sure to place a speaker on the left \"**SPK OUT**, **+**\" and \"**SPK OUT**,**-**\" pins. For an analog input on the right (**AUD IN**, **R**), make sure to place a speaker on the right \"**SPK OUT**, **+**\" and \"**SPK OUT**,**-**\" pins.

[![Speaker Output Pins](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Speaker_Output_Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Speaker_Output_Pins.jpg)

**Note:** When wiring differential speakers to speaker out terminals, make sure to match the \"+\" to \"+\" and \"-\" to \"-\" for both speakers. If one of the stereo speakers is wired \"+\" to \"-\" and \"-\" to +\" while the other speaker is wired \"+\" to \"+\" and \"-\" to \"-\", the audio signals will interfere and cancel each other out. If there are no labels on the speakers, just make sure to wire the speakers consistently.

### LED

There is one LED to indicate when power is applied to the Qwiic Speaker Amp. This is labeled as PWR. When power is applied to the board\'s VIN, the LED will light up. If jumper JP1 is closed, the LED will light up when the board is connected to a board through a Qwiic cable.

[![LED Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_LED.jpg)

### Jumpers

**Note:** If this is your first time working with jumpers, check out the [How to Work with Jumper Pads and PCB Traces](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all) tutorial for more information.

The following three jumpers are included.

- **LED** - By default, this jumper is closed and located on the bottom of the board. Cut this trace to disable the power LED that is connected to 3.3V.
- **I2C** - The I^2^C jumpers are closed by default. By cutting the traces between the jumper pads, it will disconnect to the 2.2kΩ pull-up resistors for the I^2^C bus. Most of the time you can leave these alone unless your project requires you to [connect the pull-up resistors](https://learn.sparkfun.com/tutorials/i2c/all#i2c-at-the-hardware-level).
- **JP1** - This jumper is open by default. For users that just want to provide power to the TPA2016D2 via the Qwiic cable\'s 3.3V line, add a solder jumper to the pads. Depending on the 3.3V voltage regulator that you are using, you may not have enough power to drive the speakers at their full potential as stated earlier.

[![Jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Jumpers.jpg)

### Board Dimensions

The overall length and width is about 1.70\" x 1.00\". This does not include the length of the 3.5mm TRS connector that is sticking slight out of the board. The board includes 4x mounting holes on the edge of the board.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/0/1/5/6/3/SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Board_Dimensions.png)](https://cdn.sparkfun.com/assets/0/1/5/6/3/SparkFun_Qwiic_Speaker_Amp-TPA2016D2_Board_Dimensions.png)

## Hardware Hookup

⚡ **Danger:** While there is short circuit protection, we recommend removing power when connecting the boards and components together. We still managed to blow out the IC by shorting the speaker output terminals during our stress tests.

This board is great for projects that require you to amplify an audio signal for small, differential speakers. This breakout is also great when pairing it with your smartphone, computer, portable digital player, or any audio boards (such as the MP3 Trigger, Tsunami Super WAV Trigger, MP3 Player Shield, or Music Instrument Shield to name a few)! In this section, we will show you a few ways to connect to the Qwiic Speaker Amp.

### Soldering Wire vs Quick Disconnects

Depending on your setup, you may need to [strip some wire](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) and [solder the ends to terminals](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) before connecting your speakers or power supply to the Qwiic Speaker Amp. You can also use jumper wires with male pins.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

February 8, 2013

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

One example are the 8Ω small, cone speakers. These do not have wires connected to the tabs. The best method of connecting the cone speaker would be to solder wires to the tabs. In this case, jumper wires with male pins were soldered the ends. You could also connect to the tabs using alligator clips for a temporary connection. However, you need to ensure that the alligator clips are not touching the speaker frame as this will short the speaker pins and blow out the Qwiic Speaker Amp.

[![Cone Speaker Connections](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/Cone_Speakers_Connection.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/Cone_Speakers_Connection.jpg)

⚡ **Danger:** The alligator clips connecting to the terminals in the image are a temporary connection and not recommended for the small cone speakers. A small bump can cause the alligator clips to touch the frame and cause a short. As a result, the TPA2016D2 can blow out from the speaker output terminals shorting.

For larger speakers (like the [Wide Frequency Range Speaker - 3in](https://www.sparkfun.com/products/18379)) have 1/4\" tabs. You could use [1/4\" spade quick disconnects with crimped wire](https://www.sparkfun.com/products/14166) for a secure connection or [crimp them yourself](https://www.sparkfun.com/products/14407).

  ------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------
  [![Cone Speaker Tabs](https://cdn.sparkfun.com//assets/parts/1/7/7/6/5/COM-18379_04.jpg)](https://www.sparkfun.com/products/18379)   [![Spade Connector Wire - Female](https://cdn.sparkfun.com//assets/parts/1/2/0/8/0/14166-03.jpg)](https://www.sparkfun.com/products/14166)

  *Wide Frequency Range Speaker - 3in\                                                                                                 *Spade Connector Wire - Female\
  \[ [COM-18379](https://www.sparkfun.com/products/18379) \]*                                                                          \[ [COM-14166](https://www.sparkfun.com/products/14166) \]*
  ------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------

### Audio In via 3.5mm TRS Audio Jack

For a quick connection to audio boards and portable digital players with a 3.5mm TRS audio jack, you can connect a TRS cable between the two.

[![Audio In - 3.5mm Audio Jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_TRS_Audio_Input.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_TRS_Audio_Input.jpg)

### Audio In via Screw Terminals

You can also insert a jumper wire to the R, L, and GND from your audio board. In this case, we used an old Tsunami Super WAV Trigger to connect to the Qwiic Speaker Amp. Depending the audio board that you use, additional soldering may be required. Just make sure to connect your stereo output between both boards (i.e. R to R, L to L, and GND to GND between the boards).

[![WAV Trigger Connected to Audio Input Pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_PTH_Pins_WAV_Trigger.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_PTH_Pins_WAV_Trigger.jpg)

### Power In via Screw Terminals

For the a louder output, you will want to go this route with a separate power supply as shown below. Insert power into the \"VIN\" and \"GND\" terminals between the power supply and the Qwiic Speaker Amp. Make sure that the voltage that you are applying to the \"VIN\" terminal is between **2.5V** and **5V**. In this case, we used a [5V wall adapter with barrel jack](https://www.sparkfun.com/products/15312), female barrel jack adapter. We then connected some stripped wire from \"+\" to \"VIN\" and \"-\" to \"GND\".

[![5V Power Supply, Barrel Jack Adapter, Qwiic Speaker Amp](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Power_Wall_Adapter.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Power_Wall_Adapter.jpg)

### Power In via Qwiic Cable

If you would like to power the board with your Arduino using Qwiic cable, you can simply insert a Qwiic cable between the two connectors. In this case we used a RedBoard Plus to power the Qwiic Spaker Amp.

[![RedBoard Plus Providing Power for the Qwiic Speaker Amp via Qwiic Cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_RedBoard_Plus.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_RedBoard_Plus.jpg)

As stated in the Hardware Overview, make sure that the JP1 jumper is soldered if you decide to power the Qwiic Speaker Amp through the Qwiic cable.

[![JP1](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_JP1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp-TPA2016D2_JP1.jpg)

[] **Warning:** For users powering the Qwiic Speaker Amp through the Qwiic cable, the development board\'s 3.3V voltage regulator might not be able to fully power the Qwiic Speaker Amp, your microcontroller, and Qwiic-enabled device that is daisy chained.

### Speaker Out

Attach the speaker of your choice to the outputs. For the scope of this tutorial, we will use the 8Ω thin speakers with wires already attached. Connect \"+\" to \"+\" and \"-\" to \"-\" for both channel. Then tighten down the screws to secure.

[![Thin Speakers Connected via Screw Terminals](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Speakers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Speakers.jpg)

**Note:** For a secure connection, you may want to apply hot glue the thin wires and speaker terminals for strain relief. You could also solder your own wire to the speaker pins as shown in the image with the blue wires.

**Note:** The speakers have magnets and can stick to each other magnetically. Make sure to secure the speakers or spread out the speakers when audio is being played.

**Note:** When wiring differential speakers to speaker out terminals, make sure to match the \"+\" to \"+\" and \"-\" to \"-\" for both speakers. If one of the stereo speakers is wired \"+\" to \"-\" and \"-\" to +\" while the other speaker is wired \"+\" to \"+\" and \"-\" to \"-\", the audio signals will interfere and cancel each other out. If there are no labels on the speakers, just make sure to wire the speakers consistently.

The Qwiic Speaker Amp can also power the 4Ω large surface transducer. While the large surface transducer is rated for 10W, it was still able to make a decent amount of sound when applying it to a surface. The example shown below shows one surface transducer connected to one channel. If you decide to only connect one speaker, make sure to match the connection on the input side as well (i.e. left audio in and left speaker out).

[![Surface Transducer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Surface_Transducer.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Surface_Transducer.jpg)

### Connecting an Audio Device

The Qwiic Speaker Amp can operate without an Arduino microcontroller. Simply connect a media player through the TRS connector, speakers, and a power supply to the board. Power up the board and hit play on your favorite track. The Qwiic Speaker Amp will amplify the signal and output it to the speakers using its default settings. Of course, you could also connect an audio board through the screw terminals as explained earlier.

[![Smartphone Connected to Qwiic Speaker Amp, 5V Power Supply, and 8 Ohm Thin Speakers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Smartphone_TRS.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Smartphone_TRS.jpg)

### Connecting an Audio Device and Arduino

To control the gain and configure the Qwiic Speaker Amp, you will need an Arduino microcontroller. The setup is pretty much the same as the previous section. However, we connect an Arduino\'s I^2^C pins to the Qwiic Speaker Amp\'s Qwiic connector. You will also need to power the Arduino with a separate power supply. You could use a computer\'s USB port for programming and power. When you are finished writing your program based on the example code, you could use a 5V USB wall adapter for power.

[![Audio In from a TRS Cable, RedBoard Plus Programmed with Arduino, 5V Power Supply, 8 Ohm Thin Speakers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Arduino.jpg)

Depending on your setup, you may need additional power adapter. The example shown below shows the MP3 Trigger with an additional power supply.

[![Audio In from the MP3 Trigger TRS Cable, RedBoard Plus Programmed with Arduino, 5V Power Supply, 8 Ohm Thin Speakers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_MP3_Trigger_RedBoard_Plus.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_MP3_Trigger_RedBoard_Plus.jpg)

## Example 0: Without an Arduino

As stated at the end of the hardware hookup, you could simply power the board up and send an audio signal to the Qwiic Speaker Amp. When everything is connected and secure, power the Qwiic Speaker Amp up and start playing the your favorite track!

[![Smartphone Connected to Qwiic Speaker Amp, 5V Power Supply, and 8 Ohm Thin Speakers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Smartphone_TRS.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Smartphone_TRS.jpg)

**Note:** The default gain for the TPA2016D2 is 6dB. For a larger gain and a louder volume from the speakers, you will need an Arduino microcontroller to configure the gain settings.

## Installing Drivers

We will be using the RedBoard Plus to control and configure the Qwiic Speaker Amp. You may need to install drivers to upload code. If necessary, check out the tutorial below. If you are using a different USB-to-Serial converter, you will need to install a different driver. Check out the tutorial associated with your Arduino microcontroller for more information.

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

## Software Installation

**Note:** If this is your first time using Arduino IDE, library, or board add-on, please review the following tutorials.\
\

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

The Qwiic Speaker Amp\'s Arduino library can be downloaded with the Arduino library manager by searching \'**SparkFun Qwiic Speaker Amp (TPA2016D2)**\' or you can grab the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_Qwiic_Speaker_Amp) to manually install.

[SparkFun Qwiic Speaker Amp Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_Speaker_Amp/archive/refs/heads/main.zip)

## Example 1: Gain Control

Let\'s upload the sketch to control the gain for the Qwiic Speaker Amp using an Arduino microcontroller.

[![Audio In from a TRS Cable, RedBoard Plus Programmed with Arduino, 5V Power Supply, 8 Ohm Thin Speakers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Arduino.jpg)

From the menu, select the following: **File** \> **Examples** \> Examples from Custom Libraries \| **SparkFun TPA2016D2 Arduino Library** \> **Example_01_Gain**.

Or you can copy and paste the following code in the Arduino IDE. Select the correct board definition from the menu (in this case, **Tools** \> **Boards** \> **Arduino Uno**). Then select the correct COM port that the board enumerated to (in this case, it was **COM13**). Hit the upload button.

    language:c
    /******************************************************************************
      Example _01_Gain.ino
      Sets a few different gain values on the TPA2016D2 speaker amp.

      Note, when gain is "0", it still passes sound through.
      To turn the sound off, use shutdown or enable/disable examples.

      Note, you can't REALLY turn off the AGC on the TPA2016D2,
      But if you disable the limiter, noisegate, and set fast release/attack
      times, then it only minimally effects gain changes.

      SparkFun TPA2016D2 Arduino Library
      Pete Lewis @ SparkFun Electronics
      September 8, 2022
      https://github.com/sparkfun/SparkFun_TPA2016D2_Arduino_Library

      This code was originally created by Mike Grusin at SparkFun Electronics
      Included with the LilyPad MP3 example code found here:
      Revision history: version 1.0 2012/07/24 MDG Initial release
      https://github.com/sparkfun/LilyPad_MP3_Player

      Do you like this library? Help support SparkFun. Buy a board!

        SparkFun Qwiic Speaker Amp - TPA2016D2
        https://www.sparkfun.com/products/20690

      Development environment specifics:

        IDE: Arduino 1.8.19
        Hardware Platform: SparkFun Redboard Qwiic
        SparkFun Qwiic Speaker Amp - TPA2016D2 Version: 1.0

      Hardware Connections:
      Use a qwiic cable to connect from the Redboard Qwiic to the Qwiic Speaker Amp.
      Connect audio-in, speakers, and power to the Qwiic Speaker Amp.

        For information on the data sent to and received from the amplifier,
        refer to the TPA2016D2 datasheet at:
        http://www.ti.com/lit/ds/symlink/tpa2016d2.pdf

      This program is distributed in the hope that it will be useful,
      but WITHOUT ANY WARRANTY; without even the implied warranty of
      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
      GNU General Public License for more details.

      You should have received a copy of the GNU General Public License
      along with this program.  If not, see <http://www.gnu.org/licenses/>.
    ******************************************************************************/

    #include <Wire.h>
    #include <SparkFun_TPA2016D2_Arduino_Library.h> //Click here to get the library: http://librarymanager/All#SparkFun_TPA2016D2
    TPA2016D2 amp;

    void setup()
    
      Serial.println("Device is connected properly.");

      // for gain control to react to changes quickly, we need to adjust some of the AGC settings as so...
      amp.disableLimiter(); // note this also changes compression ratio to 1:1, then disables limiter.
      amp.disableNoiseGate(); // disabling the noisegate allows us to always change the gain, even with very little sound at the source.
      amp.writeRelease(1); // 1-63 are valid values. 1 being the shortest (aka fastest) release setting, this allows gain increases to happen quickly.
      amp.writeAttack(1); // 1-63 are valid values. 1 being the shortest (aka fastest) attack setting, this allows gain decreases to happen quickly.

      Serial.println("gain:+30 (max)");
      amp.writeFixedGain(30); // aka "full gain at +30dB", accepts values from 0 to 30
      delay(5000);

      Serial.println("gain:+15 (mid)");
      amp.writeFixedGain(15);
      delay(5000);

      Serial.println("gain:0 (min)");
      amp.writeFixedGain(0);
      delay(5000);

      Serial.println("Example complete. Hit Reset to try again.");
    }

    void loop()
    

Hit the play button on your portable digital player to begin sending audio to amplifier and speakers. Make sure that the volume on your device is turned up as well. Open the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at **115200** if you need to see the serial output when the gain adjusts. You should see the example adjust the gain once based on the settings and the audio getting quieter every 5 seconds.

[![Gain](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/Arduino_Serial_Plotter_TPA2016D2_Serial_Output-Gain.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/Arduino_Serial_Plotter_TPA2016D2_Serial_Output-Gain.JPG)

Note that a gain of \"0\" will still pass the audio signal to the speakers. If you are looking to turn the speakers fully off (i.e. \"0\" volume), try adding code from example 2 to disable the channel or example 3 to shutdown the amplifier.

**Note:** You will need to send the configuration to the TPA2016D2 upon every power cycle. Hit the reset button to resend the commands if the gain is not changing fast enough.\
\

``` c
 // for gain control to react to changes quickly, we need to adjust some of the AGC settings as so...
  amp.disableLimiter(); // note this also changes compression ratio to 1:1, then disables limiter.
  amp.disableNoiseGate(); // disabling the noisegate allows us to always change the gain, even with very little sound at the source.
  amp.writeRelease(1); // 1-63 are valid values. 1 being the shortest (aka fastest) release setting, this allows gain increases to happen quickly.
  amp.writeAttack(1); // 1-63 are valid values. 1 being the shortest (aka fastest) attack setting, this allows gain decreases to happen quickly.
```

## Example 2: Enable Channel

Let\'s upload the sketch to control the channels of the Qwiic Speaker Amp using an Arduino microcontroller.

[![Audio In from a TRS Cable, RedBoard Plus Programmed with Arduino, 5V Power Supply, 8 Ohm Thin Speakers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Arduino.jpg)

From the menu, select the following: **File** \> **Examples** \> Examples from Custom Libraries \| **SparkFun TPA2016D2 Arduino Library** \> **Example_02_Enable_Channel**.

Or you can copy and paste the following code in the Arduino IDE. Select the correct board definition from the menu (in this case, **Tools** \> **Boards** \> **Arduino Uno**). Then select the correct COM port that the board enumerated to (in this case, it was **COM13**). Hit the upload button.

    language:c
    /******************************************************************************
      Example _02_Enable_Channel.ino
      Enables and Disables each channel individually on the TPA2016D2 speaker amp.

      SparkFun TPA2016D2 Arduino Library
      Pete Lewis @ SparkFun Electronics
      September 8, 2022
      https://github.com/sparkfun/SparkFun_TPA2016D2_Arduino_Library

      This code was originally created by Mike Grusin at SparkFun Electronics
      Included with the LilyPad MP3 example code found here:
      Revision history: version 1.0 2012/07/24 MDG Initial release
      https://github.com/sparkfun/LilyPad_MP3_Player

      Do you like this library? Help support SparkFun. Buy a board!

        SparkFun Qwiic Speaker Amp - TPA2016D2
        https://www.sparkfun.com/products/20690

      Development environment specifics:

        IDE: Arduino 1.8.19
        Hardware Platform: SparkFun Redboard Qwiic
        SparkFun Qwiic Speaker Amp - TPA2016D2 Version: 1.0

      Hardware Connections:
      Use a qwiic cable to connect from the Redboard Qwiic to the Qwiic Speaker Amp.
      Connect audio-in, speakers, and power to the Qwiic Speaker Amp.

        For information on the data sent to and received from the amplifier,
        refer to the TPA2016D2 datasheet at:
        http://www.ti.com/lit/ds/symlink/tpa2016d2.pdf

      This program is distributed in the hope that it will be useful,
      but WITHOUT ANY WARRANTY; without even the implied warranty of
      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
      GNU General Public License for more details.

      You should have received a copy of the GNU General Public License
      along with this program.  If not, see <http://www.gnu.org/licenses/>.
    ******************************************************************************/

    #include <Wire.h>
    #include <SparkFun_TPA2016D2_Arduino_Library.h> //Click here to get the library: http://librarymanager/All#SparkFun_TPA2016D2
    TPA2016D2 amp;

    void setup()
    
      Serial.print("Device is connected properly.");
    }

    void loop()
    

Hit the play button on your audio device to begin sending audio to amplifier and speakers. Make sure that the volume on your device is turned up as well. The example turn on and off each channel every 3 seconds. Open the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at **115200** if you need to see the serial output when the channels are enabled/disabled.

[![Serial Output Enable/Disable Audio Channel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/Arduino_Serial_Plotter_TPA2016D2_Serial_Output-Enable_Audio_Channel.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/Arduino_Serial_Plotter_TPA2016D2_Serial_Output-Enable_Audio_Channel.JPG)

## Example 3: Shutdown

Let\'s upload the sketch to shutdown the Qwiic Speaker Amp using an Arduino microcontroller.

[![Audio In from a TRS Cable, RedBoard Plus Programmed with Arduino, 5V Power Supply, 8 Ohm Thin Speakers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/20690_SparkFun_Qwiic_Speaker_Amp_Arduino.jpg)

From the menu, select the following: **File** \> **Examples** \> Examples from Custom Libraries \| **SparkFun TPA2016D2 Arduino Library** \> **Example_03_Shutdown**.

Or you can copy and paste the following code in the Arduino IDE. Select the correct board definition from the menu (in this case, **Tools** \> **Boards** \> **Arduino Uno**). Then select the correct COM port that the board enumerated to (in this case, it was **COM15**). Hit the upload button.

    language:c
    /******************************************************************************
      Example _03_Shutdown.ino
      Demonstrates how to shutdown the TPA2016D2 via software command.
      Enables and disables shutdown once every 5 seconds. "blinks" the sound :)

      SparkFun TPA2016D2 Arduino Library
      Pete Lewis @ SparkFun Electronics
      September 8, 2022
      https://github.com/sparkfun/SparkFun_TPA2016D2_Arduino_Library

      This code was originally created by Mike Grusin at SparkFun Electronics
      Included with the LilyPad MP3 example code found here:
      Revision history: version 1.0 2012/07/24 MDG Initial release
      https://github.com/sparkfun/LilyPad_MP3_Player

      Do you like this library? Help support SparkFun. Buy a board!

        SparkFun Qwiic Speaker Amp - TPA2016D2
        https://www.sparkfun.com/products/20690

      Development environment specifics:

      IDE: Arduino 1.8.19
      Hardware Platform: SparkFun Redboard Qwiic
      SparkFun Qwiic Speaker Amp - TPA2016D2 Version: 1.0

      Hardware Connections:
      Use a qwiic cable to connect from the Redboard Qwiic to the Qwiic Speaker Amp.
      Connect audio-in, speakers, and power to the Qwiic Speaker Amp.

      For information on the data sent to and received from the amplifier,
      refer to the TPA2016D2 datasheet at:
      http://www.ti.com/lit/ds/symlink/tpa2016d2.pdf

      This program is distributed in the hope that it will be useful,
      but WITHOUT ANY WARRANTY; without even the implied warranty of
      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
      GNU General Public License for more details.

      You should have received a copy of the GNU General Public License
      along with this program.  If not, see <http://www.gnu.org/licenses/>.
    ******************************************************************************/

    #include <Wire.h>
    #include <SparkFun_TPA2016D2_Arduino_Library.h> //Click here to get the library: http://librarymanager/All#SparkFun_TPA2016D2
    TPA2016D2 amp;

    void setup()
    
      Serial.println("Device is connected properly.");
    }

    void loop()
    

Hit the play button on your audio device to begin sending audio to amplifier and speakers. Make sure that the volume on your device is turned up as well. The example shuts down the TPA2016D2 every 5 seconds. Open the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at **115200** if you need to see the serial output when the TPA2016D2 is shutdown.

[![Serial Output Shutdown](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/4/9/Arduino_Serial_Plotter_TPA2016D2_Serial_Output-Shutdown.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/4/9/Arduino_Serial_Plotter_TPA2016D2_Serial_Output-Shutdown.JPG)

**Note:** You can also manually shutdown the Qwiic Speaker Amp. The shutdown pin (SHDN) is active low. Using a jumper wire and grounding the pin will shutdown the amplifier.

## More Examples!

Make sure to check out the other examples that are listed in the SparkFun TPA2016D2 Arduino Library to detect faults (i.e. shorts on the speaker channels or excessive heat), control limiter, and/or control the automatic gain control (AGC).

[GitHub: SparkFun TPA2016D2 Arduino Library - Examples](https://github.com/sparkfun/SparkFun_TPA2016D2_Arduino_Library/tree/main/examples)

⚡ **Danger:** Caution is advised when testing and reading the short circuit fault. **DO NOT** connect speakers leads while sound is playing through speaker. This should only be used to detect shorts on speaker lines **BEFORE** actually turning on your source.\
\
While there is short circuit protection, we recommend removing power when connecting the boards and components together. We still managed to blow out the IC by shorting the speaker output terminals during our stress tests.

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
If you don\'t find what you need there, our [SparkFun Forums](https://forum.sparkfun.com/viewforum.php?f=143) are a great place to find and ask for help.\
\

[SparkFun Forums](https://forum.sparkfun.com/)

### Qwiic Speaker Amp Responding Slow

By default, the TPA2016D2 can take a few seconds before changes to its configuration are applied. Try following the application note in example 1 to disable the limiter, disable the noise gate, and adjust the release/attach values to 1. The changes are not saved upon every power cycle. If power is removed from the Qwiic Speaker Amp, you will need to send the configuration again.

### No Sound from Speakers

Not hearing any sound from either speaker? Try checking your connections and ensuring that the are secure.

- The thin wires attached on the thin speakers might not be fully in the screw terminals.
- If you are using alligator clips, make sure that they are not touching the speaker\'s frame. The 8Ω small, cone speakers do not have a lot of space between the tabs and its frame. A small bump may cause the alligator clips to touch the metal frame, cause a short, and damage the amplifier.
- Make sure that there is a sufficient power supply connected to the board and the PWR LED is lighting up (assuming that the jumper is still closed).
- Make sure that the TRS cable or wires are fully connected to the audio source.
- Check the volume and ensure that it is not set to 0 on your audio source.
- Make sure that there is power applied on the audio board.