# Source: https://learn.sparkfun.com/tutorials/getting-started-with-ltspice

## Introduction to LTspice

[Linear Technology](http://www.linear.com/) provides useful and *free* [design simulation tools](http://www.linear.com/designtools/software/) as well as device models. This tutorial will cover the basics of using LTspice IV, a free integrated circuit simulator.

## Getting Started

To download LTspice IV for Windows click [here](http://ltspice.linear-tech.com/software/LTspiceIV.exe), and for Mac OS X 10.7+ click [here](http://ltspice.linear-tech.com/LTspiceIV.dmg). Linear Technology updates these packages so check the [website](http://www.linear.com/designtools/software/#LTspice) for updates. I linked the executable because this is the version I will be using for the tutorial.

**Note:** For Ubuntu Linux users, you can look into using a Wine derivative called PlayOnLinux. One of our customers tested it out with Ubuntu. You can check out their [forum post](https://electronics.stackexchange.com/questions/18760/comparison-between-spice-simulators/43329#43329) for more information.\
\
Here are some installation guides for PlayOnLinux:

- [PlayOnLinux Ubuntu Documentation](https://help.ubuntu.com/community/PlayOnLinux)
- [How does one install PlayOnLinux?](https://askubuntu.com/questions/233782/how-does-one-install-playonlinux)

Once you open an instance of LTspice IV check out the video below to see how to get started navigating through the menu, setting your schematic and waveform preferences, adding a new schematic, placing parts and organizing your schematic and finally running a simple DC operating point on a voltage divider.

### Helpful Hints

[Hot keys and Simulator Directives](http://cds.linear.com/docs/en/software-and-simulation/LTspiceIV_flyer.pdf) - Make your life easier with shortcuts. The Simulator Directives are your Dot commands. I suggest you look through these very carefully in the HELP menu in LTspice. The help menu will show you the syntax and give descriptions for each one. Specific commands will be covered one-by-one in future videos. If you are having trouble getting one or more to work please head over to the forum.

[Labels](http://cds.linear.com/docs/en/software-and-simulation/LTspiceGettingStartedGuide.pdf)- Turn to page 23 to see how to label values such as using 8k instead of 8000.

## Simulation: Transient Analysis 

A time domain transient analysis is where a parameter such as a voltage or current is plotted against time. If you are looking at an output you can see the behavior over a specified length of time. For this example we are going simulate the output of a [half-wave rectifier](http://www.circuitstoday.com/half-wave-rectifiers). For this type of analysis we will cover how to add an AC signal source to your schematic and choose a specific diode.

## Simulation: AC Analysis

Ac analysis provides the frequency response of your circuit. The output waveform will be a [bode plot](http://lpsa.swarthmore.edu/Bode/Bode.html) showing you the amplitude and phase across a specified frequency range. There are several options with AC analysis. You can view frequency response as a bode plot, on the Cartesian coordinate plane with the real and imaginary axis and you can view it as a Nyquist plot.

We are going to build a passive, first order, [low-pass filter](http://www.electronics-tutorials.ws/filter/filter_2.html) and see what information can be obtained about the circuit from the plot.

## Simulation: DC Sweep

A DC Sweep is a type of simulation that allows you to vary the voltage or current of a specified device. On all schematics of SparkFun\'s parts we give you a voltage range for which the product can safely operate. I thought it would be a good idea to check a Sparkfun product to see just how accurate those voltage ranges are. For this example we are going to look at the [Electret Microphone Breakout Board](https://www.sparkfun.com/products/12758).

## Simulation: Noise

[Noise analysis](http://www.ni.com/tutorial/14516/en/) let you view the noise inherent in your system as well as injected noise from outside source when modeled properly. Noise is most commonly concerning in op-amp circuit where precision is everything. For example, a battery management system using op-amps to sense the current. Charging cycles of rechargeable batteries as well the load current are very important parameters to monitor for the overall health of the battery and safety of the user. A noisy op-amp circuit may skew that current reading and cause unwanted effects such as incorrect current readings on the microcontroller which keeps the battery from being over or under current. I\'m sure an audio example would have been better to use here. But you get the idea, noise can be bad when it is unwanted.

We are going to continue using the pre-amplifer circuit from the Electret Mic Breakout Board and run a noise analysis. LTspice can model the \[shot, flicker and thermal\](https://en.wikipedia.org/wiki/Noise\_(electronics) noise your circuit.

## Simulation: DC Transfer 

The DC Transfer function calculates the low frequency gain and the input and output resistances of your circuit. Continuing with the Electret Mic Breakout Board product as our example we can first compute the transfer function. We know that the output voltage is biased at 1/2 the input voltage. Since the Transfer function describes the behavior of the output as a function of the input and we can say the transfer function should be equal to 1/2. If we choose VCC to be 5V then Vout is 2.5V. This circuit should have low output impedance because we want op-amps to operate like ideal voltage sources. This ensures maximum power is delivered at the output giving your ADC the best values. The closer the output impedance is to zero the better. Similarly we want the input impedance to be high as to not draw current from the source. Let\'s sim the transfer function and verify it has been designed accordingly.

## Creating a New Model 

There are several steps to create your own model in LTspice. A model consists of a subcircuit and a symbol. For an example, we are going to build a model for a potentiometer. It will be based off the SparkFun 10k trimpot. A few months ago I designed a soldering kit for personal use based off the 555 timer. LTspice does not come with a standard potentiometer so we will build one. Most of the time simulating a trim-pot as a resistor is fine. But I plan on giving this kit to new students of electronics and want them to understand the difference between a resistor symbol and its use and a potentiometer symbol and how it is used in this circuit.

See the video below to create your own potentiometer model in LTspice.

## Adding Third Party Models

There are many ways to import third party models into LTspice. I have found one particular method to be the fastest and easiest for importing models and subcircuits. Eventually, I will add another video on the Forum on how to do this other ways. If you have a way that works for you, please share on the forum. If you are having trouble using a specific method just ask on the forum and I will respond with a video.