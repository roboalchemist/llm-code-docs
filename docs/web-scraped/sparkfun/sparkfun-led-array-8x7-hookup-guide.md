# Source: https://learn.sparkfun.com/tutorials/sparkfun-led-array-8x7-hookup-guide

## Introduction

The [LED Array (8x7)](https://www.sparkfun.com/products/13795) is a set of 56 LEDs arranged in a nice 8x7 grid. It relies on [Charlieplexing](https://en.wikipedia.org/wiki/Charlieplexing) to control individual LEDs, which means less GPIO pins are used (as opposed to a traditional [grid format](http://www.appelsiini.net/2011/how-does-led-matrix-work)). This guide will walk you through connecting the LED array and using some code examples to make those LEDs light up. We even wrote a library to help you display some simple graphics and scrolling text!

**IMPORTANT:** For the time being, the library for this board only supports ATmega 168 and 328-based Arduinos (e.g. UNO, RedBoard, Pro, Pro Mini, etc.). You can still use the LED Array board with other platforms, just not the library.

[![SparkFun LED Array - 8x7](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/3/6/9/13795-01.jpg)](https://www.sparkfun.com/products/13795)

### [SparkFun LED Array - 8x7](https://www.sparkfun.com/products/13795) 

[ COM-13795 ]

The SparkFun LED Array is a set of 56 red LEDs arranged in a nice 8x7 grid. This little board requires eight pins while the l...

**Retired**

### Required Materials

To follow along with this guide, you will need the following additional parts:

### Suggested Reading

If any of these subjects sound unfamiliar, considering reading the following tutorials before continuing on.

- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)
- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [How to Solder - Through-hole Soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

## Board Overview

### How Charlieplexing Works

To understand how the LED Array (8x7) works, we need to first learn a little about Charlieplexing. The name came from Charlie Allen at [Maxim Integrated](https://en.wikipedia.org/wiki/Maxim_Integrated), who proposed the solution in 1995 for controlling multiple LEDs with less pins from a microcontroller.

The technique relies on using the ability for microcontroller pins to enter into a high impedance state (tri-state) and thus prevent current from entering or leaving that pin. Let\'s take a 3-pin example. With Charlieplexing, we can have 6 LEDs attached to 3 pins: `n x (n - 1) = 3 x (3 - 1) = 6`.

[![Charlieplexing 6 LEDs](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/Charlie.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/Charlie.png)

We need to use the microcontroller\'s ability to tri-state pins to make this work. If we make pin 1 an output and high, pin 2 output and low, and pin 3 high impedance (\"Hi-Z\"), then D1 will light up.

[![Lighting up first LED with Charlieplexing](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/Charlie_1to2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/Charlie_1to2.png)

If we switch it and make pin 2 high and pin 1 low, then D3 will light up.

[![Lighting up D3 with Charlieplexing](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/Charlie_2to1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/Charlie_2to1.png)

And if we make pin 3 high, pin 2 low, and pin 1 Hi-Z, D6 will light up.

[![Lighting up D6 with Charlieplexing](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/Charlie_3to2a.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/Charlie_3to2a.png)

This works because we can make the unused pins high impedance from the microcontroller. High impedance mode looks like an open circuit, so current does not flow into or out from the Hi-Z pins.

If we cycle through all 6 permutations quickly enough, we can trick our eyes into thinking that all the LEDs are on. If we leave selected LEDs off, we can create simple images with our LED array!

[![Shape on LED Array](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/8/LED_Array_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/LED_Array_Hookup_Guide-03.jpg)

### The LED Array 8x7

[![Top of LED Array 8x7](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/LED_Array_Product_top.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/LED_Array_Product_top.jpg)

The 8x7 LED array takes our 6-LED example and expands it out to 56 LEDs and 8 pins. We can cycle through all 56 permutations of the pins to turn each LED on individually, and if we cycle fast enough, we can create simple images and text (at least according to our eyes).

## Hardware Setup

The LED Array can be connected many ways so long as you have 8 pins available on your Arduino. For this example, we are going to use a RedBoard and pins 2-9. Solder 8 male header pins facing away from the LEDs:

[![Male header pins on the LED Array](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/8/LED_Array_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/LED_Array_Hookup_Guide-01.jpg)

Attach the LED Array to a breadboard and connect pins 2-9 on the RedBoard to pins A-H, respectively:

[![LED Array Fritzing diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/8/LED_Array_and_RedBoard_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/LED_Array_and_RedBoard_bb.png)

Note that you can also solder right-angle headers to the LED Array and [RedStick](https://www.sparkfun.com/products/13741) or [Pro Mini](https://www.sparkfun.com/products/11113) (again, pins A-H attached to pins 2-9) to achieve a seamless look:

[![LED Array on the RedStick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/8/LED_Array_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/LED_Array_Hookup_Guide-02.jpg)

## Code Example

Now that we have the LED Array connected to our Arduino, we can run a simple test to make sure it is working. This example doesn\'t require any additional libraries. Simply plug the shield into your Arduino, and upload the example code. Should you want to read how to install the libraries manually with Arduino, skip to [the next section](https://learn.sparkfun.com/tutorials/sparkfun-led-array-8x7-hookup-guide#arduino-library).

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

    language:c
    /**
     * BadgerHack Hello World
     * Shawn Hymel @ SparkFun Electronics
     * September 23, 2015
     * 
     * Scrolls "Hello world" across the Badger's LED array.
     * 
     * License: http://opensource.org/licenses/MIT
     * 
     * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
     * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
     * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
     * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
     * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
     * THE SOFTWARE.
     */

    #include <SparkFun_LED_8x7.h>
    #include <Chaplex.h>

    // Global variables
    static byte led_pins[] = ; // Pins for LEDs

    void setup() 

    void loop() 

Your LED Array should scroll \"Hello World.\"

[![Hello World on the LED Array](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/8/LED_Array_Hookup_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/LED_Array_Hookup_Guide-04.jpg)

## Arduino Library

You can manually download the LED Array 8x7 Arduino library. To start, we\'ll need the [Chaplex library](https://code.google.com/archive/p/yacll/):

[Download the Chaplex library](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/yacll/Chaplex.zip)

Additionally, we need the LED Array 8x7 Arduino library, which you can download as a ZIP file from [GitHub](https://github.com/sparkfun/SparkFun_LED_Array_8x7_Arduino_Library) or directly from this link:

[Download the SparkFun LED Array 8x7 Arduino library](https://github.com/sparkfun/SparkFun_LED_Array_8x7_Arduino_Library/archive/master.zip)

Once you have both libraries downloaded, follow [this guide](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) to install them in Arduino.

Open the Arduino IDE, and select **File \> Examples \> SparkFun LED Array 8x7 \> Demo**. Select your Arduino and serial port, and upload the program.

[![LED Array Arduino demo](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/Demo.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/Demo.png)

You should see the LED array scroll through some example text and graphics.

[![SparkFun logo on the LED Array](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/8/LED_Array_Hookup_Guide-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/8/LED_Array_Hookup_Guide-05.jpg)