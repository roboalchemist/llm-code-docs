# Source: https://learn.sparkfun.com/tutorials/understanding-thermal-resistance

## Introduction

When working with low power devices, thermal management isn't much of an issue. Once you start adding motors, LED strips, and the current draw of the project goes up, parts can start to get hot. If you don't manage the heat, parts can overheat, shortening the life of the component. In this tutorial we'll cover what thermal resistance is, how it's used for thermal management, and how to maximize the life of your project.

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)

### How to Use a Multimeter 

Learn the basics of using a multimeter to measure continuity, voltage, resistance and current.

## Thermal Resistance

To understand how power losses affect the heat generated, you first need to understand Thermal Resistance (R~θ~). Similar to how electrical resistance resists the flow of current in ohms, thermal resistance resists the flow of heat in Kelvins per watt, or in degrees Celsius per watt. We can use thermal resistance to estimate how hot a particular part might get under various loads based on how easily the heat is able to be transfered from one place to another. For electronics the heat starts at the source, such as a semiconductor junction, and spreads to be eventually dissipated to ambient air.

If the junction of a semiconductor exceeds its maximum temperature it will break and let all the magic smoke out. To make sure we don\'t do that, we need to look at how efficiently the device is able to use the power\.....

### Ohm's Law and Thermal Resistance

We can use ohm's law to calculate the temperatures from the heatsink to the junction, and everywhere in between using Ohm's Law. As mentioned earlier, electrical resistance is very similar to thermal resistance. We can use Ohm's Law which states that V = I\*R, and replace the voltage for temperature (T) and current for power (P), which gives us:

