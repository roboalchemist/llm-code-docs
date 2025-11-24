# Source: https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/wiring.md

# Adafruit INA219 Current Sensor Breakout

## Wiring

The INA219 breakout board can be powered by the&nbsp;5V or 3V pin on your Arduino&nbsp;and communicates via I2C.

To wire up the STEMMA QT version:

- Connect&nbsp;**board VIN (red wire)** to&nbsp; **Arduino 5V** &nbsp;if you are running a **5V** board Arduino (Mega, etc.). If your board is **3V,** connect to that instead.
- Connect **board GND (black wire)&nbsp;**to&nbsp; **Arduino**  **GND**
- Connect **board SCL (yellow wire)&nbsp;**to&nbsp; **Arduino**  **SCL**
- Connect **board SDA (blue wire)&nbsp;**to&nbsp; **Arduino**  **SDA**
- Connect **Vin+** to the **positive terminal of the power supply for the circuit under test**
- Connect **Vin-** to the **positive terminal or lead of the load**

![adafruit_products_INA219QT_Arduino_STEMMA_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/104/420/medium640/adafruit_products_INA219QT_Arduino_STEMMA_bb.jpg?1631131311)

![adafruit_products_INA219QT_Arduino_breadboard_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/104/421/medium640/adafruit_products_INA219QT_Arduino_breadboard_bb.jpg?1631131331)

To wire up the original version:

## Connect to the microcontroller

- Connect **GND** to **GND**
- Connect **VCC** to **5v**
- Then connect **SDA** to **SDA** (Analog pin 4 on pre-R3 Arduinos)
- And connect **SCL** to **SCL** (Analog pin 5 on pre-R3&nbsp;Arduinos)

![adafruit_products_Current_Measurement_Alternate_Signals_bb.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/461/medium640/adafruit_products_Current_Measurement_Alternate_Signals_bb.jpg?1550283333)

On R3 and later Arduinos, you can connect to the new dedicated SDA & SCL pins next to the AREF pin. &nbsp;On pre-R3 Megas, SDA & SCL are on pins 20 & 21.

  
Next we must insert the INA219 current sensor into the circuit we want to measure: ![](https://cdn-learn.adafruit.com/assets/assets/000/010/941/medium800/adafruit_products_INA219_WS2812_bb.jpg?1378995140)

Danger: 

## Connect to the circuit

- Connect V+ to the positive terminal of the power supply for the circuit under test.
- Connect V- to the positive terminal or lead of the load. &nbsp;This puts the sense resistor&nbsp;in-line with&nbsp;the circuit.
- Finally, connect a wire from the negative terminal of the power supply to GND. &nbsp;This allows the sensor to measure the load voltage as well as the load current.

The photo below shows an INA219 breakout board configured to measure the motor supply current on an Adafruit Motor&nbsp;Shield.

Primary: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/459/medium800/adafruit_products_2012_10_26_IMG_0725-1024.jpg?1396783330)

- [Previous Page](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/assembly.md)
- [Next Page](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/arduino-code.md)

## Featured Products

### INA219  High Side DC Current Sensor Breakout - 26V ±3.2A Max

