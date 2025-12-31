# Source: https://learn.sparkfun.com/tutorials/qwiic-haptic-driver-da7280-hookup-guide

## Introduction

The [Qwiic Haptic Driver](https://www.sparkfun.com/products/17590) includes an itty-bitty, Linear Resonant Actuator (LRA) vibration motor and Dialog Semiconductor\'s DA7280 motor driver IC for applications that require haptic feedback. There is also a kit for those that would like the motor mounted separately from the board. Note that you will need to manually solder the wires and motor to the board.

[![SparkFun Qwiic Haptic Driver - DA7280](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/6/6/7/17590-SparkFun_Qwiic_Haptic_Driver_-_DA7280-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-haptic-driver-da7280.html)

### [SparkFun Qwiic Haptic Driver - DA7280](https://www.sparkfun.com/sparkfun-qwiic-haptic-driver-da7280.html) 

[ ROB-17590 ]

The Qwiic Haptic Motor Driver includes an itty-bitty, Linear Resonant Actuator (LRA) vibration motor and DialogSemi\'s DA7280 ...

[ [\$11.50] ]

[![SparkFun Qwiic Haptic Driver Kit - DA7280](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/5/7/6/18247-SparkFun_Qwiic_Haptic_Driver_Kit_-_DA7280-01a.jpg)](https://www.sparkfun.com/sparkfun-qwiic-haptic-driver-kit-da7280.html)

### [SparkFun Qwiic Haptic Driver Kit - DA7280](https://www.sparkfun.com/sparkfun-qwiic-haptic-driver-kit-da7280.html) 

[ ROB-18247 ]

The Qwiic Haptic Motor Driver Kit includes a small LRA vibration motor, wires, and the breakout board for Dialog Semi\'s DA728...

**Retired**

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![SparkFun Qwiic Haptic Driver - DA7280](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/6/6/7/17590-SparkFun_Qwiic_Haptic_Driver_-_DA7280-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-haptic-driver-da7280.html)

### [SparkFun Qwiic Haptic Driver - DA7280](https://www.sparkfun.com/sparkfun-qwiic-haptic-driver-da7280.html) 

[ ROB-17590 ]

The Qwiic Haptic Motor Driver includes an itty-bitty, Linear Resonant Actuator (LRA) vibration motor and DialogSemi\'s DA7280 ...

[ [\$11.50] ]

[![Reversible USB A to Reversible Micro-B Cable - 0.8m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/7/15428-Reversible_USB_A_to_Reversible_Micro-B_Cable_-_0.8m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-reversible-micro-b-cable-0-8m.html)

### [Reversible USB A to Reversible Micro-B Cable - 0.8m](https://www.sparkfun.com/reversible-usb-a-to-reversible-micro-b-cable-0-8m.html) 

[ CAB-15428 ]

These 0.8m cables have minor, yet genius modifications that allow both ends to be plugged into their ports regardless of thei...

[ [\$5.50] ]

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic) .

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/8/2/Qwiic-registered-black.png "Click to learn more about the Qwiic Connect System!")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you aren't familiar with the following concepts, we also recommend checking out a few of these tutorials before continuing. While the Haptic Motor Driver hookup guide linked below uses a different IC on the board, there is some [useful information about different motors available in the tutorial](https://learn.sparkfun.com/tutorials/haptic-motor-driver-hook-up-guide#erm-and-lra-motors).

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/haptic-motor-driver-hook-up-guide)

### Haptic Motor Driver Hook-Up Guide 

Good vibes only. Getting started with the Haptic Motor Driver.

## Hardware Overview

### Haptic Driver and LRA Motor

The haptic driver IC rotated at 45° with respect to the board while the circular disk is the LRA motor. If you received the kit version, the motor will need to be soldered to the board using the wires. Note that the Arduino library used in this tutorial configures the DA7280\'s settings based on the LRA motor\'s specifications.

[![DA7280 Haptic Driver and LRA Motor](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_IC_LRA_Motor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_IC_LRA_Motor.jpg)

### Power and Logic Levels

We recommend powering the board through the Qwiic connector when quickly prototyping. For a more secure connection, you can always [solder to the PTHs](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) labeled **3V3/VDD** and **GND**. The recommended input voltage when using the board with a microcontroller is **3.3V**. However, you could potentially power the board between *2.8V to 5.5V* as explained in the datasheet. Note that the **3V3/VDD** is connected to **VDDIO**. There is a jumper on the back of the board to disconnect the input voltage and the logic levels if you decide to use different voltages. If you decide to adjust the logic level, this is typically *1.8V*. However, you can set the logic levels between *1.35V and 5.5V* as long as **VDDIO** ≤ **VDD** and if `GPI0`, `GPI1`, and `GPI2` are not grounded as it is recommended in the datasheet.

[![Power Rails Highlighted on Qwiic Haptic Driver DA7280](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_Power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_Power.jpg)

### I^2^C

The main method of controlling the DA7280 and the vibe motor is through the I^2^C bus. The board includes two Qwiic connectors for fast prototyping and removes the need for soldering. All you need to do is plug a Qwiic cable into the Qwiic connector and voila! You can also [solder to the PTHs](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) labeled as **SDA** and **SCL** as an alternative. The address for the DA7280 is **0x4A**.

[![Qwiic Connectors and I2C Port Highlighted for the Qwiic Haptic Driver DA7280](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_I2C.jpg)

### Interrupt

The interrupt is active low and notifies the host microcontroller when the DA7280 has finished driving the motor. This connection is optional and available for those that decide to include an interrupt for their application.

[![Interrupt Pin Highlighted on Qwiic Haptic Driver DA7280](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_Interrupt.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_Interrupt.jpg)

### PWM Pin

The second method of controlling the DA7280 is to send a PWM signal to the `GPI0` pin. Once the DA7280 is configured to PWM mode via I^2^C, the duty cycle of the PWM signal will be reflected on the DA7280\'s output drive to the vibration motor. The DA7280 requires that the PWM signal is at least 10kHz. The top of the board only labels the PTH as `GPI0` due to the space available around the pin while the back of the board labels the pin as `GPI0/PWM`.

[![GPI0/PWM Pin Highlighted on Qwiic Haptic Driver DA7280](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_PWM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_PWM.jpg)

### GPI Pins

**Note:** Before you can operate the board in stand-alone embedded operation, you must configure the DA7280 with a host microcontroller. Once configured, the DA7280 can operate without the need of a host microcontroller.

The third method of controlling DA7280 and the motor is through the general purpose input (GPI) pins. These can be configured to edge trigger based on the the combination of the pins and waveforms that are stored in the DA7280\'s memory.

[![GPI Pins Highlighted on Qwiic Haptic Driver DA7280](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_General_Purpose_Inputs_GPI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_General_Purpose_Inputs_GPI.jpg)

### LED

The board includes an LED indicator that lights up when there is power available.

[![LED Highlighted on Qwiic Haptic Driver DA7280](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_PWR_LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_PWR_LED.jpg)

### Jumpers

There are four jumpers on the back of the board. For more information, check out our [tutorial on working with jumper pads and PCB traces](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all) should you decide to cut the traces with a hobby knife.

- **LED** - This is connected to the PWR LED on the top of the board. Cutting this disables the LED.
- **I2C** - The I2C jumper is connected to the 4.7kΩ pull-up resistors for the I^2^C bus. Most of the time you can leave these alone unless your project requires you to [disconnect the pull-up resistors](https://learn.sparkfun.com/tutorials/i2c/all#i2c-at-the-hardware-level).
- **QISO** - The QISO jumper is connected to the Qwiic bus power line (i.e. 3.3V). Cut this trace to separate power from the Qwiic ports if you decide to power the board with a different voltage on **3V3/VDD**. Note that the I^2^C lines are still pulled up to 3.3V.
- **IO** - The IO jumper connects **3.3V/VDD** to **VDDIO** for the DA7280. Cut this trace and supply **VDDIO** with a different voltage to adjust the DA7280\'s logic levels. This is typically *1.8V*. However, you can set the logic levels between *1.35V and 5.5V* as long as **VDDIO** ≤ **VDD** and if **GPI0**, **GPI1**, and **GPI2** are not grounded as it is recommended in the datasheet

[![LED, I2C Pullup Resistor, QISO, IO, Jumpers Highlighted on Qwiic Haptic Driver DA7280](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/17590-SparkFun_Qwiic_Haptic_Driver_DA7280_Jumpers.jpg)

### Board Dimensions

The board dimension is 1.00\" x 1.15\" and includes 3x mounting holes. The mounting holes are spaced using the Qwiic standard for 1.0\"x1.0\" sized boards. Note that the board is longer on one side to accommodate the SMD vibe motor.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/3/3/6/1/a/Qwiic_Haptic_Motor_Driver_DA7280_Board_Dimensions.png)](https://cdn.sparkfun.com/assets/3/3/6/1/a/Qwiic_Haptic_Motor_Driver_DA7280_Board_Dimensions.png)

## Hardware Assembly

There are three modes (I^2^C, PWM, and stande-alone with the GPI) available for the DA7280. For the scope of this tutorial and Arduino Library, we will be using the I^2^C and PWM modes. If you are using the PTHs, we recommend [soldering header pins](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) or wires to the board for a secure connection.

### I^2^C Mode

The main method to control the DA7280 is through an I^2^C bus. You\'ll need the RedBoard Qwiic and a USB cable to program the microcontroller. Insert the USB cable into the RedBoard. Then insert a Qwiic cable between the RedBoard Qwiic and Qwiic Haptic Driver. Depending on your application, you can also solder to the plated through holes for a secure connection.

[![RedBoard Qwiic Connected to Qwiic Haptic Driver for I2C Mode](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/1/Qwiic_Haptic_Driver_DA7280_Vibration_Motor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/Qwiic_Haptic_Driver_DA7280_Vibration_Motor.jpg)

### PWM Mode

The second method of controlling the DA7280 is via PWM. The Haptic Driver IC requires that the PWM signal frequency given to `GPI0/PWM` pin is at least 10kHz. The default PWM methods of `analogWrite()` does not provide a method of controlling the frequency of the PWM signal. To use with the RedBoard with ATmega328P, you will need to use the TimerOne Arduino Library by Paul Stoffregen as explained later in this tutorial. Note that this library is limited to certain boards. For the Arduino Uno (e.g. the RedBoard with ATmega328P) the pins that are reserved for PWM are on pins **9** and **10**.

In this case, we will connect the Qwiic Haptic\'s **GPIO0/PWM** pin to the RedBoard\'s pin **9**. We also still need to control the DA7280. Make sure to include a Qwiic cable between the boards as well.

[![PWM Mode](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/1/Qwiic_Haptic_Driver_DA7280_Vibration_Motor_PWM_Input.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/Qwiic_Haptic_Driver_DA7280_Vibration_Motor_PWM_Input.jpg)

Before powering up, you will also need to ensure that you cut the trace for the RedBoard Qwiic\'s I/O and add a solder jumper to the 3.3V pin.

[![Cut Jumper and Add Solder Jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/1/Adjust_RedBoard_Logic_Levels_3V3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/Adjust_RedBoard_Logic_Levels_3V3.jpg)

### Soldering Wires

For those that want to attach the LRA motor separately from the board, you will need to solder wires between the Qwiic Haptic Driver board\'s castellated pins. For a flush connection, we recommend cutting the male header pins and [stripping the wire](https://learn.sparkfun.com/tutorials/working-with-wire/how-to-strip-a-wire). Solder the black wire to the castellated pin (which is connected to DA7280\'s OUTN pin) that is the closest to the PWR LED. Then solder the red wire to the other castellated pin (which is connected to the DA7280\'s OUTP pin).

[![Solder Wires to Qwiic Haptic Driver Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/1/Qwiic_Haptic_Driver_DA7280_Solder_Wire_Vibration_Motor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/Qwiic_Haptic_Driver_DA7280_Solder_Wire_Vibration_Motor.jpg)

Cut and strip the wire on the other ends. With the LRA motor\'s SMD pads facing you (as shown in the image below), solder the black wire on the left pad. Then solder the red wire on the right pad.

[![Solder Wires to LRA Vibration Motor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/1/Qwiic_Haptic_Driver_DA7280_Solder_Wire_LRA_Vibration_Motor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/Qwiic_Haptic_Driver_DA7280_Solder_Wire_LRA_Vibration_Motor.jpg)

If you decide to leave the header pins on the wires, your setup will look similar the image on the left. With the header pins removed, your setup will look similar to the image on the right. For a secure connection, you may want to add some hot glue to the terminals for strain relief. Once soldered, simply attach a Qwiic cable between the Qwiic connectors or solder wire to your connections as explained above. Remember, you will need to adjust the RedBoard Qwiic\'s logic level to 3.3V if you decide to use the PWM mode.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![M/M jumper wires soldered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/1/Qwiic_Haptic_Driver_DA7280_Jumper_Wire_Pins_Vibration_Motor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/Qwiic_Haptic_Driver_DA7280_Jumper_Wire_Pins_Vibration_Motor.jpg)   [![M/M jumper pins cut and wire soldered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/1/Qwiic_Haptic_Driver_DA7280_Jumper_Wire_Vibration_Motor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/1/Qwiic_Haptic_Driver_DA7280_Jumper_Wire_Vibration_Motor.jpg)
  *M/M jumper wires soldered*                                                                                                                                                                                                                                                                  *M/M jumper pins cut and wire soldered*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Arduino Library

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

The SparkFun DA7280 Haptic Driver Arduino library can be downloaded with the Arduino library manager by searching \'**SparkFun Qwiic Haptic Driver DA7280**\' or you can manually install the library by downloading the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_Qwiic_Haptic_Driver_DA7280_Arduino_Library):

[SparkFun DA7280 Haptic Driver Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_Haptic_Driver_DA7280_Arduino_Library/archive/main.zip)

## Example 1: I2C Mode

We\'re just going to look the **I2C_Mode.ino** example. Open the **File** \> **Examples** \> **SparkFun Qwiic Haptic Driver DA7280 Arduino Library** \> **I2C_Mode**. Select your board (in this case **Arduino Uno**) and COM port. Then hit the upload button.

Once uploaded, the Qwiic Haptic Driver should begin vibrating every half a second. Note that the value for `hapDrive.setVibrate()` range from `0` to `127`. A value of `0` turns the motor off while a value of `127` turns the motor fully on. Try adjusting the value to a higher intensity. If the motor does not vibrate, try uncommenting the code to clear the interrupt.

**Note:** Make sure to disable the frequency tracking with `hapDrive.enableFreqTrack(false);`. Restricting the PCB (e.g. squeezing) raises an error which stops operation because it can not reach resonance.

## Example 2: PWM Mode

**Note:** The Haptic Driver IC requires that the PWM signal frequency given to `GPI0/PWM pin` is at least 10kHz. The default PWM methods of `analogWrite()` does not provide a method of controlling the frequency of the PWM signal. To use with the RedBoard with ATmega328P, you will need to use the [TimerOne Arduino Library by Paul Stoffregen](https://www.pjrc.com/teensy/td_libs_TimerOne.html). Note that this library is limited to certain boards. For the Arduino Uno (e.g. the RedBoard with ATmega328P) the PWM pins that are reserved are on pins **9** and **10**.\
\
Since the library version is not included in the Arduino Library Manager, you will need to [manually install](https://www.arduino.cc/en/Guide/Libraries#importing-a-zip-library) the [TimerOne library by Paul Stoffregen](https://github.com/PaulStoffregen/TimerOne) by downloading it from the GitHub repository. In the Arduino IDE\'s menu, navigate to **Sketch** \> **Include Library** \> **Add .ZIP Library\...**. A window will open up requesting for the ZIP file to be included. Head to the Downloads folder where the **TimerOne-master.zip** is saved.\
\

[GitHub \| TimerOne Arduino Library (ZIP)](https://github.com/PaulStoffregen/TimerOne/archive/refs/heads/master.zip)

We\'re just going to look the **PWM_Mode_Timer1.ino** example. Open the **File** \> **Examples** \> **SparkFun Qwiic Haptic Driver DA7280 Arduino Library** \> **PWM_Mode_Timer1.ino**. Select your board (in this case **Arduino Uno**) and COM port. Then hit the upload button.

Once uploaded, the Qwiic Haptic Driver will first clear a flag that shuts the motor off if the PWM signal is cut off suddenly without being set into inactive mode. The motor will begin vibrating based on the PWM signal in the `for` loop. In this case, the PWM signal is dependent on the value for `power` and we slowly increase the intensity.

**Note:** Unlike the RedBoard with ATmega328P that requires the Timer1 library, you can also choose a microcontroller that has the ability to control the frequency of the PWM signal like the Teensy or Artemis. These have more power. For more information, check out the **File** \> **Examples** \> **SparkFun Haptic Driver Arduino Library** \> **PWM_Mode_Teensy_Artemis.ino**.\
\
You will need to [install the Teensyduino](https://learn.sparkfun.com/tutorials/getting-started-with-the-teensy/programming) for Teensy or the [Ambiq Apollo3 board definitions (v2.0.6+)](https://learn.sparkfun.com/tutorials/artemis-development-with-arduino#arduino-installation) for the Artemis if you decide to use the example. Once installed, make sure to select your board and COM port before uploading the example.