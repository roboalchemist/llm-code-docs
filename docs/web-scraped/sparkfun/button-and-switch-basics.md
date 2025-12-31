# Source: https://learn.sparkfun.com/tutorials/button-and-switch-basics

## Introduction

One of the most elementary and easy-to-overlook circuit component is the switch.

[![switches](https://cdn.sparkfun.com/r/600-600/assets/c/5/d/3/d/517eb719ce395f8f17000000.png)](https://cdn.sparkfun.com/assets/c/5/d/3/d/517eb719ce395f8f17000000.png)

Switches don't require any fancy equations to evaluate. All they do is select between an open circuit and a short circuit. Simple. But how could we live without buttons and switches!? What good is a blinky circuit with no user input? Or a deadly robot with no kill switch? What would our world be without with big red buttons you should [never, ever press](http://www.youtube.com/watch?v=ku2wFaaPAzI).

### Covered in This Tutorial

- Momentary vs. Maintained Switches
- What do SPST, SPDT, DPDT, etc. all mean?
- The difference between normally closed and normally open buttons
- Lots of pretty button pictures
- Important switch ratings
- Switch applications

### Suggested Reading

Before diving into this tutorial, make sure you're up to snuff on the most basic of electronics knowledge. If you're not familiar with the following concepts, consider reading their tutorials first. Then come back, and we'll have some fun button talk.

- [What is a circuit?](https://learn.sparkfun.com/tutorials/what-is-a-circuit) - Especially know the difference between an [open and closed circuit](https://learn.sparkfun.com/tutorials/what-is-a-circuit/short-and-open-circuits)
- [Voltage, Current, Resistance, and Ohm's Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
- [Power](https://learn.sparkfun.com/tutorials/electric-power)
- [How to Use a Multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)
- [Binary](https://learn.sparkfun.com/tutorials/binary)

## Looking to explore different switches?

We\'ve got you covered!

[![Toggle Switch](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/7/7/09276-1.jpg)](https://www.sparkfun.com/toggle-switch.html)

### [Toggle Switch](https://www.sparkfun.com/toggle-switch.html) 

[ COM-09276 ]

This is a heavy duty SPST toggle switch - your basic on/off toggle. Rated for 2A at 250V or 4A at 125V. Includes a face plate...

[ [\$2.25] ]

[![SPDT Slide Switch](https://cdn.sparkfun.com/r/140-140/assets/parts/3/4/3/1/09609-01.jpg)](https://www.sparkfun.com/spdt-slide-switch.html)

### [SPDT Slide Switch](https://www.sparkfun.com/spdt-slide-switch.html) 

[ COM-09609 ]

This is a simple SPDT slide switch - great for use as an ON/OFF button, or just as a general control switch. The pins are spa...

[ [\$0.95] ]

[![5-way Tactile Switch](https://cdn.sparkfun.com/r/140-140/assets/parts/4/3/3/7/10063-01.jpg)](https://www.sparkfun.com/5-way-tactile-switch.html)

### [5-way Tactile Switch](https://www.sparkfun.com/5-way-tactile-switch.html) 

[ COM-10063 ]

A 5-way tactile switch allows for a joystick-like interface in a very small package. These are surface mount, but easily sold...

[ [\$3.95] ]

[![Foot Pedal Switch](https://cdn.sparkfun.com/r/140-140/assets/parts/6/7/5/1/11192-01.jpg)](https://www.sparkfun.com/products/11192)

### [Foot Pedal Switch](https://www.sparkfun.com/products/11192) 

[ COM-11192 ]

Put the pedal to the metal with this metal foot switch. This is the same kind of foot pedal you might find switching the powe...

**Retired**

[See all buttons and switches](https://www.sparkfun.com/categories/145)

------------------------------------------------------------------------

## What is a Switch?

A switch is a component which controls the open-ness or closed-ness of an electric circuit. They allow control over current flow in a circuit (without having to actually get in there and manually cut or splice the wires). Switches are critical components in any circuit which requires user interaction or control.

A switch can only exist in one of two states: open or closed. In the **off** state, a switch looks like an open gap in the circuit. This, in effect, looks like an **open circuit**, preventing current from flowing.

In the **on** state, a switch acts just like a piece of perfectly-conducting wire. A short. This **closes the circuit**, turning the system \"on\" and allowing current to flow unimpeded through the rest of the system.

[![alt text](https://cdn.sparkfun.com/assets/6/8/1/3/d/517afd7cce395f5349000003.gif)](https://cdn.sparkfun.com/assets/1/5/1/f/5/517afd67ce395f2f49000003.gif)

*A circuit diagram with an LED, resistor, and a switch. When the switch is closed, current flows and the LED can illuminate. Otherwise no current flows, and the LED receives no power.*

There are tons and tons of switches out there: toggle, rotary, DIP, push-button, rocker, membrane, \... the list just goes on and on. Each of those switch types has a set of unique characteristics to differentiate it from others. Characteristics like what action flips the switch, or how many circuits the switch can control. Next up, we\'ll go over some of the more basic switch characteristics.

## Defining Characteristics

### Actuation Method

In order to change from one state to another, a switch must be **actuated**. That is, some sort of physical action must be performed to "flip" the switch's state. The actuation-method of a switch is one of its more defining characteristics.

[![Switch actuation examples](https://cdn.sparkfun.com/r/600-600/assets/2/6/5/7/e/5181896ece395fba47000000.jpg)](https://cdn.sparkfun.com/assets/2/6/5/7/e/5181896ece395fba47000000.jpg)

*Some examples of switch types. [Push button](https://www.sparkfun.com/products/9190), [rocker](https://www.sparkfun.com/products/10727), [slide](https://www.sparkfun.com/products/9609), and [magnetic](https://www.sparkfun.com/products/8642).*

Switch actuation can come from pushing, sliding, rocking, rotating, throwing, pulling, key-turning, heating, magnetizing, kicking, snapping, licking,\...any physical interaction which can cause the mechanical linkages inside the switch to come into, or go out of, contact.

### Momentary vs. Maintained

All switches fall into one of two distinct categories: momentary or maintained.

**Maintained** switches \-- like the light switches on your wall \-- stay in one state until actuated into a new one, and then remain in that state until acted upon once again. These switches might also be called **toggle** or **ON/OFF** switches.

**Momentary** switches only remain active as long as they're actuated. If they\'re not being actuated, they remain in their "off" state. You've probably got a momentary switch (or 50) right in front of you\...keys on a keyboard!

Semantic alert! Most of the switches we refer to as \"buttons\" fall in the momentary category. Activating a button usually means pressing down on it in some manner, which just *feels* like a momentary control. There are such things as a [maintained button](https://www.sparkfun.com/products/9808), but for this tutorial when we slip and talk about \"buttons\", think "momentary push-down switch".

### Mounting Style

As with most components, the termination style of a switch always comes down to either surface mount (SMD) or through-hole (PTH). Through-hole switches are usually larger in size. Some might be designed to fit in a [breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) for easy prototyping.

[![Buttons in a breadboard](https://cdn.sparkfun.com/r/600-600/assets/d/7/f/d/b/517ebaf2ce395f1f18000002.jpg)](https://cdn.sparkfun.com/assets/d/7/f/d/b/517ebaf2ce395f1f18000002.jpg)

*These [Tactile buttons](https://www.sparkfun.com/products/10302) are through-hole and fit perfectly in a breadboard. Great for prototyping!*

SMD switches are smaller than their PTH counterparts. They sit flat, on top of a PCB. SMD switches usually require a gentle touch, they're not built to sustain as much switching force as a through-hole switch.

[![SMD buttons on an Arduino Pro](https://cdn.sparkfun.com/assets/e/c/a/0/5/517eba4ece395f2418000002.png)](https://cdn.sparkfun.com/assets/e/c/a/0/5/517eba4ece395f2418000002.png)

*The [Arduino Pro](https://www.sparkfun.com/products/10915) has two SMD switches: a [slide switch](https://www.sparkfun.com/products/10860) for power control, and a [push-button](https://www.sparkfun.com/products/8720) for reset control.*

Panel mount switches \-- designed to sit outside an enclosure \-- are a popular mounting style as well. It's hard to flip a switch when it's hidden inside an enclosure. Panel mount switches come in all sorts of termination styles: PTH, SMD, or heavy-duty solder lugs for soldering to wires.

[![Panel mounted toggle switch](https://cdn.sparkfun.com/r/400-400/assets/e/6/b/6/e/517ec466ce395f246c000000.jpg)](https://cdn.sparkfun.com/assets/e/6/b/6/e/517ec466ce395f246c000000.jpg)

*A panel mounted [illuminated toggle switch](https://www.sparkfun.com/products/11314).*

------------------------------------------------------------------------

One more important switch characteristic, which really deserves a page of its own, is the internal circuit arrangement of a switch. Are you looking for an SPST? DPST? 4PDT? What-P-what-now?

## Poles and Throws, Open and Closed

A switch must have at least two terminals, one for the current to (potentially) go in, another to (potentially) come out. That only describes the simplest version of a switch though. More often than not, a switch has more than two pins. So how do all of those terminals line up with the internal workings of the switch? This is where knowing how many poles and throws a switch has is essential.

The number of **poles**[\*](#not-pulls) on a switch defines how many separate circuits the switch can control. So a switch with one pole, can only influence one single circuit. A four-pole switch can separately control four different circuits.

A switch's **throw**-count defines how many positions each of the switch's poles can be connected to. For example, if a switch has two throws, each circuit (pole) in the switch can be connected to one of two terminals.

Knowing how many poles and throws a switch has, it can be more specifically classified. Commonly you'll see switches defined as "single-pole, single-throw", "single-pole, double-throw", "double-pole, double-throw", which are more often abbreviated down to SPST, SPDT, and DPDT, respectively.

#### SPST

A single-pole, single-throw (**SPST**) switch is as simple as it gets. It\'s got one output and one input. The switch will either be closed or completely disconnected. SPSTs are perfect for on-off switching. They're also a very common form of [momentary](momentary-switches) switches. SPST switches should only require **two terminals**.

[![SPST circuit example and real-life example](https://cdn.sparkfun.com/r/600-600/assets/6/d/9/2/e/517ed955ce395f471d000000.png)](https://cdn.sparkfun.com/assets/6/d/9/2/e/517ed955ce395f471d000000.png)

*The circuit symbol for an SPST switch in the off position and a [through-hole, right-angle, maintained, SPST, rocker switch](https://www.sparkfun.com/products/8837).*

#### SPDT

Another common switch-type is the **SPDT**. SPDTs have three terminals: one common pin and two pins which vie for connection to the common. SPDTs are great for selecting between two power sources, swapping inputs, or whatever it is you do with two circuits trying to go one place. Most simple slide switches are of the SPDT variety. SPDT switches should usually have **three terminals**. (Sidenote: in a pinch an SPDT can actually be made into an SPST by just leaving one of the switch throws unconnected).

[![An SPDT circuit example and real-life example](https://cdn.sparkfun.com/r/600-600/assets/2/7/c/c/c/517edaface395f581d000001.png)](https://cdn.sparkfun.com/assets/2/7/c/c/c/517edaface395f581d000001.png)

*An SPDT switch circuit symbol, and an [SPDT slide switch](https://www.sparkfun.com/products/102).*

#### DPDT

Adding another pole to the SPDT creates a double-pole, double-throw (**DPDT**) switch. Basically two SPDT switches, which can control two separate circuits, but are always switched together by a single actuator. DPDTs should have **six terminals**.

[![DPDT examples](https://cdn.sparkfun.com/r/600-600/assets/6/e/d/9/0/517edbabce395fd51d000000.png)](https://cdn.sparkfun.com/assets/6/e/d/9/0/517edbabce395fd51d000000.png)

*A DPDT circuit symbol, and a 6-terminal [DPDT rocker switch](https://www.sparkfun.com/products/11139).*

#### XPYT

Switches with more than two poles or throws are not too common, but they're out there (in all their oddly-shaped, difficult-to-connect-to glory). Once we get past one or two poles/throws, we just start sticking numbers in the abbreviation. Here\'s a 4PDT switch, for example, it can control four separate circuits, 2 positions per circuit:

[![A 4PDT switch](https://cdn.sparkfun.com/r/600-600/assets/8/f/8/6/6/517ed3fcce395f991d000000.png)](https://cdn.sparkfun.com/assets/8/f/8/6/6/517ed3fcce395f991d000000.png)

*A massive 4PDT circuit symbol, and an physically massive [4PDT toggle switch](https://www.sparkfun.com/products/11153).*

------------------------------------------------------------------------

[]\
\* Just remember: it's \"poles\", not \"pulls\". Seasoned engineers just *love* picking on poor saps who were only looking for a "single-pull, double-throw" switch. (Not speaking from experience here or anything\... I mean, in my defence, I didn't read it in a book, just heard it ambiguously pronounced by the professor. Meanies.)

### Normally Open/Closed

When a momentary switch is not actuated, it's in a "normal" state. Depending on how the button is constructed, its normal state can be either an open circuit or a short circuit. When a button is open until actuated, it's said to be **normally open** (abbreviated *NO*). When you actuate an NO switch, you're closing the circuit, which is why these are also called "push-to-make" switches.

Conversely, if a button usually acts like a short circuit unless actuated, it's called a **normally closed** (*NC*) switch. NC switches are "push-to-break"; actuating the switch creates an open circuit.

Among the two types, you're probably much more likely to encounter a normally open momentary switch.

## Momentary Switches

Momentary switches are switches which only remain in their on state as long as they're being actuated (pressed, held, magnetized, etc.). Most often momentary switches are best used for intermittent user-input cases; stuff like reset or keypad buttons.

### Examples of Momentary Switches

#### Push-button

Push-button switches are the classic momentary switch. Typically these switches have a really nice, tactile, "clicky" feedback when you press them. They come in all sorts of flavors: big, small, colorful, illuminated (when an LED shines up through the button). They might be terminated as through-hole, surface-mount, or even panel-mount.

[![Assortment of tactile switches](https://cdn.sparkfun.com/r/600-600/assets/b/6/1/a/0/518189efce395f1f45000000.jpg)](https://cdn.sparkfun.com/assets/b/6/1/a/0/518189efce395f1f45000000.jpg)

*An assortment of tactile push-button switches. Starting top-left, clockwise: [blue](https://www.sparkfun.com/products/9337) and [pink](https://www.sparkfun.com/products/9177) arcade buttons, [12mm push button](https://www.sparkfun.com/products/9190), [white capped button](https://www.sparkfun.com/products/10302), [orange illuminated](https://www.sparkfun.com/products/10441), [right-angle](https://www.sparkfun.com/products/10791), [panel-mount](https://www.sparkfun.com/products/9807), and a [mini push button](https://www.sparkfun.com/products/97).*

#### Button Matrices

Large arrays of momentary buttons, like your keyboard or even smaller groupings like a keypad, usually arrange all of their switches into a big matrix. Every button on the pad is assigned a row and column . This requires some extra button-press-processing on the microcontroller end, but frees up a big chunk of I/O pins.

[![12-button keypad](https://cdn.sparkfun.com/assets/6/9/4/d/c/517ee389ce395f1c1d000000.jpg)](https://cdn.sparkfun.com/assets/6/9/4/d/c/517ee389ce395f1c1d000000.jpg)

#### Etc.

Momentary switches don't always have to be actuated by a pushdown. It could be push-sideways, like the movement action in a handful of joysticks.

[![Joysticks](https://cdn.sparkfun.com/r/500-500/assets/a/2/f/9/8/5182a714ce395fed1d000000.png)](https://cdn.sparkfun.com/assets/a/2/f/9/8/5182a714ce395fed1d000000.png)

*An [arcade joystick](https://www.sparkfun.com/products/9182) uses four [microswitches](https://www.sparkfun.com/products/9414) to sense up, down, left and right movements. The tiny little surface-mount [5-way tactile switch](https://www.sparkfun.com/products/11187) is an SP5T directional switch (up, down, left, right, and press-down).*

On the other end of the spectrum, [reed switches](https://www.sparkfun.com/products/8642) open or close when exposed to the presence of a magnetic field. These are great for making a non-contact switch.

[![Reed switches](https://cdn.sparkfun.com/r/600-600/assets/a/2/0/d/7/51818ba1ce395fab44000000.jpg)](https://cdn.sparkfun.com/assets/a/2/0/d/7/51818ba1ce395fab44000000.jpg)

*A couple of reed switches: [non-insulated](https://www.sparkfun.com/products/8642) (bottom) and [insulated](https://www.sparkfun.com/products/10601)*.

## Maintained Switches

A maintained switch retains its state until it's actuated into a new one. Just look to the nearest wall for an example of a maintained switch \-- the thing controlling your lights! Maintained switches are great for set-it-and-leave it applications like turning power on and off.

### Examples of Maintained Switches

#### Slide Switch

Need a really basic, no-frills ON/OFF or selector switch. Slide switches might be for you! These switches have a tiny little nub which protrudes from the switch, and it slides across the body into one of two (or more) positions.

You'll usually find slide switches in SPDT or DPDT configurations. The common terminal is usually in the middle, and the two select positions are on the outside.

[![Examples of slide switches](https://cdn.sparkfun.com/r/600-600/assets/a/1/e/f/b/5182bd5ece395fa91d000000.jpg)](https://cdn.sparkfun.com/assets/a/1/e/f/b/5182bd5ece395fa91d000000.jpg)

*Some examples of slide switches: a [mini PTH slide switch](https://www.sparkfun.com/products/102), an [SMD right-angle switch](https://www.sparkfun.com/products/10860), and an [SMD DPDT slide switch](https://www.sparkfun.com/products/597) mounted on a [LilyPad](https://www.sparkfun.com/products/9350).*

#### Toggle Switch

When you hear toggle switch, think "fire ze missiles!". Toggle switches have a long lever, which moves in a rocking motion. As they move to a new position, toggle switches make a really satisfying "snap".

[![Toggle switch covered](https://cdn.sparkfun.com/r/400-400/assets/a/2/0/9/e/517eee88ce395f521d000000.jpg)](https://cdn.sparkfun.com/assets/a/2/0/9/e/517eee88ce395f521d000000.jpg)

*[Missle-launch covers](https://www.sparkfun.com/products/9278) are a must when using [toggle switches](https://www.sparkfun.com/products/9276).*

Toggle switches are commonly [SPST](https://www.sparkfun.com/products/9276) (two terminals) or SPDT (three terminals), though you can find them in [other](https://www.sparkfun.com/products/11137) [flavors](https://www.sparkfun.com/products/11153) as well. As usual, you can find them in through-hole, surface-mount, or \-- probably most commonly \-- as panel-mountable.

#### DIP Switch

DIP switches are through-hole switches designed in the same mold as a through-hole DIP IC. They can be placed in a [breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard), in the same manner a through-hole IC might, by straddling the center area.

[![An 8-position DIP switch](https://cdn.sparkfun.com/r/300-300/assets/2/f/b/6/b/5182be69ce395ff81c000004.jpg)](https://www.sparkfun.com/products/8034)

*An [8-position DIP switch](https://www.sparkfun.com/products/8034), handy for configuring 8 somethings.*

These switches often come in arrays of eight or more separate SPST switches, with tiny little sliding levers. They were widely used in the olden days of computing, but they're still useful for configuring a devices via hardware.

#### Latching Buttons

Push-buttons aren\'t *all* momentary. [Some push-buttons](https://www.sparkfun.com/products/9808) will latch into place, maintaining their state until pressed again latching back to where the started. These can be found, for example, in stomp switches on guitar effect pedals.

[![Latching button](https://cdn.sparkfun.com/r/250-250/assets/e/0/e/2/f/517ef121ce395f701d000003.jpg)](https://www.sparkfun.com/products/9808)

#### Etc.

We\'ve barely started to cover the huge variety of maintained switches out there. There's [pull-chain switches](https://www.sparkfun.com/products/11136), which add a really classy touch to your project. [Key-switches](https://www.sparkfun.com/products/14947), for when you don't want just anybody turning on your killer robot. [Rotary switches](https://www.sparkfun.com/products/10064) \-- like those on a multimeter \-- provide a unique input device, especially when you've need a high number of throws.

[![Assorted maintained switches](https://cdn.sparkfun.com/r/600-600/assets/0/9/3/8/1/5182bf0ece395f7420000001.jpg)](https://cdn.sparkfun.com/assets/0/9/3/8/1/5182bf0ece395f7420000001.jpg)

And, of course, what mad scientist could live without a big ol' [knife-switch](http://www.youtube.com/watch?v=mOPTriLG5cU&feature=youtu.be&t=13s)?

## Switch Applications

### On/Off Control

Among the most obvious of switch applications is simple on and off control. The type of control you perform every time you walk into a dark room. An on/off switch can be implemented by simply sticking an SPST **switch in series** with a power-line. Usually the on/off switch will be maintained, like a toggle or slide switch, but momentary on/off switches can have their purpose.

[![Example on/off circuit](https://cdn.sparkfun.com/r/600-600/assets/6/5/f/1/0/5182b590ce395f7b1d000000.png)](https://cdn.sparkfun.com/assets/6/5/f/1/0/5182b590ce395f7b1d000000.png)

*On this [Breadboard Power Supply](https://www.sparkfun.com/products/114), an SPDT switch is used to turn the circuit on and off. (A second SPDT switch is used to select the adjustable voltage regulator\'s output value by adjusting a [voltage divider](https://learn.sparkfun.com/tutorials/voltage-dividers).)*

When implementing such a switch, keep in mind that all the current your project consumes is going to run through that switch. Ideally a switch is a perfect conductor, but realistically it\'s got a small amount of resistance between the two contacts. Because of that resistance, all switches are rated for a **maximum amount of current** they can withstand. Exceed a switch\'s maximum current rating, and you can expect melted plastic and magic smoke.

For example, this [SPDT slide switch](https://www.sparkfun.com/products/102) is great for controlling current flow in small projects (like [Simons](https://www.sparkfun.com/products/9276) or [Metronomes](https://www.sparkfun.com/products/9236)), but don\'t try using it to control beefy motor controllers, or strings of 100 LEDs. For that, consider using something like a [4A toggle switch](https://www.sparkfun.com/products/9276) or a [6A lamp switch](https://www.sparkfun.com/products/11477).

### User Input

Of course, user input is one of the more common applications for switches. For example, if you want to connect a switch to a microcontroller input pin, a simple circuit like this is all you\'d need:

[![Switch into MCU and a pull-up resistor](https://cdn.sparkfun.com/assets/f/c/2/6/c/5182b949ce395fbe1d000000.jpg)](https://cdn.sparkfun.com/assets/f/c/2/6/c/5182b949ce395fbe1d000000.jpg)

When the switch is open, the MCU pin is connected through the resistor to 5V. When the switch is closed, the pin is tied directly to GND. The resistor in that circuit is a [pull-up resistor](https://learn.sparkfun.com/tutorials/pull-up-resistors), required to bias the input high, and prevent a short to ground when the switch is closed.