# Source: https://learn.adafruit.com/adafruit-motor-shield/using-stepper-motors.md

# Adafruit Motor Shield

## Using Stepper Motors

Warning: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/900/medium800/adafruit_products_bipolar.jpg?1396777256)

Stepper motors are great for (semi-)precise control, perfect for many robot and CNC projects. This motor shield supports up to 2 stepper motors. The library works identically for bi-polar and uni-polar motors

For unipolar motors: to connect up the stepper, first figure out which pins connected to which coil, and which pins are the center taps. If its a 5-wire motor then there will be 1 that is the center tap for both coils. [Theres plenty of tutorials online on how to reverse engineer the coils pinout.](http://learn.adafruit.com/adafruit-motor-shield/resources) The center taps should both be connected together to the GND terminal on the motor shield output block. then coil 1 should connect to one motor port (say M1 or M3) and coil 2 should connect to the other motor port (M2 or M4).

For bipolar motors: its just like unipolar motors except theres no 5th wire to connect to ground. The code is exactly the same.

Running a stepper is a little more intricate than running a DC motor but its still very easy

1. Make sure you #include \<AFMotor.h\>
2. Create the stepper motor object with **AF\_Stepper(_steps_**_, **stepper#** _**)** to setup the motor H-bridge and latches. _ **Steps** _ indicates how many steps per revolution the motor has. a 7.5degree/step motor has 360/7.5 = 48 steps. _ **Stepper#** _ is which port it is connected to. If you're using M1 and M2, its port 1. If you're using M3 and M4 it's port 2
3. Set the speed of the motor using **setSpeed(_rpm_)** where _ **rpm** _ is how many revolutions per minute you want the stepper to turn.
4. Then every time you want the motor to move, call the **step(_#steps_, _direction_, _steptype_)** procedure._ **#steps** _ is how many steps you'd like it to take **. _direction_** is either **FORWARD** or **BACKWARD** and the step type is **SINGLE, DOUBLE. INTERLEAVE** or **MICROSTEP**.  
"Single" means single-coil activation, "double" means 2 coils are activated at once (for higher torque) and "interleave" means that it alternates between single and double to get twice the resolution (but of course its half the speed). "Microstepping" is a method where the coils are PWM'd to create smooth motion between steps. Theres tons of [information about the pros and cons of these different stepping methods in the resources page.](http://learn.adafruit.com/adafruit-motor-shield/resources "Link: http://learn.adafruit.com/adafruit-motor-shield/resources")  
You can use whichever stepping method you want, changing it "on the fly" to as you may want minimum power, more torque, or more precision.
5. By default, the motor will 'hold' the position after its done stepping. If you want to release all the coils, so that it can spin freely, call **release()**
6. The stepping commands are 'blocking' and will return once the steps have finished.

Because the stepping commands 'block' - you have to instruct the Stepper motors each time you want them to move. If you want to have more of a 'background task' stepper control, [check out AccelStepper library](https://github.com/adafruit/AccelStepper) (install similarly to how you did with AFMotor) which has some examples for controlling two steppers simultaneously with varying accelleration  
```
#include &lt;AFMotor.h&gt;


AF_Stepper motor(48, 2);


void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Stepper test!");

  motor.setSpeed(10);  // 10 rpm   

  motor.step(100, FORWARD, SINGLE); 
  motor.release();
  delay(1000);
}

void loop() {
  motor.step(100, FORWARD, SINGLE); 
  motor.step(100, BACKWARD, SINGLE); 

  motor.step(100, FORWARD, DOUBLE); 
  motor.step(100, BACKWARD, DOUBLE);

  motor.step(100, FORWARD, INTERLEAVE); 
  motor.step(100, BACKWARD, INTERLEAVE); 

  motor.step(100, FORWARD, MICROSTEP); 
  motor.step(100, BACKWARD, MICROSTEP); 
}
```

- [Previous Page](https://learn.adafruit.com/adafruit-motor-shield/using-rc-servos.md)
- [Next Page](https://learn.adafruit.com/adafruit-motor-shield/using-dc-motors.md)

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
