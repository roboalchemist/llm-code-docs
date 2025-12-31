# Source: https://learn.sparkfun.com/tutorials/sound-reactive-el-wire-costume

## Introduction 

Bring science fiction to life with a personalized light-up outfit! [EL wire](https://www.sparkfun.com/search/results?term=el+wire) is a delightfully futuristic-looking luminescent wire that has the added benefit of staying cool, making it ideal for wearable projects. Combining sensors and a microcontroller with EL wire allow for a wide range of feedback and control options.

This project uses the [SparkFun Sound Detector](https://www.sparkfun.com/products/12642) and the [EL Sequencer](https://www.sparkfun.com/products/11323) to flash the EL wire to the rhythm of ambient sound, including music, clapping, and talking. You could accomplish the same with the [EL Escudo DOS Arduino Shield](https://www.sparkfun.com/products/10878).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/FinalCostume_Demo_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/FinalCostume_Demo_copy.JPG)

For a video breakdown of the costume, check out the video below.

### Materials

#### Electronics

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/Materials_Electronics_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/Materials_Electronics_copy.JPG)

- [EL Wire](https://www.sparkfun.com/search/results?term=el+wire)
  - El Wire comes in a variety of colors, so pick your favorite(s)!
- [EL Sequencer](https://www.sparkfun.com/products/11323)
- [Lithium Ion Battery](https://www.sparkfun.com/products/8483)
- [5V FTDI Breakout](https://www.sparkfun.com/products/9716) (or cable)
- [DC to AC Inverter - 3V](https://www.sparkfun.com/products/10201)
- [Sound Detector](https://www.sparkfun.com/products/12642)
- [Stackable Header pins](https://www.sparkfun.com/products/553) (15 total: 5 for FTDI BOB, 5 for EL Sequencer, and 5 for sound detector)
- [Five (5) Female-to-Female Breadboard Wires](https://www.sparkfun.com/products/10898) (or regular wire is fine, too)
- Note: Purchase [**three (3) JST connectors**](https://www.sparkfun.com/products/8670) for the EL wire, battery, and inverter if these components do not already have connectors.

#### Costume

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/WearableLights_OutfitMaterials_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/WearableLights_OutfitMaterials_copy.JPG)

- Article(s) of clothing
  - For a Tron-esque look, go for stretchy black material. Yoga pants and other athletic gear works great!
- Belt
- Old jacket with large pocket, preferably zippered or otherwise sealable.
  - The pocket will house the electronics. If you intend to wear the costume outdoors in potentially wet weather, choose a pocket that is waterproof (i.e. cut a pocket from a waterproof jacket).
- Piece of packing foam or styrofoam (to insulate the sound detector)

### Tools

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/Tools_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/Tools_copy.JPG)

- Safety goggles
- Soldering Iron
- Wire Cutter/Stripper
- Epoxy (waterproof)
- Scissors
- Needle + thread OR fabric adhesive

### Recommended Reading

- New to EL wire and/or the EL Sequencer? [Check out this tutorial on how to set up the EL Sequencer.](https://learn.sparkfun.com/tutorials/el-sequencerescudo-dos-hookup-guide)
- For a thorough overview of the sound detector used in this project, [here\'s a great tutorial.](https://learn.sparkfun.com/tutorials/sound-detector-hookup-guide)
- Lastly, this project uses a high capacity lithium ion battery (\"LIB\"). It is very important to handle these batteries safely. [Here\'s a tutorial on proper care and handling for LIBs.](https://www.sparkfun.com/tutorials/241)

## Build It!

**CAUTION:** Although it is low current, EL wire runs on high voltage AC (100 VAC). There are exposed connections on the EL Sequencer board so BE CAREFUL when handling the board. Always double (and triple) check that the power switch is OFF before touching any part of the board. For final projects, it is recommended to coat all exposed connections in epoxy, hot glue, electrical tape, or other insulating material.

1.  Test EL Sequencer with EL Wire.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/ELSeqTest_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/ELSeqTest_copy.JPG)

    Connect the inverter, battery, and at least one strand of EL wire to the EL Sequencer. (Note that the two black wires of the inverter correspond to the AC side.)

    Be sure that the EL Wire lights up and blinks when you power the EL Sequencer on battery mode.

2.  Solder header pins onto **5V FTDI pinholes** on the EL Sequencer and onto the **VCC, Ground, and A2 input pins**.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/ELSeq_HeaderPins1_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/ELSeq_HeaderPins1_copy.JPG)

3.  Solder header pins to the sound detector.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/SoundDetector_HeaderPins_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/SoundDetector_HeaderPins_copy.JPG)

4.  Connect sound detector to EL Sequencer via female-to-female jumper wires (you can also skip the header installation, and solder wire directly to the header pins).

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/SoundDetector_HeaderPins_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/SoundDetector_HeaderPins_copy.JPG)

    Connect the sound detector VCC and Ground pins to the VCC and Ground pins on the EL Sequencer. Connect the sound detector **Gate output** to the **A2 input** pin on the EL Sequencer. If you are using the envelope and/or audio output signals, connect these to pins A3 and A4 on the EL Sequencer (more on this in the Program It! section below).

5.  Make a protective casing for the sound detector using packing foam or styrofoam to prevent jostling or other physical vibrations (aka collisions) from triggering it.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/SD_CaseOutline_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/SD_CaseOutline_copy.JPG)

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/SD_CaseCloseUp4_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/SD_CaseCloseUp4_copy.JPG)

    Place sound detector on top of foam, outline the board with a pen, and cut out a hole in the foam for the detector to fit snugly inside. It is also recommended that you epoxy the wires onto the foam (but not the sound detector board).

6.  Cut out a pocket from the jacket, and sew onto the belt.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/BeltPocket_Full_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/BeltPocket_Full_copy.JPG)

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/BeltPocket_Attaching_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/BeltPocket_Attaching_copy.JPG)

7.  Put belt on, connect EL Wire to EL Sequencer, and place EL Sequencer in pocket pouch. Determine approximate placement of each EL wire strand based on location of electronics.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/Pocket_CloseUp_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/Pocket_CloseUp_copy.JPG)

8.  Mark and/or adhere the base of the EL wire JST connector onto clothing, allowing the full length of the connector to flex. Be sure that the JST connector can easily reach the EL Sequencer.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/ELWire_JST_SafetyPin_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/ELWire_JST_SafetyPin_copy.JPG)

9.  Starting at the base of the JST connector, attach EL wire strands to your chosen article of clothing.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/ELWire_JST_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/ELWire_JST_copy.JPG)

    Sew EL wire onto clothing using strong thread or dental floss, or use an appropriate fabric adhesive.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/ELWire_Attached_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/ELWire_Attached_copy.JPG)

    Prior to adhering the EL wire, it is recommended to use safety pins to determine placement of the EL wire on each article of clothing while you are wearing it. EL wire is flexible but not so stretchy, so give yourself some wiggle room.

    It is also recommended to use separate EL wire strands on different articles of clothing to facilitate the process of taking it on/off.

