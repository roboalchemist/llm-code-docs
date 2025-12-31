# Source: https://learn.sparkfun.com/tutorials/polarity

## What is Polarity?

In the realm of electronics, **polarity** indicates whether a circuit component is **symmetric** or not. A non-polarized component \-- a part *without* polarity \-- can be connected in any direction and still function the way it\'s supposed to function. A symmetric component rarely has more than two terminals, and every terminal on the component is equivalent. You can connect a non-polarized component in any direction, and it\'ll function just the same.

A **polarized** component \-- a part *with* polarity \-- can only be connected to a circuit in one direction. A polarized component might have two, twenty, or even two-hundred pins, and each one has a unique function and/or position. If a polarized component was connected to a circuit incorrectly, at best it won\'t work as intended. At worst, an incorrectly connected polarized component will smoke, spark, and be one very dead part.

[![Examples of Polarized Components](https://cdn.sparkfun.com/r/600-600/assets/5/4/1/e/0/5193d2adce395f3d7a000001.jpg)](https://cdn.sparkfun.com/assets/5/4/1/e/0/5193d2adce395f3d7a000001.jpg)

*An assortment of polarized components: batteries, integrated circuits, transistors, voltage regulators, electrolytic capacitors, and diodes, among others.*

Polarity is a very important concept, especially when it comes to physically building circuits. Whether you\'re plugging parts into a breadboard, soldering them to a PCB, or sewing them into an e-textile project, it\'s critical to be able to identify polarized components and to connect them in the correct direction. So that\'s what we\'re here for! In this tutorial we\'ll discuss which components do and don\'t have polarity, how to identify component polarity, and how to test some components for polarity.

### Consider Reading

If your head\'s not swimming yet, it\'s probably safe to read through the rest of this tutorial. Polarity is a concept which builds on some lower-level electronics concepts and reinforces a few others. If you haven\'t already, consider checking out some of the below tutorials, before you read through this one.

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)

### How to Use a Multimeter 

Learn the basics of using a multimeter to measure continuity, voltage, resistance and current.

## Diode and LED Polarity

**Note:** We will be referring to the flow of current that is relative to the positive charges (i.e. [conventional current](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law#current)) in a circuit.

[Diodes](https://learn.sparkfun.com/tutorials/diodes) only allow current to flow in one direction, and they\'re *always* polarized. A diode has two terminals. The positive side is called the *anode*, and the negative one is called the *cathode*.

[![Diode circuit symbol, with anode/cathode labeled](https://cdn.sparkfun.com/assets/learn_tutorials/7/5/backwardsDiode.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/5/backwardsDiode.png)

*The diode circuit symbol, with the anode and cathode marked.*

Current through a diode can only flow from the anode to the cathode, which would explain why it\'s important for a diode to be connected in the correct direction. Physically, every diode should have some sort of indication for either the anode or cathode pin. Usually the diode will have a **line near the cathode pin**, which matches the vertical line in the diode circuit symbol.

Below are a few examples of diodes. The top diode, a [1N4001](http://www.sparkfun.com/products/8589) rectifier, has a grey ring near the cathode. Below that, a [1N4148](http://www.sparkfun.com/products/8588) signal diode uses a black ring to mark the cathode. At the bottom are a couple surface mount diodes, each of which use a line to mark which pin is the cathode.

[![Some real diodes and their cathode markings](https://cdn.sparkfun.com/assets/1/e/8/1/4/518aca69ce395f6437000002.png)](https://cdn.sparkfun.com/assets/1/e/8/1/4/518aca69ce395f6437000002.png)

*Notice the lines on each device, denoting the Cathode side, which match the line in the symbol above.*

### LEDs

LED stands for [light-emitting *diode*](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds), which means that much like their diode cousins, they\'re polarized. There are a handful of identifiers for finding the positive and negative pins on an LED. You can try to find the **longer leg**, which should indicate the positive, anode pin.

Or, if someone\'s trimmed the legs, try finding the flat edge on the LED\'s outer casing. The pin nearest the **flat edge** will be the negative, cathode pin.

[![LED polarity indicators](https://cdn.sparkfun.com/assets/0/c/5/d/a/518d2d78ce395f2675000000.png)](https://cdn.sparkfun.com/assets/0/c/5/d/a/518d2d78ce395f2675000000.png)

There might be other indicators as well. SMD diodes have a range of anode/cathode identifiers. Sometimes it\'s easiest to just use a [multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter) to test for polarity. Turn the multimeter to the diode setting (usually indicated by a diode symbol), and touch each probe to one of the LED terminals. If the LED lights up, the positive probe is touching the anode, and the negative probe is touching the cathode. If it doesn\'t light up, try swapping the probes around.

[![LED polarity test with multimeter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/5/GreyMultimeterLED.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/5/GreyMultimeterLED.png)

*The polarity of a tiny, yellow, surface-mount LED is tested with a multimeter. If the positive lead touches the anode and negative touches the cathode, the LED should light up.*

------------------------------------------------------------------------

Diodes certainly aren't the only polarized component. There are tons of parts out there that won't work if connected incorrectly. Next we'll discuss some of the other common polarized components, beginning with integrated circuits.

## Integrated Circuit Polarity

Integrated circuits (ICs) might have eight pins or eighty pins, and each pin on an IC has a unique function and position. It\'s very important to keep polarity straight with ICs. There\'s a good chance they\'ll smoke, melt, and be ruined if connected incorrectly.

Through-hole ICs usually come in a dual-inline package (DIP) \-- two rows of pins, each spaced by 0.1\" wide enough to straddle the center of a breadboard. DIP ICs usually have a **notch** to indicate which of the many pins is the first. If not a notch, the IC might have an etched **dot** in the casing near pin 1.

[![IC Polarity Labeled](https://cdn.sparkfun.com/assets/3/2/3/3/b/51b8cd4cce395f5b4d000002.png)](https://cdn.sparkfun.com/assets/3/2/3/3/b/51b8cd4cce395f5b4d000002.png)

*An IC with both a dot and a notch to indicate polarity. Sometimes you get both, sometimes you only get one or the other.*

For all IC packages, pin numbers increase sequentially as you move counter-clockwise away from pin 1.

[![MCP3002 pin-numbering](https://cdn.sparkfun.com/r/300-300/assets/7/0/7/6/0/518ad5ebce395f2138000002.png)](https://cdn.sparkfun.com/assets/7/0/7/6/0/518ad5ebce395f2138000002.png)

Surface-mount ICs might come in QFN, SOIC, SSOP, or a number of other form-factors. These ICs will usually have a **dot** near pin 1.

[![ATmega32U4](https://cdn.sparkfun.com/r/600-600/assets/3/5/4/1/8/518ad8c5ce395fca37000003.png)](https://cdn.sparkfun.com/assets/3/5/4/1/8/518ad8c5ce395fca37000003.png)

*An [ATmega32U4](https://www.sparkfun.com/products/11181) in a TQFP package, next to the datasheet pinout.*

## Electrolytic Capacitors

Not all [capacitors](https://learn.sparkfun.com/tutorials/capacitors) are polarized, but when they are, it\'s *very* important not to mix their polarity up.

Ceramic capacitors \-- the small (1µF and less), commonly yellow guys \-- are **not** polarized. You can stick those in either way.

[![Ceramic caps \-- NOT polarized](https://cdn.sparkfun.com/r/400-400/assets/0/c/8/a/d/518bd819ce395f174f000000.png)](https://cdn.sparkfun.com/assets/0/c/8/a/d/518bd819ce395f174f000000.png)

*[Through-hole](https://www.sparkfun.com/products/8375) and [SMD](https://www.sparkfun.com/products/11245) 0.1µF ceramic capacitors. These are NOT polarized.*

Electrolytic caps ([they\'ve got electrolytes](http://www.youtube.com/watch?v=-Vw2CrY9Igs)), which look like little tin cans, **are polarized**. The negative pin of the cap is usually indicated by a **\"-\" marking**, and/or a **colored strip** along the can. They might also have a **longer positive leg**.

Below are [10µF](https://www.sparkfun.com/products/523) (left) and a [1mF](https://www.sparkfun.com/products/8982) electrolytic capacitors, each of which has a dash symbol to mark the negative leg, as well as a longer positive leg.

[![Electrolytic Capacitors](https://cdn.sparkfun.com/r/600-600/assets/9/4/2/8/8/518d258ace395f9a51000000.png)](https://cdn.sparkfun.com/assets/9/4/2/8/8/518d258ace395f9a51000000.png)

Applying a negative voltage for an extended period to an electrolytic capacitor results in a briefly exciting, but catastrophic, failure. They\'ll make a *pop*, and the top of the cap will either swell or burst open. From then on the cap will be as good as dead, acting like a short circuit.

## Other Polarized Components

### Batteries and Power Supplies

Getting polarity right in your circuit all starts and ends with getting the [power supply](https://learn.sparkfun.com/tutorials/how-to-power-a-project) connected correctly. Whether you\'re project\'s getting power from a [wall-wart](https://www.sparkfun.com/products/298) or a [LiPo battery](../battery-technologies/lithium-polymer), it\'s critical to make sure you don\'t accidently connect them backwards and apply **-**9V or **-**4.2V to your project accidently.

Anyone that\'s ever replaced batteries knows how to find their polarity. Most batteries will indicate the positive and negative terminals with a \"+\" or \"-\" symbol. Other times it might be red wire for positive and a black wire for negative.

[![Assorted batteries, each have some way to identify polarity](https://cdn.sparkfun.com/r/600-600/assets/b/3/0/7/7/518bc702ce395fb64e000000.jpg)](https://cdn.sparkfun.com/assets/b/3/0/7/7/518bc702ce395fb64e000000.jpg)

*An assortment of batteries. [Lithium polymer](../battery-technologies/lithium-polymer), [coin cell](../battery-technologies/coin-cell), [9V alkaline](../battery-technologies/alkaline), [AA alkaline](../battery-technologies/alkaline), and [AA NiMH](../battery-technologies/nickel-metal-hydride). Each has some way to represent positive or negative terminals.*

Power supplies usually have a standardized [connector](https://learn.sparkfun.com/tutorials/connector-basics), which should usually have polarity itself. A [barrel jack](https://www.sparkfun.com/products/119), for example, has two conductors: outer and inner; the inner/center conductor is usually the positive terminal. Other connectors, like a [JST](https://www.sparkfun.com/products/8613), are **keyed** so you just can\'t connect them backwards.

[![Power supply connector](https://cdn.sparkfun.com/assets/e/3/b/a/3/518bce4ece395f374f000000.jpg)](https://cdn.sparkfun.com/assets/e/3/b/a/3/518bce4ece395f374f000000.jpg)

For extra protection against reversing power supply polarity, you can add [reverse polarity protection](https://learn.sparkfun.com/tutorials/diodes#reversePolarity) using a diode, or a MOSFET.

### Transistors, MOSFETs, and Voltage Regulators

These (traditionally) three-terminal, polarized components are lumped together because they share similar package types. Through-hole [transistors](https://learn.sparkfun.com/tutorials/transistors), MOSFETs, and voltage regulators commonly come in a TO-92 or TO-220 package, seen below. To find which pin is which, look for the flat edge on the TO-92 package or the metal heatsink on the TO-220, and match that up to the pin-out in the datasheet.

[![TO-92 transistor and TO-220 Vreg](https://cdn.sparkfun.com/assets/9/4/3/4/1/518d2bfdce395fa672000000.png)](https://cdn.sparkfun.com/assets/9/4/3/4/1/518d2bfdce395fa672000000.png)

*Above, a [2N3904 transistor](https://www.sparkfun.com/products/521) in a TO-92 package, note the curved and straight edges. A [3.3V regulator](https://www.sparkfun.com/products/526) in a TO-220 package, note the metal heatsink on the back.*

### Etc.

This is just the tip of the polarized-component iceberg. Even non-polarized components, like [resistors](https://learn.sparkfun.com/tutorials/resistors), can come in polarized packages. A resistor pack \-- a grouping of five-or-so pre-arranged resistors \-- is one such example.

[![Resistor pack](https://cdn.sparkfun.com/r/600-600/assets/7/c/b/8/4/518d2c93ce395f0e73000000.png)](https://cdn.sparkfun.com/assets/7/c/b/8/4/518d2c93ce395f0e73000000.png)

*A polarized resistor pack. An [array of five 330Ω resistors](https://www.sparkfun.com/products/10855), all tied together at one end. The dot represents the first, common pin.*

Fortunately, every polarized component should have some way to inform you which pin is which. Be sure to always **read the datasheets**, and check the case for dots or other markers.