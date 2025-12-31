# Source: https://learn.sparkfun.com/tutorials/cackling-apple-head-witch

## Introduction

In this tutorial, we\'ll show you how to create a fun, easy Halloween prop out of an apple and a few SparkFun parts. You\'ll sew a [LilyPad Light Sensor](https://www.sparkfun.com/products/8464) and [LilyPad MP3 Trigger](https://www.sparkfun.com/products/11013) onto a witch\'s dress and be able to customize your own sounds for the witch to make. By the end of the project you\'ll have a completed witch doll that will cackle as soon as the lights go down!

[![Apple Head Witch](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/01_completed_witch_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/01_completed_witch_2.jpg)

### Suggested Reading

If you\'ve never worked with e-textiles before, you may want to have a look at these other tutorials.

- [Getting Started with the LilyPad MP3 Player](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player)
- [E-Textiles Basics](https://learn.sparkfun.com/tutorials/e-textile-basics)
- [Sewing with Conductive Thread](https://learn.sparkfun.com/tutorials/sewing-with-conductive-thread)

## Materials and Tools

Let\'s go over all of the things you\'ll need to put your project together:

### You will also need:

- Stiff interfacing (18 inch circle cut in half)
- Fabric for your witch dress (19 inch circle cut in half)
- Felt for the speaker pocket (8x12 sheet will be plenty)
- Sharpened full length pencil
- Black pipe cleaner
- Black cardstock for your witch hat (one 8.5x11 sheet will do)
- Gray or black yarn for your witch hair (4 feet or so)
- White, black & red sewing pins (about 4-5)
- Small apple
- Hot glue gun
- Scissors

Here are some extra materials you might need in case you do not have these things at home.

## Step 1: Shrinking the Apple Head

[![Apple](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/03_apple.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/03_apple.jpg)

Peel a small apple, and leave it to dry out near a sunny window for about a week.

[![Peeling Apple](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/04_peeling_apple.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/04_peeling_apple.jpg)

[![Fully Peeled Apple](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/05_fully_peeled_apple.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/05_fully_peeled_apple.jpg)

You want the apple to become dried out for the witch face. It will naturally shrink in size.

![](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/apple_1.gif "Apple drying time lapse (gif - your browser does not support the <video> tag)")

Once the apple has been dried out and to the desired facial texture, cut off the top portion of the apple where the stem is (about a ¼ inch) to create a flat surface.

[![Cut Off Apple Head](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/06_dried_apple_top_cutoff.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/06_dried_apple_top_cutoff.jpg)

## Step 2: Programming the MP3 Trigger

While you\'re waiting for your apple head to shrink, let\'s get all the electronic bits together, and program the LilyPad MP3 Player with the sketch that will monitor the light sensor and play the scary sound when a shadow falls across it.

### Testing the circuit

To make sure everything works before you start sewing it into your project, we recommend using alligator clips to temporarily make all the electrical connections. You can easily attach alligator clips to the bare metal around the holes on the LilyPad boards.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/alligator2_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/alligator2_2.png)

Follow the above diagram to make the following connections:

  ---------------------------------------- --------------------------------------
  **from**                                 **to**
  LilyPad MP3 Player \"3.3V\"              LilyPad Light Sensor \"+\"
  LilyPad MP3 Player \"GND\"               LilyPad Light Sensor \"-\"
  LilyPad MP3 Player \"T1\"                LilyPad Light Sensor \"S\"
  LilyPad MP3 Player \"RIGHT SPEAKER +\"   Speaker + \*
  LilyPad MP3 Player \"RIGHT SPEAKER -\"   Speaker - \*
  Lipo Battery                             LilyPad MP3 Player battery connector
  5V FTDI board                            LilyPad MP3 Player FTDI connector
  ---------------------------------------- --------------------------------------

\

\* It doesn\'t matter which side of the speaker you connect to \"+\" and \"-\". However, if you use two speakers, make sure they\'re both connected the same way.

**OPTIONAL:** You can use one or two speakers. If you want to use two speakers, connect one speaker to the right speaker connections (+ and -), and the second speaker to the left speaker connections (+ and -).

**OPTIONAL:** If you want to connect LEDs that light up while audio is playing, you can connect them between the LilyPad MP3 Player\'s T2 terminal and GND.

The 5V FTDI board is used to program the LilyPad MP3 Player and recharge the battery. Plug the FTDI board\'s socket into the 6-pin connector on the LilyPad MP3 Player, and plug the other end of the USB cable into your computer. (It\'s normal for the yellow \"charge\" LED to come on when you do this, it will go out when the battery is fully charged.)

**TIP:** If you look closely at the FTDI board, you\'ll see labels that say \"GRN\" (green) and \"BLK\" (black). Match these up with the labels on the LilyPad MP3 Player when you\'re plugging them together. (These \"colors\" match the wires on a different FTDI cable.)

### Copy your sound file to the SD card

You can use almost any sound file you wish. Here\'s the one we\'re using for this project:

**[cackle.mp3](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/cackle.mp3)**

Right-click the above link, choose \"Save link\" to download the file to your computer, and copy it to your SD card. Insert the SD card into the socket on the LilyPad MP3 Player.

**NOTE:** The Arduino sketch (below) looks for a file called \"cackle.mp3\". If you use a different file, either rename it to \"cackle.mp3\", or change the filename at the top of the Arduino sketch.

Now, let\'s program the LilyPad MP3 Player!

### Install the Arduino software

If you have never used the Arduino software before, go through our [getting started tutorial](https://learn.sparkfun.com/tutorials/installing-arduino-ide) first. This will walk you through installing the Arduino software on your computer.

### Install the extra libraries

You\'ll now need to add the extra libraries needed to program the LilyPad MP3 Player. The easiest way to do this is:

1.  Go to the [LilyPad MP3 Player Github page](https://github.com/sparkfun/LilyPad_MP3_Player)
2.  Click the \"Download Zip\" button on the right-hand side to download an archive of the files you need. Save it on your computer.
3.  Locate your personal Arduino folder. This should be in your documents folder.
4.  Open the archive you downloaded, open the \"Arduino\" folder inside it, and drag the contents of that folder into your personal Arduino folder.

If any of this is confusing, check out our [Arduino library tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library).

### Load the sketch into the editor

Once you\'ve done that, start the Arduino IDE, and copy and paste the following sketch into the editing window:

    language:c
    // Applehead_witch
    // Demo program for Sparkfun's LilyPad MP3 Player
    // Mike Grusin, SparkFun Electronics

    // This sketch works with Amanda Clark's Apple Head Witch tutorial.
    // If your shadow passes over an innocent-looking apple-head doll,
    // the LilyPad MP3 Player will play a scary sound!

    // HOW IT WORKS:

    // The sketch monitors a light sensor connected to TRIG1.
    // When the sketch first runs, it will sample a baseline light level
    // and compute a threshold value (baseline * 0.9). After that, if the 
    // light level falls below this threshold, a sound file will play.
    // Also, TRIG2 will be set to HIGH while the file is playing, and 
    // LOW otherwise (for optional scary LED eyes or other features).

    // SOFTWARE INSTALLATION:

    // If you haven't yet, you should install the LilyPad MP3 Player
    // libraries available here: https://github.com/sparkfun/LilyPad_MP3_Player

    // HARDWARE CONNECTIONS:

    // Connect the "S" pin of the LilyPad Light Sensor to TRIG1.
    // Also connect 3.3V to the Light Sensor's "+" pin, and 
    // GND to the Light Sensor's "-" pin.
    // (Optional) Connect TRIG2 to LEDs through a resistor for 3.3V supply.
    // (330 Ohms is a common value).
    // Connect one or two speakers to the left and/or right speaker terminals.
    // Put a sound file on a microSD card and place it in the player.
    // Change the below filename to match the one you put on the SD card:

    char filename[] = "cackle.mp3";

    // Connect a 3.7V Lipo battery to the battery connector.
    // Connect a 5V FTDI Basic Breakout.
    // Remember to turn on the player before programming it!

    // RUNNING THE SKETCH

    // When you first run the sketch, the light sensor will be sampled for
    // the baseline light level. So have the project in it's installed position,
    // and avoid casting shadows on it, before turning it on.

    // Once it is on, when you cast a shadow over the project, it should play
    // the audio file through the speaker.

    // If it doesn't activate properly (too often or not often enough), 
    // you can adjust the sensitivity value below.
    // The sensitivity can be from 0.0 to 1.0. The closer it is to 1.0, the more
    // sensitive the sketch will be. If you make it 1.0, it will probably activate
    // continuously.
    // If your project it too sensitive, make the sensitivity smaller.
    // If your project is not sensitive enough, make the sensitivity larger.

    const float sensitivity = 0.9;

    // If the sketch does not work properly, connect your 5V FTDI and open a
    // Serial Monitor at 9600 baud to receive debugging information.

    // HAVE FUN!
    // Your friends at SparkFun

    // We'll need a few libraries to access all this hardware!

    #include <SPI.h>            // To talk to the SD card and MP3 chip
    #include <SdFat.h>          // SD card file system
    #include <SFEMP3Shield.h>   // MP3 decoder chip

    // Constants for the trigger pins:

    const int TRIG1 = A0;
    const int TRIG2 = A4;

    // Save the light sensor baseline reading:

    int threshold;

    // And a few output pins we'll be using:

    const int ROT_LEDR = 10; // Red LED in rotary encoder (optional)
    const int EN_GPIO1 = A2; // Amp enable + MIDI/MP3 mode select
    const int SD_CS = 9;     // Chip Select for SD card

    // Create library objects:

    SFEMP3Shield MP3player;
    SdFat sd;

    // Set debugging = true to send status messages to the serial port:

    boolean debugging = true;

    void setup()
    

      // Initialize the SD card; SS = pin 9, half speed at first

      if (debugging) Serial.print(F("initialize SD card... "));

      result = sd.begin(SD_CS, SPI_HALF_SPEED); // 1 for success

      if (result != 1) // Problem initializing the SD card
      
      else
        if (debugging) Serial.println(F("success!"));

      // Start up the MP3 library

      if (debugging) Serial.print(F("initialize MP3 chip... "));

      result = MP3player.begin(); // 0 or 6 for success

      // Check the result, see the MP3 library readme for error codes.

      if ((result != 0) && (result != 6)) // Problem starting up
      
        errorBlink(result); // Halt forever, blink red LED if present.
      }
      else
        if (debugging) Serial.println(F("success!"));

      // Set the VS1053 volume. 0 is loudest, 255 is lowest (off):

      MP3player.setVolume(10,10);

      // Get baseline readings from the light sensor:

      threshold = (analogRead(TRIG1));
      if (debugging)
      

      threshold = threshold * sensitivity;
      if (debugging)
      

      // Turn on the amplifier chip:

      digitalWrite(EN_GPIO1,HIGH);
      delay(2);
    }

    void loop()
    

      // Check to see whether we're below the threshold

      if (sensorvalue < threshold)
        

        // If we're currently playing a file, let it finish (don't start over)

        if (MP3player.isPlaying())
        
        }
        else
        
            else
            
            Serial.println(filename);
          }
        }
      }

      // For fun, we'll set TRIG2 HIGH while we're playing a file,
      // and LOW when the player is silent.

      if (MP3player.isPlaying())
        digitalWrite(TRIG2,HIGH);
      else
        digitalWrite(TRIG2,LOW);
    }

    void errorBlink(int blinks)
    
        delay(1500); // Longer pause between blink-groups
      }
    }

