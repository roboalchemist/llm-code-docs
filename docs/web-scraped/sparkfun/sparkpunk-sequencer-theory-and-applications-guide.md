# Source: https://learn.sparkfun.com/tutorials/sparkpunk-sequencer-theory-and-applications-guide

## Introduction

The [SparkPunk Sequencer](https://www.sparkfun.com/products/12707) is a musical control voltage sequencer designed to control the [SparkPunk Sound Generator](https://www.sparkfun.com/products/11177).

[![SparkFun SparkPunk Sound Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/6/6/9/0/11177-04.jpg)](https://www.sparkfun.com/sparkfun-sparkpunk-sound-kit.html)

### [SparkFun SparkPunk Sound Kit](https://www.sparkfun.com/sparkfun-sparkpunk-sound-kit.html) 

[ KIT-11177 ]

The SparkFun SparkPunk Kit is a sound generator made in the spirit of the Atari Punk Console. Rather than simply recreating t...

**Retired**

[![SparkFun SparkPunk Sequencer Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/9/4/4/9/12707-02.jpg)](https://www.sparkfun.com/sparkfun-sparkpunk-sequencer-kit.html)

### [SparkFun SparkPunk Sequencer Kit](https://www.sparkfun.com/sparkfun-sparkpunk-sequencer-kit.html) 

[ KIT-12707 ]

The SparkFun SparkPunk Sequencer is a musical control voltage sequencer designed to control the SparkPunk Sound Kit. With the...

**Retired**

With the pair, you can create ten-step musical motifs, but there are hidden opportunities in the sequencer: it can be modified and connected to external hardware in clever and interesting ways.

[![SparkPunk and Sequencer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/product-paired-angle.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/product-paired-angle.jpg)

We will start by explaining the internals of the sequencer in more detail. We\'ll step through the major functional blocks of the schematic, learn how they interrelate, and examine the important signals that connect those blocks. Then we\'ll step into some simple modifications that change the behavior of the sequencer. From there, we\'ll look at how we can add more hardware to make increasingly sophisticated systems.

This document picks up where the [Hookup Guide](https://learn.sparkfun.com/tutorials/sparkpunk-sequencer-hookup-guide) left off. If you haven\'t yet built your sequencer, start there, then come back.

[](https://learn.sparkfun.com/tutorials/sparkpunk-hookup-guide)

### SparkPunk Hookup Guide 

June 12, 2014

How to assemble and modify the SparkPunk Sound Generator kit.

## Theory Of Operations

In order to modify the sequencer, it is useful to understand some of its internal workings. We\'re going to step through the functional blocks on the schematic, and discuss how each works in more detail. If you\'d like a better look at the schematic or PCB artwork, you can download the Eagle files from [Github](https://github.com/sparkfun/Sparkpunk_Sequencer).

The sequencer was designed in simulation before the prototype hardware was constructed. Also in the Github repo are Spice simulation files, which run in the free [LTSpice](http://www.linear.com/designtools/software/) environment. The simulations proved to be very valuable, especially in getting the variable-width gate circuit working.

The SparkPunk Sequencer is a mixed-signal circuit \-- it consists of a digital section for the clocking and play logic, and an analog section to generate the control voltage and gate.

------------------------------------------------------------------------

### Digital Section

We\'ll start with the digital portions of the circuit. These are mostly implemented using CD4000-series CMOS logic chips. These chips are rated for a wide range of supply voltage \-- unlike some newer, more sensitive logic chips, they\'re prefectly happy being powered by a 9V battery.

------------------------------------------------------------------------

#### Run Button

The RUN pushbutton on the sequencer is a momentary-contact type switch. To use it in a toggling application (push once to turn on, push again to turn off), it\'s connected to one section of a CD4013 flip-flop. The switch is connected to the clock input on the flip-flop, and the inverted logic output is looped back to the data input.

[![button circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/schem-button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/schem-button.png)

Every time the button is pushed, the flip-flop output changes state.

The flip-flop has two outputs, called Q and [Q], and their functions can be described as:

- Q is called \"Stop.\" It is asserted when the sequencer is stopped.
- [Q] is called \"Run.\" It is asserted when the sequencer is running.

The run and stop signals are used in other portions of the circuit \-- other circuitry needs to react appropriately when the sequencer is started or stopped, and these signals allow for those actions.

The flip-flop also has data preset inputs (the Set and Reset pins). When power is applied, the capacitor on the Set input holds it high for a moment, causing the flip-flop to initialize in the Set state, so the sequencer is stopped by default.

The Run signal is connected to the LED in the button, so it illuminates while the sequencer is playing.

------------------------------------------------------------------------

#### Tempo Clock and Divider

The next functional block of the circuit is the tempo clock. It consists of two stages: the clock oscillator, and a divider.

The oscillator portion is is based around a 7555, which is a low-power CMOS version of the venerable [555 timer IC](https://www.sparkfun.com/products/9273). The basic circuit configures the timer in astable (free-running) mode, with the timing set by a potentiometer.

[![Clock and Divider Schematic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/schem-clock.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/schem-clock.png)

When the sequencer is running, the clock is enabled by the Run signal from the button circuit. The 7555 does not run when the sequencer is stopped.

The output from the 7555 is not used directly by the rest of the sequencer. The 7555 output is further conditioned using a divide-by-two circuit, using the other flip-flop in the CD4013. This is done for several reasons:

- First, the clock generated by the 7555 isn\'t perfectly symmetrical - the pulse width changes with frequency. This made the short/long switching hard to achieve, and also made the tempo LED hard to discern - wide pulses meant it was almost always illuminated.
- Second, by dividing the clock down, we can achieve a useful range of tempos with smaller timing capacitors. The division in half has the same effect as doubling the capacitor value.
- The divided-down clock has a pulse width of 50%, which is then used as an input to the system the generates the short (half-step long) gates.
- Finally, there was an otherwise unused flip-flop in the CD4013.

The Q output of the flip-flop is the clock signal used by the rest of the circuit. It also drives the RATE indicator LED.

------------------------------------------------------------------------

#### CD4017

The CD4017 is essentially a sequencer on a chip. It\'s the heart of this kit, and the rest of the circuit serves in a role to support its basic functionality. Internally, it has a binary ripple counter and a demultiplexer. It receives pluses on pin 14, which causes the counter to increment. The value of the counter is decoded so that one of the ten output pins (labeled Q0 through Q9) is active at a time. Each clock pulse causes the next output pin to be selected, and the selection starts over at Q0 after Q9 has been reached.

[![CD4017 Timing](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/4017-timing.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/4017-timing.png)

The timing of the CD4017 can be seen in the diagram above. The clock is the bottom trace, and the ten outputs are the traces above that. On each rising edge of the clock, the high logic level progresses to the next successive output.

[![Heart of Sequencer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/schem-4017.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/schem-4017.png)

The CD4017 also has a reset pin, which restarts the output selection from Q0 when it is asserted. This allows us to implement some more subtle behavior:

- When the sequencer is not playing, it sits at the first step. This is done by connecting the stop signal to the reset pin on the CD4017.
- When the sequence starts playing, the reset line is held high for a brief moment by capacitor C10. This means that the CD4017 effectively ignores the first clock pulse, and that the sequence starts on the first step. Without this cap, the clock starts as soon as the run button is pressed, and the sequence immediately advances to the second step.
- By feeding the selection pulse from one of the step outputs back to the reset pin, we can constrain the pattern to fewer than ten steps.

------------------------------------------------------------------------

### Analog Circuitry

#### The Steps

The ten outputs from the CD4017 are fed to the ten step circuits. Each step is a copy of the same circuit.

[![Step Schematic](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/schem-step.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/schem-step.png)

The CD4017 outputs are only rated to supply a couple of milliamps, so the step circuit starts with a transistor configured as an emitter follower, allowing for more output current to illuminate the LED. The step selection voltage is also fed to the slider, which is wired as a voltage divider. When the step is selected, the wiper of the slider travels between ground and about 8.3V. The gate switch on each step selects between the selection voltage, and ground.

The slider wipers and switches are coupled to common buses, POTSUM and GATESUM respectively, using diodes. This configuration implements the selection of the maximum voltage. Since only one step is selected at a time, that means all but one input to the max function will be zero, allowing the selected step to dominate.

------------------------------------------------------------------------

#### Slider Voltage Processing

To understand how the slider voltage is manipulated, we need to step back and look a little more closely at the device it is feeding. The SparkPunk Sound Generator uses a 7556 dual timer IC as its main tone source. The 7556 has control voltage inputs, but they behave in a somewhat counterintuitive manner \-- a *higher* voltage on the CV pin results in a *lower* frequency \-- an *inverse relationship*. It also works best in the middle of the range between ground and the power supply voltage \-- leaving that range causes the 7556 to stutter or stall.

The [LM358 amplifier IC](https://www.sparkfun.com/products/9456) is also constrained. The [datasheet](http://www.sparkfun.com/datasheets/Components/General/LM358.pdf) states that the maximum input level is 1.5V below the positive supply rail.

The sequencer manages the voltages coming from the slider wipers accordingly, inverting and scaling the voltage into a usable range.

[![CV circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/schem-cv.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/schem-cv.png)

Follwing the signal through the circuit, first we find a divider, to drop the level into the LM358\'s allowable range. That signal is buffered with an opamp stage, then fed to the variable lowpass filter that implements the slide. As the resistance of RV2 is increased, it takes C3 longer to charge. The filter is buffered with another opamp stage. Finally, the third opamp inverts and offsets the control voltage into a range suitable for the 7556.

------------------------------------------------------------------------

#### Switch Voltage Processing

The gate behavior of the sequencer can be changed between short gates, which are each one-half step in duration, and long gates, which are a complete step long. Additionally, the gate is only driven when the sequencer is running, so it sits quietly when stopped. The logic behind the gate can be expressed by the following equations:

    Long gate = running && step switch 
    Short gate = running && step switch && clock pulse

This logic is implemented using analog processing.

[![Gate Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/schem-gate.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/schem-gate.png)

The running, clock, and switch signals are scaled and added together, resulting in a stair-step shaped waveform. Each of those signals contributes a portion to the overall sum, as denoted by the colored rectangles below.

[![Gate Voltage-Staircase](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/staircade-colors.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/staircade-colors.png)

Notice that when a clock pulse overlaps a step switch that is turned on, they add up to the highest step shown, and the step switch by itself is the second highest step. A clock pulse that doesn\'t overlap the switch being set is lower still. We use an op-amp comparator circuit to apply thresholds to discern those first two stairstep levels.

The actual circuit uses an inverting op-amp stage to do the summing, so the result is upside down compared to that shown above. This is corrected by the comparator stage that generates the gate, which is also inverts.

The threshold voltage on the comparator determines the length of the gate pulses. Short gates are generated when the threshold voltage is tripped by the sum of the clock and switch signals.

[![Short Gate Waveforms](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/short-gate.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/short-gate.png)

*Short Gate Pulse Generation*

The clock is shown in red, and the inverted stairstep waveform in green. The comparator threshold is shown in light blue, superimposed over the stairstep. When the stairstep falls below the threshold, the comparator output, in dark blue, switches high.

Long gates use the same processing, but the threshold voltage is adjusted so that only the switch voltage is required to trip the comparator.

[![Long Gate Waveforms](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/long-gate.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/long-gate.png)

*Long Gate Pulse Generation*

### Strong Foundation

With the understanding of the internal details described above, we\'re how ready to look at some ways that those details can be leveraged into modifications and more sophisticated deployments.

## Simple Modifications

With the knowledge of the sequencer internals from the previous section, we can explore some modifications and more advanced uses of the sequencer.

We\'ll start with some simple modifications that don\'t require much effort, or very much external hardware.

### Sequence Length Adjustment

The CD4017 IC at the heart of the Sequencer has ten outputs. While ten is the basis for decimal counting, it\'s not always the obvious choice for musical composition - four, six or eight steps are much more common musical time signatures. As we mentioned in the [hookup guide](https://learn.sparkfun.com/tutorials/sparkpunk-sequencer-hookup-guide), the length of the sequence can be constrained to shorten the sequence.

The CD4017 has a pin that resets the internal counter. By feeding one of the step voltages back to that pin, we can constrain the sequence to a shorter range.

The Sequencer PCB has ten pairs of pads across the lower right edge. The step voltage from each step is present on the top pad, and the bottom pad is the counter reset. If you connect the top pad to the bottom pad, it causes the sequence to reset when that step is selected. For instance, if you short the *Step Out 9* pad to the adjacent *Seq Reset* pad, when step 9 is selected, it will cause the sequence to reset to the first step, effectively limiting the sequence to 8 steps.

[![Last Step With Shunts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/closeup-last-step.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/closeup-last-step.jpg)

You can make the connection between the pads a number of different ways. If you wanted the constraint to be permanent, you could solder in a short piece of wire. For a manually adjustable limit, snap [breakaway headers](https://www.sparkfun.com/products/116) off into 2-pin pairings, and solder them into each pair of pads. Then you can use [jumper shunts](https://www.sparkfun.com/products/9044) to bridge them.

------------------------------------------------------------------------

### One-Shot Sequence Playback

Similar to the reset pin on the CD4017, there is an asynchronous set pin on the flip-flop that latches the play button (recall that the Q output from the flip-flop is the source of the \"stop\" signal). If we route a step voltage to that pin, we can cause the sequence to stop itself when that step is reached.

This is easy do do using the pads near the CD4013, marked `ONCE`. Again, you can use a 2-pin header or a switch to make the connection.

[![One Shot Setting](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/closeup-oneshot.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/closeup-oneshot.jpg)

This works in conjunction with the \"last step\" setting described above \-- a last step is selected, and the sequence will run once, halting when it reaches that step. Because the flip-flop requires a pulse to set it, there is no easy way to do this with a full set of ten steps, as there is no additional pluse to indicate it has moved beyond the tenth step.

------------------------------------------------------------------------

### Component Values

#### Tempo Clock

The tempo clock is based around the parallel combination of C2 and C4. By changing those caps, we can change the rate of sequence playback. The equation that governs the frequency is stated in the [7555 datassheet](https://cdn.sparkfun.com/datasheets/Kits/icm7555-56.pdf), as

    7555 frequency = 1/(1.4 * R * C)

Where R is the series combination of R1 and RV1, adjustable between 470 Ω and 10,470 Ω, and C is 20 µF, the parallel combination of C2 and C4

Because we\'re dividing the 7555 clock in half, the actual tempo clock is half that

    clock frequency = (7555 frequency/2)

This results in a range of about 1.5 Hz at the lowest, to 35 Hz at the highest.

To make the clock run slower, increase the capacitance. Lowering the capacitance will raise the frequency.

#### Slide Time

Similarly, we can change the maximum slide time by adjusting cap C3. Again, larger values will take longer to charge, lengthening the slide. Reducing the time with smaller values is probably not terribly useful, as we can already adjust the time downwards with potentiometer RV2.

------------------------------------------------------------------------

#### Colored LEDs

If red is not to you liking, you can switch out the LEDs for other colors. The board was fits regular 5mm (AKA T-1 3/4) LEDs. We offer them in many colors, including [red](https://www.sparkfun.com/products/9590), [yellow](https://www.sparkfun.com/products/9594), [blue](https://www.sparkfun.com/products/11372), and [green](https://www.sparkfun.com/products/9592). You may need to substitute different resistors for the series 2.2K Ω, to adjust the brightness.

## Interfacing With More Hardware

### Heads Up!

We\'re working our way into more advanced territory. The sections below are a more adventurous than anything we\'ve touched on yet, and involve desoldering, modifications to the PCB, and more detailed troubleshooting skills. Some of the descriptions are purposefully vague, as an exercise for more knowledgable users.

### Synchronizing Multiple Sequencers

[![Twins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/flotilla.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/flotilla.jpg)

If you were following the theory of operations carefully, you probably noticed that when the text described the signals run, stop, clock, and button, the signals in the schematic were actually marked \"out\" and \"in,\" with a jumper connecting them. These signals are intended to be broken up that way so they can be easily routed between multiple sequencers.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/closeup-sync-port.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/closeup-sync-port.jpg)

*Synchronization Interface*

Those signals are all present in the synchronization interface, on the left edge between the run button and tempo knob. The following table denotes the behavior of each of those signals exhibits.

  ----------------------- ------------------------------------------- ------------------------------------
  **Signal**              **As Output**                               **As Input**

  **CLK**                 Pulses at tempo generated by clock system   Causes CD4017 counter to increment

  **STOP**                Indicates sequencer is stopped              Resets CD4017\
                                                                      Holds clock divider in reset

  **RUN**                 Indicates sequence is playing               Allows 7555 to run

  **BTN**                 Indicates button has been pushed            Pulses cause play/stop to toggle
  ----------------------- ------------------------------------------- ------------------------------------

\

In paticular, notice that for the sequencer to advance, the stop line must be low, run line must be high, and clock pulses need to come in on the clock line.

The most obvious way to use this port is to synchronize multiple sequencers. One acts as the master clock, with other sequencers following (or \"chasing\") that clock.

#### Modifications

If you have two sequencers, it\'s not hard to modify them to use the synchronization port. Select one to be the the master clock, and the other to follow that clock.

1.  First, on the slave sequencer, cut the copper traces that run between the columns of the synch port.

    [![Cutting Traces](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/closeup-knife.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/closeup-knife.jpg)

2.  Then run wires from the pads in the \"O\" (output) column on the master sequencer to the \"I\" (input) column on the slave. We\'re using [snappable headers](https://www.sparkfun.com/products/116) and [4-pin jumper wires](https://www.sparkfun.com/products/10364), so we can easily disconnect the units later.

    [![Synch Cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/closeup-sync-cable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/closeup-sync-cable.jpg)

3.  You\'ll also need to join the grounds of both sequencers together. It\'s easiest to tack-solder a short length of wire to the \"GND\" pin of the 9V battery box on one sequencer, and run it to the same point on the other.

    [![Power Jumpers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/closeup-power-tacks.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/closeup-power-tacks.jpg)

    You can also connect the nearby 9V terminals, so that you only need a single battery to power the whole conglomeration, but it will eat batteries twice as fast.

4.  Now, when you press play on the master, both sequencers will start and run together.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/flotilla.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/flotilla.jpg)

One clock master can drive multiple slaves, if you connect the slave synch input ports in parallel with each other.

To make a sequencer that can convert between being a master and slave, you can use [normalled jacks](https://www.sparkfun.com/products/11144), or install two pins from a [snappable header](https://www.sparkfun.com/products/116) and use [jumper shunts](https://www.sparkfun.com/products/9044) to reconnect the pins.

### Power

As you start to stack up multiple SparkPunks and Sequencers, you start to wind up against the limits of what a 9V battery can reliably power. The first symptom of insufficient power is that the long/short gate feature stops working reliably.

If you\'d like to avoid batteries altogether, you can substitute a [9V wall adapter](https://www.sparkfun.com/products/298). Each Sequencer & SparkPunk pair draw a maximum of about 20 mA, so that adapter should be good for many, many pairs. The best way to connect it is using a star topology, with each sequencer having a dedicated power and ground cables back to the power supply, rather than daisy-chaining power to multiple sequencers.

### Other Synthesizers

One last modification worth mentioning is to use the Sequencer with other synthesizers.

As we reviewed in the description of the control voltage interface, the main control voltage output is inverted - a higher voltage results in a lower frequency from the Sound Generator. This is counter-intuitive, and also the opposite of the convention used by most other synthesizers. Regular analog synthesizers with control voltage inputs produce higher frequencies for higher control voltages. This voltage is present inside the Sequencer, and is found on the solder pad marked `RAW CV OUT`. This is the stage after the slide has been applied, but before the amplifier that inverts it for the SparkPunk.

[![Pads Closeup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/8/closeup-raw-cv.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/8/closeup-raw-cv.jpg)

Before you try this, you should check the specification of the synthesizer you intend to control \-- additional circuitry may be needed to get the raw CV scaled into a suitable range. Some synths are limited to a gate of only 5V \-- you can use a divider or Zener diode clamp to attenuate the 9V gate into that range.

### Tempo CV Input

The eagle eyed reader will have also spotted the `TEMPO CV IN` pad in the photo above. It is similar to the CV inputs on the Sound Generator \-- voltages between ⅓ Vcc and ⅔ Vcc adjust the tempo over about a 2-to-1 range. The response is inverted \-- higher voltage results in lower frequency. Exceeding the ⅓ to ⅔ window can cause the 7555 to stutter or stall.

We don\'t have any specific mods for the Tempo CV, but it is worth mentioning as an option, so someone will sure dream up a use for it!