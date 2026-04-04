# Source: https://learn.adafruit.com/2-8-tft-touchscreen/touchscreen.md

# 2.8" TFT Touchscreen

## Touchscreen

Danger: 

The LCD has a 2.8" 4-wire resistive touch screen glued onto it. You can use this for detecing finger-presses, stylus', etc. You'll need 4 pins to talk to the touch panel **but** you can **reuse** some of the pins for the TFT LCD! This is because the resistance of the panel is high enough that it doesn't interfere with the digital input/output and we can query the panel in between TFT accesses, when the pins are not being used.  
  
You can wire up the 4 remaining pins as follows. the one on the very left ( **Y-** orange) can connect to digital **9** , the next one over ( **X-** green) connects to **Analog 2** , The next one over ( **Y+** blue) connects to **Analog 3** and the last one ( **X+** gray) connects to digital **8**. The X- and Y+ pins pretty much have to connect to those analog pins (or to analog 4/5) but Y-/X+ can connect to any digital or analog pins.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/046/medium800/lcds___displays_touchwire.jpg?1396790601)

# Download Library

Begin by opening up the Arduino library manager

![](https://cdn-learn.adafruit.com/assets/assets/000/084/057/medium800/graphic_lcds_library_manager_menu.png?1573528610)

Search for the&nbsp; **Adafruit TouchScreen** &nbsp;library and install it

![](https://cdn-learn.adafruit.com/assets/assets/000/084/058/medium800/graphic_lcds_touchscreen.png?1573528630)

We also have a great tutorial on Arduino library installation at:  
[http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use](http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use "Link: http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use")

Now start up the **tftpaint** example in the Arduino library. The right hand side will have 'color boxes' you can press to select which color you want to draw with. If you press the area to the **left** where the screen ends, it will erase the screen.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/047/medium800/lcds___displays_paint.jpg?1396790611)

You can use your fingertip to draw.![](https://cdn-learn.adafruit.com/assets/assets/000/003/048/medium800/lcds___displays_helloworld.jpg?1396790617)

![](https://cdn-learn.adafruit.com/assets/assets/000/003/049/medium800/lcds___displays_star.jpg?1396790626)

![](https://cdn-learn.adafruit.com/assets/assets/000/003/050/medium800/lcds___displays_heart.jpg?1396790636)

If you press the area to the **left** where the screen ends, it will erase the screen.

- [Previous Page](https://learn.adafruit.com/2-8-tft-touchscreen/graphics-library.md)
- [Next Page](https://learn.adafruit.com/2-8-tft-touchscreen/bitmaps.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### MicroSD card breakout board+

[MicroSD card breakout board+](https://www.adafruit.com/product/254)
Not just a simple breakout board, this microSD adapter goes the extra mile - designed for ease of use.

- Onboard 5v-\>3v regulator provides 150mA for power-hungry cards
- 3v level shifting means you can use this with ease on either 3v or 5v systems
- Uses a proper level...

In Stock
[Buy Now](https://www.adafruit.com/product/254)
[Related Guides to the Product](https://learn.adafruit.com/products/254/guides)

## Related Guides

- [Adafruit Motor Shield](https://learn.adafruit.com/adafruit-motor-shield.md)
- [Photocells](https://learn.adafruit.com/photocells.md)
- [Circuit Playground: D is for Diode](https://learn.adafruit.com/circuit-playground-d-is-for-diode.md)
- [Micro SD Card Breakout Board Tutorial](https://learn.adafruit.com/adafruit-micro-sd-breakout-board-card-tutorial.md)
- [0.96" mini Color OLED](https://learn.adafruit.com/096-mini-color-oled.md)
- [Halloween Pumpkin](https://learn.adafruit.com/halloween-pumpkin.md)
- [Multi-tasking the Arduino - Part 1](https://learn.adafruit.com/multi-tasking-the-arduino-part-1.md)
- [Low Power WiFi Datalogger](https://learn.adafruit.com/low-power-wifi-datalogging.md)
- [Arduino Lesson 3. RGB LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds.md)
- [Create an Internet of Things Dashboard with Adafruit IO](https://learn.adafruit.com/create-an-internet-of-things-dashboard-with-adafruit-dot-io.md)
- [Adafruit 4-Channel ADC Breakouts](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts.md)
- [Trinket Audio Player](https://learn.adafruit.com/trinket-audio-player.md)
- [TTL Serial Camera](https://learn.adafruit.com/ttl-serial-camera.md)
- [Wave Shield Voice Changer](https://learn.adafruit.com/wave-shield-voice-changer.md)
- [All About Arduino Libraries](https://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use.md)