### Upload the sketch to the LilyPad MP3 Player

Turn the power switch on the LilyPad MP3 Player to ON. The red LED should light up.

In the Arduino IDE, go to the \"tools/board\" menu. Select **Arduino Pro or Pro Mini (3.3V, 8MHz) w/ ATmega328**.

Now go to the \"tools/serial port\" menu. Select the serial port that your FTDI is using. If you just installed it, this will be the highest number.

Now click the right-arrow button above the editing window. This will compile the sketch and upload it through the FTDI board to the LilyPad MP3 Player.

Hopefully you\'ll see some blinking on the FTDI, followed by an \"upload successful\" message. If there are errors, see the troubleshooting tips below.

### Try it out!

Once you\'ve uploaded the sketch, it will automatically start running. The first thing the sketch does is take a baseline reading from the light sensor. It will then keep monitoring the sensor, and if the sensor dips below that level (such as when a shadow passes across it), it will play the scary sound. *For best results, whenever you turn your project on, try not to be casting a shadow over it*.

**Try passing your hand over the light sensor, and see if it plays the scary sound**.

If it works, congratulations! If not, don\'t worry, see the troubleshooting tips below.

Once you know everything works, you\'re ready to build the rest of your project. Note that you won\'t have to reprogram the LilyPad MP3 Player again (unless you want to), it will remember the last sketch you uploaded to it!

