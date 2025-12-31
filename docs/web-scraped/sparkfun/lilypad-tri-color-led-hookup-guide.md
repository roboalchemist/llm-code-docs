# Source: https://learn.sparkfun.com/tutorials/lilypad-tri-color-led-hookup-guide

## Introduction

**Heads up!** This tutorial was written for the LilyPad Tri-Color LED with common anode. If you are using the LilyPad RGB LED with common cathode, please refer to the [LilyPad RGB LED Hookup Guide](https://learn.sparkfun.com/tutorials/lilypad-rgb-led-hookup-guide).

The [LilyPad Tri-Color LED](https://www.sparkfun.com/products/8467) is a specialty board that can produce a variety of colors. On the board is an RGB (red-green-blue) LED, made of three tiny LEDs connected together. Each of the colors in the RGB LED are connected to one of the sew tabs on the board labeled as R, G, and B.

[![LilyPad Tri-Color LED](https://cdn.sparkfun.com/r/600-600/assets/parts/8/7/4/08467-01.jpg)](https://www.sparkfun.com/products/8467)

### [LilyPad Tri-Color LED](https://www.sparkfun.com/products/8467) 

[ DEV-08467 ]

Blink any color you need! Use the Tri-Color LED board as a simple indicator, or by pulsing the red, green, and blue channels,...

**Retired**

To follow along with the code examples, we recommend:

### Suggested Reading

To add this LED to a project, you should be comfortable sewing with conductive thread and uploading code to your LilyPad Arduino (for the programming examples). Here are some tutorials to review before working with this part:

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/light)

### Light 

Light is a useful tool for the electrical engineer. Understanding how light relates to electronics is a fundamental skill for many projects.

[](https://learn.sparkfun.com/tutorials/insulation-techniques-for-e-textiles)

### Insulation Techniques for e-Textiles 

Learn a few different ways to protect your conductive thread and LilyPad components in your next wearables project.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

Learn how to use conductive thread with LilyPad components.

[](https://learn.sparkfun.com/tutorials/getting-started-with-lilypad)

### Getting Started with LilyPad 

An introduction to the LilyPad ecosystem - a set of sewable electronic pieces designed to help you build soft, sewable, interactive e-textile projects.

[] **Note on Common Anode vs Common Cathode**\
\
The color channels on this RGB LED are all connected through a common anode (positive) pin. Unlike some other RGB LEDs, this configuration means that to light up the LED you need to ground the individual red, green, and blue LEDs instead of sending them power. For simple circuit hookups, this means you need to connect the R, G, or B sew tabs to ground (-) and in code set them to LOW (for digital output) or 0 (for analog output) to turn them on.\
\

[![Common Anode RGB LED LilyPad Breakout Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/1/Dev_RGBDetail.png)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/1/Dev_RGBDetail.png)

\
\

*The RGB LED on the tri-color LED has 4 connections: red, green, blue channels, and a common anode pin.\
If you look closely you can see the individual LEDs inside the package.*

## Using in a Simple E-Sewing Project

The tri-color LED doesn\'t need to be connected to a microcontroller in order to control it. Here are some examples of using simple circuits to mix colors with the LED.

To experiment with basic color mixing, you can use alligator clips on the tri-color LED\'s sew tabs to temporarily connect them to a power source, such as a [LilyPad Coin Cell Battery Holder](https://www.sparkfun.com/products/13883) with a coin cell battery. Connect the positive tab **(+)** to the positive sew tab on the battery holder with a clip, and each color tab **R** (Red), **G** (Green), and **B** (Blue) to the negative tab **(-)** to connect them. The combination of color sew tabs that are connected to power and illuminated will create a variety of colors.

[![LilyPad Tri-Color LED connected to three alligator clips and a LilyPad Battery Holder](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/5/TriColorLED_SimpleClips.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/5/TriColorLED_SimpleClips.png)

You can replace these connections with switches or buttons for a simple color mixing circuit. After prototyping and testing a project with the tri-color LED you can replace the connections with conductive thread in your project.

[![Tri-Color LED stitched with conductive thread to three LilyPad Switches and a LilyPad Battery Holder](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/5/TriColorLED_SimpleStitched.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/5/TriColorLED_SimpleStitched.png)

*Simple color mixing circuit using a LilyPad Switches connected to each color tab of the tri-color LED.*

## Attaching to a LilyPad Arduino

To follow along with the code examples in this tutorial, connect the tri-color LED to a LilyPad Arduino as shown below. Use alligator clips to temporarily connect the **R** (Red) tab on the LED to **11**, **G** (Green) to **9**, **B** (Blue) to **10**, and **(+)** to **(+)**. When you are finished prototyping, replace the alligator clips with conductive thread traces for permanent installation in your project.

The numbered labels next to the R, G, and B tabs on the tri-color LED were originally made for the LED\'s use on the [LilyPad Development Board](https://www.sparkfun.com/products/11262). To make our diagrams easier to follow, and to avoid any potential short circuits in our stitching, we\'ve chosen different tabs than the labels to connect to in the following code examples.\
\
**Note:** To follow along with the Custom Color Mixing example code, you will need to attach the R, G, and B tabs to a sew tabs on the LilyPad with PWM capabilities.

[![Attaching the Tri-Color LED to a LilyPad Arduino USB](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/5/TriColorLEDHookup_Arduino.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/5/TriColorLEDHookup_Arduino.png)

### Additional Board Hookup

If you\'d like to use the tri-color LED with the [LilyPad ProtoSnap Plus](https://www.sparkfun.com/products/14346), attach the R, G, and B tabs to the ProtoSnap\'s expansion ports. Only port 10 has PWM capabilities, so you will not be able to follow along with the Custom Color Mixing example unless you snap the ProtoSnap Plus apart and connect the tri-color LED directly to tabs on the LilyPad USB Plus.

If using the the pre-wired tri-color LED on the [ProtoSnap - LilyPad Development Board](https://www.sparkfun.com/products/11262), the connection is different than what was explained earlier. R is attached to 9, G is attached to 11, and B is attached to 10. We recommend checking out the [LilyPad Development Board Activity Guide](https://learn.sparkfun.com/tutorials/lilypad-development-board-activity-guide/2-basic-color-mixing) for step-by-step examples using this LED.

## Basic Color Mixing with Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

This example code demonstrates how to display a simple rainbow of colors using the tri-color LED. In order to create colors with the RGB LED, you\'ll have to set each of the LEDs within it individually. The combination of light from the LEDs mixed together creates new colors.

Upload the following code to your LilyPad Arduino, making sure to select the correct LilyPad board from the drop down menu below. Choose **LilyPad Arduino USB** if using a LilyPad Arduino USB. The LilyPad Arduino Simple, LilyPad Arduino, and LilyPad Development Board, and Development Board Simple all use a **LilyPad ATmega 328**. Select **LilyPad USB Plus** if following along with the LilyPad ProtoSnap Plus.

Copy and paste the following code into the Arduino IDE and upload it to your LilyPad Arduino.

    language:c
    /*
    LilyPad Tri-Color LED: Basic Color Mixing
    SparkFun Electronics
    https://www.sparkfun.com/products/8467

    Create primary and secondary colors on the tri-color (Red/Green/Blue)
    LED connected to a LilyPad Arduino.

    Tri-Color LED connections:
    * R pin to 11
    * G pin to 10
    * B pin to 9
    * + pin to +

    This code is released under the MIT License (http://opensource.org/licenses/MIT)

    ******************************************************************************/

    // This example uses a tri-color, also known as an RGB 
    // (Red / Green / Blue) LED.
    // This example uses digitalWrite to turn the three LEDs on and off
    // in various combinations to create eight primary and secondary colors.

    // Create integer variables for our LED pins:

    int RGB_red = 11;
    int RGB_green = 10;
    int RGB_blue = 9;

    void setup()
    

    void loop()
    

After uploading your code, the RGB LED will step through a color sequence beginning with all LEDs off (\'black\'), red, yellow, green, cyan, blue, magenta, and white. Once the color sequence is complete, the program will loop back to the beginning and repeat the sequence.

Turning on different combinations of three LEDs inside the RGB LED will create new colors. Combining the primary colors of light (red, green, and blue) gives different results than combining pigments in paints or inks. Turning on all three colors will create white - this is called [additive color](https://en.wikipedia.org/wiki/Additive_color). Take a look a the graphic below to see what colors combine to create primary and secondary colors with light.

[![Venn Diagram for Additive Colors ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/0/RGB_ColorMix.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/0/RGB_ColorMix.jpg)

## Custom Color Mixing with Code

In this example, you will but use `analogWrite()` function to change the brightness of each channel in relation to each other. Adjusting the brightness of the red, green, and blue LEDs within the LED will allow you to create a new range of values and color combinations. You will need to confirm that the sew tabs you connect to the tri-color LED have PWM capabilities - this code will run on a LilyPad Arduino USB, LilyPad Arduino Simple, LilyPad Arduino SimpleSnap, and LilyPad Main board without any changes needed.

In the last example, you created basic primary and secondary colors by turning the red, green, and blue channels on or off with different combinations. In this activity, you\'ll create [tertiary colors](https://en.wikipedia.org/wiki/Tertiary_color) by combining the three color channels at 50% brightness levels. There are actually millions of color combinations available using RGB LEDs once you begin experimenting by adjusting the brightness/saturation of each channel. This example will cover a set of twelve tertiary colors.

Copy and paste the following code into the Arduino IDE and upload to your LilyPad Arduino.

    language:c
    /*
    LilyPad Tri-Color LED: Custom Color Mixing
    SparkFun Electronics
    https://www.sparkfun.com/products/8467

    Expand your color options using analogWrite and the LilyPad Tri-Color LED

    Tri-Color LED connections:
    * R pin to 11
    * G pin to 10
    * B pin to 9
    * + pin to +

    This code is released under the MIT License (http://opensource.org/licenses/MIT)

    ******************************************************************************/
    // In this example we'll use analogWrite to control the brightness of the three channels
    // of the tri-color LED.
    // Here we'll create a rainbow of tertiary colors by adding a 50%-brightness option.

    // Create integer variables for our LED pins:

    int RGB_red = 11;
    int RGB_green = 10;
    int RGB_blue = 9;

    void setup() 

    void loop()
    

After uploading your code the RGB LED will step through a rainbow sequence of red, orange, yellow, chartruese, green, spring green, cyan, azure, blue, violet, magenta, and rose, repeatedly.

By adjusting the brightness of each LED in the RGB LED individually, we open up a much wider range of color options to display than the previous example. In fact, there are many more combinations than we show in the example code. The image below shows a chart of the tertiary colors the example program creates by stepping down the LEDs to half brightness, creating a rainbow with more color transitions than the Basic Color Mixing example. By using analog output to adjust the brightness of each color channel individually, the RGB LED can display almost any color you can choose from a color picker - if you are familiar with RGB sliders in a graphics program, you\'ll recognize the 0-255 values used in this code.

[] **Remember the Tri-Color LED is Common Anode**\
\
In a typical `analogWrite()` function, 0 is 0% (OFF) and 255 100% (ON), but because the tri-color LED is common anode, in the code we\'ll use 0 for 100% (ON) and 255 for 0% (OFF). Refer to the chart below for color mixing values specifically for the tri-color LED.

[![Tertiary Colors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/1/TertiaryColors.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/1/TertiaryColors.png)

## Project Examples

Need some inspiration for your next project? Check out some of the projects below:

### Light Up Silk Flower Corsage

This tutorial uses a specialty [Silk Flower LED](https://www.sparkfun.com/products/13270) with embedded RGB LED in it, but functions similar to the example circuit above. You can create a similar project using a tri-color LED and your own flower or fabric covering.

[](https://learn.sparkfun.com/tutorials/light-up-silk-flower-corsage)

### Light Up Silk Flower Corsage 

April 20, 2015

Combine a silk flower with a built-in RGB LED and some LilyPad Switches to create a customizable accessory.

### Color Changing LED Brooch by Becky Stern

In this project for [Craftzine](https://makezine.com/2009/05/08/craft_video_color_changing_led/), Becky uses three potentiometers to make a customizable colored LED brooch using the tri-color LED.

\
\

### Skirt Full of Stars by Shannon Henry

This skirt reacts to movement and displays in color with tri-color LEDs and fiber optic strands. It uses a [LilyPad Accelerometer](https://www.sparkfun.com/products/9267) connected to a [LilyPad Arduino Main Board](https://www.sparkfun.com/products/13342) to sense movement while being worn.

[![Skirt Full of Stars project by Shannon Henry](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/5/SkirtFullofStars.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/5/SkirtFullofStars.jpg)

*Photo courtesy of [PolyMath Design Lab](http://www.polymathdesignlab.com/etextiles/starskirt/)*