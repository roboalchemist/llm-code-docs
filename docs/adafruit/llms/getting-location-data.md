# Source: https://learn.adafruit.com/flora-wearable-gps/getting-location-data.md

# Flora Wearable GPS

## Getting location data

## Detailed GPS Test

Now that we know it basically works, we'll try to get 'fix data' from the GPS. For this, you will have to have the GPS outside. It cannot be inside a building, even if its right at the window. The silver antenna must be pointing up with a clear view of the sky!

![](https://cdn-learn.adafruit.com/assets/assets/000/033/727/medium800/flora_hwparse.png?1468294236)

Wire up the GPS module according to the hookup

![](https://cdn-learn.adafruit.com/assets/assets/000/002/560/medium800/flora_GPSoutside.jpg?1396784508)

[Check your board and serial port settings](http://learn.adafruit.com/getting-started-with-flora/blink-onboard-led) and upload this sketch to your Flora using the Upload button in the IDE.

**Place the GPS module (still connected to the Flora)&nbsp; outside.** Once the GPS has located the satellite data, the red LED on the GPS will stop blinking.

If you see the LED blinking once a second, it does not yet have a fix!

It can take many minutes to get a fix if it doesn't see any satellites immediately.

Once it has a fix, you can check the serial monitor for the GPS data, which includes the current date and time in UTC. It will also give you your latitude, longitude and approximate altitude with the Serial monitor

Danger: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/572/medium800/flora_parsed.gif?1448059620)

Now we know where we are. According to the GPS, my location is **&nbsp;4043.5715 N** (Latitude 40 degrees, 43.5815 minutes North) &&nbsp; **07400.2783 W**. (Longitude 74 degrees, 0.2783 minutes West) To look at this location in Google maps, type&nbsp; **+40°**  **43.5715', -74° 00.2783'** &nbsp;into the&nbsp;[google maps search box](http://maps.google.com/)&nbsp;. Unfortunately gmaps requires you to use +/- instead of NSWE notation. N and E are positive, S and W are negative.

Danger: 

- [Previous Page](https://learn.adafruit.com/flora-wearable-gps/program-flora.md)
- [Next Page](https://learn.adafruit.com/flora-wearable-gps/downloads.md)

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
