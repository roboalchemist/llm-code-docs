# Source: https://learn.sparkfun.com/tutorials/rotary-dial-kit-assembly-guide

## A Simple Interface

[![](https://cdn.sparkfun.com/assets/custom_pages/2/6/9/sparkx-logo.png)](https://www.sparkfun.com/sparkx)

\
**Experimental Products:** [SparkX products](https://www.sparkfun.com/sparkx) are rapidly produced to bring you the most cutting edge technology as it becomes available. These products are tested but come with no guarantees. Live technical support is not available for SparkX products.

The [Rotary Dial Kit](https://www.sparkfun.com/products/14790) is designed to be a simple interface device for your project. Input is achieved using a rotating encoder bezel and output is handled by a ring of addressable RGB LEDs along the inside edge of the ring. Two keyhole hangers are milled into the back of the Rotary Dial so it can be wall mounted.

[![Rotary Dial Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/0/4/8/14790-Rotary_Dial-01.jpg)](https://www.sparkfun.com/products/14790)

### [Rotary Dial Kit](https://www.sparkfun.com/products/14790) 

[ SPX-14790 ]

The Rotary Dial Kit is designed to be a simple interface device for your project. Input is achieved using a rotating encoder ...

**Retired**

The design was inspired by the rotating bezel on my Samsung Gear smartwatch as well as wall-mounted IoT devices such as the Nest thermostat.

### Tools

To assemble the kit, you\'ll need:

- A small Phillips screwdriver
- A soldering iron and some solder (a [flux pen](https://www.sparkfun.com/products/14579) helps too!)
- Pliers or Tweezers are handy but not necessary

## Hardware Assembly

### Step 1 - Count Your Parts!

Make sure you have everything that you need. The kit includes three PCBs, three pogo pins, four 4-40 bolts, four 4-40 nuts and four 1/4\" standoffs.

[![top down shot of all kit components as described above](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/2/RotaryDialComponents_small.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/RotaryDialComponents_small.jpg)

### Step 2 - Solder the Pogo Pins

The trickiest part of the assembly will be [soldering](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) these pins. It\'s not too tough, though, so let\'s get it out of the way now! Start off by applying some flux to each pad, if you have it.

[![Close up of a hand holding a flux pen and applying flux to one of the small solder pads on the base board in preparation for soldering the pogo pin.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/2/ApplyFluxtoSoldertoPad.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/ApplyFluxtoSoldertoPad.jpg)

Then place a pogo pin on it\'s pad and center it as best you can. Don\'t worry too much about it because it will self-center if you add enough solder. Very carefully apply solder to the pad and allow it to flow to the pin. Add enough solder so that there is a rounded pool around the base of the pin. Once you have a small blob of solder, pull the iron away swiftly and smoothly, careful not to knock over the pogo pin. The surface tension of the still-molten solder should drag the pogo pin to the center of the pad.

[![Close up view of a soldering iron tip making the necessary solder joint](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/2/AddSolderPogoPin.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/AddSolderPogoPin.jpg)

Check to make sure that the pin is aligned vertically. It doesn\'t need to be perfectly perpendicular to the board, but it should be sticking relatively straight up. You may need to grab the pin with some tweezers, reheat the solder, and press it down onto the pad to get it aligned.

[![Macro shot of the completed solder joint showing an abundance of solder forming a rounded base around the pogo pin.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/2/SolderedPogoPin.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/SolderedPogoPin.jpg)

Repeat this process for each pin.

### Step 3 - Add Some Solder to the Standoff Holes

The bolts that hold the assembly together are also the signal route for the RGB LEDs on the retainer ring, so it\'s important to create a good electrical connection. To aid in this, add a little bit of solder to the face of each standoff hole on the back of the base board and the front of the retainer board. Make sure not to overdo it and make the hole too tight for the bolt to go through. The goal is to make a little bump for the nut or the head of the bolt to tighten against.

[![Hands hold a soldering iron and a length of solder against the exposed copper surrounding a standoff hole in the base board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/2/SolderOnMountingHoles.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/SolderOnMountingHoles.jpg)

### Step 4 - Build Your Sandwich!

Now it\'s time to stack everything together! There are probably a lot of ways to accomplish this, but this is the way I find easiest.

Start by putting the 4-40 bolts through the front of the retainer ring (the board with the LEDs on it) so that the LEDs are on the opposite side from the head of the bolts. Now set this aside and place your base board with the pogo pins facing up.

[![A ring shaped board is laying face up to the right with LEDs on its face and bolts protruding toward the camera. In the center of the photo another round board is sitting with pogo pins facing up. A hand holds another ring shaped board overtop of the round board.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/2/SandwichComponentsRotaryDial.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/SandwichComponentsRotaryDial.jpg)

Carefully place a nylon standoff over each of the four standoff holes and place the ring pcb with the shiny side facing up and the tracks facing down onto the pogo pins.

[![The larger ring shaped board is now sitting on top of the round board with four nylon standoffs sitting along its inside circumference. The LED ring still sits to the side.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/2/AttachNylonStandoffs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/AttachNylonStandoffs.jpg)

Now pick up your LED retainer board and carefully place it on top, threading each bolt through its corresponding standoff. Three out of the four mounting holes on the boards have exposed copper pads and are highlighted in green in the image below. To get the orientation right, make sure to align the mounting holes relative to the one without the plated through holes (highlighted in red) for the base board and LED ring.

[![Mounting Holes Highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/2/MountingHolesHighlighted.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/MountingHolesHighlighted.png)

If your orientation isn\'t right, the LED ring won\'t work. Carefully lift the entire stack and place the nuts on the end of the bolts.

[![Two hands hold the LED ring, now in position on top of the stack with LEDs facing down.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/2/AlignMountingHolesPlatedThroughHoles.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/AlignMountingHolesPlatedThroughHoles.jpg)

Tighten everything down firmly but not crazy tight.

[![Side view of the stack as it is held and the nuts are tightened onto the backside of the assembly.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/2/TightenScrews.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/TightenScrews.jpg)

### Step 5 - Enjoy!

You can now solder some wires or pin headers to the 5-pin header on the base board and hook it up to your project!

[![top down view of the completed assembly. A round contraption with a notched ring along the outside, trapped in place by a top retaining ring. You can see through the center of the retaining ring to the base board below which is covered in white silkscreen. This is designed to reflect the LEDs which are mounted on the underside of the retaining ring.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/2/AssembledRotaryDial.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/AssembledRotaryDial.jpg)

## Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

[![GIF Rotary Dial](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/14790-Rotary_Dial.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/14790-Rotary_Dial.gif)

### Hookup Table

Here are two simple Arduino examples to get you started. Both of them have been tested to work with the SparkFun RedBoard with the following connections:

  RedBoard   Rotary Dial
  ---------- -------------
  GND        GND
  **5V**     **5V**
  D8         LED IN
  D5         ENC A
  D6         ENC B

Once connected, your setup should look similar to the image below.

[![Hardware Hookup between Arduino and Rotary Dial](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/14790-Rotary_Dial-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/14790-Rotary_Dial-05.jpg)

Both examples also make use of the [PJRC Encoder Library](https://www.pjrc.com/teensy/td_libs_Encoder.html) and the [Adafruit NeoPixel Library](https://github.com/adafruit/Adafruit_NeoPixel).

### Example 1 - Color Wheel

This example uses pieces of the NeoPixel example code combined with pieces of the Encoder example code to implement a color selector. As you turn the encoder wheel one direction or the other, you will cycle through the RGB color space on all eight RGB LEDs at once.

    language:c
    #include <Adafruit_NeoPixel.h>
    #include <Encoder.h>

    Encoder myEnc(5, 6);

    Adafruit_NeoPixel strip = Adafruit_NeoPixel(8, 8, NEO_GRB + NEO_KHZ800);

    void setup() 

    long oldPosition  = -999;

    void loop() 

        strip.show();

      }

    }

    // Input a value 0 to 255 to get a color value.
    // The colours are a transition r - g - b - back to r.
    uint32_t Wheel(byte WheelPos) 
      if(WheelPos < 170) 
      WheelPos -= 170;
      return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
    }

### Example 2 - Rotary Selector

This example is almost identical except that as you turn the encoder ring, only one LED will light at a time, moving in the same direction that you turn the ring.

    language:c
    #include <Adafruit_NeoPixel.h>
    #include <Encoder.h>

    Encoder myEnc(5, 6);

    Adafruit_NeoPixel strip = Adafruit_NeoPixel(8, 8, NEO_GRB + NEO_KHZ800);

    void setup() 

    long oldPosition  = -999;

    void loop() 

        int dot = abs(newPosition)%8;
        strip.setPixelColor(dot, Wheel((newPosition*5) & 255));
        strip.show();

      }

    }

    // Input a value 0 to 255 to get a color value.
    // The colours are a transition r - g - b - back to r.
    uint32_t Wheel(byte WheelPos) 
      if(WheelPos < 170) 
      WheelPos -= 170;
      return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
    }

[![This image is an invisible square but it\'s here so that I can ask you a favor if you\'re enjoying this tutorial using a screen reader. I\'m trying to improve our site\'s accessibility, so I would love to hear your feedback about the image alt tags in this article. You can email me at nick.poole@sparkfun.com and please put the phrase \"image tags\" in the subject line. Thank you so much. Happy Hacking!](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/FFFFFF-0.0.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/2/FFFFFF-0.0.png)