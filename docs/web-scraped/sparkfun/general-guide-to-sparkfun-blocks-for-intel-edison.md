# Source: https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison

## What is a \"Block\"?

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Edison_Block_Stack_ISO.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/2/Edison_Block_Stack_ISO.jpg)

[SparkFun Blocks for the Intel® Edison](https://www.sparkfun.com/search/results?term=edison+blocks) are a great way to unlock all the features provided by the miniature 70-pin expansion connector. By mixing and matching Blocks, users can custom-tailor their Edison for any application. To get started, let\'s look at the anatomy of a stack of Blocks.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Edison_Stack_Side_Annotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/2/Edison_Stack_Side_Annotated.png)

*A sample stack of Blocks*

- [Intel® Edison](https://www.sparkfun.com/products/13024) - The \"brain\" of the stack, provides processing and communication.
- 70-pin connector - The backbone of the stack, provides a path of power and data to all Blocks.
- Standoffs - Provides mechanical strength to stacking Blocks.
- Blocks - Boards that breakout functionality of the 70-pin expansion connector.

Blocks allow applications to remain small, utilizing the miniature size of the Edison. Doing so required the continued use of the 70-pin connectors.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Connectors_annotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/2/Connectors_annotated.png)

*Hirose DF40 Socket and Plug*

The manufacturer (Hirose) named the connectors Headers and Receptacles. We have named both respective connectors Plugs and Sockets to better describe how the interface with each other.

- Socket (Receptacle) - This connector is found on the application board. This allows signals to be received by the Edison or a stacked Block.
- Plug (Header) - This connector is found on the Edison. This allows signals to pass to the next Block in a stack when used on Blocks.

Most Blocks will have two connectors that allow the signals to be used, then passed along to the next Block in the stack. This is very similar to how [Arduino Shields](https://learn.sparkfun.com/tutorials/arduino-shields) work. Let\'s now look at the different types of Blocks and learn how to create your own stack.

## Which Blocks do I Need?

All Blocks are not created equally. There are Blocks for power, communication, and for interacting with the environment. SparkFun engineer, Shawn, gives a great overview of the Edison and Blocks in the following video. After the video we will try to categorize the blocks to give a general idea on the uses for each Block. Some blocks are capable of multiple functions and will show up in multiple categories.

ReplaceMeOpen

ReplaceMeClose

------------------------------------------------------------------------

## Power Blocks

The first concern when building a stack of Blocks is power. There are a number of blocks available to power an Intel® Edison. These blocks have the ability to supply the required power to the Edison VSYS input located on the 70-pin expansion connector. All power Blocks built by SparkFun are designed to provide 4.0-4.1V to the VSYS bus.

------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [SparkFun Block for Intel® Edison - Base](https://www.sparkfun.com/products/13045)\                                                                                                                                                                                                                                                                                                     ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_Base.jpg)
  The Base Block can power an Edison Stack through either micro USB connector. The preferred method is to power through the port labled \"Console\". This leaves the OTG port available for USB devices such as web cameras, mass storage devices, or other USB-enabled devices. The power button is capable of putting the Edison in hibernation and powering off the module entirely.   

  ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_Console_1.jpg)                                                                                                                                                                                                                                                                                                [SparkFun Block for Intel® Edison - Console](https://www.sparkfun.com/products/13039)\
                                                                                                                                                                                                                                                                                                                                                                                          The Console Block can power an Edison Stack through the micro USB connector. The power button is capable of putting the Edison in hibernation and powering off the module entirely.

  [SparkFun Block for Intel® Edison - UART](https://www.sparkfun.com/products/13040)\                                                                                                                                                                                                                                                                                                     ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_UART.jpg)
  The UART Block paired with a 5V Compatible FTDI device, such as our [FTDI Basic Breakout](https://www.sparkfun.com/products/9716), will power an Edison Stack. The UART will power Stacks that do not consume over 500mA. This is a limitation of the typical FTDI devices on the market.                                                                                               

  ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_Battery_1.jpg)                                                                                                                                                                                                                                                                                                [SparkFun Block for Intel® Edison - Battery](https://www.sparkfun.com/products/13037)\
                                                                                                                                                                                                                                                                                                                                                                                          The Battery Block is likely the simplest way to power an Edison Stack. With a flip of the switch, a 400mAh Lithium Polymer battery can power an Edison for over an hour. Battery life will vary with CPU and WiFi usage. The micro USB connector on the Battery Block provides a way to charge the battery. The micro USB connector is only used for charging.

  [SparkFun Block for Intel® Edison - GPIO](https://www.sparkfun.com/products/13038)\                                                                                                                                                                                                                                                                                                     ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_GPIO.jpg)
  The GPIO Block gives access to the VSYS and GND lines pins in an Edison Stack. While it is possible to power an Edison Stack through the GPIO Block, there are risks. You must pay careful attention to only supply 3.3-4.5V. Exceeding these ranges will damage the Stack and the Edison.                                                                                              
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## Console Communication Blocks

Now that we have power to our Edison Stack, we need to log into our Edison. The Edison uses a [serial terminal](/tutorials/terminal-basics) interface to allow users to access the Edison console. This console is located on **UART2**. All SparkFun Communication Blocks provide the necessary level conversions.

------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------
  [SparkFun Block for Intel® Edison - Base](https://www.sparkfun.com/products/13045)\                                                                                                                                                                                                ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_Base.jpg)
  The Base Block utilizes the FT231x to provide a USB-Serial interface to the Console. There are two status LED\'s that illuminate when the UART is active. The Base Block also utilizes the USB OTG port to break out the USB-Netork functionality provided by the Edison module.   

  ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_Console_1.jpg)                                                                                                                                                                                           [SparkFun Block for Intel® Edison - Console](https://www.sparkfun.com/products/13039)\
                                                                                                                                                                                                                                                                                     The Console Block utilizes the FT231x to provide a USB-Serial interface to the Console. There are two status LED\'s that illuminate when the UART is active.

  [SparkFun Block for Intel® Edison - UART](https://www.sparkfun.com/products/13040)\                                                                                                                                                                                                ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_UART.jpg)
  The UART Block provides a level shifted interface to the console port. This is a great solution when USB is not an option. This allows the Edison module to be interfaced with legacy hardware by providing a protected signal interface.                                          
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## Input Blocks

The input Block category shows how each Block can bring data into the Edison for processing. These inputs can be raw signal level, or processed data from an external sensor. These inputs rely on a number of communication methods that are explained with each Block. These blocks take the raw functionality of the Edison and make it accessible to the user.

------------------------------------------------------------------------

[SparkFun Block for Intel® Edison - 9 Degrees of Freedom](https://www.sparkfun.com/products/13033)\
The 9 DOF Block leverages the [LSM9DS0](https://www.sparkfun.com/products/12636) to provide the Edison with an Inertial Measurement Unit (IMU). Use this Block to determine orientation, acceleration, and compass headings. The sensor utilizes [I2C](/tutorials/i2c) by default. With some reconfiguration of the jumpers, it can be used with the [SPI](/tutorials/serial-peripheral-interface-spi) interface.

![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_9DOF.jpg)

![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_ADC.jpg)

[SparkFun Block for Intel® Edison - ADC](https://www.sparkfun.com/products/13046)\
The [Analog-Digital Converter](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion) (ADC) Block is a great way to interface with sensors and devices that output signals in an analog (variable voltage) format. The block gives the users a 12-bit delta-sigma converter that is multiplexed to 4 single inputs or 2 differential input pairs. This Block communicates over I2C and with some jumpers, you can support up to 4 Blocks in a stack.

[SparkFun Block for Intel® Edison - Arduino](https://www.sparkfun.com/products/13036)\
The Arduino Block is extremely versatile. Programmed via UART1 on the expansion header, it\'s possible to use the Arduino as a serial interface to any sensor that would normally work with an [Arduino Pro Mini](https://www.sparkfun.com/products/11114). The Arduino Block is great when you need precise timing of sensors such as [WS2812 LED\'s](https://www.sparkfun.com/products/11820)

![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_Arduino.jpg)

![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_GPIO.jpg)

[SparkFun Block for Intel® Edison - GPIO](https://www.sparkfun.com/products/13038)\
The GPIO block provides level shifted input capabilities to the Edison. All general purpose GPIO has been broken out and grouped by function. The Edison has eight general GPIO, four GPIO with PWM capability, and four GPIO that can act as a second UART. Due to the bi-directional capability of the level shifters, it\'s necessary to provide pullup/pulldown resistors when using pins as an input.

[SparkFun Block for Intel® Edison - I2C](https://www.sparkfun.com/products/13034)\
The I2C Block is a great way to interface with any external sensor or device that communicates over [I2C](/tutorials/i2c). This block is capable of providing 3.3V or VSYS power to your devices. This device provides level shifting from the 1.8V Edison signals to either of the selected voltages on the Block. It is possible to hack this device to provide 5V level shifting.

![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_I2C.jpg)

![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_OLED.jpg)

[SparkFun Block for Intel® Edison - OLED](https://www.sparkfun.com/products/13035)\
Based on the [Micro OLED breakout](https://www.sparkfun.com/products/13003) and [MicroView](https://www.sparkfun.com/products/12923), the OLED Block gives the user 64x48 pixels of blue-on-black display. This Block also has two buttons and a [5-way switch](https://www.sparkfun.com/products/10063). Use these to create games, and interactive menues.

[SparkFun Block for Intel® Edison - UART](https://www.sparkfun.com/products/13040)\
The UART block can be useful in connecting the Edison with legacy hardware or GPS receivers. The UART block provides level shifted access to either UART1 or UART2. Using a [RS232 Shifter](https://www.sparkfun.com/products/449) it is possible to connect an Edison to RS232 devices commonly found in older automation equipment and instrumentation.

![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_UART.jpg)

------------------------------------------------------------------------

## Output Blocks

The output Block category shows how the Edison can utilize each block to control an external component or feature.

------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [SparkFun Block for Intel® Edison - Arduino](https://www.sparkfun.com/products/13036)\                                                                                                                                                                                                                                                                                                                   ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_Arduino.jpg)
  The Arduino Block is extremely versatile. Programmed via UART1 on the expansion header, it\'s possible to use the Arduino as a serial interface to any output device that would normally work with an [Arduino Pro Mini](https://www.sparkfun.com/products/11114). The Arduino Block is great when you need precise timing of outputs such as [WS2812 LED\'s](https://www.sparkfun.com/products/11820)   

  ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_GPIO.jpg)                                                                                                                                                                                                                                                                                                                      [SparkFun Block for Intel® Edison - GPIO](https://www.sparkfun.com/products/13038)\
                                                                                                                                                                                                                                                                                                                                                                                                           The GPIO block provides level shifted output capabilities to the Edison. All general purpose GPIO has been broken out and grouped by function. The Edison has eight general GPIO, four GPIO with PWM capability, and four GPIO that can act as a second UART. Due to the bi-directional capability of the level shifters, it\'s necessary to provide an external switch when using high current devices such as relays and LED\'s. The Level shifter is only capable of supplying 20mA. You can illuminate an LED directly from the level shifter, but it may appear less bright.

  [SparkFun Block for Intel® Edison - Dual H-Bridge](https://www.sparkfun.com/products/13043)\                                                                                                                                                                                                                                                                                                             ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_H_Bridge.jpg)
  The Dual H-bridge block is capable of driving two bushed DC motors up to 1A each from an external source. The voltage input can be from 5-15V DC. There is a jumper available that allows the motors to be driven from VSYS but this limits the motor voltage to 4V and 500mA per channel. This block is based off the [SparkFun Motor Driver](https://www.sparkfun.com/products/9457).                  

  ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_I2C.jpg)                                                                                                                                                                                                                                                                                                                       [SparkFun Block for Intel® Edison - I2C](https://www.sparkfun.com/products/13034)\
                                                                                                                                                                                                                                                                                                                                                                                                           The I2C Block is a great way to interface with any external sensor or device that communicates over [I2C](https://cdn.sparkfun.com/tutorials/i2c). This block is capable of providing 3.3V or VSYS power to your devices. This device provides level shifting from the 1.8V Edison signals to what either selected voltages on the Block. It is possible to hack this device to provide 5V level shifting. See the I2C Block hookup guide for more info.

  [SparkFun Block for Intel® Edison - OLED](https://www.sparkfun.com/products/13035)\                                                                                                                                                                                                                                                                                                                      ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_OLED.jpg)
  Based on the [Micro OLED breakout](https://www.sparkfun.com/products/13003) and [MicroView](https://www.sparkfun.com/products/12923), the OLED Block gives the user 64x48 pixels of blue-on-black display. Use this to create user feedback displays, games, and interactive menus.                                                                                                                      

  ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_PWM.jpg)                                                                                                                                                                                                                                                                                                                       [SparkFun Block for Intel® Edison - PWM](https://www.sparkfun.com/products/13042)\
                                                                                                                                                                                                                                                                                                                                                                                                           The PWM block adds additional PWM functionality to the Edison module. The PWM Block communicates over I2C and can control 8 channels with 12bit resolution. Using the address jumpers, it is possible to stack an additional 8-10 blocks (due to signal integrity breakdown). Use this block to control [LED\'s](https://www.sparkfun.com/categories/89) or [servos](https://www.sparkfun.com/categories/245).

  [SparkFun Block for Intel® Edison - UART](https://www.sparkfun.com/products/13040)\                                                                                                                                                                                                                                                                                                                      ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_UART.jpg)
  The UART block can be useful in connecting the Edison with legacy hardware. The UART block provides level shifted access to either UART1 or UART2. Using a [RS232 Shifter](https://www.sparkfun.com/products/449) it is possible to connect an Edison to RS232 devices commonly found in older automation equipment and instrumentation.                                                                 
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## Special Function Blocks

------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [SparkFun Block for Intel® Edison - Arduino](https://www.sparkfun.com/products/13036)\                                                                                                                                                                                                                                                                                                                                                                                         ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_Arduino.jpg)
  The Arduino Block is extremely versatile. Programmed via UART1 on the expansion header, it\'s possible to use the Arduino as a serial interface to anything that would normally work with an [Arduino Pro Mini](https://www.sparkfun.com/products/11114). The Arduino Block is great when you need precise timing of sensors or outputs such as [encoders](https://www.sparkfun.com/search/results?term=encoder) or [WS2812 LED\'s](https://www.sparkfun.com/products/11820)   

  ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_Base.jpg)                                                                                                                                                                                                                                                                                                                                                                                            [SparkFun Block for Intel® Edison - Base](https://www.sparkfun.com/products/13045)\
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 The Base is useful for mounting an Edison as a file system on a host computer. The Base Block provides the same functionality as the [Intel® Edison and Mini Breakout](https://www.sparkfun.com/products/13025) board. The Base Block has the added capability of powering the Edison through the Console port, freeing the OTG port for device usage.

  [SparkFun Block for Intel® Edison - microSD](https://www.sparkfun.com/products/13041)\                                                                                                                                                                                                                                                                                                                                                                                         ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_SD.jpg)
  The microSD card holder gives access to the Edison\'s high speed SD port. Turn your Edison into a mobile file server, high capacity data logger, or extend the file system of your OS.                                                                                                                                                                                                                                                                                         

  ![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/Block_OLED.jpg)                                                                                                                                                                                                                                                                                                                                                                                            [SparkFun Block for Intel® Edison - OLED](https://www.sparkfun.com/products/13035)\
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 The OLED Block earns it\'s special function categorization because it is considered an \"End Block\". It must always be at the end of a Block stack since it is a user interface. The OLED block was designed to allow users to create a custom controller or portable game system.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## How Do I Make My Own Blocks? 

If you have outgrown our [current offering](https://www.sparkfun.com/categories/272) of Blocks, we are here to help! In case you missed our [homepage post](https://www.sparkfun.com/news/1591), we released a template to jump start your next idea. This template is designed to help create new blocks that will interface with the existing ecosystem.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/EdisonEagle.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/2/EdisonEagle.png)

**[Here are our template design files](https://github.com/sparkfun/Sparkfun_Blocks_Template)**, take them and see what you can come up with! There are all kinds of helpful messages in the schematics and board files. The library parts for the Edison connectors are there as well.

[Download the Edison Block Template](https://github.com/sparkfun/Sparkfun_Blocks_Template)

Here is a detailed diagram of the Edison connector showing the pin numbers along with names and functions. This may also prove useful for testing signals.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/2/edison-pinout_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/2/edison-pinout_1.png)

[Download the Edison Pinout Diagram as a PDF](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/2/edison-pinout.pdf)

Hopefully we have given you a good start to understanding the SparkFun Blocks for Intel Edison ecosystem.