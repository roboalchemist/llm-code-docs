# Source: https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc

## Thunderstruck!

[![alt text](https://cdn.sparkfun.com/assets/a/5/4/8/2/520d6a32757b7f6d708b4569.png)](https://cdn.sparkfun.com/assets/a/5/4/8/2/520d6a32757b7f6d708b4569.png)

Where did the Australian rock band AC/DC get their name from? Why, Alternating Current and Direct Current, of course! Both AC and DC describe types of current flow in a circuit. In **direct current** (DC), the electric charge (current) only flows in one direction. Electric charge in **alternating current** (AC), on the other hand, changes direction periodically. The voltage in AC circuits also periodically reverses because the current changes direction.

Most of the digital electronics that you build will use DC. However, it is important to understand some AC concepts. Most homes are wired for AC, so if you plan to connect your [Tardis music box project](https://learn.sparkfun.com/tutorials/mp3-player-shield-music-box) to an outlet, you will need to convert AC to DC. AC also has some useful properties, such as being able to convert voltage levels with a single component (a transformer), which is why AC was chosen as the primary means to transmit electricity over long distances.

### What You Will Learn

- The history behind AC and DC
- Different ways to generate AC and DC
- Some examples of AC and DC applications

### Recommended Reading

- [What is Electricity](https://learn.sparkfun.com/tutorials/what-is-electricity)
- [What is a Circuit?](https://learn.sparkfun.com/tutorials/what-is-a-circuit)
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
- [Electric Power](https://learn.sparkfun.com/tutorials/electric-power)

 

![AC vs DC](https://info.sparkfun.com/hubfs/Poster%20Downloads/ac_dc_thumbnail.png)

 

## Alternating Current (AC)

Alternating current describes the flow of charge that changes direction periodically. As a result, the voltage level also reverses along with the current. AC is used to deliver power to houses, office buildings, etc.

### Generating AC

AC can be produced using a device called an alternator. This device is a special type of electrical generator designed to produce alternating current.

A loop of wire is spun inside of a magnetic field, which induces a current along the wire. The rotation of the wire can come from any number of means: a wind turbine, a steam turbine, flowing water, and so on. Because the wire spins and enters a different magnetic polarity periodically, the voltage and current alternates on the wire. Here is a short animation showing this principle:

\

*(Video credit: Khurram Tanvir)*

Generating AC can be compared to our [previous water analogy](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law/voltage):

[![alt text](https://cdn.sparkfun.com/assets/a/0/7/b/a/522783e0757b7fc2168b4567.gif)](https://cdn.sparkfun.com/assets/a/0/7/b/a/522783e0757b7fc2168b4567.gif)

To generate AC in a set of water pipes, we connect a mechanical crank to a piston that moves water in the pipes back and forth (our \"alternating\" current). Notice that the pinched section of pipe still provides [resistance](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law/resistance) to the flow of water regardless of the direction of flow.

### Waveforms

AC can come in a number of forms, as long as the voltage and current are alternating. If we hook up an oscilloscope to a circuit with AC and plot its voltage over time, we might see a number of different waveforms. The most common type of AC is the sine wave. The AC in most homes and offices have an oscillating voltage that produces a sine wave.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/b/7/3/d/a/521e6ed1757b7fcc778b456a.png)](https://cdn.sparkfun.com/assets/b/7/3/d/a/521e6ed1757b7fcc778b456a.png)

Other common forms of AC include the square wave and the triangle wave:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/0/2/0/3/d/521e6ed1757b7fa1778b4567.png)](https://cdn.sparkfun.com/assets/0/2/0/3/d/521e6ed1757b7fa1778b4567.png)

Square waves are often used in digital and switching electronics to test their operation.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/f/e/f/f/6/521e6ed1757b7fc6778b4567.png)](https://cdn.sparkfun.com/assets/f/e/f/f/6/521e6ed1757b7fc6778b4567.png)

Triangle waves are found in sound synthesis and are useful for testing linear electronics like amplifiers.

![](https://cdn.sparkfun.com/assets/home_page_posts/3/1/9/0/collage-of-product.jpg)

## Expecting a Pay Wall? 

### Not Our Style. 

### Describing a Sine Wave

We often want to describe an AC waveform in mathematical terms. For this example, we will use the common sine wave. There are three parts to a sine wave: *amplitude, frequency, and phase.*

Looking at just voltage, we can describe a sine wave as the mathematical function:

[![alt text](https://cdn.sparkfun.com/assets/5/f/f/0/6/521e33e5757b7fe71d8b456d.gif)](https://cdn.sparkfun.com/assets/5/f/f/0/6/521e33e5757b7fe71d8b456d.gif)

***V(t)*** is our voltage as a function of time, which means that our voltage changes as time changes. The equation to the right of the equals sign describes how the voltage changes over time.

***V~P~*** is the *amplitude*. This describes the maximum voltage that our sine wave can reach in either direction, meaning that our voltage can be +V~P~ volts, -V~P~ volts, or somewhere in between.

The **sin()** function indicates that our voltage will be in the form of a periodic sine wave, which is a smooth oscillation around 0V.

***2π*** is a constant that converts the freqency from cycles (in hertz) to [angular frequnecy](http://en.wikipedia.org/wiki/Angular_frequency) (radians per second).

***f*** describes the *frequency* of the sine wave. This is given in the form of *hertz* or *units per second*. The frequency tells how many times a particular wave form (in this case, one cycle of our sine wave - a rise and a fall) occurs within one second.

***t*** is our independent variable: time (measured in seconds). As time varies, our waveform varies.

***φ*** describes the *phase* of the sine wave. Phase is a measure of how shifted the waveform is with respect to time. It is often given as a number between 0 and 360 and measured in degrees. Because of the periodic nature of the sine wave, if the wave form is shifted by 360° it becomes the same waveform again, as if it was shifted by 0°. For simplicity, we sill assume that phase is 0° for the rest of this tutorial.

We can turn to our trusty outlet for a good example of how an AC waveform works. In the United States, the power provided to our homes is AC with about 170V zero-to-peak (amplitude) and 60Hz (frequency). We can plug these numbers into our formula to get the equation (remember that we are assuming our phase is 0):

[![AC equation](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/5/AC_eqn.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/5/AC_eqn.gif)

We can use our handy graphing calculator to graph this equation. If no graphing calculator is available we can use a free online graphing program like [Desmos](https://www.desmos.com/calculator) (Note that you might have to use \'y\' instead of \'v\' in the equation to see the graph).

[![AC_sinewave](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/5/AC_sinewave_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/5/AC_sinewave_1.png)

Notice that, as we predicted, the voltage rise up to 170V and down to -170V periodically. Additionally, 60 cycles of the sine wave occurs every second. If we were to measure the voltage in our outlets with an oscilloscope, this is what we would see (**WARNING:** do not attempt to measure the voltage in an outlet with an oscilloscope! This will likely damage the equipment).

**NOTE:** You might have heard that AC voltage in the US is 120V. This is also correct. How? When talking about AC (since the voltage changes constantly), it is often easier to use an average or mean. To accomplish that, we use a method called [\"Root mean squared.\"](http://en.wikipedia.org/wiki/Root_mean_square) (RMS). It is often helpful to use the RMS value for AC when you want to calculate [electrical power](https://learn.sparkfun.com/tutorials/electric-power). Even though, in our example, we had the voltage varying from -170V to 170V, the root mean square is 120V RMS.

### Applications

Home and office outlets are almost always AC. This is because generating and transporting AC across long distances is relatively easy. At high voltages (over 110kV), less energy is lost in electrical power transmission. Higher voltages mean lower currents, and lower currents mean less [heat generated](https://learn.sparkfun.com/tutorials/electric-power/calculating-power) in the power line due to resistance. AC can be converted to and from high voltages easily using transformers.

AC is also capable of powering electric motors. Motors and generators are the exact same device, but motors convert electrical energy into mechanical energy (if the shaft on a motor is spun, a voltage is generated at the terminals!). This is useful for many large appliances like dishwashers, refrigerators, and so on, which run on AC.

## Direct Current (DC)

Direct current is a bit easier to understand than alternating current. Rather than oscillating back and forth, DC provides a constant voltage or current.

### Generating DC

DC can be generated in a number of ways:

- An AC generator equipped with a device called a [\"commutator\"](http://en.wikipedia.org/wiki/Commutator_(electric)) can produce direct current
- Use of a device called a [\"rectifier\"](http://en.wikipedia.org/wiki/Rectifier) that converts AC to DC
- [Batteries](https://learn.sparkfun.com/tutorials/battery-technologies) provide DC, which is generated from a chemical reaction inside of the battery

Using our water analogy again, DC is similar to a tank of water with a hose at the end.

[![alt text](https://cdn.sparkfun.com/assets/6/3/9/5/e/521f92ee757b7fbe778b456c.png)](https://cdn.sparkfun.com/assets/6/3/9/5/e/521f92ee757b7fbe778b456c.png)

The tank can only push water one way: out the hose. Similar to our DC-producing battery, once the tank is empty, water no longer flows through the pipes.

### Describing DC

DC is defined as the \"unidirectional\" flow of current; current only flows in one direction. Voltage and current can vary over time so long as the direction of flow does not change. To simplify things, we will assume that voltage is a constant. For example, we assume that a AA battery provides 1.5V, which can be described in mathematical terms as:

[![alt text](https://cdn.sparkfun.com/assets/e/6/d/b/5/5220b8cc757b7f8b2a8b4567.gif)](https://cdn.sparkfun.com/assets/e/6/d/b/5/5220b8cc757b7f8b2a8b4567.gif)

If we plot this over time, we see a constant voltage:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/d/9/f/7/e/5220ba6b757b7fff2a8b4568.png)](https://cdn.sparkfun.com/assets/d/9/f/7/e/5220ba6b757b7fff2a8b4568.png)

What does this mean? It means that we can count on most DC sources to provide a constant voltage over time. In reality, a battery will slowly lose its charge, meaning that the voltage will drop as the battery is used. For most purposes, we can assume that the voltage is constant.

### Applications

Almost all electronics projects and parts for sale on SparkFun run on DC. Everything that runs off of a battery, plugs in to the wall with an [AC adapter](https://en.wikipedia.org/wiki/AC_adapter), or uses a USB cable for power relies on DC. Examples of DC electronics include:

- Cell phones
- The LilyPad-based [D&D Dice Gauntlet](https://learn.sparkfun.com/tutorials/dungeons-and-dragons-dice-gauntlet)
- Flat-screen TVs (AC goes into the TV, which is converted to DC)
- Flashlights
- Hybrid and electric vehicles

## Battle of the Currents

Almost every home and business is wired for AC. However, this was not an overnight decision. In the late 1880s, a variety of inventions across the United States and Europe led to a full-scale battle between alternating current and direct current distribution.

In 1886, Ganz Works, an electric company located in Budapest, electrified all of Rome with AC. Thomas Edison, on the other hand, had constructed 121 DC power stations in the United States by 1887. A turning point in the battle came when George Westinghouse, a famous industrialist from Pittsburgh, purchased Nikola Tesla\'s patents for AC motors and transmission the next year.

### AC vs. DC

[![Edison](https://cdn.sparkfun.com/assets/8/d/4/a/3/5226182b757b7f67228b4568.jpg)](https://cdn.sparkfun.com/assets/8/d/4/a/3/5226182b757b7f67228b4568.jpg)

*Thomas Edison (Image courtesy of [biography.com](http://www.biography.com/people/thomas-edison-9284349))*

\

In the late 1800s, DC could not be easily converted to high voltages. As a result, Edison proposed a system of small, local power plants that would power individual neighborhoods or city sections. Power was distributed using three wires from the power plant: +110 volts, 0 volts, and -110 volts. Lights and motors could be connected between either the +110V or 110V socket and 0V (neutral). 110V allowed for some voltage drop between the plant and the load (home, office, etc.).

Even though the voltage drop across the power lines was accounted for, power plants needed to be located within 1 mile of the end user. This limitation made power distribution in rural areas extremely difficult, if not impossible.

\

  ----------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------
  ![Tesla](https://cdn.sparkfun.com/assets/d/1/6/b/8/5226182b757b7ff95f8b4568.jpeg)                           ![Westinghouse](https://cdn.sparkfun.com/assets/f/8/a/8/7/5226137a757b7f995e8b4568.jpg)
  Nikola Tesla (Image courtesy of [wikipedia.org](http://en.wikipedia.org/wiki/File:Tesla_circa_1890.jpeg))   George Westinghouse (Image courtesy of [pbs.org](http://www.pbs.org/tesla/ll/wc_west_pop.html))
  ----------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------

\

With Tesla\'s patents, Westinghouse worked to perfect the AC distribution system. Transformers provided an inexpensive method to step up the voltage of AC to several thousand volts and back down to usable levels. At higher voltages, the same power could be transmitted at much lower current, which meant less power lost due to resistance in the wires. As a result, large power plants could be located many miles away and service a greater number of people and buildings.

### Edison\'s Smear Campaign

Over the next few years, Edison ran a campaign to highly discourage the use of AC in the United States, which included lobbying state legislatures and spreading disinformation about AC. Edison also directed several technicians to publicly electrocute animals with AC in an attempt to show that AC was more dangerous than DC. In attempt to display these dangers, Harold P. Brown and Arthur Kennelly, employees of Edison, designed the first electric chair for the state of New York using AC.

### The Rise of AC

In 1891, the International Electro-Technical Exhibition was held in Frankfurt, Germany and displayed the first long distance transmission of three-phase AC, which powered lights and motors at the exhibition. Several representatives from what would become General Electric were present and were subsequently impressed by the display. The following year, General Electric formed and began to invest in AC technology.

[![alt text](https://cdn.sparkfun.com/assets/e/3/b/3/0/52264ad0757b7f1b5f8b456a.jpg)](https://cdn.sparkfun.com/assets/e/3/b/3/0/52264ad0757b7f1b5f8b456a.jpg)

*Edward Dean Adams Power Plant at Niagara Falls, 1896 (Image courtesy of [teslasociety.com](http://www.teslasociety.com/exhibition.htm))*

Westinghouse won a contract in 1893 to build a hydroelectric dam to harness the power of Niagara falls and transmit AC to Buffalo, NY. The project was completed on November 16, 1896 and AC power began to power industries in Buffalo. This milestone marked the decline of DC in the United States. While Europe would adopt an AC standard of 220-240 volts at 50 Hz, the standard in North America would become 120 volts at 60 Hz.

### High-Voltage Direct Current (HVDC)

Swiss engineer René Thury used a series of motor-generators to create a high-voltage DC system in the 1880s, which could be used to transmit DC power over long distances. However, due to the high cost and maintenance of the Thury systems, HVDC was never adopted for almost a century.

With the invention of semiconductor electronics in the 1970s, economically transforming between AC and DC became possible. Specialized equipment could be used to generate high voltage DC power (some reaching 800 kV). Parts of Europe have begun to employ HVDC lines to electrically connect various countries.

HVDC lines experience less loss than equivalent AC lines over extremely long distances. Additionally, HVDC allows different AC systems (e.g. 50 Hz and 60 Hz) to be connected. Despite its advantages, HVDC systems are more costly and less reliable than the common AC systems.

In the end, Edison, Tesla, and Westinghouse may have their wishes come true. AC and DC can coexist and each serve a purpose.