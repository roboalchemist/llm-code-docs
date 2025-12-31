# Source: https://learn.adafruit.com/2-2-tft-display/python-wiring-and-setup.md

# Source: https://learn.adafruit.com/1-8-tft-display/python-wiring-and-setup.md

# Source: https://learn.adafruit.com/096-mini-color-oled/python-wiring-and-setup.md

# 0.96" mini Color OLED

## Python Wiring and Setup

# Wiring
It's easy to use display breakouts with Python and the&nbsp;[Adafruit CircuitPython RGB Display](https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display)&nbsp;module.&nbsp; This module allows you to easily write Python code to control the display.

We'll cover how to wire the display to your Raspberry Pi. First assemble your display.

Since there's&nbsp;_dozens_&nbsp;of Linux computers/boards you can use we will show wiring for Raspberry Pi. For other platforms,&nbsp;[please visit the guide for CircuitPython on Linux to see whether your platform is supported](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).&nbsp;

Connect the display as shown below to your Raspberry Pi.

Info: 

Warning: 

## ILI9341 and HX-8357-based Displays

### 2.2" Display

- **CLK** connects to SPI clock. On the Raspberry Pi, that's **SCLK**
- **MOSI** connects to SPI MOSI. On the Raspberry Pi, that's also **MOSI**
- **CS** &nbsp;connects to our SPI Chip Select pin. We'll be using&nbsp; **CE0**
- **D/C** connects to our SPI Chip Select pin. We'll be using **GPIO 25** , but this can be changed later.
- **RST** &nbsp;connects to our Reset pin. We'll be using&nbsp; **GPIO 24** but this can be changed later as well.
- **Vin** connects to the Raspberry Pi's **3V** &nbsp;pin
- **GND** connects to the Raspberry Pi's **ground**

