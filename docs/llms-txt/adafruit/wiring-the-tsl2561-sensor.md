# Source: https://learn.adafruit.com/tsl2561/wiring-the-tsl2561-sensor.md

# TSL2561 Luminosity Sensor

## Wiring the TSL2561 Sensor

# Breakout Board Prep

This is an easy sensor to get started with. If you have the Breakout board version, it comes with a 6-pin header strip that you can use to plug the sensor into a breadboard or perfboard. Simply plug the header into a solderless breadboard with the long pins down and short pins up. Place the sensor on top so each pad has a header pin in it and solder the two together.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/583/medium800/light_tslsolder.jpg?1396764248)

# Wiring up the sensor

Next we will connect it to our microcontroller. In this case we'll be using an Arduino but nearly any microcontroller can be used by adapting our code

- Connect the&nbsp; **VCC&nbsp;** pin to a&nbsp; **3.3V** &nbsp;or **5v** power source (Whatever the logic level of your microcontroller is!)
- Connect&nbsp; **GND** &nbsp;to the ground pin.
- Connect the&nbsp; **i2c SCL clock&nbsp;** pin to your i2c clock pin. On the classic Arduino Uno/Duemilanove/Diecimila/etc this is&nbsp; **Analog pin #5**
- Connect the&nbsp; **i2c SDA data&nbsp;** pin to your i2c data pin. On the classic Arduino Uno/Duemilanove/Diecimila/etc this is&nbsp; **Analog pin #4**

The i2c lines on most microcontrollers are fixed so you're going to have to stick with those pins.

![](https://cdn-learn.adafruit.com/assets/assets/000/036/109/medium800/light_unotsl2561.png?1475165716)

[uno + tsl2561 Fritzing diagram](https://cdn-learn.adafruit.com/assets/assets/000/036/110/original/unotsl2561.fzz?1475165730)
You don't need to connect the&nbsp; **ADDR** &nbsp;(i2c address change) or&nbsp; **INT** &nbsp;(interrupt output) pins.

The&nbsp; **ADDR** &nbsp;pin can be used if you have an i2c address conflict, to change the address. Connect it to ground to set the address to&nbsp; **0x29** , connect it to 3.3V (vcc) to se t the address to&nbsp; **0x49** &nbsp;or leave it floating (unconnected) to use address&nbsp; **0x39**.

The&nbsp; **INT&nbsp;** pin is an ouput&nbsp;_from_&nbsp;the sensor used when you have the sensor configured to signal when the light level has changed. We don't have that code written in this tutorial so you don't have to use it. If you do end up using it, use a 10K-100K pullup from&nbsp; **INT** &nbsp;to 3.3V (vcc)

- [Previous Page](https://learn.adafruit.com/tsl2561/overview.md)
- [Next Page](https://learn.adafruit.com/tsl2561/arduino-code.md)

## Featured Products

### Adafruit TSL2561 Digital Luminosity/Lux/Light Sensor Breakout

[Adafruit TSL2561 Digital Luminosity/Lux/Light Sensor Breakout](https://www.adafruit.com/product/439)
The TSL2561 luminosity sensor is an advanced digital light sensor, ideal for use in a wide range of light situations. Compared to low cost CdS cells, this sensor is more precise, allowing for exact lux calculations and can be configured for different gain/timing ranges to detect light ranges...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/439)
[Related Guides to the Product](https://learn.adafruit.com/products/439/guides)
### Flora Lux Sensor - TSL2561 Light Sensor

[Flora Lux Sensor - TSL2561 Light Sensor](https://www.adafruit.com/product/1246)
Add light-reactive sensing to your wearable Flora project with this high precision Lux sensor. The TSL2561 luminosity sensor is an advanced digital light sensor, ideal for use in a wide range of light situations. Compared to low cost CdS cells, this sensor is more precise, allowing for exact...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1246)
[Related Guides to the Product](https://learn.adafruit.com/products/1246/guides)

## Related Guides

- [Adafruit Metro M7 with microSD](https://learn.adafruit.com/adafruit-metro-m7-microsd.md)
- [Adafruit Qualia High Res Displayport Desktop Monitor](https://learn.adafruit.com/qualia-high-res-displayport-desktop-monitor.md)
- [Adafruit NeoPixel Breakout](https://learn.adafruit.com/adafruit-neopixel-breakout.md)
- [3D Printed Flexible LED Glove with Conductive Filament](https://learn.adafruit.com/3d-printed-flexible-conductive-filament-led-glove.md)
- [DC & USB Boarduino Kits](https://learn.adafruit.com/boarduino-kits.md)
- [Adafruit PDM Microphone Breakout](https://learn.adafruit.com/adafruit-pdm-microphone-breakout.md)
- [Adafruit LSM6DS33 6-DoF IMU Breakout](https://learn.adafruit.com/lsm6ds33-6-dof-imu-accelerometer-gyro.md)
- [Adafruit 7-Segment LED FeatherWings](https://learn.adafruit.com/adafruit-7-segment-led-featherwings.md)
- [Adafruit Mini TFT with Joystick Featherwing](https://learn.adafruit.com/adafruit-mini-tft-featherwing.md)
- [Adafruit QT Py CH32V203](https://learn.adafruit.com/adafruit-qt-py-ch32v203.md)
- [Pro Trinket Tachometer](https://learn.adafruit.com/pro-trinket-tachometer.md)
- [Open Sesame! A SMS-controlled door lock](https://learn.adafruit.com/open-sesame-a-sms-controlled-door-lock.md)
- [Adafruit Circuit Playground Tri-Color E-Ink Gizmo](https://learn.adafruit.com/adafruit-circuit-playground-tri-color-e-ink-gizmo.md)
- [Tent Lantern](https://learn.adafruit.com/tent-lantern.md)
- [Adafruit SCD-30 - NDIR CO2 Temperature and Humidity Sensor](https://learn.adafruit.com/adafruit-scd30.md)
