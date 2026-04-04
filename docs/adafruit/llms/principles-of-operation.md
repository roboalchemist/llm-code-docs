# Source: https://learn.adafruit.com/wave-shield-voice-changer/principles-of-operation.md

# Wave Shield Voice Changer

## Principles of Operation

Here we explain some of the geeky background theory stuff. If you just want to get into building the thing, you can skip ahead to the next page.

# Graaains…
Regardless whether you’re old enough to have played with Dad’s LP turntable, or have dabbled in digital audio programs on the newest&nbsp;modern PC, you’ve likely experienced some version of&nbsp;this&nbsp;phenomenon:&nbsp;take an audio recording that’s normally played back at one specific speed…and then change that speed, either compressing or expanding time…and the pitch of the audio changes along with it. Compress time and the pitch rises. Expand time and the pitch drops.&nbsp;_Frequency is inversely proportional to wavelength._

![](https://cdn-learn.adafruit.com/assets/assets/000/002/199/medium800/projects_pitch.png?1396780374)

That’s easy with recordings…but with live audio, we don’t really have that luxury. Realtime is _realtime_…we can’t compress or expand it…it’s happening as it happens. What’s a would-be voice-changer to do?

There’s a complex technique called a _Fourier transform_ that converts a function (or, say,&nbsp;a stream of audio samples) into its frequency spectrum. The resulting frequency values can be altered and an _inverse transform_ applied to turn this back into audio. This is all mathematically good and proper…but it’s a very demanding process and way beyond what our little Arduino can handle. A fairly potent CPU or DSP is usually required. We’ll need a shortcut or some hack…

In digital music circles, _granular synthesis_&nbsp;is a technique of joining and layering&nbsp;lots&nbsp;of very short audio samples (or&nbsp;“grains”) — on the order of one to a few milliseconds — to build up more complex sounds or instruments.&nbsp;Now picture just a single “grain,” 10 milliseconds or so…and we continually refresh this one grain from a live microphone. By time-compressing or -stretching this one tiny loop, repeating or dropping short segments to keep up with realtime, we have the basis for a realtime pitch shifter.&nbsp;It really seems like this shouldn’t work…but it does!&nbsp;Speech waveforms tend to repeat over the very short term, and we can drop or repeat some of those waves with only minor degradation in legibility.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/200/medium800/projects_granular.png?1396780390)

This approach is totally suited to the Arduino’s limited processing power and RAM.&nbsp;The result isn’t going to be Hollywood quality, but it’s still vastly better than&nbsp;the majority of voice-changing toys and masks on store shelves. And you get to make it yourself…how cool is that?

# Sampling Audio
The frequency range of human voice covers about 300 Hz to 3,500 Hz (and harmonics may extend above this).&nbsp;The [Nyquist sampling theorem](http://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem) states that a minimum 2X sample rate is needed to faithfully reconstruct a signal. For human voice, that means 7 KHz sampling…but a little more wouldn’t hurt.

Repeatedly calling the Arduino’s standard analogRead() function in a loop is way, WAY too slow for this. We need to get deeper into the works of the Arduino’s analog-to-digital converter, fiddling directly with special registers and modes.&nbsp;A capability called&nbsp;_free-run mode_&nbsp;collects analog samples at a fast, fixed interval without repeated polling in our code. An interrupt handler is automatically called each time a new sample is ready, which happens like clockwork.&nbsp;Running full tilt, a 16 MHz Arduino can capture 9,615 10-bit samples per second. More than enough&nbsp;for sampling voice!

The audio samples are stored in a _circular buffer,_&nbsp;which is really just big fancy computer science words for “when you reach the end of the buffer, roll back around to the beginning and write over it.” But conceptually, it helps to think of it as a literal circle:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/201/medium800/projects_circular.png?1396780404)

The frequency of recorded sound will seldom match the buffer length exactly, and audio samples are stored and read&nbsp;at different rates.&nbsp;This can produce a sharp discontinuity — a popping noise — each time the “in” and “out” points cross. A small extra buffer is used to store some of the&nbsp;prior audio samples, and the code cross-fades the audio over this boundary to reduce the “pop.”

Because our audio “grain” is relatively short (about 10 milliseconds), the RAM requirements should be fairly modest, a few hundred bytes.&nbsp;Problem is, we’d also like to continue doing&nbsp;those things that the Wave Shield was designed&nbsp;for — namely, playing back WAV files. That requires reading files from an SD card, and that in turn consumes <u>lots</u> of RAM.&nbsp;Fortunately the design of&nbsp;the WAV-playing code lets us gain access that library’s memory and recycle it for our own needs.

The technical details are all well-commented in the source code. So if you’re curious about the specifics of this implementation…use the source, Luke!

# Limitations
When introducing new users to Arduino, I often describe it as “just enough computer to do any <u>one</u> thing really well.” Walking while chewing gum is a challenge. And so it goes with this project as well. Keep the following limitations in mind:

- It can process the voice effect <u>or</u> play back WAVs (and can do both within the same sketch), but you <u>can’t</u>&nbsp;do both simultaneously.
- You <u>can’t</u> read other analog inputs when the voice effect is running (case in point,&nbsp;you can’t alter the pitch continually with&nbsp;a potentiometer). If using analog sensors as sound triggers (e.g. force-sensing resistor pads in shoes), consider work-arounds such as using a carefully-trimmed voltage divider to a digital input, or a second MCU to process analog inputs, forwarding triggers over a serial or I2C connection.
- Although this can change the _pitch_ of one’s voice, it can’t change _timbre._ It won’t, for instance, make things more metallic or robotic-sounding.

- [Previous Page](https://learn.adafruit.com/wave-shield-voice-changer/overview.md)
- [Next Page](https://learn.adafruit.com/wave-shield-voice-changer/building-it.md)

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
