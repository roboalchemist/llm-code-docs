# Source: https://learn.adafruit.com/wave-shield-voice-changer/building-it.md

# Wave Shield Voice Changer

## Building It

# Phase 1:

## Follow the original Wave Shield tutorial
We can’t emphasize this one enough: work through the [original Wave Shield tutorial](http://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino "Link: http://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino") before moving on to the voice changer!  
  
This project has many separate parts, and a misstep with any one of them can stop the whole system from working. It would be tricky to debug the point of failure among all the possibilities. Invest a little time now to get the basic Wave Shield examples working — especially the “Pi speak” demo. This lets you know that the shield is properly assembled, the SD card properly formatted and so forth. _Then_ we’ll add the extra features.  
  
Start by [downloading the WaveHC library for Arduino](https://github.com/adafruit/WaveHC "https://github.com/adafruit/WaveHC")…not only for WAV playback, but the voice changer relies on this code too. [We have a tutorial explaining how Arduino libraries are installed](http://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-libraries). Download [this ZIP file containing WAV files](http://learn.adafruit.com/system/assets/assets/000/010/145/original/piwav.zip) for the digits of pi. Then proceed through the tutorial until your Wave Shield is speaking them.

# Phase 2:

## Adding voice effects and a sound&nbsp;trigger keypad
With the basic Wave Shield working,&nbsp;now we can add the voice changer and a sound-triggering keypad. You can complete this phase on your workbench using a breadboard…we’ll make it portable later, after confirming that it works.

[Download the Adavoice sketch for Arduino](https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/master/AdaVoice). And you should already have the [WaveHC](http://code.google.com/p/wavehc/) library installed from the prior phase.

[Download the project code and files in Zip](https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/master/AdaVoice)
The GND and&nbsp;3.3V lines from the Arduino need to connect to several points, so you may want to a breadboard’s power rails for this. 3.3V from the Arduino&nbsp;should connect to the Electret&nbsp;Mic Amp VCC pin, one outside leg of a 10K potentiometer, and the Arduino’s AREF pin. GND from Arduino&nbsp;should connect to GND on the Mic Amp and the opposite outside leg of the potentiometer.

Danger: 

The Mic Amp output connects to analog pin 0, and the center leg of the potentiometer connects to analog pin 1.  
  
If you plan to use prerecorded sound effects (some examples are in the “wavs” folder included with the sketch), you’ll need a FAT-formatted SD card with the files placed in the root directory (similar to how the “Pi speak” sketch worked). A 12-button keypad connects to digital pins 6, 7, 8 (columns) and analog pins 2, 3, 4, 5 (rows). But with some changes to the sketch, this can be adapted to use just a few buttons or other triggers. (The keypad is great for haunted house sounds, but too cumbersome for a costume.)  
  
A small speaker can be connected directly to the Wave Shield’s amplifier output. For more volume, we recommend using amplified speakers such as the portable type for iPods and MP3 players, or our Class D Audio Amplifier breakout.

![](https://cdn-learn.adafruit.com/assets/assets/000/106/528/medium800/projects_circuit1.png?1637005925)

Upload the Adavoice sketch to the Arduino if you haven’t already done this.&nbsp;If everything is wired up and loaded correctly, you should head a startup chime when the sketch starts (if using an SD card with the sample WAVs). If there’s no sound, use the Arduino serial monitor and watch for diagnostic messages.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/212/medium800/projects_built1.jpg?1396780544)

Once up and running, you can then talk into the microphone and should hear the altered result through the speaker or headphones (keep the mic away from the speaker to avoid feedback). Pressing any of the keypad buttons will stop the voice effect to play the corresponding sound, then resume afterward.  
  
Note that the pitch dial <u>does not work in real time</u>! This is normal and a limitation of the way we’re running the analog-to-digital converter at full speed.&nbsp;To get a new pitch reading, you need to either play back a sound or press the reset button.

# Phase 3:

## Making it battery-powered and portable
To simplify the wiring diagram, we’ll illustrate this next section without the keypad. But you can still include it if you want! The connections are the same as above.

Because breadboard circuits are too delicate for portable use, we’ll join components directly this time.  
  
The Wave Shield can drive a small speaker on its own, but this doesn’t provide a lot of “oomph.” Parties and comic conventions are loud, so you’ll probably want a boost! We’re using our Class D Audio amplifier here with a pair of 4 Ohm speakers. Alternately, there are a lot of ready-to-go battery-powered speakers designed for iPods and other MP3 players that can plug right into the Wave Shield headphone jack. Using our own amp and speakers lets us custom-tailor the placement of all the parts.  
  
It’s best&nbsp;to power the Arduino and audio amplifier separately. During particularly loud moments, the audio amp can draw a <u>lot</u> of current, resulting in a momentary voltage “sag” causing the Arduino to reset. Giving the Arduino it’s own separate power supply prevents this. We’re using a 9 Volt battery connected to the DC barrel jack, or a 6X AA battery pack will last considerably longer.&nbsp;In any case, the ground connection is common between the Arduino and audio power sections, as well as the 3.3V part of the circuit (for the mic amp and trim pot).

![](https://cdn-learn.adafruit.com/assets/assets/000/002/215/medium800/projects_circuit2.png?1396780576)

Here we’ve mounted all the parts on a sheet of acrylic using double-stick foam tape, then fastened this to a nylon strap so it can be worn over one’s chest. We chose tape for expediency only…give some thought to making your rig more durable, using mounting screws, zip ties, etc.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/213/medium800/projects_finished.jpg?1396780547)

You can run the microphone connection&nbsp;a couple feet to reach inside a mask or helmet. A&nbsp;[servo extension cable](http://adafruit.com/products/973)&nbsp;provides a very handy 3-conductor separation point, so you can pop your head and set it down! Cut the servo cable in half, soldering one end to the mic amp board and the other side to the Arduino circuit.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/216/medium800/projects_servo.jpg?1396780580)

- [Previous Page](https://learn.adafruit.com/wave-shield-voice-changer/principles-of-operation.md)
- [Next Page](https://learn.adafruit.com/wave-shield-voice-changer/special-considerations-for-costumes.md)

## Featured Products

### Stereo 3.7W Class D Audio Amplifier - MAX98306

[Stereo 3.7W Class D Audio Amplifier - MAX98306](https://www.adafruit.com/product/987)
This incredibly small stereo amplifier is surprisingly powerful - able to deliver 2 x 3.7W channels into 3 ohm impedance speakers. Inside the miniature chip is a class D controller, able to run from 2.7V-5.5VDC. Since the amp is a class D, its incredibly efficient (over 90% efficient when...

In Stock
[Buy Now](https://www.adafruit.com/product/987)
[Related Guides to the Product](https://learn.adafruit.com/products/987/guides)
### Electret Microphone Amplifier - MAX4466 with Adjustable Gain

[Electret Microphone Amplifier - MAX4466 with Adjustable Gain](https://www.adafruit.com/product/1063)
Add an ear to your project with this well-designed electret microphone amplifier. This fully assembled and tested board comes with a 20-20KHz electret microphone soldered on. For the amplification, we use the Maxim MAX4466, an op-amp specifically designed for this delicate task! The amplifier...

In Stock
[Buy Now](https://www.adafruit.com/product/1063)
[Related Guides to the Product](https://learn.adafruit.com/products/1063/guides)
### Adafruit Wave Shield for Arduino Kit

[Adafruit Wave Shield for Arduino Kit](https://www.adafruit.com/product/94)
Adding quality audio to an electronic project is surprisingly difficult. Here is a shield for Arduino 328's that solves this problem. It can play up to 22KHz 12bit uncompressed audio files of any length. It's low cost, available as an easy-to-make kit. It has an onboard DAC, filter and...

Out of Stock
[Buy Now](https://www.adafruit.com/product/94)
[Related Guides to the Product](https://learn.adafruit.com/products/94/guides)
### Music & sound add-on pack for Arduino

[Music & sound add-on pack for Arduino](https://www.adafruit.com/product/175)
Its a Wave shield party pack! Just add an Arduino to create your own iPod-killer, audio art, sound-effects box...

Comes with:

- Latest [Wave shield kit](http://www.adafruit.com/products/94), works with more SD cards and with older NG Arduinos! Unassembled
- 8 GB...

Out of Stock
[Buy Now](https://www.adafruit.com/product/175)
[Related Guides to the Product](https://learn.adafruit.com/products/175/guides)
### Adafruit Proto Shield for Arduino Kit

[Adafruit Proto Shield for Arduino Kit](https://www.adafruit.com/product/51)
Works with the Uno! This prototyping shield is the best out there (well, we think so, at least). It works with UNO, NG, Diecimila and Duemilanove Arduinos. You can use it with a Leonardo but it will not break out the hardware SPI pins (they're only on the ISP connector underneath) or the...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/51)
[Related Guides to the Product](https://learn.adafruit.com/products/51/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Shield stacking headers for Arduino (R3 Compatible)

[Shield stacking headers for Arduino (R3 Compatible)](https://www.adafruit.com/product/85)
_“How could something so simple be so useful?”&nbsp;_

We heard once that&nbsp;in the 4th millennium B.C.&nbsp;some guy asked the person who invented the wheel that question.&nbsp; The person who invented the wheel’s answer, we were told, was...

In Stock
[Buy Now](https://www.adafruit.com/product/85)
[Related Guides to the Product](https://learn.adafruit.com/products/85/guides)
### 6 x AA battery holder with 5.5mm/2.1mm plug

[6 x AA battery holder with 5.5mm/2.1mm plug](https://www.adafruit.com/product/248)
Make a portable power brick with plenty of juice! Use Alkaline AA's for a 9V 3000-4000mAh power supply, or rechargeable NiMH for 2000mAh 7.5V supply. Either one is good for running electronics that have a 5V voltage regulator (thus requiring a 7V+ supply). Will last about 10 times longer...

In Stock
[Buy Now](https://www.adafruit.com/product/248)
[Related Guides to the Product](https://learn.adafruit.com/products/248/guides)

## Related Guides

- [Boombox Beach Bag with Audio Amp and Speakers](https://learn.adafruit.com/boombox-beach-bag-with-audio-amp-and-speakers.md)
- [DIY 8x2 LCD Shield](https://learn.adafruit.com/diy-8x2-lcd-shield.md)
- [3D Printed Animatronic Robot Head](https://learn.adafruit.com/3d-printed-animatronic-robot-head.md)
- [Arduino Lesson 17. Email Sending Movement Detector](https://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector.md)
- [Arduino Lesson 11. LCD Displays - Part 1](https://learn.adafruit.com/adafruit-arduino-lesson-11-lcd-displays-1.md)
- [Line Following Zumo Robot Using Simulink](https://learn.adafruit.com/line-following-zumo-robot-programmed-with-simulink.md)
- [3D Printed Bone Conduction Transducer Box](https://learn.adafruit.com/3d-printed-bone-conduction-transducer-box.md)
- [Affordable HAL 9000 Replica](https://learn.adafruit.com/hal-9000-replica.md)
- [Electronic Demon Costume](https://learn.adafruit.com/electronic-demon-costume.md)
- [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors.md)
- [Naughty or Nice Machine](https://learn.adafruit.com/naughty-or-nice-machine.md)
- [Nokia 5110/3310 Monochrome LCD](https://learn.adafruit.com/nokia-5110-3310-monochrome-lcd.md)
- [Track Your Treats: Halloween Candy GPS Tracker](https://learn.adafruit.com/track-your-treats-halloween-candy-gps-tracker.md)
- [Smart Measuring Cup](https://learn.adafruit.com/smart-measuring-cup.md)
- [Wave Shield](https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino.md)