### Troubleshooting

**Syntax errors** are almost always caused by not restarting the Arduino IDE after installing the libraries, or not installing the libraries correctly. Check your above steps to make sure you placed the new libraries into a \"libraries\" directory within your personal Arduino sketch folder.

**Uploading errors** may be caused by the LilyPad MP3 Player being switched off (it must be on to upload code), The FTDI drivers not being installed correctly, or selecting the wrong port in the \"tools/serial port\" menu.

**No sound?** If the code uploaded without errors but the sound still doesn\'t play, try looking at the debugging information. In the Arduino IDE, click on the magnifying glass button at the upper right. This will open a serial monitor window. Set the baud rate (bottom of window) to 9600 baud.

The LilyPad MP3 Player should now fill the window with text showing what it\'s doing and if there are any problems such as not being able to find the SD card or the proper filename on it.

**Still stumped?** If after all this you still can\'t get it working, don\'t panic! You can always contact our [Tech Support Department](https://www.sparkfun.com/static/technical_assistance). They\'ll be happy to help you get up and running.

## Step 3: Soldering the Speaker to the LilyPad MP3

Next, you're going to be doing some minimal [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering). Make sure to wear your safety glasses! Take your thin speaker and solder the positive wire into the positive left speaker pin on the MP3 trigger. Using flux on the pin will help the solder flow nicely onto it. Take the negative wire and solder it into the negative left speaker pin. (You may need to strip back some wire for more exposed wire to solder to the pin. Using [wire strippers](https://www.sparkfun.com/products/8696) will help.)

