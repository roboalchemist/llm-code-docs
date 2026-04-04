# Source: https://learn.adafruit.com/flora-wearable-gps/program-flora.md

# Flora Wearable GPS

## Program FLORA

![](https://cdn-learn.adafruit.com/assets/assets/000/002/556/medium800/flora_program-with-gps.jpg?1396784428)

Make sure the USB cable is connecting your computer and Flora.

## Basic Echo Test
  
We'll start with the most basic test, where we listen to the raw GPS data, to make sure it shows up! Copy and paste this code into a new sketch window and upload it to your Flora  
# Install Adafruit GPS Library

Our helper library will make using the GPS easy since we have working code already. [The library is available on GitHub](https://github.com/adafruit/Adafruit_GPS)

You can download the most recent version from the Arduino library manager.

First, open up the Arduino library manager

![](https://cdn-learn.adafruit.com/assets/assets/000/084/051/medium800/gps_library_manager_menu.png?1573526978)

Search for the&nbsp; **Adafruit GPS** &nbsp;library and install it

![](https://cdn-learn.adafruit.com/assets/assets/000/084/052/medium800/gps.png?1573527037)

We also have a great tutorial on Arduino library installation at:  
http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use

# Load Echo Demo

We'll begin by loading up the HardwareSerial echo test example available in the Adafruit\_GPS library

![](https://cdn-learn.adafruit.com/assets/assets/000/033/726/medium800/flora_hwecho.png?1468294154)

Wire up the GPS module according to the hookup. [Check your board and serial port settings](http://learn.adafruit.com/getting-started-with-flora/blink-onboard-led) and upload this sketch to your Flora using the Upload button in the IDE. Open up the **Serial Monitor.**

You should see something like the following from the serial monitor. You may not have as many numbers, but there should be sentences that start with **$GPRMC** and **$GPGGA** , etc. If you see text like that it means your GPS and connection are working fine.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/568/medium800/flora_rawecho.gif?1448059633)

- [Previous Page](https://learn.adafruit.com/flora-wearable-gps/hook-up-gps.md)
- [Next Page](https://learn.adafruit.com/flora-wearable-gps/getting-location-data.md)

## Featured Products

### FLORA - Wearable electronic platform: Arduino-compatible

[FLORA - Wearable electronic platform: Arduino-compatible](https://www.adafruit.com/product/659)
FLORA is Adafruit's fully-featured wearable electronics platform. It's a round, sewable, Arduino-compatible microcontroller designed to empower amazing wearables projects.FLORA comes with Adafruit's support, [tutorials and...](http://learn.adafruit.com/category/flora)

In Stock
[Buy Now](https://www.adafruit.com/product/659)
[Related Guides to the Product](https://learn.adafruit.com/products/659/guides)
### Flora Wearable Ultimate GPS Module

[Flora Wearable Ultimate GPS Module](https://www.adafruit.com/product/1059)
This module is the best way to add a GPS to your wearable project. It's part of the Adafruit Flora series of wearable electronics, designed specifically for use with the Flora motherboard. Installed on the PCB is the latest of our Ultimate GPS modules, a small, super-thin, low-power GPS...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1059)
[Related Guides to the Product](https://learn.adafruit.com/products/1059/guides)
### Small Alligator Clip Test Lead (set of 12)

[Small Alligator Clip Test Lead (set of 12)](https://www.adafruit.com/product/1008)
Connect this to that without soldering using these handy mini alligator clip test leads. 15" cables with alligator clip on each end, color coded. You get 12 pieces in 6 colors. Strong and grippy, these always come in handy! We often use these in conjunction with a multimeter so we...

In Stock
[Buy Now](https://www.adafruit.com/product/1008)
[Related Guides to the Product](https://learn.adafruit.com/products/1008/guides)
### Getting Started with Adafruit FLORA

[Getting Started with Adafruit FLORA](https://www.adafruit.com/product/1839)
 **Making Wearables with an Arduino-Compatible Electronics Platform**  
  
This book introduces readers to building wearable electronics projects using Adafruit's tiny FLORA board: at 4.4 grams, and only 1.75 inches in diameter, and featuring Arduino compatibility, it's the...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1839)
[Related Guides to the Product](https://learn.adafruit.com/products/1839/guides)
### Getting Started with Adafruit FLORA Book Pack

[Getting Started with Adafruit FLORA Book Pack](https://www.adafruit.com/product/2404)
Pickup a copy of&nbsp;[Getting Started with Adafruit FLORA](https://www.adafruit.com/products/1839)&nbsp;and then hit the ground running with everything that you need to become an [Adafruit FLORA](https://www.adafruit.com/products/659) supreme being!

This pack is...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2404)
[Related Guides to the Product](https://learn.adafruit.com/products/2404/guides)
### FLORA GPS Starter Pack

[FLORA GPS Starter Pack](https://www.adafruit.com/product/1090)
Get started with the fabulous Adafruit Flora platform with this lovely starter kit. Included are plenty of parts to make a few different fun projects! There's a Flora motherboard, a GPS module that can also perform location datalogging, eight ultra-bright chainable RGB pixels, a battery...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1090)
[Related Guides to the Product](https://learn.adafruit.com/products/1090/guides)
### FLORA Sensor Pack

[FLORA Sensor Pack](https://www.adafruit.com/product/1458)
Sense the world around you! The FLORA Sensor Pack includes many types of sensors for your wearable enjoyment. Sense motion, direction, color, light levels, touch, and connections with FLORA sensor breakouts and conductive materials, and a few NeoPixels for experimenting with displaying your...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1458)
[Related Guides to the Product](https://learn.adafruit.com/products/1458/guides)
### FLORA Budget Pack

[FLORA Budget Pack](https://www.adafruit.com/product/1405)
Get started with the fabulous Adafruit Flora platform with this lovely budget kit, just enough to get you started with this fun wearable computer. Included are enough parts to make your first wearable electronic project. There's a Flora motherboard, four ultra-bright chainable RGB pixels,...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1405)
[Related Guides to the Product](https://learn.adafruit.com/products/1405/guides)

## Related Guides

- [FLORA TV-B-Gone](https://learn.adafruit.com/flora-tv-b-gone.md)
- [Zipper Switch](https://learn.adafruit.com/zipper-switch.md)
- [Flora GPS Jacket](https://learn.adafruit.com/flora-gps-jacket.md)
- [Getting Started with FLORA](https://learn.adafruit.com/getting-started-with-flora.md)
- [NeoPixel Ring Clock](https://learn.adafruit.com/neopixel-ring-clock.md)
- [SMSsenger Bag](https://learn.adafruit.com/smssenger-bag.md)
- [VU Meter Baseball Hat](https://learn.adafruit.com/vu-meter-baseball-hat.md)
- [Sparkle Skirt](https://learn.adafruit.com/sparkle-skirt.md)
- [Citi Bike Helmet](https://learn.adafruit.com/citi-bike-helmet.md)
- [Flora MIDI Drum Glove](https://learn.adafruit.com/midi-drum-glove.md)
- [Haptic Headband](https://learn.adafruit.com/haptic-headband.md)
- [Mailbox Notification Service](https://learn.adafruit.com/mailbox-notification-service.md)
- [LED Stego Flex Spike Hoodie](https://learn.adafruit.com/led-stego-flex-spike-hoodie.md)
- [Sunscreen Reminder Hat](https://learn.adafruit.com/sunscreen-reminder-hat.md)
- [Custom Milled PCB Pins](https://learn.adafruit.com/custom-milled-pcb-pins.md)
