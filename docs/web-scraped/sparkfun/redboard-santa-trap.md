# Source: https://learn.sparkfun.com/tutorials/redboard-santa-trap

## Overview

A fun holiday project to try for anyone looking to catch Santa on Christmas!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/8/Santa_Trap_Image.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/8/Santa_Trap_Image.jpg)

### Required Materials

#### Electronics

#### Tools:

- [Soldering iron](https://www.sparkfun.com/products/12724%5D)
- [Solder](https://www.sparkfun.com/products/9325)

### Suggested Reading

Here are some other tutotials that may be helpful while completing this project.

- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering)
- [Working with Wire](https://learn.sparkfun.com/tutorials/working-with-wire)
- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)
- [Using the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

## Assembly

With this set up, you can try to catch Santa coming down the chimney, but even if he\'s clever enough to get past motion sensor without being detected, you can catch him when he goes to drink the milk left out for him.

[![Fritzing Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/8/Santa_trap_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/8/Santa_trap_bb.jpg)

Click image for a larger view.

The circuit works as follows:

- The LED is connected from [ground to 5V ^\[1\]^](https://learn.sparkfun.com/tutorials/redboard-santa-trap#min_voltage) through a resistor so it will be lit when there is power. This functions as an "ON" indicator, should the circuitry be far away from the RedBoard.
- The motion sensor has an alarm pin that goes LOW when it detects motion, so we can check that by hooking it up to the RedBoard and using a resistor to pull it to HIGH (or 5V) when it isn't detecting motion.
- The tilt sensor acts like a closed circuit when it is upright. However, it acts like an [open circuit](https://learn.sparkfun.com/tutorials/what-is-a-circuit#short-and-open-circuits) if it is tilted past 15 degrees. This means that we can set up a circuit with two resistors and hook it up to the RedBoard so that when the tilt sensor is upright, the RedBoard pin will read HIGH (or 5V), and, when it is tilted, the RedBoard pin will read LOW (0V or Ground).
- All that is left is to hook up the buzzer, which just needs to go from ground to an output pin from the RedBoard, where the RedBoard can give it power. In this fritzing diagram, it's set up with a resistor, but that isn't needed unless you want the buzzer to be quieter. The bigger the resister you put in series with the buzzer, the less noise the buzzer will make.

[\[1\]](https://learn.sparkfun.com/tutorials/redboard-santa-trap#min_voltage) **Note:** The PIR motion sensor can work with at least 5V. However, the voltage may not be enough for the L78L05 voltage regulator to work reliably depending on your power supply. For more information, check out the note in the [PIR Motion Sensor Hookup Guide](https://learn.sparkfun.com/tutorials/pir-motion-sensor-hookup-guide#min_voltage).

## Code

With some programing to the RedBoard, which can be programmed with Arduino IDE, we can program the buzzer to play a song when motion or the cup tilting is detected. Upload the following code to your RedBoard.

    language:c
    int pirPin = 2; // alarm pin from motion sensor
    int tilPin = 7; // alarm pin from tilt sensor
    const int buzzerPin = 9; // output pin for buzzer

    const int songLength = 18; // number of notes in the buzzer song
    char notes[] = "e e e e e e egcde "; // notes and rests of the buzzer song
    int beats[] = ; // length of each note and rest in the buzzer song
    int tempo = 150; // speed of the buzzer song

    int motionCheck[] = ; // storing the last 6 alarms from the motion sensor
    int j = 0; // counter
    int tiltCheck[] = ; // storing the last 6 alarms from the tilt sensor
    int t = 0; // counter

    void setup()

    void loop()
      for (t=0; t < 6; t++)
      

      int i = 0; // counter for the buzzer song
      int duration; // value for the duration of the buzzer song

      // This if test is asking if motion or tilt has been sensed by
      // checking that the last 6 tests came back sensing motion or tilt.
      if(((motionCheck[0] == 0) && (motionCheck[1] == 0) && (motionCheck[2] == 0) && (motionCheck[3] == 0) && (motionCheck[4] == 0) && (motionCheck[5] == 0)) or ((tiltCheck[0] == 0) && (tiltCheck[1] == 0) && (tiltCheck[2] == 0) && (tiltCheck[3] == 0) && (tiltCheck[4] == 0) && (tiltCheck[5] == 0)))
            else // otherwise, play the note                       
            
            delay(tempo/10);     // brief pause between notes   
          }
        }
        delay(1000);   //wait a second before starting all the checks over again
    }

    int frequency(char note) 
    ;
      int frequencies[] = ;
      /*
      note  frequency
      c     262 Hz
      d     294 Hz
      e     330 Hz
      f     349 Hz
      g     392 Hz
      a     440 Hz
      b     494 Hz
      C     523 Hz
      */

      // Now we'll search through the letters in the array, and if
      // we find it, we'll return the frequency for that note.

      for (i = 0; i < numNotes; i++)  // Step through the notes
      
      }
      return(0);  // We looked through everything and didn't find it,
                  // but we still need to return a value, so return 0.
    }

With this you should have everything you need to put it all together. Once you have everything hooked up and you upload the included code you should be ready for Santa!