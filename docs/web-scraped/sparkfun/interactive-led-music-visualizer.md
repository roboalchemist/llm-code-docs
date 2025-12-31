# Source: https://learn.sparkfun.com/tutorials/interactive-led-music-visualizer

## Introduction 

Let\'s face it: nowadays, most musical performances are complimented by some fancy light shows. Go to any concert, festival, club \-- they all have a corresponding visual performance or effects. Why not add your own home to that list? Here\'s a simple yet effective project to make your very own [son et lumière](https://en.wikipedia.org/wiki/Son_et_lumi%C3%A8re_(show\))!

*All palettes work with every visualization, but, for timeliness, not every combination is shown.*

### Required Materials

To follow along with this tutorial, you\'ll need the following materials. The partial wishlist on the left is for the simple circuit. It does not include the potentiometer and buttons. The full wishlist on the right is for the full circuit. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

Any microcontroller with 3.3V and 5V pins will suffice. Any analog potentiometer and size momentary button should work. Depending on your intent, the trimpot and buttons may not be necessary.

- **Trimpot** \-- The trimpot is only used to adjust the **brightness threshold**, so, if you want maximum brightness, you don\'t have to worry about incorporating it.
- **Buttons** \-- The three buttons **cycle color schemes, visualizations, and shuffle mode** respectively, so, if you want to do without those features (and just use shuffle mode all the time), that\'s also a possibility.

If you\'re compiling from the [Arduino IDE](https://www.arduino.cc/en/Main/Software) or similar, you\'ll want to snag the the [NeoPixel Library](https://github.com/adafruit/Adafruit_NeoPixel) since the code used is heavily based on it. The resistor and capacitor are not required, but they will help prevent possible damage to the LEDs. Any resistor between 300--500 Ω can be used.

