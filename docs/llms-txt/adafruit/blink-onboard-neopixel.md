# Source: https://learn.adafruit.com/getting-started-with-flora/blink-onboard-neopixel.md

# Getting Started with FLORA

## Blink onboard NeoPixel

If you have a Flora v2, your Flora comes with an onboard NeoPixel! This lets you have a nice glowy LED using only one pin (Digital 8)

# Install the NeoPixel Library

If you are running Arduino IDE 1.6.1 or higher, you can install the library using the built in library manager, search for and install **Adafruit\_NeoPixel**

![](https://cdn-learn.adafruit.com/assets/assets/000/025/471/medium800/flora_includelib.png?1431531449)

![](https://cdn-learn.adafruit.com/assets/assets/000/025/472/medium800/flora_neopix.png?1431531546)

Install and close out the Library manager.

[If you're not able to use the library manager or have an older IDE, you can always 'manually' install the library!](../../../../adafruit-neopixel-uberguide)

# Demo Code

Upload the following sketch, note that we consider the 'strip' to be 1 pixel long, and connected to **Digital 8**

```
#include &lt;Adafruit_NeoPixel.h&gt;

#define PIN 8

Adafruit_NeoPixel strip = Adafruit_NeoPixel(1, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();
  strip.setBrightness(50);
  strip.show(); // Initialize all pixels to 'off'
}

void loop() {
  // Some example procedures showing how to display to the pixels:
  colorWipe(strip.Color(255, 0, 0), 500); // Red
  colorWipe(strip.Color(0, 255, 0), 500); // Green
  colorWipe(strip.Color(0, 0, 255), 500); // Blue
  rainbowCycle(20);
}

// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i&lt;strip.numPixels(); i++) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
  }
}

// Slightly different, this makes the rainbow equally distributed throughout
void rainbowCycle(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j&lt;256*5; j++) { // 5 cycles of all colors on wheel
    for(i=0; i&lt; strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) &amp; 255));
    }
    strip.show();
    delay(wait);
  }
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos &lt; 85) {
   return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else if(WheelPos &lt; 170) {
    WheelPos -= 85;
   return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  } else {
   WheelPos -= 170;
   return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  }
}
```

![](https://cdn-learn.adafruit.com/assets/assets/000/025/473/medium800thumb/flora_659-06.gif.pagespeed.ce.4pa4OesOoa.jpg?1448318156)

- [Previous Page](https://learn.adafruit.com/getting-started-with-flora/blink-onboard-led.md)
- [Next Page](https://learn.adafruit.com/getting-started-with-flora/power-your-flora.md)

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
