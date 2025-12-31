# Source: https://learn.sparkfun.com/tutorials/pulse-width-modulation

## What is Pulse-width Modulation?

[Pulse Width Modulation](http://en.wikipedia.org/wiki/Pulse-width_modulation) (PWM) is a fancy term for describing a type of digital signal. Pulse width modulation is used in a variety of applications including sophisticated control circuitry. A common way we use them here at SparkFun is to control dimming of [RGB LEDs](https://www.sparkfun.com/products/105) or to control the direction of a [servo](https://www.sparkfun.com/servos). We can accomplish a range of results in both applications because pulse width modulation allows us to vary how much time the signal is high in an analog fashion. While the signal can only be high (usually 5V) or low (ground) at any time, we can change the proportion of time the signal is high compared to when it is low over a consistent time interval.

[![Two servo motors used to control the pan/tilt of a robotic claw with PWM](//cdn.sparkfun.com/assets/8/2/c/8/3/512e85a6ce395f4d64000000.jpg)](//cdn.sparkfun.com/assets/8/2/c/8/3/512e85a6ce395f4d64000000.jpg)

*Robotic claw controlled by a servo motor using pulse-width modulation*

### Suggested Reading

Some background tutorials you might consider first:

- [Voltage, Current, Resistance, and Ohm\'s Law](http://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
- [Analog vs Digital](https://learn.sparkfun.com/tutorials/analog-vs-digital)
- [Voltage Dividers](https://learn.sparkfun.com/tutorials/voltage-dividers)
- [Digital Logic](https://learn.sparkfun.com/tutorials/digital-logic)

## Duty Cycle

When the signal is high, we call this \"on time\". To describe the amount of \"on time\" , we use the concept of duty cycle. Duty cycle is measured in percentage. The percentage duty cycle specifically describes the percentage of time a digital signal is on over an interval or period of time. This period is the inverse of the frequency of the waveform.

If a digital signal spends half of the time on and the other half off, we would say the digital signal has a duty cycle of 50% and resembles an ideal square wave. If the percentage is higher than 50%, the digital signal spends more time in the high state than the low state and vice versa if the duty cycle is less than 50%. Here is a graph that illustrates these three scenarios:

[![Duty Cycle Percentage reflects percentage of \'on\' time per interval](//cdn.sparkfun.com/assets/f/9/c/8/a/512e869bce395fbc64000002.JPG)](//cdn.sparkfun.com/assets/f/9/c/8/a/512e869bce395fbc64000002.JPG)

*50%, 75%, and 25% Duty Cycle Examples*

100% duty cycle would be the same as setting the voltage to 5 Volts (high). 0% duty cycle would be the same as grounding the signal.

## Examples

You can control the brightness of an LED by adjusting the duty cycle.

[![Three dim LEDs](//cdn.sparkfun.com/assets/4/a/f/c/e/512e8754ce395fac64000000.jpg)](//cdn.sparkfun.com/assets/4/a/f/c/e/512e8754ce395fac64000000.jpg)

*PWM used to control LED brightness*

With an [RGB (red green blue) LED](https://www.sparkfun.com/products/105), you can control how much of each of the three colors you want in the mix of color by dimming them with various amounts.

[![Red + Blue = Purple\... etc](//cdn.sparkfun.com/assets/c/f/a/7/e/51479890ce395f1f2f000000.jpg)](//cdn.sparkfun.com/assets/c/f/a/7/e/51479890ce395f1f2f000000.jpg)

*Basics of color mixing*

If all three are on in equal amounts, the result will be white light of varying brightness. Blue equally mixed with green will get teal. As slightly more complex example, try turning red fully on, and green 50% duty cycle and blue fully off to get an orange color.

[![pick a color in the spectrum, then use PWM to achieve it](//cdn.sparkfun.com/assets/b/9/f/f/8/512e8756ce395f8e60000000.jpg)](//cdn.sparkfun.com/assets/b/9/f/f/8/512e8756ce395f8e60000000.jpg)

*PWM can be used to mix RGB color*

The frequency of the square wave does need to be sufficiently high enough when controlling LEDs to get the proper dimming effect. A 20% duty cycle wave at 1 Hz will be obvious that it's turning on and off to your eyes meanwhile, 20% duty cycle at 100 Hz or above will just look dimmer than fully on. Essentially, the period can not be too large if you're aiming for a dimming effect with the LEDs.

You can also use pulse width modulation to control the angle of a servo motor attached to something mechanical like a robot arm. Servos have a shaft that turns to specific position based on its control line. Our [servo motors](https://www.sparkfun.com/products/9347) have a range of about 180 degrees.

Frequency/period are specific to controlling a specific servo. A typical servo motor expects to be updated every 20 ms with a pulse between 1 ms and 2 ms, or in other words, between a 5 and 10% duty cycle on a 50 Hz waveform. With a 1.5 ms pulse, the servo motor will be at the natural 90 degree position. With a 1 ms pulse, the servo will be at the 0 degree position, and with a 2 ms pulse, the servo will be at 180 degrees. You can obtain the full range of motion by updating the servo with an value in between.

[![Servo Motor at a controlled specific angle](//cdn.sparkfun.com/assets/a/6/7/4/e/512e8755ce395fc264000000.jpg)](//cdn.sparkfun.com/assets/a/6/7/4/e/512e8755ce395fc264000000.jpg)

*PWM used to hold a servo motor at 90 degrees relative to its bracket*