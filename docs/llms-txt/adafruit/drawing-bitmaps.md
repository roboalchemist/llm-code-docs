# Source: https://learn.adafruit.com/096-mini-color-oled/drawing-bitmaps.md

# 0.96" mini Color OLED

## Drawing Bitmaps

We have an example sketch in the library showing how to display full color bitmap images stored on an SD card. You'll need a microSD card such as this one . This example will only work for Arduino v1.0 and later.

You'll also need an image. We suggest starting with this bitmap of a flower If you want to later use your own image, use an image editing tool and crop your image to no larger than 64 pixels high and 96 pixels wide. Save it as a 24-bit color&nbsp; **BMP** &nbsp;file - it must be 24-bit color format to work, even if it was originally a 16-bit color image - becaue of the way BMPs are stored and displayed!

Copy the&nbsp; **violet.bmp** &nbsp;to the microSD card and insert it into the back of the breakout board.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/843/medium800/lcds___displays_microholder.jpg?1396766370)

We'll have to add an extra 2 wires so we can 'select' and 'receive data' from the SD card

# Old Style Board: (two rows of pins)

Connect the third pin **SD ChipSelect** of the OLED (gray wire) to pin #18 of the 74LVC245. Then connect pin #2 of the 74LVC245 to Arduino **Digital #4**. This is the pin to select that we want to talk to the microSD card.

Then connect second-from-the bottom pin of the OLED - **SDOUT** - with a wire directly to **Arduino Digital #12** this is the longer white wire shown - this wire does not need to be level shifted.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/844/medium800/lcds___displays_microsdwire.jpg?1396766375)

# New Style Board: (Single row of pins)

Add the following two connections between the breakout board and the Arduino:

- **SDCS** (SC) - Digital #4.(Gray Wire)
- **MISO** (SO) - Digital #12 (Orange Wire)

&nbsp;

![](https://cdn-learn.adafruit.com/assets/assets/000/075/975/medium800/arduino_compatibles_SSD1331_fritzing_resized.png?1558672473)

# Bitmap Example Sketch

To display bitmaps from the on-board micro SD slot, you will need a&nbsp;[micro SD card](http://www.adafruit.com/products/102)&nbsp;formatted **&nbsp;FAT16 or FAT32** &nbsp;(they almost always are by default).

![](https://cdn-learn.adafruit.com/assets/assets/000/076/123/medium800/arduino_compatibles_lcds___displays_SD102_MED.jpg?1558987818)

There is a built in microSD card slot on the rear of the breakout and we can use that to load bitmap images!  
  
It's really easy to draw bitmaps. We have a library for it, Adafruit\_ImageReader, which can be installed through the Arduino Library Manager&nbsp;(Sketch→Include Library→Manage Libraries…). Enter “imageread” in the search field and the library is easy to spot:

![](https://cdn-learn.adafruit.com/assets/assets/000/076/124/medium800/arduino_compatibles_adafruit_products_install-imagereader-lib.png?1558988108)

Next you can either download the image here or copy it from the images folder from inside the library files.

[Download daffodil.bmp](https://raw.githubusercontent.com/adafruit/Adafruit_ImageReader/1.1.1/images/daffodil.bmp)
## Insert the card

Insert the micro SD card into the slot on the back of the SSD1331 breakout board.

![arduino_compatibles_ssd1331-sd.png](https://cdn-learn.adafruit.com/assets/assets/000/076/135/medium640/arduino_compatibles_ssd1331-sd.png?1559004743)

## Copy the bitmap file

Copy the file&nbsp; **"daffodil.bmp"** &nbsp;from the Adafruit\_ImageReader\_Library\images folder (or wherever you saved it if you downloaded the file) over to the root directory of your micro-SD card.

![arduino_compatibles_daffodil-image-location.png](https://cdn-learn.adafruit.com/assets/assets/000/076/130/medium640/arduino_compatibles_daffodil-image-location.png?1558996000)

## Load the bitmap example sketch

Select&nbsp; **"Examples-\>Adafruit\_ImageReader\_Library-\>BreakoutSSD1331"** &nbsp;and upload it to your Arduino.

![arduino_compatibles_example-location.png](https://cdn-learn.adafruit.com/assets/assets/000/076/131/medium640/arduino_compatibles_example-location.png?1558996060)

You should see the daffodil! If you don't see it, check the Serial Monitor for hints on what might have gone wrong (maybe the microSD card had an issue).

![](https://cdn-learn.adafruit.com/assets/assets/000/000/845/medium800/lcds___displays_2013_07_14_IMG_2037-1024.jpg?1396766385)

- [Previous Page](https://learn.adafruit.com/096-mini-color-oled/wiring.md)
- [Next Page](https://learn.adafruit.com/096-mini-color-oled/circuitpython-displayio-quickstart.md)

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

- [Tiny Arduino Music Visualizer](https://learn.adafruit.com/piccolo.md)
- [Create an Internet of Things Dashboard with Adafruit IO](https://learn.adafruit.com/create-an-internet-of-things-dashboard-with-adafruit-dot-io.md)
- [Adafruit Ultimate GPS](https://learn.adafruit.com/adafruit-ultimate-gps.md)
- [Ladyada's Learn Arduino - Lesson #0](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-0.md)
- [Arduino Lesson 15. DC Motor Reversing](https://learn.adafruit.com/adafruit-arduino-lesson-15-dc-motor-reversing.md)
- [Wireless Gardening with Arduino + CC3000 WiFi Modules](https://learn.adafruit.com/wireless-gardening-arduino-cc3000-wifi-modules.md)
- [Arduino Lesson 9. Sensing Light](https://learn.adafruit.com/adafruit-arduino-lesson-9-sensing-light.md)
- [Low Power Coin Cell Voltage Logger](https://learn.adafruit.com/low-power-coin-cell-voltage-logger.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [Skill Badge Requirements: Microcontrollers](https://learn.adafruit.com/skill-badge-requirements-microcontrollers.md)
- [WiFi Weather Station](https://learn.adafruit.com/wifi-weather-station-arduino-cc3000.md)
- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [Electronic Demon Costume](https://learn.adafruit.com/electronic-demon-costume.md)
- [DIY 8x2 LCD Shield](https://learn.adafruit.com/diy-8x2-lcd-shield.md)
- [Circuit Playground Sound-Controlled Robot](https://learn.adafruit.com/circuit-playground-sound-controlled-robot.md)
