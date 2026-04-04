# Source: https://learn.adafruit.com/adafruit-arduino-lesson-1-blink/how-blink-works.md

# Arduino Lesson 1. Blink

## How 'Blink' Works

Here is the code for the Blink sketch.

```
/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 13;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);               // wait for a second
}
```

The first thing to note is that quite a lot of this sketch is what is called 'comments'. Comments are not actual program instructions, they are just comments about how the program works. They are there for out benefit, so that there is some explanation to accompany the sketch.  
  
Everything between /\* and \*/ at the top of the sketch is a block comment, that explains what the sketch is for.  
  
There are also single line comments that start with // and everything up intil the end of the line counts as being a comment.  
  
The first actual line of code is:

```
int led = 13;
```

As the comment above explains, this is giving a name to the pin that the LED is attached to. This is 13 on most Arduinos, including the Uno and Leonardo.  
  
Next, we have the 'setup' function. Again, as the comment says, this is run when the reset button is pressed. It is also run whenever the board resets for any reason, such as power first being applied to it, or after a sketch has been uploaded.

```
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
}
```

Every Arduino sketch must have a 'setup' function, and the part of it where you might want to add instructions of your own is between the { and the }.  
  
In this case, there is just one command there, which, as the comment states tells the Arduino board that we are going to use the LED pin as an output.  
  
It is also mandatory for a sketch to have a 'loop' function. **Unlike the 'setup' function that only runs once, after a reset, the 'loop' function will, after it has finished running its commands, immediately start again.**

```
void loop() {
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);               // wait for a second
}
```

Inside the loop function, the commands first of all turn the LED pin on (HIGH), then 'delay' for 1000 milliseconds (1 second), then turn the LED pin off and pause for another second.

- [Previous Page](https://learn.adafruit.com/adafruit-arduino-lesson-1-blink/uploading-blink-to-the-board.md)
- [Next Page](https://learn.adafruit.com/adafruit-arduino-lesson-1-blink/blinking-faster.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### USB Cable - Standard A-B

[USB Cable - Standard A-B](https://www.adafruit.com/product/62)
This here is your standard A-B USB cable, for USB 1.1 or 2.0. Perfect for connecting a PC to your Arduino, USBtinyISP (among other things).  
  
3 feet / 1 meter long  
  
Color may vary!

In Stock
[Buy Now](https://www.adafruit.com/product/62)
[Related Guides to the Product](https://learn.adafruit.com/products/62/guides)

## Related Guides

- [WiFi Weather Station](https://learn.adafruit.com/wifi-weather-station-arduino-cc3000.md)
- [Naughty or Nice Machine](https://learn.adafruit.com/naughty-or-nice-machine.md)
- [Adafruit VS1053 MP3/AAC/Ogg/MIDI/WAV Codec Breakout Tutorial](https://learn.adafruit.com/adafruit-vs1053-mp3-aac-ogg-midi-wav-play-and-record-codec-tutorial.md)
- [How to program a Zumo Robot with Simulink](https://learn.adafruit.com/zumo-robot-control-with-simulink.md)
- [DIY 8x2 LCD Shield](https://learn.adafruit.com/diy-8x2-lcd-shield.md)
- [3D Printed Animatronic Robot Head](https://learn.adafruit.com/3d-printed-animatronic-robot-head.md)
- [Arduino Lesson 7. Make an RGB LED Fader](https://learn.adafruit.com/adafruit-arduino-lesson-7-make-an-rgb-led-fader.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [Light Meter](https://learn.adafruit.com/light-meter.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [Trellis 3D Printed Enclosure](https://learn.adafruit.com/trellis-3d-printed-enclosure.md)
- [Deciphering Strange Arduino Code](https://learn.adafruit.com/deciphering-strange-arduino-code.md)
- [Collin's Lab: MIDI](https://learn.adafruit.com/collins-lab-midi.md)
- [Tiny Arduino Music Visualizer](https://learn.adafruit.com/piccolo.md)
- [Adafruit Music Maker Shield](https://learn.adafruit.com/adafruit-music-maker-shield-vs1053-mp3-wav-wave-ogg-vorbis-player.md)
