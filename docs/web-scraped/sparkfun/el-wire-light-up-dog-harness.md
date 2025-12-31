# Source: https://learn.sparkfun.com/tutorials/el-wire-light-up-dog-harness

## Introduction

Whether it\'s to keep Fido (or in my case, Marley) visible on an adventure or as an awesome all-year-round costume, a light up dog harness is an excellent accessory for your favorite pup.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/LightUpDogHarness_FinalTest.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/LightUpDogHarness_FinalTest.JPG)

[EL wire](https://www.sparkfun.com/search/results?term=el+wire) is a great option for wearable lights. It stays cool, is flexible, and comes in lots of different colors. This design uses the [SparkFun EL Sequencer](https://www.sparkfun.com/products/11323) to automatically turn on EL wire when it is sufficiently dark outside, so you don\'t have to worry about locating Mr. Dog to turn the on system.

### Materials

Here is a list of all the parts and tools used in making this project.

#### Electronics

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/Materials_Electronics.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/Materials_Electronics.JPG)

- [EL Wire](https://www.sparkfun.com/search/results?term=el+wire&_ga=1.61978479.273388466.1418147030)
  - El Wire comes in a variety of colors, pick your favorite!
- [EL Sequencer](https://www.sparkfun.com/products/11323)
- [Lithium Ion Battery](https://www.sparkfun.com/products/8483)
- [5V FTDI BOB](https://www.sparkfun.com/products/9716) (or cable)
- [DC to AC Inverter - 3V](https://www.sparkfun.com/products/10201)
- [Ambient Light Sensor](https://www.sparkfun.com/products/8688)
- [Stackable Header pins](https://www.sparkfun.com/products/553) (8 total: 5 for FTDI BOB and 3 for light sensor)
- Three (3) [Male-to-Female Breadboard Wires](https://www.sparkfun.com/products/9385)
- Note: Purchase **three (3) JST connectors** for the EL wire, battery, and inverter if these components do not already have connectors.

#### Harness Materials

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/Materials_DogHarness.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/Materials_DogHarness.JPG)

- Dog harness
  - A vest or backpack will also work
- Waterproof jacket w/ pocket(s)
- Optional: Tupperware or other sealable plastic container

### Tools

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/Tools.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/Tools.JPG)

- Safety goggles
- Soldering Iron
- Wire Cutter/Stripper
- Epoxy (waterproof)
- Scissors
- Needle + thread OR fabric adhesive
- Optional: Velcro

### Recommended Reading

If you are new to electronics, EL wire, or the EL Sequencer, or would like more information on the main components in this project, check out this tutorial:

- [Getting started with the EL Sequencer](https://www.sparkfun.com/tutorials/353)

As this design also uses a lithium ion battery, I also recommend reading [this tutorial](https://www.sparkfun.com/tutorials/241) to give you an overview on proper care and handling of lithium batteries.

## Assembly

**CAUTION:** Although it is low current, EL wire runs on high voltage AC (100 VAC). There are exposed connections on the EL Sequencer board so BE CAREFUL when handling the board. Always double (and triple) check that the power switch is OFF before touching any part of the board. For final projects, it is recommended to coat all exposed connections in epoxy, hot glue, electrical tape, or other insulating material.

1.  Test the EL Sequencer with EL wire. Connect EL Wire, inverter, and battery to EL sequencer. Turn on power switch and check that the EL wire turns on (should be blinking). You can connect, and control, up to 8 different strands of EL wire.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/ELSeqTest.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/ELSeqTest.JPG)

2.  Solder header pins onto 5V FTDI pinholes on the EL Sequencer.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/ELSeq_HeaderPins1.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/ELSeq_HeaderPins1.JPG)

3.  Solder header pins to the \"GND,\" \"VCC,\" and \"A2\" pinholes EL Sequencer (right side).

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/ELSeq_LightSensorPins.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/ELSeq_LightSensorPins.JPG)

4.  Solder male end of breadboard wires to ambient light sensor. Coat exposed metal on the sensor in epoxy (do not coat actual sensor).

    Note: Recommended to solder the pins on the bottom of the sensor so that the sensor can more easily be attached to the harness (found this out the hard way..).

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/LightSensor_Wires.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/LightSensor_Wires.JPG)

5.  Attach EL wire to harness.

    ::: 
    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/ELWire_Start.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/ELWire_Start.JPG)
    :::

    Sew EL wire onto harness with dental floss for a strong, durable bond. Can also use an appropriate fabric adhesive.

    ::: 
    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/ELWire_StrapsBuckles.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/ELWire_StrapsBuckles.JPG)
    :::

    ::: 
    *For straps/buckles: leave about 1\" of unadhered EL wire on either side of the strap/buckle.*
    :::

    You can either wrap the ELwire for its entire length, or cut it and insulate the ends.

    ::: 
    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/ELWire_Wrapped.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/ELWire_Wrapped.JPG)
    :::

6.  Make a durable pouch for the electronics.

    For a waterproof pouch, cut out a pocket in a waterproof jacket. I also included a small tuperware container to house the electronics in the pouch to further insulate and protect them from weather and dog conditions.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/Materials_HarnessPouch.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/Materials_HarnessPouch.JPG)

