# Source: https://learn.adafruit.com/adalight-diy-ambient-tv-lighting/wiring-1.md

# Adalight Project Pack

## Wiring

The LED strand has a specific “input” and “output” end. The Arduino _must_ connect to the “input” end! This is the smaller of the two plastic end connectors, the one with the triangular “arms”:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/487/medium800/led_pixels_bullet-conn.jpg?1396773290)

You can press wires directly into the plug connector. This works best with&nbsp;breadboarding jumper wires or solid-core (not stranded)&nbsp;copper wire.  
  
Only three wires will be&nbsp;used.&nbsp; **The red wire does not connect to the Arduino.**

![led_pixels_jam-wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/485/medium640/led_pixels_jam-wires.jpg?1396773281)

Alternately, if you don’t want to use the “jammed wires” trick, an optional mating connector is&nbsp;[available in the Adafruit shop](http://adafruit.com/products/579 "Link: http://adafruit.com/products/579"). This has&nbsp;a plug housing at one end and four tinned wires at the opposite end…strip a little more insulation to press these into Arduino pin sockets.  
  
**The red wire does not connect to the Arduino.** You can trim this wire from the mating connector&nbsp;or insulate it with tape or heat-shrink tube.

![led_pixels_connector.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/486/medium640/led_pixels_connector.jpg?1396773286)

<u>Three</u> wires connect the Arduino UNO to the <u>input end</u> of the LED strand: the **BLUE** wire can connect to any Arduino **GND** pin. **GREEN** should connect to **PIN 13** (SPI clock), and **YELLOW** to **PIN 11** (SPI MOSI). The **RED** wire is **NOT CONNECTED**.  
  
Even though we don't suggest it, you can use an Arduino Mega, connect Green to **52** (SPI Clock) and Yellow to **51** (SPI MOSI), red and blue are the same as above. With the Leonardo, unfortunately the SPI pins are on the 6 pin programming header in the center of the board, so its _really_ not suggested.  
  
The extra red and blue wires are for connecting power, but we’ll do this at the other end of the strand.  
  
Info: 

Power will be connected to the same red and blue wires at the&nbsp;<u>output end</u>&nbsp;of the strand. Data can only go one direction, but power can flow either way!&nbsp;The DC power jack has embossed “+” and “–” symbols on the top face. Connect the&nbsp; **RED** &nbsp;wire to&nbsp; **+** &nbsp;and the&nbsp; **BLUE** &nbsp;wire to&nbsp; **–**. Insert the wires into the “jaws” of the jack and cinch down the screws to hold the wires securely.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/484/medium800/led_pixels_wiring-diagram.png?1396773276)

(Click to embiggen)

- [Previous Page](https://learn.adafruit.com/adalight-diy-ambient-tv-lighting/pieces.md)
- [Next Page](https://learn.adafruit.com/adalight-diy-ambient-tv-lighting/download-and-install.md)

## Featured Products

### Adalight - DIY Ambient Monitor Lighting Project Pack

[Adalight - DIY Ambient Monitor Lighting Project Pack](https://www.adafruit.com/product/461)
Build your own ambient-light addition for a monitor or media PC television with the Adalight project pack! This project pack is for our ["Adalight" project tutorial](http://learn.adafruit.com/adalight-diy-ambient-tv-lighting). By running the Processing code on your...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/461)
[Related Guides to the Product](https://learn.adafruit.com/products/461/guides)
### 12mm  Diffused Thin Digital RGB LED Pixels (Strand of 25)

[12mm  Diffused Thin Digital RGB LED Pixels (Strand of 25)](https://www.adafruit.com/product/322)
RGB Pixels are digitally-controllable lights you can set to any color, or animate. Each RGB LED and controller chip is molded into a 'dot' of silicone. The dots are weatherproof and rugged. There are four flanges molded in so that you can 'push' them into a 12mm drill hole in...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/322)
[Related Guides to the Product](https://learn.adafruit.com/products/322/guides)
### 12mm  Diffused Flat Digital RGB LED Pixels (Strand of 25)

[12mm  Diffused Flat Digital RGB LED Pixels (Strand of 25)](https://www.adafruit.com/product/738)
RGB Pixels are digitally-controllable lights you can set to any color, or animate. Each RGB LED and controller chip is molded into a 'dot' of silicone. The dots are weatherproof and rugged. There are four flanges molded in so that you can 'push' them into a 12mm drill hole in...

In Stock
[Buy Now](https://www.adafruit.com/product/738)
[Related Guides to the Product](https://learn.adafruit.com/products/738/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Female DC Power adapter - 2.1mm jack to screw terminal block

[Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/product/368)
If you need to connect a DC power wall wart to a board that doesn't have a DC jack - this adapter will come in very handy! There is a 2.1mm DC jack on one end, and a screw terminal block on the other. The terminals are labeled with positive/negative assuming a positive-tip configuration...

In Stock
[Buy Now](https://www.adafruit.com/product/368)
[Related Guides to the Product](https://learn.adafruit.com/products/368/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

In Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)

## Related Guides

- [2.2" TFT Display](https://learn.adafruit.com/2-2-tft-display.md)
- [Arduin-o-Phone](https://learn.adafruit.com/arduin-o-phone-arduino-powered-diy-cellphone.md)
- [Adafruit CC3000 WiFi and Xively](https://learn.adafruit.com/adafruit-cc3000-wifi-and-xively.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [Ladyada's Learn Arduino - Lesson #0](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-0.md)
- [Adafruit 1.27" and 1.5" Color OLED Breakout Board](https://learn.adafruit.com/adafruit-1-5-color-oled-breakout-board.md)
- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Arduino Lesson 7. Make an RGB LED Fader](https://learn.adafruit.com/adafruit-arduino-lesson-7-make-an-rgb-led-fader.md)
- [Wave Shield](https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino.md)
- [Adafruit 1.14" 240x135 Color TFT Breakout LCD Display](https://learn.adafruit.com/adafruit-1-14-240x135-color-tft-breakout.md)
- [Adafruit Arduino Selection Guide](https://learn.adafruit.com/adafruit-arduino-selection-guide.md)
- [Arduino Lesson 3. RGB LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds.md)
- [Character LCDs](https://learn.adafruit.com/character-lcds.md)
- [Arduino Lesson 11. LCD Displays - Part 1](https://learn.adafruit.com/adafruit-arduino-lesson-11-lcd-displays-1.md)
- [RGB LED Matrix Basics](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix.md)
