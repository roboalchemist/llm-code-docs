# Source: https://learn.sparkfun.com/tutorials/vox-imperium-stormtrooper-voice-changer

## Introduction

The Empire\'s finest have a distinct nasal and mechanical voice when talking through their intercoms. As you work diligently on that Stormtrooper costume and apply for the [501st](http://www.501st.com/), you can up your armor game by including a voice changer.

[![Stormtrooper helmet](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/Stormtrooper_Helmet_scaled.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/Stormtrooper_Helmet_scaled.png)

There are [pre-built solutions](http://www.501st-creations.co.uk/store2.htm) available for budding Stormtrooper cadets, but most are bulky and sometimes require wiring outside the helmet. However, with a little bit of coding and wiring, you can build your own inside a helmet using SparkFun parts.

### Required Materials

In this tutorial, we\'ll build the voice changer on a breadboard for testing. Each helmet will be different, so the wiring will have to be adjusted. The parts list below details what you\'ll need for the breadboard prototype.

**Update:** The [MEMS Microphone](https://www.sparkfun.com/products/9868) works way better than the Electret Microphone for removing audio feedback in the system.

Note that from the resistor kit you\'ll need:

- 1x 2.2kΩ
- 1x 4.7kΩ

### Suggested Reading

We suggest you be familiar with the following before embarking upon this tutorial:

- [Soldering Basics](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering)
- [Programming the Teensy](https://learn.sparkfun.com/tutorials/getting-started-with-the-teensy)

## Hardware Hookup

### Prep Connectors

**Note:** This part is optional if you do not plan to connect things to a breadboard. Skip to the Fritzing section to see how to wire things up if you plan to put the components directly into a helmet without headers.

To start, solder headers onto the Teensy and Prop Shield. You\'ll also want to solder female headers to the edge pins on the Teensy, the edge pins on the Prop Shield, and the Prop Shield\'s audio out port.

[![Headers on Teensy and Prop Shield](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/vox_imperium_04.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/vox_imperium_04.png)

Cut and strip six lengths of wire, each about 6 inches long. Solder them to the speakers (note that you\'ll need to splice two wires to one for each positive and negative terminal).

[![Wires on the speakers](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/vox_imperium_05.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/vox_imperium_05.png)

### Fritzing Wire Diagram

Connect the components as shown in the breadboard. Follow the wires if you plan to put this into a helmet.

**Note:** You can also stack the Teensy on top of the Prop Shield and solder header pins between them. The wiring diagram is meant to show which connections are needed if you plan to wire them separately.

[![Vox Imperium Fritzing wiring diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/8/Vox_Imperium_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/Vox_Imperium_bb.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

## Audio System Design

One of the coolest tools for developing on the Teensy is the [PJRC Audio System Design Tool](http://www.pjrc.com/teensy/gui). With it, you can drag and drop blocks that correspond to various components on the Teensy, like the ADC and DAC, in addition to useful functions like filters. After connecting them with \"patch cords,\" you can export the whole thing as Arduino code. Pretty sweet.

Feel free to try it out and replicate the block diagram.

**Note:** You don\'t actually have to recreate the block diagram; the code in The Code section already has the necessary audio pieces built in.

[![Vox Imperium Audio System Design Tool](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/8/Audio_System_Design_Tool.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/Audio_System_Design_Tool.png)

Doing a basic microphone-to-speaker pass through requires simply connecting the ADC to the DAC. To add features, we\'ll need to put blocks in between those two.

Stormtrooper voices are marked by a nasal sound that can easily be accomplished by turning the treble way up and turning the bass way down. To accomplish this in the Design Tool, we\'ll use a [state variable filter](https://en.wikipedia.org/wiki/State_variable_filter) with a corner frequency set to 2000 Hz. Frequencies below that are considered \"bass\" (for a voice), and frequencies above that are \"treble.\" By separating the low and high frequencies, we can put them back into a mixer and play with the individual gain. In the code, we\'ll set the treble gain to 0.25 (so as not to blow out the amplifier) and bass to 0.01 (we want it pretty much gone). You can play with any of the `GAIN` parameters in the code to adjust the volume and treble/bass mix.

You\'ll also notice that we added a [biquad filter](https://en.wikipedia.org/wiki/Digital_biquad_filter) right after the ADC. We ultimately want to use this as a low-pass filter to reduce feedback we might get between the microphone and speakers. However, if we enable it in the code, it reduces the quality of the sound, as we effectively filter out most of the voice frequencies we want. Feel free to play with the `FEEDBACK_SUPPRESSION` and `LOWPASS_CUTOFF` parameters in the code to try setting the low-pass filter to an acceptable frequency.

The *peak* is an analysis block that gives us a measure of the amplitude of the audio signal. We use this to determine when someone is talking into the microphone. Play with the `SQUELCH_CUTOFF` parameter to adjust the volume where the Teensy begins playing sound through the speakers.

*playFlashRaw* allows us to play a raw audio file that has been loaded into the Prop Shield\'s serial flash memory. We\'ll upload the \"click\" and \"static burst\" sounds and play them whenever a user starts or finishes talking. Change the `BEGIN_CLICK` parameter to choose whether to play the click sound at the start, and change `END_SOUND` to choose whether to play a randomly chosen click or static burst at the end of talking.

Click the **export** button to get the necessary Arduino code. You can just copy it into a sketch!

If you want to try the other blocks, feel free to drag them in and connect some patch cables. To really get some distorted sound, I recommend the [Bitcrusher](http://www.pjrc.com/teensy/gui/?info=AudioEffectBitcrusher) (details for each audio block can be found on the righthand side of the Audio System Design Tool).

## Sound Clips

To play the quintessential Stormtrooper \"click\" and \"static burst\" sounds, we need to rip them from a sound clip, convert them to a raw format and load them into the Prop Shield\'s serial flash memory.

### Convert Sound Clips to Raw

**Note:** You can skip this section if you choose. The raw sound clips can be found in the [GitHub repository](https://github.com/sparkfun/Vox_Imperium).

Find a Stormtrooper sound clip, like [this one](http://admin.soundboard.com/sb/sound/367028). Download it and open it with an editing program, like [Audacity](http://www.audacityteam.org/).

Make sure the project is set to **44.1kHz**, highlight the portion of the clip you want (we\'ll highlight the \"click\" noise) and crop it (*Trim Audio* in Audacity).

[![Audio editing in Audacity](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/8/Audacity_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/Audacity_1.png)

Export the clip (**File \> Export Audio\...**), name the new file *click.raw* and adjust the file options to:

- Save as type: Other uncompressed files
- Header: RAW (header-less)
- Encoding: Signed 16-bit PCM

[![Export raw audio file from audacity](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/Audacity_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/Audacity_2.png)

Repeat this process for the static burst sound, which we named *break.raw*.

### Upload Sound Clips to Prop Shield

Before you begin this part, make sure you have [Teensyduino](http://www.pjrc.com/teensy/td_download.html) installed in the Arduino development environment. This tutorial was tested using [Arduino 1.6.9](https://www.arduino.cc/en/Main/OldSoftwareReleases#previous).

Now that we have the raw sound clips, we need to upload them to the Teensy. To do that, we\'ll use the TeensyTransfer Tool.

Download the [TeensyTransfer repository](https://github.com/FrankBoesing/TeensyTransfer) as a ZIP file. Open a new Arduino sketch and select **Sketch \> Include Library \> Add .ZIP Library**. Find and select the **TeensyTransfer-master.zip** file. This will install the TeensyTransfer library.

Open **File \> Examples \> TeensyTransfer-master \> teensytransfertool**.

In **Tools**, select:

- Board: Teensy 3.2 / 3.1
- USB Type: Raw HID
- CPU Speed: 96 MHz optimized (overclock)
- Port: \\\<Your Teensy\'s Port\>

[![Uploading teensytransfertool](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/vox_imperium_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/vox_imperium_01.png)

Upload the sketch to the Teensy. Find the downloaded **TeensyTransfer-master.zip** file and unzip it. Go to *TeensyTransfer-master/extras* and unzip the pre-compiled teensytransfer program for your operating system:

- teensytransfer.gz for Linux
- teensytransfer.mac.zip for OS X
- teensytransfer.zip for Windows

Open a command prompt, navigate to the *TeensyTransfer-master/extras/teensytransfer* directory and run the program to upload the raw audio clips to the Prop Shield\'s flash memory:

    cd <Downloads directory>TeensyTransfer-master/extras/teensytransfer
    teensytransfer -w <GitHub directory>/Vox_Imperium/sfx/click.raw
    teensytransfer -w <GitHub directory>/Vox_Imperium/sfx/break.raw

You can check if the transfer worked by entering `teensytransfer -l`, and the tool should output the files found on the serial flash memory.

[![Using the TeensyTransfer tool to upload sound clips to the Teensy Prop Shield](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/vox_imperium_02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/vox_imperium_02.png)

## The Code

Create a new Arduino sketch and copy in the code:

    language:c
    #include <Audio.h>
    #include <Wire.h>
    #include <SPI.h>
    #include <SD.h>
    #include <SerialFlash.h>

    // GUItool: begin automatically generated code
    AudioInputAnalog         adc1;           //xy=255,182
    AudioFilterBiquad        biquad1;        //xy=394,182
    AudioPlaySerialflashRaw  playFlashRaw1;  //xy=535,319
    AudioFilterStateVariable filter1;        //xy=558,189
    AudioAnalyzePeak         peak1;          //xy=559,255
    AudioMixer4              mixer1;         //xy=710,196
    AudioOutputAnalog        dac1;           //xy=844,196
    AudioConnection          patchCord1(adc1, biquad1);
    AudioConnection          patchCord2(biquad1, 0, filter1, 0);
    AudioConnection          patchCord3(biquad1, peak1);
    AudioConnection          patchCord4(playFlashRaw1, 0, mixer1, 2);
    AudioConnection          patchCord5(filter1, 0, mixer1, 0);
    AudioConnection          patchCord6(filter1, 2, mixer1, 1);
    AudioConnection          patchCord7(mixer1, dac1);
    // GUItool: end automatically generated code

    // Parameters
    const bool DEBUG = false;
    const bool BEGIN_CLICK = true;  // Play click on voice start
    const bool END_SOUND = true;    // Play click/burst on voice end
    const bool FEEDBACK_SUPPRESSION = false;  // Enables input filter
    const unsigned int LOWPASS_CUTOFF = 2200; // Hz
    const unsigned int CROSSOVER_FREQ = 2000; // Filter center freq
    const float BASS_GAIN_ON = 0.01;
    const float BASS_GAIN_OFF = 0.0;
    const float TREBLE_GAIN_ON = 0.25;    // Voice output volume
    const float TREBLE_GAIN_OFF = 0.0;
    const float SFX_GAIN = 0.5;           // Sound clip volume
    const float SQUELCH_CUTOFF = 0.10;    // Voice threshold
    const int HYSTERESIS_TIME_ON = 20;    // Milliseconds
    const int HYSTERESIS_TIME_OFF = 400;  // Milliseconds

    // Pins
    const int FLASH_CS = 6;               // Serial flash chip select
    const int AMP_ENABLE = 5;             // Amplifier enable pin

    // On/Off state machine states
    typedef enum volState  VolState;

    // Global variables
    elapsedMillis fps; // Sample peak only if we have available cycles
    VolState state = QUIET;
    unsigned long timer;

    void setup() 

      // Initialize amplifier
      AudioMemory(20);
      dac1.analogReference(EXTERNAL); // much louder!
      delay(50);                      // time for DAC voltage stable
      pinMode(AMP_ENABLE, OUTPUT);

      // wait up to 10 seconds for Arduino Serial Monitor
      unsigned long startMillis = millis();
      if ( DEBUG ) 

      // Butterworth lowpass filter (reduces audio feedback)
      if ( FEEDBACK_SUPPRESSION )  else 

      // Configure the State Variable filter
      filter1.frequency(CROSSOVER_FREQ);
      filter1.resonance(0.707);

      // Adjust gain into the mixer
      mixer1.gain(0, BASS_GAIN_OFF);
      mixer1.gain(1, TREBLE_GAIN_OFF);
      mixer1.gain(2, SFX_GAIN);

      // Initialize serial flash
      if ( !SerialFlash.begin(FLASH_CS) ) 
      }

      // Use the time since boot as a seed (I know, not great, but
      // the audio toolbox took away my analogRead)
      int seed = micros() % 32767;
      if ( DEBUG ) 
      randomSeed(seed);

      if ( DEBUG ) 
    }

    void loop() 
            break;

          // If sound continues, play sound effect
          case QUIET_TO_LOUD:
            if ( peak1.read() <= SQUELCH_CUTOFF )  else 

                // Turn on amp, play sound, turn on mic
                digitalWrite(AMP_ENABLE, HIGH);
                if ( BEGIN_CLICK ) 
                mixer1.gain(0, BASS_GAIN_ON);
                mixer1.gain(1, TREBLE_GAIN_ON);

                // Go to next state
                state = LOUD;
              }
            }
            break;

          // Filter mic input and play it through speakers
          case LOUD:
            if ( peak1.read() <= SQUELCH_CUTOFF ) 
            break;

          // If no sound for a time, play click or burst
          case LOUD_TO_QUIET:
            if ( peak1.read() > SQUELCH_CUTOFF )  else 

                // Play a random sound
                if ( END_SOUND )  else 
                }

                // Turn off mic and amp
                digitalWrite(AMP_ENABLE, LOW);
                mixer1.gain(0, BASS_GAIN_OFF);
                mixer1.gain(1, TREBLE_GAIN_OFF);
                state = QUIET;
              }
            }
            break;

          // You really shouldn't get here
          default:
            break;
        }
      }
    }

    // Play a sound clip from serial flash
    void playFile( const char* filename ) 

      // Start playing the file
      playFlashRaw1.play(filename);

      // A brief delay for the library read info
      delay(5);

      // Wait for the file to finish playing
      while ( playFlashRaw1.isPlaying() );

      if ( DEBUG ) 
    }

Make sure the board has the following settings:

- Board: Teensy 3.2 / 3.1
- USB Type: Serial
- CPU Speed: 96 MHz optimized (overclock)
- Port: \\

[![Upload the Vox Imperium to the Teensy](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/vox_imperium_03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/vox_imperium_03.png)

Upload the sketch to the Teensy, and you\'re ready to join the Imperial Army!

### Run It!

Whenever you speak into the microphone, you\'ll hear a click followed by a nasal version of your voice. When you stop talking, the Teensy will play a click or a static burst. You can disable the initial click by changing `BEGIN_CLICK` to `false`, and you can disable the ending sound by changing `END_SOUND` to `false`.

You can also plug a [LiPo battery](https://www.sparkfun.com/products/341) into the [Power Cell](https://www.sparkfun.com/products/11231) to power the whole contraption.

[![Powering the Vox Imperium off a battery](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/vox_imperium_06.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/8/vox_imperium_06.png)