7.  Attach electronics pouch to harness.

    Sew pouch onto top side of harness, or wherever is comfortable and practical for your pup. Recommended to put harness on dog to find a suitable location for the pouch.

    ::: 
    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/HarnessPouchFront.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/HarnessPouchFront.JPG)
    :::

8.  Cut small holes on underside of pouch for the EL wire JST connector and the light sensor wires.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/HarnessPouchBack_WireSlit.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/HarnessPouchBack_WireSlit.JPG)

9.  Attach and secure light sensor to harness. Recommended to put harness on pooch and mark location for light sensor so that it faces upward.

    There was an ideal flap in the rainjacket pocket for me to cut a hole, push the sensor through, and epoxy the other side. You can also use velcro or sew the light sensor onto the pocket or harness, just be sure that it stays stationary and won\'t get covered when the dog is moving.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/HarnessPouch_LightSensor.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/HarnessPouch_LightSensor.JPG)

10. If using tuperware, cut or drill holes in tuperware for EL wire JST connector and light sensor wires.

    If you are not using tuperware, it is recommended to cushion the electronics and/or epoxy all connections (except the JST connectors) to protect them from your dog\'s antics.

    ::: 
    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/HarnessPouch_Tupperware_Connected.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/HarnessPouch_Tupperware_Connected.JPG)
    :::

11. Connect EL wire and light sensor to EL Sequencer (through holes in the tuperware), then epoxy the holes to keep wires in place and maintain a waterproof seal.

    ::: 
    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/HarnessPouch_Complete.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/HarnessPouch_Complete.JPG)
    :::

## Programming

Now it\'s time to program the electronics.

Connect EL Sequencer to computer via 5V FTDI BOB or cable.

Program the EL Sequencer using the Arduino platform; the EL Sequencer runs an ATmega 328p at 8 MHz and 3.3V.

Write a program to read in the analog value of the ambient light sensor, turn on the appropriate EL wire channels at a value that corresponds to low light, and turn off once the light sensor value is above the low light threshold.

Below is a sample Arduino sketch with a preset light threshold:

    language:c
    // EL Wire Dog Harness Program
    // Turn EL wire on when ambient light is low.
    // JenFoxBot
    // Based on test sketch by Mike Grusin, SparkFun Electronics

    void setup() 

    void loop() 
    

        Serial.println(analogRead(A2)); // Use this to check value of ambient light 

        digitalWrite(10, status);   // blink both status LEDs
        digitalWrite(13, status);
      }
    }

Check that the EL wire turns on when the ambient light is low and turns off in bright light.

## The Final Product

Place EL Sequencer, inverter, and battery inside the pouch (and tupperware). Connect all components to the EL Sequencer and turn it on using battery power. Test it in low and bright light to ensure that it functions properly.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/LightUpDogHarness_FinalTest.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/LightUpDogHarness_FinalTest.JPG)

If system works as expected, put on dog and go exploring! As an added bonus, you can use the electronics pouch to store other small, non-magnetic items. Enjoy!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/LightUpDogVestV4.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/LightUpDogVestV4.JPG)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/LightUpDogVest_FinalV2.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/LightUpDogVest_FinalV2.JPG)

And here\'s a video of it in action.