# Source: https://learn.sparkfun.com/tutorials/audio-codec-breakout---wm8960-hookup-guide

## Introduction

The [SparkFun Audio Codec Breakout - WM8960](https://www.sparkfun.com/products/21250) is a low power, high quality stereo codec with 1W Stereo Class D speaker drivers and headphone drivers. The WM8960 acts as a stereo audio ADC and DAC, and communicates using I^2^S, a standard audio data protocol (not to be confused with I^2^C). This audio codec is chock full of features some of which includes advanced on-chip digital signal processing for automatic level control (ALC) for the line or microphone input, programmable gain amplifier (PGA), pop and click suppression, and its ability to configure I^2^S settings and analog audio path through software via I^2^C.

[![SparkFun Audio Codec Breakout - WM8960 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/0/1/0/21250-_BOB_SparkFun_Audio_Codec_Breakout-_01.jpg)](https://www.sparkfun.com/sparkfun-audio-codec-breakout-wm8960.html)

### [SparkFun Audio Codec Breakout - WM8960 (Qwiic)](https://www.sparkfun.com/sparkfun-audio-codec-breakout-wm8960.html) 

[ BOB-21250 ]

The SparkFun WM8960 Audio Codec Breakout is a low-power, high-quality stereo codec with 1W Stereo Class D speaker drivers and...

**Retired**

[![SparkFun Audio Codec Breakout - WM8960 with Headers (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/5/7/8/21772-01.jpg)](https://www.sparkfun.com/sparkfun-audio-codec-breakout-wm8960-with-headers-qwiic.html)

### [SparkFun Audio Codec Breakout - WM8960 with Headers (Qwiic)](https://www.sparkfun.com/sparkfun-audio-codec-breakout-wm8960-with-headers-qwiic.html) 

[ BOB-21772 ]

The SparkFun WM8960 Audio Codec Breakout with Headers is a low-power, high-quality stereo codec with 1W Stereo speaker driver...

**Retired**

### Required Materials

To follow along with this tutorial, you will need the following materials at a minimum. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary. Note that the wishlist does not include any microphones or speakers.

**Note:** For users interested in just the wireless speaker and example 9, check out the [SparkFun Qwiic Wireless Speaker Kit](https://www.sparkfun.com/products/21773) below! The kit includes a TRRS breakout with headers instead of the TRS breakout. RING2 of the TRRS connector also connects to the TRS cable\'s sleeve. When wiring your circuit up, we recommend connecting to the sleeve in case you have a headphone with a TRRS connector. The kit also includes a mini amplified speaker.\
\

[![SparkFun Qwiic Wireless Speaker Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/5/7/9/21773-_KIT-_1.jpg)](https://www.sparkfun.com/sparkfun-qwiic-wireless-speaker-kit.html)

### [SparkFun Qwiic Wireless Speaker Kit](https://www.sparkfun.com/sparkfun-qwiic-wireless-speaker-kit.html) 

[ KIT-21773 ]

The SparkFun Qwiic Wireless Speaker Kit provides you with everything you need to make a wireless audio speaker.

**Retired**

### Arduino Microcontroller

You will need an Arduino microcontroller to configure the WM8960. We recommend the Espressif\'s ESP32 WROOM. For the scope of this tutorial, we will be using the IoT RedBoard ESP32 - Development Board since it already includes female headers on the board to connect jumper wires to the WM8960.

[![SparkFun Thing Plus - ESP32 WROOM (USB-C)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/9/6/8/20168Diagonal.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html)

### [SparkFun Thing Plus - ESP32 WROOM (USB-C)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html) 

[ WRL-20168 ]

The USB-C variant of ESP32 Thing Plus is a development board with WiFi, SPP, BLE, Qwiic connector, 21 I/O pins, RGB status LE...

[ [\$33.73] ]

[![SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/4/1/15663-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html)

### [SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html) 

[ WRL-15663 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

[ [\$24.95] ]

[![SparkFun IoT RedBoard - ESP32 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/8/0/0/ESP32_03.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html)

### [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html) 

[ WRL-19177 ]

The IoT RedBoard is an ESP32 WROOM-equipped development board that has everything you need in an Arduino Uno with extra perks...

[ [\$41.87] ]

### Differential Microphone Input

Below is a differential microphone from the catalog that you can connect as a differential microphone input. Note that you will need a resistor and the MICBIAS pin to connect to the eletret microphone.

[![Electret Microphone](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/6/9/08635-03-L.jpg)](https://www.sparkfun.com/electret-microphone.html)

### [Electret Microphone](https://www.sparkfun.com/electret-microphone.html) 

[ COM-08635 ]

Small electret microphone. Useful in acoustic and audio applications.

[ [\$1.50] ]

### Single Ended Microphone Input

Below are a few [electret and MEMS microphones from the catalog](https://www.sparkfun.com/categories/tags/microphone) that you can connect as a single ended microphone input.

[![SparkFun Analog MEMS Microphone Breakout - SPH8878LR5H-1](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/0/2/5/19389-SparkFun_Analog_MEMS_Microphone_Breakout_-_SPH8878LR5H-1-01.jpg)](https://www.sparkfun.com/sparkfun-analog-mems-microphone-breakout-sph8878lr5h-1.html)

### [SparkFun Analog MEMS Microphone Breakout - SPH8878LR5H-1](https://www.sparkfun.com/sparkfun-analog-mems-microphone-breakout-sph8878lr5h-1.html) 

[ BOB-19389 ]

The SparkFun Analog MEMS Microphone Breakout makes it easy to work with the SPH8878LR5H-1 analog microphone from Knowles.

[ [\$8.95] ]

[![SparkFun Electret Microphone Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/9/5/2/0/12758-02.jpg)](https://www.sparkfun.com/sparkfun-electret-microphone-breakout.html)

### [SparkFun Electret Microphone Breakout](https://www.sparkfun.com/sparkfun-electret-microphone-breakout.html) 

[ BOB-12758 ]

This small breakout board couples an Electret microphone (100Hz\--10kHz) with a 60x mic preamplifier to amplify the sounds of ...

[ [\$8.50] ]

[![SparkFun Analog MEMS Microphone Breakout - ICS-40180](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/2/2/1/18011-SparkFun_Analog_MEMS_Microphone_Breakout_-_ICS-40180-01.jpg)](https://www.sparkfun.com/sparkfun-analog-mems-microphone-breakout-ics-40180.html)

### [SparkFun Analog MEMS Microphone Breakout - ICS-40180](https://www.sparkfun.com/sparkfun-analog-mems-microphone-breakout-ics-40180.html) 

[ BOB-18011 ]

The SparkFun Analog MEMS Microphone Breakout makes it easy to work with the InvenSense ICS-40180 analog microphone.

**Retired**

### Differential Speaker Output

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

Note that some speakers may be rated as a higher wattage (more than what the Audio Codec\'s speaker driver can output). Higher wattage speakers will still play sound but they won\'t be fully powered.

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

**Note:** Amplified speakers that have a 3.5mm TRS audio connector can also be used. However, you will not be using the speaker output channels. Users can connect the headphone output to amplified speakers with a TRS audio connector as well. The hamburger mini speaker could be one option.\
\

[![Hamburger Mini Speaker](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/3/1/14023-01.jpg)](https://www.sparkfun.com/hamburger-mini-speaker.html)

### [Hamburger Mini Speaker](https://www.sparkfun.com/hamburger-mini-speaker.html) 

[ COM-14023 ]

This will be a treat for your ears! The Hamburger Mini Speaker is a 3W economical speaker option for any project needing stan...

[ [\$7.95] ]

**Looking for more power?** Try connecting the audio codec\'s headphone output to another external amplifier like the Qwiic Speaker Amp. The Qwiic Speaker Amp is capable of driving 4Ω speakers at up to 2.8W in stereo, and 8Ω speakers at up to 1.7W in stereo.\
\

[![SparkFun Qwiic Speaker Amp](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/5/3/2/20690_DEV-_SparkFun_Qwiic_Speaker_Amp-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-speaker-amp.html)

### [SparkFun Qwiic Speaker Amp](https://www.sparkfun.com/sparkfun-qwiic-speaker-amp.html) 

[ DEV-20690 ]

The SparkFun Qwiic Speaker Amp includes the Texas Instruments TPA2016D2 class-D stereo audio amp.

[ [\$15.50] ]

### Audio Accessories

Depending on your setup, you may need an adapter or cable for the TRS audio connection for line level input or headphone output.

[![Audio Cable TRS - 1m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/5/5/8/18983-TRS_3.5mm_Cable-01.jpg)](https://www.sparkfun.com/audio-cable-trs-1m.html)

### [Audio Cable TRS - 1m](https://www.sparkfun.com/audio-cable-trs-1m.html) 

[ CAB-18983 ]

This cable has a standard TRS 3.5mm plug on both ends allowing for easy connections to any 3.5mm jack.

[ [\$2.75] ]

[![Audio Jack 3.5mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/8/2/08032-Audio_Jack_3.5mm-01.jpg)](https://www.sparkfun.com/audio-jack-3-5mm.html)

### [Audio Jack 3.5mm](https://www.sparkfun.com/audio-jack-3-5mm.html) 

[ PRT-08032 ]

Low profile 3.5mm stereo audio jack.

[ [\$1.75] ]

[![SparkFun Audio Jack Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/5/2/2/9/10588-01a.jpg)](https://www.sparkfun.com/sparkfun-audio-jack-breakout.html)

### [SparkFun Audio Jack Breakout](https://www.sparkfun.com/sparkfun-audio-jack-breakout.html) 

[ PRT-10588 ]

Simple breakout board for the 3.5mm audio jack. Use this breakout (shipped bare) to allow breadboard or SIP access to the sup...

[ [\$1.50] ]

You can also use a TRRS breakout instead of the TRS breakout listed above. RING2 of the TRRS connector also connects to the TRS cable\'s sleeve. When wiring your circuit up, we recommend connecting to the sleeve in case you have a headphone with a TRRS connector.

[![SparkFun TRRS 3.5mm Jack Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/7/5/4/6/11570-01.jpg)](https://www.sparkfun.com/sparkfun-trrs-3-5mm-jack-breakout.html)

### [SparkFun TRRS 3.5mm Jack Breakout](https://www.sparkfun.com/sparkfun-trrs-3-5mm-jack-breakout.html) 

[ BOB-11570 ]

TRRS connectors are the audio-style connectors that you see on some phones, MP3 players and development boards. TRRS stands f...

[ [\$4.50] ]

### Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49) for a secure connection when using the plated through hole pads.

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

#### Prototyping Accessories

Depending on your setup, you may want to use IC hooks for a temporary connection. However, you will want to solder header pins to connect devices to the plated through holes for a secure connection. Note that you will need to breakaway the male header pins or cut the female header pins down to fit the two rows of 1x16 PTH on the breakout. Of course, you could also solder wire as well.

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![IC Hook with Pigtail](https://cdn.sparkfun.com/r/140-140/assets/parts/3/6/9/6/09741-01.jpg)](https://www.sparkfun.com/ic-hook-with-pigtail.html)

### [IC Hook with Pigtail](https://www.sparkfun.com/ic-hook-with-pigtail.html) 

[ CAB-09741 ]

These are good quality IC test hooks with a male connection wire. Instead of a single hook, these have two hooks that are cap...

[ [\$5.75] ]

[![Thing Stackable Header Set](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/7/9/14311-01.jpg)](https://www.sparkfun.com/esp32-thing-stackable-header-set.html)

### [Thing Stackable Header Set](https://www.sparkfun.com/esp32-thing-stackable-header-set.html) 

[ PRT-14311 ]

These headers are made to work with the SparkFun ESP32 Thing to connect to ESP32 Shield boards.

[ [\$2.50] ]

[![Jumper Wires Premium 6\" M/M Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/1/JumperWire-Male-01-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html)

### [Jumper Wires Premium 6\" M/M Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html) 

[ PRT-08431 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumpers with male connectors on both ends. Use these to jumper fro...

[ [\$5.25] ]

For users that are interested in adding an input to adjust volume or modes, you can add a trimpot and button to the setup. A few of the examples used in this tutorial use the trimpot to adjust. You will need to add a few lines of code if you want to toggle certain modes (i.e. 3D enhance, loopback, etc) or if you decided to use buttons to turn up or down the volume. For advanced users using their own differential microphones, you will need to add a 2.2kΩ resistor in series with each microphone. Other passives like capacitors may also be needed depending on your application.

[![Resistor Kit - 1/4W (500 total)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/1/7/1/10969-Resistor_Kit_-_1_4W__500_total_-01.jpg)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html)

### [Resistor Kit - 1/4W (500 total)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html) 

[ COM-10969 ]

Nothing stops a project dead in its tracks faster than not having the right resistor. These components are arguably the most ...

[ [\$10.50] ]

[![Trimpot 10K Ohm with Knob](https://cdn.sparkfun.com/r/140-140/assets/parts/3/8/2/3/09806-01.jpg)](https://www.sparkfun.com/trimpot-10k-ohm-with-knob.html)

### [Trimpot 10K Ohm with Knob](https://www.sparkfun.com/trimpot-10k-ohm-with-knob.html) 

[ COM-09806 ]

This 10K trimmable potentiometer has a small knob built right in and it\'s breadboard friendly to boot!

[ [\$1.25] ]

[![Multicolor Buttons - 4-pack](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/1/8/14460-01.jpg)](https://www.sparkfun.com/multicolor-buttons-4-pack.html)

### [Multicolor Buttons - 4-pack](https://www.sparkfun.com/multicolor-buttons-4-pack.html) 

[ PRT-14460 ]

This is a simple 4-pack of momentary, multicolor buttons, great for all sorts of projects! Unlike previous iterations of mult...

[ [\$1.95] ]

[![Electrolytic Decoupling Capacitors - 100uF/25V](https://cdn.sparkfun.com/r/140-140/assets/parts/8/9/00096-03-L.jpg)](https://www.sparkfun.com/electrolytic-decoupling-capacitors-100uf-25v.html)

### [Electrolytic Decoupling Capacitors - 100uF/25V](https://www.sparkfun.com/electrolytic-decoupling-capacitors-100uf-25v.html) 

[ COM-00096 ]

Electrolytic decoupling capacitors 100uF/25V. These capacitors are great transient/surge suppressors. Attach one between the ...

[ [\$0.50] ]

For those that want to take advantage of the Qwiic enabled devices, you\'ll want to grab a Qwiic cable.

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

### You Will Also Need

Depending on your setup, you will also need some sort of audio source. This can be from your smartphone or computer. Most of the examples listed in this tutorial will output the audio through the headphones. You will also need to have a pair of headphones with a 3.5mm TRS audio jack on the end.

- Audio Source
  - MP3 Player
  - Bluetooth ® Audio Device (e.g. smartphone, computer, transmitter)
- Headphones with 3.5mm TRS Audio Jack

### Suggested Reading

If you aren\'t familiar with the MicroMod ecosystem, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic) if you decide to take advantage of the Qwiic connector.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/8/2/Qwiic-registered-black.png "Click to learn more about the Qwiic Connect System!")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you aren't familiar with the following concepts, we also recommend checking out a few of these tutorials before continuing. Make sure to check the respective hookup guides for your microcontroller to ensure that you are installing the correct USB-to-serial converter. You may also need to follow additional instructions that are not outlined in this tutorial to install the appropriate software.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/sparkfun-serial-basic-ch340c-hookup-guide)

### SparkFun Serial Basic CH340C Hookup Guide 

SparkFun Serial Basic Breakout takes advantage of USB-C and is an easy-to-use USB-to-Serial adapter based on the CH340C IC from WCH. With USB-C you can get up to three times the power delivery over the previous USB generation and has the convenient feature of being reversable.

[](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Installing Board Definitions in the Arduino IDE 

How do I install a custom Arduino board/core? It\'s easy! This tutorial will go over how to install an Arduino board definition using the Arduino Board Manager. We will also go over manually installing third-party cores, such as the board definitions required for many of the SparkFun development boards.

[](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide)

### IoT RedBoard ESP32 Development Board Hookup Guide 

Delve into the functionality-rich world of the IoT RedBoard ESP32 Development Board!

## Hardware Overview

We broke out the pins of the WM8960 onto a breakout board to standard 0.1\" spaced PTH. We\'ll highlight relevant application circuits, hardware, and pins that are broken out in this section.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Top View](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_Top_View.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_Top_View.jpg)   [![Bottom View](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_Bottom_View.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_Bottom_View.jpg)
  *Top View*                                                                                                                                                                                                                          *Bottom View*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Keep in mind that the WM8960 is chock full of features as you can see from the datasheet\'s block diagram below. The input and output will depend on your project\'s needs. We recommend referencing the block diagrams listed in the datasheet to follow along. For more information, check out the datasheet linked in the [Resources and Going Further](https://learn.sparkfun.com/tutorials/audio-codec-breakout---wm8960-hookup-guide#resources-and-going-further).

[![Block Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/Block_Diagram_WM8960.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/Block_Diagram_WM8960.JPG)

*Block diagram from the WM8960 Datasheet (v4.2) on page 1.*

### Power

There are a variety of power and power-related nets broken out to the Qwiic connector and through hole pads on the edge of the board. The nets consist of the following.

- **VIN** - Voltage input for the analog and speaker circuits. The input voltage is between **3.7V** and **5.5V**.
  - **SPKVDD** - By default, the **VIN** pin is connected directly to **SPKVDD**. The connection can be disabled but cutting the jumper on the back between **VIN** and **SPKVDD**. There is an option to connect the **SPKVDD** pad to the **3V3** pin by adding a solder blob between the two pads. If you decide to provide your own voltage, users will need to keep the jumpers open. The recommended voltage for this pin is between **2.7V** and **5.5V**.
  - **AVDD** - Voltage from the **VIN** pin is regulated down to **3.3V** from the XC6222 3.3V/700mA voltage regulator. This voltage is used to power the analog circuit. For users that want to provide their own voltage, cut the jumper on the back of the board labeled as **AVDD-ISO**. The recommended voltage for this pin is between **2.7V** and **3.6V**.
- **3V3** - This pin is broken out on the edge of the board as well as the Qwiic connector. This voltages is used to power the digital circuit. This voltage is tied to the IC\'s DCVDD and DBVDD pins. Note that this is on a separate net and not connected to the 3.3V voltage regulator. The recommended voltage for this pin is between **1.7V** and **3.6V**. This will typically be **3.3V** when connecting to a microcontroller\'s 3.3V voltage regulator and Qwiic connector.
- **GND** - Common, ground voltage (0V reference) for the system.

[![Various Power and Ground Nets](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout-Power_Ground_Nets.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout-Power_Ground_Nets.jpg)

To get started powering the audio codec, you will just need to provide power to the **VIN** and **3V3** pins. We recommend using your development board\'s voltages without adjusting the jumpers. For example, the IoT RedBoard - ESP32 Development Board can provide 5V through the female header and 3.3V through the Qwiic connector. Users can connect 5V to the audio codec\'s VIN pin to power the analog and speaker circuit. To power the digital circuit, users can provide 3.3V by adding a Qwiic cable between the Qwiic connectors. Of course, you will need to also connect your reference voltage for your system. By using the Qwiic cable, you will be connecting GND on both boards.

**⚡ Warning!** If you decide to cut the trace between **VDD** and **SPKVDD** to connect **SPKVDD** to **3V3**, make sure to avoid any shorts between **VDD** and **SPKVDD**. If you place an input voltage on **VIN** that is higher than **3V3** pin is rated for will damage the WM8960 and anything connected to **3V3**.\
\
For users providing their own power supply for **SPKVDD** and **AVDD**, make sure to keep the jumpers open.

### Enable Pin

The enable pin (labeled as [EN]) on the edge of the board is active low. Pulling the pin low will disable the 3.3V voltage regulator XC6222 that is connected to AVDD.

[![Analog Voltage Regulator Enable Pin](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_enable_pin.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_enable_pin.jpg)

### Digital Audio Interface

The board breaks out pins for the digital audio interface. This is used for inputting DAC data into the WM8960 and outputting ADC data from the IC.

- **BCLK** - Bit clock, for synchronization. This can be set as an input or output depending on the configuration.
- **DLRC** or **DACLRC** - DAC data left and right alignment clock. This can be set as an input or output depending on the configuration.
- **DDAT** or **DACDAT** - DAC data input.
- **ALRC** or **ADCLRC** - ADC data left and right alignment clock. This can be set as an input or output depending on the configuration.
  - This pin can also be configured as a GPIO pin (e.g. GPIO1). As stated in the datasheet, the ADC will use the DACLRC as a frame clock for the ADCs and DACs. The ADCLRC/GPIO1 pin function should not be modified when the ADC is enabled. For more information check out the section about the Digital Audio Interface in the datasheet on pg 48.
- **ADAT** or **ADCDAT** - ADC data output.

[![Digital Audio Interface](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_Digital_Audio_Interface.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_Digital_Audio_Interface.jpg)

Four audio data formats listed below are supported.

- Left justified
- Right justified
- I^2^S (not to be confused with I^2^C)
- DSP

### Qwiic and I^2^C

The board includes one Qwiic connector to configure the I^2^S settings and analog audio path. For users that need to solder directly to the board, the pins are also broken out on the edge PTH. The I^2^C data and clock lines are also tied to 2.2kΩ pull-up resistors. The default address of the WM8960 is **0x1A**. *Note that the datasheet shows the address as 0x34h, which is 0x1A shifted left 1 bit and then includes the appended \"0\" (aka write bit).*

[![Qwiic Connector and I2C Port](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_Qwiic_I2C_Port.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_Qwiic_I2C_Port.jpg)

### Stereo Input

The WM8960 includes 6x flexible analog input pins. These pins can be used for line level or microphone level (balanced or un-balanced). Note that balanced microphones refers to differential microphones while un-balanced microphones refers to single-ended microphones.

- **RIN3** / **RINPUT3** - Right analog input 3 pin. This is connected to *RINPUT3* or JD3.
  - right channel, line input
  - right channel, differential +MIC input
  - jack detect input pin
- **RIN2** / **RINPUT2** - Right analog input 2 pin. This is connected to *RINPUT2*.
  - right channel, line input
  - right channel, differential +MIC input
- **RIN1** / **RINPUT1** - Right analog input 1 pin. This is connected to *RINPUT1*.
  - right channel, single-ended MIC input
  - right channel, differential -MIC input
- **LIN1** / **LINPUT1** - Left analog input 1 pin. This is connected to *LINPUT1*.
  - left channel, single-ended MIC input
  - left channel differential -MIC input
- **LIN2** / **LINPUT2** - Left analog input 2 pin. This is connected to *LINPUT2*.
  - left channel, line input
  - left channel, differential +MIC input
- **LIN3** / **LINPUT3** - Left analog input 3 pin. This is connected to *LINPUT3* or *JD2*.
  - left channel, line input
  - left channel, differential +MIC input
  - jack detect input pin

[![Line and Microphone Input Pins](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_line_input.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_line_input.jpg)

Remember the block diagram that was linked earlier just before soldering the headers to the board? The datasheet goes into more detail with the input path for the left and right channel.

Below is a modified image of the block diagram that highlights the input signal path before the left ADC for the left input channels on page 19.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/Block_Diagram_WM8960_Left_Input_zoomed_in.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/Block_Diagram_WM8960_Left_Input_zoomed_in.jpg)

*Left Input Signal Path from the WM8960 Datasheet (v4.2) on page 19.*

**Note:** Note that the pins are flipped from the initial block diagram and the left input channels. Instead of LINPUT3 at the top, it starts with LINPUT1.

Below is a modified image of the block diagram that highlights the input signal path before the right ADC for the right input channels on page 20.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/Block_Diagram_WM8960_Right_Input_zoomed_in.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/Block_Diagram_WM8960_Right_Input_zoomed_in.jpg)

*Right Input Signal Path from the WM8960 Datasheet (v4.2) on page 20.*

### Microphone Bias

The **MICB** or **MICBIAS** provides a low noise reference voltage for biasing eletret condenser microphones (ECMs).

[![Microphone Bias](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_MICBIAS.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_MICBIAS.jpg)

### Speaker Out

The WM8960 includes differential stereo speaker outputs for the left and right speaker. The speaker is rated as a class D speaker driver and can drive 1W into 8Ω speakers. For users looking to power the speakers with a separate power supply, you can cut the jumper between the pads labeled as **SPKVDD** and **VIN** on the back of the board.

- **SL+** / **SPK_LP** - Speaker left positive output.
- **SL-** / **SPK_LN** - Speaker left negative output.
- **SR+** / **SPK_RP** - Speaker right positive output.
- **SR-** / **SPK_RN** - Speaker right negative output.

[![Speaker Pins](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_Speaker_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_Speaker_Output.jpg)

**Note:** When wiring differential speakers to speaker out terminals, make sure to match the \"+\" to \"+\" and \"-\" to \"-\" for both speakers. If one of the stereo speakers is wired \"+\" to \"-\" and \"-\" to +\" while the other speaker is wired \"+\" to \"+\" and \"-\" to \"-\", the audio signals will interfere and cancel each other out. If there are no labels on the speakers, just make sure to wire the speakers consistently.

### Headphones Output

The WM8960 can drive 16Ω and 32Ω headphones. The connection will depend on your setup. Make sure to check out the **Headphone Output** in the datasheet on page 41 for more information.

- **HPL** - The left headphone out will be connected to the Tip of a TRS connector.
- **OUT3** - This is connected to the Sleeve of a TRS connector. If using DC blocking capacitors, connect this pin to AGND.
- **HPR** - The right headphone out will be connected to the Ring of a TRS connector.

[![Headphone Output Pins](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_headphone_output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_headphone_output.jpg)

### LED

The board includes one LED labeled as **PWR**. This indicates when there is power on the 3.3V net to power the IC\'s digital circuit. You can disable it with the jumper on the back of the board.

[![LED](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_LED.jpg)

### Jumpers

**Note:** If this is your first time working with jumpers, check out the [How to Work with Jumper Pads and PCB Traces](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all) tutorial for more information.

The following ten jumpers are included on the Audio Codec Breakout - WM8960.

- **VIN**, **SPKVDD**, and **3V3** - This 3-pad jumper allows users to select a voltage source for the speaker VDD (**SPKVDD**). By default, the center pad (**SPKVDD**) is closed on the **VIN** pad. Cut this trace and add a solder blob on the **3V3** side to provide **SPKVDD** with 3.3V. Leave both jumpers open to provide an external voltage for SPKVDD from the header pin.
- **AVDD-ISO** - By default, this jumper is closed. Cut this jumper to isolate AVDD from the voltage regulator to provide a VDD from the header pin.
- **LED** - By default, this jumper is closed and located on the bottom of the board. Cut this trace to disable the LED that is connected to the output of the 3.3V voltage regulator.
- **I2C** - By default, this 3-pad jumper is closed and located on the bottom of the board. The 2.2kΩ pull-up resistors are attached to the primary I^2^C bus; if multiple devices are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, [disable all but one pair of pull-up resistors](https://learn.sparkfun.com/tutorials/i2c/all#i2c-at-the-hardware-level) if multiple devices are connected to the bus.

[![Jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/21250-SparkFun_Audio_Codec_Breakout_Jumpers.jpg)

**⚡ Warning!** If you decide to cut the trace between **VDD** and **SPKVDD** to connect **SPKVDD** to **3V3**, make sure to avoid any shorts between **VDD** and **SPKVDD**. If you place an input voltage on **VIN** that is higher than **3V3** pin is rated for will damage the WM8960 and anything connected to **3V3**.\
\
For users providing their own power supply for **SPKVDD** and **AVDD**, make sure to keep the jumpers open.

### Board Dimensions

The board dimensions of the Audio Codec Breakout - WM8960 is 1.60\" x 1.00\".

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/d/d/b/9/4/SparkFun_Audio_Codec_Breakout_WM8960_Board_Dimensions.png)](https://cdn.sparkfun.com/assets/d/d/b/9/4/SparkFun_Audio_Codec_Breakout_WM8960_Board_Dimensions.png)

## Hardware Hookup

There are a number of ways to connect to the input and output pins of the WM8960. We will go over each .

### Soldering

Header pins were left off the Audio Codec Breakout to allow users the flexibility of connecting any type of 0.1\"-spaced header to the board. Depending on your connections, you may need to solder additional breakout boards and adapters. For temporary connections to the I/O pins, you could use IC hooks to test out the pins. However, you\'ll need to [solder headers or wires of your choice to the board](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) for a secure connection. For the scope of this tutorial, we will be soldering male header pins on the board and wiring the circuit on a breadboard. Here are a few tutorials to connect to the pads depending on your personal preference.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

February 8, 2013

How to strip, crimp, and work with wire.

### Power

To power the WM8960 appropriately, you will just need to provide power to **VIN** and the **3V3** pins. As stated in the Hardware Overview: Power, you can take advantage of your development board\'s voltages without adjusting jumpers. We recommend making the following connection listed in the table.

  -----------------------------------------------------------------------
  Audio Codec - WM8960                IoT RedBoard - ESP32
  ----------------------------------- -----------------------------------
  VIN                                 5V

  GND                                 GND\
                                      (Additional Ground, optional)

  Qwiic Cable\'s 3.3V pin\            Qwiic Cable\'s 3.3V pin\
  (or 3.3V)                           (or 3.3V)

  Qwiic Cable\'s GND pin\             Qwiic Cable\'s GND pin\
  (or GND)                            (or GND)
  -----------------------------------------------------------------------

Using wires and the Qwiic cable to power VIN and 3V3, your circuit should look similar to the circuit diagram below. We will use this method to power the audio codec for the proceeding circuit diagrams.

[![Power Input and Power from Qwiic Cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Power_In-bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Power_In-bb.jpg)

⚡ **Danger:** Note that we are connecting 5V to the audio codec\'s VIN pin. Depending on the development board that you are using VIN from your Arduino may be too high of a voltage for the Audio Codec\'s VIN pin. Exceeding the voltage beyond the absolue maximum rating can damage the components on the audio codec breakout.

Depending on your setup, you could provide a separate input voltage to the SPKVDD and VDD. Just make sure to adjust the jumpers on the back as necessary.

**⚡ Warning!** If you decide to cut the trace between **VDD** and **SPKVDD** to connect **SPKVDD** to **3V3**, make sure to avoid any shorts between **VDD** and **SPKVDD**. If you place an input voltage on **VIN** that is higher than **3V3** pin is rated for will damage the WM8960 and anything connected to **3V3**.\
\
For users providing their own power supply for **SPKVDD** and **AVDD**, make sure to keep the jumpers open.

### Qwiic and I^2^C

To configure the I^2^S settings or signal path, you will need to connect to the I^2^C port. Users can save some time wiring this part of the circuit up by adding a Qwiic cable between the audio codec breakout and the IoT RedBoard ESP32. As an alternative, users could also solder to the PTH as well. We recommend making the following connection listed in the table.

  -----------------------------------------------------------------------
  Audio Codec - WM8960                IoT RedBoard - ESP32
  ----------------------------------- -----------------------------------
  Qwiic Cable\'s SCL pin\             Qwiic Cable\'s SCL pin\
  (or SCL)                            (or SCL)

  Qwiic Cable\'s SDA pin\             Qwiic Cable\'s SDA pin\
  (or SDA)                            (or SDA)

  Qwiic Cable\'s 3.3V pin\            Qwiic Cable\'s 3.3V pin\
  (or 3.3V)                           (or 3.3V)

  Qwiic Cable\'s GND pin\             Qwiic Cable\'s GND pin\
  (or GND)                            (or GND)
  -----------------------------------------------------------------------

Surprise! Your connection is basically the same as the circuit diagram in the previous section. We just highlighted the circuit connection for I^2^C data and clock lines here.

[![Power and I2C](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_I2C-bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_I2C-bb.jpg)

### Line Input 3

The following connection is for a line level input 3. For simplicity, the table does not include the power and I^2^C pins.

  Audio Codec - WM8960   TRS Connector
  ---------------------- ---------------
  LINPUT3                Tip
  RINPUT3                Ring
  GND                    Sleeve

Your circuit should look similar to the circuit diagram below.

[![Power, I2C, and Line Input 3](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_3-bb1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_3-bb1.jpg)

### Line Input 2

The following connection is for a line level input 2. For simplicity, the table does not include the power and I^2^C pins.

  Audio Codec - WM8960   TRS Connector
  ---------------------- ---------------
  LINPUT2                Tip
  RINPUT2                Ring
  GND                    Sleeve

Your circuit should look similar to the circuit diagram below.

[![Power, I2C, and Line Input 2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_2-bb1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_2-bb1.jpg)

### Line Input 1

The following connection is for a line level input 1. For simplicity, the table does not include the power and I^2^C pins.

  Audio Codec - WM8960   TRS Connector
  ---------------------- ---------------
  LINPUT1                Tip
  RINPUT1                Ring
  GND                    Sleeve

Your circuit should look similar to the circuit diagram below.

[![Power, I2C, and Line Input 1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_1-_bb1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_1-_bb1.jpg)

### I^2^S Passthrough

The following connection is for passing an audio source through the ADC and immediately back to the DAC. For simplicity, the table does not include the power and I^2^C pins. Note that this is for setting the codec as a I^2^S peripheral.

  Audio Codec - WM8960   IoT RedBoard - ESP32
  ---------------------- ----------------------
  DACDAT                 4
  BCLK                   16
  ADCDAT                 17
  DACLRC                 25
  ADCLRC                 25

Your circuit should look similar to the circuit diagram below.

[![Power, I2C, and I2S Passthrough](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_I2S_Passthrough_Arduino-bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_I2S_Passthrough_Arduino-bb.jpg)

### I^2^S Decoder

The following connection is for decoding audio. One example is if users connect an audio Bluetooth® device (such as your phone or laptop) to the ESP32 and stream music wirelessly. For simplicity, the table does not include the power and I^2^C pins. Note that this is for setting the codec as a I^2^S peripheral.

  Audio Codec - WM8960   IoT RedBoard - ESP32
  ---------------------- ----------------------
  DACDAT                 4
  BCLK                   16
  DACLRC                 25

Your circuit should look similar to the circuit diagram below.

[![Power, I2C, and I2S Decoder](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_I2S_Decoder_Arduino-bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_I2S_Decoder_Arduino-bb.jpg)

### Differential Microphone Input

The following connection is for connecting differential microphones to the audio codec. When using a pseudo-differential microphone configuration, make sure to include a 2.2kΩ resistor between the MICBIAS and the + terminals of each differential microphone. You will also need to set voltage on the MICBIAS pin. For simplicity, the table does not include the power and I^2^C pins.

  Audio Codec - WM8960   Resistor   Electret Microphone
  ---------------------- ---------- ---------------------
  GND                               Left Mic -
  LINPUT1                           Left Mic -
  LINPUT2                           Left Mic +
  MICBIAS                2.2kΩ      Right Mic +
  GND                               Right Mic -
  LINPUT1                           Right Mic -
  LINPUT2                           Right Mic +
  MICBIAS                2.2kΩ      Right Mic +

Your circuit should look similar to the circuit diagram below.

[![Psuedo-Differential Microphone Configuration](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Microphone-Bias-Eletret_Micsbb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Microphone-Bias-Eletret_Micsbb.jpg)

### Single Ended Microphone Input

The following connection is for connecting single ended microphones to the audio codec. Instead of using a line level input from the TRS connector, users can also connect unbalanced microphones (these are usually microphones with an amplifier on the breakout boards and have one audio output pin) to the left and right pins of INPUT1. Make sure to also connect power and GND to the boards. For simplicity, the table does not include the power and I^2^C pins between the ESP32 and WM8960.

  ----------------------------------------------------------------------------------------------------------------
  Audio Codec - WM8960   Single Ended Microphone (Left)   Single Ended Microphone (Right)   IoT RedBoard - ESP32
  ---------------------- -------------------------------- --------------------------------- ----------------------
  Qwiic Cable\'s\        GND                              GND                               GND
  GND pin\                                                                                  
  (or GND)                                                                                  

  LINPUT1                AUD                                                                

  RINPUT1                                                 AUD                               

  Qwiic Cable\'s\        3.3V                             3.3V                              3.3V
  3.3V pin\                                                                                 
  (or 3.3V)                                                                                 
  ----------------------------------------------------------------------------------------------------------------

Your circuit should look similar to the circuit diagram below.

[![Single Ended Microphone Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Single_Ended_Mic_In_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Single_Ended_Mic_In_bb.jpg)

### Headphone Output

Based on the recommended output configuration from the datasheet, we will be using a capless headphone output in this tutorial.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/Headphone_Output_Block_Diagram-WM8960.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/Headphone_Output_Block_Diagram-WM8960.JPG)

*Recommended headphone output configuration from the WM8960 Datasheet (v4.2) on page 41.*

The following connection is for connecting headphones to the audio codec\'s headphone output. For simplicity, the table does not include the power and I^2^C pins.

  Audio Codec - WM8960   TRS Connector
  ---------------------- ---------------
  HPL                    Tip
  HPR                    Ring
  OUT3                   Sleeve

[![Power, I2C, and Headphone Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Headphone_Out-bb1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Headphone_Out-bb1.jpg)

### Differential Speaker Output

There are a few recommended speaker output configurations from the datasheet to minimize the speaker connection losses due to series resistance and EMI. For a basic setup, we will be using a short wire connection between the audio codec\'s breakout board and each differential speaker. For those that require long exposed track and want to go the extra mile, users can build an LC filter circuit, add ferrite beads, or shield the wires using PCB ground plane (or Vdd).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/Recommended_Speaker_Configurations_WM8960.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/Recommended_Speaker_Configurations_WM8960.JPG)

*Recommended speaker output configuration from the WM8960 Datasheet (v4.2) on page 88.*

The following connection is for connecting speakers to the audio codec\'s speaker output channels. For simplicity, the table does not include the power and I^2^C pins.

  Audio Codec - WM8960   Speakers
  ---------------------- -----------------
  SL+                    Speaker Left +
  SL-                    Speaker Left -
  SR+                    Speaker Right +
  SR+                    Speaker Right -

[![Power, I2C, and Speakers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Speaker_Out-bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Speaker_Out-bb.jpg)

## Software Installation

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review the following tutorials.\
\

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Arduino Board Definitions and Driver

We\'ll assume that you installed the necessary board files and drivers for your development board. In this case, we used the IoT RedBoard - ESP32 which uses the CH340 USB-to-serial converter. If you are using a Processor Board, make sure to check out its hookup guide for your Processor Board.

[](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Installing Board Definitions in the Arduino IDE 

September 9, 2020

How do I install a custom Arduino board/core? It\'s easy! This tutorial will go over how to install an Arduino board definition using the Arduino Board Manager. We will also go over manually installing third-party cores, such as the board definitions required for many of the SparkFun development boards.

[](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide)

### IoT RedBoard ESP32 Development Board Hookup Guide 

August 18, 2022

Delve into the functionality-rich world of the IoT RedBoard ESP32 Development Board!

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

### Installing the Arduino Library

The SparkFun Arduino library can be downloaded with the Arduino library manager by searching \'**SparkFun Audio Codec Breakout WM8960**\' or you can grab the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library) to manually install.

[SparkFun WM8960 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/archive/refs/heads/main.zip)

## Example 1: Volume

In this example, we will pass a line level audio source into the WM8960\'s line input 3 port. The signal will go through the mixers and gain stages of the audio codec. For this output, we will be sending the audio to the headphones.

### Hardware Hookup

Connect power, I^2^C, line input 3 port, and the headphone output as explained earlier. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In-3_Line_Out-bb1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In-3_Line_Out-bb1.jpg)

Connect a USB cable into your IoT RedBoard ESP32 and a TRS cable from your audio source (e.g. MP3 player, smartphone, or computer) into the audio connector. Then connect your headphones to the output. For those that are sensitive to sounds, you may want to hear the example output before inserting the headphones into your ears.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_01_Volume](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_01_Volume/Example_01_Volume.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Monitor and set it to **115200** baud to view the serial output. Then hit the play button on your audio source. Make sure that the volume from the audio source is turned up. You should hear some music from the headphones. After every 5 seconds, the volume will decrease until it is muted.

If you waited too long to hit the play button, the audio codec may have already muted the track. Try hitting the reset button on the IoT RedBoard to restart the example since it executes the code once.

## Example 2: Line Input 2

In this example, we will pass a line level audio source into the WM8960\'s line input 2 port. The signal will go through the mixers and gain stages of the audio codec like the previous example. For the output we will be sending the audio to the headphones as well.

### Hardware Hookup

Connect power, I^2^C, line input 2 port, and the headphone output as explained earlier. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In-2_Line_Out-bb1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In-2_Line_Out-bb1.jpg)

If you have not already, insert a USB cable into your IoT RedBoard ESP32 and a TRS cable from your audio source (e.g. MP3 player, smartphone, or computer) into the audio connector. Then connect your headphones to the output. For those that are sensitive to sounds, you may want to hear the example output before inserting the headphones into your ears.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_02_INPUT2](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_02_INPUT2/Example_02_INPUT2.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Monitor and set it to **115200** baud to view the serial output. Then hit the play button on your audio source. Make sure that the volume from the audio source is turned up. You should hear some music from the headphones. Compared to the first example, this just sets the volume once.

## Example 3: Line Input 1 \[or Single Ended Microphone Input \] 

Similar to the past two examples, we will pass the line level audio source into the WM8960\'s line input 1 port. As an alternative, users can also wire up single ended microphones to input 1 instead of using a line level audio source from the TRS connector. The signal will go through the mixers and gain stages of the audio codec. Again, we will be sending the audio to the headphone output.

### Hardware Hookup 1

Connect power, I^2^C, line input 1, and the headphone output as explained earlier. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In-1_Line_Out-bb1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In-1_Line_Out-bb1.jpg)

Connect a USB cable into your IoT RedBoard ESP32 and a TRS cable from your audio source (e.g. MP3 player, smartphone, or computer) into the audio connector. Then connect your headphones to the output. For those that are sensitive to sounds, you may want to hear the example output before inserting the headphones into your ears.

### Hardware Hookup 2

Input 1 also has the ability to allow single ended microphones to the left and right inputs. As an alternative, you can also connect single ended electret or MEMS microphones to these pins. Connect power, I^2^C, single ended microphones, and the headphone output as explained earlier. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Single_Ended_Mic_In_Line_Out_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Single_Ended_Mic_In_Line_Out_bb.jpg)

**Note:** The audio input for each of the MEMS Mic is located on the bottom of the board. The Fritzing part show the top view of the MEMs Mic. Depending on your application, you may want to consider soldering wire, using a right angle header, or soldering the male header pins from the bottom side.

Connect a USB cable into your IoT RedBoard ESP32. Then connect your headphones to the output. For those that are sensitive to sounds, you may want to hear the example output before inserting the headphones into your ears.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_03_INPUT1](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_03_INPUT1/Example_03_INPUT1.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Monitor and set it to **115200** baud to view the serial output. Then hit the play button on your audio source if you are using a TRS connector. Make sure that the volume from the audio source is turned up. You should hear some music from the headphones. This is basically the same as the previous two examples but now we are using input 1.

## Example 4: Speaker

In this example, we will pass a line level audio source into the WM8960\'s line input 1 port. The signal will go through the mixers and gain stages of the audio codec. For the output, we will be sending the audio to a pair of differential speakers.

### Hardware Hookup

Connect power, I^2^C, line input 1, and the speakers on the output channels as explained earlier. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_Stereo_Speakers-bb1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_Stereo_Speakers-bb1.jpg)

If you have not already, insert a USB cable into your IoT RedBoard ESP32 and a TRS cable from your audio source (e.g. MP3 player, smartphone, or computer) into the audio connector.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_04_Speaker](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_04_Speaker/Example_04_Speaker.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Monitor and set it to **115200** baud to view the serial output. Then hit the play button on your audio source. Make sure that the volume from the audio source is turned up. You should hear some music from the speakers.

## Example 5: Loopback

In this example, we will pass a line level audio source into the WM8960\'s line input 1 port. The signal will go through the mixers and gain stages of the audio codec. What\'s different in this example is that we will also turn on loopback so that the ADC is fed directly to the DAC. The output of the DAC will then be sent to the headphone output.

### Hardware Hookup

Connect power, I^2^C, line input 1, and the headphone output as explained earlier. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In-1_Line_Out-bb1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In-1_Line_Out-bb1.jpg)

If you have not already, insert a USB cable into your IoT RedBoard ESP32 and a TRS cable from your audio source (e.g. MP3 player, smartphone, or computer) into the audio connector. Then connect your headphones to the output. For those that are sensitive to sounds, you may want to hear the example output before inserting the headphones into your ears.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_05_Loopback](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_05_Loopback/Example_05_Loopback.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Monitor and set it to **115200** baud to view the serial output. Then hit the play button on your audio source. Make sure that the volume from the audio source is turned up. You should hear some music from the headphones.

## Example 6: 3D Enhance

In this example, we will pass a line level audio source into the WM8960\'s line input 1 port. The audio source will go through the mixers and gain stages into the ADC. With the loopback turned on, the ADC is sent directly to the DAC and output to the headphone output. In the `loop()` function, turn on and off the 3D enhance feature every 5 seconds.

### Hardware Hookup

Connect power, I^2^C, line input 1, and the headphone output as explained earlier. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In-1_Line_Out-bb1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In-1_Line_Out-bb1.jpg)

Connect a USB cable into your IoT RedBoard ESP32 and a TRS cable from your audio source (e.g. MP3 player, smartphone, or computer) into the audio connector. Then connect your headphones to the output. For those that are sensitive to sounds, you may want to hear the example output before inserting the headphones into your ears.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_06_3D_Enhance](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_06_3D_Enhance/Example_06_3D_Enhance.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Monitor and set it to **115200** baud to view the serial output when the 3D enhance mode is enabled. Then hit the play button on your audio source. Make sure that the volume from the audio source is turned up. Experience the virtual surround sound!

## Example 7: Microphone Bias

in this example, we will set the microphone bias voltage and measure the voltage. This is for advanced users looking to add a differential microphone to the microphone input pins.

### Hardware Hookup

Connect power and I^2^C. as explained earlier. Then grab a multimeter with alligator clips and M/M jumper wires. Connect the wires to MICBIAS and GND to measure the voltage. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Microphone-Bias-_-_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Microphone-Bias-_-_bb.jpg)

If you have not already, insert a USB cable into your IoT RedBoard ESP32.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_07_MicBias](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_07_MicBias/Example_07_MicBias.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Monitor and set it to **115200** baud to view the serial output. Measuring the output with a multimeter, the voltage should be similar to the voltages that were set for the MICBIAS pin. After 3 seconds, the pin will be disabled. If you missed the window to measure the MICBIAS voltage, hit the reset button the IoT RedBoard to run the example again.

If you are satisfied with your MICBIAS voltage, head over to example 14 to add a resistor in series with each electret microphone.

## Example 8: I2S Passthrough

In this example, we will pass a line level audio source into the WM8960\'s line input 1 port. The signal will go through the mixers and gain stages of the codec. The audio will be read from the ADC via I^2^S and then immediately sent back to the DAC via I^2^S. The output of the DAC will then be sent to the headphone output.

### Hardware Hookup

Connect power, I^2^C, line input 3, and the headphone output as explained earlier. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_I2S_Passthrough_Headphone_Out-bb3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_I2S_Passthrough_Headphone_Out-bb3.jpg)

Connect a USB cable into your IoT RedBoard ESP32 and a TRS cable from your audio source (e.g. MP3 player, smartphone, or computer) into the audio connector. Then connect your headphones to the output. For those that are sensitive to sounds, you may want to hear the example output before inserting the headphones into your ears.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_08_I2S_Passthrough](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_08_I2S_Passthrough/Example_08_I2S_Passthrough.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Monitor and set it to **115200** baud to view the serial output. Then hit the play button on your audio source. Make sure that the volume from the audio source is turned up. You should hear some music from the headphones.

## Example 9: I2S Bluetooth

In this example, we will wirelessly connect a Bluetooth audio source and use the IoT RedBoard ESP32 as a Bluetooth audio sink. Once the audio codec is set as an I^2^S peripherial, the ESP32 will receive audio and play it back via I^2^S. Once the WM8960 receives the I^2^S audio, it will be sent to the DAC and then the headphone output.

### Hardware Hookup

**Note:** For users using the [SparkFun Qwiic Wireless Speaker Kit](https://www.sparkfun.com/products/21773), the kit includes a TRRS breakout with headers instead of the TRS breakout. RING2 of the TRRS connector also connects to the TRS cable\'s sleeve. When wiring your circuit up for this example, we recommend connecting to the sleeve in case you have a headphone with a TRRS connector.\
\

[![SparkFun Qwiic Wireless Speaker Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/5/7/9/21773-_KIT-_1.jpg)](https://www.sparkfun.com/sparkfun-qwiic-wireless-speaker-kit.html)

### [SparkFun Qwiic Wireless Speaker Kit](https://www.sparkfun.com/sparkfun-qwiic-wireless-speaker-kit.html) 

[ KIT-21773 ]

The SparkFun Qwiic Wireless Speaker Kit provides you with everything you need to make a wireless audio speaker.

**Retired**

Connect power, I^2^C, I^2^S, and the headphone output as explained earlier. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_I2S_Decoder_Headphone_Out-bb1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_I2S_Decoder_Headphone_Out-bb1.jpg)

Connect a USB cable into your IoT RedBoard ESP32. Turn on the Bluetooth on your audio source (e.g. MP3 player, smartphone, or computer). Then connect your headphones to the output. For those that are sensitive to sounds, you may want to hear the example output before inserting the headphones into your ears.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_09_I2S_Bluetooth](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_09_I2S_Bluetooth/Example_09_I2S_Bluetooth.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Monitor and set it to **1152000** baud to view the serial output. On your phone, pair and connect to the ESP32\'s Bluetooth. In this case, the name of the ESP32\'s Bluetooth is called \"**myCodec**\". Then hit the play button on your audio source. Make sure that the volume from the audio source is turned up. You should hear some music from the headphones.

Try adding a battery to the mix to untether the circuit from your computer. Do a little dance or flip and rock to the beat of the music! Of course, you\'ll want to be careful of the wires while moving around. For a more secure connection, you could take a solderable breadboard or an Arduino shield and manually wire the circuit together

## Example 10: ADC Gain

This example is pretty much example 5. The difference is that we are adding a trim pot to the ESP32\'s analog input and using the measurement to adjust the codec\'s ADC digital volume.

### Hardware Hookup.

Connect power, I^2^C, line input 1, trim pot, and the headphone output. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_Line_Out_Digital_Volume_bb3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_Line_Out_Digital_Volume_bb3.jpg)

If you have not already, insert a USB cable into your IoT RedBoard ESP32 and a TRS cable from your audio source (e.g. MP3 player, smartphone, or computer) into the audio connector. Then connect your headphones to the output. For those that are sensitive to sounds, you may want to hear the example output before inserting the headphones into your ears.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_10_AdcGain](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_10_AdcGain/Example_10_AdcGain.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Monitor and set it to **115200** baud to view the serial output. Then hit the play button on your audio source. Make sure that the volume from the audio source is turned up. You should hear some music from the headphones. Adjust the volume to your desired setting by rotating the trim pot clockwise or counterclockwise.

## Example 11: Volume Plotter

This example is similar to example 3. However, we will be connecting to reading I2S audio from the ADC and plotting the audio samples on the Arduino Serial Plotter.

### Hardware Hookup

Connect power, I^2^C, I^2^S, line input 1, and the headphone output. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_I2S_Input_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_I2S_Input_bb.jpg)

If you have not already, insert a USB cable into your IoT RedBoard ESP32 and a TRS cable from your audio source (e.g. MP3 player, smartphone, or computer) into the audio connector. Then connect your headphones to the output. For those that are sensitive to sounds, you may want to hear the example output before inserting the headphones into your ears.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_11_VolumePlotter](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_11_VolumePlotter/Example_11_VolumePlotter.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Plotter and set it to **115200** baud to view the output. Then hit the play button on your audio source. Make sure that the volume from the audio source is turned up. You should hear some music from the headphones and view the audio samples on the Serial Plotter.

## Example 12: Automatic Level Control

This example builds off of example 5. The difference is that we are adding a trim pot toe the ESP32\'s analog input and using the measurement to configures the Automatic Level Control (ALC) target value. The ALC will adjust the gain of the PGA input buffer to try and keep the signal level at the target.

### Hardware Hookup

Connect power, I^2^C, line input 1, trim pot, and the headphone output as explained earlier. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_Line_Out_Digital_Volume_bb3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_Line_Out_Digital_Volume_bb3.jpg)

If you have not already, insert a USB cable into your IoT RedBoard ESP32 and a TRS cable from your audio source (e.g. MP3 player, smartphone, or computer) into the audio connector. Then connect your headphones to the output. For those that are sensitive to sounds, you may want to hear the example output before inserting the headphones into your ears.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_12_AutomaticLevelControl](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_12_AutomaticLevelControl/Example_12_AutomaticLevelControl.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Monitor and set it to **115200** baud to view the serial output. Then hit the play button on your audio source. Make sure that the volume from the audio source is turned up. You should hear some music from the headphones.

## Example 13: DAC Gain

This example is similar to example 10. The difference is that we are adding a trim pot to the ESP32\'s analog input and using the measurement to adjust the codec\'s DAC digital volume.

### Hardware Hookup

Connect power, I^2^C, I^2^S, line input 1, trim pot, and the headphone output. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_Line_Out_Digital_Volume_bb3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Line_In_Line_Out_Digital_Volume_bb3.jpg)

If you have not already, insert a USB cable into your IoT RedBoard ESP32 and a TRS cable from your audio source (e.g. MP3 player, smartphone, or computer) into the audio connector. Then connect your headphones to the output. For those that are sensitive to sounds, you may want to hear the example output before inserting the headphones into your ears.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_13_DacGain](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_13_DacGain/Example_13_DacGain.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Monitor and set it to **115200** baud to view the serial output. Then hit the play button on your audio source. Make sure that the volume from the audio source is turned up. You should hear some music from the headphones. Adjust the volume to your desired setting by rotating the trim pot clockwise or counterclockwise.

## Example 14: Electret Mic

Continuing on from example 7, we will use differential microphones as the audio input based on the \"pseudo-differential MIC configuration.\" The example will configure the PGA before passing it to the mixers and gain stages of the codec like the previous examples. The output will be to the headphones.

### Hardware Hookup

Connect power, I^2^C, I^2^S, differential microphones (each with a 2.2kΩ resistor wired in series with the MICBIAS pin), and the headphone output. Your circuit should look similar to the circuit diagram below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Microphone-Bias-Eletret_bb1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/1/SparkFun_IoT_RedBoard_ESP32_Audio_Codec_WM8960_Qwiic_Fritzing_Arduino_Microphone-Bias-Eletret_bb1.jpg)

If you have not already, insert a USB cable into your IoT RedBoard ESP32. Then connect your headphones to the output. For those that are sensitive to sounds, you may want to hear the example output before inserting the headphones into your ears.

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun WM8960 Arduino Library** \> **[Example_14_Electret_Mics](https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library/blob/main/examples/Example_14_ElectretMics/Example_14_ElectretMics.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

Open the Arduino Serial Monitor and set it to **115200** baud to view the serial output. Make some noise on the differential microphones. You should hear some audio from the headphones.

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[SparkFun Forums](https://forum.sparkfun.com/)