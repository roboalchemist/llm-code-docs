# Source: https://learn.adafruit.com/ir-sensor/testing-an-ir-sensor.md

# IR Sensor

## Testing an IR Sensor

Because there is a semiconductor/chip inside the sensor, it must be powered with 3 - 5V to function. Contrast this to photocells and FSRs where they act like resistors and thus can be simply tested with a multimeter.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/549/medium800/light_pna4602pinout.gif?1447976100)

Here we will connect the detector as such:

- Pin 1 is the output so we wire this to a visible LED and resistor
- Pin 2 is ground
- Pin 3 is VCC, connect to 3-5V

When the detector sees IR signal, it will pull the output low, turning on the LED - since the LED is red its much easier for us to see than IR!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/550/medium800/light_irremotetest.gif?1447976110)

We will use 4xAA 1.3V batteries (I use NiMH) so that the voltage powering the sensor is about 4V.

2 batteries (3V) may be too little. 3 Batteries should be fine if you have a triple-AA holder

You can also get 5V from a microcontroller like an Arduino if you have one around. Ground goes to the middle pin.

The positive (longer) head of the Red LED connects to the +6V pin and the negative (shorter lead) connects through a 200 to 1000 ohm resistor to the first pin on the IR sensor.

Now grab any remote control like for a TV, DVD, computer, etc. and point it at the detector while pressing some buttons, you should see the LED blink a couple times whenever the remote is pressed.

- [Previous Page](https://learn.adafruit.com/ir-sensor/overview.md)
- [Next Page](https://learn.adafruit.com/ir-sensor/ir-remote-signals.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### IR (Infrared) Receiver Sensor

[IR (Infrared) Receiver Sensor](https://www.adafruit.com/product/157)
IR sensor tuned to 38KHz, perfect for receiving commands from a TV remote control. Runs at 3V to 5V so it's great for any microcontroller.  
  
To use, connect pin 3 (all the way to the right) to 5V power, pin 2 (middle) to ground and listen on pin 1. It doesn't do any decoding...

In Stock
[Buy Now](https://www.adafruit.com/product/157)
[Related Guides to the Product](https://learn.adafruit.com/products/157/guides)
### Super-bright 5mm IR LED

[Super-bright 5mm IR LED](https://www.adafruit.com/product/387)
Infrared LEDs are used for remote controls (they're the little LED in the part you point at your TV) and 'night-vision' cameras, and these little blue guys are high powered ones! They are 940nm wavelength, which is what nearly all devices listen to. They're 20 degree beamwidth,...

In Stock
[Buy Now](https://www.adafruit.com/product/387)
[Related Guides to the Product](https://learn.adafruit.com/products/387/guides)
### Mini Remote Control

[Mini Remote Control](https://www.adafruit.com/product/389)
This little remote control would be handy for controlling a robot or other project from across the room. It has 21 buttons and a layout we thought was handy: directional buttons and number entry buttons. The remote uses the NEC encoding type and sends data codes 0 thru 26 (it skips #3, #7,...

In Stock
[Buy Now](https://www.adafruit.com/product/389)
[Related Guides to the Product](https://learn.adafruit.com/products/389/guides)
### Super-bright 5mm IR LED (25 pack)

[Super-bright 5mm IR LED (25 pack)](https://www.adafruit.com/product/388)
Infrared LEDs are used for remote controls (they're the little LED in the part you point at your TV) and 'night-vision' cameras, and these little blue guys are high powered ones! They are 940nm wavelength, which is what nearly all devices listen to. They're 20 degree beamwidth,...

In Stock
[Buy Now](https://www.adafruit.com/product/388)
[Related Guides to the Product](https://learn.adafruit.com/products/388/guides)
### Adafruit METRO 328 - Arduino Compatible - with Headers

[Adafruit METRO 328 - Arduino Compatible - with Headers](https://www.adafruit.com/product/2488)
This is the&nbsp; **Adafruit METRO Arduino-Compatible - with&nbsp;headers.&nbsp;** It's a fully assembled and tested microcontroller and physical computing board with through-hole headers attached.&nbsp; If you don't want a&nbsp;Metro with the headers attached for...

In Stock
[Buy Now](https://www.adafruit.com/product/2488)
[Related Guides to the Product](https://learn.adafruit.com/products/2488/guides)

## Related Guides

- [RePaper eInk Development Board](https://learn.adafruit.com/repaper-eink-development-board.md)
- [Adafruit MSA301 Triple Axis Accelerometer](https://learn.adafruit.com/msa301-triple-axis-accelerometer.md)
- [Bluetooth Controlled Motorized Camera Slider](https://learn.adafruit.com/bluetooth-motorized-camera-slider.md)
- [Adafruit  PCA9685 16-Channel Servo Driver](https://learn.adafruit.com/16-channel-pwm-servo-driver.md)
- [Adalight Project Pack](https://learn.adafruit.com/adalight-diy-ambient-tv-lighting.md)
- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
- [Introducing Adafruit Trellis ](https://learn.adafruit.com/adafruit-trellis-diy-open-source-led-keypad.md)
- [Sending an SMS with Temboo](https://learn.adafruit.com/sending-an-sms-with-temboo.md)
- [20mm LED Pixels](https://learn.adafruit.com/20mm-led-pixels.md)
- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [Character LCDs](https://learn.adafruit.com/character-lcds.md)
- [Smart Measuring Cup](https://learn.adafruit.com/smart-measuring-cup.md)
- [Memories of an Arduino](https://learn.adafruit.com/memories-of-an-arduino.md)
- [Arduino Lesson 2. LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds.md)
- [Smart Cocktail Shaker](https://learn.adafruit.com/smart-cocktail-shaker.md)
