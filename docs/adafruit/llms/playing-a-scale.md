# Source: https://learn.adafruit.com/adafruit-arduino-lesson-10-making-sounds/playing-a-scale.md

# Arduino Lesson 10. Making Sounds

## Playing a Scale

For the first part of this lesson, the only thing on the breadboard is the Piezo buzzer. One pin of the piezo sounder goes to GND connection and the other to digital pin 12.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/300/medium800/learn_arduino_just_sounder.jpg?1396781468)

![](https://cdn-learn.adafruit.com/assets/assets/000/002/303/medium800/learn_arduino_fritzing.jpg?1396781518)

Program your Arduino with the following sketch:

```
/*
Adafruit Arduino - Lesson 10. Simple Sounds
*/

int speakerPin = 12;

int numTones = 10;
int tones[] = {261, 277, 294, 311, 330, 349, 370, 392, 415, 440};
//            mid C  C#   D    D#   E    F    F#   G    G#   A

void setup()
{
  for (int i = 0; i &lt; numTones; i++)
  {
    tone(speakerPin, tones[i]);
    delay(500);
  }
  noTone(speakerPin);
}

void loop()
{
}
```

To play a note of a particular pitch, you specify the frequency. See the following section on sound. The different frequencies for each note are kept in an array. An array is like a list. So, a scale can be played by playing each of the notes in the list in turn.

The 'for' loop will count from 0 to 9 using the variable 'i'. To get the frequency of the note to play at each step, we use 'tone[i]'. This means, the value in the 'tones' array at position 'i'. So, for example, 'tones[0]' is 261, 'tones[1]' is 277 etc.

The Arduino command 'tone' takes two parameters, the first is the pin to play the tone on and the second is the frequency of the tone to play.

When all the notes have been played, the 'noTone' command stops that pin playing any tone.

We could have put the tone playing code into 'loop' rather than 'setup', but frankly the same scale being played over and over again gets a bit tiresome. So in this case, 'loop' is empty.

To play the tune again, just press the reset button.

- [Previous Page](https://learn.adafruit.com/adafruit-arduino-lesson-10-making-sounds/parts.md)
- [Next Page](https://learn.adafruit.com/adafruit-arduino-lesson-10-making-sounds/sound.md)

## Featured Products

### Piezo Buzzer

[Piezo Buzzer](https://www.adafruit.com/product/160)
Piezo buzzers are used for making beeps, tones and alerts. This one is petite but loud! Drive it with 3-30V peak-to-peak square wave. To use, connect one pin to ground (either one) and the other pin to a square wave out from a timer or microcontroller. For the loudest tones, stay around 4 KHz,...

In Stock
[Buy Now](https://www.adafruit.com/product/160)
[Related Guides to the Product](https://learn.adafruit.com/products/160/guides)
### Photo cell (CdS photoresistor)

[Photo cell (CdS photoresistor)](https://www.adafruit.com/product/161)
CdS cells are little light sensors. As the squiggly face is exposed to more light, the resistance goes down. When it's light, the resistance is about ~1KΩ, when dark it goes up to ~10KΩ.

To use, connect one side of the photocell (either one, it's symmetric) to power...

In Stock
[Buy Now](https://www.adafruit.com/product/161)
[Related Guides to the Product](https://learn.adafruit.com/products/161/guides)
### Premium Male/Male Jumper Wires - 40 x 6" (150mm)

[Premium Male/Male Jumper Wires - 40 x 6" (150mm)](https://www.adafruit.com/product/758)
Handy for making wire harnesses or jumpering between headers on PCB's. These premium jumper wires are 6" (150mm) long and come in a 'strip' of 40 (4 pieces of each of ten rainbow colors). They have 0.1" male header contacts on either end and fit cleanly next to each other...

In Stock
[Buy Now](https://www.adafruit.com/product/758)
[Related Guides to the Product](https://learn.adafruit.com/products/758/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [Multi-tasking the Arduino - Part 2](https://learn.adafruit.com/multi-tasking-the-arduino-part-2.md)
- [Adafruit  PCA9685 16-Channel Servo Driver](https://learn.adafruit.com/16-channel-pwm-servo-driver.md)
- [Adafruit CC3000 WiFi and Xively](https://learn.adafruit.com/adafruit-cc3000-wifi-and-xively.md)
- [Trellis 3D Printed Enclosure](https://learn.adafruit.com/trellis-3d-printed-enclosure.md)
- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [Smart Measuring Cup](https://learn.adafruit.com/smart-measuring-cup.md)
- [0.96" mini Color OLED](https://learn.adafruit.com/096-mini-color-oled.md)
- [Adafruit Analog Accelerometer Breakouts](https://learn.adafruit.com/adafruit-analog-accelerometer-breakouts.md)
- [Circuit Playground: D is for Diode](https://learn.adafruit.com/circuit-playground-d-is-for-diode.md)
- [TMP36 Temperature Sensor](https://learn.adafruit.com/tmp36-temperature-sensor.md)
- [RGB LED Matrix Basics](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix.md)
- [Automatic Monitor Color Temperature Adjustment](https://learn.adafruit.com/automatic-monitor-color-temperature-adjustment.md)
- [Line Following Zumo Robot Using Simulink](https://learn.adafruit.com/line-following-zumo-robot-programmed-with-simulink.md)
- [Wireless Game Show Poppers for the Classroom!](https://learn.adafruit.com/wireless-game-show-poppers.md)
- [Arduino Lesson 4. Eight LEDs and a Shift Register](https://learn.adafruit.com/adafruit-arduino-lesson-4-eight-leds.md)
