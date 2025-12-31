# Source: https://learn.sparkfun.com/tutorials/vibe-o-matic-3000

## Introduction

It all started because a friend sent me a link to a baby crib that Ford made.

I had no idea how much money or time Ford spent but I figured I could do something similar. It might be a little too DIY\... And my son might not like it at all\... But I present to you **The Vibe-O-Matic 3000**:

[![Baby in bouncy chair with Arduino](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/7/Vibe-O-Matic-0.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/7/Vibe-O-Matic-0.jpg)

## VOM3K

Ok, what's going on here? The VOM3K is designed to replicate every aspect of riding in a car. The seat vibrates to varying degrees much the way a car will turn on, drive for a bit, stop at lights, etc. The seat lights up on the sides in a pulsating way just like a car's headlights will light up the cabin. And the speakers play a recording of road noise recorded during a 15 minute drive.

Now for the big question. Does the baby like it, or LOVE it? Turns out the baby is just confused by it. The smart little bugger knows it's not the car but he doesn't quite know what it is. He doesn't fuss or cry when he's in it but doesn't pass out like in the back seat of the car. Instead, he tends to stare up at me with an inquisitive look I can only interpret as "Dad, why do you keep saying the word Arduino. Am I Arduino-ing right now?!"

### Required Materials

Here\'s the part list:

- [Arduino Pro 328 - 5V/16MHz](https://www.sparkfun.com/products/10915)
  - [Male Break Away Headers - Straight](https://www.sparkfun.com/products/116)
  - [5V FTDI](https://www.sparkfun.com/products/9716)
  - [mini-B USB Cable](https://www.sparkfun.com/products/11301)
- [MP3 Player Shield](https://www.sparkfun.com/products/12660)
  - [microSD Card](https://www.sparkfun.com/products/13833)
  - [Female Headers](https://www.sparkfun.com/products/115)
- [Hook-up Wire](https://www.sparkfun.com/search/results?term=hook-up+wire)
- [Enclosure](https://www.sparkfun.com/products/retired/8632)
- [5V Power Supply](https://www.sparkfun.com/products/12889)
- [Panel Mount Barrel Jack](https://www.sparkfun.com/products/retired/10785)
- [MOSFET Power Control Kit](https://www.sparkfun.com/products/12959)
- [JST Jumper 3 Wire Assembly](https://www.sparkfun.com/products/9915)
- [Rocker Switch](https://www.sparkfun.com/products/8837)
- [Momentary Push Button](https://www.sparkfun.com/products/11992)

You will also need:

- [PC Speakers](https://www.amazon.com/gp/product/B000R9AAJA/ref=oh_aui_search_detailpage?ie=UTF8&psc=1)
- [Individually Addressable Warm White LED Strip (APA102 Driver IC)](https://www.amazon.com/Mokungit-2700-3200K-Individually-Addressabled-Non-waterproof/dp/B01IX5FQIE/ref=sr_1_3?ie=UTF8&qid=1510931291&sr=8-3&keywords=apa102+warm+white)
- Zip Ties
- MDF board
- Screws
- Phillips Screw Driver

### Tools

You will need a soldering iron, solder, [general soldering accessories](https://www.sparkfun.com/categories/49), and tools to connect the project.

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Needle Nose Pliers](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/3/3/08793-03-L.jpg)](https://www.sparkfun.com/needle-nose-pliers.html)

### [Needle Nose Pliers](https://www.sparkfun.com/needle-nose-pliers.html) 

[ TOL-08793 ]

Mini Pliers. These are great little pliers! A must have for any hobbyist or electrical engineer. Crucial for inserting device...

[ [\$3.60] ]

[![Diagonal Cutters](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/3/4/08794-03-L.jpg)](https://www.sparkfun.com/diagonal-cutters.html)

### [Diagonal Cutters](https://www.sparkfun.com/diagonal-cutters.html) 

[ TOL-08794 ]

Mini Diagonal Cutters. These are great little cutters! A must have for clipping leads and extra solder tails. 4\" long.

[ [\$3.75] ]

[![Wire Strippers - 30AWG Hakko](https://cdn.sparkfun.com/r/140-140/assets/parts/9/3/1/2/12630-Hakko-Wire-Strippers-30AWG-Feature.jpg)](https://www.sparkfun.com/wire-strippers-30awg-hakko.html)

### [Wire Strippers - 30AWG Hakko](https://www.sparkfun.com/wire-strippers-30awg-hakko.html) 

[ TOL-12630 ]

It can be used as: Shears, Multi-diameter Wire stripper, pliers.

[ [\$13.95] ]

[![Hakko FX888D Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/7/8/8/5/11704-01.jpg)](https://www.sparkfun.com/products/11704)

### [Hakko FX888D Soldering Station](https://www.sparkfun.com/products/11704) 

[ TOL-11704 ]

For over 50 years, Hakko has been producing superior quality soldering and desoldering tools. They\'re dependable, a good valu...

**Retired**

You will also need:

- Hot Glue Gun w/ Hot Glue
- Comfy Baby Seat
- Hobby Motor

## The Build

To build the Vibe-O-Matic, I needed three things:

- Vibration
- Sound
- Light

Luckily, the bouncy seat that friends gave us (thank you Victoria!) had a small vibration motor attached.

[![Baby bouncy chair](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/7/Vibe-O-Matic-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/7/Vibe-O-Matic-1.jpg)

The original vibration design used a single C cell battery (approximately 1.5V) with a simple ON/OFF slide switch. I removed the power switch and battery and used the [MOSFET power control kit](https://www.sparkfun.com/products/12959) to control the motor via the Arduino at 5V. Since the DC motor was used to vibrate the seat, it did not matter what pin was used when connecting it to the \"Device\" side of the n-channel MOSFET\'s breakout board.

[![Vibration motor modified with MOSFET control](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/7/Vibe-O-Matic-2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/7/Vibe-O-Matic-2.jpg)

*Vibration motor modified with MOSFET control*

What does the motor do when run at 5V instead of the designed 1.5V? It runs a lot faster and a lot louder. Thankfully, the Arduino has PWM on a handful of pins so we are able to run the motor from 0 to 100% throttle. Therefore, if the vibration is too great (or the motor gets too warm), we can ramp down the power to an acceptable level. I ended up running the motor from about 40% to 80% power. Any higher and the boy gets even more weirded out.

Next, I [soldered](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) an Arduino Pro to the MP3 Player Shield. Note that the Arduino is mounted above the shield. It's not mandatory that an Arduino go below a shield. I knew I was going to need to solder a variety of additional things like switches and buttons to the Arduino. It was easier for me to mount the MP3 shield below so I could see the pins I needed to access on the Arduino. After stacking, the following wired connections were made as shown in the following table.

[![Arduino Pro with MP3 Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/7/Vibe-O-Matic-3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/7/Vibe-O-Matic-3.jpg)

*5V Arduino Pro stacked on MP3 Shield with wired connections*

  ------------------------------------------------------------------------------------------------
  Component                                          Arduino Pro 5V/16MHz
  -------------------------------------------------- ---------------------------------------------
  Panel Mount Barrel Jack\'s **Center Pin**          Barrel Jack **VIN pin**

  Panel Mount Barrel Jack\'s **Sleeve Pin**          Barrel Jack **GND pin**

  N-Channel MOSFET Breakout Board: **\"C\" Pin**     **Pin 10**

  N-Channel MOSFET Breakout Board: **\"-\" Pin**     **GND Pin**

  N-Channel MOSFET Breakout Board: **\"+\" Pin**     **VIN Pin**

  APA102 Ground:                                     **\"-\" Pin** Next to Barrel Jack Footprint
                                                     
  GND                                                

  APA102 Data: **D1 Pin**                            **Pin 5**

  APA102 Clock: **C0 Pin**                           **Pin 4**

  APA102 Vcc:                                        **\"+\" Pin** Next to Barrel Jack Footprint
                                                     
  5V                                                 

  Go!: Momentary Push Button Pin                     **Pin A0**

  Go!: Momentary Push Button Pin                     **Pin A1**

  Vibe Mode: Rocker Switch **Normally Closed Pin**   **Pin A1**

  Car Mode: Rocker Switch **Normally Open Pin**      **Pin A2**
  ------------------------------------------------------------------------------------------------

I made a base board out of MDF to mount everything to. I had some extra paint around so I painted it (thinking a coat of paint would have a positive impact on my wife's feelings about this whole endeavor). The speakers are attached with a couple of screws through the MDF into the plastic speaker housing. The enclosure and electronics were similarly secured with a couple screws.

[![MDF base board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/7/Vibe-O-Matic-4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/7/Vibe-O-Matic-4.jpg)

*MDF base board*

The chair was then zip tied to the MDF. The individually addressable APA102 warm white LEDs had an adhesive backing like most strips do. But like most LED strips, this backing tends to wear out after a few days so I added hot-glue to various points on the LED strip to secure it.

[![Bouncy chair mounted to baseboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/7/Vibe-O-Matic-5.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/7/Vibe-O-Matic-5.jpg)

*Bouncy chair mounted to baseboard*

The APA102 LEDs are controlled with the excellent [FastLED library](https://github.com/FastLED/FastLED). The 'Cylon' example was modified to mimic car's headlights illuminating the cabin as they pass on the left, right, and front.

[![Cylon LEDs emulating passing headlights](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/7/Vibe-O-Matic-Headlights.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/7/Vibe-O-Matic-Headlights.gif)

*Cylon LEDs emulating passing headlights*

Next, I recorded a [12 minute drive](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/7/baby.mp3) through my city with the windows down. If you listen to the track you can hear where a couple large diesel trucks pass by. It's a pretty good track although it's hard to pick up good road noises. At one point I envisioned using a light sensor, GPS, and accelerometer to properly record the light and vibration through the drive. At that same moment my son started to scream and I decided it was better to take the SISI (screw it, ship it) approach: the LEDs trigger every 30 seconds with a random right/front/left decision and the vibration motor changes to a new, random, vibration level (40 to 80% throttle) every 60 seconds.

## The Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

To follow along with this project, you will need to install the following libraries:

[FastLED Arduino Library](https://github.com/FastLED/FastLED)

[SparkFun MP3 Player Shield Arduino Library](https://github.com/madsci1016/Sparkfun-MP3-Player-Shield-Arduino-Library)

A rocker switch was used to select between **Vibe** (vibrate for 15 minutes, no lights or sound) and **Car** (the full effect). The **Go!** button allows the user to start or stop an action.

[![Buttons to make the baby chair go](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/7/Vibe-O-Matic-7.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/7/Vibe-O-Matic-7.jpg)

*A stripped down UI*

You can find the code for the Vibe-O-Matic 3000 [here](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/7/Vibe-O-Matic-3000.ino):

[Vibe-O-Matic 3000 Example Code](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/7/Vibe-O-Matic-3000.ino)

It looks at the state of the rocker switch and the start button to determine what to do. Once actuated the MP3 shield plays the track until completion. The LEDs and motor turn ON/OFF randomly every 30 and 60 seconds, respectively. There's also a vibe-only mode that vibrates the chair for 15 minutes.

## The Result

ReplaceMeOpen

ReplaceMeClose

In the end, Jack doesn\'t really like or dislike the seat. I suspect the snugness of car seat is important. I also think the vibrations in a car are at a lower frequency and a much higher amplitude than the small vibe motor can do. I hope someone can learn from my lessons and do an even better version!