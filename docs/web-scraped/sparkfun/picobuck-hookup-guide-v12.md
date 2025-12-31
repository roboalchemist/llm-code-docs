# Source: https://learn.sparkfun.com/tutorials/picobuck-hookup-guide-v12

## Introduction

Please note that this tutorial is for the newest version of the PicoBuck, V12. If you have an older version of the PicoBuck, please refer to [this tutorial](https://learn.sparkfun.com/tutorials/picobuck-hookup-guide).

------------------------------------------------------------------------

Developed in collaboration with [Ethan Zonca of protofusion](http://protofusion.org/wordpress/), the [PicoBuck](https://www.sparkfun.com/products/13705) is a small-size, triple-output, constant current LED driver. By default, each channel is driven at 330mA; that current can be reduced by either presenting an analog voltage or a PWM signal to the board. Version 12 of the board adds a solderable jumper that can be closed to increase the maximum current to 660mA. It also increased the voltage rating on the various components on the board, allowing the board to be used up to the full 36V rating of the AL8860 part.

It\'s important to note that the PicoBuck is designed for lighting either single LEDs or LEDs in series. Most LED strips are designed to be fed by a constant voltage and should not be used with the PicoBuck.

[![PicoBuck LED Driver](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/1/8/9/13705-01.jpg)](https://www.sparkfun.com/picobuck-led-driver.html)

### [PicoBuck LED Driver](https://www.sparkfun.com/picobuck-led-driver.html) 

[ COM-13705 ]

The PicoBuck LED Driver is an economical and easy to use driver that will allow you to control and blend three different LEDs...

[ [\$17.50] ]

### Suggested Reading

Here are some topics you should know before using the PicoBuck. Have a look if you need more information.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/resistors)

### Resistors 

A tutorial on all things resistors. What is a resistor, how do they behave in parallel/series, decoding the resistor color codes, and resistor applications.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

[](https://learn.sparkfun.com/tutorials/electric-power)

### Electric Power 

An overview of electric power, the rate of energy transfer. We\'ll talk definition of power, watts, equations, and power ratings. 1.21 gigawatts of tutorial fun!

## PicoBuck Overview

Since the PicoBuck is a constant current driver, the current drawn from the supply will drop as supply voltage rises. At 12V, the PicoBuck drives the three LEDs on our [Luxeon Rebel Triple Play board](https://www.sparkfun.com/products/9738) at 350mA per LED while drawing less than 350mA **total** from the power supply. You can also use the board to drive any high power LED like the ones listed below. The PicoBuck is perfect for using with the triple output high power RGB LED or driving a few high power LEDs in series.

[![Triple Output High Power RGB LED](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/2/4/15200-Triple_Output_High_Power_RGB_LED-01.jpg)](https://www.sparkfun.com/triple-output-high-power-rgb-led.html)

### [Triple Output High Power RGB LED](https://www.sparkfun.com/triple-output-high-power-rgb-led.html) 

[ COM-15200 ]

This 3W per channel, Triple Output High Power RGB LED is sure to shed a lot of light on any project you add it to.

[ [\$6.95] ]

[![LED - 3W Aluminum PCB (5 Pack, Warm White)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/1/5/3/13104-00.jpg)](https://www.sparkfun.com/led-3w-aluminum-pcb-5-pack-warm-white.html)

### [LED - 3W Aluminum PCB (5 Pack, Warm White)](https://www.sparkfun.com/led-3w-aluminum-pcb-5-pack-warm-white.html) 

[ COM-13104 ]

So much power and light from such a small package. This 5 pack of \"Warm\" white 3 Watt aluminum backed PCBs is sure to shed a ...

[ [\$12.45] ]

[![LED - 3W Aluminum PCB (5 Pack, Cool White)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/1/5/4/13105-00.jpg)](https://www.sparkfun.com/led-3w-aluminum-pcb-5-pack-cool-white.html)

### [LED - 3W Aluminum PCB (5 Pack, Cool White)](https://www.sparkfun.com/led-3w-aluminum-pcb-5-pack-cool-white.html) 

[ COM-13105 ]

So much power and light from such a small package. This 5 pack of \"Cool\" white 3 Watt aluminum backed PCBs is sure to shed a ...

[ [\$12.45] ]

[![LED - 3W Aluminum PCB (5 Pack, Red)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/1/5/5/13106-00.jpg)](https://www.sparkfun.com/products/13106)

### [LED - 3W Aluminum PCB (5 Pack, Red)](https://www.sparkfun.com/products/13106) 

[ COM-13106 ]

So much power and light from such a small package. This 5 pack of red 3 Watt aluminum backed PCBs is sure to shed a lot of li...

**Retired**

[![LED - 3W Aluminum PCB (5 Pack, Blue)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/1/5/6/13107-00.jpg)](https://www.sparkfun.com/products/13107)

### [LED - 3W Aluminum PCB (5 Pack, Blue)](https://www.sparkfun.com/products/13107) 

[ COM-13107 ]

So much power and light from such a small package. This 5 pack of blue 3 Watt aluminum backed PCBs is sure to shed a lot of l...

**Retired**

[![LED - 3W Aluminum PCB (5 Pack, Green)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/3/2/2/13185-01.jpg)](https://www.sparkfun.com/products/13185)

### [LED - 3W Aluminum PCB (5 Pack, Green)](https://www.sparkfun.com/products/13185) 

[ COM-13185 ]

So much power and light from such a small package. This 5 pack of green 3 Watt aluminum backed PCBs is sure to shed a lot of ...

**Retired**

### Control Pins

Three signal inputs are provided for dimming control. You can use the PWM signal from an Arduino or your favorite microcontroller to dim each channel individually, or you can tie them all to the same PWM for simultaneous dimming. A separate ground pin (labeled GND) is provided to reference against the controlling module for accuracy. The pin spacing for the two pairs of pins is 0.1\", but the two pairs are slightly 0.2\" apart, to allow for a [2.54mm pitch screw terminal pair](https://www.sparkfun.com/products/10571) to be used, or for a five-position standard 0.1\" header with the middle pin removed.

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Long Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/4/4/5/2/10158-01.jpg)](https://www.sparkfun.com/break-away-headers-long.html)

### [Long Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-long.html) 

[ PRT-10158 ]

These are a longer version of our \[standard\](http://www.sparkfun.com/commerce/product_info.php?products_id=116) break away he...

[ [\$3.50] ]

[![Screw Terminals 2.54mm Pitch (2-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/5/2/0/4/10571-01.jpg)](https://www.sparkfun.com/screw-terminals-2-54mm-pitch-2-pin.html)

### [Screw Terminals 2.54mm Pitch (2-Pin)](https://www.sparkfun.com/screw-terminals-2-54mm-pitch-2-pin.html) 

[ PRT-10571 ]

These are simple 2-position screw terminals with 2.54mm pitch pins. Rated up to 150V @ 6A, this terminal can accept 30 to 18A...

[ [\$0.95] ]

Dimming can be done by an analog voltage (20%-100% of max current by varying voltage from 0.0V-2.5V) or by PWM (so long as PWM minimum voltage is less than 0.4V and maximum voltage is more than 2.4V but not more than 5V) for a full 0-100% range. Avoid analog voltages above 5V, as these may damage the part.

[![Signal Inputs](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/Pico_02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/Pico_02.png)

*Signal Inputs*

### Input Voltage (VIN)

The power supply pads are sized for 3.5mm screw terminals as are the output pads.

[![Power Input](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/Pico_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/Pico_01.png)

*Power Input*

[3.5mm screw terminals](https://www.sparkfun.com/products/8084) or [hookup wire](https://www.sparkfun.com/products/11367) can be used to connect to the pins depending on your personal preference.

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/2/0/11375-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html)

### [Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html) 

[ PRT-11375 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of stranded wire in a cardboard dispens...

[ [\$23.95] ]

[![Screw Terminals 3.5mm Pitch (2-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/7/08084-01.jpg)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-2-pin.html)

### [Screw Terminals 3.5mm Pitch (2-Pin)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-2-pin.html) 

[ PRT-08084 ]

Screw Terminal 3.5mm pitch pins with slide-locking together to form any size you need. Rated up to 125V @ 6A, and can accept ...

[ [\$1.25] ]

### Channel Outputs

The output pads are also sized for 3.5mm screw terminals. Each output is independent from the other two.

[![Output Pads](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/Pico_05.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/Pico_05.png)

*Output Pads*

**Note:** The PicoBuck **cannot** be used to drive a common anode or common cathode LED or LED string, and the individual channel +/- pads **must not** be connected to one another.

#### Default Current Output Per Channel

A small jumper is provided for each channel to allow you to increase the drive strength from 330mA to 660mA. More information on this can be found below.

[![Solder Jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/Pico_03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/Pico_03.png)

*Solder Jumpers*

#### Alternative Current Output

It is possible to increase the maximum current of the PicoBuck board up to 1A per channel; to do so, replace the three current sense resistors with smaller values. To calculate the new value for the resistor, use this formula:

**I~LED~ = 0.1 / R~set~**

Thus, for a 1A current, you\'d want a 0.1Ω resistor. Don\'t forget to be wary of current ratings. At 1A, the sense resistor will be dissipating 1/10W, so you probably want a resistor of at least 1/8W rating. The package is a standard 0805.

[![Current Set Resistors](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/Pico_04.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/Pico_04.png)

*Current Set Resistors*

#### Closing the Current Setting Jumpers

[![Demonstration of closed jumpers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/4/3/picobuck_jumpers.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/picobuck_jumpers.png)

As you can see from the image above, the solder jumper doesn\'t need to be closed particularly neatly. All of the pads in its vicinity are connected to it anyway, so if you glob a little extra solder on, it\'s no big deal. Just be careful not to actually short the resistors, as in the rightmost circuit!

### Mounting Holes

Two mounting holes for 4-40 or M3 screws are provided on either side of the board. They are perforated so they can be easily snapped off with a pair of pliers, if a smaller footprint is desired.

[![Mounting Holes](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/Pico_06.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/Pico_06.png)

*Mounting Holes*

## Dimming with a Microcontroller

As mentioned earlier, the PicoBuck\'s three channels can be individually dimmed by either varying the input voltage of the channel from 0-2.5V or using a PWM signal. You could use a preprogrammed microcontroller like the capacitive touch potentioemter or custom control each channel using any microcontroller with PWM outputs.

### Pre-Programmed Capacitive Touch Potentiometer

If you are looking for a preprogrammed microcontroller with capacitive touch capabilities, check out the [Touch Potentiometer](https://learn.sparkfun.com/tutorials/touch-potentiometer-hookup-guide#example-1-pwm-lighting-controller). There is additional software that can be used to fine tune the settings of the capacitive touch potentiometer.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Touch Potentiometer Controlling the PicoBuck](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/8/Touch_Potentiometer_Tutorial-10.jpg)](https://learn.sparkfun.com/tutorials/touch-potentiometer-hookup-guide#example-1-pwm-lighting-controller)
  *Touch Potentiometer for [PWM Lighting Controller](https://learn.sparkfun.com/tutorials/touch-potentiometer-hookup-guide#example-1-pwm-lighting-controller)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Arduino

Otherwise, the PWM signal from an Arduino board is also perfectly suited for this.

#### Connecting One LED Per Channel

Here\'s a diagram showing how to connect the PicoBuck to an Arduino.

[![Arduino connection with one LED per channel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/4/3/picobuck_1led.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/picobuck_1led.png)

Note that each channel must be independently connected to the + and - connections of the LED it is to drive! **Do not** connect the + or - connections of any two channels together.

**Note:** When using an external supply for the PicoBuck, the grounds of the two boards must be connected! If the power supply is 12V or less, the Arduino can be powered from it as well, but do not attempt to power the PicoBuck from the Arduino if you are using anything higher! Below are a few power options and accessories that can be used with the PicoBuck\
\

[![DC Barrel Jack Adapter - Female](https://cdn.sparkfun.com/r/140-140/assets/parts/4/6/8/4/10288-02.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html)

### [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html) 

[ PRT-10288 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.75] ]

[![Wall Adapter Power Supply - 9VDC 650mA](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/5/00298-01a.jpg)](https://www.sparkfun.com/products/298)

### [Wall Adapter Power Supply - 9VDC 650mA](https://www.sparkfun.com/products/298) 

[ TOL-00298 ]

High quality switching \'wall wart\' AC to DC 9V 650mA wall power supply manufactured specifically for Spark Fun Electronics. T...

**Retired**

[![Power Supply - 24V (5A)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/2/0/13758-Power_supply_24V_5A-01.jpg)](https://www.sparkfun.com/products/13758)

### [Power Supply - 24V (5A)](https://www.sparkfun.com/products/13758) 

[ TOL-13758 ]

This 5A power supply outputs both 24VDC and is terminated with a center-positive 5.5 x 2.1mm barrel connector.

**Retired**

[![Global Power Supply - 15V 4.34A](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/1/4/14338-01.jpg)](https://www.sparkfun.com/global-power-supply-15v-4-34a.html)

### [Global Power Supply - 15V 4.34A](https://www.sparkfun.com/global-power-supply-15v-4-34a.html) 

[ PRT-14338 ]

This isn\'t your ordinary power supply. The Global Power Supply is a 15V, 4.34A power device specifically designed to work wit...

[\$34.95] [ [\$19.95] ]

[![SparkFun ATX Power Connector Breakout Kit - 12V/5V (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/5/0/15701-SparkFun_ATX_Power_Connector_Breakout_Kit_-_12V_5V__4-pin_-01.jpg)](https://www.sparkfun.com/products/15701)

### [SparkFun ATX Power Connector Breakout Kit - 12V/5V (4-pin)](https://www.sparkfun.com/products/15701) 

[ KIT-15701 ]

The ATX power connector breaks out the standard 4-pin computer peripheral port for you 12V & 5V devices from one wall adapter...

**Retired**

#### More Than One LED Per Channel

Multiple LEDs can be connected in series, as shown, and the supply voltage should be at least 2-3V higher than the sum of the forward voltages of the LEDs.

[![Arduino connection with four LEDs per channel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/4/3/picobuck_4led.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/3/picobuck_4led.png)

Multiple LEDs can be connected per channel; they should be connected in series, as shown above, and the power supply voltage must be at least 1-2V higher that the sum of the forward voltages of the LEDs.

For instance, our [blue 3W LEDs](https://www.sparkfun.com/products/13107) have a forward voltage of 3.2V to 3.8V. To be on the safe side, use the highest voltage in the range. If you want to connect four of them, you\'d need a power supply of \~17V or greater (3.8V + 3.8V + 3.8V + 3.8V = 15.2V; add 2V of \"head room\").

Since 17V is greater than the Arduino can tolerate on its input, we have to provide an external supply for the Arduino as well. This can be the standard 5V USB supply.

It\'s perfectly acceptable to mix colors either between channels or on one channel, so long as all of the LEDs can handle the current (330mA or 660mA, depending on the jumper setting). Just make sure that the power supply voltage is high enough to handle the sum voltages of the highest voltage string. There is also no requirement that the three strings of LEDs have the same forward voltage of LEDs across them; you could have one white LED on channel 1, two red LEDs on channel 2, and four green LEDs on channel 3.

#### Arduino Code Example

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

Code for controlling this device is trivial; simply use the `analogWrite()` function to adjust the brightness via PWM.

    language:c
    /**
     * PicoBuck Breakout Example
     * Mike Hord @ SparkFun Electronics
     * Nov 5 2015
     * 
     * A simple example showing how to control a PicoBuck with an Arduino.
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

    const int CHL_1 = 3;
    const int CHL_2 = 5;
    const int CHL_3 = 6;

    void setup()
    

    void loop()
    

**[] Tip:** Looking for more inspiration for mixing colors individually? Try using [Arduino.cc\'s Color Cross Fader example](https://www.arduino.cc/en/Tutorial/ColorCrossfader) to mix the colors like a rainbow if you are using the high power RGB LED.\
\

[![](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/1/0/TertiaryColorWheel_Chart.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/0/TertiaryColorWheel_Chart.png)

\
Try checking the example that was used in the [LilyPad ProtoSnap Plus Activity Guide for custom color mixing with tertiary colors](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-activity-guide/3-custom-color-mixing). Just make sure to update the pin definitions.\
\

[![LilyPad ProtoSnap Plus Activity Guide: Custom Color Mixing](https://cdn.sparkfun.com/r/480-270/assets/learn_tutorials/7/1/0/ProtoSnap_PingPongBall.jpg)](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-activity-guide/3-custom-color-mixing)\
\
*RGB LED Lighting Up from [Experiment 3: Custom Color Mixing](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-activity-guide/3-custom-color-mixing)*

\
Or try using the code from the [Non-Addressable RGB LED Strip Hookup Guide](https://learn.sparkfun.com/tutorials/non-addressable-rgb-led-strip-hookup-guide). While the code was written for RGB strips with transistors, the code functions the same with the the PickBuck.\
\

[](https://learn.sparkfun.com/tutorials/non-addressable-rgb-led-strip-hookup-guide)

### Non-Addressable RGB LED Strip Hookup Guide 

February 19, 2020

Add color to your projects with non-addressable LED strips! These are perfect if you want to control and power the entire strip with one color for your props, car, fish tank, room, wall, or perhaps under cabinet lighting in your home.

------------------------------------------------------------------------