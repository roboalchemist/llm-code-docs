# Source: https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/wippersnapper.md

# Adafruit INA219 Current Sensor Breakout

## WipperSnapper

group_elements = page.element_group_for(element).try(:elements) || []
group_elements.each_with_index do |group_element, i|
  markdown.partial("elements/#{group_element.element_type}", locals: {
    page: page,
    element: present(group_element),
    elements: group_elements,
    i: i,
    add_links: true
  })
end
## What is WipperSnapper

WipperSnapper is a firmware designed to turn any WiFi-capable board into an Internet-of-Things device without programming a single line of code. WipperSnapper connects to [Adafruit IO](https://io.adafruit.com/), a web&nbsp;platform designed ([by Adafruit!](https://www.adafruit.com/about)) to&nbsp;_display_,&nbsp;_respond_, and&nbsp;_interact_&nbsp;with your project's data.

Simply load the WipperSnapper firmware onto your board, add credentials, and plug it into power. Your board will automatically register itself with your Adafruit IO account.

From there, you can add&nbsp;_components_&nbsp;to your board such as buttons, switches, potentiometers, sensors, and more! Components are&nbsp;_dynamically&nbsp;_added to hardware, so you can&nbsp;immediately start interacting, logging, and streaming the data your projects produce without writing code.

If you've never used WipperSnapper, click below to read through the quick start guide before continuing.

[Quickstart: Adafruit IO WipperSnapper](https://learn.adafruit.com/quickstart-adafruit-io-wippersnapper)
## Wiring
group_elements = page.element_group_for(element).try(:elements) || []
group_elements.each_with_index do |group_element, i|
  markdown.partial("elements/#{group_element.element_type}", locals: {
    page: page,
    element: present(group_element),
    elements: group_elements,
    i: i,
    add_links: true
  })
end
## Usage

Connect your board to Adafruit IO Wippersnapper and **[navigate to the WipperSnapper board list](https://io.adafruit.com/wippersnapper).**

On this page, **select the WipperSnapper board you're using** to be brought to the board's interface page.

group_elements = page.element_group_for(element).try(:elements) || []
group_elements.each_with_index do |group_element, i|
  markdown.partial("elements/#{group_element.element_type}", locals: {
    page: page,
    element: present(group_element),
    elements: group_elements,
    i: i,
    add_links: true
  })
end
If you do not see your board listed here - you need [to connect your board to Adafruit IO](https://learn.adafruit.com/quickstart-adafruit-io-wippersnapper) first.

group_elements = page.element_group_for(element).try(:elements) || []
group_elements.each_with_index do |group_element, i|
  markdown.partial("elements/#{group_element.element_type}", locals: {
    page: page,
    element: present(group_element),
    elements: group_elements,
    i: i,
    add_links: true
  })
end
Next, make sure the sensor is plugged into your board and click the **&nbsp;I2C Scan&nbsp;** button.

![](https://cdn-learn.adafruit.com/assets/assets/000/113/177/medium800/sensor_page_crop_scan.png?1657724520)

group_elements = page.element_group_for(element).try(:elements) || []
group_elements.each_with_index do |group_element, i|
  markdown.partial("elements/#{group_element.element_type}", locals: {
    page: page,
    element: present(group_element),
    elements: group_elements,
    i: i,
    add_links: true
  })
end
group_elements = page.element_group_for(element).try(:elements) || []
group_elements.each_with_index do |group_element, i|
  markdown.partial("elements/#{group_element.element_type}", locals: {
    page: page,
    element: present(group_element),
    elements: group_elements,
    i: i,
    add_links: true
  })
end
###  I don't see the sensor's I2C address listed! 


First, double-check the connection and/or wiring between the sensor and the board.

Then, reset the board and let it re-connect to Adafruit IO WipperSnapper.

With the sensor detected in an I2C scan, you're ready to add the sensor to your board.

**Click the New Component button or the + button** to bring up the component picker.

group_elements = page.element_group_for(element).try(:elements) || []
group_elements.each_with_index do |group_element, i|
  markdown.partial("elements/#{group_element.element_type}", locals: {
    page: page,
    element: present(group_element),
    elements: group_elements,
    i: i,
    add_links: true
  })
end
![](https://cdn-learn.adafruit.com/assets/assets/000/127/931/medium800/sensor_page_temperature___humidity_06_AddComponent.png?1708631009)

group_elements = page.element_group_for(element).try(:elements) || []
group_elements.each_with_index do |group_element, i|
  markdown.partial("elements/#{group_element.element_type}", locals: {
    page: page,
    element: present(group_element),
    elements: group_elements,
    i: i,
    add_links: true
  })
end
group_elements = page.element_group_for(element).try(:elements) || []
group_elements.each_with_index do |group_element, i|
  markdown.partial("elements/#{group_element.element_type}", locals: {
    page: page,
    element: present(group_element),
    elements: group_elements,
    i: i,
    add_links: true
  })
end
Your device interface should now show the sensor components you created. After the interval you configured elapses, WipperSnapper will automatically read values from the sensor(s) and send them to Adafruit IO.

group_elements = page.element_group_for(element).try(:elements) || []
group_elements.each_with_index do |group_element, i|
  markdown.partial("elements/#{group_element.element_type}", locals: {
    page: page,
    element: present(group_element),
    elements: group_elements,
    i: i,
    add_links: true
  })
end
To view the data that has been logged from the sensor, click on the graph next to the sensor name.

group_elements = page.element_group_for(element).try(:elements) || []
group_elements.each_with_index do |group_element, i|
  markdown.partial("elements/#{group_element.element_type}", locals: {
    page: page,
    element: present(group_element),
    elements: group_elements,
    i: i,
    add_links: true
  })
end
Here you can see the feed history and edit things about the feed such as the name, privacy, webhooks associated with the feed and more. If you want to learn more about how feeds work, [check out this page](https://learn.adafruit.com/all-the-internet-of-things-episode-four-adafruit-io/advanced-feeds).

group_elements = page.element_group_for(element).try(:elements) || []
group_elements.each_with_index do |group_element, i|
  markdown.partial("elements/#{group_element.element_type}", locals: {
    page: page,
    element: present(group_element),
    elements: group_elements,
    i: i,
    add_links: true
  })
end
- [Previous Page](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/python-circuitpython.md)
- [Next Page](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/downloads.md)

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
