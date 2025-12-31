# Source: https://learn.sparkfun.com/tutorials/sik-keyboard-instrument

## Introduction

The [SparkFun Inventor\'s Kit](https://www.sparkfun.com/products/12060) (SIK) is a great starting place for learning about electronics, programming, and physical computing. We can combine some of the concepts found in the [SIK Guide](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32) to make our own projects. In this tutorial, we will make a keyboard using parts found in the SIK.

[![SIK Piano Keyboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-14.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-14.jpg)

We can use the Arduino to read the location of a touch on the soft potentiometer strip (\"soft pot\") and use that information to play a particular note from the buzzer. While it may be small, we can divide the soft pot into 8 segments. That\'s enough for a scale! In this case, we\'ll use the [C major scale](https://en.wikipedia.org/wiki/C_major).

### Required Materials

From the SIK, you will need:

In addition, you will need a few tools:

- Scissors
- Masking tape
- [Hobby knife](https://www.sparkfun.com/products/9200)
- Ruler
- Pen or Sharpie
- Cardboard (a small box is preferable)

[![Other required tools](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-01.jpg)

### Suggested Reading

Before continuing with this project, we suggest you be familiar with a few concepts:

- [SIK Guide: Reading a Soft Potentiometer](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32/experiment-10-reading-a-soft-potentiometer)
- [SIK Guide: Using a Piezo Buzzer](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32/experiment-11-using-a-piezo-buzzer)

## Hardware Hookup 

### Prepare the Breadboard

Before connecting anything, we recommend separating the breadboard into its three parts. Use a pair of scissors to cut the adhesive backing. This part is optional, but it helps the breadboard fit into the project enclosure later.

[![Cutting the breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-02.jpg)

### Connect the Components

Once you are ready to connect the components, check out the Fritzing diagram below.

Polarized Components []

Pay special attention to the component's markings indicating how to place it on the breadboard. Polarized components can only be connected to a circuit in one direction.

[![SIK keyboard Fritzing diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/sik_keyboard_fritzing_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/sik_keyboard_fritzing_bb.png)

*Having a hard time seeing the circuit? Click on the Fritzing diagram to see a bigger image.*

Once you are done, the soft pot should be sticking straight up from the breadboard.

[![Completed wiring](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-03.jpg)

### Create the Keyboard

The \"keyboard\" is actually the soft potentiometer. We will divide up the soft pot into eight (8) segments, and the resistance we read with the Arduino from touching the soft pot will determine the key being pressed.

To create something that looks like a keyboard, place a piece of masking tape over the soft pot so it covers the entire length with some overhand (we will use the overhang to attach the soft pot to the box).

[![Tape on the soft pot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-04.jpg)

Place a ruler next to the touchable (silver) area on the soft pot. Starting from the breadboard end, mark every 6mm. Fill in or note that the first 6mm section is not to be used.

[![Marking out the keyboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-05.jpg)

Starting from the breadboard side, write the note of each key in between the marks. We\'ll use C, D, E, F, G, A, B, C.

[![Marking notes on the keys](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-06.jpg)

### Make the Project Box

While we can play our keyboard on the breadboard, it might be more fun to have it in a project box to add a little stability.

Peel the backing off the two pieces of the breadboard to which we attached components.

[![Peel off the breadboard backing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-07.jpg)

Attach the large breadboard piece to the side of the cardboard box with the soft pot lying flat on the box\'s floor. Stick the smaller breadboard piece (the one with the buzzer) to the box\'s floor opposite the soft pot. Stick the overhang tape on the soft pot to the floor of the box.

[![Attach the breadboard pieces to the inside of the box](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-08.jpg)

Fold a piece of tape over (into a loop), and stick it to the RedBoard.

[![Sticking tape to the RedBoard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-09.jpg)

Place the RedBoard in between the soft pot and top breadboard piece.

[![Arduino in place](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-10.jpg)

Use the scissors to remove the top of the box.

[![Cut off the box top](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-11.jpg)

Use the hobby knife to cut a hole in the side of the box so you can pass the USB cable through for power.

[![Cut a hole in the box](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-12.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-12.jpg)

Cut a large notch in the front of the box just above the keyboard. This allows for easier access to the keyboard.

[![Cut a hole in the front to access the keyboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-13.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-13.jpg)

## The Code

To program the Arduino from your browser, select **SparkFun RedBoard** in the first drop-down menu in the window below, select the COM port associated with your RedBoard, and click **Run on Arduino**.

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Copy the following code into the editor and click the **Upload** button.

    language:c
    /**
     * SparkFun Inventor's Kit Project
     * Keyboard Instrument
     * Date: March 29, 2016
     * 
     * Description:
     *  Use the soft touch potentiometer as a keyboard segmented into
     *  8 keys: C, D, E, F, G, A, B, C. When each key is pressed, the 
     *  corresponding note is played through a buzzer.
     * 
     * Hardware Connections:
     *  Arduino | Soft Pot | Buzzer
     *  ---------------------------
     *    5V    |   pin 3  |   
     *    A0    |   pin 2  |   
     *    GND   |   pin 1  |   
     *    9     |          |   +
     *    GND   |          |   -
     *    
     *  You will also need to attach a 10k resistor from pin 2 to
     *  pin 1 (GND) on the soft pot.
     *  
     * License:
     *  Public Domain
     */

    // Constants
    const int SENSOR_PIN = 0;   // Analog input pin for soft pot
    const int BUZZER_PIN = 9;   // PWM digital output pin for buzzer
    const int DURATION = 10;    // Time (ms) to play a note

    // This function is run only once as soon as the Arduino boots
    void setup() 
    

    // This gets run over and over right after the setup() function
    void loop() 
    
    }

    // Given an ADC value (0 - 1023), map it to a note
    char findNote(int val)
    
      if ( (val > 160) && (val <= 250) )
      
      if ( (val > 250) && (val <= 350) )
      
      if ( (val > 350) && (val <= 450) )
      
      if ( (val > 450) && (val <= 560) )
      
      if ( (val > 560) && (val <= 690) )
      
      if ( (val > 690) && (val <= 850) )
      
      if ( (val > 850) && (val <= 1023) )
      

      // Return 0 to show that no key was pressed
      return 0;
    }

    // Translate a note (a, b, c, d, e, f, g) to its frequency
    int getFrequency(char note) 
    ;
      int frequencies[] = ;

      // Step though the notes
      for (i = 0; i < numNotes; i++)  // Step through the notes
      
      }

      // If we looked through everything and didn't find a note,
      // return 0, as we still need to return something.
      return(0);
    }

### Code to Note

We combine the code from [Part 10: Reading a Soft Potentiometer](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32/experiment-10-reading-a-soft-potentiometer) and [Part 11: Using a Piezo Buzzer in the SIK Guide](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32/experiment-11-using-a-piezo-buzzer), and we recommend you read the \"Code to Note\" sections in each of those to understand how we are getting data from the soft pot as well as playing particular frequencies on the buzzer.

    language:c
    if ( (val > 10) && (val <= 160) )
    
    ...

We pass the `findNote(int val)` function the analog-to-digital (ADC) value read from the soft pot. This information is stored in the `val` parameter. If we touch the soft pot towards the breadboard end, it will produce a *lower* value than if we touched it at the other end. The ADC value on the Arduino can be between 0 and 1023 (inclusive). So, we would read a value close to 10 if we touched it on the breadboard end and a value close to 1023 on the other end.

Since we divided up the soft pot\'s length into 6 mm segments, we also need to divide up the values we might receive from the soft pot. Let\'s say we touched the soft pot on the third segment (the one we labeled \"E\"), and the ADC value was 296 as a result. The first two `if` statements would return false, but the third one would be true, since 296 falls between 250 and 350. So, \'e\' is returned as the note we pressed on the soft pot.

## What You Should See

Once you have uploaded the code to the RedBoard, try lightly pressing on the soft potentiometer. You should hear some musical notes from the speaker!

[![Playing the keyboard instrument](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-15.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/2/SIK_Keyboard_Instrument_Tutorial-15.jpg)

Want to play a song? How about *Twinkle, Twinkle, Little Star* (\'C\' is the first \'C\' on the left in this case):

**C, C, G, G, A, A, G (hold)\
F, F, E, E, D, D, C (hold)**

What other songs can you play? [Here are some ideas to get you started](http://missjacobsonsmusic.blogspot.com/2009/10/recorder-songs-also-played-on-keyboard.html).

### Troubleshooting

#### No Sound

Given the size and shape of the piezo buzzer it is easy to miss the right holes on the breadboard. Try double checking its placement. Additionally, check the wiring for the soft pot.

#### Can\'t Press More than One Key

The soft potentiometer is incapable of detecting more than one press at a time. What happens if you try to press two keys at once?