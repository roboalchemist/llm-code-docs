# Source: https://learn.adafruit.com/wave-shield-voice-changer.md

# Wave Shield Voice Changer

## Overview

The [Wave Shield for Arduino](http://adafruit.com/products/94) is one of Adafruit's earliest shield kits and remains a perennial favorite.&nbsp;And for good reason — it's among the easiest and most flexible means of adding quality sound effects to an Arduino project!  
  
Like a fine wine, open source projects improve with age. We've taught this classic shield a new trick: a _realtime voice changer!_ Speak like everyone's favorite baritone Sith lord or&nbsp;sing along with the Lollipop Guild.&nbsp;The Wave Shield has long been a staple among makers' Halloween projects. This latest addition really cinches it!

http://youtu.be/eRdSi4gJz98

# Core Parts List

There are three central components to this project:

- [Adafruit Metro 328 or Arduino Uno](https://www.adafruit.com/product/2488) (an older Arduino Duemilanove or “328” Diecimila can be used as well…but <u>not</u>&nbsp;an Arduino Mega nor Leonardo, sorry).
- [Adafruit Wave Shield](https://www.adafruit.com/products/94 "Link: https://www.adafruit.com/products/94")&nbsp;(also available as part of the [Music & sound add-on pack for Arduino](https://www.adafruit.com/product/175)).&nbsp;
- [Adafruit Microphone Amplifier Breakout.](http://www.adafruit.com/products/1063)

You’ll also need basic soldering tools, wire and&nbsp;bits & bobs.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/197/medium800/projects_coreparts.jpg?1396780354)

# Additional Parts
This is an “open ended” project&nbsp;and the exact components for completion will depend on where you want to take it.&nbsp;<u>Read through the full tutorial</u> for ideas and recommendations on specific parts.  

- For sound output you’ll want headphones, portable MP3 player speakers or&nbsp;our&nbsp;[Class D Audio Amplifier](https://www.adafruit.com/products/987 "Link: https://www.adafruit.com/products/987").  
- The example sketch uses a [12-button keypad](http://adafruit.com/products/419 "Link: http://adafruit.com/products/419") for triggering pre-recorded sounds. But your application might need just a few simple [buttons](http://adafruit.com/products/476 "Link: http://adafruit.com/products/476")…or none at all, if you’re only using the voice effect.
- If adding pre-recorded sounds, you’ll also need an [SD card](http://adafruit.com/products/102) containing WAV files.
- A [10K potentiometer](http://adafruit.com/products/562 "Link: http://adafruit.com/products/562") is used for setting the voice pitch…or you can simply rig the code for a permanent setting.
- If you want to noodle around with wiring, [an extra prototyping shield](http://www.adafruit.com/products/51 "Link: http://www.adafruit.com/products/51") and [stacking headers can come in very handy](http://www.adafruit.com/products/85) - solder the wave shield with stacking headers and put the proto shield on top  
- For portable use (such as costumes and props), add batteries, [battery holders](http://adafruit.com/products/771 "Link: http://adafruit.com/products/771"), etc.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/198/medium800/projects_otherparts.jpg?1396780364)

To reiterate, it’s a very good idea to read through the full tutorial and firm up your own project concept before making a shopping list. We’ll demonstrate a couple of examples, but these aren’t the last word. That’s really the essence of Arduino, isn’t it? Make it your own!

# First Things First…
We also <u>very strongly recommend</u>…no, make that <u>require</u>…that you work through the [original Wave Shield tutorial](http://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino "Link: http://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino") before commencing with this project. It’s a good way to verify the core pieces are working before adding extra layers of complexity. ### 

Afraid not. Realtime voice changing requires issuing data directly to the audio DAC bit-by-bit on the fly. MP3 and the decoder on the associated shield work with prerecorded audio (ditto for OGG format audio).

- [Next Page](https://learn.adafruit.com/wave-shield-voice-changer/principles-of-operation.md)

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
