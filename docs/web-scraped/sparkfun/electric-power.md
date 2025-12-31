# Source: https://learn.sparkfun.com/tutorials/electric-power

## With Great Power\... 

Why do we care about power? Power is the measurement of energy transfer over time, and energy costs money. Batteries aren't free, and neither is that stuff coming out of your electrical outlet. So, power measures how fast the pennies are draining out of your wallet!

Also, energy is\...energy. It comes in many, potentially harmful, forms \-- heat, radiation, sound, nuclear, etc. \-- ,and more power means more energy. So, it's important to have an idea of what kind of power you're working with when playing with electronics. Fortunately, in playing with [Arduinos](https://learn.sparkfun.com/tutorials/what-is-an-arduino), lighting up LEDs, and spinning small motors, losing track of how much power you\'re using only means smoking a resistor or melting an IC. Nevertheless, [Uncle Ben's advice](http://en.wikipedia.org/wiki/Uncle_Ben#.22With_great_power_comes_great_responsibility.22) doesn't just apply to superheros.

### Covered in this Tutorial

- The definition of power
- Examples of electric energy transfers
- Watts, the [SI unit](https://learn.sparkfun.com/tutorials/metric-prefixes-and-si-units) of power
- Calculating power using voltage, current, and resistance
- Maximum power ratings

### Suggested Reading

Power is one of the more fundamental concepts in electronics. But before learning about power, there might be some other tutorials you should read first. If you\'re not familiar with some these topics, consider checking out those tutorials first:

- [What is Electricity](https://learn.sparkfun.com/tutorials/what-is-electricity)
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
- [What is a Circuit](https://learn.sparkfun.com/tutorials/what-is-a-circuit)
- [How to use a Multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)

## What is Electric Power?

There are many types of power \-- physical, social, super, [odor blocking](http://www.youtube.com/watch?v=dTvtFp_iPKc), [love](http://www.youtube.com/watch?v=-NMph943tsw) \-- but in this tutorial, we'll be focusing on electric power. So what is electric power?

In general physics terms, *power* is defined as the **rate at which energy is transferred (or transformed)**.

So, first, what is energy and how is it transferred? It\'s hard to state simply, but energy is basically the ability of *something* to *move* something else. There are many forms of energy: mechanical, electrical, chemical, electromagnetic, thermal, and many others.

Energy can never be created or destroyed, only transferred to another form. A lot of what we\'re doing in electronics is converting different forms of energy to and from **electric energy**. Lighting LEDs turns electric energy into electromagnetic energy. Spinning motors turns electric energy into mechanical energy. Buzzing buzzers makes sound energy. Powering a circuit off a 9V alkaline battery turn chemical energy into electrical energy. All of these are forms of **energy transfers**.

  Energy type converted   Converted by
  ----------------------- ----------------
  Mechanical              Electric Motor
  Electromagnetic         LED
  Heat                    Resistor
  Chemical                Battery
  Wind                    Windmill

*Example electric components, which transfer electric energy to another form.*

Electric energy in particular, begins as electric *potential* energy \-- what we lovingly refer to as [voltage](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law/voltage). When [electrons flow](https://learn.sparkfun.com/tutorials/what-is-electricity/flowing-charges) through that potential energy, it turns into electric energy. In most useful circuits, that electric energy transforms into some other form of energy. Electric power is measured by combining both **how much** electric energy is transferred, and **how fast** that transfer happens.

### Producers and Consumers

Each component in a circuit either **consumes** or **produces** electric energy. A consumer transforms electric energy into another form. For example, when an LED lights up, electric energy is transformed into electromagnetic. In this case, the lightbulb **consumes** power. Electric power is **produced** when energy is transferred *to* electric from some other form. A battery supplying power to a circuit is an example of a **power producer**.

## Wattage

Energy is measured in terms of joules (J). Since power is a measure of energy over a set amount of time, we can measure it in **joules per second**. The SI unit for joules per second is the **watt** abbreviated as *W*.

[![watt = w = joule/second = j/s](https://cdn.sparkfun.com/assets/9/9/6/9/b/5182d5f5ce395f7932000000.png)](https://cdn.sparkfun.com/assets/9/9/6/9/b/5182d5f5ce395f7932000000.png)

It's very common to see \"watts\" preceded by one of the standard [SI prefixes](https://learn.sparkfun.com/tutorials/metric-prefixes-and-si-units): microwatts (µW), miliwatt (mW), kilowatt (kW), megawatt (MW), and [gigawatts](http://www.youtube.com/watch?v=iGlrobvb-ao) (GW), are all common depending on the situation.

  Prefix Name   Prefix Abbreviation   Weight
  ------------- --------------------- --------
  Nanowatt      nW                    10^-9^
  Microwatt     µW                    10^-6^
  Milliwatt     mW                    10^-3^
  Watt          W                     10^0^
  Kilowatt      kW                    10^3^
  Megawatt      MW                    10^6^
  Gigawatt      GW                    10^9^

\

Microcontrollers, like the [Arduino](https://learn.sparkfun.com/tutorials/what-is-an-arduino) will usually operate in the the µW or mW range. Laptop and desktop computers operate in the standard watt power range. Energy consumption of a house is usually in the kilowatt range. Large stadiums might operate at the megawatt scale. And gigawatts come into play for large-scale power stations and time machines.

## Calculating Power

Electric power is the rate at which energy is transferred. It's measured in terms of joules per second (J/s) \-- a watt (W). Given the few [basic electricity terms](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) we know, how could we calculate power in a circuit? Well, we've got a very standard measurement involving potential energy \-- volts (V) \-- which are defined in terms of joules per unit of charge (coulomb) (J/C). Current, another of our favorite electricity terms, measures charge flow over time in terms of the ampere (A) \-- coulombs per second (C/s). Put the two together and what do we get?! Power!

[![Deriving watts from volts and amps](https://cdn.sparkfun.com/r/600-600/assets/c/8/1/5/e/5182e262ce395f9032000002.png)](https://cdn.sparkfun.com/assets/c/8/1/5/e/5182e262ce395f9032000002.png)

To calculate the power of any particular component in a circuit, multiply the voltage drop across it by the current running through it.

[![P = VI](https://cdn.sparkfun.com/assets/9/1/a/a/e/5182e13cce395fd931000000.png)](https://cdn.sparkfun.com/assets/9/1/a/a/e/5182e13cce395fd931000000.png)

### For Example[]

Below is a simple (though not all that functional) circuit: a 9V battery connected across a 10Ω resistor.

[![Simple circuit: 9V battery connected to 10Ω resistor](https://cdn.sparkfun.com/r/500-500/assets/6/c/1/e/8/5182e3cece395f1b32000002.png)](https://cdn.sparkfun.com/assets/6/c/1/e/8/5182e3cece395f1b32000002.png)

How do we calculate the power across the resistor? First we have to find the current running through it. Easy enough\...[Ohm's law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law/ohms-law)!

[![I = V/R = 9/10 = 900mA](https://cdn.sparkfun.com/assets/1/9/b/5/d/5182ea5fce395fe331000000.png)](https://cdn.sparkfun.com/assets/1/9/b/5/d/5182ea5fce395fe331000000.png)

Alright, 900mA (0.9A) running through the resistor, and 9V across it. What kind of power is being applied to the resistor then?

[![P=IV=9\*.9=8.1W](https://cdn.sparkfun.com/assets/4/f/0/5/4/5182eab2ce395f4f32000006.png)](https://cdn.sparkfun.com/assets/4/f/0/5/4/5182eab2ce395f4f32000006.png)

A resistor transforms electric energy into heat. So this circuit transforms 8.1 joules of electric energy to heat every second.

### Calculating Power in Resistive Circuits

When it comes to calculating power in a purely resistive circuit, knowing two of three values (voltage, current, and/or resistance) is all you really need.

[![Power across a resistor example circuit](https://cdn.sparkfun.com/r/400-400/assets/b/6/f/1/3/51881353ce395f9f3c000000.png)](https://cdn.sparkfun.com/assets/b/6/f/1/3/51881353ce395f9f3c000000.png)

By plugging Ohm\'s law (V=IR or I=V/R) into our traditional power equation we can create two new equations. The first, purely in terms of voltage and resistance:

[![P=V\^2/R](https://cdn.sparkfun.com/assets/7/5/1/6/d/5182eb42ce395fca32000000.png)](https://cdn.sparkfun.com/assets/7/5/1/6/d/5182eb42ce395fca32000000.png)

So, in our previous example, 9V^2^/10Ω (V^2^/R) is 8.1W, and we never have to calculate the current running through the resistor.

A second power equation can be formed solely in terms of current and resistance:

[![P=I\^2\*R](https://cdn.sparkfun.com/assets/d/a/b/4/6/5182eb42ce395f6e32000000.png)](https://cdn.sparkfun.com/assets/d/a/b/4/6/5182eb42ce395f6e32000000.png)

------------------------------------------------------------------------

Why do we care about the power dropped on a resistor? Or any other component for that matter. Remember that power is the transfer of energy from one type to another. When that electrical energy running from the power source hits the resistor, the energy transforms into heat. Possibly more heat than the resistor can handle. Which leads us to\...power ratings.

## Power Ratings

All electronic components transfer energy from one type to another. Some energy transfers are desired: LEDs emitting light, motors spinning, batteries charging. Other energy transfers are undesirable, but also unavoidable. These unwanted energy transfers are **power losses**, which usually show up in the form of heat. Too much power loss \-- too much heat on a component \-- can become *very* undesirable.

Even when energy transfers are the main goal of a component, there'll still be losses to other forms of energy. LEDs and motors, for example, will still produce heat as a byproduct of their other energy transfers.

Most components have a rating for maximum power they can dissipate, and it's important to keep them operating under that value. This'll help you avoid what we lovingly refer to as "letting the magic smoke out".

### Resistor Power Ratings

Resistors are some of the more notorious culprits of power loss. When you drop some voltage across a resistor, you're also going to induce current flow across it. More voltage, means more current, means more power.

Remember back to our first [power-calculation example](calculating-power#ResistorPower), where we found that if 9V were dropped across a 10Ω resistor, that resistor would dissipate 8.1W. 8.1 is a *lot* of watts for most resistors. Most resistors are rated for anywhere from ⅛W (0.125W) to ½W (0.5W). If you drop 8W across a standard ½W resistor, ready a fire extinguisher.

[![1/2 and 1/4W resistors](https://cdn.sparkfun.com/assets/9/2/5/3/1/5182ed9ece395f9132000000.png)](https://cdn.sparkfun.com/assets/9/2/5/3/1/5182ed9ece395f9132000000.png)

*If you\'ve seen resistors before, you\'ve probably seen these. Top is a ½W resistor and below that a ¼W. These aren\'t built to dissipate very much power.*

There are resistors built to handle large power drops. These are specifically called out as **power resistors**.

[![Power resistors](https://cdn.sparkfun.com/r/600-600/assets/6/3/d/2/f/5182ece4ce395f3e32000001.jpg)](https://cdn.sparkfun.com/assets/6/3/d/2/f/5182ece4ce395f3e32000001.jpg)

*These large resistors are built to dissipate lots of power. From left to right: two 3W 22kΩ resistors, two 5W 0.1Ω resistors, and 25W 3Ω and 2Ω resistors.*

If you ever find yourself picking out a resistor value. Keep it's power rating in mind as well. And, unless your goal is to heat something up (heating elements are basically really high-power resistors), try to minimize power loss in a resistor.

#### For Example

Resistor power ratings can come into play when you're trying to decide on a value for an LED current-limiting resistor. Say, for example, you want to light up a [10mm super-bright red LED](https://www.sparkfun.com/products/8862) at maximum brightness, using a 9V battery.

[![Red LED lit up](https://cdn.sparkfun.com/r/300-300/assets/8/1/c/2/0/51842315ce395fd01b000002.jpg)](https://cdn.sparkfun.com/assets/8/1/c/2/0/51842315ce395fd01b000002.jpg)

That LED has a maximum forward current of 80mA, and a forward voltage of about 2.2V. So to deliver 80mA to the LED, you\'d need an 85Ω resistor to do so.

[![LED circuit with current-limiting resistor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/power_example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/power_example.png)

6.8V dropped on the resistor, and 80mA running through it means 0.544W (6.8V\*0.08A) of power lost on it. A half-watt resistor isn't going to like that very much! It probably won\'t melt, but it\'ll get **hot**. Play it safe and move up to a 1W resistor (or save power and use a dedicated LED driver).

------------------------------------------------------------------------

Resistors certainly aren\'t the only components where maximum power ratings must be considered. Any component with a resistive property to it is going to produce thermal power losses. Working with components that are commonly subjected to high power \-- voltage regulators, [diodes](https://learn.sparkfun.com/tutorials/diodes), amplifiers, and motor drivers, for example \-- means paying extra special attention to power loss and thermal stress.