It is also suggested that you use an [Arduino and Breadboard Holder](https://www.sparkfun.com/products/11235) to simplify wiring and to mount the LED strip:

[![Full Visualizer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/0/Music_Visualizer_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/0/Music_Visualizer_Tutorial-01.jpg)

*A small notch was cut in the Breadboard Holder to hold a piece of MDF, on which the LEDs are attached.*

### Recommended Reading

Before embarking upon this tutorial, you may find the following links useful:

- Arduino.cc
  - [Arduino Sketch Tutorial](https://www.arduino.cc/en/Tutorial/Sketch)
  - [Arduino Reference](https://www.arduino.cc/en/Reference/HomePage)
- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [Wikipedia: RGB Color Model](https://en.wikipedia.org/wiki/RGB_color_model)
- [WS2812 Breakout Hookup Guide](https://learn.sparkfun.com/tutorials/ws2812-breakout-hookup-guide)
- [Sound Detector Hookup Guide](https://learn.sparkfun.com/tutorials/sound-detector-hookup-guide)
- [How to Power a Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

Since we\'re using the NeoPixel library, it may also be a good idea to get familiar with the [NeoPixel Documentation](http://learn.adafruit.com/downloads/pdf/adafruit-neopixel-uberguide.pdf).

## Assembly

Depending on your setup, the project may not require any soldering! The few exceptions will probably be soldering some pins to the sound detector, and, if you\'ve cut a roll of addressable LEDs in the middle, you\'ll have to solder some wires to the starting LED\'s pins. If you\'ve never soldered before, I highly suggest taking a look at [this guide to solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering).

Below is also a general chart for how the pin(s) on each component should be routed and an accompanying diagram. Before you begin, here are some things to keep in mind:

- Be conscious of the orientation you think would allow the sound detector to take optimal readings for your intentions. Bending the pins to hold the sound detector perpendicular to the breadboard is a recommended option.
- Electrolytic capacitors are [polarized](https://learn.sparkfun.com/tutorials/polarity), so how they are oriented is important. Make sure to place the side with a white stripe and a negative symbol into a negative current (ground) and the other into positive current.
- Resistors and pushbuttons are not polarized.
- Trimpots are not polarized either, however their middle pin is the analog output, so don\'t power that directly.

The pins used in the diagram and the code are in parentheses. If you use a different pin, don\'t forget to change it in the code as well:

Sound Detector

Addressable LED strip

Trimpot

Pushbutton

1 mF (1000 µF) Capacitor

300--500 Ω Resistor

Envelope → Analog (A0)

Digital/Analog (A5) → Resistor → DIN

5V → left or right pin

GND → Either side

Between ground and 5V

Between Digital/Analog (A5) and DIN on LED strip

3.3V → VCC

5V →5V

Middle pin → Analog (A1)

Other side → Digital (4, 5, 6)

GND → GND

GND → GND

Remaining left or right pin → GND

The circuit should look something like the diagrams below. If you just want the LEDs to react to sound using one visualizer and one color palette, you can build the simple circuit on the left. If you want to take advantage of all the visuals, palettes, and shuffle mode, you can build the full circuit on the right.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Simple Interactive LED Music Visualizer Fritzing Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/0/SparkFun_Simple_Interactive_LED_Music_Visualizer_Fritzing_bb.jpg "Simple Interactive LED Music Visualizer Fritzing Circuit, Click Image for a Closer Look")](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/0/SparkFun_Simple_Interactive_LED_Music_Visualizer_Fritzing_bb.jpg)   [![Full Interactive LED Music Visualizer Fritzing Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/0/SparkFun_Full_Interactive_LED_Music_Visualizer_Fritzing_bb.jpg "Full Interactive LED Music Visualizer Fritzing Circuit, Click Image for a Closer Look")](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/0/SparkFun_Full_Interactive_LED_Music_Visualizer_Fritzing_bb.jpg)
  *Simple Circuit*                                                                                                                                                                                                                                                                                                                                                                                                    *Full Circuit*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Fritzing diagram for the circuit as described above. Click the images for a closer look.*

After assembling the circuit, you should have something similar to the image below. Depending on your setup, you may have less components.

[![Circuit Connected Together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/0/Music_Visualizer_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/0/Music_Visualizer_Tutorial-03.jpg)

**Sound Detector Notes:** The microphone used is not a sophisticated, logarithmic sound receiver like your ear; it is only measuring compressional waves in the air. Consequently, the microphone is more likely to detect and/or prioritize lower-frequency sounds since they require more energy to propagate, and therefore oscillate the air more intensely. Also, a resistor can be placed in the \"GAIN\" slots to modify the gain. Standard gain should be sufficient for our purposes, but, for more info, visit [this tutorial to modify the gain.](https://learn.sparkfun.com/tutorials/sound-detector-hookup-guide#configuration)\
\

[![Through Hole to Adjust Gain](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/0/7/Sound_Detector_Hookup_Guide-01.jpg "Click for more information about adjsting the gain in the Sound Detector Hookup Guide: Configuration")](https://learn.sparkfun.com/tutorials/sound-detector-hookup-guide#configuration)

## Programming 

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### WS2812 Arduino Library

If you have not already, install the library by searching for **NeoPixel** within the Arduino IDE\'s library manager. You can also manually install the [NeoPixel library](https://github.com/adafruit/Adafruit_NeoPixel) by downloading a zip.

[NeoPixel Arduino Library (ZIP)](https://github.com/adafruit/Adafruit_NeoPixel/archive/master.zip)

### Simple Visualizer Program

Below is a small sample program to test if everything is connected properly with the simple and full circuit. It only contains **one visualizer** and **one color palette** to keep things concise. It doesn\'t need buttons since there\'s nothing to toggle, but you can still use it to test your potentiometer. Make sure to adjust the number of LEDs (i.e. `LED_TOTAL`) depending on the length of LED strip that you are using. Copy and paste the code in the Arduino IDE. Select your board, COM port, and press the upload button!

    language:c
    //Program by Michael Bartlett

    //Libraries
    #include <Adafruit_NeoPixel.h>  //Library to simplify interacting with the LED strand
    #ifdef __AVR__
    #include <avr/power.h>   //Includes the library for power reduction registers if your chip supports them. 
    #endif                   //More info: http://www.nongnu.org/avr-libc/user-manual/group__avr__power.htlm

    //Constants (change these as necessary)
    #define LED_PIN   A5  //Pin for the pixel strand. Does not have to be analog.
    #define LED_TOTAL 60  //Change this to the number of LEDs in your strand.
    #define LED_HALF  LED_TOTAL/2
    #define AUDIO_PIN A0  //Pin for the envelope of the sound detector
    #define KNOB_PIN  A1  //Pin for the trimpot 10K

    //////////<Globals>
    //  These values either need to be remembered from the last pass of loop() or 
    //  need to be accessed by several functions in one pass, so they need to be global.

    Adafruit_NeoPixel strand = Adafruit_NeoPixel(LED_TOTAL, LED_PIN, NEO_GRB + NEO_KHZ800);  //LED strand objetc

    uint16_t gradient = 0; //Used to iterate and loop through each color palette gradually

    uint8_t volume = 0;    //Holds the volume level read from the sound detector.
    uint8_t last = 0;      //Holds the value of volume from the previous loop() pass.

    float maxVol = 15;     //Holds the largest volume recorded thus far to proportionally adjust the visual's responsiveness.
    float knob = 1023.0;   //Holds the percentage of how twisted the trimpot is. Used for adjusting the max brightness.
    float avgVol = 0;      //Holds the "average" volume-level to proportionally adjust the visual experience.
    float avgBump = 0;     //Holds the "average" volume-change to trigger a "bump."

    bool bump = false;     //Used to pass if there was a "bump" in volume

    //////////</Globals>

    //////////<Standard Functions>

    void setup() 

    void loop() 

      //If there is a decent change in volume since the last pass, average it into "avgBump"
      if (volume - last > avgVol - last && avgVol - last > 0) avgBump = (avgBump + (volume - last)) / 2.0;

      //if there is a notable change in volume, trigger a "bump"
      bump = (volume - last) > avgBump;

      Pulse();   //Calls the visual to be displayed with the globals as they are.

      gradient++;    //Increments gradient

      last = volume; //Records current volume for next pass

      delay(30);   //Paces visuals so they aren't too fast to be enjoyable
    }

    //////////</Standard Functions>

    //////////<Helper Functions>

    //PULSE
    //Pulse from center of the strand
    void Pulse() 
        //Sets the max brightness of all LEDs. If it's loud, it's brighter.
        //  "knob" was not used here because it occasionally caused minor errors in color display.
        strand.setBrightness(255.0 * pow(volume / maxVol, 2));
      }

      //This command actually shows the lights. If you make a new visualization, don't forget this!
      strand.show();
    }

    //Fades lights by multiplying them by a value between 0 and 1 each pass of loop().
    void fade(float damper) 
    }

    uint8_t split(uint32_t color, uint8_t i ) 

    //This function simply take a value and returns a gradient color
    //  in the form of an unsigned 32-bit integer

    //The gradient returns a different, changing color for each multiple of 255
    //  This is because the max value of any of the 3 LEDs is 255, so it's
    //  an intuitive cutoff for the next color to start appearing.
    //  Gradients should also loop back to their starting color so there's no jumps in color.

    uint32_t Rainbow(unsigned int i) 

    //////////</Helper Functions>

### Full Visualizer Program

The complete program featured in the video can be found from a copy of [bartlettmic\' GitHub repository: SparkFun RGB LED Music Sound Visualizer Arduino Code](https://github.com/sparkfun/SparkFun-RGB-LED-Music-Sound-Visualizer-Arduino-Code). However, you can also find the code below with the number of LEDs adjusted for one addressable LED strip. Copy and paste the code in the Arduino IDE. Select your board, COM port, and press the upload button!

    language:c
    /* SparkFun Addressable RGB LED Sound and Music Visualizer Tutorial Arduino Code
     * by: Michael Bartlett
     * SparkFun Electronics
     * date: 2/7/16
     * license: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)
     * Do whatever you'd like with this code, use it for any purpose.
     * Please attribute and keep this license.
    */

    //Libraries
    #include <Adafruit_NeoPixel.h>  //Library to simplify interacting with the LED strand
    #ifdef __AVR__
    #include <avr/power.h>   //Includes the library for power reduction registers if your chip supports them. 
    #endif                   //More info: http://www.nongnu.org/avr-libc/user-manual/group__avr__power.htlm

    //Constants (change these as necessary)
    #define LED_PIN   A5  //Pin for the pixel strand. Can be analog or digital.
    #define LED_TOTAL 60  //Change this to the number of LEDs in your strand.
    #define LED_HALF  LED_TOTAL/2
    #define VISUALS   6   //Change this accordingly if you add/remove a visual in the switch-case in Visualize()

    #define AUDIO_PIN A0  //Pin for the envelope of the sound detector
    #define KNOB_PIN  A1  //Pin for the trimpot 10K
    #define BUTTON_1  6   //Button 1 cycles color palettes
    #define BUTTON_2  5   //Button 2 cycles visualization modes
    #define BUTTON_3  4   //Button 3 toggles shuffle mode (automated changing of color and visual)

    //////////<Globals>
    //  These values either need to be remembered from the last pass of loop() or
    //  need to be accessed by several functions in one pass, so they need to be global.

    Adafruit_NeoPixel strand = Adafruit_NeoPixel(LED_TOTAL, LED_PIN, NEO_GRB + NEO_KHZ800);  //LED strand objetcs

    uint16_t gradient = 0; //Used to iterate and loop through each color palette gradually

    //IMPORTANT:
    //  This array holds the "threshold" of each color function (i.e. the largest number they take before repeating).
    //  The values are in the same order as in ColorPalette()'s switch case (Rainbow() is first, etc). This is simply to
    //  keep "gradient" from overflowing, the color functions themselves can take any positive value. For example, the
    //  largest value Rainbow() takes before looping is 1529, so "gradient" should reset after 1529, as listed.
    //     Make sure you add/remove values accordingly if you add/remove a color function in the switch-case in ColorPalette().
    uint16_t thresholds[] = ;

    uint8_t palette = 0;  //Holds the current color palette.
    uint8_t visual = 0;   //Holds the current visual being displayed.
    uint8_t volume = 0;   //Holds the volume level read from the sound detector.
    uint8_t last = 0;     //Holds the value of volume from the previous loop() pass.

    float maxVol = 15;    //Holds the largest volume recorded thus far to proportionally adjust the visual's responsiveness.
    float knob = 1023.0;  //Holds the percentage of how twisted the trimpot is. Used for adjusting the max brightness.
    float avgBump = 0;    //Holds the "average" volume-change to trigger a "bump."
    float avgVol = 0;     //Holds the "average" volume-level to proportionally adjust the visual experience.
    float shuffleTime = 0;  //Holds how many seconds of runtime ago the last shuffle was (if shuffle mode is on).

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //NOTE: The reason "average" is quoted is because it is not a true mathematical average. This is because I have
    //      found what I call a "sequenced average" is more successful in execution than a real average. The difference
    //      is that the sequenced average doesn't use the pool of all values recorded thus far, but rather averages the
    //      last average and the current value received (in sequence). Concretely:
    //
    //          True average: (1 + 2 + 3) / 3 = 2
    //          Sequenced: (1 + 2) / 2 = 1.5 --> (1.5 + 3) / 2 = 2.25  (if 1, 2, 3 was the order the values were received)
    //
    //      All "averages" in the program operate this way. The difference is subtle, but the reason is that sequenced
    //      averages are more adaptive to changes in the overall volume. In other words, if you went from loud to quiet,
    //      the sequenced average is more likely to show an accurate and proportional adjustment more fluently.
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    bool shuffle = false;  //Toggles shuffle mode.
    bool bump = false;     //Used to pass if there was a "bump" in volume

    //For Traffic() visual
    int8_t pos[LED_TOTAL] = ;    //Stores a population of color "dots" to iterate across the LED strand.
    uint8_t rgb[LED_TOTAL][3] = ;  //Stores each dot's specific RGB values.

    //For Snake() visual
    bool left = false;  //Determines the direction of iteration. Recycled in PaletteDance()
    int8_t dotPos = 0;  //Holds which LED in the strand the dot is positioned at. Recycled in most other visuals.
    float timeBump = 0; //Holds the time (in runtime seconds) the last "bump" occurred.
    float avgTime = 0;  //Holds the "average" amount of time between each "bump" (used for pacing the dot's movement).

    //////////</Globals>

    //////////<Standard Functions>

    void setup() 

    void loop() 

      //If there is a decent change in volume since the last pass, average it into "avgBump"
      if (volume - last > 10) avgBump = (avgBump + (volume - last)) / 2.0;

      //If there is a notable change in volume, trigger a "bump"
      //  avgbump is lowered just a little for comparing to make the visual slightly more sensitive to a beat.
      bump = (volume - last > avgBump * .9);  

      //If a "bump" is triggered, average the time between bumps
      if (bump) 

      Visualize();   //Calls the appropriate visualization to be displayed with the globals as they are.

      gradient++;    //Increments gradient

      last = volume; //Records current volume for next pass

      delay(30);     //Paces visuals so they aren't too fast to be enjoyable
    }
    //////////</Standard Functions>

    //////////<Visual Functions>

    //This function calls the appropriate visualization based on the value of "visual"
    void Visualize() 
    }

    //////////////////////////////////////////////////////////////////////////////////////////////////////////
    //NOTE: The strand displays RGB values as a 32 bit unsigned integer (uint32_t), which is why ColorPalette()
    //      and all associated color functions' return types are uint32_t. This value is a composite of 3
    //      unsigned 8bit integer (uint8_t) values (0-255 for each of red, blue, and green). You'll notice the
    //      function split() (listed below) is used to dissect these 8bit values from the 32-bit color value.
    //////////////////////////////////////////////////////////////////////////////////////////////////////////

    //This function calls the appropriate color palette based on "palette"
    //  If a negative value is passed, returns the appropriate palette withe "gradient" passed.
    //  Otherwise returns the color palette with the passed value (useful for fitting a whole palette on the strand).
    uint32_t ColorPalette(float num) 
    }

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //NOTE: All of these visualizations feature some aspect that affects brightness based on the volume relative to
    //      maxVol, so that louder = brighter. Initially, I did simple proportions (volume/maxvol), but I found this
    //      to be visually indistinct. I then tried an exponential method (raising the value to the power of
    //      volume/maxvol). While this was more visually satisfying, I've opted for a balance between the two. You'll
    //      notice something like pow(volume/maxVol, 2.0) in the functions below. This simply squares the ratio of
    //      volume to maxVol to get a more exponential curve, but not as exaggerated as an actual exponential curve.
    //      In essence, this makes louder volumes brighter, and lower volumes dimmer, to be more visually distinct.
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

    //PULSE
    //Pulse from center of the strand
    void Pulse() 
          avgCol /= 3.0, avgCol2 /= 3.0;

          //Compare the average colors as "brightness". Only overwrite dim colors so the fade effect is more apparent.
          if (avgCol > avgCol2) strand.setPixelColor(i, strand.Color(colors[0], colors[1], colors[2]));
        }
      }
      //This command actually shows the lights. If you make a new visualization, don't forget this!
      strand.show();
    }

    //PALETTEPULSE
    //Same as Pulse(), but colored the entire pallet instead of one solid color
    void PalettePulse() 
          avgCol /= 3.0, avgCol2 /= 3.0;
          if (avgCol > avgCol2) strand.setPixelColor(i, strand.Color(colors[0], colors[1], colors[2]));
        }
      }
      strand.show();
    }

    //TRAFFIC
    //Dots racing into each other
    void Traffic() 
        }

        //If there is an open slot, set it to an initial position on the strand.
        if (slot != -3) 
        }
      }

      //Again, if it's silent we want the colors to fade out.
      if (volume > 0) 
      }
      strand.show(); //Again, don't forget to actually show the lights!
    }

    //SNAKE
    //Dot sweeping back and forth to the beat
    void Snake() 

      fade(0.975); //Leave a trail behind the dot.

      uint32_t col = ColorPalette(-1); //Get the color at current "gradient."

      //The dot should only be moved if there's sound happening.
      //  Otherwise if noise starts and it's been moving, it'll appear to teleport.
      if (volume > 0) 

      strand.show(); // Display the lights

      //Check if dot position is out of bounds.
      if (dotPos < 0)    dotPos = strand.numPixels() - 1;
      else if (dotPos >= strand.numPixels())  dotPos = 0;
    }

    //PALETTEDANCE
    //Projects a whole palette which oscillates to the beat, similar to the snake but a whole gradient instead of a dot
    void PaletteDance() 

        //After all that, appropriately reposition "dotPos."
        dotPos += (left) ? -1 : 1;
      }

      //If there's no sound, fade.
      else  fade(0.8);

      strand.show(); //Show lights.

      //Loop "dotPos" if it goes out of bounds.
      if (dotPos < 0) dotPos = strand.numPixels() - strand.numPixels() / 6;
      else if (dotPos >= strand.numPixels() - strand.numPixels() / 6)  dotPos = 0;
    }

    //GLITTER
    //Creates white sparkles on a color palette to the beat
    void Glitter() 

      //Create sparkles every bump
      if (bump) 
      bleed(dotPos);
      strand.show(); //Show the lights.
    }

    //PAINTBALL
    //Recycles Glitter()'s random positioning; simulates "paintballs" of
    //  color splattering randomly on the strand and bleeding together.
    void Paintball() 
      strand.show(); //Show lights.
    }

    /////////////////////////////////////////////////////////////////////////////////////////////////////
    //DEBUG CYCLE
    //No reaction to sound, merely to see gradient progression of color palettes
    //NOT implemented in code as is, but is easily includable in the switch-case.
    void Cycle() 
      strand.show();
      gradient += 32;
    }
    /////////////////////////////////////////////////////////////////////////////////////////////////////

    //////////</Visual Functions>

    //////////<Helper Functions>

    void CyclePalette() 
      ///////////////////////////////////////////////////////////////////////////////////////////////////

      //If shuffle mode is on, and it's been 30 seconds since the last shuffle, and then a modulo
      //  of gradient to get a random decision between palette or visualization shuffle
      if (shuffle && millis() / 1000.0 - shuffleTime > 30 && gradient % 2) 
    }

    void CycleVisual() 

        //Like before, this delay is to prevent a button press from affecting "maxVol."
        delay(350);

        maxVol = avgVol; //Set max volume to average for a fresh experience
      }

      ///////////////////////////////////////////////////////////////////////////////////////////////////

      //If shuffle mode is on, and it's been 30 seconds since the last shuffle, and then a modulo
      //  of gradient WITH INVERTED LOGIC to get a random decision between what to shuffle.
      //  This guarantees one and only one of these shuffles will occur.
      if (shuffle && millis() / 1000.0 - shuffleTime > 30 && !(gradient % 2)) 
        maxVol = avgVol;
      }
    }

    //IMPORTANT: Delete this function  if you didn't use buttons./////////////////////////////////////////
    void ToggleShuffle() 
    }
    //////////////////////////////////////////////////////////////////////////////////////////////////////

    //Fades lights by multiplying them by a value between 0 and 1 each pass of loop().
    void fade(float damper) 
    }

    //"Bleeds" colors currently in the strand by averaging from a designated "Point"
    void bleed(uint8_t Point) ;

        for (int i = 0; i < 2; i++) ;

          //Sets the new average values to just the central point, not the left and right points.
          strand.setPixelColor(point, strand.Color(
                                 float( split(colors[0], 0) + split(colors[1], 0) + split(colors[2], 0) ) / 3.0,
                                 float( split(colors[0], 1) + split(colors[1], 1) + split(colors[2], 1) ) / 3.0,
                                 float( split(colors[0], 2) + split(colors[1], 2) + split(colors[2], 2) ) / 3.0)
                              );
        }
      }
    }

    //As mentioned above, split() gives you one 8-bit color value
    //from the composite 32-bit value that the NeoPixel deals with.
    //This is accomplished with the right bit shift operator, ">>"
    uint8_t split(uint32_t color, uint8_t i ) 

    //////////</Helper Functions>

    //////////<Palette Functions>

    //These functions simply take a value and return a gradient color
    //  in the form of an unsigned 32-bit integer

    //The gradients return a different, changing color for each multiple of 255
    //  This is because the max value of any of the 3 RGB values is 255, so it's
    //  an intuitive cutoff for the next color to start appearing.
    //  Gradients should also loop back to their starting color so there's no jumps in color.

    uint32_t Rainbow(unsigned int i) 

    uint32_t Sunset(unsigned int i) 

    uint32_t Ocean(unsigned int i) 

    uint32_t PinaColada(unsigned int i) 

    uint32_t Sulfur(unsigned int i) 

    uint32_t NoGreen(unsigned int i) 

    //NOTE: This is an example of a non-gradient palette: you will get straight red, white, or blue
    //      This works fine, but there is no gradient effect, this was merely included as an example.
    //      If you wish to include it, put it in the switch-case in ColorPalette() and add its
    //      threshold (764) to thresholds[] at the top.
    uint32_t USA(unsigned int i) 

    //////////</Palette Functions>

