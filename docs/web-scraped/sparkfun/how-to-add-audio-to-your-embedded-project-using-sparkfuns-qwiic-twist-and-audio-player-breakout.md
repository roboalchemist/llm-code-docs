# Source: https://learn.sparkfun.com/tutorials/how-to-add-audio-to-your-embedded-project-using-sparkfuns-qwiic-twist-and-audio-player-breakout

## Introduction

Looking to bring sound into your next embedded project? In this tutorial, we\'ll walk you through using the SparkFun Audio Player Breakout in combination with the Qwiic Twist to let you select and play tracks from a microSD card. It\'s a compact and powerful way to add audio interactivity to your prototype using simple I2C and serial connections.

Follow along on video here, or find the full tutorial below.\

\

## Hardware

To follow this experiment, you will need the following materials. While this is a simple project, we wanted to make sure that you have everything you need to get started before we get to the code.

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Flexible Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/4/6/17259-Flexible_Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-100mm.html)

### [Flexible Qwiic Cable - 100mm](https://www.sparkfun.com/flexible-qwiic-cable-100mm.html) 

[ PRT-17259 ]

This polarized I2C cable insulation is made from silicon making it more flexible than our original Qwiic cable particularly i...

[ [\$1.95] ]

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![Jumper Wires - Connected 6\" (M/M, 20 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/6/1/3/12795-00.jpg)](https://www.sparkfun.com/jumper-wires-connected-6-m-m-20-pack.html)

### [Jumper Wires - Connected 6\" (M/M, 20 pack)](https://www.sparkfun.com/jumper-wires-connected-6-m-m-20-pack.html) 

[ PRT-12795 ]

These are 6\" long jumper wires with male connectors on both ends. Use these to jumper from any female header on any board, to...

[ [\$2.95] ]

[![SparkFun Qwiic Twist - RGB Rotary Encoder Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/3/15083-SparkFun_Qwiic_Twist_-_RGB_Rotary_Encoder_Breakout-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-twist-rgb-rotary-encoder-breakout.html)

### [SparkFun Qwiic Twist - RGB Rotary Encoder Breakout](https://www.sparkfun.com/sparkfun-qwiic-twist-rgb-rotary-encoder-breakout.html) 

[ DEV-15083 ]

The SparkFun Qwiic Twist is a digital RGB rotary encoder breakout that is also able to connect to our Qwiic Connect System.

[ [\$25.50] ]

[![Thin Speaker - 0.5W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/8/15350-Feature.jpg)](https://www.sparkfun.com/thin-speaker-0-5w.html)

### [Thin Speaker - 0.5W](https://www.sparkfun.com/thin-speaker-0-5w.html) 

[ COM-15350 ]

This 0.5W, 8Ohm speaker is only 40mm in diameter and just over 4mm thick, the same kind you might find in one of those \"talki...

[ [\$1.50] ]

[![SparkFun Mono Audio Amp Breakout - TPA2005D1](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/0/0/11044-01a.jpg)](https://www.sparkfun.com/sparkfun-mono-audio-amp-breakout-tpa2005d1.html)

### [SparkFun Mono Audio Amp Breakout - TPA2005D1](https://www.sparkfun.com/sparkfun-mono-audio-amp-breakout-tpa2005d1.html) 

[ BOB-11044 ]

This tiny audio amplifier is based on the Texas Instruments TPA2005D1. Its efficient class-D operation means low heat and lon...

[ [\$10.50] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![SparkFun Audio Player Breakout - MY1690X-16S](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/6/1/6/28038-Audio-Player-Breakout-Feature.jpg)](https://www.sparkfun.com/sparkfun-audio-player-breakout-my1690x-16s.html)

### [SparkFun Audio Player Breakout - MY1690X-16S](https://www.sparkfun.com/sparkfun-audio-player-breakout-my1690x-16s.html) 

[ BOB-28038 ]

The SparkFun M71690X-16S Audio Player Breakout is a compact serial-controlled audio player designed around the MY1690X-16S de...

[ [\$14.95] ]

[![USB-A to USB-C Cable - 1m, USB 2.0 (Flexible Silicone)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/1/8/5/CAB-25630-USB-to-USB-C-1mm-Feature.jpg)](https://www.sparkfun.com/usb-a-to-usb-c-cable-1m-usb-2-0-flexible-silicone.html)

### [USB-A to USB-C Cable - 1m, USB 2.0 (Flexible Silicone)](https://www.sparkfun.com/usb-a-to-usb-c-cable-1m-usb-2-0-flexible-silicone.html) 

[ CAB-25630 ]

This is a flexible USB-A to USB-C cable.

[ [\$10.95] ]

[![microSD Card - 1GB (Class 4)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/7/0/15107-microSD_Card_-_1GB__Class_4_-01.jpg)](https://www.sparkfun.com/microsd-card-1gb-class-4.html)

### [microSD Card - 1GB (Class 4)](https://www.sparkfun.com/microsd-card-1gb-class-4.html) 

[ COM-15107 ]

For the times when all you need is a basic SD card this is the card for you. 1GB capacity is plenty to store MP3s or log envi...

[ [\$5.50] ]

## Wiring

\

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/7/1/image2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/7/1/image2.jpg)

\

Qwiic Twist connected to RedBoard Qwiic via Qwiic cable Audio Player Breakout:

- `TXO` → RedBoard `D8`
- `RXI` → RedBoard `D9`
- `VIN` → RedBoard `5V`
- `GND` → RedBoard `GND`

Audio Out → Mono Audio Amp → Speaker Mono Audio Amp

- `PWR -` → `GND`
- `PWR +` → `5V`

## Software Setup

To follow along, install the following libraries via the Arduino Library Manager:

- [SparkFun MY1690 MP3 Decoder Arduino Library](https://github.com/sparkfun/SparkFun_MY1690_MP3_Decoder_Arduino_Library)
- [SparkFun Qwiic Twist Arduino Library](https://github.com/sparkfun/SparkFun_Qwiic_Twist_Arduino_Library)

\

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/7/1/image1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/7/1/image1.png)

\

Use Example4_QwiicTwist.ino from the SparkFun MY1690 MP3 Decoder Library examples. It enables the Qwiic Twist to:

- Rotate to change track number
- Press to play the selected track
- Display info via serial monitor

How It Works:

- The Audio Player Breakout receives serial messages from the RedBoard Qwiic.
- The Qwiic Twist allows you to navigate through tracks by rotating and play one by pressing.
- The selected audio file is played through the MY1690 and sent to the mono amp and speaker.

Serial Feedback: The sketch prints useful debug messages to the Serial Monitor, including the number of tracks on your SD card and the currently selected track.

Tips:

- Make sure your microSD card is formatted correctly and contains MP3/WAV files.
- Use a single-cell LiPo if you\'d like to run this portable.
- You can customize the playback behavior by editing the example sketch.