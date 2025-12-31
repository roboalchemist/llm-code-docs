# Source: https://learn.sparkfun.com/tutorials/continuous-rotation-servo-trigger-hookup-guide

## Introduction

When we introduced the regular [Servo Trigger](https://www.sparkfun.com/products/13118), we mentioned that it could be reprogrammed to be more useful with continuous rotation servo motors. However, reprogramming the firmware is somewhat tedious, and users asked for a Servo Trigger preprogrammed with the continuous rotation logic. You asked, and we listened! Introducing the [Continuous Rotation Servo Trigger](https://www.sparkfun.com/products/13872)! The name is a mouthful, but if you\'re looking for an easy way to deploy continuous rotation servos, it should be exactly what you\'re looking for.

[![SparkFun Servo Trigger - Continuous Rotation](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/4/9/0/13872-01.jpg)](https://www.sparkfun.com/sparkfun-servo-trigger-continuous-rotation.html)

### [SparkFun Servo Trigger - Continuous Rotation](https://www.sparkfun.com/sparkfun-servo-trigger-continuous-rotation.html) 

[ WIG-13872 ]

Simple, Code-Free Control for Continuous Rotation Servos The SparkFun Continuous Rotation (CR) Servo Trigger is designed f...

[ [\$17.50] ]

Like its sibling, the Continuous Rotation Servo Trigger allows you to control a hobby servo motor without any programming. The servo speed and direction are adjusted using trimpots, and the direction can be changed by attaching a switch.

[![Continuous Rotation Servo Trigger in Automated Camera Dolly ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/7/cart-overview.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/cart-overview.jpg)

In this guide, we\'ll show you how to quickly get your CR Servo Trigger working, then discuss some of the finer details of using and configuring it. Finally, we\'ll show how it was used to build a simple automated camera dolly.

### Suggested Reading

- We\'re not going to get too deep into the basics of hobby servos in this hookup guide. If you want more detailed information, check out our [Hobby Servo Tutorial](https://learn.sparkfun.com/tutorials/hobby-servo-tutorial).
- Some more background on [motors](https://learn.sparkfun.com/tutorials/motors-and-selecting-the-right-one).
- If you came here looking for information about the regular [Servo Trigger](https://www.sparkfun.com/products/13118), you can find its [hookup guide over here](https://learn.sparkfun.com/tutorials/servo-trigger-hookup-guide).

## Continuous Rotation Servo Motors

A continuous rotation servo (sometimes called a **full rotation** or **360°** servo) looks like a regular hobby servo. While a regular servo motor only turns over a narrow range, with precise control over position, a continuous rotation servo has a shaft that spins continuously, with control over its speed and direction.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/servo-type-compare.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/servo-type-compare.png)

The control is performed using a pulse train signal, typically with pulses that vary from 1 to 2 milliseconds, sent every 20 milliseconds (50 Hz). A one millisecond pulse corresponds to full speed in one direction, while a two millisecond pulse is full speed in the other direction. These pulses are easy to generate using the [pulse-width-modulation](https://learn.sparkfun.com/tutorials/pulse-width-modulation) hardware on a modest microcontroller.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/TEK0016.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/TEK0016.png)

*Two millisecond pulses, sent every 20 milliseconds.*

Halfway between those extremes, a 1.5 millisecond pulse should cause the motor to stop. Most CR servos have an adjustment screw or trimpot that allows you to fine tune the point at which it stops, a calibration procedure often called **nulling**.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/7/cr-servo-trimmer.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/cr-servo-trimmer.jpg)

*Nulling trimpot*

With the CR Servo Trigger, the stop point can be adjusted on the board, but if it behaves unexpectedly, double check that the trim on the servo itself isn\'t the root of the problem.

## Getting Started Quickly

Let\'s jump in and build a circuit to show how the Servo Trigger works!

### Materials and Tools

You\'ll need to following materials to build this example circuit found in this tutorial.

[![DC Barrel Jack Adapter - Female](https://cdn.sparkfun.com/r/140-140/assets/parts/4/6/8/4/10288-02.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html)

### [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html) 

[ PRT-10288 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.75] ]

[![Servo - Generic High Torque Continuous Rotation (Standard Size)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/1/1/09347-1.jpg)](https://www.sparkfun.com/servo-generic-high-torque-continuous-rotation-standard-size.html)

### [Servo - Generic High Torque Continuous Rotation (Standard Size)](https://www.sparkfun.com/servo-generic-high-torque-continuous-rotation-standard-size.html) 

[ ROB-09347 ]

Here, for all your mechatronic needs, is a simple, high quality continuous rotation servo motor. This servo is able to take i...

[ [\$20.50] ]

[![Momentary Pushbutton Switch - 12mm Square](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/2/9/09190-03-L.jpg)](https://www.sparkfun.com/momentary-pushbutton-switch-12mm-square.html)

### [Momentary Pushbutton Switch - 12mm Square](https://www.sparkfun.com/momentary-pushbutton-switch-12mm-square.html) 

[ COM-09190 ]

This is a standard 12mm square momentary button. What we really like is the large button head and good tactile feel (it \'clic...

[ [\$0.75] ]

[![SparkFun Servo Trigger - Continuous Rotation](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/9/0/13872-01.jpg)](https://www.sparkfun.com/sparkfun-servo-trigger-continuous-rotation.html)

### [SparkFun Servo Trigger - Continuous Rotation](https://www.sparkfun.com/sparkfun-servo-trigger-continuous-rotation.html) 

[ WIG-13872 ]

Simple, Code-Free Control for Continuous Rotation Servos The SparkFun Continuous Rotation (CR) Servo Trigger is designed f...

[ [\$17.50] ]

[![Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/8/00553-03-L.jpg)](https://www.sparkfun.com/break-away-male-headers-right-angle.html)

### [Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-male-headers-right-angle.html) 

[ PRT-00553 ]

A row of right angle male headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custo...

[ [\$2.50] ]

[![Wall Adapter Power Supply - 5V DC 2A (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/1/12889-01.jpg)](https://www.sparkfun.com/products/12889)

### [Wall Adapter Power Supply - 5V DC 2A (Barrel Jack)](https://www.sparkfun.com/products/12889) 

[ TOL-12889 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA Barrel Jack wall power supply manufactured specifically for S...

**Retired**

You\'ll also need some [hookup wire](https://www.sparkfun.com/products/11375) and a [small screwdriver](https://www.sparkfun.com/products/9146).

### Doublecheck The Trigger

Before we start building, doublecheck that you\'ve got a [Continuous Rotation Servo Trigger](https://www.sparkfun.com/products/13872). There are tick boxes on the back of the PCB, and the \"continuous rotation\" box should be marked.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/tickbox-callouts.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/tickbox-callouts.png)

### Preparations

To start, [solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) some wires to the tactile switch. If you solder to legs on on opposite corners (top-right and lower-left, for instance), you can be confident that you\'ll get a contact closure when you press the button.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/7/switch-pigtail.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/switch-pigtail.jpg)

*Switch Assembly*

Next, prepare the power plug pigtail. Take a pair of wires, and strip the ends. Then screw them to the power jack adapter \-- if you look closely at the adaptor, you\'ll notice that there are a small `+` and `-` embossed in the plastic. We used a red wire for VCC on the `+` terminal and a black wire for ground on the `-` terminal.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/7/power-pigtail.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/power-pigtail.jpg)

*Power Jack Closeup*

Take your right-angle male headers, and snap of a section of three headers. Solder the 3-pin header to the three pads on the end the board, and plug the servo into the the header. Be careful to get the plug oriented correctly \-- you can check the [color code table](https://learn.sparkfun.com/tutorials/hobby-servo-tutorial/servo-motor-background#colortable) in the servo tutorial, or consult the servo manufacturer\'s datasheet.

Solder the switch wires to the `IN` and `GND` pads on the Servo Trigger and the power pigtail to the `VCC` and `GND` pads on the edge of the board. These are mirrored on opposite edges of the board \-- they\'re wired in parallel, so you can use either set of pads. The red wire should connect to the `VCC` pad and the black to `GND`.

Before we power up, take a moment to double-check your work against the photo below (click on the picture for a larger version). In particular, make sure that the power and servo connections are oriented correctly.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/7/tweaking.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/tweaking.jpg)

*Adjusting the trimpots.*

Adjust the trimpots on the back of the board. Set `A` fully counterclockwise, `B` fully clockwise, and set `T` to the middle.

Finally, apply power. The servo should start to turn. If not, power down, and recheck your work.

While it\'s running, tap the switch. The servo will take a couple of seconds to slow down, stop, then reverse. Tap the switch again, and it will go back to the original direction.

Now you can adjust the trimpots to configure the servo.

- `A` sets the speed and direction of the motor before the switch is actuated.
- `B` sets the speed and direction of the motor after the switch is actuated.
- `T` sets the time it takes to get from A to B and back.

When A and B are near the middle of their rotation, the servo will stop. Turning them clockwise from there instructs the servo to turn in one direction; turning them counterclockwise results in the opposite direction. The farther from the center, the faster the servo turns. The transition time is adjustable between 50 milliseconds and 10 seconds. The transition time is constant \-- when set to 2 seconds, the servo will take 2 seconds to move between A and B, regardless of how close the A and B settings are.

In the next section, we\'ll explore some of the finer details of the Continuous Rotation Servo Trigger.

## Theory Of Operations

The Servo Trigger consists of two major engineering deliverables, the hardware design, and the firmware. The hardware is actually the same for the regular and continuous rotation boards, but they\'re loaded with different firmware, tailoring the board\'s behavior to each type of servo motor. Both sets of deliverables are in the [Servo Trigger Github repository](https://github.com/sparkfun/Servo_Trigger).

### On The Board

Let\'s look at the components on the board and examine what they do.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/PCB-arrows2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/PCB-arrows2.png)

The heart of the Servo Trigger is an Atmel ATTiny84 microcontroller, running a small program that implements the servo control features we are discussing here. Just because the Servo Trigger saves you from needing to write code doesn\'t mean that there was no programming involved!

The servo control signal is generated using a 16-bit hardware timer. It runs off a 1 MHz clock, counting to 20000 to generate the 20 mSec (50 Hz) period and is configured to generate pulses that range from 1000 to 2000 µSec (1 to 2 milliseconds).

The three potentiometers are connected as voltage dividers between VCC and ground. They are read using analog inputs ADC0, ADC3, and ADC7.

The switch input is read using PortA, input pin 1. It is debounced in software and can be configured to watch for a switch closure or a logic level pulse.

The board also includes the common 6-pin in-system-programming header, which we\'ll discuss in the [Servo Trigger Programming Guide](https://learn.sparkfun.com/tutorials/servo-trigger-programming-guide). But we\'re getting a bit ahead of ourselves \-- there are some configuration options you can use without programming.

### Configuration

The Servo Trigger has a couple of configuration options. If you look at the back of the PCB, you\'ll notice two solder jumpers that can be used to change Servo Trigger\'s response.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/jumper-callouts.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/jumper-callouts.png)

*Configuration Jumpers, SJ1 and SJ2.*

When it first powers up, the servo trigger reads these jumpers and configures itself accordingly.

#### Modes

The Servo Trigger has two different servo control modes, selected with solder jumper 1 (SJ1). They can be used to tailor the response of the board for different applications.

The default mode implements **toggling** control. The trigger initializes driving the servo as instructed by trimmer `A`. When the switch closes, it transitions to the speed indicated by `B`. When the switch closes again, it returns to `A`. The time taken to get between `A` and `B` is selected using trimmer `T`, which ranges from nearly instantaneous to 10 seconds, allowwing the motor to gradually slow, stop, and reverse.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/toggling-diagram.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/toggling-diagram.png)

*Mode Jumper Cleared - Toggling Control*

This behavior can be changed by flowing solder between the pads of the mode jumper.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/7/sj1-blob.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/sj1-blob.jpg)

*Closing SJ1 to select bistable mode.*

With the solder jumper closed, the mode changes to **bistable** control \-- the servo will drive at speed A while the switch is open, and speed B while the switch is closed. While the switch input stays in a state, the servo drives at the corresponding speed \-- it is *stable* in *two* different states.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/bistable-diagram.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/bistable-diagram.png)

*Mode Jumper Cleared - Bistable Control*

#### Input Polarity

The Servo Trigger input sensitivity can also be changed, using solder jumper 2 (SJ2).

The default configuration, with no solder applied, configures the Servo Trigger for use with a normally-open switch, with the internal pull-up resistor on the microcontroller enabled. This configuration is also suitable for use with an active-low logic input.

With SJ2 closed, the internal pull-up is disabled, and the input is set as an active-high logic input.

If SJ2 is closed, be careful about powering up the Servo Trigger when the input is not connected to anything. When the input is floating, it can randomly jump between active and inactive and may cause the motor to behave unpredictably.

*A note about nomenclature*: since the input polarity can be swapped, it can be hard to talk about \-- the voltage might be high, but when the sense is inverted, it indicates that the input isn\'t being actuated. To help navigate this, the polarity-neutral terms **active** or **asserted** are used to describe when the input is being used, and **inactive** or **deasserted** to describe the default state.

### More components

The servo trigger can be used with a wider variety of external components than used in the example above. We used a [standard size continuous rotation servo](https://www.sparkfun.com/products/9347), though we also offer a [micro size](https://www.sparkfun.com/products/10189) one.

You can also use different switches, such as [micro switches](https://www.sparkfun.com/products/9506) or [foot pedals](https://www.sparkfun.com/products/11192).

### Power Notes

Compared to a servo motor, the Servo Trigger board draws very little current \-- roughly 5 mA.

The motor draws significantly more \-- a quick bench test using a small servo, with only a lightwieght horn attached, shows the motor draws 10 mA sitting idle, and about 70 mA while moving. Grabbing the horn and twisting causes the controller to apply current to the motor, counteracting the twist. It drew 700 mA during this test \-- a larger servo could draw even more!

These currents can get surprisingly high as you add more motors to the system \-- you\'ll need to select a power supply with adequate capacity. An Ampere per motor is a reasonable guideline. For more information about powering servos, please see the [powering a servo](https://learn.sparkfun.com/tutorials/hobby-servo-tutorial/servo-motor-background#powering) section of our Servo Tutorial.

When in doubt, grab a multimeter, measure the current consumed, and check whether VCC at the board input is falling below the expected voltage when the servos are turning.

### Troubleshooting

If there\'s no change when you actuate the input, first check that A and B are not set to the same position, otherwise there\'s no speed change!

If you\'re feeding the input with a logic signal from an external device, be sure to drive the signal for more than 50 milliseconds. The PWM signal is updated every 50 mSec, and events shorter than that may be missed.

If the servo only turns on one direction, doublecheck that the trimpot on the servo is near the center of its range. If it\'s near one end or the other, the servo will go from full speed to stopped, but not reverse.

For additional servo troubleshooting ideas, please consult the [Servo Turorial](https://learn.sparkfun.com/tutorials/hobby-servo-tutorial/troubleshooting).

## Example Project

To demonstrate the usefulness of the Continuous Rotation Servo Trigger, we put a continuous rotation servo on a small camera dolly. The dolly has a whisker switch at each end, allowing it to do automated tabletop camera moves.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/7/cart-overview.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/cart-overview.jpg)

Lacking an old-fashioned rollerskate to dismantle for the chassis, we started with a commercial [camera skate dolly](http://www.bhphotovideo.com/c/product/999686-REG/revo_scaled_skter_dly_w.html).

[![Servo - Generic High Torque Continuous Rotation (Standard Size)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/1/1/09347-1.jpg)](https://www.sparkfun.com/servo-generic-high-torque-continuous-rotation-standard-size.html)

### [Servo - Generic High Torque Continuous Rotation (Standard Size)](https://www.sparkfun.com/servo-generic-high-torque-continuous-rotation-standard-size.html) 

[ ROB-09347 ]

Here, for all your mechatronic needs, is a simple, high quality continuous rotation servo motor. This servo is able to take i...

[ [\$20.50] ]

[![Jumper Wire - 0.1\", 2-pin, 6\"](https://cdn.sparkfun.com/r/140-140/assets/parts/4/8/1/9/10367-01.jpg)](https://www.sparkfun.com/jumper-wire-0-1-2-pin-6.html)

### [Jumper Wire - 0.1\", 2-pin, 6\"](https://www.sparkfun.com/jumper-wire-0-1-2-pin-6.html) 

[ PRT-10367 ]

This is a simple two wire cable. Great for jumping from board to board or just about anything else. There is a 2-pin JST RE c...

[ [\$1.95] ]

[![Jumper Wire - 0.1\", 2-pin, 4\"](https://cdn.sparkfun.com/r/140-140/assets/parts/4/8/1/4/10362-01.jpg)](https://www.sparkfun.com/jumper-wire-0-1-2-pin-4.html)

### [Jumper Wire - 0.1\", 2-pin, 4\"](https://www.sparkfun.com/jumper-wire-0-1-2-pin-4.html) 

[ PRT-10362 ]

This is a simple two wire cable. Great for jumping from board to board or just about anything else. There is a 2-pin JST RE c...

[ [\$1.25] ]

[![SparkFun Servo Trigger - Continuous Rotation](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/9/0/13872-01.jpg)](https://www.sparkfun.com/sparkfun-servo-trigger-continuous-rotation.html)

### [SparkFun Servo Trigger - Continuous Rotation](https://www.sparkfun.com/sparkfun-servo-trigger-continuous-rotation.html) 

[ WIG-13872 ]

Simple, Code-Free Control for Continuous Rotation Servos The SparkFun Continuous Rotation (CR) Servo Trigger is designed f...

[ [\$17.50] ]

[![SparkFun RedBot Sensor - Mechanical Bumper](https://cdn.sparkfun.com/r/140-140/assets/parts/8/4/9/3/11999-01a.jpg)](https://www.sparkfun.com/sparkfun-redbot-sensor-mechanical-bumper.html)

### [SparkFun RedBot Sensor - Mechanical Bumper](https://www.sparkfun.com/sparkfun-redbot-sensor-mechanical-bumper.html) 

[ SEN-11999 ]

These simple switches are the Mechanical Bumper sensor for the SparkFun RedBot, giving you the ability to detect a collision ...

[ [\$6.50] ]

[![Lithium Ion Battery - 2000mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/2/Batt2AJST-01-L.jpg)](https://www.sparkfun.com/products/8483)

### [Lithium Ion Battery - 2000mAh](https://www.sparkfun.com/products/8483) 

[ PRT-08483 ]

These are very slim, extremely light weight batteries based on the new Polymer Lithium Ion chemistry. This is the highest ene...

**Retired**

[![SparkFun Power Cell - LiPo Charger/Booster](https://cdn.sparkfun.com/r/140-140/assets/parts/6/8/2/8/11231-01b.jpg)](https://www.sparkfun.com/products/11231)

### [SparkFun Power Cell - LiPo Charger/Booster](https://www.sparkfun.com/products/11231) 

[ PRT-11231 ]

The PowerCell board is a single cell LiPo boost converter (to 3.3V and 5V) and micro-USB charger in one. The board comes with...

**Retired**

We also had some [derelict robot parts](https://www.sparkfun.com/news/1660) around the workshop that we used to hold everything together. We improvised using materials we had handy and suggest that you do the same!

### Build the Circuit

To start, we assembled the circuit on the workbench.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/7/little-cart_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/little-cart_bb.png)

We used male and female headers to stack the Power Cell atop the Servo Trigger board.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/7/powercell-stack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/powercell-stack.jpg)

*Headers used to stack Power Cell on Servo Trigger.*

The whisker switches were assembled as described in this [hookup guide](https://learn.sparkfun.com/tutorials/redbot-assembly-guide-rev-02/redbot-sensor---mechanical-bumpers), with one built in right-hand orientation and the other left-handed.

The whisker switches also needed a quick electronic modification to make them compatible with the Servo Trigger. We desoldered the resistor from the PCB and replaced it with a blob of solder, so the whisker acts as a simple switch closure.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/7/whisker-blob.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/whisker-blob.jpg)

We plugged the 2 pin jumper wires into the `GND` and `5V` pins on the switches and stuck some [long pin headers](https://www.sparkfun.com/products/10158) through the switch contacts on the trigger PCB, so the switches could both plug in in parallel, one from above, the other from beneath.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/7/longpins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/longpins.jpg)

We gave it a quick test on the bench. Each time a whicker switch closed, the motor drove the other way. The `A`, `B`, and `T` adjustments each had the desired effect.

### Mechanical Integration

With the electronics working, we put them on the chassis.

The chassis itself consists of a platform with a couple of protruding M6 machine screws. The axles are mounted to the screws with wingnuts.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/7/cart-spread.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/cart-spread.jpg)

The drive mechanism for the cart is a simple slip clutch. We fashioned a double-width rubber wheel onto the servo using [Actobotics 2\" wheels](https://www.sparkfun.com/products/12425) and a pair of [servo hubs](https://www.sparkfun.com/products/12443). The motor was mounted to a [B-type servo bracket](https://www.sparkfun.com/products/12444), which was connected to the end of a [4.5\" channel](https://www.sparkfun.com/products/12122). The bracket was free to pivot in the end of the channel.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/slip-clutch.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/7/slip-clutch.gif)

The bracket channel was simply placed over the axle bolt on the cart chassis. A rubber band was looped around the assembly, putting tension on the servo, so that the drive wheel gently touched one of the skate wheels.

On the other end of the cart, a [1.5\" channel](https://www.sparkfun.com/products/12383) was placed over the other pivot. This allowed both axles on the cart to be spaced evenly, ensuring that all four skate wheels touch the tabletop. It also gave us some holes to mount the front whisker switch and a place to secure the battery and other electronics.

### Testing Results

The first time out was somewhat disappointing \-- the cart would drive until the first switch closed, then stall. It turns out the battery was nearly discharged! After a couple hours charging from a USB port, it behaved as expected.

We adjusted the trimmers so it drove slowly in both directions, with a medium transition time, so it wouldn\'t skid or jerk as it turned around.