# Source: https://learn.adafruit.com/adafruit-arduino-lesson-5-the-serial-monitor/the-serial-monitor.md

# Arduino Lesson 5. The Serial Monitor

## The Serial Monitor

Upload the following sketch to your Arduino. Later on, we will see exactly how it works.

```
/*
Adafruit Arduino - Lesson 5. Serial Monitor
*/

int latchPin = 5;
int clockPin = 6;
int dataPin = 4;

byte leds = 0;

void setup() 
{
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);  
  pinMode(clockPin, OUTPUT);
  updateShiftRegister();
  Serial.begin(9600);
  while (! Serial); // Wait untilSerial is ready - Leonardo
  Serial.println("Enter LED Number 0 to 7 or 'x' to clear");
}

void loop() 
{
  if (Serial.available())
  {
    char ch = Serial.read();
    if (ch &gt;= '0' &amp;&amp; ch &lt;= '7')
    {
      int led = ch - '0';
      bitSet(leds, led);
      updateShiftRegister();
      Serial.print("Turned on LED ");
      Serial.println(led);
    }
    if (ch == 'x')
    {
      leds = 0;
      updateShiftRegister();
      Serial.println("Cleared");
    }
  }
}

void updateShiftRegister()
{
   digitalWrite(latchPin, LOW);
   shiftOut(dataPin, clockPin, LSBFIRST, leds);
   digitalWrite(latchPin, HIGH);
}
```

After you have uploaded this sketch onto your Arduino, click on the right-most button on the toolbar in the Arduino IDE. The button is circled below.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/179/medium800/learn_arduino_ide_serial_moniotor_button.jpg?1396780247)

The following window will open.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/180/medium800/learn_arduino_serial_monitor_0.jpg?1396780248)

This window is called the Serial Monitor and it is part of the Arduino IDE software. Its job is to allow you to both send messages from your computer to an Arduino board (over USB) and also to receive messages from the Arduino.  
  
The message “Enter LED Number 0 to 9 or 'x' to clear” has been sent by the Arduino, and it is telling us what commands we can send to the Arduino which is either to send the 'x' (to turn all the LEDs off) or the number of the LED you want to turn on (where 0 is the bottom LED, 1 is the next one up right up to 7 for the top LED).  
  
Try typing the following commands, into the top area of the Serial Monitor that is level with the 'Send' button. Press 'Send', after typing each of these characters: x 0 3 5  
  
Typing x, will have no effect, if the LEDs are already all off, but as you enter each number, the corresponding LED should light and you will get a confirmation message from the Arduino board, so that the Serial Monitor will appear as shown below.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/181/medium800/learn_arduino_serial_monitor.jpg?1396780252)

You can see that I am about to press send after entering 'x' again. Do this and all the LEDs will turn off.

- [Previous Page](https://learn.adafruit.com/adafruit-arduino-lesson-5-the-serial-monitor/overview.md)
- [Next Page](https://learn.adafruit.com/adafruit-arduino-lesson-5-the-serial-monitor/arduino-code.md)

## Featured Products

### USB Cable - Standard A-B

[USB Cable - Standard A-B](https://www.adafruit.com/product/62)
This here is your standard A-B USB cable, for USB 1.1 or 2.0. Perfect for connecting a PC to your Arduino, USBtinyISP (among other things).  
  
3 feet / 1 meter long  
  
Color may vary!

In Stock
[Buy Now](https://www.adafruit.com/product/62)
[Related Guides to the Product](https://learn.adafruit.com/products/62/guides)
### Diffused Red 5mm LED (25 pack)

[Diffused Red 5mm LED (25 pack)](https://www.adafruit.com/product/299)
Need some indicators? We are big fans of these diffused red LEDs, in fact we use them exclusively in our kits. They are fairly bright so they can be seen in daytime, and from any angle. They go easily into a breadboard and will add that extra zing to your project.

- Pack of 25...

In Stock
[Buy Now](https://www.adafruit.com/product/299)
[Related Guides to the Product](https://learn.adafruit.com/products/299/guides)
### 74HC595 Shift Register - 3 pack

[74HC595 Shift Register - 3 pack](https://www.adafruit.com/product/450)
Add lots more outputs to a microcontroller system with chainable shift registers. These chips take a serial input (SPI) of 1 byte (8 bits) and then output those digital bits onto 8 pins. You can chain them together so putting three in a row with the serial output of one plugged into the serial...

In Stock
[Buy Now](https://www.adafruit.com/product/450)
[Related Guides to the Product](https://learn.adafruit.com/products/450/guides)
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

- [74HC595 Shift Register](https://learn.adafruit.com/74hc595.md)
- [Adafruit Music Maker Shield](https://learn.adafruit.com/adafruit-music-maker-shield-vs1053-mp3-wav-wave-ogg-vorbis-player.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [Arduino Lesson 4. Eight LEDs and a Shift Register](https://learn.adafruit.com/adafruit-arduino-lesson-4-eight-leds.md)
- [Character LCDs](https://learn.adafruit.com/character-lcds.md)
- [Arduino Lesson 10. Making Sounds](https://learn.adafruit.com/adafruit-arduino-lesson-10-making-sounds.md)
- [WiFi Weather Station](https://learn.adafruit.com/wifi-weather-station-arduino-cc3000.md)
- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
- [36mm LED Pixels](https://learn.adafruit.com/36mm-led-pixels.md)
- [Ladyada's Learn Arduino - Lesson #2](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-2.md)
- [Automatic Monitor Color Temperature Adjustment](https://learn.adafruit.com/automatic-monitor-color-temperature-adjustment.md)
- [Low Power WiFi Datalogger](https://learn.adafruit.com/low-power-wifi-datalogging.md)
- [LED Lightbox](https://learn.adafruit.com/led-lightbox.md)
- [Arduino Lesson 11. LCD Displays - Part 1](https://learn.adafruit.com/adafruit-arduino-lesson-11-lcd-displays-1.md)
- [Adafruit Data Logger Shield](https://learn.adafruit.com/adafruit-data-logger-shield.md)
- [Bluefruit LE Connect for iOS and Android](https://learn.adafruit.com/bluefruit-le-connect.md)
