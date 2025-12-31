# Source: https://learn.sparkfun.com/tutorials/argos-artic-r2-satellite-communication-guide

## Introduction

Looking for a satellite communication board for your next project? We\'ve got three to pick from!

[![ARGOS Satellite Transceiver Shield - ARTIC R2](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/1/7/17236-Artic_R2_Breakout-01a.jpg)](https://www.sparkfun.com/argos-satellite-transceiver-shield-artic-r2.html)

### [ARGOS Satellite Transceiver Shield - ARTIC R2](https://www.sparkfun.com/argos-satellite-transceiver-shield-artic-r2.html) 

[ SPX-17236 ]

Is your project linked to environmental protection, awareness or study, or to protecting human life? Perhaps you are developi...

**Retired**

[![SparkFun IOTA - Satellite Communication Module (ARTIC R2)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/1/5/8/17984-SparkFun_IOTA_-_Satellite_Communication_Module__ARTIC_R2_-01.jpg)](https://www.sparkfun.com/sparkfun-iota-satellite-communication-module-artic-r2.html)

### [SparkFun IOTA - Satellite Communication Module (ARTIC R2)](https://www.sparkfun.com/sparkfun-iota-satellite-communication-module-artic-r2.html) 

[ SPX-17984 ]

Is your project linked to environmental protection, awareness or study, or to protecting human life? Perhaps you are developi...

**Retired**

[![smôl ARTIC R2](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/1/1/5/18618-smo__l_ARTIC_R2-01.jpg)](https://www.sparkfun.com/smol-artic-r2.html)

### [smôl ARTIC R2](https://www.sparkfun.com/smol-artic-r2.html) 

[ SPX-18618 ]

Our RedBoards are great. But don\'t they sometimes seem a little \*\*\_BIG\_\*\*?! Enter \*\*smôl\*\*, a new range of boards which a...

**Retired**

The [ARGOS Satellite Transceiver Shield - ARTIC R2](https://www.sparkfun.com/products/17236), is the biggest of the three and the easiest to get your fingers around. It has the same footprint as our Feather-compatible Thing Plus boards and is designed to stack directly on top of a Thing Plus for easy development. If you are looking for a board to allow you to get to know how ARGOS satellite communication works, or are just starting out on your product development, or want a board you can plug into breadboard, or are not worried about making your tracking system as compact as possible, then this is the board for you.

[IOTA - the Integrated Open source Transceiver for ARGOS](https://www.sparkfun.com/products/17984) - is ideal if you are ready to incorporate an ARGOS transceiver into your design. Its castellated pads can be reflowed or hand-soldered as required. It also has slots for an RF screening can, should your certification process require one. The antenna connection is available on both a castellated pad and a u.FL connector. You will find an Eagle symbol and footprint for IOTA in the [SparkFun Eagle Libraries](https://github.com/sparkfun/SparkFun-Eagle-Libraries) [RF Library](https://github.com/sparkfun/SparkFun-Eagle-Libraries/blob/main/SparkFun-RF.lbr).

The [smôl ARTIC R2](https://www.sparkfun.com/products/18618) is the baby of the three, but it still packs the same punch as its larger siblings. If you are developing a compact dart for whale tracking, or a small backpack for avian tracking, or a very discrete satellite tracker, then the smôl ARTIC R2 is the one for you.

[![Pictured are the three Spark Fun satellite boards](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/2/1/ARGOS_Comparison_Product_Photo.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/2/1/ARGOS_Comparison_Photo_Tutorial.jpg)

*Having a hard time seeing? Click the image for a closer look.*

[![Pictured are the dimensions of the three Spark Fun satellite boards](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/2/1/Trinity.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/2/1/Trinity.png)

All three boards use the same ARTIC R2 satellite transceiver chip. All three have the same power amplifier, with the same maximum output power and adjustable gain. All three have the same receive sensitivity. All three have on-board flash memory containing the ARTIC R2 firmware and Platform ID. All three are supported by our comprehensive [Arduino Library](https://github.com/sparkfun/SparkFun_ARGOS_ARTIC_R2_Arduino_Library) which includes a full set of tried-and-tested [examples](https://github.com/sparkfun/SparkFun_ARGOS_ARTIC_R2_Arduino_Library/tree/main/examples).

This guide provides background information about the ARGOS satellite system and the ARTIC R2 satellite transceiver chipset. If you are looking for specific information about our three boards, you can open their individual hookup guides by clicking on the buttons below:

[ARGOS ARTIC R2 Shield Hookup Guide](https://learn.sparkfun.com/tutorials/argos-artic-r2-satellite-transceiver-shield-hookup-guide)

[IOTA Satellite Communication Module Hookup Guide](https://learn.sparkfun.com/tutorials/iota-artic-r2-satellite-communication-module-hookup-guide)

[smôl ARTIC R2 Hookup Guide](https://learn.sparkfun.com/tutorials/sml-artic-r2-hookup-guide)

## The ARGOS Satellite System

[![Pictured is the ANGELS satellite](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/2/3/Copyright-David-Ducros-Vue-Angels.jpg)](https://learn.sparkfun.com/tutorials/argos-artic-r2-satellite-communication-guide#credits)

Image credits: Copyright David Ducros

\

The ARGOS satellite system has been around for quite a while. It was created in 1978 by the French Space Agency (CNES), the National Aeronautics and Space Administration (NASA) and the National Oceanic and Atmospheric Administration (NOAA), originally as a scientific tool for collecting and relaying meteorological and oceanographic data around the world. Today, ARGOS is revolutionising satellite communication, adding a constellation of 25 nanosatellites to complement the 6 traditional satellites carrying ARGOS instrumentation. The first of these, ANGELS, is already in operation and SparkFun were among the first users to transmit data to ANGELS in October 2020. When the constellation is complete, there will be a maximum of 10-15 minutes between satellite passes.

ARGOS uses a constellation of Low Earth Orbit (LEO), polar-orbiting satellites to provide worldwide two-way data communication. A global network of terrestrial receiving stations and two data processing centers provide support for continuous, round-the-clock operation.

ARGOS can determine the location of a transmitter using Doppler location. By simply transmitting a unique 28-bit serial number (Platform ID), ARGOS can determine where the transmitter is located without needing GPS / GNSS. This is a big deal since it means the data transmissions can be kept very short, dramatically extending your transmitter\'s battery life. The more times you transmit the better the positioning accuracy becomes, but ARGOS can estimate your position from a single transmission.

ARGOS is also optimized for low power operation. ARGOS transmission (uplink) is centered on 401MHz, towards the bottom end of the Ultra High Frequency (UHF) radio band. The downlink from the satellites is centered on 466MHz. The receivers on the satellites are *very* sensitive, which means that you can transmit using much lower power compared to other satellite systems, again dramatically extending your transmitter\'s battery life. We have seen the satellites reliably receive messages with receive signal strengths as low as -140dBm!

## The Satellites

Here are the details of the seven satellites carrying ARGOS instrumentation:

  Name      Designation    Alternate designation   Launched   Instrumentation
  --------- -------------- ----------------------- ---------- -----------------
  NOAA-K    NK             NOAA-15                 1998       ARGOS-2
  NOAA-N    NN             NOAA-18                 2005       ARGOS-2
  NOAA-P    NP (or NN\')   NOAA-19                 2009       ARGOS-3
  METOP-B   MB                                     2012       ARGOS-3
  METOP-C   MC                                     2018       ARGOS-3
  SARAL     SR                                     2013       ARGOS-3
  ANGELS    A1                                     2019       ARGOS-4 ^\*^

The new kid on the block is ANGELS - Argos NEO Generic Economic Light Satellites. Launched in December 2019, ANGELS A1 became operational for ARGOS data in October 2020. ANGELS is a 12U nanosatellite weighing in at only 20kg! ANGELS is important as it supports ARGOS-4, which supports even lower signal strengths further extending your transmitter\'s battery life. The ANGELS nanosatellite format will be used for the next 25 ARGOS satellites.

^\*^ Note: ANGELS A1 carries ARGOS-NEO (ARGOS-4 Light) instrumentation. It does not support A4 HD and does not have an A4 downlink.

The satellite instrumentation is backwards-compatible. ANGELS supports ARGOS 2, 3 and 4. The METOP satellites support ARGOS 2 and 3.

## Who can use ARGOS?

At the time of writing, the ARGOS system is **currently** limited to programs which are related in some way or other to environmental protection, awareness or study, or to protecting human life.

If your project qualifies, then the ARGOS satellite system and our ARTIC R2 products are the perfect solution. The ARGOS instrumentation on board the satellites is extremely sensitive, meaning that your equipment can transmit ARGOS-4 VLD at 100 mW and even lower, extending your battery life considerably. The power draw of our ARTIC R2 products is *much* lower than equivalent Iridium or Swarm products.

However, the environmental limitations for ARGOS are about to change! Kinéis, heir of the ARGOS System, are in the process of testing a new frequency band between 399.9MHz and 400.05MHz on ANGELS in preparation for the launch of the new constellation of 25 nanosatellites. This new MSS (Mobile Satellite Service) band is ***not restricted*** to environmental programmes. Kinéis will become a true Internet-of-Things communication provider - open to all!

The new 399.9MHz to 400.05MHz band is subject to national certification, and so may not be available in all countries.

It is an exciting time for satellite communication. You may enjoy the following news links:

- [Rocket Lab will deploy the 25 new nanosatellites for Kinéis](https://www.kineis.com/en/rocket-lab-lands-deal-to-launch-entire-iot-satellite-constellation-for-kineis/)
- [Kinéis obtains new licenses in the United States](https://www.kineis.com/en/kineis-obtains-new-licenses-in-the-united-states-and-accelerates-its-development-across-the-atlantic/)
- [ANGELS offers ARGOS 4 VLD](https://www.kineis.com/en/angels-offers-a-new-very-low-data-rate-modulation-for-iot/)

## How much does it cost?

The costs for ARGOS are different if you are a [Regular, Commercial or Individual User](https://www.cls-telemetry.com/wp-content/uploads/2020/03/CLS-Argos-Price-List-2021.pdf) or a [Governmental or Institutional (Educational) User](https://www.cls-telemetry.com/wp-content/uploads/2020/03/CLS-Argos-JTA-Public-Pricelist-2020.pdf). ^**\***^

The currency that the fees are charged in depends on your geographical location. If you are in the USA or Canada, the fees are charged in US Dollars. If you are in Europe, the fees are charged in Euros.

There is a monthly fee per active platform, plus a daily fee for any day on which you transmit. However, the daily fee is capped allowing unlimited monthly usage for a competitive fixed fee - currently: 87 Dollars/Euros per month for Regular, Commercial or Individual users; 63 Dollars/Euros per month for Governmental or Institutional (Educational) users. ^**\***^

You can access your data via ARGOS Web for free, or choose to pay an additional fee to receive your data via email, FTP or SMS.

How does this compare with other service providers? A direct comparison is tricky. Here is one way of looking at the numbers:

- Swarm:
  - A Swarm data plan (750 packets, 192 bytes per packet = 144000 Bytes) costs \$5 USD per month
  - Swarm allows you to stack up to 4 data plans per device (3000 \* 192 = 576000 Bytes) costing \$20 USD per month
  - The cost per 1000 Bytes is \$0.035
- Iridium communication through Rock7:
  - Costs are £12 (GBP) per month line rental plus £0.13 to £0.04 per message credit, depending on how many credits you buy in one go
  - One message credit is charged per 50 bytes sent (or received) - or part thereof
  - Sending 144000 Bytes per month would cost: £12 plus £115.20 (at £0.04 per credit) = £127.20 (approx. \$169)
  - The cost per 1000 Bytes is approx. \$1.17
- ARGOS (Commercial / Individual):
  - ARGOS charge monthly plus daily fees independent of data use
  - A3 HD supports message lengths up to 4636 bytes (see [ARGOS Message Formats](https://learn.sparkfun.com/tutorials/argos-artic-r2-satellite-communication-guide#argos-message-formats) below)
  - Transmitting say ten times per day: 10 \* 4636 bytes per day = 46360 Bytes per day = 1390800 Bytes per month for \$87 per month ^**\***^
  - The cost per 1000 Bytes is approx. \$0.063

^**Notes:\ Exchange\ rates\ and\ prices\ correct\ at\ December\ 2nd\ 2021.\ Prices\ exclude\ taxes.**^

^**\*\ Please\ note\ that\ ARGOS\ pricing\ for\ 2022\ is\ still\ being\ reviewed.\ For\ lower\ transmission\ rate,\ large\ volume\ of\ platforms,\ or\ Proof\ Of\ Concept,\ a\ discount\ may\ apply.**^

## ARTIC R2

The ARTIC R2 is an integrated, low-power, small-size ARGOS 2/3/4 single chip transceiver. ARTIC implements a message based wireless interface. For satellite uplink communication, ARTIC will encode, modulate and transmit provided user messages. For downlink communication, ARTIC will lock to the downstream, demodulate and decode and extract the satellite messages. The ARTIC can transmit signals in frequency bands around 401MHz and receive signals in the bands around 466MHz, in accordance with the ARGOS satellite system specifications.

The ARTIC R2 supports:

- Uplink:
  - ARGOS 2/3/4
- Downlink:
  - ARGOS 3/4

## ARGOS Message Formats

The table below summarizes the properties of each ARGOS message format as supported by the ARTIC R2:

+----------------+-----------+---------------------+-----------------+-----------------+--------------------------+
| Message Format | Mode      | Data Rate           | Min Length      | Max Length      | Notes                    |
|                |           |                     |                 |                 |                          |
|                |           | (bits/sec) ^**\#**^ | (bits) ^**\***^ | (bits) ^**\***^ |                          |
+================+===========+=====================+=================+=================+==========================+
| A2             | ARGOS-2   | 400                 | 52              | 276             |                          |
+----------------+-----------+---------------------+-----------------+-----------------+--------------------------+
| A3             | ARGOS-3   | 400                 | 52              | 276             |                          |
+----------------+-----------+---------------------+-----------------+-----------------+--------------------------+
| ZE             | ARGOS-3   | 400                 | 28              | 28              |                          |
+----------------+-----------+---------------------+-----------------+-----------------+--------------------------+
| A3 HD          | ARGOS-3   | 4800                | 60              | 4636            | HD = High Data rate      |
+----------------+-----------+---------------------+-----------------+-----------------+--------------------------+
| A4 HD          | ARGOS-4   | 4800                | 992             | 4960            | HD = High Data rate      |
+----------------+-----------+---------------------+-----------------+-----------------+--------------------------+
| A4 MD          | ARGOS-4   | 1200                | 480             | 960             | MD = Medium Data rate    |
+----------------+-----------+---------------------+-----------------+-----------------+--------------------------+
| A4 VLD         | ARGOS-4   | 200                 | 28              | 84              | VLD = Very Low Data rate |
+----------------+-----------+---------------------+-----------------+-----------------+--------------------------+

^**\#**^ The data bit rate quoted in the table is the bit rate *before* convolutional encoding (where used)

^**\***^ The message lengths quoted in the table *include* the 28-bit Platform ID but *exclude* the message length identifier or any required tail bits. The ARTIC R2 always calculates and transmits the FEC for A3 HD and the FCS for A4 HD/MD. The quoted maximum message lengths *exclude* the FEC/FCS.

The ARGOS-4 VLD mode is exciting since the uplink can use much lower transmit power (100mW or even less) compared to the other modes. The message are short, including only the 28-bit Platform ID, or the Platform ID plus 56 bits of user data. However, 56-bits is enough to [encode GNSS position (latitude and longitude)](https://learn.sparkfun.com/tutorials/argos-artic-r2-satellite-communication-guide#encoding-latitude-and-longitude) to 4 decimal places and accurate to ±5.55m at the equator.

ARGOS-3 ZE and ARGOS-4 VLD (Short) messages contain *only* the 28-bit Platform ID. ARGOS is still able to calculate the position of the transmitter using Doppler location.

If you want to dig further into the message formats and encoding schemes, they are defined in the CNES *Physical Layer Requirements*:

  Message Format   CNES Physical Layer Requirements
  ---------------- ----------------------------------
  A2               AS3-SP-516-2098-CNES
  A3 + ZE          AS3-SP-516-274-CNES
  A3 HD            AS3-SP-516-273-CNES
  A4 HD/MD         A4-SS-TER-SP-0078-CNES
  A4 VLD           A4-SS-TER-SP-0079-CNES

------------------------------------------------------------------------

**Don\'t Panic!** Our [ARGOS ARTIC R2 Arduino Library](https://github.com/sparkfun/SparkFun_ARGOS_ARTIC_R2_Arduino_Library) does all of the message encoding for you!

------------------------------------------------------------------------

## Satellite Pass Prediction

There are **currently** only seven satellites carrying ARGOS instrumentation. This means that there are frequently times when there are no satellites overhead and that you need to wait until the next satellite rises if you want to avoid wasted transmissions.

Depending on the capacity of your battery, how complex you want your tracker to be, and where you are transmitting from, you may decide that simply hoping there is a satellite overhead when you transmit is the best way forward. However, being able to predict when the next satellite will rise is of course very beneficial.

There are two main ways to do this:

## ARGOS Web

When you log into your ARGOS Web account, you can use the Satellite pass prediction tool to generate a table or spreadsheet of the times of the satellite passes for the coming days. You can generate the table based on a chosen latitude and longitude, or based on the last known location for an individual ARGOS ID.

The Latitude and Longitude are entered in degrees. Longitudes west of the meridian are entered as negative numbers. The prediction tool asks for the altitude (in km) too. You also need to enter the minimum satellite elevation: 5 degrees is a good minimum if you have a clear view to the horizon; for urban or forested areas a higher elevation is sensible.

[![Pictured is the ARGOS Web satellite pass prediction tool](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/2/3/Satellite_Prediction_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/2/3/Satellite_Prediction_1.png)

*Having a hard time seeing? Click the image for a closer look.*

Click on **Simulate**, and the satellite passes are calculated and displayed:

[![Pictured are the satellite pass predictions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/2/3/Satellite_Prediction_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/2/3/Satellite_Prediction_2.png)

*Having a hard time seeing? Click the image for a closer look.*

By default, the table lists the satellite passes in date/time order, but you can choose to list them by satellite, middle (highest) elevation, pass duration etc..

The **Middle date/time** is the date and time when the satellite will be at its highest elevation - the peak of its pass. The time is in UTC (Universal Time Coordinate), you will need to add/subtract your time zone to convert to local time.

The **Middle elevation** indicates how high the satellite will be in the sky at the peak of the pass. Higher passes are of course better.

The **azimuth** data shows the heading where the satellite will rise, peak and set. The azimuth is relative to geographic north, not magnetic north. If your view of the sky is obstructed in a particular direction, you may choose to ignore passes where the middle elevation is low in that direction.

The **Duration** is useful. It indicates how long the satellite pass is from rise to set. Longer durations will allow you to attempt more transmissions. ARGOS transmissions are normally made 90 seconds apart (the \"repetition interval\") with a mandatory ±10% jitter or dither on the interval. On a typical pass, there is usually time for five transmissions. You should not attempt to transmit more frequently than your repetition interval.

------------------------------------------------------------------------

**Don\'t Panic!** Our [ARGOS ARTIC R2 Arduino Library](https://github.com/sparkfun/SparkFun_ARGOS_ARTIC_R2_Arduino_Library) examples handle the repetition interval and jitter/dither for you!

------------------------------------------------------------------------

You will notice that - for 55 degrees north - there is an interval (\'dead zone\') from 12:10 until 17:12 when there are no satellites overhead. That is normal at the moment. When the ANGELS constellation is complete, there will be a maximum of 10-15 minutes between satellite passes.

You can click on the **Export** button to export the data in a variety of formats.

## Pass Prediction Code

Being able to use ARGOS Web to predict the satellite passes is useful, but what if you want your tracker to be able to predict the passes for itself? Never fear! Our [ARGOS ARTIC R2](https://github.com/sparkfun/SparkFun_ARGOS_ARTIC_R2_Arduino_Library) comes to the rescue! Our library contains a pass prediction calculator based on code kindly provided by CLS. If you have included a GPS / GNSS receiver in your tracker project, you can use the latitude, longitude and time to calculate when the next satellite pass will take place. Several of the [library examples](https://github.com/sparkfun/SparkFun_ARGOS_ARTIC_R2_Arduino_Library/tree/main/examples) include pass prediction.

If your tracker will be confined to a particular geographical region, you may not need a GNSS receiver. Knowing the time alone would be enough to predict the next pass.

## AOP (Adapted Orbit Parameters)

The pass prediction code also needs to know the orbit parameters for the satellites in order to predict each pass. You will see the parameters included at the start of the \"WithPrediciton\" examples:

    language:c
    const char AOP[] =      " MA A 5 3 0 2020 10  1 22  7 29  7195.569  98.5114  336.036  -25.341  101.3592   0.00 MB 9 3 0 0 2020 10  1 23 21 58  7195.654  98.7194  331.991  -25.340  101.3604   0.00 MC B 7 3 0 2020 10  1 22 34 23  7195.569  98.6883  344.217  -25.340  101.3587   0.00 15 5 0 0 0 2020 10  1 22 44 11  7180.495  98.7089  308.255  -25.259  101.0408   0.00 18 8 0 0 0 2020 10  1 21 50 32  7225.981  99.0331  354.556  -25.498  102.0000  -0.79 19 C 6 0 0 2020 10  1 22  7  6  7226.365  99.1946  301.174  -25.499  102.0077  -0.54 SR D 4 3 0 2020 10  1 22 33 38  7160.233  98.5416  110.362  -25.154  100.6146  -0.12";

The orbits of the satellites do change or drift over time. The AOP data remains valid for up to six months, but Kinéis recommend updating every 2 to 3 months.

You can download the AOP data from ARGOS Web by clicking the **Download satellite AOP** button on the satellite pass prediction page. You can then copy and paste the AOP data directly into your code.

Alternately, you can download the orbit parameters in JSON format. Click on the **System** button and then click on the **Satellite Allcast Info** option. You will then see an option to download the allcast data.

[![Pictured is the ARGOS Web system button](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/2/3/Satellite_Prediction_3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/2/3/Satellite_Prediction_3.png)

*Having a hard time seeing? Click the image for a closer look.*

[![Pictured is the allcast option](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/2/3/Satellite_Prediction_4.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/2/3/Satellite_Prediction_4.png)

*Having a hard time seeing? Click the image for a closer look.*

[Example 9](https://github.com/sparkfun/SparkFun_ARGOS_ARTIC_R2_Arduino_Library/tree/main/examples/Example9_TestJSONSatellitePassPredictor) in our ARGOS ARTIC R2 library demonstrates how to use the JSON format data. It is heavy on RAM use, so we do not recommend it for Arduino platforms with limited RAM.

The satellites themselves also broadcast their AOP data, so your tracker can update the orbit parameters in the field without needing access to ARGOS Web. [Example 7](https://github.com/sparkfun/SparkFun_ARGOS_ARTIC_R2_Arduino_Library/blob/main/examples/Example7_ContinuousReceiveWithAOPParsing/Example7_ContinuousReceiveWithAOPParsing.ino) in our ARGOS ARTIC R2 library demonstrates how to download the data and record it in the format needed by the pass prediction code.

## Encoding Latitude and Longitude

We normally think of GNSS Latitude and Longitude as both needing 32-bit storage, either as an integer or a floating point value. So, is it possible to send both Latitude and Longitude in the 56-bits available in a single ARGOS-4 VLD (Long) message? Well, yes, of course it is! But you have to be a little bit crafty about how you do it.

------------------------------------------------------------------------

**Thanks!** The following encoding scheme was recommended by Lucas Nicolle at CLS.

------------------------------------------------------------------------

If we want to encode latitude and longitude to four decimal places, giving us an accuracy of ±5.55m at the equator:

- Longitude is in the range ± 0.0000 to 180.0000 degrees
  - If we allocate one bit for the sign (plus/minus or east/west)
  - And if we multiply the longitude by 10000 and turn it into an integer
  - We need 21 binary bits to encode 1800000~10~ (21 bits can encode values up to 2^21^ - 1 = 2097151)
  - Including the sign, we need 22 binary bits to encode the longitude
- Latitude is in the range ± 0.0000 to 90.0000 degrees
  - If we allocate one bit for the sign (plus/minus or north/south)
  - And if we multiply the latitude by 10000 and turn it into an integer
  - We need 20 binary bits to encode 900000~10~ (20 bits can encode values up to 2^20^ - 1 = 1048575)
  - Including the sign, we need 21 binary bits to encode the latitude

We use that same format in our [ARGOS ARTIC R2 Arduino Library examples](https://github.com/sparkfun/SparkFun_ARGOS_ARTIC_R2_Arduino_Library/tree/main/examples). If you ask CLS or Woods Hole Group to apply the **SPARKFUN_GPS** template to your account on ARGOS Web, the latitude, longitude, south and west fields will appear in your data automatically:

[![Pictured are the latitude longitude south and west fields](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/2/3/Satellite_Prediction_5.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/2/3/Satellite_Prediction_5.png)

*Having a hard time seeing? Click the image for a closer look.*

Now, what should we do with those left-over 13 bits!? We\'ll leave that up to you. You might want to encode altitude as m above sea level. 13 bits would allow you to encode altitudes up to 8191m. For high altitude, you might want to encode altitude as 10\'s of m?

## Platform ID

Each ARGOS transmitter has a unique Platform ID number. When you buy an ARGOS ARTIC R2 board from SparkFun, you will receive a card with it which shows:

- Your decimal Platform ID
  - This is used and displayed in ARGOS Web
- The 28-bit hexadecimal Platform ID
  - This is programmed into the ARTIC R2\'s flash memory and used in all transmissions
- The transmission repetition interval
  - The default interval is 90 seconds

You will need to ask CLS / Woods Hole Group to add the Platform ID to your account in order to see your data.

You will need to seek special permission from CLS / Woods Hole Group to use a repetition interval shorter than 90 seconds.

We were instructed by CLS to program the (hexadecimal) Platform ID into flash memory, so that the wrong ID could not be entered into code by accident. (Entering the wrong number has happened - a polar bear that was being tracked via ARGOS suddenly appeared to be in Africa!)

------------------------------------------------------------------------

If you have one of our very first ARGOS ARTIC R2 Transceiver Shields, it may not have the Platform ID programmed into flash memory. For those boards, and only those boards, it is necessary to: request a Platform ID from CLS / Woods Hole Group; use v1.0.9 of the ARGOS ARTIC R2 Arduino Library; and enter the ***HEXADECIMAL*** Platform ID into your code. Please see the [Shield Hookup Guide](https://learn.sparkfun.com/tutorials/argos-artic-r2-satellite-transceiver-shield-hookup-guide#software-setup) for more details.

------------------------------------------------------------------------

## Resources and Going Further

**ARGOS Resources:**

- [The ARGOS System](https://www.argos-system.org/argos/who-we-are/international-cooperation/)
- [How ARGOS works](https://www.argos-system.org/using-argos/how-argos-works/)
- [Register as an ARGOS user](https://www.argos-system.org/become-a-user/)
- [ARGOS Publications and Resources](https://www.argos-system.org/argos-publications/)
- [ARGOS Web Login](https://argos-system.cls.fr/argos-cwi2/login.html)
- [Kinéis IoT everywhere](https://www.kineis.com/en/)
- [ARGOS Chipset Info Sheet](https://cdn.sparkfun.com/assets/2/d/c/6/6/ARGOS-Chipset-Info-sheet.pdf)
- [ARTIC R2 User Datasheet v1.1](https://cdn.sparkfun.com/assets/c/0/8/d/4/ENA303_ARTIC_R2_User_Datasheet_1v10.pdf)

**Arduino Library:**

- [Arduino Examples](https://github.com/sparkfun/SparkFun_ARGOS_ARTIC_R2_Arduino_Library/tree/main/examples)
- [SparkFun ARGOS ARTIC R2 Arduino Library](https://github.com/sparkfun/SparkFun_ARGOS_ARTIC_R2_Arduino_Library)

**SparkFun Hookup Guides:**

[ARGOS ARTIC R2 Shield Hookup Guide](https://learn.sparkfun.com/tutorials/argos-artic-r2-satellite-transceiver-shield-hookup-guide)

[IOTA Satellite Communication Module Hookup Guide](https://learn.sparkfun.com/tutorials/iota-artic-r2-satellite-communication-module-hookup-guide)

[smôl ARTIC R2 Hookup Guide](https://learn.sparkfun.com/tutorials/sml-artic-r2-hookup-guide)