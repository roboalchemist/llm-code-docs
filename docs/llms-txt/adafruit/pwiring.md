# Source: https://learn.adafruit.com/36mm-led-pixels/pwiring.md

# 36mm LED Pixels

## Wiring

The “magic” of&nbsp;these pixels is that they're digitally controlled…even though there are only two control lines, you can have as many pixels as you’d like in a single long strand, yet each remains independently controllable.

Though it looks like the 4-conductor ribbon cable is continuous,&nbsp;_it isn't!_&nbsp;The pixels have a distinct “in” and “out” side. Data from the microcontroller arrives on the input side, where it’s received by the driver chip. The output side then connects to the input of the next pixel, all the way down the line.

When connecting these pixels to a microcontroller, make sure you're connecting to the strand's&nbsp; **input** &nbsp;pins! On these large pixels, it's easy to spot: examine the circuit board, looking for the "IN" label and an arrow indicating the direction of data flow. If connecting multiple strands together, make sure the output of one strand goes to the input of the next.![](https://cdn-learn.adafruit.com/assets/assets/000/001/138/medium800/led_pixels_36mm-io.jpg?1396769148)

The pixel strands&nbsp;include plugs&nbsp;for joining multiple strands, plus two wires for connecting power:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/139/medium800/led_pixels_36mm-power.jpg?1396769156)

Wiring is pretty easy since there are only 4 wires. The only important thing is that you should not try to power the LED strand from the Arduino's 5V line — these LEDs require a dedicated 12V source separate from the microcontroller.

Use this diagram with the red wire going to +12V from the power supply, green (serial clock) to Arduino digital pin 3, yellow (serial data) to digital pin 2, and black to both the ground connection on the power supply and any available GND pin on the Arduino.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/140/medium800/led_pixels_arduinowiring12v.png?1396769173)

Our Arduino library can use any two pins, but the examples are written to use pins 2 and 3 as above.

- [Previous Page](https://learn.adafruit.com/36mm-led-pixels/project-ideas.md)
- [Next Page](https://learn.adafruit.com/36mm-led-pixels/powering.md)

## Featured Products

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
### 12V 5A switching power supply

[12V 5A switching power supply](https://www.adafruit.com/product/352)
This is a beefy switching supply, for when you need a lot of power! It can supply 12V DC up to 5 Amps, running from 110V or 220V power (the plug it comes with is for US/Canada/Japan but you can use any plug adapter for your country, or just replace the cable with a standard 'figure-8'...

In Stock
[Buy Now](https://www.adafruit.com/product/352)
[Related Guides to the Product](https://learn.adafruit.com/products/352/guides)
### 36mm  Square 12V Digital RGB LED Pixels (Strand of 20)

[36mm  Square 12V Digital RGB LED Pixels (Strand of 20)](https://www.adafruit.com/product/683)
RGB Pixels are digitally-controllable lights you can set to any color, or animate. Each metal 'pixel square' contains 4 RGB LEDs and a controller chip soldered to a PCB. The pixel is then 'flooded' with epoxy to make it water resistant, however we cannot say 100% waterproof you...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/683)
[Related Guides to the Product](https://learn.adafruit.com/products/683/guides)

## Related Guides

- [Adafruit Data Logger Shield](https://learn.adafruit.com/adafruit-data-logger-shield.md)
- [Track Your Treats: Halloween Candy GPS Tracker](https://learn.adafruit.com/track-your-treats-halloween-candy-gps-tracker.md)
- [Adafruit 1.27" and 1.5" Color OLED Breakout Board](https://learn.adafruit.com/adafruit-1-5-color-oled-breakout-board.md)
- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [Adafruit 16-channel PWM/Servo Shield](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield.md)
- [Light Meter](https://learn.adafruit.com/light-meter.md)
- [Cloud Thermometer](https://learn.adafruit.com/cloud-thermometer.md)
- [Character LCDs](https://learn.adafruit.com/character-lcds.md)
- [Ladyada's Learn Arduino - Lesson #0](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-0.md)
- [Program an AVR or Arduino Using Raspberry Pi GPIO](https://learn.adafruit.com/program-an-avr-or-arduino-using-raspberry-pi-gpio-pins.md)
- [Arduino Lesson 17. Email Sending Movement Detector](https://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector.md)
- [Arduino Prototyping Mounting Plate](https://learn.adafruit.com/arduino-prototyping-mounting-plate.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [All About Arduino Libraries](https://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use.md)
- [Trainable Robotic Arm](https://learn.adafruit.com/trainable-robotic-arm.md)
