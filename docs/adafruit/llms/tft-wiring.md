# Source: https://learn.adafruit.com/2-8-tft-touchscreen/tft-wiring.md

# 2.8" TFT Touchscreen

## TFT Wiring

Info: 

Now that the backlight is working, we can get the TFT LCD working. There are many pins required, and to keep the code running fairly fast, we have 'hardcoded' Arduino digital pins #2-#9 for the 8 data lines.  
  
Start at the end of the TFT (other side than the power pins) and in order connect the pins to digital 7 thru 2. If you're using a mega, connect the TFT Data Pins #0-7 to Mega pins #22-29, in that order. Those Mega pins are on the 'double' header.  
![](https://cdn-learn.adafruit.com/assets/assets/000/003/035/medium800/lcds___displays_datahigh.jpg?1396790504)

Then connect the next two pins to digital 9 and 8.  
  
If you're using a mega, connect the TFT Data Pins #0-7 to Mega pins #22-29, in that order. Those Mega pins are on the 'double' header.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/036/medium800/lcds___displays_datalow.jpg?1396790514)

In addition to the 8 data lines, you'll also need 4 or 5 control lines.

- Connect the third pin **CS** ( **Chip Select** ) to Analog 3
- Connect the fourth pin **C/D** ( **Command/Data** ) to Analog 2
- Connect the fifth pin **WR** ( **Write** ) to Analog 1
- Connect the sixth pin **RD** ( **Read** ) to Analog 0
- Connect the seventh pin **RST** ( **Reset** ) to the Arduino Reset line. This will reset the panel when the Arduino is Reset. You can also use a digital pin for the LCD reset but this will save us a pin.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/037/medium800/lcds___displays_controlwire.jpg?1396790524)

Now we can run some code!- [Previous Page](https://learn.adafruit.com/2-8-tft-touchscreen/backlight-wiring.md)
- [Next Page](https://learn.adafruit.com/2-8-tft-touchscreen/lcd-test.md)

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
