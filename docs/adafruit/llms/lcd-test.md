# Source: https://learn.adafruit.com/2-8-tft-touchscreen/lcd-test.md

# Source: https://learn.adafruit.com/2-8-tft-touch-shield/lcd-test.md

# 2.8" TFT Touch Shield

## LCD Test

We have a library with example code ready to go for use with these TFTs. The library is not incredibly fast and optimized but its a good start and can easily be ported to other micrcontrollers. However, we'll assume you're using an Arduino.  
  
_Two_&nbsp;libraries need to be downloaded and installed: the&nbsp;[TFTLCD library](https://github.com/adafruit/TFTLCD-Library)&nbsp;and the&nbsp;[GFX library.](https://github.com/adafruit/Adafruit-GFX-Library)&nbsp;You can install these libraries through the Arduino library manager.

Open up the Arduino library manager:

![](https://cdn-learn.adafruit.com/assets/assets/000/084/302/medium800/arduino_compatibles_library_manager_menu.png?1573836935)

Search for the&nbsp; **Adafruit GFX&nbsp;** library and install it:

![](https://cdn-learn.adafruit.com/assets/assets/000/084/303/medium800/arduino_compatibles_gfx.png?1573836968)

If using an older Arduino IDE (pre-1.8.10), do the same for&nbsp; **Adafruit\_BusIO** &nbsp;(newer versions do this one automatically).

Then search for the&nbsp; **Adafruit TFTLCD&nbsp;** library and install it:

![](https://cdn-learn.adafruit.com/assets/assets/000/086/810/medium800/arduino_compatibles_tftlcd.png?1578606675)

We also have a great tutorial on Arduino library installation at:  
[http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use](http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use "Link: http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use")

Danger: 

```
//comment or uncomment the next line for special pinout! 
#define USE_ADAFRUIT_SHIELD_PINOUT
```

Restart the Arduino software. You should see a new **example** folder called **TFTLCD** and inside, an example called **graphicstest**. Upload that sketch to your Arduino. You should see a collection of graphical tests draw out on the TFT.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/797/medium800/lcds___displays_lines.jpg?1396787150)

- [Previous Page](https://learn.adafruit.com/2-8-tft-touch-shield/connect.md)
- [Next Page](https://learn.adafruit.com/2-8-tft-touch-shield/adafruit-gfx-library.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [LED Lightbox](https://learn.adafruit.com/led-lightbox.md)
- [Trinket Audio Player](https://learn.adafruit.com/trinket-audio-player.md)
- [Geofencing with the FONA 808 & Adafruit IO](https://learn.adafruit.com/geofencing-with-the-fona-808-and-adafruit-io.md)
- [Adafruit Analog Accelerometer Breakouts](https://learn.adafruit.com/adafruit-analog-accelerometer-breakouts.md)
- [Electronic Demon Costume](https://learn.adafruit.com/electronic-demon-costume.md)
- [Adafruit Ultimate GPS Logger Shield](https://learn.adafruit.com/adafruit-ultimate-gps-logger-shield.md)
- [Mini Thermal Receipt Printers](https://learn.adafruit.com/mini-thermal-receipt-printer.md)
- [Bluefruit LE Connect for iOS and Android](https://learn.adafruit.com/bluefruit-le-connect.md)
- [Introducing Adafruit Trellis ](https://learn.adafruit.com/adafruit-trellis-diy-open-source-led-keypad.md)
- [Arduino Lesson 9. Sensing Light](https://learn.adafruit.com/adafruit-arduino-lesson-9-sensing-light.md)
- [36mm LED Pixels](https://learn.adafruit.com/36mm-led-pixels.md)
- [Adafruit 16-channel PWM/Servo Shield](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield.md)
- [Naughty or Nice Machine](https://learn.adafruit.com/naughty-or-nice-machine.md)
- [Wireless Gardening with Arduino + CC3000 WiFi Modules](https://learn.adafruit.com/wireless-gardening-arduino-cc3000-wifi-modules.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
