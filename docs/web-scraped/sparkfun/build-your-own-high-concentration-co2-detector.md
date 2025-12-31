# Source: https://learn.sparkfun.com/tutorials/build-your-own-high-concentration-co2-detector

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Build Your Own High-Concentration CO2 Detector

# Build Your Own High-Concentration CO2 Detector

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/c79948e7cb0fb6cc0dbfaa77301914ce?d=retro&s=20&r=pg) Christo-boots with the-pher], [![](https://cdn.sparkfun.com/avatar/5c320824995fcd6990beaf7a3d3f6037?d=retro&s=20&r=pg) Elias The Sparkiest]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft3969&name=Build+Your+Own+High-Concentration+CO2+Detector "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft3969 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Build+Your+Own+High-Concentration+CO2+Detector&url=http%3A%2F%2Fsfe.io%2Ft3969&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft3969&t=Build+Your+Own+High-Concentration+CO2+Detector "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft3969&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F9%2F6%2F9%2FCo2SensingCarThumb.png&description=Build+Your+Own+High-Concentration+CO2+Detector "Pin It")

## Introduction

The [SparkFun CO~2~ Sensor - STC31](https://www.sparkfun.com/sparkfun-co2-sensor-stc31-qwiic.html) is a Qwiic breakout featuring the STC31 CO~2~ sensor and the SHTC3 Temperature and Humidity sensor from Sensirion, which accurately measures CO~2~ concentrations up to 100% with high repeatability and long-term stability, thanks to humidity and temperature compensation provided by the built-in SHTC3.

[![SparkFun CO2 Sensor - STC31 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/3/1/1/0/7/29260-CO2-Sensor-STC31-Feature-Corrected.jpg)](https://www.sparkfun.com/sparkfun-co2-sensor-stc31-qwiic.html)

### [SparkFun CO2 Sensor - STC31 (Qwiic)](https://www.sparkfun.com/sparkfun-co2-sensor-stc31-qwiic.html) 

[ SEN-29260 ]

The SparkFun STC31 is a high-precision, Qwiic-enabled sensor that accurately measures extreme CO₂ concentrations up to 100%...

[ [\$124.95] ]

The STC3x sensor family is Sensirion's series of Gas Concentration sensors designed for high-volume applications. The STC3x utilizes a revolutionized thermal conductivity measurement principle, which results in superior repeatability and long-term stability. This makes the STC31 an ideal choice for applications where reliability is crucial. The outstanding performance of these sensors is based on Sensirion's patented CMOSens® sensor technology, which combines the sensor element, signal processing, and digital calibration on a small CMOS chip. The well-proven CMOS technology is ideally suited for high-quality mass production and is the ideal choice for demanding and cost-sensitive OEM applications.

This tutorial covers how to get CO~2~ and other environmental readings from the STC31 using both Arduino and MicroPython when connecting the CO~2~ Sensor Breakout to a compatible development board over Qwiic. To follow along with this guide, you\'ll need the CO~2~ Sensor - STC31 along with the following materials:

- [SparkFun IoT RedBoard - ESP32 MicroPython Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-micropython-development-board.html) (or other Arduino/MicroPython development board like the [ESP32-S2 WROOM Thing+](https://www.sparkfun.com/sparkfun-thing-plus-esp32-s2-wroom.html) we use in the video)
- [Qwiic Cable](https://www.sparkfun.com/qwiic-cable-100mm.html)
- [USB-C Cable](https://www.sparkfun.com/usb-a-to-usb-c-cable-1m-usb-2-0-flexible-silicone.html)

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![SparkFun Thing Plus - ESP32-S2 WROOM](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/6/2/17743-SparkFun_Thing_Plus_-_ESP32-S2_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-s2-wroom.html)

### [SparkFun Thing Plus - ESP32-S2 WROOM](https://www.sparkfun.com/sparkfun-thing-plus-esp32-s2-wroom.html) 

[ WRL-17743 ]

The SparkFun ESP32-S2 WROOM Thing Plus is a highly-integrated, Feather form-factor development board equipped with the 2.4 GH...

[ [\$24.50] ]

[![SparkFun IoT RedBoard - ESP32 MicroPython Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/3/0/2/5/7/28434-Redboard-Iot-ESP32-Micropython-Feature.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-micropython-development-board.html)

### [SparkFun IoT RedBoard - ESP32 MicroPython Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-micropython-development-board.html) 

[ WRL-28434 ]

The IoT RedBoard is an ESP32 WROOM-equipped development board with everything you need in an Arduino Uno with extra perks lik...

[ [\$29.95] ]

[![USB-A to USB-C Cable - 1m, USB 2.0 (Flexible Silicone)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/1/8/5/CAB-25630-USB-to-USB-C-1mm-Feature.jpg)](https://www.sparkfun.com/usb-a-to-usb-c-cable-1m-usb-2-0-flexible-silicone.html)

### [USB-A to USB-C Cable - 1m, USB 2.0 (Flexible Silicone)](https://www.sparkfun.com/usb-a-to-usb-c-cable-1m-usb-2-0-flexible-silicone.html) 

[ CAB-25630 ]

This is a flexible USB-A to USB-C cable.

[ [\$10.95] ]

If you prefer a soldered connection, you may need one or more of these materials along with a [soldering iron](https://www.sparkfun.com/tools/soldering/soldering-irons-and-tips.html) and [solder](https://www.sparkfun.com/tools/soldering/solder.html):

- [Breakaway Headers Straight](https://www.sparkfun.com/break-away-headers-straight.html)
- [Jumper Wires - Connected 6\" (M/M, 20 pack)](https://www.sparkfun.com/jumper-wires-connected-6-m-m-20-pack.html)
- [Breadboard](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

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

[![Jumper Wires Premium 6\" M/M Pack of 100](https://cdn.sparkfun.com/r/140-140/assets/parts/5/9/8/2/10897-01.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-100.html)

### [Jumper Wires Premium 6\" M/M Pack of 100](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-100.html) 

[ PRT-10897 ]

These are 26 AWG jumper wires terminated as male to male. Use these to jumper from any female header on any board, to any oth...

[ [\$27.50] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Hakko FX-888DX Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/6/4/6/TOL-25926-Hakko-FX-888DX-Soldering-Station-feature.jpg)](https://www.sparkfun.com/hakko-fx-888dx-soldering-station.html)

### [Hakko FX-888DX Soldering Station](https://www.sparkfun.com/hakko-fx-888dx-soldering-station.html) 

[ TOL-25926 ]

The HAKKO FX-888DX Digital Soldering Station improves the user interface from the FX-888D using a more intuitive method for a...

[ [\$129.95] ]

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Straight Header - Female (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/00115-03-L.jpg)](https://www.sparkfun.com/female-headers.html)

### [Straight Header - Female (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/female-headers.html) 

[ PRT-00115 ]

Single row of 40-holes, female header. Can be cut to size with a pair of wire-cutters. Standard .1\" spacing. We use them exte...

[ [\$1.95] ]

[![Solder - 1/4lb Spool (0.032\") Special Blend](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/9/3/10243-Solder_-_1_4lb_Spool__0.032___Special_Blend-01.jpg)](https://www.sparkfun.com/solder-1-4lb-spool-0-032-special-blend.html)

### [Solder - 1/4lb Spool (0.032\") Special Blend](https://www.sparkfun.com/solder-1-4lb-spool-0-032-special-blend.html) 

[ TOL-10243 ]

We don\'t want to hype this solder TOO much, but this could possibly be the best solder in the world. There, we\'ve said it. Th...

[ [\$28.50] ]

### Topics Covered

This document contains two main sections: **Quickstart Guide** and **Project Setup**.

The Quickstart Guide assumes a working knowledge of how to use a development board and the required software to program them for your project\'s needs. It covers a quick assembly and then jumps right into getting the necessary software packages installed to start getting spectral data in just a few short minutes.

The Project Setup pages are split into sections covering the SparkFun STC31 Arduino Library and STCx Python driver. Each software page gives instructions on how to download install the software package (Arduino library or Python driver), as well as detailed looks at the examples included in the software packages.

If you are looking for the [full Hookup Guide](https://docs.sparkfun.com/SparkFun_CO2_Sensor-STC31) for the SparkFun CO~2~ Sensor - STC31, click the button bellow. This basic tutorial only covers the project that get this CO~2~ sensor up and running as fast as possible thanks to our Qwiic connect system.

[View the Full Hookup Guide](https://docs.sparkfun.com/SparkFun_CO2_Sensor-STC31)

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft3969&name=Build+Your+Own+High-Concentration+CO2+Detector "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft3969 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Build+Your+Own+High-Concentration+CO2+Detector&url=http%3A%2F%2Fsfe.io%2Ft3969&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft3969&t=Build+Your+Own+High-Concentration+CO2+Detector "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft3969&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F9%2F6%2F9%2FCo2SensingCarThumb.png&description=Build+Your+Own+High-Concentration+CO2+Detector "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/build-your-own-high-concentration-co2-detector/all) [Next Page →\
[Quickstart Guide]](https://learn.sparkfun.com/tutorials/build-your-own-high-concentration-co2-detector/quickstart-guide)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/build-your-own-high-concentration-co2-detector/introduction) [Quickstart Guide](https://learn.sparkfun.com/tutorials/build-your-own-high-concentration-co2-detector/quickstart-guide) [Project Setup - STC3x Arduino Library](https://learn.sparkfun.com/tutorials/build-your-own-high-concentration-co2-detector/project-setup---stc3x-arduino-library) [Project Setup - STC3x Python Package](https://learn.sparkfun.com/tutorials/build-your-own-high-concentration-co2-detector/project-setup---stc3x-python-package) [Troubleshooting Tips](https://learn.sparkfun.com/tutorials/build-your-own-high-concentration-co2-detector/troubleshooting-tips)

[Comments [0]](https://learn.sparkfun.com/tutorials/build-your-own-high-concentration-co2-detector/discuss) [Single Page](https://learn.sparkfun.com/tutorials/build-your-own-high-concentration-co2-detector/all) [Print]

- **Tags**
- - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]