![](https://cdn-learn.adafruit.com/assets/assets/000/084/668/medium800/arduino_compatibles_2.2_TFT_bb.jpg?1574277297)

[Download the Fritzing Diagram](https://cdn-learn.adafruit.com/assets/assets/000/084/669/original/2.2_TFT.fzz?1574277335)
### 2.4", 2.8", 3.2", and 3.5" Displays

These displays are set up to use the 8-bit data lines by default. We want to use them for SPI. To do that, you'll need to either solder bridge some pads on the back or connect the appropriate IM lines to 3.3V with jumper wires. Check the back of your display for the correct solder pads or IM lines to put it in SPI mode.

- **Vin** connects to the Raspberry Pi's **3V** &nbsp;pin
- **GND** connects to the Raspberry Pi's **ground**
- **CLK** connects to SPI clock. On the Raspberry Pi, thats **SLCK**
- **MOSI** connects to SPI MOSI. On the Raspberry Pi, thats also **MOSI**
- **CS** &nbsp;connects to our SPI Chip Select pin. We'll be using&nbsp; **CE0**
- **D/C** connects to our SPI Chip Select pin. We'll be using **GPIO 25** , but this can be changed later.
- **RST** &nbsp;connects to our Reset pin. We'll be using&nbsp; **GPIO 24** but this can be changed later as well.

Warning: 

![](https://cdn-learn.adafruit.com/assets/assets/000/084/676/medium800/arduino_compatibles_2.8_TFT_bb.jpg?1574277504)

[Download the Fritzing Diagram](https://cdn-learn.adafruit.com/assets/assets/000/084/670/original/2.8_TFT.fzz?1574277361)
## ST7789 and ST7735-based Displays

### 1.3", 1.54", and 2.0" IPS TFT Display

- **Vin** connects to the Raspberry Pi's **3V** &nbsp;pin
- **GND** connects to the Raspberry Pi's **ground**
- **CLK** connects to SPI clock. On the Raspberry Pi, thats **SLCK**
- **MOSI** connects to SPI MOSI. On the Raspberry Pi, thats also **MOSI**
- **CS** &nbsp;connects to our SPI Chip Select pin. We'll be using&nbsp; **CE0**
- **RST** &nbsp;connects to our Reset pin. We'll be using&nbsp; **GPIO 24** but this can be changed later.
- **D/C** connects to our SPI Chip Select pin. We'll be using **GPIO 25** , but this can be changed later as well.

![](https://cdn-learn.adafruit.com/assets/assets/000/084/677/medium800/arduino_compatibles_2.0_TFT_bb.jpg?1574277527)

[Download the Fritzing Diagram](https://cdn-learn.adafruit.com/assets/assets/000/084/671/original/2.0_TFT.fzz?1574277392)
### 0.96", 1.14", and 1.44" Displays

- **Vin** connects to the Raspberry Pi's **3V** &nbsp;pin
- **GND** connects to the Raspberry Pi's **ground**
- **CLK** connects to SPI clock. On the Raspberry Pi, thats **SLCK**
- **MOSI** connects to SPI MOSI. On the Raspberry Pi, thats also **MOSI**
- **CS** &nbsp;connects to our SPI Chip Select pin. We'll be using&nbsp; **CE0**
- **RST** &nbsp;connects to our Reset pin. We'll be using&nbsp; **GPIO 24** but this can be changed later.
- **D/C** connects to our SPI Chip Select pin. We'll be using **GPIO 25** , but this can be changed later as well.

![](https://cdn-learn.adafruit.com/assets/assets/000/084/678/medium800/arduino_compatibles_1.44_TFT_bb.jpg?1574277538)

[Download the Fritzing Diagram](https://cdn-learn.adafruit.com/assets/assets/000/084/672/original/1.44_TFT.fzz?1574277409)
### 1.8" Display

- **GND** connects to the Raspberry Pi's **ground**
- **Vin** connects to the Raspberry Pi's **3V** &nbsp;pin
- **RST** &nbsp;connects to our Reset pin. We'll be using&nbsp; **GPIO 24** but this can be changed later.
- **D/C** connects to our SPI Chip Select pin. We'll be using **GPIO 25** , but this can be changed later as well.
- **CS** &nbsp;connects to our SPI Chip Select pin. We'll be using&nbsp; **CE0**
- **MOSI** connects to SPI MOSI. On the Raspberry Pi, thats also **MOSI**
- **CLK** connects to SPI clock. On the Raspberry Pi, thats **SLCK**
- **LITE** connects to the Raspberry Pi's **3V** pin. This can be used to separately control the backlight.

![](https://cdn-learn.adafruit.com/assets/assets/000/084/679/medium800/arduino_compatibles_1.8_TFT_bb.jpg?1574277564)

[Download the Fritzing Diagram](https://cdn-learn.adafruit.com/assets/assets/000/084/673/original/1.8_TFT.fzz?1574277427)
## SSD1351-based Displays

### 1.27" and 1.5" OLED Displays

- **GND** connects to the Raspberry Pi's **ground**
- **Vin** connects to the Raspberry Pi's **3V** &nbsp;pin
- **CLK** connects to SPI clock. On the Raspberry Pi, thats **SLCK**
- **MOSI** connects to SPI MOSI. On the Raspberry Pi, thats also **MOSI**
- **CS** &nbsp;connects to our SPI Chip Select pin. We'll be using&nbsp; **CE0**
- **RST** &nbsp;connects to our Reset pin. We'll be using&nbsp; **GPIO 24** but this can be changed later.
- **D/C** connects to our SPI Chip Select pin. We'll be using **GPIO 25** , but this can be changed later as well.

![](https://cdn-learn.adafruit.com/assets/assets/000/084/680/medium800/arduino_compatibles_1.5_OLED_bb.jpg?1574277589)

[Download the Fritzing Diagram](https://cdn-learn.adafruit.com/assets/assets/000/084/674/original/1.5_OLED.fzz?1574277454)
## SSD1331-based Display

### 0.96" OLED Display

- **MOSI** connects to SPI MOSI. On the Raspberry Pi, thats also **MOSI**
- **CLK** connects to SPI clock. On the Raspberry Pi, thats **SLCK**
- **D/C** connects to our SPI Chip Select pin. We'll be using **GPIO 25** , but this can be changed later.
- **RST** &nbsp;connects to our Reset pin. We'll be using&nbsp; **GPIO 24** but this can be changed later as well.
- **CS** &nbsp;connects to our SPI Chip Select pin. We'll be using&nbsp; **CE0**
- **Vin** connects to the Raspberry Pi's **3V** &nbsp;pin
- **GND** connects to the Raspberry Pi's **ground**

![](https://cdn-learn.adafruit.com/assets/assets/000/096/091/medium800/arduino_compatibles_0.96_OLED_bb.jpg?1603118613)

[Download the Fritzing Diagram](https://cdn-learn.adafruit.com/assets/assets/000/096/092/original/0.96_OLED.fzz?1603118637)
# Setup

You'll need to install the Adafruit\_Blinka library that provides the CircuitPython support in Python. This may also require enabling SPI on your platform and verifying you are running Python 3. [Since each platform is a little different, and Linux changes often, please visit the CircuitPython on Linux guide to get your computer ready](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux)!

Warning: 

## Python Installation of RGB Display Library

Once that's done, from your command line run the following command:

- `pip3 install adafruit-circuitpython-rgb-display`

If your default Python is version 3 you may need to run 'pip' instead. Just make sure you aren't trying to use CircuitPython on Python 2.x, it isn't supported!

If that complains about pip3 not being installed, then run this first to install it:

- `sudo apt-get install python3-pip`

## DejaVu TTF Font

Raspberry Pi usually comes with the DejaVu font already installed, but in case it didn't, you can run the following to install it:

- `sudo apt-get install fonts-dejavu`

This package was previously calls **ttf-dejavu** , so if you are running an older version of Raspberry Pi OS, it may be called that.

## Pillow Library

We also need PIL, the Python Imaging Library, to allow graphics and using text with custom fonts. There are several system libraries that PIL relies on, so installing via a package manager is the easiest way to bring in everything:

- `sudo apt-get install python3-pil`

If you installed the PIL through PIP, you may need to install some additional libraries:

- `sudo apt-get install libopenjp2-7 libtiff5 libatlas-base-dev`

That's it. You should be ready to go.

- [Previous Page](https://learn.adafruit.com/096-mini-color-oled/circuitpython-displayio-quickstart.md)
- [Next Page](https://learn.adafruit.com/096-mini-color-oled/python-usage.md)

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
