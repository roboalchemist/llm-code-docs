# Source: https://learn.adafruit.com/ir-sensor/ir-remote-signals.md

# IR Sensor

## IR Remote Signals

Now we know that the sensor works, we want to figure out whats being sent right? But before we do that let's first examine exactly how data is being sent from the IR remote (in your hand) to the IR receiving sensor (on the breadboard)

For this example we will use the Sony power on/off IR code from a Sony TV remote. Its very simple and commonly documented!

Lets pretend we have a Sony remote, and we can look at exactly what light is being blasted out of the IR LED. We'll hookup a basic light sensor (like a basic photocell!) and listen in. We won't use a decoder like a PNA4602 (just yet) because we want to see the undecoded signal. What we see is the following:

![](https://cdn-learn.adafruit.com/assets/assets/000/000/551/medium800/light_sonycodepulses.jpg?1396763963)

Basically we see pulses or IR signal. the yellow 'blocks' are when the IR LED is transmitting and when there is only a line, the IR LED is off. (Note that the voltage being at 3VDC is just because of the way I hooked up the sensor, if I had swapped the pullup for a pulldown it would be at ground.)

The first 'block' is about 2.5ms long (see the cursors and the measurement on the side)

If you zoom into one of those blocks…

![](https://cdn-learn.adafruit.com/assets/assets/000/000/552/medium800/light_sonycodepulsezoom.jpg?1396763967)

You see that they're not really 'blocks' but actually very fast pulses!

If you zoom in all the way…

![](https://cdn-learn.adafruit.com/assets/assets/000/000/553/medium800/light_sonycodepwm.jpg?1396763974)

You can measure the frequency of the IR pulses. As you can tell by the cursors and the measurements on the side, the frequency is about 37.04KHz

OK so now we can understand how IR codes are sent. The IR transmitter LED is quickly pulsed (PWM - pulse width modulated) at a high frequency of 38KHz and then that PWM is likewise pulsed on and off much slower, at times that are about 1-3 ms long.

Why not have the LED just on and off? Why have PWM 'carrier' pulsing? Many reasons!

One reason is that this lets the LED cool off. IR LEDs can take up to 1 Amp (1000 milliamps!) of current. Most LEDs only take 20mA or so. This means IR LEDs are designed for high-power blasting BUT they can only take it for a few microseconds. By PWM'ing it, you let the LED cool off half the time

Another reason is that the TV will only listen to certain frequencies of PWM. So a Sony remote at 37KHz wont be able to work with a JVC DVD player that only wants say 50KHz.

Finally, the most important reason is that by pulsing a carrier wave, you reduce the affects of ambient lighting. The TV only looks for changes in light levels that clock in around 37KHz. Just like its easier for us to tell differences between audio tones than to pin down the precsise pitch of a tone (well, for most people at least)

OK so now we know the carrier frequency. Its 37KHz. Next lets find the pulse widths!

Looking back at the first scope picture

![](https://cdn-learn.adafruit.com/assets/assets/000/000/554/medium800/light_sonycodepulses.jpg?1396763981)

The first pulse is 2.5ms. We can use the cursors to measure the remaining pulses. I'll spare you the 12 images and let you know that the pulses are:| **PWM ON** | **OFF** |
| 2.4 ms | 0.6 ms |
| 1.2 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 1.2 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 1.2 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 1.2 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 0.6 ms | 0.6 ms |
| 0.6 ms | 270 ms |

So lets say you don't have a $1000 oscilloscope, how else can you read these signals? Well the IR decoder such as the PNA4602 does us one favor, it 'filters out' the 38KHz signal so that we only get the big chunks of signal in the milliscond range. This is much easier for a microcontroller to handle. Thats what we'll do in the next section!- [Previous Page](https://learn.adafruit.com/ir-sensor/testing-an-ir-sensor.md)
- [Next Page](https://learn.adafruit.com/ir-sensor/using-an-ir-sensor.md)

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
