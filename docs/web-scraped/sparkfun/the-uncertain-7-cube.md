# Source: https://learn.sparkfun.com/tutorials/the-uncertain-7-cube

## Magic Isn\'t Real

It's sad but true. We can't levitate, we can't teleport and we definitely can't see the future. That last bit makes the so-called ["Magic 8-Ball"](https://en.wikipedia.org/wiki/Magic_8-Ball) especially sinister. There's nothing magical about randomly answering a yes or no question. Knowing that, the only responsible thing to do is to build a better, more honest, fortune telling device for the enlightened age. I present to you: The Uncertain 7-Cube.

[![7Cube](//cdn.sparkfun.com/r/600-600/assets/4/6/8/9/4/512ff98fce395fe532000001.jpg)](//cdn.sparkfun.com/assets/4/6/8/9/4/512ff98fce395fe532000001.jpg)

The Uncertain 7-Cube is a non-committal, less-than-helpful, but also entirely honest fortune teller. Simply ask it a yes or no question, give it a nudge, and the 7-Cube will dutifully inform you that it doesn't have all the facts and doesn't feel comfortable making a guess. That's right, in a variety of voices and a multitude of responses, the Uncertain 7-Cube will preserve your sense of responsibility for the future by refusing to make your decisions for you!

To make this happen we'll need a few things:

- [Parallax Emic2 Text-to-Speech Module](https://www.sparkfun.com/products/11711)
- [Arduino Pro Mini 5V](https://www.sparkfun.com/products/11113)
- [2" Square ProtoBoard](https://www.sparkfun.com/products/8811)
- [Mono Audio Amp Breakout](https://www.sparkfun.com/products/11044)
- [Thin Speaker](https://www.sparkfun.com/products/10722)
- [Power Cell LiPo Charger/Booster](https://www.sparkfun.com/products/11231)
- [1000mAh Polymer Lithium Ion Battery](https://www.sparkfun.com/products/339)
- [Wake-on-Shake Board](https://www.sparkfun.com/products/11447)
- [FTDI Basic Breakout 5V](https://www.sparkfun.com/products/9716)
- Some [Male Right Angle](https://www.sparkfun.com/products/553) and [Female Headers](https://www.sparkfun.com/products/115)
- Some Kind of Enclosure (I used acrylic)
- A Soldering Iron and Some Solder

## Behind the Uncertainty

Since magic isn't making this thing tick, what is? Well, it's a bit of a jumble:

[![Fritzing Schematic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/Uncertain7_bb2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/Uncertain7_bb2.png)

The ability of the Uncertain 7-Cube to remain in 'stasis' while waiting to be picked up or bumped is a function of the Wake-on-Shake board. The Wake-on-Shake uses an ultra low power accelerometer to detect motion. When motion is detected, the on-board microcontroller wakes up and turns on power to the rest of the cube.

The ability to speak (magical as it may seem) is actually provided by the emic2 Text-to-Speech module from Parallax. This module simply takes character strings over a serial connection, parses them into pronounceable words, and uses a built-in voice synthesizer to speak them out loud. Our Mono Amp breakout turns the volume to 11 so you can clearly hear the cube's non-advice.

All of the different non-committal answers are stored on an Arduino Pro Mini, which is programmed to randomly choose an answer from the list and transmit it over the serial port. When it gets a signal back from the emic2 module that it's done talking, the Pro Mini shuts everything down and the cube goes back into stasis.

The emic2 module has an input voltage of 5V, so the supply voltage for the cube needed to be able to provide that. A lithium polymer battery and a Powercell board provide 5V to the system. The Powercell also provides an easy way to charge the battery without having to remove it.

## The Build

The Uncertain 7-Cube was supposed to be about the size of a Magic 8-Ball except, you know, cube shaped. The way this was accomplished is that almost all of the component boards were mounted vertically on a 2" square ProtoBoard using right-angle headers. This kept everything mounted firmly to the cube and left room in the center for a battery.

[![buildpic](//cdn.sparkfun.com/r/600-600/assets/0/c/b/e/9/512ffa88ce395fb545000000.jpg)](//cdn.sparkfun.com/assets/0/c/b/e/9/512ffa88ce395fb545000000.jpg)

As you can see, there's a ribbon cable attached to the FTDI header on the Arduino Pro Mini. That's just there to allow the Arduino to be programmed after the whole thing is enclosed. The headphone jack on the Text-to-Speech module, the charging jack on the Powercell and the FTDI ribbon are all accessible from one side of the assembly; That way, I could avoid taking the whole enclosure apart if I needed to get to something.

The only part that isn't mounted vertically is the Wake-on-Shake board. Since it uses an accelerometer to detect when it changes position, it needs to be firmly connected to the board so it can't wiggle around and decrease the reliability of the sensor. You'll also notice the speaker is just hanging off of the board. When everything is mounted in the enclosure, the standoffs keep the speaker from moving.

## The Enclosure

Cubes are a nice shape. They're made up of regular planes and are therefore really easy to fabricate out of almost anything. I decided that laser cut acrylic was the fastest way to make a really good looking enclosure. To make the basic box shape, I used an awesome online tool called [BoxMaker](http://boxmaker.rahulbotics.com/) which takes the dimensions of your box and the thickness of your material and generates a vector file with the pattern. I imported the pattern into [InkScape](http://inkscape.org/) (a free vector drawing tool) and added a little flair of my own.

[![svgpng](//cdn.sparkfun.com/r/600-600/assets/6/2/8/1/f/5130007ece395f0833000001.png)](//cdn.sparkfun.com/assets/6/2/8/1/f/5130007ece395f0833000001.png)

After I had the file drawn out, I sent it to the laser cutter. The thin lines were cut and the thick features and shapes were raster etched. When the pieces came out of the laser cutter I cleaned them with a plastic polish and painted inside of the etched features using a white paint pen.

When everything was clean and dry, it was puzzle time. I started by screwing the electronics to the bottom plate of the cube. There were three holes cut in the piece that would match the position of the standoffs. I used a handheld drill to add a chamfer to the holes which would hide the head of the machine screws.

Once the core was in place, I started assembling the cube one panel at a time using hot glue. I left one panel loose so that I could still access the board to change/charge the battery or connect to the emic2 module's headphone jack.

## The Code

Since the Wake-on-Shake board handles all of the hibernation and motion detecting functions, all that the Arduino has to do is pick a phrase, send it to the voice synth, and then tell the Wake-on-Shake to turn everything off again. The code is based heavily on the Emic2 example code provided by Parallax.

    language:C
    #include <SoftwareSerial.h>
    #include <TrueRandom.h>

    #define rxPin 2    // Serial input (connects to Emic 2 SOUT)
    #define txPin 3    // Serial output (connects to Emic 2 SIN)
    #define ledPin 13  // Most Arduino boards have an on-board LED on this pin
    #define wakePin 9 // Wake on Shake "Keep Awake" Pin

    // set up a new serial port
    SoftwareSerial emicSerial =  SoftwareSerial(rxPin, txPin);

    void setup()  // Set up code called once on start-up
    

    void loop()
    

     emicSerial.print('\n'); // Terminate the speech command
     while (emicSerial.read() != ':');   // Wait here until the Emic 2 responds with a ":" indicating it's done talking
     digitalWrite(wakePin, LOW); // Let the Wake-On-Shake module know it's okay to turn off
     while(1); // Hang out here until the WOS module shuts us down
    }

So there it is, I simply used a random number generator library called ["TrueRandom"](https://code.google.com/p/tinkerit/wiki/TrueRandom) to pick a number. Then I used that number to select a phrase from a list. That phrase was sent to the serial port, and then the sleep pin was allowed to fall to 0V, signalling the Wake-on-Shake to shut down. Pick up the cube and the whole process starts over again!