[![Thermal version of Ohm\'s Law](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/ThermalOhmsLaw.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/ThermalOhmsLaw.gif)

The equivalent thermal circuit is shown below where:

- **T_Junction (T~J~):** the junction temperature
- **R~θJC~:**the junction to case thermal resistance
- **T_Case (T~C~):** the junction temperature
- **R~θCH~:** the case to heatsink thermal resistance
- **T_Heatsink (T~H~):** the heatsink temperature
- **R~θHA~:** the heatsink to ambient air thermal resistance
- **T_Ambient (T~A~):** the ambient air temperature

[![Thermal Circuit Schematic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/3/Thermal_Resistance_Schematic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Thermal_Resistance_Schematic.jpg)

To better understand how thermal resistance is used, lets look at the following example:

- **Power dissipated:** 2W
- **R~θJC~** = 4°C/W
- **R~θCH~** = 0.25°C/W
- **R~θHA~** = 6°C/W
- **T~A~** = 25°C

Starting with the thermal equivalent of Ohm\'s Law:

[![Thermal version of Ohm\'s Law](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/ThermalOhmsLaw.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/ThermalOhmsLaw.gif)

We want to solve for our junction temperature rise , so T becomes T~J~. Our power dissipated, P, is 2W. And our thermal resistances are in series, so just like resistors in series in a circuit we can add the values together:

[![Thermal version of Ohm\'s Law](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/SolveThermalOhmsLaw.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/SolveThermalOhmsLaw.gif)

The junction temperature is 20.5°C above ambient temperature (25°C in this case), which means the absolute temperature is 20.5°C + 25°C, which would be 45.5°C.

Where do you find the thermal resistance values? For parts like voltage regulators, diodes, transistors, and other semiconductors, the datasheet will have a section for the thermal information, mainly the Junction to Air (R~θJA~) if some type of heatsink weren\'t used, or Junction to Case (R~θJC~) if a heatsink was going to be used, which would have its own thermal resistance and is covered in the next section. The typical thermal resistance data would look similar to the image below.

[![Thermal Resistance in a Datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Datasheet_Thermal_Resistance.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Datasheet_Thermal_Resistance.jpg)

## How to Transfer Heat

### Metal Fin Heatsinks

[![Photo of a heatsink](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Heatsink.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Heatsink.jpg)

Heatsinks some in all shapes and sizes, with a single purpose: transfer heat to the air. The purpose of each of the fins on a heatsink is to create as much surface area as possible for the air to interact with and pull heat away from the heatsink, which helps to pull heat away from the semiconductor's junction. The thermal resistance of a heatsink can be a bit complicated though because a metal fin heatsink performs at different rates based on the amount of air flowing past the fins. A typical datasheet for a heatsink provides not only the dimensions of the part, but the thermal characteristics as well, which looks like this:

[![Typical thermal characteristics of a heatsink](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Highlighted_Heatsink_Graph.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Highlighted_Heatsink_Graph.jpg)

The arrows on each plot line correspond to the axis they represent. For example, the red highlight shows that in free air (ie without a fan), dissipating 10W of power would raise the temperature of heatsink around 78°C above ambient temperature. If instead you had around 400ft/min of air flowing along the fins of the heatsink, the green line shows the heatsink would have a thermal resistance of around 1.8°C/W, or 18°C above ambient temperature dissipating the same 10W of power.

### Vias

If you need to add a heatsink to the design, designs like switch mode power supplies where it's important to keep components as close to the IC as possible, vias can not only transfer signals from one side of the PCB to the other, but they can transfer heat too!

If you don't feel like doing a bunch of math, the [PCB Toolkit from Saturn PCB Design Inc](https://saturnpcb.com/pcb_toolkit/) has a lot of great tools to solve a ton of the equations an electrical engineer might use. One of the tabs in particular is for via properties:

[![Photo of PCB Toolkit from Saturn PCB Design Inc](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/3/Saturn_PCB_Toolkit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Saturn_PCB_Toolkit.jpg)

Image courtesy of [SaturnPCB](https://saturnpcb.com/pcb_toolkit/)

To get the thermal resistance of the vias, I entered in the boxes I highlighted red the properties of the PCB I have. Setting the layer set to 2 layer, and the via hole diameter should be the only setting you might need to change. The via plating thickness and via height are pretty standard for most PCBs. After clicking solve, in the blue box in the bottom right corner I got the thermal resistance which was 179.3°C/W per via. With 10 vias, the via thermal resistance drops down to 17.9°C/W. If you were going to calculate the junction temperature now, you would add another thermal resistance in series for the vias, which would be added with the other thermal resistances when you do the calculation.

### PCB Heatsinking

When it comes to transferring heat in a PCB, the math can get complicated pretty quickly, which is one of the reasons why for via thermal resistance, using the tool from Saturn PCB is the easier way to go. Even more complicated is using a PCB as a heatsink. There's the thermal resistance not only of the copper, which is a function of the surface area, but the solder mask, substrate material, which also transfers heat to surrounding isolated copper planes. For a thorough explanation, you can read this [application report from Texas Instruments](http://www.ti.com/lit/an/snva419c/snva419c.pdf). For easier to digest information, Paul Bryson has a great blog post on the subject and provides some great tips and findings which can be found [here](http://www.brysonics.com/pcb-thermal-resistance-some-unexpected-results/).

For a **rough** guide you can use the graph from Paul Bryson\'s post below:

[![PCB Thermal Resistance Graph](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/PCB_Thermal_Resistance.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/PCB_Thermal_Resistance.jpg)

Image courtesy of Paul Bryson of [brysonics.com](http://www.brysonics.com/)

## Example: PTH Linear Regulator

Let's see how well the thermal resistance calculations work in the real world. For these examples I'm going to use two different kinds of voltage regulators, a linear regulator, specifically the [LM7805](https://www.sparkfun.com/products/107), as well as a [DC-DC converter](https://www.sparkfun.com/products/15208). We'll see how well they stand up to the numbers we get from the datasheets.

## Linear Regulator

Having a low cost and low noise voltage regulator, how can you go wrong? Linear regulators are a great choice for many applications, but where they fall short is their efficiency. We can see the basic design of a linear regulator below:

[![Linear Regulator Schematic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/3/Linear_Regulator_Schematic.gif)](https://cdn.sparkfun.comr/600-600//assets/learn_tutorials/1/1/8/3/Linear_Regulator_Schematic.gif)

Image courtesy of [EE Times](https://www.eetimes.com/signal-chain-basics-part-19-exploring-and-understanding-linear-voltage-regulators/)

To determine how hot a linear regulator will get, let's start with the understanding that the input power must equal the output power. Ideally, the system would be 100% efficient, but in the real world there are going to be some losses, and that power loss is dissipated in the form of heat (P~D~). This can be expressed as the following formula:

[![Calculating Pin as Pout plus Pdissipated](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg-SolvedForPin.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg-SolvedForPin.gif)

This means that the power dissipated can be expressed as:

[![Calculating Power dissipated as Power In minus Power out](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg-SolvedForPd.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg-SolvedForPd.gif)

In electronics power can be expressed as the product of the voltage and current. Which means we can rewrite the first equation as:

[![Power Dissipated is (Vin \* Iin) minus (Vout \* Iout)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg-SolvedForPd-Again.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg-SolvedForPd-Again.gif)

With linear regulators the input and output current is the same, so we can simplify the equation to the following:

[![Simplified, the Power dissipated is the Current times (Vin minus Vout)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg-SolvedForPd_-_Simplified.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg-SolvedForPd_-_Simplified.gif)

Now we need to look at the thermal characteristics of the linear regulator. The LM7805, has the following thermal resistances for the TO-220 package being used:

[![Thermal Characteristics for the LM7805](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LM7805_Thermal_Data.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LM7805_Thermal_Data.jpg)

### Without a heatsink (R~θJA~)

For this first example, we'll see how hot a linear regulator gets with only a 200mA load. TheLM7805 has an output voltage of 5V, and the input voltage will be around 12V. Plugging those numbers into our power loss equation from above, gives us:

[![Simplified, the Power dissipated is the Current times (Vin minus Vout)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/PdWithoutAHeatsinkVariables.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/PdWithoutAHeatsinkVariables.gif)

[![Calculating power dissipated as 1.4 watts without a heatsink](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/PdWithoutAHeatsinkNumbers.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/PdWithoutAHeatsinkNumbers.gif)

To figure out how hot that will get without a heatsink, we'll need to use the Junction to Air thermal resistance, which is 50°C/W. Using the formula from the thermal resistance section, and assuming ambient air temperature is 23°C, we can calculate the junction temperature to be:

[![Junction temperature is Power Dissipated times AirThermalResistance plus Ambient temp](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg_-_JunctionTemp-Variables.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg_-_JunctionTemp-Variables.gif)

[![Calculating Junction Temperature as 93 degrees C](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg_-_JunctionTemp-Numbers.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg_-_JunctionTemp-Numbers.gif)

To see how that compares to the real world, I measured the input voltage to be 12.1V and the output voltage under load to be 4.90V. I used a constant current dummy load set to 200mA connected to the output. Using the measured values, the dissipated power is:

[![Setting up dummy load to calculate power dissipation as 1.44W](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg_-_PowerDissipated.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg_-_PowerDissipated.gif)

The expected junction temperature should then be:

[![Adjusted junction temperature calculation is 95 degrees C](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg_-_JunctionTemp-Solved.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg_-_JunctionTemp-Solved.gif)

[![Thermal Image of LM7805 Under Load without a heatsink](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Flir_LM7805_No_Heatsink.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Flir_LM7805_No_Heatsink.jpg)

As the thermal image above shows, after turning on the load and letting the regulator heat up, it settled at a temperature of around 98°C. Pretty close, but it's a good example of why it's important to add margins to numbers. Due to the lack of precision, the power supply was slightly higher than we calculated, and under load, the regulator has a output voltage tolerance of 4%, which could allow the output voltage to drop to as low as 4.8V and still be in spec.

### With a Heatsink (Using R~θJC~)

Now with the addition of a heatsink, instead of using the thermal resistance from the junction to air, we need to use the value for junction to case, which is around 5°C/W. After looking at the datasheet for the heatsink I'm using, \~1.4W of power in free air would result in a 25°C temperature rise:

[![Heatsink temperature raise for 1.4W of power](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Heatsink_Graph_for_Linear_Regulator_Example.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Heatsink_Graph_for_Linear_Regulator_Example.jpg)

Because the heatsink provides a temperature rise instead of a thermal resistance, We will need to first calculate the junction temperature rise using the thermal resistance from the junction to the heatsink, and then add on temperature rise from the heatsink and ambient air temperature to get the junction temperature. Using thermal compound lowers the thermal resistance from the case to the heatsink (\~0.25°C/W), without it we\'ll assume the thermal resistance is around 1°C/W. The junction temperature equation therefore becomes:

[![Junction temperature calculated with a heatsink added in ](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg-WithHeatsink-Part1.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg-WithHeatsink-Part1.gif)

[![Junction temperature is calculated as 56.4 degrees C when using a heatsink](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg-WithHeatsink-Part2.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/LinearReg-WithHeatsink-Part2.gif)

The actual voltages were the same as without a heatsink: Vin = 12.10V, Vout = 4.90V, Iout = 200mA. This resulted in the same 1.44W of power that actually needed to be dissipated, which only increased the calculated junction temperature to 56.64°C. After turning on power and enabling the load, I waited to let the temperature get up to a steady state temperature and measured the temperature of the regulator to be around 54°C.

[![Thermal Image of LM7805 Under Load with a heatsink](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Flir_LM7805_With_Heatsink.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Flir_LM7805_With_Heatsink.jpg)

This time the temperature was lower than we calculated. Most likely the error came from reading the temperature rise in still air for the heatsink, instead of 25°C, it could have been closer to 23°C. In the last example we'll use a surface mount regulator and try to estimate how hot the regulator gets using the PCB as a heatsink.

## Example: SMD DC/DC Converter

The board we're using is the [Buck-Boost](https://www.sparkfun.com/products/15208), which uses the [TPS63070 DC-DC converter](https://cdn.sparkfun.com/assets/e/4/a/1/4/TPS63070_DataSheet.pdf). The board is 1.25x1.25 inches using 1oz copper. Other things to note, is the regulator is in the center of the board, and is over 95% solid copper. Because of the size, I'm going to make some assumptions by using the total board area for the thermal resistance, and use all 41 vias for the via thermal resistance.

To get started we need to figure out how much power we need to dissipate. With a DC-DC converter, the input current does not equal the output current, so we can't use the same formula as we did for the linear regulator. Instead we can estimate using the efficiency graph from the datasheet:

[![DC/DC Converter Efficency Graph at 5V out](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/3/DC-DC_Converter_Efficiency_Graph.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/DC-DC_Converter_Efficiency_Graph.jpg)

The efficiency graph plots the efficiency as a function of the output current, which is different based on the input and output voltages. For this test, we'll use the same values before, having an input voltage of 12V and output voltage of 5V. This time though we'll increase the load current to 1.0A. Using the 5V efficiency graph above, the efficiency should be around 93%, which would make our power loss 7% of the output power.

[![Example power dissipation efficiency](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/CalculatingHowMuchPowerToDissipate.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/CalculatingHowMuchPowerToDissipate.gif)

For the thermal resistances I used the via thermal resistance calculator and approximated the thermal resistance with the vias to be around 4.4°C/W using the values from the via calculation tool. To estimate the PCB thermal resistance, the board will be elevated off the table, to prevent using the table a heatsink. But because the bottom of the board is also in contact with the air, the surface area is now doubled from 10.08cm\^2 to 20.16cm\^2. Based on the surface area for the buck-boost board, I can estimate the PCBs thermal resistance to be around 65°C/W.

[![PCB Thermal Resistance Highlight](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/3/PCB_Thermal_Resistance_example.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/PCB_Thermal_Resistance_example.jpg)

The datasheet for the TPS63070 has the following for the thermal characteristics:

[![TPS63070 Thermal Characteristics](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/TPS63070_Thermal_Characteristics.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/TPS63070_Thermal_Characteristics.jpg)

*Click on the image for a closer view.*

The junction to case thermal resistance is not applicable, however the junction to board thermal resistance is, which is around 13°C/W. Using the thermal resistance values, we can plug that into the junction temperature equation:

[![calculating junction temperature with Power dissipated, junction to board thermal resistance, Via to Board thermal resistance, board to air thermal resistance, and ambient temperature](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/CalculatingPowerDissWithHeatsink-Part1-REDO.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/CalculatingPowerDissWithHeatsink-Part1.gif)

[![Final junction temperature calculation using heat sink](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/CalculatingPowerDissWithHeatsink-Part2.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/CalculatingPowerDissWithHeatsink-Part2.gif)

Just like before, I enabled the dummy load and let the board heat up until the temperature stopped rising. As shown below, I recorded a temperature of around 54°C.

[![Thermal Image of a PCB Heatsink](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Flir_PCB_Heatsink.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/3/Flir_PCB_Heatsink.jpg)