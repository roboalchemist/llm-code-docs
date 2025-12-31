# Source: https://learn.sparkfun.com/tutorials/adding-a-timed-button-to-a-project

## Introduction

[![Finished SparkFun timed power button](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/0/Timer_Button_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/0/Timer_Button_Tutorial-04.jpg)

In this tutorial you will learn how to add an on button that will provide power to your project for an amount of time and then turn off again. We will be using a [Solid State Relay (SSR)](https://www.sparkfun.com/products/10636) to deal with AC (alternating current) voltages like what you would see coming out of your wall at your house.

**PLEASE DON\'T HURT YOURSELF!** When dealing with high voltages, and high currents, please be extra careful and take any and all precautions.

### Required Materials

If you would like to follow along with this tutorial, you will need the following:

### Suggested Readings

Before getting started, you may find some of the concepts below helpful.

- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering)
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law?_ga=1.62810284.1840025642.1408565558)
- [How to Use a Multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter?_ga=1.41190690.1840025642.1408565558)
- [Alternating Current (AC) vs. Direct Current (DC)](https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc?_ga=1.268724849.1840025642.1408565558)
- [How to Power a Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project?_ga=1.200557870.1840025642.1408565558)
- [Connector Basics](https://learn.sparkfun.com/tutorials/connector-basics)
- [Electric Power](https://learn.sparkfun.com/tutorials/electric-power)
- [Controllable Power Outlet](https://www.sparkfun.com/tutorials/119)

## Why Have a Timed Power Button?

Saving energy is always a good thing, but some projects have sensitive components that need a bit of a break and would last much longer if they weren\'t on all the time.

Some interactive projects should not stay powered on indefinitely. Parts of LEDs (especially RGB LEDs) can burn out, systems can lock up. In SparkFun's new retail space we have dozens of demos that could benefit from a big button that allows the user to power up the project for 5 minutes then powers down until the next customer walks by. The first project to get this attention is our classic [Picture Frame Tetris](https://www.sparkfun.com/tutorials/40). We hate leaving this on for 24 hours a day because it wastes power, it doesn't have a good screen saver mode, and we are worried that the LEDs may burn out over time. This button was designed for that, a simple way to provide power to a project for a short time, only when needed.

## Getting Started and Uploading Code

Since the project to which I am adding a timer uses DC (direct current), I could have easily added the timer to regulate the DC voltage using just a [simple DC relay switch](https://www.sparkfun.com/products/100). Most projects in your home will be running off power from the wall, so this tutorial will focus more on how to regulate the AC voltage and current.

We will start with uploading the code. For this project, I have chosen a [5V Pro Mini](https://www.sparkfun.com/products/11113). To Program a Pro Mini, you\'ll need a [5V FTDI Breakout](https://www.sparkfun.com/products/9716). If your system is using 3.3V instead of 5V, we also have a [3.3V Pro Mini](https://www.sparkfun.com/products/11114), and [3.3V FTDI Breakout](https://www.sparkfun.com/products/9873) to match.

To connect the Pro Mini to the FTDI Breakout, all you need to do is solder some [right-angle male headers](https://www.sparkfun.com/products/553) onto the FTDI inputs on the Pro Mini.

[![Pro Mini with right-angle male headers for the FTDI breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/0/Timer_Button_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/0/Timer_Button_Tutorial-03.jpg)

*Pro Mini with right-angle male headers for the FTDI breakout*

Once you have the FTDI breakout plugged into the Pro Mini, you can use a [USB to Mini-B Cable](https://www.sparkfun.com/products/11301) to plug it right into your computer.

Open up the Arduino IDE, and upload the example code to your Pro Mini (for specific info on what the code is doing take a look at the comments in the code):

    language:c
     /* 
    SparkFun simple code for running an On timer 
    for power from a button push
    By: Sarah Al-Mutlaq 
    7/9/15
    */

    int startButton = 13; //pin recieving info from start button
    int controlPin = 4;   //pin we will use to contol power 

    unsigned long timerCount = 0; // variable to hold our timer info

    void setup()
    

    void loop()
    
      if (timerCount != 0)
        
       else 
    }

## Hardware Hookup

As you can see in the code, we will be hooking up the button to pin 13 of the Pro Mini (this can be changed to any pin in the code) and pin 4, as well as 5V high and Ground to our SSR kit (also can be changed in the code). To connect the Pro Mini, you can either directly solder wires onto the pins, 5V, and ground. Or, you can solder on [female headers](https://www.sparkfun.com/products/743), and plug wires into those.

[![Photo of Pro Mini Arduino with headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/0/Timer_Button_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/0/Timer_Button_Tutorial-02.jpg)

*Photo of Pro Mini Arduino with headers*

[![Fritzing diagram of button Pro Mini and SSR kit hooked up](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/0/Timed_power_button_pro_mini_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/0/Timed_power_button_pro_mini_bb.jpg)

*Fritzing diagram of button, Pro Mini, and SSR kit hooked up*

The [SSR kit](https://www.sparkfun.com/products/10684) does not come with all of its parts soldered on, so you will need to assemble it.

[![SparkFun Solid state relay kit all hooked up](https://cdn.sparkfun.com/assets/parts/5/4/9/0/10684-Action.jpg)](https://cdn.sparkfun.com/assets/parts/5/4/9/0/10684-Action.jpg)

*Solid state relay kit all hooked up*

This solid state relay kit is rated for a max of **125VAC at 8A**, so, for a small-medium size project, this is a fine option. However if your project is going to be pulling more current or voltage you might want to look into a [full blown Solid State Relay (SSR)](https://www.sparkfun.com/products/13015), this one can handle **380VAC and 40A**!

**Warning!** That is a lot of current so please, be extra extra careful with those kind of projects.

Since I used a [Big Dome Pushbutton](https://www.sparkfun.com/products/9181), I will also be hooking up the LED inside to Vcc and Ground. The code recognizes that the button is pushed when the pin goes high. This means the button will be pulled low and only go high when the button is pushed (meaning 5V will be connected to the pin the button connects when it is pushed).

Last, the load pins on the SSR kit will be hooked up to one of the wires that are going from your project to the AC power supply (usually the wall).

[![Photo of SparkFun SSR kit hooked up to an AC to DC power supply](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/0/Timer_Button_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/0/Timer_Button_Tutorial-01.jpg)

*Photo of SparkFun SSR kit hooked up to an AC to DC power supply*

To protect the project and make sure that nothing is going to short, I recommend covering everything with electrical tape or [Heat Shrink](https://www.sparkfun.com/products/9353). I also added a fair amount of hot glue to this project to protect all the connections and keep everything in place.

Once everything is hooked up and in place, you can plug your Pro Mini (through the FTDI Breakout) into the wall with a [5V adapter](https://www.sparkfun.com/products/11456), plug in your connected project, and there you have it! A timed on button for your project!

I cut a few pieces of plywood and glued them together to form a little housing for the button.

[![Finished timer button in enclosure](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/0/Timer_Button_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/0/Timer_Button_Tutorial-04.jpg)