[![Soldering the Speaker](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/12_soldering_speakers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/12_soldering_speakers.jpg)

[![Speaker Attached to LilyPad MP3](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/13_speakers_attached_to_MP3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/13_speakers_attached_to_MP3.jpg)

## Step 4: Sewing in Your Components

Now, you'll take your interfacing and cut out an 18 inch diameter circle. After the circle is cut you'll want to cut the circle in half.

[![Interfacing Half Circle](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/07_interfacing_half_circle.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/07_interfacing_half_circle.jpg)

Grab your dress fabric and cut out a 19 inch diameter circle. You'll want this circle to be just a tad bit bigger than the interfacing circle so that it covers up the interfacing and you\'ll only see the dress fabric. After the circle is cut you'll want to cut the circle in half.

[![Interfacing & Velvet Half Circles](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/08_interfacing___velvet_half_circles.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/08_interfacing___velvet_half_circles.jpg)

Hot glue (or an adhesive that bonds well with fabric) the dress fabric onto the interfacing making sure that you don't see any of interfacing behind it. Make sure the two pieces are lined up well and that the bond is clean and tight with no wrinkles. This is one of the main focal points of the witch, so you want it to look good!

Next, take your LilyPad MP3 with the soldered speaker and position it inside of the dress with the speaker facing outward towards the front. By doing this you\'ll be able to hear the cackle more clearly when it is turned on. The MP3 Trigger may be hot glued to the inside of the dress. When hot gluing the MP3 board to the dress, make sure to avoid gluing any areas with exposed pins that are on the board. Make sure the side with the components on the MP3 board is facing out so you can easily access the pins.

Take your LilyPad light sensor, and figure out where you want it to be sewn into the dress. I find that the best place is the front of the dress for the best light exposure.

You're going to carefully sew traces to each of the following through the dress:

  ---------------------------------------------- -------------------------------------
  **from**                                       **to**
  S pin on the LilyPad light sensor              T1 pin on the MP3 Trigger
  negative pin (-) on the LilyPad light sensor   GND (ground) pin on the MP3 Trigger
  positive pin (+) on the LilyPad light sensor   3.3v pin on the MP3 Trigger
  ---------------------------------------------- -------------------------------------

\

Next, cut out two 3 inch squares of a sturdy fabric (felt will do). These are going to be your pockets for your speaker and battery to sit in inside of the dress .

Position the pockets so that they sit close to the front of the dress. Hot glue the sides and bottom of the squares and position them within the dress on the interfacing. Test to make sure your speaker and battery will sit nicely inside the pockets.

[![Sewing Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/back2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/back2.png)

[![Light Sensor Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/front2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/front2.png)

## Step 5: Getting Crafty with the Witch

Take your half circle of interface and fabric that are glued together with all of the components, and wrap it into a cone shape. Glue it together with your hot glue gun or some sort of strong, fabric adhesive. Make sure to leave enough space for your pencil body to go through at the top of the cone. (about ¼ inch diameter)

[![Cone Dress](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/09_cone_dress.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/09_cone_dress.jpg)

Make sure your pencil is sharpened. Use the leaded side of your pencil and stick it about halfway through the dried out apple. This will be your witch body. You may need to reinforce it by adding some hot glue so it stays in place.

[![Pencil Stab Apple](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/17_pencil_stab_apple.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/17_pencil_stab_apple.jpg)

Take your apple head on the pencil, and slide it through the top of the cone dress until the head is about ¼ inch away from where it'll meet the dress. Glue the cone dress to the pencil with your hot glue gun. Make sure the bond is secure.

[![Apple Head & Dress](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/18_apple_head_and_dress.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/18_apple_head_and_dress.jpg)

Take one black pipe cleaner, and wrap it around the area of the pencil that is exposed (in between the apple head and the dress). You are making the witch arms, so be sure they are even on both sides.

[![Twisting Arms](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/19_twisting_arms.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/19_twisting_arms.jpg)

[![Completed Arms](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/20_arms.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/20_arms.jpg)

Grab your bundle of yarn, and cut a piece about 5 inches long and leave it to the side. Take more of the yarn from the bundle and wrap it loosely around your four fingers about 40 times or so.

[![Yarn Bundle & Single Piece](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/21_yarn_bundle_and_single_piece.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/21_yarn_bundle_and_single_piece.jpg)

Cut the bottom of the loop of yarn. This will be the hair for your witch.

[![Cutting Yarn Bundle](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/22_cutting_yarn_bundle.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/22_cutting_yarn_bundle.jpg)

[![Yarn Cut in Half](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/23_yarn_cut_in_half.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/23_yarn_cut_in_half.jpg)

Grab the cut yarn and use the other 5 inch cut piece of cut yarn to tie the loop of yarn together.

[![Yarn Tied](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/24_yarn_tied.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/24_yarn_tied.jpg)

Using your hot glue gun, dab a drop of glue on the knot of the hair you tied together. Place it on the top of the dried apple making it look like a head of hair. Make sure the bond is nice and strong by holding the glued hair down on the apple for about 30 seconds.

[![Yarn Hair on Apple Head](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/25_yarn_as_hair_on_apple_head.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/25_yarn_as_hair_on_apple_head.jpg)

Now to make the witch's hat. Cut one 3 inch circle and one 6 inch circle out of black cardstock or felt. Cut a 2 inch hole within the middle of the 3 inch circle. Take the unused 6 inch circle, and cut it in half.

[![Hat Cutouts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/26_hat_cutouts.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/26_hat_cutouts.jpg)

Bend one of the half circles into a cone, and glue the seam. You have just made the base of the hat. For more detailed instructions check out [this video](https://www.youtube.com/watch?v=7vJxsvgnmlI). Make little 1/2 inch slits all around the base of the cone, and fold them up. This is where the brim of the hat will be glued to the cone base. Take the 3 inch circle with the 2 inch hole in it, and stick it through the top of the cone pulling it down to where the folded up fringe of the cone base is. This is the brim of your hat.

[![Fringe Hat Side View](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/27_fringe_hat_side_view.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/27_fringe_hat_side_view.jpg)

[![Fringe Hat Inside View](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/28_fringe_hat_inside_view.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/28_fringe_hat_inside_view.jpg)

Glue both pieces together, and now your hat is complete.

[![Completed Witch Hat](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/29_completed_witch_hat.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/29_completed_witch_hat.jpg)

Place the hat on the top of the apple head adjusting it to where it looks best. You may glue it down to the apple head if it tends to easily fall off.

Take your red sewing pins, and place them as eyes on your apple head. Then, take your white and black sewing pins, and use them to make the teeth. Using one black pin helps give the witch a rotten tooth look.

[![Sewing Needles](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/30_sewing_needles.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/30_sewing_needles.jpg)

[![Witch Eyes & Teeth](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/31_witch_eyes___teeth.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/31_witch_eyes___teeth.jpg)

Your witch is complete! Turn on the LilyPad MP3 and display your witch somewhere scary. Turn the lights low and hear her cackle. Enjoy!

[![Completed Apple Head Witch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/5/32_completed_witch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/5/32_completed_witch.jpg)