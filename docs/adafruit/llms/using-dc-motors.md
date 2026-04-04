# Source: https://learn.adafruit.com/adafruit-motor-shield/using-dc-motors.md

# Adafruit Motor Shield

## Using DC Motors

Warning: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/899/medium800/adafruit_products_dcmotor.jpg?1396777246)

## DC motors are used for all sort of robotic projects.   

The motor shield can drive up to 4 DC motors bi-directionally. That means they can be driven forwards and backwards. The speed can also be varied at 0.5% increments using the high-quality built in PWM. This means the speed is very smooth and won't vary!

Note that the H-bridge chip is not meant for driving loads over 0.6A or that peak over 1.2A so this is for _small_ motors. Check the datasheet for information about the motor to verify its OK.

To connect a motor, simply solder two wires to the terminals and then connect them to either the **M1, M2, M3,** or **M4**. Then follow these steps in your sketch

1. Make sure you #include \<AFMotor.h\>
2. Create the AF\_DCMotor object with **AF\_DCMotor(_motor#, frequency_)**, to setup the motor H-bridge and latches. The constructor takes two arguments.   
The first is which port the motor is connected to, **1, 2, 3** or **4**.   
**_frequency_** is how fast the speed controlling signal is.   
For motors 1 and 2 you can choose **MOTOR12\_64KHZ** , **MOTOR12\_8KHZ** , **MOTOR12\_2KHZ** , or **MOTOR12\_1KHZ**. A high speed like 64KHz wont be audible but a low speed like 1KHz will use less power. Motors 3 & 4 are only possible to run at 1KHz and will ignore any setting given
3. Then you can set the speed of the motor using **setSpeed(_speed_)** where the _ **speed** _ ranges from 0 (stopped) to 255 (full speed). You can set the speed whenever you want.
4. To run the motor, call **run(_direction_)** where _ **direction** _ is **FORWARD** , **BACKWARD** or **RELEASE**. Of course, the Arduino doesn't actually know if the motor is 'forward' or 'backward', so if you want to change which way it thinks is forward, simply swap the two wires from the motor to the shield.

```
#include &lt;AFMotor.h&gt;

AF_DCMotor motor(2, MOTOR12_64KHZ); // create motor #2, 64KHz pwm

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Motor test!");
  
  motor.setSpeed(200);     // set the speed to 200/255
}

void loop() {
  Serial.print("tick");
  
  motor.run(FORWARD);      // turn it on going forward
  delay(1000);

  Serial.print("tock");
  motor.run(BACKWARD);     // the other way
  delay(1000);
  
  Serial.print("tack");
  motor.run(RELEASE);      // stopped
  delay(1000);
}
```

- [Previous Page](https://learn.adafruit.com/adafruit-motor-shield/using-stepper-motors.md)
- [Next Page](https://learn.adafruit.com/adafruit-motor-shield/af-dcmotor-class.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [All About Arduino Libraries](https://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use.md)
- [RePaper eInk Development Board](https://learn.adafruit.com/repaper-eink-development-board.md)
- [Multi-tasking the Arduino - Part 2](https://learn.adafruit.com/multi-tasking-the-arduino-part-2.md)
- [Bluetooth Controlled Motorized Camera Slider](https://learn.adafruit.com/bluetooth-motorized-camera-slider.md)
- [Electronic Demon Costume](https://learn.adafruit.com/electronic-demon-costume.md)
- [Adafruit INA219 Current Sensor Breakout](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout.md)
- [Ladyada's Learn Arduino - Lesson #2](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-2.md)
- [Arduino Lesson 6. Digital Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-6-digital-inputs.md)
- [2.2" TFT Display](https://learn.adafruit.com/2-2-tft-display.md)
- [Arduino Lesson 2. LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds.md)
- [Collin's Lab: MIDI](https://learn.adafruit.com/collins-lab-midi.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [Programming Arduino with Android and Windows Tablets](https://learn.adafruit.com/programming-arduino-with-android-and-windows-tablets.md)
