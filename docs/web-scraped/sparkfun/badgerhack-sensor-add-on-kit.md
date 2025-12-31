# Source: https://learn.sparkfun.com/tutorials/badgerhack-sensor-add-on-kit

## Introduction

The BadgerStick that you received by visiting a SparkFun booth at one of the various events we\'ve attended can be hacked to perform a wide variety of tasks. The BadgerStick is a fully capable microcontroller that can sense the environment around it.

[![BadgerHack](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/badgerboard-02_tag.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/3/badgerboard-02_tag.png)

This tutorial will guide you through turning your BadgerStick into an environment sensing station. We\'ll do so by adding a temperature sensor and a soil moisture sensor.

[![SparkFun BadgerStick and Sensor add-on kit with plant](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/6/Badger_add-on_tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/6/Badger_add-on_tutorial-02.jpg)

*Plant not included*

**NOTE:** The BadgerStick and RedStick are two different products. The BadgerStick (aka BadgerHack) originated as an event-only platform to aid SparkFun in teaching soldering and programming at events like Maker local Faires and SXSW. The [RedStick](https://www.sparkfun.com/products/13741) evolved from that concept and is the retail version of the BadgerStick, available for sale on SparkFun.com. All of the BadgerStick tutorials and expansion kits are compatible with both the BadgerStick and the RedStick, unless otherwise stated.

### Required Materials

On top of your Badgerstick/Redstick and LED array display you will need a few more parts for this project:

\

### Suggested Reading

Before starting this tutorial, we highly recommend you work through the main BadgerHack guide first.

[](https://learn.sparkfun.com/tutorials/badgerhack)

### BadgerHack 

September 23, 2015

This tutorial shows users how to solder their SparkFun interactive badges as well as put them to use in other projects.

Additionally, if you are new to soldering or electronics, we recommend you check out the following:

- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)
- [What is Electricity](https://learn.sparkfun.com/tutorials/what-is-electricity)
- [What is a Circuit](https://learn.sparkfun.com/tutorials/what-is-a-circuit)
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

When you are ready to start hacking your badge, we definitely recommend reading:

- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

## Hardware Hook-up

There is a little bit of soldering, so if you need a quick refresher on that I suggest taking a look at [our soldering tutorial](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering?_ga=1.1425845.564444804.1449868290).

To begin, snap off 15 pins from the break-away headers, and solder them to the through-holes on the side opposite the LED array of the BadgerStick.

[![BadgerStick with headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/6/Badger_add-on_tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/6/Badger_add-on_tutorial-03.jpg)

You can place the headers in the breadboard to help keep them in place as you solder.

[![Soldering BadgerStick with breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/6/Badger_add-on_tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/6/Badger_add-on_tutorial-04.jpg)

The rest of the setup will be using the breadboard and the jumper wires.

Start by sticking the headers you just soldered to your stick at a corner of your breadboard.

Now we will connect the sensors as follows:

+---------------------------+---------------------------------------+
| Component Pin             | Badger/Redstick Pin                   |
+===========================+=========+=========+=========+=========+
| Soil Moisture Sensor VCC  | VCC     |         |         |         |
+---------------------------+---------+---------+---------+---------+
| Soil Moisture Sensor GND  | GND     |         |         |         |
+---------------------------+---------+---------+---------+---------+
| Soil Moisture Sensor SIG  | A0      |         |         |         |
+---------------------------+---------+---------+---------+---------+
| Temperature Sensor left   | GND     |         |         |         |
+---------------------------+---------+---------+---------+---------+
| Temperature Sensor middle | A4      |         |         |         |
+---------------------------+---------+---------+---------+---------+
| Temperature Sensor right  | VCC     |         |         |         |
+---------------------------+---------+---------+---------+---------+

*\* Pins not listed are not used.*\

Here is a picture layout of how to connect everything up

[![Fritzing Diagram of badgerstick badgerhack add-on kit hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/6/Badgerhack_Sensor_add-on_kit_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/6/Badgerhack_Sensor_add-on_kit_bb.jpg)

*Fritzing diagram of a RedStick hookup (GND and VCC slightly different on a BadgerStick).*

[![SparkFun BadgerStick and Sensor Add-on kit layout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/6/Badger_add-on_tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/6/Badger_add-on_tutorial-01.jpg)

**IMPORTANT:** You will need to power your Badgerstick/Redstick through its USB port or a [USB extension cable](https://www.sparkfun.com/products/517), so that the analog sensors are getting a known voltage. You can cut the battery pack off, you can leave the battery pack attached but turned off, or you can power it through the battery pack. Just know that your temp reading will become less accurate the more your battery drains.

With everything hooked up, it\'s time to upload some code.

## Code

Analog sensors work by providing a voltage output that is proportional to the what they are measuring. This means with something like analog temp sensor we are using, the output voltage can be converted to temperature easily using the scale factor of 10 mV/°C. However, a little bit of math is required depending on what the input voltage is, so that will change based on if you are using the Badgerstick at 3.3V or the Redstick at 5V. (But don\'t worry, this has already been done for you in the code.)

The soil moisture sensor works the same way, but we are leaving the data as is, since converting it to something usable like kg of water per kg or soil would be very difficult without knowing what kind of soil you have and how it reacts to electricity.

Plug the USB side of your BadgerStick into your computer. Make sure \"BadgerStick\" and the associated COM port are selected in the Arduino IDE, and click upload.

If you have the Redstick Make sure \"Arduino Uno\" and the associated COM port are selected before uploading. Also if you are using a Redstick, you will need to go into the code and change one variable at the end to have the correct temp output (instructions in the code).

    language:c
    /**
     * BadgerHack Sensor add on kit
     * Sarah Al-Mutlaq @ SparkFun Electronics
     * January 22, 2016
     * 
     * Scrolls temp reading and soil moisture across the Badger's LED array.
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
     *
     *NOTE: for this add on kit, you will want to power the badger
     *through its USB port, so that you know you have 3.3V instead 
     *of an unknown amount from a battery pack, which would make 
     *the temperature reading less accurate. 
     */

    #include <SparkFun_LED_8x7.h>
    #include <Chaplex.h>

    // Global variables
    static byte led_pins[] = ; // Pins for LEDs
    const int moisturePin = A0;     //signal pin from the moisture sensor
                                    //is hooked up to pin A0 on the badger
    const int temperaturePin = A4;  //singnal pin from temp sensor is 
                                    //hooked up to pin A4 of the badger        

    void setup() 

    void loop() 

    float getVoltage(int pin)