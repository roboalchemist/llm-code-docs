# Source: https://learn.sparkfun.com/tutorials/what-is-gps-rtk

## Real Time Kinematics

RTK is short for **real time kinematics**. A GPS receiver capable of RTK takes in the normal signals from the Global Navigation Satellite Systems along with a correction stream to achieve 1cm positional accuracy. GNSS includes satellites from GPS (USA), GLONASS (Russia), Beidou (China), and Galileo (Europe). On top of these signals an RTK receiver takes in an RTCM correction stream and then calculates your location with 1cm accuracy in real time. The rate varies between receivers but most will output a solution at least once per second; some receivers can output this higher precision solution up to 20 times a second. RTK capable GPS receivers used to be thousands of dollars and were limited to professional surveyors and government groups. Thanks to science, math, and economics, RTK receivers are now less than \$300.

[![SparkFun GPS-RTK-SMA Breakout - ZED-F9P (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/3/5/2/16481-SparkFun_GPS-RTK-SMA_Breakout_-_ZED-F9P__Qwiic_-01a.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk-sma-breakout-zed-f9p-qwiic.html)

### [SparkFun GPS-RTK-SMA Breakout - ZED-F9P (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk-sma-breakout-zed-f9p-qwiic.html) 

[ GPS-16481 ]

The SparkFun GPS-RTK-SMA raises the bar for high-precision GPS and is the latest in a line of powerful RTK boards featuring t...

[ [\$259.95] ]

[![SparkFun GPS-RTK2 Board - ZED-F9P (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/5/1/4/15136-SparkFun_GPS-RTK2_Board_-_ZED-F9P__Qwiic_-03.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk2-board-zed-f9p-qwiic-gps-15136.html)

### [SparkFun GPS-RTK2 Board - ZED-F9P (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk2-board-zed-f9p-qwiic-gps-15136.html) 

[ GPS-15136 ]

The SparkFun GPS-RTK2 is a powerful breakout for the ZED-F9P module. The ZED-F9P is a top-of-the-line module for GNSS & GPS s...

[ [\$259.95] ]

[![SparkFun GPS-RTK Board - NEO-M8P-2 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/3/2/0/15005-SparkFun_GPS-RTK__Qwiic__-_NEO-M8P-2-00.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk-board-neo-m8p-2-qwiic.html)

### [SparkFun GPS-RTK Board - NEO-M8P-2 (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk-board-neo-m8p-2-qwiic.html) 

[ GPS-15005 ]

The SparkFun GPS-RTK Board is a powerful breakout for the NEO-M8P-2 module from u-blox. The NEO-M8P-2 is a top-of-the-line mo...

[\$269.95] [ [\$179.95] ]

[![SparkFun MicroMod GNSS Carrier Board (ZED-F9P)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/8/3/0/17722-SparkFun_MicroMod_GNSS_Carrier_Board__ZED-F9P_-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-gnss-carrier-board-zed-f9p.html)

### [SparkFun MicroMod GNSS Carrier Board (ZED-F9P)](https://www.sparkfun.com/sparkfun-micromod-gnss-carrier-board-zed-f9p.html) 

[ GPS-17722 ]

The SparkFun MicroMod GNSS carrier board has the accuracy of GNSS Real Time Kinematics (RTK) with the flexibility of the Micr...

[ [\$269.95] ]

[![SparkFun RTK Facet L-Band](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/7/4/6/20000-SparkFun_RTK_Facet_L-Band-04.jpg)](https://www.sparkfun.com/sparkfun-rtk-facet-l-band.html)

### [SparkFun RTK Facet L-Band](https://www.sparkfun.com/sparkfun-rtk-facet-l-band.html) 

[ GPS-20000 ]

The RTK Facet L-Band is your one-stop shop for high precision geolocation and surveying needs without needing a Base or Rover...

**Retired**

[![SparkFun RTK Express](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/8/7/7/18019-SparkFun_RTK_Express-09.jpg)](https://www.sparkfun.com/sparkfun-rtk-express.html)

### [SparkFun RTK Express](https://www.sparkfun.com/sparkfun-rtk-express.html) 

[ GPS-18442 ]

The SparkFun RTK Express is an easy to use GNSS receiver for centimeter-level positioning. Perfect for surveying, logging, an...

[ [\$534.95] ]

On the left we have a extremely high quality GPS receiver (the [ZED-F9P](https://www.sparkfun.com/products/15136) seen above) with no correction data. The position wanders greatly over 1.5 meters and beyond. On the right the same receiver, with the same antenna, with RTCM correction data brings the position under 25cm with tight groupings under 10cm.

[![GPS with and without RTCM Data correction](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/3/Location-Wandering-GPS-combined.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/3/Location-Wandering-GPS-combined.jpg)

### Did You Say 1 *cm*? Zomg How Do I Get 1 cm Accuracy!?

You\'ll need a GPS receiver capable of receiving and incorporating the RTCM correction data into its location solution. You'll also need a source of RTCM correction data. This usually comes from an internet connection or a long distance radio capable of approximately 500 bytes per second. LoRa and LTE-CAT M1 are superb choices for this backhaul.

Once it\'s all setup and working, the rover GPS module will output normal NMEA sentences but with *really* accurate lat and long. To be clear, it's not 1cm precision; it\'s 1cm *accuracy*. The precision is 0.1mm!

1 cm accuracy is also possible with a few lower cost receivers (such as the NEO-M8T) by capturing raw streams from the GPS satellites and then post processing the logs with an open source program called [RTKLIB](http://www.rtklib.com/). This is handy for applications like aerial photography and agricultural inspection where alignment is important after the fact. It\'s also possible to tether a lower cost receiver (such as the NEO-M8T) to a laptop and run RTKLIB in unison and achieve real time solutions but this is a rather large, power hungry setup that is not ideal for embedded mobile applications. In these tutorials we will be focusing on real time (RTK) capable receivers.

## What is RTCM?

RTCM is an acronym for **R**adio **T**echnical **C**ommission for **M**aritime. This governmental body came up with a way to communicate positions for boats and other vessels many decades ago. Technically, RTCM is just a protocol. We, however, will be using the term *RTCM* to mean the bytes of correction data related to GPS timing anomalies.

[![TRCM Protocol Message Structure](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/3/RTCM_3_Format_with_Preamble.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/3/RTCM_3_Format_with_Preamble.jpg)

*From [Review of GNSS Formats for Real-Time Positioning](https://www.researchgate.net/profile/Eldar_Rubinov/publication/268403391_Review_of_GNSS_Formats_for_Real-Time_Positioning/links/546f3db00cf2d67fc0310356/Review-of-GNSS-Formats-for-Real-Time-Positioning.pdf) and [Geo++](http://www.geopp.com/pdf/gppigs06_rtcm_f.pdf)*

The contents of RTCM frames can be decoded but you, the user, rarely need to. Instead you simply pass the bytes to the GPS receiver and it will parse the correction data.

There are a few different types of messages but the ones we care about are numbers 1005, 1077, 1087, and 1230. Each message type has a different length but as a rule of thumb it\'s a couple hundred bytes every second. Each RTCM message contains details about the GPS/GNSS network, and perturbations in the ionosphere and troposphere.

Remember, the GPS satellites are *very* far away; about 20,000km or 12,000 miles away. A lot can happen to the signal from the GPS satellites to you across that distance. Geomagnetic storms cause slight timing delays increasing the location error. Earth\'s gravitational field is not uniform so relativistic effects can add inaccuracies. If we know the second to second issues within our local vicinity, a RTCM capable receiver can correct the location solution with great precision.

**Note:** There are a few different versions of RTCM. The most popular versions are v2 and v3. Because v3 is considered an 'open' standard, and because it incorporates messages helpful for RTK, more companies have implemented version 3 making it the more common standard.

## Where Do I Get RTCM Corrections?

There\'s the not-free but super easy solution, and there\'s the freeway.

### Not-Free: Skylark

[![Skylark Coverage maps](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/3/Skylark-Coverage.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/3/Skylark-Coverage.png)

*Skylark coverage maps*

A company called SwiftNav offers a service called [Skylark](https://www.swiftnav.com/skylark). As of writing, for \$49 per month you will get corrections covering North America, Europe, and Asia Pacific. You\'ll be issued NTRIP credentials that can immediately be used with Lefebure, SW Maps, or any GIS app that supports NTRIP. One downside is that with a \'regional\' provider such as Skylark the distance to the correction station may be larger than 10km. While we\'ve *always* gotten an RTK fix, we often see accuracy of \~30mm instead of the 14mm when using our own [GNSS reference station](https://learn.sparkfun.com/tutorials/how-to-build-a-diy-gnss-reference-station/all). Your mileage may vary.

### Sort Of Free: Build You Own

[![SparkFun RTK Base Station](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/3/Roof_Enclosure.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/3/Roof_Enclosure.jpg)

*The SparkFun RTK Base Station complete with an NTRIP internet connection and a 915MHz RF connection*

[![RTK SMA transmitting RTCM over Qwiic to ESP32 Thing Plus](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/3/SparkFun_ESP32_Server_-_RTCM_connected_over_Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/3/SparkFun_ESP32_Server_-_RTCM_connected_over_Qwiic.jpg)

*SparkFun GPS RTK transmitting RTCM over Qwiic to ESP32 Thing Plus*

You can [build your own GNSS reference station](https://learn.sparkfun.com/tutorials/how-to-build-a-diy-gnss-reference-station/all#introduction). It takes some work, some hardware, and you\'ll need to stay^1^ within 10km, but there\'s no annual fee and you\'ll have control over your own system. Additionally, we get a very good reported horizontal accuracy of 14mm in RTK Fix mode.

^1^ As the distance to a reference station passes 10km the accuracy of the RTK fix [increases by a few centimeters](https://www.hindawi.com/journals/js/2019/3572605/).

### Free: UNAVCO

If you\'re lucky there\'s a station within 10km (6 miles) of you that is broadcasting RTCM 3.x data over the internet. We located one a little more than 10 km from SparkFun HQ that works really well.

[![TRCM Base Station](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/3/RTCM_Station_Distance_more_than_10km.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/3/RTCM_Station_Distance_more_than_10km.jpg)

Here's a list of stations we've found. If there are more that you know of, please let us know:

- [UNAVCO](http://www.unavco.org/instrumentation/networks/status/all/realtime) - Mostly USA
- [NTRIP Listing](https://igs.bkg.bund.de/root_ftp/NTRIP/streams/streamlist_world-wide.htm) - Global
- [European Reference Stations](http://www.epncb.oma.be/_networkdata/data_access/real_time/map.php)
- [RTK2go](http://www.rtk2go.com/) and [SNIP](https://www.use-snip.com/kb/knowledge-base/an-open-ntrip-caster/) - Runs a server where a few dozen stations can be accessed (see comments section)

Many of the stations that broadcast real time RTCM correction data require registration. It's a wild hodge-podge of scientific and non-profit civil organizations across the globe. It feels very internet-circa-1995. If anyone has a more straightforward way of discovering and connecting to RTCM providers, please let us know in the comments section.

We recommend using [RTKLIB](http://www.rtklib.com/) to subscribe to the feed and output the stream over a serial port to a GPS RTK capable module. For the best accuracy, your GPS receiver will need to be within 10km (6 miles) of the broadcast station. If you are greater than 10km, the ZED-F9P can still create a location fixed but the accuracy is degraded and the receiver will output the following:

    WARNING: DGNSS baseline big: 10km

## How Do I Get the RTCM Messages to the GPS Receiver?

It depends on your end application. If you need maximum portability, then the best solution is a radio link between base station you\'ve created and mobile GPS RTK receiver. SparkFun offers a variety of [LoRa radios and antennas](https://www.sparkfun.com/categories/410) to enable this backhaul like some of the products listed below.

[![SparkFun MicroMod LoRa Function Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/0/4/0/18573-SparkFun_MicroMod_LoRa_Function_Board-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-lora-function-board.html)

### [SparkFun MicroMod LoRa Function Board](https://www.sparkfun.com/sparkfun-micromod-lora-function-board.html) 

[ WRL-18573 ]

The SparkFun MicroMod LoRa Function Board provides LoRA and LoRaWAN capabilities to your MicroMod project.

**Retired**

[![SparkFun LoRa Gateway - 1-Channel (ESP32)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/3/8/8/18074-SparkFun_LoRa_Gateway_-_1-Channel__ESP32_-01.jpg)](https://www.sparkfun.com/sparkfun-lora-gateway-1-channel-esp32.html)

### [SparkFun LoRa Gateway - 1-Channel (ESP32)](https://www.sparkfun.com/sparkfun-lora-gateway-1-channel-esp32.html) 

[ WRL-18074 ]

The SparkFun 1-Channel LoRa Gateway is a powerful 3-network capable device thanks to an onboard ESP32 WROOM module and an RFM...

**Retired**

[![LoRa 1W Breakout - 915M30S](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/0/3/8/18572-LoRa_1W_Breakout_-_915M30S-01.jpg)](https://www.sparkfun.com/lora-1w-breakout-915m30s.html)

### [LoRa 1W Breakout - 915M30S](https://www.sparkfun.com/lora-1w-breakout-915m30s.html) 

[ SPX-18572 ]

Do you need power? This breakout for the 915M30S module from EBYTE is a 1W (30dBm) LoRa transceiver. LoRa is great for long r...

[ [\$29.95] ]

If your end application already requires an Internet connection such as GSM or LTE-CAT, then a serial connection to the GPS-RTK receiver may be the easiest way to go.

If your application has a cell phone nearby then a third option is to create a serial bridge from a cell phone to a serial Bluetooth device like the [Bluetooth Mate Silver](https://www.sparkfun.com/products/12576) that then connects to the serial port on the GPS-RTK. There are a few NTRIP compatible mobile apps. We've been pleased with [Lefebure](https://play.google.com/store/apps/details?id=com.lefebure.ntripclient) for Android.