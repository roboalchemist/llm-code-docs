# Source: https://learn.adafruit.com/096-mini-color-oled/wiring.md

# 0.96" mini Color OLED

## Wiring

## New Model
If your display has a single row header across the top, it is the newer version. For wiring instructions, skip down to "Wiring Up the Newer Version"![lcds___displays_684top_LRG.jpg](https://cdn-learn.adafruit.com/assets/assets/000/009/647/medium640/lcds___displays_684top_LRG.jpg?1396894657)

## Older Model
If your display has a row of header pins down each side, it is the older model. See "Wiring the OLDER design" below.![lcds___displays_parts.jpg](https://cdn-learn.adafruit.com/assets/assets/000/009/648/medium640/lcds___displays_parts.jpg?1396894670)

# Wiring the OLDER design (two rows of pins on either side)
The older breakout does not have a 5V level shifter on board, so its a little more complex to wire up!  
  
The OLED module supports 3 methods of communication: 4 wire SPI, 8-bit parallel in 8080 and 6800 format. Since the display is small and we like to save pins, we'll be using the SPI protocol. Our tutorial, wiring and example code is all for SPI so if you need 8-bit, check the datasheets for details on how to wire up for 8-bit parallel. ![](https://cdn-learn.adafruit.com/assets/assets/000/000/840/medium800/lcds___displays_parts.jpg?1396766345)

Since the OLED is 3.3V and also uses 3.3V logic, we need to use a logic shifter. We include a DIP logic shifter, the 74LVX245 with the OLED. If you're using a 3.3V logic chip, you can skip the logic shifter. Arduinos are all 5.0V so we'll be demonstrating that.

Danger: 

Plug in the OLED and the '245 chip. The Chip has the notch closest to the OLED. Click on the image to see a large photo if you need help orienting

Starting from the top pin of the OLED (closest to the Adafruit flower) Connect the following OLED pins:

- Common ground - black wire
- 3.3V (red wires from the Arduino)
- **SD CS Pin** - don't connect (microSD card, we'll get to this later)
- **OLED CS Pin** &nbsp;- purple wire - 74LVC245 pin #17
- **OLED Reset Pin** &nbsp;- blue wire - 74LVC245 pin #16
- **OLED D/C Pin** &nbsp;- yellow wire - 74LVC245 pin #15
- **OLED SCLK Pin** &nbsp;- orange wire - 74LVC245 pin #14
- **OLED DATA Pin** &nbsp;- brown - 74LVC245 pin #13
- **SD Detect Pin** - not used, don't connect. Later on, if you wish, you can use this pin to detect if a card is inserted, it will be shorted to ground when a card is in the holder  

![](https://cdn-learn.adafruit.com/assets/assets/000/000/841/medium800/lcds___displays_wiring.jpg?1396766354)

Next we'll connect the remaining 74LVC245 pins to the Arduino

- Pin #1 goes to 3.3V (red wire)
- Skip
- Purple wire - goes to Digital #10
- Blue wire - goes to Digital #9
- Yellow wire - goes to Digital #8
- Orange wire - goes to Digital #13
- Brown wires - goes to Digital #11
- Skip
- Skip
- Connect to common ground

Then connect pin #20 of the 74LVC245 to 3.3V and pin #19 to Ground.

Digital #12 isn't used yet (we'll connect this to the SD card later

# Wiring up the newer version (With one row of pins on top)

The updated 5v ready version of this display includes on-board level-shifting. So the 74LVC245 chip is not required and the wiring is much simpler! For the level shifter we use the [CD74HC4050](http://www.ti.com/product/CD74HC4050/) which has a typical propagation delay of ~10ns  
  
The full pin names are marked on the back of the board, but there are abbreviations on the front to help identify pins when it is plugged into the breadboard. The chart below lists the full pin name, the abbreviated name (in parentheses) and the Arduino pin name to connect it to. Wire colors are as shown in the photo.

- **GND** (G) - Gnd (Black Wire)
- **VCC** (+) - 5v (Red Wire)
- **SDCS** (SC) - skip
- **OCS** (OC) - Digital #10 (Orange Wire)
- **RST** (R) - Digital #9 (Green Wire)
- **D/C** (DC) - Digital #8 (Brown Wire)
- **SCK** (CK) - Digital #13 (White Wire)
- **MOSI** (SI) - Digital #11 (Blue Wire)
- **MISO** (SO) - skip
- **CD** (CD) - skip

![](https://cdn-learn.adafruit.com/assets/assets/000/009/650/medium800/lcds___displays_2013_07_14_IMG_2035.jpg?1396894695)

# Installing and running Arduino software

Now we can run the test software on the Arduino. We'll need to download the library first and install it

_Three_ libraries need to be installed&nbsp;using the **Arduino Library Manager** …this is the preferred and modern way. From the Arduino “Sketch” menu, select “Include Library” then “Manage Libraries…”

![](https://cdn-learn.adafruit.com/assets/assets/000/067/417/medium800/arduino_compatibles_manage-libraries.png?1544587619)

Type “gfx” in the search field to quickly find the first library — **Adafruit\_GFX** :

![](https://cdn-learn.adafruit.com/assets/assets/000/067/418/medium800/arduino_compatibles_adafruit-gfx-library-manager.png?1544587640)

Repeat the search and install steps, looking for the **Adafruit\_BusIO** and **Adafruit\_SSD1331&nbsp;** libraries.

After you restart, you should be able to select **File→Examples→Adafruit\_SSD1331→**** test** - this is the example sketch that just tests the display by drawing text and shapes. Upload the sketch and you should see the following:

![](https://cdn-learn.adafruit.com/assets/assets/000/000/842/medium800/lcds___displays_triangles.jpg?1396766360)

If alls working, then you can start looking through the test sketch for demonstrations on how to print text, circles, lines, etc.  
  
[**For a detailed tutorial on the Adafruit GFX library, including all the functions available please visit the GFX tutorial page**](http://learn.adafruit.com/adafruit-gfx-graphics-library "Link: http://learn.adafruit.com/adafruit-gfx-graphics-library")

- [Previous Page](https://learn.adafruit.com/096-mini-color-oled/power.md)
- [Next Page](https://learn.adafruit.com/096-mini-color-oled/drawing-bitmaps.md)

## Featured Products

### OLED Breakout Board - 16-bit Color 0.96" w/microSD holder

[OLED Breakout Board - 16-bit Color 0.96" w/microSD holder](https://www.adafruit.com/product/684)
We love our black and white monochrome displays but we also like to dabble with some color now and then. Our new 0.96" color OLED displays are perfect when you need an ultra-small display with vivid, high-contrast 16-bit color. The visible portion of the OLED measures 0.96" diagonal...

In Stock
[Buy Now](https://www.adafruit.com/product/684)
[Related Guides to the Product](https://learn.adafruit.com/products/684/guides)
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

## Related Guides

- [Ladyada's Bento Box](https://learn.adafruit.com/lady-adas-bento-box.md)
- [OLED TRON Clock](https://learn.adafruit.com/oled-tron-clock.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [Programming Arduino with Android and Windows Tablets](https://learn.adafruit.com/programming-arduino-with-android-and-windows-tablets.md)
- [Let’s Put LEDs in Things!](https://learn.adafruit.com/lets-put-leds-in-things.md)
- [Making Adabot: Part 2](https://learn.adafruit.com/making-adabot-part-2.md)
- [Current Limiting Stepper Driver with DRV8871](https://learn.adafruit.com/current-limiting-stepper-driver-with-drv8871.md)
- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Trinket Audio Player](https://learn.adafruit.com/trinket-audio-player.md)
- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [Arduino Lesson 17. Email Sending Movement Detector](https://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector.md)
- [Bluefruit LE Connect for iOS and Android](https://learn.adafruit.com/bluefruit-le-connect.md)
- [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors.md)
- [Adafruit CC3000 WiFi and Xively](https://learn.adafruit.com/adafruit-cc3000-wifi-and-xively.md)
- [Trellis 3D Printed Enclosure](https://learn.adafruit.com/trellis-3d-printed-enclosure.md)
