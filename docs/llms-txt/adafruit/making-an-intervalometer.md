# Source: https://learn.adafruit.com/ir-sensor/making-an-intervalometer.md

# IR Sensor

## Making an Intervalometer

OK now that we can read IR codes, lets make a basic project. The first one we will do is to make an intervalometer. An intervalometer is basically a electronic thingy that makes a camera go off every few minutes or so. This can be used for timelapse projects or kite arial photography or other photo projects.![](https://cdn-learn.adafruit.com/assets/assets/000/000/589/medium800/light_invervalcam.jpeg?1396764320)

The camera we'll be using has an IR remote you can use to set it off (most higher-end cameras have these).![](https://cdn-learn.adafruit.com/assets/assets/000/000/590/medium800/light_canonremote.jpeg?1396764323)

First we will figure out the codes by reading the signal sent when the button is pressed. Then we'll take that data and make the Arduino spit out that code into an IR LED once a minute

OK step one is easy, point the remote control at the IR sensor and press the button, we got the following for our ML-L3 Nikon remote.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/591/medium800/light_canonirread.gif?1447976274)

Looks like the data sent is:

| **PWM ON** | **OFF** |
| 2.0 ms | 27 ms |
| 0.4 ms | 1.5 ms |
| 0.5 ms | 3.5 ms |
| 0.5 ms | 62.2 ms |
| 2.0 ms | 27 ms |
| 0.5 ms | 1.5 ms |
| 0.5 ms | 3.5 ms |
| 0.5 ms |

If you look closely you'll see its actually just

| **PWM ON** | **OFF** |
| 2.0 ms | 27 ms |
| 0.4 ms | 1.5 ms |
| 0.5 ms | 3.5 ms |
| 0.5 ms | 62.2 ms |

sent twice. Sending the same signal twice is very common - doubling up to make sure it gets received

Next up we'll need to connect an IR 940nm LED to the output of the Arduino

![](https://cdn-learn.adafruit.com/assets/assets/000/000/592/medium800/light_intervalometer.gif?1447976285)

Then we'll write a sketch which will pulse pin #13 on and off very fast in the proper code sequence.https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/IR_Sensor/Arduino/Intervalometer/Intervalometer.ino

`void pulseIR(long microsecs)` is our helper procedure, it will create the PWM IR signal like we saw before. I used my scope to fine-tune it so that the delays added up right. We use the not-often-discussed&nbsp;`cli()`and&nbsp;`sei()`procedures to turn off interrupts. The Arduino does a couple things in the background like looking for serial data to read or write, keeping track of time, etc. Most of the time we can just ignore it but for delicate high speed signals like this we want to keep quiet so that we get a nice clean signal

If you look at `SendNikonCode()` you will see the IR command code that we deduced in the previous project by timing the pulses from the IR sensor.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/593/medium800/light_intervalometer.jpeg?1396764351)

We wired this up and it worked great, make sure to point the IR LED at the camera properly.

- [Previous Page](https://learn.adafruit.com/ir-sensor/using-an-ir-sensor.md)
- [Next Page](https://learn.adafruit.com/ir-sensor/reading-ir-commands.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### IR (Infrared) Receiver Sensor

[IR (Infrared) Receiver Sensor](https://www.adafruit.com/product/157)
IR sensor tuned to 38KHz, perfect for receiving commands from a TV remote control. Runs at 3V to 5V so it's great for any microcontroller.  
  
To use, connect pin 3 (all the way to the right) to 5V power, pin 2 (middle) to ground and listen on pin 1. It doesn't do any decoding...

In Stock
[Buy Now](https://www.adafruit.com/product/157)
[Related Guides to the Product](https://learn.adafruit.com/products/157/guides)
### Super-bright 5mm IR LED

[Super-bright 5mm IR LED](https://www.adafruit.com/product/387)
Infrared LEDs are used for remote controls (they're the little LED in the part you point at your TV) and 'night-vision' cameras, and these little blue guys are high powered ones! They are 940nm wavelength, which is what nearly all devices listen to. They're 20 degree beamwidth,...

In Stock
[Buy Now](https://www.adafruit.com/product/387)
[Related Guides to the Product](https://learn.adafruit.com/products/387/guides)
### Mini Remote Control

[Mini Remote Control](https://www.adafruit.com/product/389)
This little remote control would be handy for controlling a robot or other project from across the room. It has 21 buttons and a layout we thought was handy: directional buttons and number entry buttons. The remote uses the NEC encoding type and sends data codes 0 thru 26 (it skips #3, #7,...

In Stock
[Buy Now](https://www.adafruit.com/product/389)
[Related Guides to the Product](https://learn.adafruit.com/products/389/guides)
### Super-bright 5mm IR LED (25 pack)

[Super-bright 5mm IR LED (25 pack)](https://www.adafruit.com/product/388)
Infrared LEDs are used for remote controls (they're the little LED in the part you point at your TV) and 'night-vision' cameras, and these little blue guys are high powered ones! They are 940nm wavelength, which is what nearly all devices listen to. They're 20 degree beamwidth,...

In Stock
[Buy Now](https://www.adafruit.com/product/388)
[Related Guides to the Product](https://learn.adafruit.com/products/388/guides)
### Adafruit METRO 328 - Arduino Compatible - with Headers

[Adafruit METRO 328 - Arduino Compatible - with Headers](https://www.adafruit.com/product/2488)
This is the&nbsp; **Adafruit METRO Arduino-Compatible - with&nbsp;headers.&nbsp;** It's a fully assembled and tested microcontroller and physical computing board with through-hole headers attached.&nbsp; If you don't want a&nbsp;Metro with the headers attached for...

Out of Stock
[Buy Now](https://www.adafruit.com/product/2488)
[Related Guides to the Product](https://learn.adafruit.com/products/2488/guides)

## Related Guides

- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [How to Find Hidden COM Ports](https://learn.adafruit.com/how-to-find-hidden-com-ports.md)
- [WiFi Weather Station](https://learn.adafruit.com/wifi-weather-station-arduino-cc3000.md)
- [Arduino Tips, Tricks, and Techniques](https://learn.adafruit.com/arduino-tips-tricks-and-techniques.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [Motorized Camera Slider MK3 ](https://learn.adafruit.com/motorized-camera-slider-mk3.md)
- [Arduino Ethernet + SD Card](https://learn.adafruit.com/arduino-ethernet-sd-card.md)
- [Adafruit AirLift Shield - ESP32 WiFi Co-Processor](https://learn.adafruit.com/adafruit-airlift-shield-esp32-wifi-co-processor.md)
- [Adalight Project Pack](https://learn.adafruit.com/adalight-diy-ambient-tv-lighting.md)
- [Low Power Coin Cell Voltage Logger](https://learn.adafruit.com/low-power-coin-cell-voltage-logger.md)
- [A REST API for Arduino & the CC3000 WiFi Chip](https://learn.adafruit.com/a-rest-api-for-arduino-and-the-cc3000-wifi-chip.md)
- [8BitBox](https://learn.adafruit.com/8bitbox.md)
- [Mystery Box: NeoMatrix Mk I](https://learn.adafruit.com/mystery-box-neomatrix-mk-i.md)
- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Ladyada's Learn Arduino - Lesson #0](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-0.md)