[INA219  High Side DC Current Sensor Breakout - 26V ±3.2A Max](https://www.adafruit.com/product/904)
This breakout board will solve all your power-monitoring problems. Instead of struggling with two multimeters, you can just use the handy INA219 chip on this breakout to both measure both the high side voltage and DC current draw over I2C with ±1% precision.

**Please...**

In Stock
[Buy Now](https://www.adafruit.com/product/904)
[Related Guides to the Product](https://learn.adafruit.com/products/904/guides)
### STEMMA QT / Qwiic JST SH 4-pin Cable - 100mm Long

[STEMMA QT / Qwiic JST SH 4-pin Cable - 100mm Long](https://www.adafruit.com/product/4210)
This 4-wire cable is a little over 100mm / 4" long and fitted with JST-SH female 4-pin connectors on both ends. Compared with the chunkier JST-PH these are 1mm pitch instead of 2mm, but still have a nice latching feel, while being easy to insert and remove.

<a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/4210)
[Related Guides to the Product](https://learn.adafruit.com/products/4210/guides)
### STEMMA QT / Qwiic JST SH 4-pin to Premium Male Headers Cable

[STEMMA QT / Qwiic JST SH 4-pin to Premium Male Headers Cable](https://www.adafruit.com/product/4209)
This 4-wire cable is a little over 150mm / 6" long and fitted with JST-SH female 4-pin connectors on one end and premium Dupont male headers on the other. Compared with the chunkier JST-PH these are 1mm pitch instead of 2mm, but still have a nice latching feel, while being easy to insert...

In Stock
[Buy Now](https://www.adafruit.com/product/4209)
[Related Guides to the Product](https://learn.adafruit.com/products/4209/guides)
### Premium Male/Male Jumper Wires - 40 x 6" (150mm)

[Premium Male/Male Jumper Wires - 40 x 6" (150mm)](https://www.adafruit.com/product/758)
Handy for making wire harnesses or jumpering between headers on PCB's. These premium jumper wires are 6" (150mm) long and come in a 'strip' of 40 (4 pieces of each of ten rainbow colors). They have 0.1" male header contacts on either end and fit cleanly next to each other...

In Stock
[Buy Now](https://www.adafruit.com/product/758)
[Related Guides to the Product](https://learn.adafruit.com/products/758/guides)
### Full Sized Premium Breadboard - 830 Tie Points

[Full Sized Premium Breadboard - 830 Tie Points](https://www.adafruit.com/product/239)
This is a 'full-size' premium quality breadboard, 830 tie points. Good for small and medium projects. It's 2.2" x 7" (5.5 cm x 17 cm) with a standard double-strip in the middle and two power rails on both sides. You can pull the power rails off easily to make the...

In Stock
[Buy Now](https://www.adafruit.com/product/239)
[Related Guides to the Product](https://learn.adafruit.com/products/239/guides)
### Adafruit INA219 FeatherWing

[Adafruit INA219 FeatherWing](https://www.adafruit.com/product/3650)
The **INA219 FeatherWing** makes power-monitoring problems a thing of the past. Instead of struggling with two multimeters, you can just use the handy INA219&nbsp;chip on this breakout to&nbsp;measure both the high side voltage and DC current draw over I2C with 1% precision....

In Stock
[Buy Now](https://www.adafruit.com/product/3650)
[Related Guides to the Product](https://learn.adafruit.com/products/3650/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [Geofencing with the FONA 808 & Adafruit IO](https://learn.adafruit.com/geofencing-with-the-fona-808-and-adafruit-io.md)
- [Nokia 5110/3310 Monochrome LCD](https://learn.adafruit.com/nokia-5110-3310-monochrome-lcd.md)
- [Create an Internet of Things Dashboard with Adafruit IO](https://learn.adafruit.com/create-an-internet-of-things-dashboard-with-adafruit-dot-io.md)
- [Arduino Prototyping Mounting Plate](https://learn.adafruit.com/arduino-prototyping-mounting-plate.md)
- [Smart Cocktail Shaker](https://learn.adafruit.com/smart-cocktail-shaker.md)
- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [How to Build a Testing Jig](https://learn.adafruit.com/how-to-build-a-testing-fixture.md)
- [Arduino Lesson 0. Getting Started](https://learn.adafruit.com/lesson-0-getting-started.md)
- [Using NeoPixels and Servos Together](https://learn.adafruit.com/neopixels-and-servos.md)
- [Arduino Lesson 4. Eight LEDs and a Shift Register](https://learn.adafruit.com/adafruit-arduino-lesson-4-eight-leds.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [2.8" TFT Touchscreen](https://learn.adafruit.com/2-8-tft-touchscreen.md)
- [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [Multi-tasking the Arduino - Part 1](https://learn.adafruit.com/multi-tasking-the-arduino-part-1.md)
