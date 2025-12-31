# Source: https://learn.sparkfun.com/tutorials/lilypad-rgb-led-hookup-guide

## Introduction

**Heads up!** This tutorial was written for the LilyPad RGB LED with common cathode. If you are using the LilyPad Tri-Color LED with common anode, please refer to the [LilyPad Tri-Color LED Hookup Guide](https://learn.sparkfun.com/tutorials/lilypad-tri-color-led-hookup-guide).

The [LilyPad RGB LED](https://www.sparkfun.com/products/13735) is a specialty board that can produce a variety of colors. On the board is an RGB (red-green-blue) LED, made of three tiny LEDs connected together. Each of the colors in the RGB LED are connected to one of the sew tabs on the board labeled R, G, and B.

[![LilyPad RGB LED](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/2/4/6/13735-LilyPad_Tri-Color_LED-04b.jpg)](https://www.sparkfun.com/lilypad-rgb-led.html)

### [LilyPad RGB LED](https://www.sparkfun.com/lilypad-rgb-led.html) 

[ DEV-13735 ]

Blink any color you need!

[ [\$5.75] ]

### Required Materials

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
The color channels on this RGB LED are all connected through a common cathode (negative) pin. This configuration means that the individual red, green, and blue LEDs share a common ground tab. To light up each color individual LED, connect them each to a power source. For simple circuit hookups, this means you need to connect the R, G, or B sew tabs to power (+) and in code set them to HIGH (for digital output) or 255 (for analog output) to turn them on.\
\

[![Common Anode RGB LED LilyPad Breakout Board](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/5/RGB_Common_Cathode_LED_Zoomed-in-Vector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/5/RGB_Common_Cathode_LED_Zoomed-in-Vector.jpg)

\
\

*The RGB LED has 4 connections: red, green, blue channels, and a common cathode pin.\
If you look closely you can see the individual LEDs inside the package.*

## Using in a Simple E-Sewing Project

The RGB LED doesn\'t need to be connected to a microcontroller in order to control it. Here are some examples of using simple circuits to mix colors with the LED.

To experiment with basic color mixing, you can use alligator clips on the RGB LED\'s sew tabs to temporarily connect them to a power source, such as a [LilyPad Coin Cell Battery Holder](https://www.sparkfun.com/products/13883) with a coin cell battery. Connect the negative tab **(-)** to the negative sew tab on the battery holder with a clip, and each color tab **R** (Red), **G** (Green), and **B** (Blue) to the postivie tab **(+)** to connect them. The combination of color sew tabs that are connected to power will create a variety of colors.

[![LilyPad RGB LED connected to three alligator clips and a LilyPad Battery Holder](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/5/LilyPad_RGB_Common-Cathode_LED_SimpleClips.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/5/LilyPad_RGB_Common-Cathode_LED_SimpleClips.jpg)

You can replace these connections with switches or buttons for a simple color mixing circuit. After prototyping and testing a project with the RGB LED, you can replace the connections with conductive thread in your project.

[![RGB LED stitched with conductive thread to three LilyPad Switches and a LilyPad Battery Holder](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/5/LilyPad_RGB_Common-Cathode_LED_SimpleStitched.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/5/LilyPad_RGB_Common-Cathode_LED_SimpleStitched.jpg)

*Simple color mixing circuit using a LilyPad Switches connected to each color tab of the RGB LED.*

## Attaching to a LilyPad Arduino

To follow along with the code examples in this tutorial, connect the RGB LED to a LilyPad Arduino as shown below. Use alligator clips to temporarily connect the **R** (Red) tab on the LED to **11**, **G** (Green) to **10**, **B** (Blue) to **9**, and **(-)** to **(-)**. When you are finished prototyping, replace the alligator clips with conductive thread traces for permanent installation in your project.

**Note:** To follow along with the Custom Color Mixing example code, you will need to attach the R, G, and B tabs to a sew tabs on the LilyPad with PWM capabilities. In this case, we are using a [LilyPad Arduino USB](https://www.sparkfun.com/products/12049) with an ATmega32U4.

[![Attaching the RGB LED to a LilyPad Arduino USB](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/5/LilyPad_RGB_Common-Cathode_LED_Simple_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/5/LilyPad_RGB_Common-Cathode_LED_Simple_Arduino.jpg)

### Additional Board Hookup

If you\'d like to use RGB LED with the [LilyPad ProtoSnap Plus](https://www.sparkfun.com/products/14346), attach the R, G, and B tabs to the ProtoSnap\'s expansion ports. You will not be able to follow along with the Custom Color Mixing example unless you snap the ProtoSnap Plus apart and connect the RGB LED directly to tabs on the LilyPad USB Plus on pin 6, A7, and A8. Make sure to adjust the pins definitions in the example code when using the LilyPad ProtoSnap Plus.

## Basic Color Mixing with Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

This example code demonstrates how to display a simple rainbow of colors using the RGB LED. In order to create colors with the RGB LED, you\'ll have to set each of the LEDs within it individually. The combination of light from the LEDs mixed together creates new colors.

Upload the following code to your LilyPad Arduino, making sure to select the correct LilyPad board from the drop down menu below. Choose **LilyPad Arduino USB** if using a LilyPad Arduino USB. The LilyPad Arduino Simple, LilyPad Arduino, and LilyPad Development Board, and Development Board Simple all use a **LilyPad ATmega 328**. Select **LilyPad USB Plus** if following along with the LilyPad ProtoSnap Plus.

Copy and paste the following code into the Arduino IDE and upload it to your LilyPad Arduino.

    language:c
    /*
      LilyPad Tri-Color LED: Basic Color Mixing
      Written by: Gella and Ho Yun "Bobby" Chan
      SparkFun Electronics
      https://www.sparkfun.com/products/13735

      Create primary and secondary colors on the tri-color (Red/Green/Blue)
      LED connected to a LilyPad Arduino.

      Tri-Color LED connections:
      R pin to 11
      G pin to 10
      B pin to 9
      - pin to -

      This code is released under the MIT License (http://opensource.org/licenses/MIT)

    ******************************************************************************/

    // This example uses a tri-color, also known as an RGB
    // (Red / Green / Blue) LED.
    // This example uses digitalWrite() to turn the three LEDs on and off
    // in various combinations to create eight primary and secondary colors.

    //debug mode, comment one of these lines out using a syntax for a single line comment: //
    #define DEBUG 0     //0 = LEDs only
    //#define DEBUG 1     //1 = LEDs w/ serial output

    // Create integer variables for our LED pins:
    #define RGB_red 11
    #define RGB_green 10
    #define RGB_blue 9

    void setup() //end setup()

    void loop() //end loop

After uploading your code, the RGB LED will step through a color sequence beginning with all LEDs off (\'black\'), red, yellow, green, cyan, blue, magenta, and white. Once the color sequence is complete, the program will loop back to the beginning and repeat the sequence.

Turning on different combinations of three LEDs inside the RGB LED will create new colors. Combining the primary colors of light (red, green, and blue) gives different results than combining pigments in paints or inks. Turning on all three colors will create white - this is called [additive color](https://en.wikipedia.org/wiki/Additive_color). Take a look a the graphic below to see what colors combine to create primary and secondary colors with light.

[![Venn Diagram for Additive Colors ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/0/RGB_ColorMix.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/0/RGB_ColorMix.jpg)

## Custom Color Mixing with Code

In this example, you will but use `analogWrite()` function to change the brightness of each channel in relation to each other. Adjusting the brightness of the red, green, and blue LEDs within the LED will allow you to create a new range of values and color combinations. You will need to confirm that the sew tabs you connect to the RGB LED have PWM capabilities - this code will run on a LilyPad Arduino USB, LilyPad Arduino Simple, LilyPad Arduino SimpleSnap, and LilyPad Main board without any changes needed.

In the last example, you created basic primary and secondary colors by turning the red, green, and blue channels on or off with different combinations. In this activity, you\'ll create [tertiary colors](https://en.wikipedia.org/wiki/Tertiary_color) by combining the three color channels at 50% brightness levels. There are actually millions of color combinations available using RGB LEDs once you begin experimenting by adjusting the brightness/saturation of each channel. This example will cover a set of twelve tertiary colors and white.

Copy and paste the following code into the Arduino IDE and upload to your LilyPad Arduino.

    language:c
    /*
      LilyPad RGB LED: Custom Color Mixing
      Written by: Gella and Ho Yun "Bobby" Chan
      SparkFun Electronics
      https://www.sparkfun.com/products/13735

      Expand your color options using analogWrite and the LilyPad RGB LED

      RGB LED connections:
      R pin to 11
      G pin to 10
      B pin to 9
      - pin to -

      This code is released under the MIT License (http://opensource.org/licenses/MIT)

    ******************************************************************************/
    // In this example we'll use analogWrite to control the brightness of the three channels
    // of the RGB LED.
    // Here we'll create a rainbow of tertiary colors by adding a 50%-brightness option.

    //debug mode, comment one of these lines out using a syntax for a single line comment: //
    //#define DEBUG 0     //0 = LEDs only
    #define DEBUG 1     //1 = LEDs w/ serial output

    // Create integer variables for our LED pins:
    #define RGB_red 11
    #define RGB_green 10
    #define RGB_blue 9

    void setup() //end setup()

    void loop()
    //end loop

After uploading your code the RGB LED will step through a rainbow sequence of red, orange, yellow, chartruese, green, spring green, cyan, azure, blue, violet, magenta, rose, and white repeatedly.

By adjusting the brightness of each LED in the RGB LED individually, we open up a much wider range of color options to display than the previous example. In fact, there are many more combinations than we show in the example code. The image below shows a chart of the tertiary colors the example program creates by stepping down the LEDs to half brightness, creating a rainbow with more color transitions than the Basic Color Mixing example. By using analog output to adjust the brightness of each color channel individually, the RGB LED can display almost any color you can choose from a color picker - if you are familiar with RGB sliders in a graphics program, you\'ll recognize the 0-255 values used in this code.

[![Tertiary Color Wheel Chart](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/0/TertiaryColorWheel_Chart.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/0/TertiaryColorWheel_Chart.png)

## Project Examples

Need some inspiration for your next project? Check out some of the projects below. Just make sure to adjust the connections when using the common cathode RGB LED.

### Light Up Silk Flower Corsage

This tutorial uses a specialty [Silk Flower LED](https://www.sparkfun.com/products/13270) with embedded RGB LED in it, but functions similar to the example circuit above. You can create a similar project using an RGB LED and your own flower or fabric covering.

[](https://learn.sparkfun.com/tutorials/light-up-silk-flower-corsage)

### Light Up Silk Flower Corsage 

April 20, 2015

Combine a silk flower with a built-in RGB LED and some LilyPad Switches to create a customizable accessory.

### Color Changing LED Brooch by Becky Stern

In this project for [Craftzine](https://makezine.com/2009/05/08/craft_video_color_changing_led/), Becky uses three potentiometers to make a customizable colored LED brooch using the RGB LED.

\
\

### Skirt Full of Stars by Shannon Henry

This skirt reacts to movement and displays in color with RGB LEDs and fiber optic strands. It uses a [LilyPad Accelerometer](https://www.sparkfun.com/products/9267) connected to a [LilyPad Arduino Main Board](https://www.sparkfun.com/products/13342) to sense movement while being worn.

[![Skirt Full of Stars project by Shannon Henry](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/5/SkirtFullofStars.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/5/SkirtFullofStars.jpg)

*Photo courtesy of [PolyMath Design Lab](http://www.polymathdesignlab.com/etextiles/starskirt/)*