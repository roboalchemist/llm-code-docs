# Source: https://learn.sparkfun.com/tutorials/proto-pedal-example-programmable-digital-pedal

## Introduction

Having assembled the Proto Pedal in the [Proto Pedal Assembly Guide](https://learn.sparkfun.com/tutorials/proto-pedal-assembly-and-theory-guide), we'd like to continue by actually building an effect circuit on the board. This time around, we\'ll be putting a Teensy 3.2 and Audio Adapter in the pedal. The Teensy Audio library contains a bunch of building blocks that you can use to create a custom digital signal processing pedal. Rather than a single effect, you can reprogram the Teensy to create new sound effects.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-78.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-78.jpg)

*Reprogrammable digital pedal.*

### Suggested Reading

- If you\'re here, we\'ll assume that you\'re familiar with the [Proto Pedal Assembly and Theory guide](https://learn.sparkfun.com/tutorials/proto-pedal-assembly-and-theory-guide).
- This project also assumes that you\'re familiar with the [Teensy Audio Library](https://www.pjrc.com/teensy/td_libs_Audio.html).
- In parallel with this guide, you might also be interested in some information about [preparing the Proto Pedal chassis](https://learn.sparkfun.com/tutorials/proto-pedal-chassis-hookup-guide).

## Background

The [Teensy 3.2](https://www.sparkfun.com/products/13736) is a small board built upon a powerful microcontroller, the Freescale [Kinetis K20](https://cdn.sparkfun.com/datasheets/Dev/Arduino/Boards/K20P64M72SF1.pdf). It can be overclocked to 96 MHz, and features the Cortex M4 instruction set, which lends itself to signal processing tasks.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/teensy32-13736-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/teensy32-13736-01.jpg)

*Teensy 3.2.*

The Teensy is Arduino compatible, and programmable via a USB connection. If you\'ve used any Arduino-based board, you\'re already partway there.

To help take advantage of the signal processing instruction set, the [Audio Board](https://www.sparkfun.com/products/12767) adds a 16-bit stereo audio ADC and DAC.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/adapter-12767-01_600x600.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/adapter-12767-01_600x600.jpg)

*Teensy Audio Board.*

Best of all, you don\'t need to be a signal processing guru to get started with the audio board. Instead, there\'s a [web based editor](http://www.pjrc.com/teensy/gui/) that lets you start building the signal processing in a drag-and-drop, patchable GUI. To get started, you assemble the desired processing blocks in the GUI, then cut and paste a snippet of code into an Arduino sketch.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/AutoRollerAudioProject.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/AutoRollerAudioProject.png)

*Sample DSP patch.*

We\'re going to assume that the reader is familiar with Teensy and the Audio framework. If you need some additional background, there is a guide to [getting started with Teensy](https://www.pjrc.com/teensy/first_use.html). PJRC have also prepared a [detailed tutorial](http://www.pjrc.com/teensy/td_libs_Audio.html) on the Teensy Audio environment.

### In Pedal Form

What were going to do in this project is pair Teensy Audio with the Proto Pedal, resulting a reprogrammable digital guitar pedal.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-46.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-46.jpg)

*Prototype Teensy-based pedal.*

### Before we begin

This is a complicated circuit! It involves a number of different types of wiring \-- analog, digital, and power circuits are all included. *If you\'re new to building guitar pedals, this might not be the best starting point.*

Second, the noise floor performance of the circuit leaves something to be desired. There\'s a fair amount of digital crust that the authors have been struggling to remove. *If you\'re a master of noise reduction in mixed-signal systems, we\'d love for you to take a closer look!* If you find things we have missed in our haste, please inform us using the [comments link](https://learn.sparkfun.com/tutorials/proto-pedal-example-programmable-digital-pedal/discuss) in the menu to the right, and we can update this guide.

Finally, if you like the idea of this project, but want ready-made hardware, you might see if you can track down the old [Line 6 ToneCore development kit](http://line6.com/tcddk/).

## The Circuit

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/schematic-2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/schematic-2.png)

*Teensy-Pedal Schematic (click to enlarge).*

The most important component is in the middle of the schematic: the Teensy and audio adapter. We\'re using a simplified symbol to represent them, which only shows the connections we\'re using.

### Theory Of Operations

We\'re going to quickly describe what each section of the circuit does.

#### Input Buffer

The first portion of the circuit is the input buffer.

It consists of one stage of an LM358 operational amplifier, configured as a voltage follower. It\'s input is biased to 4.5 VDC with the pair of 1M Ω resistors, and the input signal is coupled to them via the 10 uf cap. The output of the buffer matches the input signal \-- the buffer increases the input impedance, but doesn\'t amplify or attenuate the signal.

It provides a reasonably high impedance of 500K Ω, defined by the parallel 1M resistors. 1M Ω is the highest value resistor in the SparkFun Resistor Kit \-- if you\'ve got higher value resistors (such as 2.2 M Ω), they should provide even better performance.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/input-schem-2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/input-schem-2.png)

*Input buffer circuit.*

The output of the buffer amplifier feeds the divider of R3 and R4, which attenuates the signal by 10K/(10K + 22K), or 10/32, roughly one-third the input value.

Since this amp stage is powered directly from the 9 VDC supply, it has roughly 9 V~peak-to-peak~ overall headroom. Dividing the output by 1/3 constrains it to about 3 Vpp, which more closely matches the input headroom of the Teensy line input that it feeds.

#### Output Amplifier

The output of the Teensy also has about 3 Vpp headroom, which we amplify back to the 9 Vpp range using an amplifier with a gain of 3.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/output-schem.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/output-schem.png)

*Output amplifier circuit.*

The gain of this noninverting stage is determined by the equation `1 + (Rfeedback/Rshunt)`, or 32/10, the reciprocal of the attenuation of the input amplifier. This pair of circuits achieve what\'s known as *unity gain*, the combined result being a multiply by one. What goes in comes back out the same.

#### Voltage Regulator

The Proto Pedal operates in a world of 9 V batteries and wall adapters, while the Teensy can operate from a miximum of 6 VDC. To help bridge the gap, we\'re using a simple LM7805 linear voltage regulator.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/regulator-schem.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/regulator-schem.png)

*Voltage regulator.*

It turns the 9 V into 5 V. The Teensy draws about 60 mA, and the regulator is dropping the voltage by 4 V, so this regulator has to dissipate about 1/4 Watt as heat. It gets a little warmer than room temperature, but doesn\'t get appreciably hot.

The Teensy has further onboard regulators, dropping the 5 V down to 3.3 V.

#### Analog controls

Finally, there are five potentiometers, wired as voltage dividers between Teensy 3.3V and AGND.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/controls-schem.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/controls-schem.png)

*Parametric controls.*

The wipers of these pots are connected to Teensy ADC inputs A1, A2, A3, A6, and A7. These controls can be assigned to effect parameters in firmware, and are not hardwired to specific parameters.

## Materials

To build this pedal, you\'ll need the folliwing materials, in addition to the [Pedal PCB](https://www.sparkfun.com/products/13124?_ga=1.7876018.1048173588.1462206339) and [chassis](https://www.sparkfun.com/products/13967?_ga=1.7876018.1048173588.1462206339).

**Heads up!** The LM358 is scheduled for EOL. We recommend the [AS358](https://www.sparkfun.com/products/15946) as a drop in replacement as the general purpose op-amp. The part is compatible with the 358.

### Tools

You\'ll also need the usual tools to solder things together.

- [Soldering Iron](https://www.sparkfun.com/products/11704)
- [Lead-based](https://www.sparkfun.com/products/9161) or [Lead-free](https://www.sparkfun.com/products/9325) solder
- [Diagonal](https://www.sparkfun.com/products/8794) or [Flush](https://www.sparkfun.com/products/11952) cutters
- [Wire Strippers](https://www.sparkfun.com/products/12630)

Additionally, while it\'s not required, we were using a [Resistor Lead Forming tool](https://www.sparkfun.com/products/13114) to get the resistors bent to precise lengths.

## Assembly Part 1 (power and analog section)

### The Jumping Off Point

To begin, we\'ll assume that you\'ve completed the [basic assembly](https://learn.sparkfun.com/tutorials/proto-pedal-assembly-and-theory-guide#assembly-instructions) of the proto pedal board.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-01.jpg)

*Proto Pedal PCB assembly.*

One detail worth noting is that you can likely omit the 9V battery snap. While it\'s possible to power this pedal from a 9V battery, the Teensy is thirsty for current, and you can expect 6 to 10 hours battery life. An external power supply is highly recommended!

If you\'re using the [Proto Pedal Chassis](http://www/sfe.io/13967), you\'ll need to prepare it by drilling holes for five potentiometers, and holes for programming the Teensy. This is the chassis shown in the [Chassis hookup guide](https://learn.sparkfun.com/tutorials/proto-pedal-chassis-hookup-guide).

With the prerequisites complete, you can start the sequence below. We\'ll build the circuit in four major stages: the voltage regulator, the analog section, the Teensy, and the panel controls. We\'re going to be stepping fairly quickly. Each step lists the required components, so you can prepare them before you commence. Once they have been placed, double-check your solder joints, and compare your work to the photos. Each of the four stages ends with a short test, to test out the results of that stage.

### Grid Notation

In the following steps, we\'re going to use the grid notation seen on a standard solderless breadboard. From left to right, the columns are numbered 1 to 30, and from bottom to top, the rows are assigned letters from A through J. Any hole in the center of the board can be referenced by number-letter coordinate, such as 27L or 7G.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/battleship-marks.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/battleship-marks.png)

*Grid coordinates and power rails.*

We\'ll also be using both of the center rails of the proto area. The upper one will be tied to `VAUX`, the output of the 5V voltage regulator, and the lower one will be tied to ground.

### Power Section

Teeny expects an input voltage in the 3.6 to 6.0 VDC range. We\'ll create a new supply rail for that voltage, using the power section between the input and output jacks, which we\'ll route to the `VAUX` trace at the center of the board.

The area near the top of the board has a 7 x 7 grid of pad-per-hole prototying area, plus rails for VCC and ground across the bottom.

We\'ll start with a LM7805 voltage regulator, and two 10 uf capacitors.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Vreg-legend-47.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Vreg-legend-47.png)

*LM7805 connections.*

To fit the voltage regulator into this area, we\'ll bend the legs as follows.

- The output, leg 3, is bent straight down along the body of the regulator.
- The input, leg 1, extends one grid space beyond the body before being bent down.
- The ground, leg 2, is one grid space longer than leg 1.

This contortion is illustrated in the photo below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-48.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-48.jpg)

*Voltage regulator assembly.\
Note the staggered legs of the regulator.*

There are also two 10 uf capacitors in this area.

  ----------------------------------------------------------------------------------------------------------------
  Capacitor Value      Value Marking   Start Coordinate           End Coordinate   Orientation Notes
  -------------------- --------------- -------------------------- ---------------- -------------------------------
  10 uf electrolytic   10uf/25V        Ground rail\               VCC rail\        \`-\` to ground rail
                                       atfar left                 at far left      

  10 uf electrolytic   10uf/25V        ground rail at far right   VAUX pad\        \`-\` to ground rail\
                                                                  at far right     + lead extends from VAUX\
                                                                                   to regulator output terminal.
  ----------------------------------------------------------------------------------------------------------------

The cap on the `VAUX` rail has a special trick: its positive leg ls run underneath the board, to the output of the voltage regulator, before being soldered in place at both the `VAUX` pad and the regulator pin. After soldering, trim the excess leads of both the cap and regulator.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-49.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-49.jpg)

*Using capacitor leg to bridge from VAUX to regulator pin.*

#### Incremental Test

With the regulator and caps in place, we can test the voltage regulator.

Apply 9V power to the board, connect a TS jack to the input, and measure the `VAUX` pin. It should be in the range of 4.9 to 5.1 VDC.

Before moving on to the next step, be sure to remove power from the unit.

------------------------------------------------------------------------

### Analog Section

With the regulator tested, we can move on to the analog portion of the circuit. We\'ll start by placing a bunch of jumpers, then add resistors and caps, finally the IC.

#### Jumpers

The analog section of the circuit has nineteen jumpers. We used multicolored solid-core 22 gauge wire. For clarity in the photos, we\'re not using any red wire.

  Jumper Number   Color    Start Coordinate   End Coordinate
  --------------- -------- ------------------ --------------------
  1               Black    3J                 Pot1 Left
  2               Blue     4J                 Pot1 Right
  3               Yellow   7J                 Pot2 Middle
  4               Blue     8J                 Pot3 Middle
  5               White    11J                Pot4 Middle
  6               Black    12J                Pot5 Middle
  7               Green    13J                Pot1 Middle
  8               Yellow   23J                VCC
  9               White    26A                Ground
  10              Blue     Input              26I
  11              Green    21A                Out
  12              Black    21D                23D
  13              Yellow   28A                Ground
  14              Blue     30A                Vcc
  15              Bare     2F                 VAUX
  16              Bare     2E                 Ground
  17              Bare     24J                25J
  18              Bare     VAUX               Top Center Rail
  19              Bare     Ground             Bottom Center Rail

With the jumpers in place the board will look like this

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/jumpers-legend-50.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/jumpers-legend-50.png)

*Wire jumper placement\
(Click to enlarge).*

#### R\'s & Cs

Next we\'ll install the passive analog components, the resistors and capacitors.

There are eight resistors. Most are folded to 0.3\" long, with the legs bent right at the ends of the body. One 10K and one 100K are 0.5\" long, as noted in the placement column below.

  Resistor Value   Value Color Code          Start Coordinate   End Coordinate   Placement Notes
  ---------------- ------------------------- ------------------ ---------------- -----------------
  1M Ω             brown-black-green-gold    26J                Upper Ground     
  10K Ω            brown-black-orange-gold   27J                Upper Ground     
  22K Ω            red-red-orange-gold       24H                27H              
  1M Ω             brown-black-green-gold    23G                26G              
  22K Ω            red-red-orange-gold       21C                24C              
  10K Ω            brown-black-orange-gold   24D                29D              0.5\" long
  100K Ω           brown-black-yellow-gold   25C                28C              
  100K Ω           brown-black-yellow-gold   25B                30B              0.5\" long

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/resistors-legend-51-2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/resistors-legend-51-2.png)

*Resistor placement\
(Click to enlarge).*

There are three 10 uf electrolytic capacitors. Take note of the polatiry - the negative leg is marked on the body of the cap with a stripe, which is also visible in the photo below.

  Capacitor Value      Value Marking   Start Coordinate   End Coordinate   Orientation Notes
  -------------------- --------------- ------------------ ---------------- -------------------
  10 uf electrolytic   10uf/25V        Input Coupling                      \`-\` to left
  10 uf electrolytic   10uf/25V        29E                Center ground    \`-\` to top
  10 uf electrolytic   10uf/25V        Output Coupling                     \`-\` to right

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/caps-legend-54.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/caps-legend-54.png)

*Capacitor placement\
(Click to enlarge).*

#### Op-amp

The last component in the analog section is the operational amplifier.

  ------------------------------------------------------------------------------------------
  Component          Marking   Start Coordinate   End Coordinate   Orientation Notes
  ------------------ --------- ------------------ ---------------- -------------------------
  DIP-8 IC Socket\             Row 23             Row 26           Spanning center trough\
  for LM358                                                        Notch facing left

  ------------------------------------------------------------------------------------------

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-52.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-52.jpg)

*IC socket placement\
(Click to enlarge).*

After soldering the socket, insert the LM358, again with the notch facing to the left.

#### Incremental Test

To test this stage, we\'ll install one extra, temporary wire, from 25A to 27I, the red wire shown below. This ties the input amplifier to the output amplifier.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-53_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-53_1.jpg)

*Test jumper from 25A to 27I.*

Apply power to the circuit, then connect the input and output. We used a signal generator and an oscilloscope. If you don\'t have them handy, you can use a guitar and amplifier \-- just be careful to keep the volume low until you\'re certain that the circuit is well behaved.

While applying input signal, press the stomp switch. Aside from the slight click when the switch engages, the output signal should be nearly the same with the pedal active or bypassed.

Again, disconnect power before moving on, and also remove the temporary jumper.

## Assembly Part 2 (Teensy and controls)

### Teensy Section

The next portion of the circuit that we\'ll be building is the Teensy and Audio Adapter. We\'ll start by turning them into a subassembly, then putting it on the pedal PCB.

#### Optional Modification

This step is optional, but has been found to help lower the noise floor of the Audio Adapter. Once the subassembly goes together, it is very hard to get access to the capacitor we\'re going to be modifying here.

As wen mentioned earlier, the Teensy Audio adapter has a rather high noise floor. On the PJRC forums, user [omjanger](https://forum.pjrc.com/threads/35715-Noise-from-sgtl5000) has posted a modification that helps reduce the noise slightly. It involves putting a 1 MΩ resistor in parallel with the 0.15 uf capacitor on the VAG pin of the codec chip. This modification is shown below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-55.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-55.jpg)

*Piggyback resistor.*

If you chose to undertake this modificaton, be warned: it takes an extremely careful touch to get the resistor in place without removing the capacitor entirely, or bridging adjacent components with solder blobs.

#### Prepare the Stack

Since we\'re going to be powereing the Teensy from the regulator on the pedal circuit board, we want to cut the jumper that bridges the USB bus voltage to the Teensy power input. We used a [hobby knife](https://www.sparkfun.com/products/9200) to cut the trace, and a continuity checker to make sure the cut was complete.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/teensy-jumper.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/teensy-jumper.png)

*Cut VUSB jumper.*

Next we want to stack the teensy and audio adapter with header pins.

The first step is to break off two 14-pin sections of snappable header, and solder them to the Teensy, with the longer portion of the pins pointing downwards. Below, we\'re using a [small breadboard](https://www.sparkfun.com/products/12043) to hold the pins straight while we solder.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-56.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-56.jpg)

*Aligning the Teensy pins.*

Then we remove the Teensy from the breadboard, and put the pins through the audio adapter. Double check the alignment before proceeding: the USB port on the Teensy and the headphone plug on the audio board both face the same direction.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-57.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-57.jpg)

*Teensy and Audio board \-- note orientation: USB and headphone jack face same direction..*

The audio board gets soldered to the pins from below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-58.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-58.jpg)

*Solder the pins from beneath.*

While we\'re looking at the bottom of the board, let\'s solder two more wires to the audio adapter. Here, you can see white and blue wires connected to the left line input and the left line output. Each wire is about 4 inches long \-- we\'ll trim them to length later.

  Wire Color   Connection   Length
  ------------ ------------ ----------
  White        Line out L   4 inches
  Blue         Line In L    4 inches

They\'re inserted from the bottom of the board\...

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-59.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-59.jpg)

*Attach wires to the left line input and output.*

\...and soldered to the top of the board.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-60.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-60.jpg)

*Line in and out pigtails.*

Now we put the stack on the proto pedal circuit board.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-62.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Pro.to_Pedal_Tutorial_Images-62.jpg)

*Teensy on main PCB, with stir stick shim.*

The stack is placed with the USB and headphone jacks pointing to the left, where the USB plug will align with the hole in the left side of the chassis. It spans from column 2 to column 15, and the pins were placed in rows C and G. We don\'t want to bottom of the audio adapter to accidentally touch anything on the pedal PCB, as we\'re using a coffee stirrer as a shim while we solder.

You can see the clearance between the stack and the pedal PCB below.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-63.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-63.jpg)

*Note the space between Teensy Audio board and main PCB..*

The last piece of this step is to run the wires from the line connections back to the analog section.

  Wire Color   Source       Destination
  ------------ ------------ -------------
  White        Line Out L   25A
  Blue         Line In L    27I

Before soldering, we ran the wires to their destination, and trimmed some excess, helping avoid clutter.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-64.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-64.jpg)

*Line in & out pigtails connected to analog circuit.*

#### Incremental Test

Testing this step is similar to the previous incremental test. Connect the input, output and power. Then load the [throughput](https://github.com/sparkfun/Proto_Pedal/tree/master/projects/teensy-based/sketches/throughput) sketch. This sketch allows the Teensy to pass audio from line input to line output.

Toggle the stomp switch a few times. The output of the pedal should be the same amplitude when it is engaged or bypassed. You will likely be able to hear the raised noise floor of the Teensy when the pedal is engaged.

### Controls section

The final quadrant of the circuit is the panel controls. Like the previous step, we\'ll build a subassembly, then integrate it with the main circuit board.

To start, mount the five 10K potentiometers in the chassis, and tighten them in place. Notice that we\'ve numbered each pot (1 through 5), and labeled it with it\'s corresponding Teensy ADC input (A12, A7, A6, A3 and A2). The numbers run right-to-left beacuse we\'re looking from the inside of the box.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-67.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-67.jpg)

*Pots in chassis.*

The pots are wired as parallel voltage dividers between the Teensy `AGND` and `3.3V` signals. Since they\'re in parallel, they\'ll be wired as busses.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/pot-legend-65.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/pot-legend-65.png)

*Potentiometer terminals.*

As indicated in the photo above, the left legs of the pots are daisy-chained with black wire, and the right legs are daisy-chained with blue wire. The middle terminal of each pot will get it\'s own color coded wire in a later step.

For the bus that runs from pot to pot, we used short pieces of solid core wire. Each leg in the daisy-chain has a wire to each of it\'s neighbors. We stripped the ends of each wire, then pushed them through the holes in the pot terminal.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-68.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-68.jpg)

*Putting bus wires in place.*

We then flow solder onto that nexus, making sure to avoid cold solder joints.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-69.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-69.jpg)

*Soldering bus wires.*

The black and blue daisy chains are run between pots, and then we add pigtails to run to the main PCB. Because these wires need to be flexible, we selected about 6 inches of stranded hookup wire, and soldered them to the end of the respective daisy chains.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-70.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-70.jpg)

*Bus wires and pigtails.*

With the buses complete, we need to add five more wires to the potentiometer wipers. Again, we\'re using stranded hookup wire, each about 6 inches long.

The following table and photos illustrate the connections.

  Pot connection         Wire Color   Board Destination
  ---------------------- ------------ -------------------
  Clockwise Bus          Blue         Pot1 Right
  Counterclockwise Bus   Black        Pot1 Left
  Wiper 1                Green        Pot1 Middle
  Wiper 2                Yellow       Pot2 Middle
  Wiper 3                Blue         Pot3 Middle
  Wiper 4                White        Pot4 Middle
  Wiper 5                Black        Pot5 Middle

When these wires in place, you should have wires as seen below. Note that we\'ve got two blue and two black wires \-- the wiper signals (to the left of the photo), and the daisy chained buses (to the right of the photo). Be careful to keep them straight when you connect them to the PCB!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-71.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-71.jpg)

*adding color-coded wires for the wipers.*

The black and blue bus wires connect to the left and right pads of the `Pot1` area, respectively. The blue wiper wire connects to the center of pot 3, and the black wiper wire connects to the center of pot 5.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-72.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-72.jpg)

*Pot connections to main board.*

With the controls soldered to the PCB, you should have an overall assembly as depicted below.

Notice that we\'ve also bolted the ground lug from the PCB to the chassis.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-73.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-73.jpg)

*Pedal with the hood up.*

#### Final Incremental Test

The [throughput]() test sketch that we loaded in the last step also serves as an integration test for the panel controls. If you open the serial port, you notice that it periodically prints a set of five values, showing the potentiometer readings. As you turn each pot, the values should change from 0 when set counterclockwise, to 1023 at when fully clockwise.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/throughput-serial-cap.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/throughput-serial-cap.png)

*Notice the five analog read values.*

### Close It Up

When the tests are passing, we\'re done soldering, and we can close the pedal up.

To put the PCB into the chassis, angle it so the TRS jacks go through the oblong holes, then pivot the board so the switch goes through its hole. As it closes, make sure that the control wires aren\'t hanging up on anything, and if you\'ve got a PTH LED, take care to get it through the chassis hole, too.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-74.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-74.jpg)

*Put PCB in chassis.*

Then put the external hardware on to hold the board in place. The switch gets a hex nut, and each TRS jack has a plastic washer and hex nut.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-75.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-75.jpg)

*Secure it with hardware.*

Before you tighten all of the hardware, doublecheck the aliignment of the barrel jack. It should be centered in the panel hole, as shown below. This alignment reduces the chances of the barrel jack shorting to the chassis, or the bottom of the PCB coming into contact with the lid of the enclosure.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-76.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-76.jpg)

*Verify barrel jack alignment.*

Finally, put the back on the box, and put knobs on the pots.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-78.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-78.jpg)

*A complete pedal.*

## Add the Software

It\'s up to your imagination to come up with the effect you want, but here\'s a few you can load right in and try.

They can be found in the [teensy sketches](https://github.com/sparkfun/Proto_Pedal/tree/master/projects/teensy-based/sketches) directory in the Proto Pedal github repository.

### Throughput

We\'ve already used the [throughput](https://github.com/sparkfun/Proto_Pedal/tree/master/projects/teensy-based/sketches/throughput) sketch to test the audio hardware. It simply passes audio straight from the input to the output. Boring, but you can use it to make sure your system is working!

You can also use this as a template when creating new sketches.

### AutoRoller

The [AutoRoller](https://github.com/sparkfun/Proto_Pedal/tree/master/projects/teensy-based/sketches/AutoRoller) has an input filter for tone control, an output low-pass filter for effect, and a modulation source consisting of a sine wave generator with rate dependent on input peak values. The louder you play, the faster the filter sweeps. It creates a dynamically controlled warble, similar to a rotary tone cabinet.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/autoroller.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/autoroller.png)

*AutoRoller block diagram.*

Within the AutoRoller patch, the input hits a tone control, which allows the relative tonal balance to be adjusted. From there, it feeds a peak detector module. The output of the peak detector modulates the frequency of a sine wave, which is used to modulate the lowpass filter. The \'tone\' knob is used to set the nominal characteristics of the output filter, combining cutoff frequency and resonance on a single knob.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/IMG_3339.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/IMG_3339.JPG)

*The completed AutoRoller. The knobs are set to a good starting place for use with an electric guitar*

More information about the AutoRoller can be found in the readme and other files in [the repository](https://github.com/sparkfun/Proto_Pedal/tree/master/projects/teensy-based/sketches/AutoRoller).

### Tape Echo Emulation

Finally, we\'ve got an example of a tape echo emulation.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/delay-block.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/delay-block.png)

It consists of a delay line with highpass and lowpass filters in the feedback loop. It can be used as a subtly colored digital delay, or tweaked into an interactive, regenerative sound effect generator.

You can find the sketch and related files [here](https://github.com/sparkfun/Proto_Pedal/tree/master/projects/teensy-based/sketches/echo).

**Please note:** the README.md file for the echo contains some additional information about compiling the effect. In order to have the maximum amount of RAM available for the delay line, be sure to select a non-optimized build configuration in the *tools-\>cpu speed* menu.