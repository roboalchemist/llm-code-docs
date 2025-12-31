# Source: https://learn.adafruit.com/1-8-tft-display/breakout-wiring-and-test.md

# 1.8" TFT Display Breakout and Shield

## Breakout Wiring & Test

There are two ways to wire up these displays - one is a more flexible method (you can use any pins on the Arduino) and the other is much faster (4-8x faster, but you are required to use the hardware SPI pins) We will begin by showing how to use the faster method, you can always change the pins later for flexible 'software SPI'

![](https://cdn-learn.adafruit.com/assets/assets/000/019/562/medium800/lcds___displays_spiwire.jpg?1409945098)

Wiring up the display in SPI mode is pretty easy as there's not that many pins! We'll be using hardware SPI, but you can also use software SPI (any pins) later. Start by connecting the power pins

- **3-5V Vin** connects to the Arduino **5V** pin - red wires
- **GND** connects to Arduino ground - black wires
- **CLK** connects to SPI clock. On Arduino Uno/Duemilanove/328-based, thats **Digital 13**. On Mega's, its **Digital 52** and on Leonardo/Due its **ICSP-3** ([See SPI Connections for more details](http://arduino.cc/en/Reference/SPI)) - this is the orange wire
- **MOSI** connects to SPI MOSI. On Arduino Uno/Duemilanove/328-based, thats **Digital 11**. On Mega's, its **Digital 51** and on Leonardo/Due its **ICSP-4** ([See SPI Connections for more details](http://arduino.cc/en/Reference/SPI "Link: http://arduino.cc/en/Reference/SPI")) - this is the white wire
- **CS** connects to our SPI Chip Select pin. We'll be using **Digital 10** but you can later change this to any pin - this is the yellow wire
- **RST** connects to our TFT reset pin. We'll be using **Digital 9** but you can later change this pin too - this is the blue wire
- **D/C** connects to our SPI data/command select pin. We'll be using **Digital 8** but you can later change this pin too - this is the green wire

# Install Adafruit ST7735 TFT Library

We have example code ready to go for use with these TFTs. It's written for Arduino, which should be portable to any microcontroller by adapting the C++ source.

_Three_ libraries need to be installed&nbsp;using the **Arduino Library Manager** …this is the preferred and modern way. From the Arduino “Sketch” menu, select “Include Library” then “Manage Libraries…”

![](https://cdn-learn.adafruit.com/assets/assets/000/065/251/medium800/arduino_compatibles_managelib.png?1541474290)

Search for and install the Adafruit GFX library:

![](https://cdn-learn.adafruit.com/assets/assets/000/065/252/medium800/arduino_compatibles_image.png?1541474525)

And the Adafruit ST7735 library:

![](https://cdn-learn.adafruit.com/assets/assets/000/065/253/medium800/arduino_compatibles_image.png?1541474578)

If using an older version of the Arduino IDE (pre-1.8.10), also locate and install the **Adafruit\_BusIO** library (newer versions do this automatically when using the Arduino Library Manager).

If this is all unfamiliar, we have a [tutorial introducing Arduino library concepts and installation](http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use).  
  
Restart the IDE!

![](https://cdn-learn.adafruit.com/assets/assets/000/019/563/medium800/lcds___displays_gfxtest.png?1409945233)

After restarting the Arduino software, you should see a new **example** folder called **Adafruit\_ST7735** and inside, an example called **graphicstest**.

Now upload the sketch to your Arduino. You may need to press the Reset button to reset the arduino and TFT. You should see a collection of graphical tests draw out on the TFT.

![](https://cdn-learn.adafruit.com/assets/assets/000/019/564/medium800/lcds___displays_358demo1_ORIG.jpg?1409945263)

Once uploaded, the Arduino should perform all the test display procedures! If you're not seeing anything - first check if you have the backlight on, if the backlight is not lit something is wrong with the power/backlight wiring. If the backlight is lit but you see nothing on the display make sure you're using our suggested wiring.

# Changing Pins

Now that you have it working, there's a few things you can do to change around the pins.

If you're using Hardware SPI, the CLOCK and MOSI pins are 'fixed' and cant be changed. But you can change to software SPI, which is a bit slower, and that lets you pick any pins you like. Find these lines:

```
// Option 1 (recommended): must use the hardware SPI pins
// (for UNO thats sclk = 13 and sid = 11) and pin 10 must be
// an output. This is much faster - also required if you want
// to use the microSD card (see the image drawing example)
Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS,  TFT_DC, TFT_RST);

// Option 2: use any pins but a little slower!
#define TFT_SCLK 13   // set these to be whatever pins you like!
#define TFT_MOSI 11   // set these to be whatever pins you like!
//Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_MOSI, TFT_SCLK, TFT_RST);


```

Comment out option 1, and uncomment option 2. Then you can change the **TFT\_** pins to whatever pins you'd like!

You can also save a pin by setting

`#define TFT_RST    9`

to

`#define TFT_RST   -1`

and connecting the RST line to the Arduino Reset pin. That way the Arduino will auto-reset the TFT as well.

- [Previous Page](https://learn.adafruit.com/1-8-tft-display/breakout-assembly.md)
- [Next Page](https://learn.adafruit.com/1-8-tft-display/displaying-bitmaps.md)

## Featured Products

### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### 1.8" Color TFT LCD display with MicroSD Card Breakout

[1.8" Color TFT LCD display with MicroSD Card Breakout](https://www.adafruit.com/product/358)
This lovely little display breakout is the best way to add a small, colorful and bright display to any project. Since the display uses 4-wire SPI to communicate and has its own pixel-addressable frame buffer, it can be used with every kind of microcontroller. Even a very small one with low...

Out of Stock
[Buy Now](https://www.adafruit.com/product/358)
[Related Guides to the Product](https://learn.adafruit.com/products/358/guides)
### Adafruit 1.8" Color TFT Shield w/microSD and Joystick

[Adafruit 1.8" Color TFT Shield w/microSD and Joystick](https://www.adafruit.com/product/802)
This lovely little shield is the best way to add a small, colorful and bright display to any project. We took our popular 1.8" TFT breakout board and remixed it into an Arduino shield complete with microSD card slot and a 5-way joystick navigation switch and three selection buttons! Since...

In Stock
[Buy Now](https://www.adafruit.com/product/802)
[Related Guides to the Product](https://learn.adafruit.com/products/802/guides)
### 1.8" SPI TFT display, 160x128 18-bit color - ST7735R driver

[1.8" SPI TFT display, 160x128 18-bit color - ST7735R driver](https://www.adafruit.com/product/618)
We just love this little 1.8" TFT display, with true TFT color (up to 18-bits per pixel!), fine 160x128 resolution, two white LED backlight that runs on 3.3V and a very easy SPI interface that requires only 4 or 5 digital pins to send pixels to the display.  
  
**Please...**

Out of Stock
[Buy Now](https://www.adafruit.com/product/618)
[Related Guides to the Product](https://learn.adafruit.com/products/618/guides)

## Related Guides

- [Wave Shield](https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino.md)
- [Adafruit 2.8" TFT Touch Shield v2 - Capacitive or Resistive](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2.md)
- [How to Build a Testing Jig](https://learn.adafruit.com/how-to-build-a-testing-fixture.md)
- [Create an Internet of Things Dashboard with Adafruit IO](https://learn.adafruit.com/create-an-internet-of-things-dashboard-with-adafruit-dot-io.md)
- [Let’s Put LEDs in Things!](https://learn.adafruit.com/lets-put-leds-in-things.md)
- [Tiny Arduino Music Visualizer](https://learn.adafruit.com/piccolo.md)
- [Circuit Playground Sound-Controlled Robot](https://learn.adafruit.com/circuit-playground-sound-controlled-robot.md)
- [Adafruit 1.27" and 1.5" Color OLED Breakout Board](https://learn.adafruit.com/adafruit-1-5-color-oled-breakout-board.md)
- [Arduino Lesson 15. DC Motor Reversing](https://learn.adafruit.com/adafruit-arduino-lesson-15-dc-motor-reversing.md)
- [TTL Serial Camera](https://learn.adafruit.com/ttl-serial-camera.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [Geofencing with the FONA 808 & Adafruit IO](https://learn.adafruit.com/geofencing-with-the-fona-808-and-adafruit-io.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [Adafruit Data Logger Shield](https://learn.adafruit.com/adafruit-data-logger-shield.md)
- [Making Adabot: Part 2](https://learn.adafruit.com/making-adabot-part-2.md)
