# Source: https://learn.sparkfun.com/tutorials/fading-with-the-mosfet-power-switch-and-buck-regulator

## Introduction

This tutorial will guide you through using the SparkFun MOSFET Power Switch and Buck Regulator (Low-Side) with your Arduino projects. This handy board combines a MOSFET switch for controlling high-power loads (up to 12V) with a built-in buck regulator that conveniently provides stable 3.3V power for your Arduino.

We\'ll explore various functionalities, starting with basic on/off control and progressing to creating dimming effects for LEDs and controlling motors with variable speeds. By the end, you\'ll be able to safely manage powerful components and add exciting features to your Arduino projects!

[![SparkFun MOSFET Power Switch and Buck Regulator (Low-Side)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/4/3/0/3/COM-23979-MOSFET-Power-Switch-Feature.jpg)](https://www.sparkfun.com/sparkfun-mosfet-power-switch-and-buck-regulator-low-side.html)

### [SparkFun MOSFET Power Switch and Buck Regulator (Low-Side)](https://www.sparkfun.com/sparkfun-mosfet-power-switch-and-buck-regulator-low-side.html) 

[ COM-23979 ]

The MOSFET Power Switch and Buck Regulator (Low-Side) can be powered with up to 12V and control up to 10A, all while providin...

[ [\$16.50] ]

If you are looking for the full Hookup Guide for the SparkFun MOSFET Power Switch and Buck Regulator (Low-Side), click the button bellow. This guide only covers a simple project to get you started quickly, while the full Hookup Guide goes over every detail of the sensor.

[View the Full Hookup Guide](https://docs.sparkfun.com/SparkFun_MOSFET_Power_Switch_and_Buck_Regulator_Low-Side/)

 

**Tip:** The 3.3V output from the MOSFET Power Switch and Buck Regulator (Low-Side) provides another alternative to power microcontrollers that may not be able to accept higher voltages. For example, most of the Thing Plus Development Boards only accept a maximum of 6V at their VIN pin, and they most operate at 3.3V. So this board is especially handy in those use-cases. Additionally, even though the Arduino Pro Mini can accept up to 12V, this will require its onboard linear regulator to work very had to regulate that voltage down to 3.3V. Thus, this MOSFET Power Switch and Buck Regulator (Low-Side) would be the \"cooler\" choice.

**Note:** The tutorial focuses on using a microcontroller with Arduino. However, if your microcontroller has a digital or PWM, you can also control the N-channel MOSFET controller as well! You can also use this using a micro:bit with MakeCode or Raspberry Pi\'s RP2040 microcontroller with MicroPython!

------------------------------------------------------------------------

## Hardware Needed

To follow this experiment, you will need the following materials. While this is a simple project we wanted to make sure that you have everything you need to get started before we get to the code. For this simple project we chose the [ESP32 IoT RedBoard Development Board](https://www.sparkfun.com/products/19177).

[![SparkFun MOSFET Power Switch and Buck Regulator (Low-Side)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/4/3/0/3/COM-23979-MOSFET-Power-Switch-Feature.jpg)](https://www.sparkfun.com/sparkfun-mosfet-power-switch-and-buck-regulator-low-side.html)

### [SparkFun MOSFET Power Switch and Buck Regulator (Low-Side)](https://www.sparkfun.com/sparkfun-mosfet-power-switch-and-buck-regulator-low-side.html) 

[ COM-23979 ]

The MOSFET Power Switch and Buck Regulator (Low-Side) can be powered with up to 12V and control up to 10A, all while providin...

[ [\$16.50] ]

[![SparkFun IoT RedBoard - ESP32 Development Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/8/0/0/ESP32_03.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html)

### [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html) 

[ WRL-19177 ]

The IoT RedBoard is an ESP32 WROOM-equipped development board that has everything you need in an Arduino Uno with extra perks...

[ [\$41.87] ]

[![LED RGB Strip - Bare (1m)](https://cdn.sparkfun.com/r/600-600/assets/parts/8/5/4/9/12021-01.jpg)](https://www.sparkfun.com/led-rgb-strip-bare-1m.html)

### [LED RGB Strip - Bare (1m)](https://www.sparkfun.com/led-rgb-strip-bare-1m.html) 

[ COM-12021 ]

These are bare non-addressable 1 meter long RGB LED strips that come packed with 60 5060 LEDs per meter. As these are bare LE...

[ [\$15.95] ]

[![Wall Adapter Power Supply - 12VDC, 600mA (Barrel Jack)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/8/1/6/TOL-15313-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-12vdc-600ma-barrel-jack.html)

### [Wall Adapter Power Supply - 12VDC, 600mA (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-12vdc-600ma-barrel-jack.html) 

[ TOL-15313 ]

This is a high quality AC to DC \'wall wart\' which produces a regulated output of 12VDC at up to 600mA.

[ [\$9.25] ]

[![DC Barrel Jack Adapter - Male](https://cdn.sparkfun.com/r/600-600/assets/parts/4/6/8/3/10287-01.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-male.html)

### [DC Barrel Jack Adapter - Male](https://www.sparkfun.com/dc-barrel-jack-adapter-male.html) 

[ PRT-10287 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.60] ]

[![DC Barrel Jack Adapter - Female](https://cdn.sparkfun.com/r/600-600/assets/parts/4/6/8/4/10288-02.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html)

### [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html) 

[ PRT-10288 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.75] ]

[![Mini Photocell](https://cdn.sparkfun.com/r/600-600/assets/parts/2/4/6/2/09088-02-L.jpg)](https://www.sparkfun.com/mini-photocell.html)

### [Mini Photocell](https://www.sparkfun.com/mini-photocell.html) 

[ SEN-09088 ]

This is a very small light sensor. A photocell changes (also called a \[photodetector\](http://en.wikipedia.org/wiki/Photodetec...

[ [\$1.75] ]

[![Trimpot 10K Ohm with Knob](https://cdn.sparkfun.com/r/600-600/assets/parts/3/8/2/3/09806-01.jpg)](https://www.sparkfun.com/trimpot-10k-ohm-with-knob.html)

### [Trimpot 10K Ohm with Knob](https://www.sparkfun.com/trimpot-10k-ohm-with-knob.html) 

[ COM-09806 ]

This 10K trimmable potentiometer has a small knob built right in and it\'s breadboard friendly to boot!

[ [\$1.25] ]

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/600-600/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![Reversible USB A to C Cable - 0.8m](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/9/8/4/15425-Reversible_USB_A_to_C_Cable_-_0.8m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html)

### [Reversible USB A to C Cable - 0.8m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html) 

[ CAB-15425 ]

These 0.8m cables have minor modifications that allow them to be plugged into their ports regardless of orientation on the US...

[ [\$6.50] ]

[![Jumper Wires Premium 6\" M/M Pack of 10](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/1/JumperWire-Male-01-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html)

### [Jumper Wires Premium 6\" M/M Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html) 

[ PRT-08431 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumpers with male connectors on both ends. Use these to jumper fro...

[ [\$5.25] ]

[![Resistor 10K Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/2/1/6/14491-03.jpg)](https://www.sparkfun.com/resistor-10k-ohm-1-4-watt-pth-20-pack-thick-leads.html)

### [Resistor 10K Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://www.sparkfun.com/resistor-10k-ohm-1-4-watt-pth-20-pack-thick-leads.html) 

[ PRT-14491 ]

These are your run-of-the-mill 1/4 Watt, +/- 5% tolerance PTH resistors. Commonly used in breadboards and other prototyping a...

[ [\$1.50] ]

------------------------------------------------------------------------

## Software Setup

**Note:** If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

SparkFun has written a library to work with the SparkFun MOSFET Power Switch and Buck Regulator. You can obtain this library by clicking on the button below, or by downloading it from the [GitHub Repository](https://github.com/sparkfun/SparkFun_Qwiic_Ultrasonic_Arduino_Library/tree/v10).

[SparkFun MOSFET Power Switch and Buck Regulator Library GitHub](https://github.com/sparkfun/SparkFun_MOSFET_Power_Switch_and_Buck_Regulator_Low-Side/tree/main/Firmware/Arduino)

 

------------------------------------------------------------------------

## Fading

In this example, we will slowly turn on the load and then slowly turn it off using the N-channel MOSFET. This example is better with a DC motor and 12V LED. You will typically want the solenoid to be fully turned on/off.

For this example you will need the [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/products/19177), a [USB-C Cable](https://www.sparkfun.com/products/15092), the [SparkFun MOSFET Power Switch and Buck Regulator (Low-Side)](https://www.sparkfun.com/products/23979), a [Mini Screwdriver](https://www.sparkfun.com/products/9146), [M/M Jumper Wires](https://www.sparkfun.com/products/8431), an [RGB LED Strip](https://www.sparkfun.com/products/12021), and a \[12V Wall Adapter Power Supply\](12V Wall Adapter Power Supply).

### Hardware Hookup

You will need to connect everything as explained earlier. For this particular example, we will use one channel from a 12V RGB LED strip as shown in the circuit diagram below.

[![Fritzing Diagram for Hardware Hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/4/2/SparkFun_Power_Control_Switch_N-Channel_MOSFET_Buck_Regulator_RedBoard_Arduino_IoT_ESP32_Fade_Red_12V_LED_Strip_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/4/2/SparkFun_Power_Control_Switch_N-Channel_MOSFET_Buck_Regulator_RedBoard_Arduino_IoT_ESP32_Fade_Red_12V_LED_Strip_bb.jpg)

**Note:** Notice that we are using pin 16 to fade the red channel instead of pin 25 on the IoT RedBoard - ESP32.

 

Your setup should look similar to the image below without the power supply.

[![Your setup should look similar to this.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/4/2/23979-MOSFET_Power_Switch_ESP32_LED_Strip_Red_Fading.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/4/2/23979-MOSFET_Power_Switch_ESP32_LED_Strip_Red_Fading.jpg)

### Upload Code

To upload code, insert the USB cable into the IoT RedBoard - ESP32.

**Note:** This example is similar to the built-in Arduino example. From the menu, select the following: **File \> Examples \> 03.Analog \> Fading**. You will need to modify the defined pin with a PWM pin for your microcontroller. Note that the logic is reversed due to the transistor.

Copy the following code and paste it in the Arduino IDE. If you have not already, select your Board (in this case, the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

    /******************************************************************************
      Example: Fading
      Modified By: Ho Yun "Bobby" Chan
      SparkFun Electronics
      Date: October 27th, 2023
      License: MIT. See license file for more information but you can
      basically do whatever you want with this code.

      This example is based on Arduino's fade example. It has been modified
      so that it can be used for the SparkFun IoT RedBoard- ESP32 but it can be
      used with any Arduino that has a PWM pin. The load (DC motor,
      or 12V LED) will slowly turn on and off. This code will be more useful for
      users connecting a DC motor or nonaddressable LED so that you can partially
      turn on/off the load.

      Users can also open the Serial Monitor at 115200 to check on
      the status of the button for debugging.

      Feel like supporting open source hardware?
      Buy a board or component from SparkFun!

          SparkFun MOSFET Power Switch and Buck Regulator (Low-Side): https://www.sparkfun.com/products/23979
          SparkFun IoT RedBoard - ESP32 Development Board: https://www.sparkfun.com/products/19177
          Hobby Motor - Gear: https://www.sparkfun.com/products/11696
          Blower - Squirrel Cage (12V): https://www.sparkfun.com/products/11270
          12V LED RGB Strip - Bare (1m): https://www.sparkfun.com/products/12021
          Wall Adapter 12V/600mA, (Barrel Jack): https://www.sparkfun.com/products/15313

      Distributed as-is; no warranty is given.
    ******************************************************************************/

    int loadPin = 16;

    // the setup function runs once when you press reset or power the board
    void setup()   //END SETUP

    // the loop function runs over and over again forever
    void loop() 

    Serial.println("<===== FADE OUT =====>");
    // fade out from max to min in increments of 5 points:
    for (int fadeValue = 0; fadeValue <= 255; fadeValue += 5) 

    }  //END LOOP

### What You Should See

Once the code has uploaded, disconnect the USB cable from the IoT RedBoard - ESP32. Then insert the barrel jack from a power supply to the MOSFET Power Switch and Buck Regulator\'s barrel jack connector. In this case, we used a 12V wall adapter power supply.

The load will slowly turn on and slowly turn off. This will loop forever until power is removed from the board. If necessary, disconnect the 3.3V jumper wire from the IoT RedBoard - ESP32, reconnect the USB cable, and open the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at 115200 baud for debugging purposes.

[![LED Fading with your MOSFET](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/4/2/23979-MOSFET_Power_Switch_ESP32_LED_Strip_Red_Fading.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/4/2/23979-MOSFET_Power_Switch_ESP32_LED_Strip_Red_Fading.gif)

While this example was used to turn on one channel of a 12V RGB LED strip, you could also use this example with a DC motor. Try using a potentiometer (or any 3.3V analog sensor) with the [map() function](https://www.arduino.cc/reference/en/language/functions/math/map/) to adjust the speed of the motor.

 

------------------------------------------------------------------------

## 12V RGB LED Strip 

In this example, we will control all three channels of the RGB LED strip. Since we\'ve already [hooked up a 12V RGB LED strip before](https://learn.sparkfun.com/tutorials/non-addressable-rgb-led-strip-hookup-guide), we will also a circuit with a potentiometer to cycle between each color and a photoresistor to turn on the LEDs whenever the light is below a certain light level. The following example code is based on the [SparkFun Inventor\'s Kit v4.1 Night Light example](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v41/circuit-1d-rgb-night-light).

[](https://learn.sparkfun.com/tutorials/non-addressable-rgb-led-strip-hookup-guide)

### Non-Addressable RGB LED Strip Hookup Guide 

Add color to your projects with non-addressable LED strips! These are perfect if you want to control and power the entire strip with one color for your props, car, fish tank, room, wall, or perhaps under cabinet lighting in your home.

[](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v41)

### SparkFun Inventor\'s Kit Experiment Guide - v4.1 

The SparkFun Inventor\'s Kit (SIK) Experiment Guide contains all of the information needed to build all five projects, encompassing 16 circuits, in the latest version of the kit, v4.1.2 and v4.1.

 

### Parts Needed

Grab the following quantities of each part listed to build this circuit:

- 1x [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/products/19177)
- 1x [USB-C Cable](https://www.sparkfun.com/products/15092)
- 3x [SparkFun MOSFET Power Switch and Buck Regulator (Low-Side)](https://www.sparkfun.com/products/23979)
- 1x [SparkFun Mini Screwdriver](https://www.sparkfun.com/products/9146)
- 19x [M/M Jumper Wires](https://www.sparkfun.com/products/11026)\*
- 1x [Breadboard](https://www.sparkfun.com/products/12002)
- 1x [10kΩ Potentiometer with Knob](https://www.sparkfun.com/products/9806)
- 1x [Mini Photocell](https://www.sparkfun.com/products/9088)
- 1x [10kΩ Resistor](https://www.sparkfun.com/products/14491)
- 1x [12V RGB LED Strip](https://www.sparkfun.com/products/12021)
- 1x [DC Barrel Jack Adapter - Male](https://www.sparkfun.com/products/10287)
- 3x [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/products/10288)
- 1x [12V Wall Adapter](https://www.sparkfun.com/products/15313)

\***Note:** You will need a minimum of 19x M/M jumper wires. Six jumper wires were stripped wires that connect the barrel jacks together for power and reference ground.

 

### Hardware Hookup

For this particular example, we will use three channels from a 12V RGB LED strip while also including a similar circuit from the SparkFun Inventor\'s Kit v4.1. The circuit diagram is shown below.

[![Three MOSFET Board Fritzing Hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/4/2/SparkFun_Power_Control_Switch_N-Channel_MOSFET_Buck_Regulator_RedBoard_Arduino_IoT_ESP32_Nightlight_RGB_12V_LED_Strip_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/4/2/SparkFun_Power_Control_Switch_N-Channel_MOSFET_Buck_Regulator_RedBoard_Arduino_IoT_ESP32_Nightlight_RGB_12V_LED_Strip_bb.jpg)

**Note:** When testing the non-addressable LED strip, the pin labeled \"G\" was actually blue and the \"B\" was actually green. Depending on the manufacturer, the label may vary. Try testing the LED strip out with a power supply to determine if the letter represents the color.

Keep in mind that instead of the RedBoard with ATmega328P, we are using the IoT RedBoard with ESP32. Since the hardware is different, the following code was modified:

    - analog and PWM pins were redefined in the example code
    - threshold was modified due to the ADC's higher resolution
    - logic is reversed due to the transistors

**Danger:** The IoT RedBoard with ESP32 has a system voltage of 3.3V. Thus, the logic levels is 3.3V instead of 5V on the RedBoard with ATmega328P. Thus, the analog reference voltage for the potentiometer and photoresistor is 3.3V. Make sure you are using 3.3V!

Your setup should look similar to the image below without the power supply.

[![Your three-board setup should look similar to this.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/4/2/23979-ESP32_Three_MOSFET_Power_Switch_LEDs_RGB_NightLight_Photoresistor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/4/2/23979-ESP32_Three_MOSFET_Power_Switch_LEDs_RGB_NightLight_Photoresistor.jpg)

 

### Upload Code

To upload code, insert the USB cable into the IoT RedBoard - ESP32.

Copy the following code and paste it in the Arduino IDE. If you have not already, select your Board (in this case, the **SparkFun ESP32 IoT RedBoard**), and associated COM port. Then hit the upload button.

    /*
    12V RGB LED Nightlight Example

    Turns an 12V RGB strip LED on or off based on the light level read by a photoresistor.
    Change colors by turning the potentiometer. This example is based off the SparkFun
    Inventor's Kit v4.2 RGB Night-Light Example:

      https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v41

    Note that instead of the RedBoard with ATmega328P, we are using the IoT RedBoard with ESP32.
    Since the hardware is different, the following code was modified:

      - analog and PWM pins were redifined
      - threshold was modified due to the ADC's higher resolution
      - logic is reversed due to the transistors

    WARNING: Since the IoT RedBoard with ESP32 has a system voltage of 3.3V, the logic levels
    is 3.3V instead of 5V on the RedBoard with ATmega328P. Thus, the analog reference voltage
    for the potentiometer and photoresistor is 3.3V. Make sure you are using 3.3V!

    This sketch was written by SparkFun Electronics, with lots of help from the Arduino community.
    This code is completely free for any use.

    */

    int photoresistor = A4;          //variable for storing the photoresistor value
    int potentiometer = A5;          //this variable will hold a value based on the position of the knob
    int threshold = 3000;            //if the photoresistor reading is lower than this value the light will turn on
                                 /*Note: The ESP32's ADC resolution is bigger. The max is 4095. In a bright room
                                 with your finger covering the sensor, the threshold was about 3000. In a dimly
                                 lit room, the threshold was about 1000. You will need to adjust this value when
                                 installing it in a room. Just make sure to make it a little more than the thresholed
                                 of the room. Try adding a button and some code  to save the threshold value! */

    //LEDs are connected to these pins
    int RedPin = 16;
    int GreenPin = 17;
    int BluePin = 25;

    void setup()  //END SETUP

    void loop() 
    else 

    delay(100);                             //short delay so that the printout is easier to read

    } //END LOOP

    void red () 
    void orange () 
    void yellow () 
    void green () 
    void cyan () 
    void blue () 
    void magenta () 
    void turnOff ()   

### What You Should See

Once the code has uploaded, disconnect the USB cable from the IoT RedBoard - ESP32. Then insert the barrel jack from a power supply to the MOSFET Power Switch and Buck Regulator\'s barrel jack connector. In this case, we used a 12V wall adapter power supply.

The MOSFET Power Switch & Buck Regulator with the wall adapter. Cover the photoresistor with your finger (or just turn off the lights in the room) and turn the potentiometer. You should notice the colors cycling through as the potentiometer is within certain ranges. You will probably want to disconnect the 3.3V jumper wire from the IoT RedBoard - ESP32, reconnect the USB cable, and open the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at **115200** baud for debugging purposes. That way you can view the serial data and adjust the threshold value based on the lighting in the room.

[![Three MOSFETs in Action](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/4/2/23979-ESP32_Three_MOSFET_Power_Switch_LEDs_RGB_NightLight_Photoresistor.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/4/2/23979-ESP32_Three_MOSFET_Power_Switch_LEDs_RGB_NightLight_Photoresistor.gif)

Now that we have ported the example from the RedBoard Qwiic with an ATmega328P to the RedBoard IoT Development Board - ESP32, try adjusting the condition statement with the potentiometer to add additional colors. Or even writing some code save the threshold value whenever a button is pressed down. You can also try to take advantage of the ESP32\'s wireless capabilities and adjust the color of the LED strip based on the weather.