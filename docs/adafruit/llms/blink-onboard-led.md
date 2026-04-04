# Source: https://learn.adafruit.com/getting-started-with-flora/blink-onboard-led.md

# Getting Started with FLORA

## Blink onboard LED

![](https://cdn-learn.adafruit.com/assets/assets/000/002/537/medium800/flora_659USB_orig.jpg?1396784206)

Next it's time to load up a program on your FLORA. There is an LED on board, so let's blink it! Plug in the USB cable and paste the following code into the Adafruit Flora IDE:

```
// Pin D7 has an LED connected on FLORA.
// give it a name:
int led = 7;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);               // wait for a second
}
```

![](https://cdn-learn.adafruit.com/assets/assets/000/002/540/medium800/flora_Screen_Shot_2012-11-08_at_12.47.41_PM.png?1396784161)

From the Tools menu, under "Board," choose "Adafruit Flora"

![](https://cdn-learn.adafruit.com/assets/assets/000/002/541/medium800/flora_Screen_Shot_2012-11-08_at_12.47.51_PM.png?1396784242)

Also in the Tools menu, under "Serial Port," choose the one that contains the phrase "usbmodem" if you have a Mac.  
&nbsp;  
If you're using a Windows computer, it will be named **COM** something, but not COM1 or COM2 (so it will be whatever comes after those two if they exist, such as COM3 or COM4).

![](https://cdn-learn.adafruit.com/assets/assets/000/002/542/medium800/flora_uploadcode.jpg?1396784249)

Press the Upload button to transmit the program to the FLORA. It looks like an arrow pointing to the right.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/538/medium800/flora_LED-blinks.jpg?1396784218)

That's it! The on board LED marked "D7" should blink on and off repeatedly, and you've successfully programmed your FLORA!

- [Previous Page](https://learn.adafruit.com/getting-started-with-flora/download-software.md)
- [Next Page](https://learn.adafruit.com/getting-started-with-flora/blink-onboard-neopixel.md)

## Featured Products

### FLORA - Wearable electronic platform: Arduino-compatible

[FLORA - Wearable electronic platform: Arduino-compatible](https://www.adafruit.com/product/659)
FLORA is Adafruit's fully-featured wearable electronics platform. It's a round, sewable, Arduino-compatible microcontroller designed to empower amazing wearables projects.FLORA comes with Adafruit's support, [tutorials and...](http://learn.adafruit.com/category/flora)

In Stock
[Buy Now](https://www.adafruit.com/product/659)
[Related Guides to the Product](https://learn.adafruit.com/products/659/guides)
### 3 x AAA Battery Holder with On/Off Switch and 2-Pin JST

[3 x AAA Battery Holder with On/Off Switch and 2-Pin JST](https://www.adafruit.com/product/727)
This battery holder connects 3 AAA batteries together in series for powering all kinds of projects. We spec'd these out because the box is slim, and 3 AAA's add up to about 3.3-4.5V, a very similar range to Lithium Ion/polymer (Li-Ion) batteries and have an on-off switch. That makes...

In Stock
[Buy Now](https://www.adafruit.com/product/727)
[Related Guides to the Product](https://learn.adafruit.com/products/727/guides)
### USB cable - USB A to Micro-B

[USB cable - USB A to Micro-B](https://www.adafruit.com/product/592)
This here is your standard A to micro-B USB cable, for USB 1.1 or 2.0. Perfect for connecting a PC to your Metro, Feather, Raspberry Pi or other dev-board or microcontroller

Approximately 3 feet / 1 meter long

In Stock
[Buy Now](https://www.adafruit.com/product/592)
[Related Guides to the Product](https://learn.adafruit.com/products/592/guides)
### Getting Started with Adafruit FLORA Book Pack

[Getting Started with Adafruit FLORA Book Pack](https://www.adafruit.com/product/2404)
Pickup a copy of&nbsp;[Getting Started with Adafruit FLORA](https://www.adafruit.com/products/1839)&nbsp;and then hit the ground running with everything that you need to become an [Adafruit FLORA](https://www.adafruit.com/products/659) supreme being!

This pack is...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2404)
[Related Guides to the Product](https://learn.adafruit.com/products/2404/guides)
### Getting Started with Adafruit FLORA

[Getting Started with Adafruit FLORA](https://www.adafruit.com/product/1839)
 **Making Wearables with an Arduino-Compatible Electronics Platform**  
  
This book introduces readers to building wearable electronics projects using Adafruit's tiny FLORA board: at 4.4 grams, and only 1.75 inches in diameter, and featuring Arduino compatibility, it's the...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1839)
[Related Guides to the Product](https://learn.adafruit.com/products/1839/guides)
### FLORA Budget Pack

[FLORA Budget Pack](https://www.adafruit.com/product/1405)
Get started with the fabulous Adafruit Flora platform with this lovely budget kit, just enough to get you started with this fun wearable computer. Included are enough parts to make your first wearable electronic project. There's a Flora motherboard, four ultra-bright chainable RGB pixels,...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1405)
[Related Guides to the Product](https://learn.adafruit.com/products/1405/guides)
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

## Related Guides

- [Datalogging Hat with FLORA BLE](https://learn.adafruit.com/datalogging-hat-with-flora-ble.md)
- [Experimenting with NeverWet + Electronics](https://learn.adafruit.com/neverwet-electronics.md)
- [Flora GPS Jacket](https://learn.adafruit.com/flora-gps-jacket.md)
- [SMSsenger Bag](https://learn.adafruit.com/smssenger-bag.md)
- [Conductive Thread](https://learn.adafruit.com/conductive-thread.md)
- [3D Printed Wireless MIDI Controller Guitar](https://learn.adafruit.com/ez-key-wireless-midi-controller-guitar.md)
- [Mailbox Notification Service](https://learn.adafruit.com/mailbox-notification-service.md)
- [GPS Logging Dog Harness](https://learn.adafruit.com/gps-logging-dog-harness.md)
- [NeoPixel Matrix Snowflake Sweater](https://learn.adafruit.com/neopixel-matrix-snowflake-sweater.md)
- [Chameleon Scarf](https://learn.adafruit.com/chameleon-scarf.md)
- [Adafruit Arduino Selection Guide](https://learn.adafruit.com/adafruit-arduino-selection-guide.md)
- [Citi Bike Helmet](https://learn.adafruit.com/citi-bike-helmet.md)
- [FLORA TV-B-Gone](https://learn.adafruit.com/flora-tv-b-gone.md)
- [Flora Wearable GPS](https://learn.adafruit.com/flora-wearable-gps.md)
- [Flora Accelerometer](https://learn.adafruit.com/flora-accelerometer.md)