## Program It!

1.  Connect EL Sequencer to computer via 5V FTDI Breakout Board or cable.

2.  Program the EL Sequencer using the Arduino platform; the EL Sequencer runs an ATmega328p at 8 MHz and 3.3V.

3.  Determine how you want to use the sound detector output(s) to control the EL wire. The sample program below utilizes the gate channel output to turn on the EL wire if there is a sound detected.

For a simple example sketch, you can copy the code below or you can visit the following [link](https://raw.githubusercontent.com/jenfoxbot/WearableSoundActivatedLights/master/build).

    language:c
    // Sound Activated EL Wire Costume
    // Blink EL Wire to music and other ambient sound.
    //JenFoxBot
    void setup() 
    void loop() 
    

        digitalWrite(2, LOW); //turn EL channel off
        digitalWrite(3, LOW);
        digitalWrite(4, LOW);

    }

This program is just one example of what is possible with the SparkFun Sound Detector. Depending on your needs, different responses can be achieved by using the \"envelope\" and \"audio\" outputs of the sound detector. The EL Sequencer can individually control up to 8 different EL wire strands using the three sound detector output signals, so there are tons of possibilities to customize your sound-activated outfit!

### More information about the sound detector output signals:

The gate channel output is a digital signal that is high when a sound is detected and low when it is quiet. The envelope channel output traces the amplitude of the sound, and the audio output is the voltage directly from the microphone. Check out the plot below for the actual output voltage of the sound detector.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/7/waves.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/7/waves.png)

In the photo above, the red trace corresponds to the gate signal output, the light green trace corresponds to the envelope signal output, and the dark green trace corresponds to the audio signal output. More info can be found in the [Sound Detector Hookup Guide](https://learn.sparkfun.com/tutorials/sound-detector-hookup-guide).

## Test, Secure, and Show Off!

1.  Connect all components to the EL Sequencer (inverter, battery, sound detector), and place in belt pouch. Turn the system on, make some noise (e.g. clapping, snapping, or music), and check that the EL wire flashes when there is a sound.

2.  If the outfit works as expected, secure all connections by coating them in a (thin) layer of epoxy. Let dry for at least 24 hours.

    **Epoxy is a very permanent adhesive**, so if you want to reuse any of the components, try other adhesives like hot glue or electrical tape (less secure, but adjustable and removable).

    You can reduce the overall strain on individual connections by ensuring that wires are securely fastened to the belt and/or pouch approximately one inch (1\") from all connections. The goal is to allow the EL wire to flex while keeping electrical connections rigid, as the connections are the most likely point of breakage.

3.  Wear your one-of-a-kind, high-tech outfit and go show it off to the world!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/9/FinalCostume_Dance_copy.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/9/FinalCostume_Dance_copy.JPG)

You can also see the costume in action in the videos below.