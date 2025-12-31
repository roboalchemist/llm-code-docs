# Source: https://learn.sparkfun.com/tutorials/gnss-correction-data-receiver-neo-d9s-hookup-guide

## Introduction

**Please note:** The u-blox Thingstream PointPerfect Correction Service is only available to \"B2B Customers\" (Business To Business Customers). Please check the [Service Terms](https://cdn.sparkfun.com/assets/2/5/a/4/f/Service_Terms.pdf) before purchasing hardware.\
\

[u-blox Service Terms](https://cdn.sparkfun.com/assets/2/5/a/4/f/Service_Terms.pdf)

The [SparkFun GNSS Correction Data Receiver - NEO-D9S](https://www.sparkfun.com/products/19390) is a satellite data receiver for L-band correction broadcast. It can be configured for use with a variety of correction services including u-blox\'s PointPerfect satellite GNSS augmentation service, which provides homogenous coverage in contiguous USA. With a clear view of the sky, especially a clear view to the South, it decodes the satellite transmission and outputs a correction stream, enabling a multi-band high precision GNSS receiver (such as the u-blox ZED-F9P) to reach accuracies down to centimeter-level positioning without needing a separate RTK or NTRIP correction!

[![SparkFun GNSS Correction Data Receiver - NEO-D9S (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/0/2/8/19390-NEO-D9S_Breakout-_01.jpg)](https://www.sparkfun.com/sparkfun-gnss-correction-data-receiver-neo-d9s-qwiic.html)

### [SparkFun GNSS Correction Data Receiver - NEO-D9S (Qwiic)](https://www.sparkfun.com/sparkfun-gnss-correction-data-receiver-neo-d9s-qwiic.html) 

[ GPS-19390 ]

The SparkFun NEO-D9S GNSS Correction Data Receiver is a satellite data receiver for L-Band correction broadcast.

[ [\$59.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Arduino Microcontroller

We recommend an Arduino microcontroller with the ability to connect to WiFi. This is useful for those users taking advantage of both the ThingStream PointPerfect Location-as-a-Service over L-Band Satellite and Internet Protocol (IP). The following boards with the ESP32 WROOM module can work.

[![SparkFun Thing Plus - ESP32 WROOM (USB-C)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/9/6/8/20168Diagonal.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html)

### [SparkFun Thing Plus - ESP32 WROOM (USB-C)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html) 

[ WRL-20168 ]

The USB-C variant of ESP32 Thing Plus is a development board with WiFi, SPP, BLE, Qwiic connector, 21 I/O pins, RGB status LE...

[ [\$33.73] ]

[![SparkFun IoT RedBoard - ESP32 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/8/0/0/ESP32_03.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html)

### [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html) 

[ WRL-19177 ]

The IoT RedBoard is an ESP32 WROOM-equipped development board that has everything you need in an Arduino Uno with extra perks...

[ [\$41.87] ]

### High Precision GNSS (HPG) Module

Along with the NEO-D9S, you will need a high precision GNSS (HPG) module from u-blox. As of the writing of his tutorial, the GNSS correction data receiver works for the ZED-F9P module. You will need to make sure that it has the latest firmware when using the modules together.

[![SparkFun GPS-RTK-SMA Breakout - ZED-F9P (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/3/5/2/16481-SparkFun_GPS-RTK-SMA_Breakout_-_ZED-F9P__Qwiic_-01a.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk-sma-breakout-zed-f9p-qwiic.html)

### [SparkFun GPS-RTK-SMA Breakout - ZED-F9P (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk-sma-breakout-zed-f9p-qwiic.html) 

[ GPS-16481 ]

The SparkFun GPS-RTK-SMA raises the bar for high-precision GPS and is the latest in a line of powerful RTK boards featuring t...

[ [\$259.95] ]

[![SparkFun GPS-RTK2 Board - ZED-F9P (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/5/1/4/15136-SparkFun_GPS-RTK2_Board_-_ZED-F9P__Qwiic_-03.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk2-board-zed-f9p-qwiic-gps-15136.html)

### [SparkFun GPS-RTK2 Board - ZED-F9P (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk2-board-zed-f9p-qwiic-gps-15136.html) 

[ GPS-15136 ]

The SparkFun GPS-RTK2 is a powerful breakout for the ZED-F9P module. The ZED-F9P is a top-of-the-line module for GNSS & GPS s...

[ [\$259.95] ]

### Antennae and Cables

**Note:** We found that the GNSS Multi-Band L1/L2 Surveying Antenna (TNC) - TOP106 worked for the NEO-D9S L-Band antenna. For users that want a specific active L-Band antenna, you could look at the following antenna listed below.\
\

- [RTL-SDR\'s Active L-Band (1525MHz to 1637MHz) Inmarsat, Iridium and GPS Patch Antenna Set](https://www.rtl-sdr.com/product/rtl-sdr-blog-l-band-1525-1637-inmarsat-to-iridium-patch-antenna-set/)

For the ZED-F9P, you will need a multi-band antenna to take advantage of the L1 and L2 bands. For the NEO-D9S, you will need a L-band antenna. While the GNSS Multi-band L1/L2 Surveying Antenna (TNC) TOP106 was designed for L1 and L2, we found that it was able to pick up the correction data tuned to a frequency within the L-band (1556.29MHz in the US). Make sure to also pick up the TNC to SMA male interface cable and if necessary, an additional SMA extension cable or u.FL to SMA interface cable for the ZED-F9P breakout boards populated with the u.FL connector.

[![GNSS Multi-Band L1/L2 Surveying Antenna - TNC (TOP106)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/7/4/17587-L1_L2_GNSS_antenna_TOP106-09-1.png)](https://www.sparkfun.com/gnss-multi-band-l1-l2-surveying-antenna-tnc-top106.html)

### [GNSS Multi-Band L1/L2 Surveying Antenna - TNC (TOP106)](https://www.sparkfun.com/gnss-multi-band-l1-l2-surveying-antenna-tnc-top106.html) 

[ GPS-17751 ]

The TOP106 from TOPGNSS is a certified GNSS/GPS surveying antenna capable of receiving the L1/L2 bands for GPS, GLONASS, Gali...

[ [\$199.95] ]

[![Reinforced Interface Cable - SMA Male to TNC Male (10m)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/5/7/0/SparkFun_Reinforced_Interface_Cable_-_SMA_Male_to_TNC_Male_-_1.jpg)](https://www.sparkfun.com/reinforced-interface-cable-sma-male-to-tnc-male-10m.html)

### [Reinforced Interface Cable - SMA Male to TNC Male (10m)](https://www.sparkfun.com/reinforced-interface-cable-sma-male-to-tnc-male-10m.html) 

[ CAB-21740 ]

This is a 10 meter (33 ft) long Male TNC to Male SMA cable with injection molded stress-relief boots.

[ [\$42.95] ]

[![Interface Cable - SMA Female to SMA Male (25cm)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/2/9/12861-01.jpg)](https://www.sparkfun.com/interface-cable-sma-female-to-sma-male-25cm.html)

### [Interface Cable - SMA Female to SMA Male (25cm)](https://www.sparkfun.com/interface-cable-sma-female-to-sma-male-25cm.html) 

[ WRL-12861 ]

This is a basic SMA (Sub-Miniature A) male to female connector cable. Each cable is 25cm (9.8\") long and has a 50Ω impedance...

[ [\$5.50] ]

[![Interface Cable U.FL to SMA - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/7/9/18154-Interface_Cable_U.FL_to_SMA-03.jpg)](https://www.sparkfun.com/interface-cable-u-fl-to-sma-100mm.html)

### [Interface Cable U.FL to SMA - 100mm](https://www.sparkfun.com/interface-cable-u-fl-to-sma-100mm.html) 

[ WRL-18154 ]

A U.FL to SMA (jack) bulkhead straight connector with a 1.32 mm diameter cable.

**Retired**

You could also use the u-blox or MagmaX2 multi-band antenna for the ZED-F9P and NEO-D9S in the US. However, you would also need the ground plate. Again, while they were designed for L1 and L2, we found that it was also able to pick up the correction data tuned to a frequency within the L-band within the US. You may also need an additional u.FL to SMA interface cable for ZED-F9P breakout boards populated with the u.FL connector.

[![GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/1/1/15192-GNSS_Multi-band_Magnetic_Mount_Antenna_SMA_-_5m-01.jpg)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html)

### [GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html) 

[ GPS-15192 ]

The ANN-MB-00 GNSS multi-band antenna is extremely unique from other GNSS/GPS antennas in that it is designed to receive both...

[ [\$109.95] ]

[![GPS Antenna Ground Plate](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/5/9/3/17519-GPS_Antenna_Ground_Plate-01.jpg)](https://www.sparkfun.com/gps-antenna-ground-plate.html)

### [GPS Antenna Ground Plate](https://www.sparkfun.com/gps-antenna-ground-plate.html) 

[ GPS-17519 ]

Using this simple steel plate effectively improves simple patch antenna performance to near professional level antenna setups...

[ [\$7.25] ]

[![MagmaX2 Active Multiband GNSS Magnetic Mount Antenna - AA.200](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/0/7/0/17108-AA.200_____MagmaX2_Active_Multiband_GNSS_Magnetic_Mount_Antenna-01A.jpg)](https://www.sparkfun.com/magmax2-active-multiband-gnss-magnetic-mount-antenna-aa-200.html)

### [MagmaX2 Active Multiband GNSS Magnetic Mount Antenna - AA.200](https://www.sparkfun.com/magmax2-active-multiband-gnss-magnetic-mount-antenna-aa-200.html) 

[ GPS-17108 ]

The AA.200 antenna is an active multiband GNSS magnetic mount antenna that exhibits excellent gain and good radiation pattern...

**Retired**

[![Interface Cable U.FL to SMA - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/7/9/18154-Interface_Cable_U.FL_to_SMA-03.jpg)](https://www.sparkfun.com/interface-cable-u-fl-to-sma-100mm.html)

### [Interface Cable U.FL to SMA - 100mm](https://www.sparkfun.com/interface-cable-u-fl-to-sma-100mm.html) 

[ WRL-18154 ]

A U.FL to SMA (jack) bulkhead straight connector with a 1.32 mm diameter cable.

**Retired**

**Note:** While we were able to get the [GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA), ANN-MB-00](https://www.sparkfun.com/products/15192) to work with the NEO-D9S in the US, we recommend using a dedicated L1/L2/L-Band antenna for best results.

### Qwiic Cables

For those that want to take advantage of the Qwiic enabled devices, you\'ll want to grab a Qwiic cable between each board.

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

### LiPo Battery

A [single-cell Lithium-ion battery](https://www.sparkfun.com/categories/tags/lithium-polymer) can be connected to the ESP32 IoT RedBoard\'s JST connector. In turn, this will power the NEO-D9S and ZED-F9P for portability.

[![Lithium Ion Battery - 850mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/1/13854-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-850mah.html)

### [Lithium Ion Battery - 850mAh](https://www.sparkfun.com/lithium-ion-battery-850mah.html) 

[ PRT-13854 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 850...

[ [\$13.61] ]

[![Lithium Ion Battery - 2Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/2/13855-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-2ah.html)

### [Lithium Ion Battery - 2Ah](https://www.sparkfun.com/lithium-ion-battery-2ah.html) 

[ PRT-13855 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 200...

[ [\$19.41] ]

[![Lithium Ion Battery - 6Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/3/13856-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-6ah.html)

### [Lithium Ion Battery - 6Ah](https://www.sparkfun.com/lithium-ion-battery-6ah.html) 

[ PRT-13856 ]

If you need some juice, this 6Ah Lithium Ion Battery is for you. These are very compact batteries based on Lithium Ion chemis...

[ [\$48.44] ]

[![Lithium Ion Battery - 1Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/0/1/13813-01.jpg)](https://www.sparkfun.com/products/13813)

### [Lithium Ion Battery - 1Ah](https://www.sparkfun.com/products/13813) 

[ PRT-13813 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1000 mAh!

**Retired**

### Tools

Depending on your setup, you may need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49) for a secure connection when using the plated through holes.

[![PINECIL Soldering Iron Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/3/8/5/KIT-24063-PINECIL-Soldering-Iron-Kit-Feature.jpg)](https://www.sparkfun.com/pinecil-soldering-iron-kit.html)

### [PINECIL Soldering Iron Kit](https://www.sparkfun.com/pinecil-soldering-iron-kit.html) 

[ KIT-24063 ]

The PINECIL Soldering Iron Kit provides a compact powerhouse and everything you need to ignite your DIY dream.

[ [\$119.95] ]

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

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/2/2/0/2/TOL-22265-Beginner-Tool-Kit-Feature.jpg)](https://www.sparkfun.com/sparkfun-beginner-tool-kit-tol-22265.html)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/sparkfun-beginner-tool-kit-tol-22265.html) 

[ TOL-22265 ]

This assortment of tools is great for those who need a solid set of tools to start your workbench on the right foot!

**Retired**

#### Prototyping Accessories

Depending on your setup, you may want to use IC hooks for a temporary connection. However, you will want to solder header pins to connect devices to the plated through holes for a secure connection.

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

[![Jumper - 2 Pin](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/0/7/09044-02-L.jpg)](https://www.sparkfun.com/jumper-2-pin.html)

### [Jumper - 2 Pin](https://www.sparkfun.com/jumper-2-pin.html) 

[ PRT-09044 ]

These are two pin jumpers (also called shunts) that will create an electrical connection between two pin headers. Commonly us...

[ [\$0.50] ]

### You Will Also Need

**Please note:** The u-blox Thingstream PointPerfect Correction Service is only available to \"B2B Customers\" (Business To Business Customers). Please check the [Service Terms](https://cdn.sparkfun.com/assets/2/5/a/4/f/Service_Terms.pdf) before purchasing hardware.\
\

[u-blox Service Terms](https://cdn.sparkfun.com/assets/2/5/a/4/f/Service_Terms.pdf)

You will need access to dynamic keys to decrypt the correct data sent from an L-band satellite. Users will need to purchase a pricing plan with the ThingStream PointPerfect Location-as-a-Service over L-Band Satellite. You can also purchase a pricing plan that includes the L-Band and Internet Protocol (IP).

[u-blox Thingstream IoT Location-as-a-Service: PointPerfect Pricing Options](https://portal.thingstream.io/pricing)

**From March 10th 2025, the u-blox PointPerfect service will only offered for the USA\'s contiguous 48 states and up to 12 nautical miles (roughly 22 kilometers) off coastlines. The EU L-Band service is being suspended on that date.** Please see u-blox website for [additional information](https://developer.thingstream.io/guides/location-services/pointperfect-service-description#h.jv0o1vz2wkn3). Make sure to check back on the u-blox\'s website to see if there is additional coverage in your region.

[![L-Band Coverage](https://www.sparkfun.com/media/.renditions/wysiwyg/Additional-Product-Page-Images/PNT/PointPerfect_Coverage-2025-Cropped-Small.png)](https://www.sparkfun.com/media/.renditions/wysiwyg/Additional-Product-Page-Images/PNT/PointPerfect_Coverage-2025-Cropped-Small.png)

*Image courtesy of [u-blox Thingstream: PerfectPoint Service Description](https://developer.thingstream.io/guides/location-services/pointperfect-service-description#h.jv0o1vz2wkn3)*

- Contiguous USA (L-band + IP)
  - All states, excluding Alaska, Hawaii, and offshore US territories

**Note:** While they recently updated the coverage to support South Korea, it seems to be only available over IP only. SPARTN correction messages do not appear be listed under their topics for L-band reception yet.

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/gps-basics)

### GPS Basics 

The Global Positioning System (GPS) is an engineering marvel that we all have access to for a relatively low cost and no subscription fee. With the correct hardware and minimal effort, you can determine your position and time almost anywhere on the globe.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/what-is-gps-rtk)

### What is GPS RTK? 

Learn about the latest generation of GPS and GNSS receivers to get 14mm positional accuracy!

[](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox)

### Getting Started with U-Center for u-blox 

Learn the tips and tricks to use the u-blox software tool to configure your GPS receiver.

[](https://learn.sparkfun.com/tutorials/gps-rtk2-hookup-guide)

### GPS-RTK2 Hookup Guide 

Get precision down to the diameter of a dime with the new ZED-F9P from u-blox.

## Hardware Overview

The NEO-D9S-00B is a satellite data receiver for L-band correction broadcast, which can be configured for use with a variety of correction services. It decodes the satellite transmission and outputs a correction stream, enabling a high precision GNSS receiver to reach accuracies down to centimeter level! In this section, we\'ll highlight important parts of the board. For more information about the NEO-D9S, check out the [Resources and Going Further](https://learn.sparkfun.com/tutorials/gnss-correction-data-receiver-neo-d9s-hookup-guide#resources-and-going-further) for more information.

[![u-blox NEO-D9S Module](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Module.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Module.jpg)

### Power

Power for this board is **3.3V** and we have provided multiple power options. This first and most obvious is the **USB-C connector**. Secondly, are the **Qwiic Connectors** on the left and right of the board for ground and 3.3V. Thirdly, there is a **5V pin** on the PTH header along the left side of the board that is regulated down to **3.3V** with the 3.3V/600mA AP2112K voltage regulator (as indicated with the 5-pin component next to the 3V3 pin). Make sure that power you provide to this pin does *not* exceed 6 volts. Just below the 5V pin is a **3V3** pin that should only be provided a clean 3.3V power signal. **3V3** are also broken out on the USB-to-serial port and on the other side of the board. GND is also provided near each power pin.

[![Power Through USB, PTH Pins, Qwiic Connector](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-Power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-Power.jpg)

[] **Warning:** There are no protection diodes on the power nets. We recommend powering the board with one power source to avoid conflicting voltages. For example, if the board is connected to USB you will want to ensure that there is no power source connected to any Qwiic enabled device that is daisy chained.

### LED

There is one power LED labeled as `PWR`. The LED will illuminate when 3.3V is activated. This can be disabled by cutting the jumper on the back of the board labeled as \"`PWR`\" as well.

[![LED](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-LED.jpg)

### Qwiic and I^2^C

There are two pins labeled `SDA` and `SCL` which indicates the I^2^C data and clock lines. Similarly, you can use either of the Qwiic connectors to provide power and utilize I^2^C. The [Qwiic ecosystem](https://www.sparkfun.com/qwiic) is made for fast prototyping by removing the need for soldering. All you need to do is plug a Qwiic cable into the Qwiic connector and voila!

[![Qwiic and I2C connectors highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-I2C_Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-I2C_Qwiic.jpg)

**Note:** The only I^2^C address for this specific u-blox product is **0x43**, though each can have their address changed through software.

### SPI

There are four pins that are labeled with their corresponding SPI functionality. These pins are broken out on both sides of the board. As mentioned in the jumpers section, you\'ll need to close the `SPI` jumper on the underside to enable SPI.

[![SPI pins highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-SPI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-SPI.jpg)

### UART

There are two pins labeled as TXD1/POCI and RXD1/PICO. The UART pins are shared with the SPI pins. By default, the UART interface is enabled. Be sure that the `SPI` jumper on the back of the board is open.

- TXD1/POCI = TX out from NEO-D9S
- RXD1/PICO = RX into NEO-D9S

[![UART1 port](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-UART1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-UART1.jpg)

There is also a second UART port. You can connect this to a u-blox F9 module that supports correction data output from the NEO-D9S. The datasheet indicates that you could potentially use any high precision GNSS receiver from the u-blox F9 platform as denoted as the ZED-F9X, where the \"X\" indicates different variant. Make sure to check the latest u-blox F9 product Integration Manual for more information on whether the correction data is supported with the respective module

[![UART2 and UART-to-Serial standard port](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-UART2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-UART2.jpg)

### Broken Out Pins

There are four other pins broken out:

- SAFEBOOT
  : The safeboot pin ([`SAFEBOOT`]) is used to start up the IC in safe boot mode, this could be useful if you somehow manage to corrupt the module\'s Flash memory.
- RESET
  : The reset pin (
  RESET
  ) resets the chip.
- **EXT INT**: The interrupt pin (`EXT INT`) can be used to wake the chip from power save mode.
- **ANT PWR**: The antenna power pin (`ANT PWR`) is available for advanced users that want to power their L-band 3.3V active antenna with an external power source.
  - **Isolate VCC_RF**: You will need to isolate the VCC_RF. Users will need to make sure to cut the trace between the two arrows (i.e. ▶ ◀) to disable the VCC_RF antenna power. You can also shift the surface mount component that connects to the trace by moving it so that it does not connect to the SMA connector.
  - **Install SMD Component**: You will then need to populate the board where L1 is located (i.e. the pads that are not currently populated and connects to the **ANT PWR** PTH) with a 0603 part with impedance \>500 Ohms at 1.5GHz.
  - **Inject Power**: When ready, connect a clean DC power supply voltage between **ANT PWR** and **GND**.

[![Miscellaneous Pins and RF Trace](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-Miscellaneous_Pins_RF_Trace.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-Miscellaneous_Pins_RF_Trace.jpg)

### Jumpers

If you flip the board over, you will notice a few jumper pads. For more information on modifying the jumpers, check out our [tutorial on working with jumper pads and PCB traces](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces).

- **SHLD**: This jumper connects the USB Type C connector\'s shield pin to GND. Cut this to isolate the USB Type C connector\'s shield pin.
- **3V3**: This jumper connects 3.3V to the UART2 port. By default, this is closed and will provide power to the your GNSS receiver. Cut this jumper if you are connecting a 3.3V USB-to-Serial converter with its own power source, or if the GNSS receiver is being powered with its own power source.
- **I^2^C**: This three way jumper labeled `I`^`2`^`C` will connect to two pull-up resistors to the I^2^C data and clock lines when closed. For users with that do not have pull-up resistors attached to the I^2^C lines on their microcontroller, make sure to close the jumpers with a little solder blob.
- **PWR**: The jumper labeled `PWR` connects to the power LED. If you cut this trace, it will disconnect the **Power** LED.
- **SPI**: The jumper labeled `SPI` enables the SPI data bus, thus disabling the UART functions on those lines. This also disables I^2^C interface.

[![Jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Module_Breakout-Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Module_Breakout-Jumpers.jpg)

### SMA Connector

The board is equipped with a SMA connector. You will need an active antenna that can receive signals from an L-Band satellite between 1525.0 MHz to 1559.0 MHz as stated in the datasheet. The specific frequency between the L-Band that the NEO-D9S uses depends on your region and service provider. Make sure to check the antenna\'s datasheet, region, and service provider for more information.

[![SMA Connector](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-SMA_Connector_L-Band.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/19390-NEO-D9S_Breakout-SMA_Connector_L-Band.jpg)

### Board Dimensions

The board dimensions are 1.70\"x1.70\". This does not include the dimensions for the SMA connector and USB Type C connector. There are four mounting holes by each corner of the board.

[![Board Dimensions](https://cdn.sparkfun.com/assets/a/1/b/1/7/Dimensions.png)](https://cdn.sparkfun.com/assets/a/1/b/1/7/Dimensions.png)

## Hardware Hookup

**Note:** If you ordered a ZED-F9P breakout, you will need to make sure to [check and update the ZED-F9P module\'s firmware](https://learn.sparkfun.com/tutorials/how-to-upgrade-firmware-of-a-u-blox-gnss-receiver/identifying-current-firmware-version) so that the module can interpret NEO-D9S module\'s correction data. We tested it using the \"[ZED-F9P FW 1.00 HPG 1.32](https://www.u-blox.com/en/product/zed-f9p-module).\"

To add GNSS correction data to your high precision GNSS receiver like the ZED-F9P, you can connect any of the serial ports between the two boards. If you are using SPI to connect, just make sure to enable the SPI port by adding a solder jumper to the SPI jumper pads. For an embedded application, we recommend adding an ESP32 to the setup. In addition to the Thingstream PointPerfect over L-band satellite, the ESP32 will also allow you to use the Thingstream PointPerfect service over Internet Protocol (IP) using MQTT.

### I^2^C via Qwiic

Below is one example to connect using the I^2^C port and Qwiic. Simply insert a Qwiic cable between the ZED-F9P, NEO-D9S, and Arduino microcontroller\'s Qwiic connectors. Plug in a compatible antenna with SMA connector to the ZED-F9P and NEO-D9S board. For the ZED-F9P, you will need the multiband antenna that is capable of receiving L1/L2 bands. For boards that have a u.FL connector, make sure use a u.FL to SMA adapter cable. For the NEO-D9S, you will need to attach an L-Band antenna. Secure the connection on both antennas using the hex nut until it is finger-tight. For power, we will use a USB-C cable to power the ESP32 development board. You can also use this cable to connect each breakout to your computer when using the u-blox u-center software.

[![ESP32 IoT RedBoard, ZED-F9P w/ u.FL connector, and NEO-D9S connected via Qwiic Cables](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/5/2/GNSS__RTK_ESP32_u-blox_ZED-F9P_NEO-D9S_Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/GNSS__RTK_ESP32_u-blox_ZED-F9P_NEO-D9S_Qwiic.jpg)

### I^2^C and UART2 Ports via PTH

For those that prefer a PTH connection, you could connect using male header pins, 2-pin jumpers, F/F jumper wires, and M/F jumper wires. In this case, the ZED-F9P and NEO-D9S breakout boards were connected using the male header pins and 2-pin jumpers. The Arduino microcontroller was connected using a Qwiic cable. Of course, you will still need to plug in a compatible antenna with SMA connector to the ZED-F9P and NEO-D9S board. For the ZED-F9P, you will need the multiband antenna that is capable of receiving L1/L2 bands. For boards that have a u.FL connector, make sure use a u.FL to SMA adapter cable. For the NEO-D9S, you will need to attach an L-Band antenna. Secure the connection using the hex nut until it is finger-tight. For power, we will use a USB-C cable to power the ESP32 development board. You can also use this cable to connect each breakout to your computer when using the u-blox u-center software.

[![ESP32 IoT RedBoard, ZED-F9P w/ u.FL connector, and NEO-D9S connected via Male Header Pins, Jumper Shunts, and Qwiic Cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/5/2/GNSS__RTK_ESP32_u-blox_ZED-F9P_NEO-D9S_UART2_I2C_Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/GNSS__RTK_ESP32_u-blox_ZED-F9P_NEO-D9S_UART2_I2C_Qwiic.jpg)

## u-blox Firmware Update

**Note:** Make sure that you are using a u-blox high precision GNSS (HPG) module that supports the SPARTN formatted corrections (i.e. `UBX-RXM-PMP`). At the time of writing, the ZED-F9P supports the SPARTN formatted corrections sent by the NEO-D9S with **FW 1.00 HPG 1.30** and above. We tested using the latest **FW 1.00 HPG 1.32+**. Check your module\'s firmware release notes if you are unsure if the version number supports the SPARTN formatted corrections.

We recommend checking the firmware on your high precision GNSS (HPG) module (in this case, the ZED-F9P). If the firmware is old, you will need to [upgrade the firmware on the HPG module](https://learn.sparkfun.com/tutorials/how-to-upgrade-firmware-of-a-u-blox-gnss-receiver).

[](https://learn.sparkfun.com/tutorials/how-to-upgrade-firmware-of-a-u-blox-gnss-receiver)

### How to Upgrade Firmware of a u-blox GNSS Receiver 

March 26, 2021

A few steps and you\'ll upgrade to the latest features on a u-blox GNSS receiver.

You can download the latest firmware from u-blox. Below is a link to the ZED-F9P module\'s product page. Click the \"**Documentation & resources**\" tab and look for the latest firmware under the section **Firmware Update**. You may need to hit the **Load more** button a few times before you can see the firmware.

[u-blox: ZED-F9P Module Product Page](https://www.u-blox.com/en/product/zed-f9p-module)

**Note:** At the time of writing, the NEO-D9S works with the ZED-F9P. Other models with the u-blox F9 engine (such as the ZED-F9R) may work as long as the firmware supports the SPARTN formatted corrections (i.e. `UBX-RXM-PMP`). Make sure to check the associated datasheets for your high precision GNSS module for more information.

## u-Blox Thingstream Services

**Please note:** The u-blox Thingstream PointPerfect Correction Service is only available to \"B2B Customers\" (Business To Business Customers). Please check the [Service Terms](https://cdn.sparkfun.com/assets/2/5/a/4/f/Service_Terms.pdf) before purchasing hardware.\
\

[u-blox Service Terms](https://cdn.sparkfun.com/assets/2/5/a/4/f/Service_Terms.pdf)

There are three key steps to be able to achieve centimeter positioning accuracy using the ZED-F9P and NEO-D9S.

- Register with u-blox Thingstream and sign up for a PointPerfect L-band plan (data stream)
- Configure the NEO-D9S to receive the u-blox PointPerfect correction data stream
- Configure the ZED-F9P with encryption key(s) so it can decrypt and use the correction data

By default, the ZED-F9P is configured such that the correction data is passed from the NEO to the ZED using the UART2 interface. However, it is also possible to read the correction data from the NEO and push (write) it to the ZED using I^2^C. We just need to configure the modules so that the I^2^C port is enabled and set the protocol.

### Thingstream and PointPerfect Services

The NEO-D9S was designed to receive correction data from an L-band satellite and push it to a high precision GNSS module like the ZED-F9P. You will need to use u-blox Thingstream and PointPerfect service to provide dynamic keys in order to decrypt the correction data.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![u-blox Thingstream Service Logo](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/u-blox_thingstream.png "Click here to visit the u-blox Thingstream landing page!")](https://www.u-blox.com/en/product/thingstream)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

[Thingstream](https://www.u-blox.com/en/product/thingstream) is u-blox service delivery platform for IoT Communication-as-a-Service, IoT Security-as-a-Service and IoT Location-as-a-Service.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![u-blox Point Perfect GNSS Augmentation Logo](https://cdn.sparkfun.com//assets/learn_tutorials/2/3/5/2/u-blox_pointperfect-gnss-augmentation-ppp.png "Click here to visit the u-blox PointPerfect landing page!")](https://www.u-blox.com/en/product/pointperfect)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[PointPerfect](https://www.u-blox.com/sites/default/files/PointPerfect_ProductSummary_UBX-21024758.pdf) is u-blox GNSS augmentation service which is designed to provide high-precision GNSS corrections to suitable receivers with decimeter-level location accuracy. The following webinar from u-blox has an excellent explanation of the service and how the system works.

PointPerfect data is delivered through Thingstream. The first step is to register with Thingstream and then request an L-Band plan:

[![PointPerfect Pricing](https://sparkfunx.github.io/u-blox_ZED-F9P_NEO-D9S_Combo_Breakout/img/hookup_guide/PointPerfect_Pricing.png)](https://sparkfunx.github.io/u-blox_ZED-F9P_NEO-D9S_Combo_Breakout/img/hookup_guide/PointPerfect_Pricing.png)

*PointPerfect pricing (correct at Sept. 14th 2022). (Click to enlarge)*

You can find the current pricing on [u-blox portal](https://portal.thingstream.io/pricing/). Select **IoT Location-as-a-Service** and then **PointPerfect**.

You may need to [contact u-blox](support@thingstream.io) first, to enable the option to purchase an L-Band plan through your Thingstream account.

The **PointPerfect L-band** plan provides unlimited access to the L-band satellite correction data stream (via the NEO-D9S).

If you have an internet connection, you can also receive PointPerfect corrections via IP (MQTT). The **PointPerfect L-band and IP** plan may be a better choice if you think you may want to receive correction data via both satellite and Internet.

Once L-band permissions are enabled on your Thingstream account, you will be able to add a new L-band Location Thing and view its credentials:

- [Login to Thingstream](https://portal.thingstream.io/)
- Select **Location Services** and then **Location Things**
- The **Add Location Thing** button (top right) will allow you to select and activate an L-Band plan
- Once your L-band plan is active, you will be able to monitor your **Activity** and view your **Credentials** via the appropriate tabs

u-blox have written a [comprehensive application note](https://www.u-blox.com/sites/default/files/documents/NEO-D9S_ZED-F9_Config_SPARTN_AppNote_UBX-22008160.pdf) which describes in detail: the configuration of both NEO and ZED; and how to interpret the expiry date for the L-band encryption keys. In the following sections, we describe how to configure the NEO and ZED using our [u-blox GNSS Arduino Library](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library).

## Installing the Arduino Library

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino IDE, library, or board add-on, please review the following tutorials.\
\

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

\
If you\'ve never connected an CH340 device to your computer before, you may need to install drivers for the USB-to-serial converter. Check out our section on [How to Install CH340 Drivers\"](https://learn.sparkfun.com/tutorials/sparkfun-serial-basic-ch340c-hookup-guide#drivers-if-you-need-them) for help with the installation.

\
The SparkFun u-blox Arduino library enables the reading of all positional datums as well as sending binary UBX configuration commands over I^2^C. This is helpful for configuring advanced modules like the ZED-F9P but also the NEO-D9S, NEO-M8P-2, SAM-M8Q and other u-blox modules that use the u-blox binary protocol.

**Note:** We support two versions of the SparkFun u-blox GNSS library. [Version 2](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library) and [Version 3](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3). [Version 3](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3) uses the u-blox Configuration Interface (VALSET and VALGET) to configure the module, instead of the deprecated UBX-CFG messages. For modules like the D9, F9 and M10, we recommend upgrading to [Version 3](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3). However, older modules like the M8 do not support the Configuration Interface. For those you will need to keep using [Version 2](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library) of the library. We will continue to support both.

The SparkFun u-blox Arduino library can be downloaded with the Arduino library manager by searching \'**SparkFun u-blox GNSS v3**\' or you can grab the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3) to manually install. Once the library is installed, you can take advantage of the examples for the ZED-F9P.

[SparkFun u-blox Arduino Library v3 (ZIP)](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3/archive/main.zip)

\

## Arduino Library Overview

We will be highlighting a few parts of the SparkFun u-blox Arduino GNSS Library below for the NEO-D9S and the ZED-F9P.

### NEO-D9S Configuration

The first step is to declare the SFE_UBLOX_GNSS object. Like most Arduino sketches, this is done at a global scope (after the include file declaration), not within the setup() or loop() functions.

    language:c
    #include <SparkFun_u-blox_GNSS_v3.h> //http://librarymanager/All#SparkFun_u-blox_GNSS_v3
    SFE_UBLOX_GNSS myLBand; // NEO-D9S

Within setup() we then need to start (initialize) communiation with the NEO-D9S. The NEO-D9S has a default I^2^C address of **0x43** and so we need to provide that when calling the begin method:

    language:c
    Wire.begin(); //Start I2C

    while (myLBand.begin(Wire, 0x43) == false) //Connect to the u-blox NEO-D9S using Wire port. The D9S default I2C address is 0x43 (not 0x42)
    
    Serial.println(F("u-blox NEO-D9S connected"));

The NEO-D9S needs to be configured so it can receive the PointPerfect correction stream. The configuration items are:

  Configuration item          Default value
  --------------------------- --------------------
  CFG-PMP-CENTER_FREQUENCY    1539812500 Hz
  CFG-PMP-SEARCH_WINDOW       2200 Hz
  CFG-PMP-USE_SERVICE_ID      1 (true)
  CFG-PMP-SERVICE_ID          50821
  CFG-PMP-DATA_RATE           2400 (B2400) bps
  CFG-PMP-USE_DESCRAMBLER     1 (true)
  CFG-PMP-DESCRAMBLER_INIT    23560
  CFG-PMP-USE_PRESCRAMBLING   0 (false)
  CFG-PMP-UNIQUE_WORD         0xe15ae893e15ae893

The centre frequency varies depending on which satellite is broadcasting corrections for your geographical area.

The up-to-date frequencies are distributed via the MQTT **/pp/frequencies/Lb** topic. At the time of writing, they are (in MHz):

    language:c
    
        }
      }
    }

We can add that to the code as follows:

    language:c
    const uint32_t myLBandFreq = 1556290000; // Uncomment this line to use the US SPARTN 1.8 service

The code to configure the NEO-D9S is as follows. Note that the `UBLOX_CFG_PMP_USE_SERVICE_ID`, `UBLOX_CFG_PMP_SERVICE_ID` and `UBLOX_CFG_PMP_DESCRAMBLER_INIT` also need to be changed.

    language:c
      uint8_t ok = myLBand.setVal32(UBLOX_CFG_PMP_CENTER_FREQUENCY,   myLBandFreq); // Default 1539812500 Hz
      if (ok) ok = myLBand.setVal16(UBLOX_CFG_PMP_SEARCH_WINDOW,      2200);        // Default 2200 Hz
      if (ok) ok = myLBand.setVal8(UBLOX_CFG_PMP_USE_SERVICE_ID,      0);           // Default 1 
      if (ok) ok = myLBand.setVal16(UBLOX_CFG_PMP_SERVICE_ID,         21845);       // Default 50821
      if (ok) ok = myLBand.setVal16(UBLOX_CFG_PMP_DATA_RATE,          2400);        // Default 2400 bps
      if (ok) ok = myLBand.setVal8(UBLOX_CFG_PMP_USE_DESCRAMBLER,     1);           // Default 1
      if (ok) ok = myLBand.setVal16(UBLOX_CFG_PMP_DESCRAMBLER_INIT,   26969);       // Default 23560
      if (ok) ok = myLBand.setVal8(UBLOX_CFG_PMP_USE_PRESCRAMBLING,   0);           // Default 0
      if (ok) ok = myLBand.setVal64(UBLOX_CFG_PMP_UNIQUE_WORD,        16238547128276412563ull); // 0xE15AE893E15AE893

Finally, we need to ensure that the communication port is set correctly. Let\'s configure the UART2 port. In order to do that, we need to:

- Change the baud rate to 38400 - to match the ZED-F9P\'s baud rate
- Ensure that the UBX protocol is enabled for output on UART2
- Enable the **RXM PMP** message on UART2
  - The **RXM PMP** message contains the **SPARTN** correction data in **UBX** format
- Perform a restart (software reset) so that the NEO-D9S starts using the new configuration items

Of course, you could set the NEO-D9S to output the correction data to the other communication ports as well (e.g. in the Arduino Library, correction data was sent via the I^2^C, UART1, and UART2 ports for example 19). The sample code below configures the NEO-D9S module\'s UART2 port to pass the correction data.

    language:c
      if (ok) ok = myLBand.setVal32(UBLOX_CFG_UART2_BAUDRATE,          38400); // match baudrate with ZED default
      if (ok) ok = myLBand.setVal8(UBLOX_CFG_UART2OUTPROT_UBX,         1);     // Enable UBX output on UART2
      if (ok) ok = myLBand.setVal8(UBLOX_CFG_MSGOUT_UBX_RXM_PMP_UART2, 1);     // Output UBX-RXM-PMP on UART2

      Serial.print(F("L-Band configuration: "));
      if (ok)
        Serial.println(F("OK"));
      else
        Serial.println(F("NOT OK!"));

      myLBand.softwareResetGNSSOnly(); // Do a restart

Once the NEO-D9S has aquired the signal from the satellite, it will start outputting **PMP** correction messages to the ZED-F9P on UART2.

### ZED-F9P Configuration

We need to declare a second **SFE_UBLOX_GNSS** object for the ZED-F9P. Again, this is done at a global scope (after the include file declaration), not within the `setup()` or `loop()` functions.

    language:c
    SFE_UBLOX_GNSS myGNSS; // ZED-F9P

Within **setup()** we need to start (initialize) communication with the ZED-F9P:

    language:c
      while (myGNSS.begin() == false) //Connect to the u-blox module using Wire port and the default I2C address (0x42)
      
      Serial.println(F("u-blox GNSS module connected"));

We then need to:

- Make sure the ZED-F9P\'s UART2 port is configured to accept the PMP correction data
- Tell the ZED-F9P to use FIXED carrier solutions when possible (this is the default setting)
- Tell the ZED-F9P to accept L-band PMP as a correction source

The sample code below configures the ZED-F9P module\'s UART2 port to accept correction data. Again, you could use the other communication ports as well. Just make sure that the communication ports match the settings that were configured on the NEO-D9S.

    language:c
              ok = myGNSS.setUART2Input(COM_TYPE_UBX | COM_TYPE_NMEA | COM_TYPE_SPARTN); //Be sure SPARTN input is enabled
      if (ok) ok = myGNSS.setDGNSSConfiguration(SFE_UBLOX_DGNSS_MODE_FIXED); // Set the differential mode - ambiguities are fixed whenever possible
      if (ok) ok = myGNSS.setVal8(UBLOX_CFG_SPARTN_USE_SOURCE, 1); // use LBAND PMP message

The final piece of the puzzle is to provide the ZED-F9P with the keys it needs to decrypt the encrypted SPARTN (PMP) corrections.

The ZED-F9P can hold two dynamic keys: the current key; and the next key. We also need to tell it when each key is valid from, so it knows when to switch to the next key.

You can find the current and next keys in the **Location Services \\ Location Things \\ Thing Details \\ Credentials tab** in Thingstream:

[![L-band Dynamic Keys](https://sparkfunx.github.io/u-blox_ZED-F9P_NEO-D9S_Combo_Breakout/img/hookup_guide/Dynamic_Keys.png)](https://sparkfunx.github.io/u-blox_ZED-F9P_NEO-D9S_Combo_Breakout/img/hookup_guide/Dynamic_Keys.png)

*PointPerfect L-band dynamic keys. (Click to enlarge)*

The ZED-F9P actually needs to know when the keys are valid **from**, rather than when they expire. Each key is valid for four weeks, so we need to work backwards 4 weeks from the expiry date.

The current key expires at midnight (UTC) at the end of Friday, September 23rd, 2022. This means it became valid 4 weeks earlier at midnight (UTC) on August 27th:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://sparkfunx.github.io/u-blox_ZED-F9P_NEO-D9S_Combo_Breakout/img/hookup_guide/Key_Valid_From.png)](https://sparkfunx.github.io/u-blox_ZED-F9P_NEO-D9S_Combo_Breakout/img/hookup_guide/Key_Valid_From.png)   [![](https://sparkfunx.github.io/u-blox_ZED-F9P_NEO-D9S_Combo_Breakout/img/hookup_guide/Key_Expiry.png)](https://sparkfunx.github.io/u-blox_ZED-F9P_NEO-D9S_Combo_Breakout/img/hookup_guide/Key_Expiry.png)
  *Current Dynamic Key Valid 4 Weeks from Expiry Date*                                                                                                                                                                  *Next Dynamic Key Valid from Expiry Date*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Dynamic Key: Expiry and Valid From dates. (Click to enlarge)*

Using the website recommended in the u-blox Application Note:

[http://navigationservices.agi.com/GNSSWeb](http://navigationservices.agi.com/GNSSWeb)

we can see that the key became valid during GPS week **2224**, at time-of-week **518400**.

We can use the Arduino Library `setDynamicSPARTNKey` method to configure a single key:

    language:c
      if (ok) ok = myGNSS.setDynamicSPARTNKey(16, 2224, 518400, "500--------------------------177");

      Serial.print(F("GNSS: configuration "));
      if (ok)
        Serial.println(F("OK"));
      else
        Serial.println(F("NOT OK!"));

Alternately, we can set both the current key and the next key together using **setDynamicSPARTNKeys**. The next key becomes valid during GPS week **2228**:

    language:c
      if (ok) ok = myGNSS.setDynamicSPARTNKeys(16, 2224, 518400, "500--------------------------177", 16, 2228, 518400, "582--------------------------a7d");

The keys can also be retrieved using MQTT. We have an [Arduino Library example](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library/tree/main/examples/ZED-F9P/Example20_PMP_with_L-Band_Keys_via_MQTT) which shows how to retrieve the keys from the L-band + IP key distribution topic **/pp/ubx/0236/Lb**. That topic provides the keys in UBX (binary) format, ready to be pushed to the ZED.

The keys are also available in human-readable JSON format from the MQTT topic **/pp/key/Lb** . But note that that topic provides the **valid from** in Unix epoch format, in milliseconds, excluding the 18 leap seconds since GPS time started!

    language:c
    ,
        "next": 
      }
    }

## NEO-D9S and NEO-D9C \> Example 1: NEO-D9S 

From the menu, select the following: **File** \> **Examples** \> Examples from Custom Libraries \| [**SparkFun u-blox GNSS v3** \> **NEO-D9S_and_NEO-D9C** \> **Example1_NEO-D9S**](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3/blob/main/examples/NEO-D9S_and_NEO-D9C/Example1_NEO-D9S/Example1_NEO-D9S.ino).

### Upload Code

When ready, select the correct board definition from the menu (in this case, **Tools** \> **Boards** \> **SparkFun ESP32 IoT RedBoard**). Then select the correct COM port that the board enumerated to (in this case, it was **COM13**). Hit the upload button.

### What You Should See

Open the Arduino Serial Monitor at **115200** baud. If all is well, you should see the following output indicating that the **UBX-RXM-PMP** correction data is being received! In this case, the NEO-D9S had a multiband antenna pointing up towards the sky from SparkFun HQ\'s rooftop.

[![Arduino Serial Monitor NEO-D9S and SparkFun ESP32 IoT RedBoard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/5/2/NEO-D9S_ESP32_RedBoard.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/NEO-D9S_ESP32_RedBoard.JPG)

*Click image for a closer view.*

## NEO-D9S and NEO-D9C \> Example 2: L-Band Corrections with NEO-D9S 

From the menu, select the following: **File** \> **Examples** \> Examples from Custom Libraries \| [**SparkFun u-blox GNSS_v3** \> \> **NEO-D9S_and_NEO-D9C** \> **Example2_LBand_Corrections_with_NEO-D9S**](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3/tree/main/examples/NEO-D9S_and_NEO-D9C/Example2_LBand_Corrections_with_NEO-D9S).

### Add Decryption Keys and Valid Dates

In the **secrets.h** tab, copy the PointPerfect keys and insert the current (i.e. `currentDynamicKey[]`) and next keys (i.e. `nextDynamicKey[]`) between each quote where it says `"<ADD YOUR L-Band or L-Band + IP DYNAMIC KEY HERE>"`. Calculate the [current and next key GPS weeks based on the expiry date](http://navigationservices.agi.com/GNSSWeb) as stated in the Arduino Library Overview for the ZED-F9P configuration. Then adjust the current and next key dates.

    language:c
    const uint8_t currentKeyLengthBytes =   16; 
    const char currentDynamicKey[] =        "<ADD YOUR L-Band or L-Band + IP DYNAMIC KEY HERE>";
    const uint16_t currentKeyGPSWeek =      2245; // Update this when you add new keys
    const uint32_t currentKeyGPSToW =       0;

    const uint8_t nextKeyLengthBytes =      16; 
    const char nextDynamicKey[] =           "<ADD YOUR L-Band or L-Band + IP DYNAMIC KEY HERE>";
    const uint16_t nextKeyGPSWeek =         2249; // Update this when you add new keys
    const uint32_t nextKeyGPSToW =          0;

### Upload Code

When ready, select the correct board definition from the menu (in this case, **Tools** \> **Boards** \> **SparkFun ESP32 IoT RedBoard**). Then select the correct COM port that the board enumerated to (in this case, it was **COM13**). Hit the upload button.

### What You Should See

Open the Arduino Serial Monitor at **115200** baud. If all is well, you should see the following output indicating that the NEO-D9S received the **UBX-RXM-PMP** correction data and ZED-F9P has decrypted the data! In this case, the NEO-D9S had a multiband antenna pointing up towards the sky from SparkFun HQ\'s rooftop. Watch the accuracy converge and decrease to a smaller number. Depending on what satellites are in view, it may take a little time before you reach the RTK floating or fixed solution.

[![Arduino Serial Monitor NEO-D9S, ZED-F9P, and SparkFun ESP32 IoT RedBoard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/5/2/ZED-F9P_NEO-D9S_ESP32_RedBoard_Output_Success.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/ZED-F9P_NEO-D9S_ESP32_RedBoard_Output_Success.JPG)

*Click image for a closer view.*

Below is the output once the RTK Fixed Solution was achieved. You will notice that the values converged to a point with a horizontal accuracy of about 20mm.

[![Arduino Serial Monitor NEO-D9S, ZED-F9P, and SparkFun ESP32 IoT RedBoard - RTK Fixed Solution Acheived](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/5/2/ZED-F9P_NEO-D9S_ESP32_RedBoard_Output_Success_RTK_Fixed_Solution_Convergence.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/ZED-F9P_NEO-D9S_ESP32_RedBoard_Output_Success_RTK_Fixed_Solution_Convergence.JPG)

*Click image for a closer view.*

**Troubleshooting:** If you see the following error when your Arduino is starting up, this may indicate that your high precision GNSS module\'s firmware is out of date and does not support the SPARTN correction data. In this case, we were using the ZED-F9P module with old firmware.\
\

    u-blox GNSS connected
    GNSS: configuration  =>  ERROR!
    u-blox NEO-D9S connected
    L-Band configuration  =>  OK

If you are able to configure both modules but do not see new correction data being pushed from the NEO-D9S, it may be due to the active antenna that you are using in your region or you have poor reception. Make sure to use an active antenna that is within the L-Band for your region or move to a different location where there is more visibility (i.e. not in a building). Make sure to also check that the dynamic keys and valid dates match what is provided with your ThingStream PointPerfect account.

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) and [u-blox Forums](https://portal.u-blox.com/s/) are great places to find and ask for help. For specific questions about the u-blox service, we recommend heading over more to the u-blox Forums.\
\

[Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)   [Log Into u-blox Forums](https://portal.u-blox.com/s/)

### ThingStream PointPerfect L-band Reception

In order to receive the u-blox ThingStream PointPerfect correction data, you will need:

- a suitable antenna
- to be located within contiguous USA
- to have a clear view of the sky to the South

#### SparkFun GNSS Multi-Band L1/L2 Surveying Antenna - TOP106

We have been successful using the [SparkFun GNSS Multi-Band L1/L2 Surveying Antenna (TNC) - TOP106 (GPS-17751)](https://www.sparkfun.com/products/17751) antenna to receive PointPerfect correction data in the USA.

[![GNSS Multi-Band L1/L2 Surveying Antenna - TNC (TOP106)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/8/7/4/17587-L1_L2_GNSS_antenna_TOP106-09-1.png)](https://www.sparkfun.com/gnss-multi-band-l1-l2-surveying-antenna-tnc-top106.html)

### [GNSS Multi-Band L1/L2 Surveying Antenna - TNC (TOP106)](https://www.sparkfun.com/gnss-multi-band-l1-l2-surveying-antenna-tnc-top106.html) 

[ GPS-17751 ]

The TOP106 from TOPGNSS is a certified GNSS/GPS surveying antenna capable of receiving the L1/L2 bands for GPS, GLONASS, Gali...

[ [\$199.95] ]

#### Thingstream PointPerfect Coverage

The PointPerfect GNSS augmentation service is available on a continental scale with seamless coverage in the contiguous USA, including up to 12 nautical miles (\~ 22 km) off coastlines. **Please note: the u-blox PointPerfect EU L-Band service is being suspended on March 10th 2025.**

[![L-Band Coverage](https://www.sparkfun.com/media/.renditions/wysiwyg/Additional-Product-Page-Images/PNT/PointPerfect_Coverage-2025-Cropped-Small.png)](https://www.sparkfun.com/media/.renditions/wysiwyg/Additional-Product-Page-Images/PNT/PointPerfect_Coverage-2025-Cropped-Small.png)

*PointPerfect Service Coverage. (Click to enlarge)*

As stated earlier, make sure to check back on u-blox\'s website to see if there is additional coverage in your region. Note that while they recently updated the coverage to support South Korea, it seems to be available over IP only. SPARTN correction messages does not appear to be listed under their topics for L-band reception yet. There are additional regions under consideration for the future but they have not been included yet for L-band reception.

#### PointPerfect Satellite Broadcast

PointPerfect augmentation data is broadcast from a satellite covering the contiguous USA. The satellite is in geostationary orbits over the equator - the same as for satellite television broadcasts. It is essential that your antenna has an unobstructed view of the sky, especially to the South where the satellite is positioned.

Depending on your latitude, the satellite for your area could be low in the sky. You need to ensure that trees, buildings etc. are not blocking the signal.