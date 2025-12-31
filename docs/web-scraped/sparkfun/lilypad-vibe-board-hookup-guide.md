# Source: https://learn.sparkfun.com/tutorials/lilypad-vibe-board-hookup-guide

## Introduction

The [LilyPad Vibe Board](https://www.sparkfun.com/products/11008) is a small vibration motor that can be sewn into projects with conductive thread and controlled by a LilyPad Arduino. The board can be used as a physical indicator on clothing and costumes for haptic feedback.

[![LilyPad Vibe Board](https://cdn.sparkfun.com/r/600-600/assets/parts/6/2/8/2/11008-01a.jpg)](https://www.sparkfun.com/lilypad-vibe-board.html)

### [LilyPad Vibe Board](https://www.sparkfun.com/lilypad-vibe-board.html) 

[ DEV-11008 ]

Apply 5V and be shaken by this small, but powerful vibration motor. Works great as an physical indicator without notifying an...

[ [\$8.60] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

Learn how to use conductive thread with LilyPad components.

[](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-hookup-guide)

### LilyPad ProtoSnap Plus Hookup Guide 

The LilyPad ProtoSnap Plus is a sewable electronics prototyping board that you can use to learn circuits and programming with Arduino, then break apart to make an interactive fabric or wearable project.

[](https://learn.sparkfun.com/tutorials/getting-started-with-lilypad)

### Getting Started with LilyPad 

An introduction to the LilyPad ecosystem - a set of sewable electronic pieces designed to help you build soft, sewable, interactive e-textile projects.

## Attaching to a LilyPad Arduino

The LilyPad Vibe Board has two sew tabs: Power (**+**) and Ground (**\--**). Next to each tab is a white label for reference. For power, you can connect an input voltage anywhere between **3.3V** and **5V**. The motor can vibrate faster as you provide more voltage. We recommend connecting the (**+**) tab to a MOSFET to drive the motor when using it with an Arduino due to the amount of current each I/O pin can source . To adjust the intensity, we recommend using a PWM capable sew tab on a LilyPad Arduino.

[![LilyPad Vibe Board top view](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/7/VibeBoardCatalog.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/7/VibeBoardCatalog.jpg)

**Note:** The [haptic motor\'s datasheet](https://www.sparkfun.com/datasheets/Robotics/310-101_datasheet.pdf?_ga=2.60991982.352581071.1547485841-965574233.1522177811) states that the voltage range is between *2.5V\~3.8V*! Don\'t worry, there is a surface mount resistor between the power sew tab and the motor. So if you were providing *5V* as the input, the resistor will drop the voltage to about *2.8V*, which is within the acceptable range to operate.

To follow along with the code examples in this tutorial, connect the vibe board and transistor to a LilyPad Arduino as shown in the images below. Use alligator clips to temporarily connect the circuit. Connect the LilyPad\'s \"**+**\" sew tab to the \"**+**\" sew tab of the vibe board. Make another connection between the \"**\--**\" sew tab and the MOSFET power controller\'s \"**\--**\" sew tab. Keep in mind that the \"**\--**\" label on the MOSFET power controller does **not represent ground** (**GND** or \"**\--**\"). Ground is represented as \"**IN\--**\". The \"**IN\--**\" should be connected to a LilyPad Arduino\'s \"**\--**\" sew tab.

To control the vibe board, connect a PWM pin (pin **10** in the following cases) to the \"**IN+**\". When testing the example for button feedback, simply connect **A4** to the LilyPad Arduino\'s \"**\--**\" ground sew tab. After you are finished prototyping, replace the alligator clips with conductive thread traces for permanent connection in your project.

[![LilyPad Arduino USB with N-Channel MOSFET Power Controller and Vibe Motor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/7/LilyPad_USB_VibeBoard_MOSFET_Button_Circuit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/7/LilyPad_USB_VibeBoard_MOSFET_Button_Circuit.jpg)

*Connecting to a LilyPad Arduino USB (**Click** image to enlarge).*

**Note:** The green alligator clips used in the LilyPad Arduino USB\'s circuit are used as a temporary button for testing. You could also use a LilyPad button or make your own using snap pins when integrating the parts in your project!\
\

[![LilyPad Button Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/9/6/08776-LilyPad_Button_Board-01.jpg)](https://www.sparkfun.com/lilypad-button-board.html)

### [LilyPad Button Board](https://www.sparkfun.com/lilypad-button-board.html) 

[ DEV-08776 ]

We designed this board to give the user a low profile button without any sharp edges. Button closes when you push it and open...

[ [\$2.10] ]

[![Conductive Thread Bobbin - 30ft (Stainless Steel)](https://cdn.sparkfun.com/r/140-140/assets/parts/5/8/9/9/10867-01.jpg)](https://www.sparkfun.com/conductive-thread-bobbin-30ft-stainless-steel.html)

### [Conductive Thread Bobbin - 30ft (Stainless Steel)](https://www.sparkfun.com/conductive-thread-bobbin-30ft-stainless-steel.html) 

[ DEV-10867 ]

This is 30 feet of conductive thread spun from stainless steel fiber and wound on a plastic bobbin. Use it to sew up all of y...

[ [\$5.75] ]

[![Snap Assortment - 30 pack (male and female)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/0/7/0/11347-01.jpg)](https://www.sparkfun.com/snap-assortment-30-pack-male-and-female.html)

### [Snap Assortment - 30 pack (male and female)](https://www.sparkfun.com/snap-assortment-30-pack-male-and-female.html) 

[ DEV-11347 ]

These sew-on fabric snaps are the same size used on the LilyPad SimpleSnap boards. You can sew these into your project to all...

**Retired**

[![LilyPad Protosnap Plus with N-Channel MOSFET Power Controller and Vibe Motor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/7/LilyPadProtoSnapPlusMOSFETVibeBoard_Circuit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/7/LilyPadProtoSnapPlusMOSFETVibeBoard_Circuit.jpg)

*Connecting to a LilyPad ProtoSnap Plus (**Click** image to enlarge).*

**Note:** The LilyPad ProtoSnap Plus setup does not require a alligator clips between A4 and GND since there is already a button between the pins.

## Using a Button to Trigger Feedback

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Copy the code below and paste it into your Arduino IDE. Select your board (i.e. **LilyPad Arduino USB** for the [LilyPad USB](https://www.sparkfun.com/products/12049), **LilyPad USB Plus** for the [LilyPad USB Plus](https://www.sparkfun.com/products/14631), etc.) and COM port. Finally, click the upload button to upload the demo on your Arduino.

    language:c
    /*
      LilyPad Vibe Board: Button Feedback
      Written by: Ho Yun "Bobby" Chan
      @ SparkFun Electronics
      Date: 1/14/2019
      https://www.sparkfun.com/products/11008

      The main code checks for a button press. If there is a button press,
      the Arduino turns on the LilyPad Vibe Board for haptic feedback.
      For a visual cue, the LED will turn on too. If not, the LED and
      motor will remain off.
    */

    const int motorPin = 10;     // motor connected to PWM pin 9
    const int button1Pin = A4;  // pushbutton 1 pin
    const int ledPin =  13;     // LED pin

    int button1State;  //check state of button press

    void setup() 
      // fade out from max to min in increments of 5 points:
      for (int fadeValue = 255 ; fadeValue >= 0; fadeValue -= 5) 

    }

    void loop() 
      else
      
    }

After uploading, you should see the built-in LED on the LilyPad Arduino and the vibe motor turn on and off. The LilyPad Arduino will then slowly increase and decrease in intensity. The vibe motor will turn on when the Arduino\'s PWM output is around `130`. Once we start looping in the `loop()` function, the LilyPad Arduino will check to see if there is a button press. If the button is pressed (i.e. or when **A4** is connected to ground), the built-in LED and vibe motor will turn on. There is a slightly longer delay after this happens so there is enough time to detect when the motor is turned on as feedback. If there is no button press, both will remain off.

## Sewing Into a Project

Once you are finished prototyping your project using the LilyPad Vibe Board, you can replace any temporary connections with conductive thread. For an overview of sewing with conductive thread, check out this guide:

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

December 17, 2016

Learn how to use conductive thread with LilyPad components.

You can also make your own button by using metal snaps or any conductive material.

[](https://learn.sparkfun.com/tutorials/ldk-experiment-5-make-your-own-switch)

### LDK Experiment 5: Make Your Own Switch 

October 2, 2013

Learn to create and integrate your own handmade switch into an e-textile circuit.

### Making Your Project Portable with Batteries

As you start embedding your circuit into your project, we recommend connecting a LiPo battery to the LilyPad\'s JST connector to regulate the voltage. There are also LiPo charge IC\'s built into LilyPad Arduinos to recharge the LiPo batteries so that it does not have to be removed from the circuit.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![LilyPad Arduino USB, MOSFET Power Controller, and Vibe Board with LiPo Battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/7/LilyPad_USB_VibeBoard_MOSFET_Button_Circuit_Battery.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/7/LilyPad_USB_VibeBoard_MOSFET_Button_Circuit_Battery.jpg) | [![LilyPad Protosnap Plus: MOSFET Power Controller, and Vibe Board with LiPo Battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/6/7/LilyPadProtoSnapPlusMOSFETVibeBoard_Circuit_Battery.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/7/LilyPadProtoSnapPlusMOSFETVibeBoard_Circuit_Battery.jpg) |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Circuits with LiPo batteries for remote power. **Click** on images for a closer view.*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

For more information about using LiPo batteries with LilyPad, check out the tutorial for [Powering Your Project](https://learn.sparkfun.com/tutorials/lilypad-basics-powering-your-project).

[](https://learn.sparkfun.com/tutorials/lilypad-basics-powering-your-project)

### LilyPad Basics: Powering Your Project 

September 24, 2018

Learn the options for powering your LilyPad projects, LiPo battery safety and care, and how to calculate and consider power constraints on your projects.

## Project Examples

### [Thermal Alert Project](https://learn.sparkfun.com/tutorials/lilypad-development-board-activity-guide/11-thermal-alert-project)

By adding a temperature sensor to the circuit, you can trigger the motor whenever it gets too hot. For more information, check out the [thermal alert project from the Lilypad Development Board Activity Guide](https://learn.sparkfun.com/tutorials/lilypad-development-board-activity-guide/11-thermal-alert-project). Just make sure to redefine the LilyPad Arduino\'s pins in code.

[![Thermal Alert Project from the LilyPad Development Board Actibity Guide](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/1/Dev_Thermal_2.png)](https://learn.sparkfun.com/tutorials/lilypad-development-board-activity-guide/11-thermal-alert-project)

*Highlighted components used for the [thermal alert project](https://learn.sparkfun.com/tutorials/lilypad-development-board-activity-guide/11-thermal-alert-project). **Click** on the image for more information.*

### [LilyPad Simblee Fitness Bracer](https://www.sparkfun.com/news/2062)

This fitness bracer uses two vibe boards to alert the wearer when they have been inactive for 60 minutes.

*Demo video of the [Bluetooth Fitness Bracer](https://www.sparkfun.com/news/2062) project.*

### [Slouch Alert Shirt](https://www.instructables.com/lesson/Slouching-and-Triggering-Sound/) by Lara Grant

This posture-sensing wearable is built with a LilyPad, conductive fabric, and vibe board provides feedback when your shoulders hunch forward. Learn how to build this project and more wearables with LilyPad in the [Instructables Wearable Electronics](https://www.instructables.com/class/Wearable-Electronics-Class/) class.

[![Slouch Alert Shirt GIF](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/7/InstructablesSlouch.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/7/InstructablesSlouch.gif)

*GIF of finished Slouch Alert shirt project courtesy of [Wearable Electronics Class](https://www.instructables.com/lesson/Slouching-and-Triggering-Sound/).*

### [Bats Have Feelings Too](https://www.instructables.com/id/Bats-Have-Feelings-Too/) by Lynne Bruning

Lynne created a jacket that uses an [LV-MaxSonar ultrasonic range finder](https://www.sparkfun.com/search/results?term=maxsonar), LilyPad Arduino, and vibe board to alert the wearer to solid objects in their path.

[![Model wearing Bats Have Feelings Too - a haptic jacket for the blind](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/7/BatsJacket.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/7/BatsJacket.jpg)

*\"Bats have feelings too\" coat, a [haptic coat](https://www.instructables.com/id/Bats-Have-Feelings-Too/) for the blind. Photo by Carl Snider.*

### Bristlebots

The LilyPad Vibe Motor is not limited to just haptic feedback. You can also build a neat little bristle bot with the vibe motor, battery holder, and coin cell. You can even add a light sensor and MOSFET to have the robot react to your environment!

[](https://news.sparkfun.com/1778 "March 18, 2015: Want to build a little friend to buzz around your desk? Join us! ")

### SparkFun Live 3/24/15 - Build Your Own Bristlebot! 

[March 18, 2015]

Read Post

[](https://news.sparkfun.com/1783 "March 24, 2015: Join us for another episode of "SparkFun Live!"")

### Build Your Own Bristlebot on today\'s SparkFun Live! 

[March 24, 2015]

Read Post