Things to remember before you compile:

- Adjust the **number of LEDs** (`LED_TOTAL`) that you are using in the strip.
- If you didn\'t use a **potentiometer**, don\'t forget to remove all references to the variable `knob` in the code ([ctrl]+[F] will come in handy for that). Otherwise, the program will think you still have a potentiometer that is set to a very low value (i.e. everything will be very dim).
- If you didn\'t use **buttons**, change the initialization `bool shuffle = false;` to `bool shuffle = true;`. The code should compile and run properly, but for good practice you should remove all blocks the code says to delete since they reference the `BUTTON` constants.\
  \

**Well Done!** For those curious about the math used to process the audio, check out the notes and graphs linked in the [code math.md](https://github.com/bartlettmic/SparkFun-RGB-LED-Music-Sound-Visualizer-Arduino-Code/blob/master/code%20math.md)! There\'s also some notes about how each visualization is calculated in each function.\
\

[![Volume Readings from bartlettmic\'s Notes](https://camo.githubusercontent.com/7e5dd682317ae82be1f6fbac20a036272998be51/687474703a2f2f692e696d6775722e636f6d2f394935347462592e706e67 "Click on the image to visit the notes.")](https://github.com/bartlettmic/SparkFun-RGB-LED-Music-Sound-Visualizer-Arduino-Code/blob/master/code%20math.md)

## Final Touches 

With the electronics and the code working, you can now add your visualizer to a variety of enclosures or art pieces. For the final touches on this project, an elk was laser etched on a piece of acrylic. The LED strip was then wrapped around the outer perimeter of the piece.

[![Elk](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/0/Elk2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/0/Elk2.jpg)

Add some music, and you have yourself a beautiful piece of interactive art.