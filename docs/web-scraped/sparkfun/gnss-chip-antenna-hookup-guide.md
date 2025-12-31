# Source: https://learn.sparkfun.com/tutorials/gnss-chip-antenna-hookup-guide

## Introduction

GPS is common but what if you need to pack your GPS receiver into a small space such as a wearable? Standard [GPS antennas](https://www.sparkfun.com/products/14986) are much too large to strap to your wrist so what do you do? You use one of the [SparkFun GNSS Chip Antennas](https://www.sparkfun.com/products/15247)!

[![SparkFun GNSS Chip Antenna Evaluation Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/7/1/2/15247-SparkFun_GNSS_Chip_Antenna_Evaluation_Board-01.jpg)](https://www.sparkfun.com/sparkfun-gnss-chip-antenna-evaluation-board.html)

### [SparkFun GNSS Chip Antenna Evaluation Board](https://www.sparkfun.com/sparkfun-gnss-chip-antenna-evaluation-board.html) 

[ GPS-15247 ]

The SparkFun GNSS Chip Antenna Evaluation Board makes it easy to test out various sized GPS antennas and geometries.

**Retired**

The SparkFun GNSS Chip Antenna Evaluation Board makes it easy to test out various sized GPS antennas and geometries. These individual antennas can even be separated and installed permanently into a project once you select the best one for your application.

### Required Materials

The GNSS Chip Antenna Evaluation Board (we'll call it the eval board from here on out for your tongues' sake) is possible because we have designed each antenna to have a 50-ohm microstrip. To connect, you'll need a [U.FL cable](https://www.sparkfun.com/products/15114) and a GPS receiver capable of connecting to a U.FL cable. You may not need everything though depending on what you have. Add it to your cart, read through the guides, and adjust the cart as necessary.

[![U.FL to U.FL Mini Coax Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/8/2/15114-U.FL_to_U.FL_Mini_Coax_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/u-fl-to-u-fl-mini-coax-cable-200mm.html)

### [U.FL to U.FL Mini Coax Cable - 200mm](https://www.sparkfun.com/u-fl-to-u-fl-mini-coax-cable-200mm.html) 

[ WRL-15114 ]

This cute little coax is a champ in our RF kit! It has a right angle female U.FL (aka I-PEX) connector on both ends. Now inst...

[ [\$2.75] ]

Below is a list of SparkFun GPS receivers that have a U.FL connector for its antenna. These are the easiest products to get working with the eval board.

[![SparkFun GPS Breakout - ZOE-M8Q (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/1/4/15193-SparkFun_GPS_Breakout_-_U.FL__ZOE-M8__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-gps-breakout-zoe-m8q-qwiic.html)

### [SparkFun GPS Breakout - ZOE-M8Q (Qwiic)](https://www.sparkfun.com/sparkfun-gps-breakout-zoe-m8q-qwiic.html) 

[ GPS-15193 ]

The SparkFun ZOE-M8Q GPS Breakout is a high accuracy, miniaturized, GPS board that is perfect for applications that don\'t pos...

[ [\$50.95] ]

[![SparkFun GPS Breakout - XA1110 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/0/14414-SparkFun_GPS_Breakout_-_XA1110__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-gps-breakout-xa1110-qwiic.html)

### [SparkFun GPS Breakout - XA1110 (Qwiic)](https://www.sparkfun.com/sparkfun-gps-breakout-xa1110-qwiic.html) 

[ GPS-14414 ]

The SparkFun XA1110 GPS Breakout is a small I2C-supported module built for easy hookup, thanks to our Qwiic Connect System. E...

[ [\$35.95] ]

One of the most common setups is shown below. The [ZOE-M8Q](https://www.sparkfun.com/products/15193) has a U.FL connector and can be attached to any of the six chip-scale GPS antennas.

[![SparkFun Qwiic ZOE connected to the GNSS antenna eval board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/1/SparkFun_GNSS_Chip_Antenna_Evaluation_Board_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/SparkFun_GNSS_Chip_Antenna_Evaluation_Board_Hookup_Guide-02.jpg)

### Suggested Reading

If you're unfamiliar with working with GPS receivers or U.FL connectors, be sure to checkout some of these foundational tutorials. You\'ll also need to check out the respective tutorials for your GPS receiver.

[](https://learn.sparkfun.com/tutorials/gps-basics)

### GPS Basics 

The Global Positioning System (GPS) is an engineering marvel that we all have access to for a relatively low cost and no subscription fee. With the correct hardware and minimal effort, you can determine your position and time almost anywhere on the globe.

[](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl)

### Three Quick Tips About Using U.FL 

Quick tips regarding how to connect, protect, and disconnect U.FL connectors.

## Hardware Overview

The SparkFun GNSS Chip Antenna Evaluation Board is composed of six 'blocks'. Each one is capable of obtaining a GPS lock but the reception quality depends on the size and shape of the antenna.

[![SparkFun GNSS Chip Antenna Evaluation Board](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/SparkFun_GNSS_Chip_Antenna_Eval.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/SparkFun_GNSS_Chip_Antenna_Eval.jpg)

### Antenna Technologies

There are six different antennas on the GNSS Chip Antenna Evaluation Board.

[![Six highlighted antennas](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/SparkFun_GNSS_Chip_Antenna_Eval-Antennas.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/SparkFun_GNSS_Chip_Antenna_Eval-Antennas.jpg)

You can find the datasheet and technical information for each, in order from top left to lower right:

- [Molex Molded - 1.4dBi](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/Molex_GNSS_Molded_1462350001_sd.pdf)
- [Pulse W3011 - 3.4dBi](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/W3011_W3011A.pdf)
- [Pulse W3062A - 2.5dBi](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/W3062A.pdf)
- [TE Puck - 0dBi](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/TE_GPS_Puck_Antenna_ENG_DS_1513634_A.pdf)
- [Molex Cube - 1dBi](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/Molex_GNSS_Cube_1462160001_sd.pdf)
- [Molex Chip - 2dBi](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/Molex_GPS_Chip_Antenna_2042830001_sd.pdf)

The gain is printed on each antenna block but take this gain with a grain of salt. Antenna manufacturers tend to report the theoretical gain of an antenna, or the gain achieved from a more-than-ideal setup (i.e., using a ground plane the size of your head).

### Individual Antenna Blocks

Each of the six antennas has its own U.FL connector, mounting holes, U.FL stress relief holes, and an isolated ground plane.

[![Single antenna block with U.FL, mounting holes, and stress relief pins highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/SparkFun_GNSS_Chip_Antenna_Eval-Connections.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/SparkFun_GNSS_Chip_Antenna_Eval-Connections.jpg)

The board comes as a single unit but can be snapped apart so that any one antenna block can be mounted into a project. In theory the antennas should perform better separated but we found no measurable performance difference between the antennas as a whole or broken apart.

[![Antenna blocks snapped apart](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/1/SparkFun_GNSS_Chip_Antenna_Evaluation_Board_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/SparkFun_GNSS_Chip_Antenna_Evaluation_Board_Hookup_Guide-01.jpg)

### U.FL Connectors and Stress Relief

U.FL connectors are generally pretty resilient but if you've got a particularly wearable project or harsh antenna environment, you can reinforce the U.FL connection by soldering a piece of wire over the cable to hold it in place. We recommend you do this *after* you've selected the antenna that best suits your project.

[![U.FL cable with attached stress relief](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/1/SparkFun_GNSS_Chip_Antenna_Evaluation_Board_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/1/SparkFun_GNSS_Chip_Antenna_Evaluation_Board_Hookup_Guide-03.jpg)

## How Well Do the Antennas Perform?

Here's our preliminary findings:

  Antenna Name                      SIV^\[[1](#note1)\]^   PDOP^\[[2](#note2)\]^   HDOP^\[[3](#note3)\]^
  --------------------------------- ---------------------- ----------------------- -----------------------
  Molex Molded                      5                      2.2                     1
  W3011                             9                      1.47                    0.69
  W3062A                            6                      2.48                    1.16
  Molex Chip                        5                      2.27                    1.18
  Molex Cube                        10                     1.16                    0.63
  TE Puck                           9                      1.27                    0.68
  Molex Flexible^\[[4](#note4)\]^   10                     1.14                    0.62

\

[]^1^ - Satellites in view: The number of satellites an antenna was able to detect after 60 seconds of searching. Higher is generally better.

[]^2^ - Position Dilution of Precision: The accuracy of the 3D solution being output by the receiver. A lower number is better. Meaning of numbers can be found on [Wikipedia](https://en.wikipedia.org/wiki/Dilution_of_precision_(navigation)#Meaning_of_DOP_Values).

[]^3^ - Horizontal Dilution of Precision: The accuracy of the horizontal location solution being output by the receiver. A lower number is better. Meaning of numbers can be found on [Wikipedia](https://en.wikipedia.org/wiki/Dilution_of_precision_(navigation)#Meaning_of_DOP_Values).

[]^4^ - The [Flexible Adhesive GPS Antenna](https://www.sparkfun.com/products/15246) is not on the GNSS Chip Antenna Evaluation Board but performed impressively.

These results are provided for illustration only. Testing was done using a Ublox ZED-F9P on the [RTK2](https://www.sparkfun.com/products/15136) with 60 seconds to obtain satellites from a cold start. Your results will vary greatly based on how clear your view is of the sky, where you are located, and the type of GPS receiver used.

As you can see, the larger antennas tend to pick up more satellites. The interesting outliers are the [flexible antenna](https://www.sparkfun.com/products/15246) (arguably the largest of all the antennas) and the Pulse W3011 (arguably one of the smallest, best performing antennas).

## FAQ and Troubleshooting

### What's the Difference Between GPS and GNSS?

*GPS* refers to the collection of satellites put into space by the USA. Other countries have their own collection of navigation satellites include Russia (their constellation is called GLONASS), the EU (Galileo), and China (BeiDou). *GNSS* refers to all navigation constellations as a whole. The GNSS Chip Antenna Evaluation Board is capable of receiving signals from any GPS/GLONASS/BeiDou/Galileo satellite transmitting on band 1 (the most common civilian frequency). If your GPS receiver was purchased after 2015 it will probably be capable of picking up most GNSS satellites.

### I'm Not Getting a Lock?!

Are you outside? Do you have a clear, unobstructed view of the sky? These antennas are small and require a very clear view of the sky. They **can not** get a [lock indoors](https://learn.sparkfun.com/tutorials/alphanumeric-gps-wall-clock#lock-problems).

Have you moved outside and are still having problems? Double check that your U.FL connections are seated nicely and orthogonal. You should feel a nice click when the connector is seated properly. Be sure to checkout our tutorial on [using U.FL connectors](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl/all) for more info.

[](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl)

### Three Quick Tips About Using U.FL 

December 28, 2018

Quick tips regarding how to connect, protect, and disconnect U.FL connectors.