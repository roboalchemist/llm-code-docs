# Source: https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces

## Introduction

Handling PCB jumper pads and traces is an essential skill. In this tutorial, you will learn how to cut a PCB trace and add a solder jumper between pads to reroute connections. You will also learn how to repair a trace with the green wire method if a trace is damaged.

[![PCB Trace Being Cut on SparkFun Lumenati Boards](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/4/PCB_TraceCutLumenati.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/PCB_TraceCutLumenati.jpg)

*[Pete](https://www.sparkfun.com/users/19939) Cutting a Trace on the SparkFun Lumenati Boards*

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/pcb-basics)

### PCB Basics 

What exactly IS a PCB? This tutorial will breakdown what makes up a PCB and some of the common terms used in the PCB world.

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)

### How to Use a Multimeter 

Learn the basics of using a multimeter to measure continuity, voltage, resistance and current.

### Required Materials

To follow along with this tutorial, you will need the following materials:

[![Digital Multimeter - Basic](https://cdn.sparkfun.com/r/140-140/assets/parts/9/9/0/7/12966-01.jpg)](https://www.sparkfun.com/digital-multimeter-basic.html)

### [Digital Multimeter - Basic](https://www.sparkfun.com/digital-multimeter-basic.html) 

[ TOL-12966 ]

The digital multimeter (DMM) is an essential tool in every electronic enthusiasts arsenal. The SparkFun Digital Multimeter, h...

[ [\$21.50] ]

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[![Hobby Knife](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/6/09200-Hobby_Knife-01.jpg)](https://www.sparkfun.com/hobby-knife.html)

### [Hobby Knife](https://www.sparkfun.com/hobby-knife.html) 

[ TOL-09200 ]

It\'s like an Xacto knife, only better. We use these extensively when working with PCBs. These small knives work well for cutt...

[ [\$3.75] ]

## What is a Jumper?

A jumper is an electrical connection designed to open or close a circuit between two or more points. Depending on the PCB, jumpers can be added into a design to change the board\'s default:

- Serial UART
- I^2^C Address
- SPI
- Voltage Level
- Pull-Up Resistor
- Mode

### Jumper Pads

Below are a few examples of 1x2 and 1x3 jumper pads that are used with SparkFun boards. The spacing between pads are usually close together making it easy to add a solder.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/12885-04ClosedOpenJumperPads.png "Sunny Buddy with JP1 Closed Jumper and JP2 Open Jumper")](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/12885-04ClosedOpenJumperPads.png)  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/09716-03_5V.jpg "5V FTDI with 1x3 Open and Closed Pads")](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/09716-03_5V.jpg)    [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/13763-02_Closed_I2CPullUp_Jumpers.png "Closed I2C PullUp Jumpers")](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/13763-02_Closed_I2CPullUp_Jumpers.png)
                                                                       *[Sunny Buddy](https://www.sparkfun.com/products/12885) w/ JP1 Closed Jumper and JP2 Open Jumper Pads*                                                                      *[5V FTDI](https://www.sparkfun.com/products/9716) w/ 1x3 Open and Closed Jumper Pads*                                                                                                                                                         *[Si7021 Humidity and Temperature Sensor](https://www.sparkfun.com/products/13763) w/ 1x3 Closed I^2^C Pull Up Jumper Pads*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Jumpers with Plated Through Hole Pads

However, that may not always be the case for jumpers. Standard 0.1\" pitched pins can have a wider gap or a development board may have a pin located in a different position. Additional solder, 2-pin jumper blocks, and jumper wires may be required to make a connection.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/4/SolderBridgeJumperSnappableProtoBoard.png "Solder Bridge between Through Hole Pins on ProtoBoard")](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/SolderBridgeJumperSnappableProtoBoard.png)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/4/ElectricImp_2-PinJumperHeader.png "Electric Imp 2-Pin Jumper")](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/ElectricImp_2-PinJumperHeader.png)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/4/ReroutingPinsUsingJumperWire.png "Rerouting Pins Using Jumper Wire")](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/ReroutingPinsUsingJumperWire.png)
                                                                *Custom cable adapter using the [snappable protoboard](https://www.sparkfun.com/products/13268) w/ solder jumpers between wires and connector.*                                                                                                                                *[Electric Imp Breakout](https://www.sparkfun.com/products/12886) w/ 2-Pin Jumper on Header*                                                                                                                                *[GPS Logger Shield](https://www.sparkfun.com/products/13750) w/ Software Serial Rerouted w/ Jumper Wires*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Cutting a Trace Between Jumper Pads

Locate the trace that you want to disconnect. The function of a jumper can vary depending on the board\'s design. For more information, try checking out the associated documentation for your board.

In this example, we will be looking at the [5V FTDI Basic Breakout](https://www.sparkfun.com/products/9716) to adjust the default voltage level from 5V to 3.3V. On the back of the board are three pads. If you look closely on the back of a 5V FTDI breakout, the center and right pads are connected together with a trace by default. On the 3.3V FTDI, the trace is connected to 3.3V by default.

[![FTDI Jumper Pads for Voltage Selection](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/09716-03_5V.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/09716-03_5V.jpg)

Using a [hobby knife](https://www.sparkfun.com/products/9200), carefully move the blade back and forth across the small trace to sever the connection under the red solder mask.

**[] Caution!** When cutting a trace, be careful not to cut any adjacent traces, pads, and your hand! The metal blade on a hobby knife is sharp so make sure to take your time.\
\
There is a [ceramic blade](https://www.sparkfun.com/products/14508) available as an alternative to reduce the risk of injury.

[![PCB Trace Cut with Hobby Knife](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/4/HobbyKnifeCutTracePCB.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/HobbyKnifeCutTracePCB.png)

## Adding a Solder Jumper

To add an intentional solder jumper, place the soldering iron\'s tip on the 3.3V side (left pad relative to the header pins facing down) and the center pad.

[![Adding a Solder Jumper on the FTDI\'s 3.3V side. ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/4/SolderJumper3_3VSide.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/SolderJumper3_3VSide.jpg)

If you decide to set the FTDI back to its default of 5V, simply heat the intentional solder jumper with a soldering iron and move the solder back to the right side. Feel free to add more solder if necessary.

[![Adding a Solder Jumper on the FTDI\'s 5V Side](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/4/SolderJumper5VSide.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/SolderJumper5VSide.jpg)

Certain PCBs already have a solder jumper connecting pads. You may just need to adjust the connection by removing the solder jumper.

## Testing the Connection

Before powering the PCB, make sure the trace between the jumper pads has been cut by testing the connection with a [multimeter](https://www.sparkfun.com/products/12966).

[![Multimeter Set to Measure Continuity](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/4/01_Multimeter_Tutorial-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/01_Multimeter_Tutorial-09.jpg)

Once the multimeter has been set to measure continuity, place one probe on the center pad and the other on the right pad. If the trace has not been fully cut, the multimeter\'s buzzer will make a noise. If the trace is fully cut, you are good to power the board!

For more information about using a multimeter to test for continuity, check out our multimeter tutorial.

[Multimeter Continuity Test](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter#continuity)

## Rerouting and Green Wire Repair

Lets take a look at Nate\'s tutorial about [Wireless Arduino Programming with Electric Imp](https://learn.sparkfun.com/tutorials/wireless-arduino-programming-with-electric-imp#hardware-connections). While modifying the serial UART connection with a hobby knife, an adjacent trace was accidentally cut!

[![PCB Trace Accidentally Cut](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/4/PCBTraceAccidentallyCut2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/PCBTraceAccidentallyCut2.jpg)

Don't see the problem? Here\'s a close up of the severed connection.

[![Adjacent Trace Accidentally Cut on PCB](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/4/Bad_Cut_Trace.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/Bad_Cut_Trace.png)

Unfortunately, Nate was going too fast and TX trace to the Imp ended up accidentally cut. After troubleshooting and probing the connection using a multimeter, he discovered the TX was not connected.

[![PCB Repair with Green Wire Fix](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/4/PCBRepairGreenWireFix.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/4/PCBRepairGreenWireFix.jpg)

With some [wire](https://www.sparkfun.com/products/11367), [wire strippers](https://www.sparkfun.com/products/12630), and some [locking tweezers](https://www.sparkfun.com/products/12572), the trace was quickly repaired by connecting to the tented via. The board was recovered and started working as expected once the connection was repaired.

**[] Tip:** While it was apparent with the Electric Imp Shield, the next available exposed copper connection may by harder to find on more complex boards. Depending on the board that you are repairing, you may need to pull up a board\'s layout file to highlight the connection.

Remember to take extra time and care when cutting traces so as to not cut beyond or nick nearby traces!