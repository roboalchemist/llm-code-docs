# Source: https://learn.adafruit.com/ir-sensor/using-an-ir-sensor.md

# IR Sensor

## Using an IR Sensor

The good news is that it is very easy to hook up this sensor. Just connect the output to a digital pin. The bad news is that the Arduino's friendly&nbsp;**digitalRead()**&nbsp;procedure is a tad too slow to reliably read the fast signal as its coming in. Thus we use the hardware pin reading function directly from pin D2, that's what the line "IRpin\_PIN&nbsp;& BV(IRpin))" does. This trick is specific to ATmega328 based boards such as Arduino Uno, Adafruit Metro, etc.

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
![Angled shot of a Adafruit METRO 328 Fully Assembled](https://cdn-shop.adafruit.com/640x480/50-09.jpg)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/555/medium800/light_arduinopna4602.gif?1447976120)

https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/IR_Sensor/Arduino/Raw_IR/Raw_IR.ino

If you run this while pointing a Sony IR remote and pressing the ON button you will get the following...![](https://cdn-learn.adafruit.com/assets/assets/000/000/556/medium800/light_sonyread.gif?1447976130)

If you ignore the first OFF pulse (its just the time from when the Arduino turned on to the first IR signal received) and the last ON pulse (it the beginning of the next code) you'll find the Sony power code:| **PWM ON** | **OFF** |
| 2.5 ms | 0.6 ms |
| 1.2 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 1.2 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 1.2 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 1.2 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 0.6 ms | 27.2 ms |

- [Previous Page](https://learn.adafruit.com/ir-sensor/ir-remote-signals.md)
- [Next Page](https://learn.adafruit.com/ir-sensor/making-an-intervalometer.md)

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
