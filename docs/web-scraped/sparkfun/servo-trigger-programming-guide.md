# Source: https://learn.sparkfun.com/tutorials/servo-trigger-programming-guide

## Introduction

The SparkFun Servo Trigger is a useful little board that control hobby servo motors. It comes in both [standard](https://www.sparkfun.com/products/13118) and [continuous rotation](https://www.sparkfun.com/products/13872) flavors.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/iso-top.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/iso-top.jpg)

The Servo Trigger was designed to make using servo motors easy, but it may not fit every application. You might need different timing, or different logic that interprets how the input is translated into the motor drive signal. You might even have some idea that doesn\'t involve servo motors at all!

Since the heart of the Servo Trigger is a microcontroller, the firmware can be reprogrammed. And, because the design is released as Open Source Hardware, the source code is published in the device\'s [GitHub Repository](https://github.com/sparkfun/Servo_Trigger). You\'re welcome to download and modify it!

This guide applies to both versions of the Servo Trigger. They use identical hardware, but they get loaded with different firmware.

This guide will introduce the tools used to program the Servo Trigger and guide you through the software design. By the end, you\'ll be able to transmute a regular Servo Trigger into a Continuous Rotation one (or vice versa), or even develop new behaviors from scratch.

### Suggested Reading

- [Servo Tutorial](https://learn.sparkfun.com/tutorials/hobby-servo-tutorial)
- [Servo Trigger Hookup Guide](https://learn.sparkfun.com/tutorials/servo-trigger-hookup-guide)
- [Continuous Rotation Servo Trigger Hookup Guide](https://learn.sparkfun.com/tutorials/continuous-rotation-servo-trigger-hookup-guide)

## Programming Tools

This guide will walk you through recreating the development environment used in Servo Trigger developemt. Atmel Studio makes a nice graphical front end and has a full-featured debugger, it is not required to recompile the firmware or reprogram the IC.\
\
However, it only runs under Windows.\
\
If you\'re running Linux or OSX, you can still use the the command-line AVR-GCC tools. Here is [a guide to setting them up.](http://maxembedded.com/2015/06/setting-up-avr-gcc-toolchain-on-linux-and-mac-os-x/) However, you\'ll be in uncharted territory, as the author isn\'t using those environments.

## The IDE

The Servo Trigger firmware was developed using [Atmel Studio 6.2](http://www.atmel.com/tools/studioarchive.aspx). Atmel Studio merges Microsoft\'s Visual Studio IDE with compiler and debugging tools targeting Atmel microcontrollers. The AVR tools use [AVR-GCC](http://www.nongnu.org/avr-libc/), the same compiler used by the Arduino IDE.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/splash.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/splash.png)

The IDE communicates with the microcontroller using a programming dongle. The Servo Trigger was developed with the [JTAGICE3](http://www.atmel.com/tools/JTAGICE3.aspx) and [AtmelICE PCBA](http://www.atmel.com/tools/atatmel-ice.aspx) debugging modules. These units can configure and program the chip and also offer a full-featured interactive debugger. You can pause execution and inspect the chip internals, which makes troubleshooting the application significantly simpler \-- especially because the Tiny84 lacks a serial port that could print debugging information. If you\'re coming from platforms that don\'t offer it, interactive debugging is a [very powerful technique](https://www.sparkfun.com/news/1894).

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/jtagice3_with_box.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/jtagice3_with_box.png)

If you\'re using Atmel Studio, the `/firmware/` directory in the repo contains the solution (\*.atsln) file.

## Getting Started

The Atmel debug tools are very convenient, but they require detailed configuration to get working. This page will walk you through creating a brand new project and getting the debugger talking to the Servo trigger.

### Hardware Configuration

The Servo Trigger has the standard 6-pin in-system programming (**ISP**) connector.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/header-callout.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/header-callout.png)

In order to connect to this header, you can solder a header to the PCB or use a pogo pin adapter.

[![Straight Header - Male (PTH, 0.1in., 2x3-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/8/1/2/12807-02.jpg)](https://www.sparkfun.com/header-2x3-male-0-1.html)

### [Straight Header - Male (PTH, 0.1in., 2x3-Pin)](https://www.sparkfun.com/header-2x3-male-0-1.html) 

[ PRT-12807 ]

This is a simple 2x3 male PTH header. This header is in the common configuration for an ISP connector. Each pin has a spacing...

[ [\$0.80] ]

[![SparkFun ISP Pogo Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/7/5/9/7/11591-02.jpg)](https://www.sparkfun.com/products/11591)

### [SparkFun ISP Pogo Adapter](https://www.sparkfun.com/products/11591) 

[ KIT-11591 ]

Pogo pins make life so much easier when you are trying to program without having to solder a single thing, and when you attac...

**Retired**

If you\'re going to use the debugger, soldering in a header is highly recommended. Otherwise, you\'ll have to hold the pogo pins in place for the duration of your debug session.

Finally, the debug interface box isn\'t designed to serve as a power supply for the board. You\'ll need to power the Servo Trigger by applying 5 Volts to its `VCC` and `GND` pins.

### Creating a New Project

In order to use the debugger, you\'ll need a project file. Let\'s create one from scratch.

To create a project, first open Atmel Studio, and select \"New Project\".

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/9/step1_3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step1_3.png)

Select the GCC C or C++ Executable Project options.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/9/step2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step2.png)

It will take a moment to initialize the project, then show a list of target microcontrollers. Select ATtiny84 from the list.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/9/step3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step3.png)

It takes another moment, then comes up with empty project. `main()` is the entry point for your application.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/9/step4.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step4.png)

### Programming Interface Modes

Before we go any deeper, lets take a quick break to explore the two modes that the debugger uses to communicate with the chip. While they appear to be similar, they aren\'t totally equivalent. They\'re also configured in *two places* in the IDE, and the settings need to match in order for them to function correctly.

- The first mode is **ISP**, which uses clock and data signals akin to SPI. It\'s the older of the two modes, intended to be used to program the flash memory on the processor and interact with some of the low-level nonvolatile configuration, such as the chip ID register and fuse bits. Being low level, it doesn\'t allow for interactive debugging.
- The other mode is **debugWIRE**. It was developed more recently, retrofitted into the chips, using communications over the reset pin. debugWIRE can program the flash and allows interactive debugging, but it can\'t access the ID register or fuse bits.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/9/modes.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/modes.png)

Since neither mode has all of the capabilities, we\'ll have to switch between them, depending on what we\'re doing. If you\'re having trouble using the features of one mode, the most likely problem is that the chip and IDE don\'t agree on the current mode.

[]

### Getting the Interface Talking The First Time

With a new project open in the IDE, connect the debugger module to the USB port.

Click \"Project-\> Properties\...\", then select the *Tool* tab along the left edge to configure the debugging tools.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/9/step5.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step5.png)

Select the connected debugger, and set the interface to **ISP**.

After selecting the interface, click on \"tools-\>device programming\" to open the chip configuration dialog. It will open with the tool, target device, and interface selected. Click *Apply*, and it initializes the interface. More information will appear in the lower portion of the window.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step6.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step6.png)

Connect the debugger unit to the servo trigger, and power it up. Click the \"Target Voltage Read\" button near the top right.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step7.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step7.png)

The neighboring box should indicate approximately 5.0V. This verifies that the chip has power and should be able to communicate.

Then, click the \"Read device signature\" button.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step8.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step8.png)

It should report an ID of `0x1E930C` in the neighboring box, indicating an ATTiny84.

*At this point, we\'ve got confidence that the ISP interface is working, and we can turn on debugWIRE mode.*

### Enabling debugWIRE

In the Device Programming dialog, click on the \"Fuses\" tab on the left side of the box. Then mark the box next to the \"DWEN\" (Debug Wire ENable) fuse. The circle next to the name will turn yellow, to indicate that the bit has not been programmed.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step9.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step9.png)

Make sure \"Verify after programming\" box is checked, then press \"program.\" The progress will be reported in the lower portion of the dialog. If the IDE requests a power cycle of the target, do so. At the end, it should say \"Verify registers \...OK\", and the circle next to DWEN should turn green.

At this point, close the Device Programming dialog. You should be back at the project properties tab. Now, switch the interface to debugWIRE.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/9/step10.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step10.png)

*DebugWIRE has been enabled by setting the fuse on the chip, and the IDE has been instructed to use it instead of ISP.*

### Using Debug Wire

After the steps above have been completed, select `Debug->Start Debugging and Break`.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step11.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step11.png)

The compiler will run, and the IDE will rearrange its windows several times. Ultimately, it will open some memory inspection windows and the source code file.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/9/step12.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step12.png)

The yellow arrow in the left margin indicates that the debugger is running and has paused at the entry to `main()`.

At this point, Atmel Studio performs like most debuggers. You can set breakpoints on specific lines of code, observe the call stack, inspect variables, and interact with the peripherals by accessing I/O registers in the memory map.

When you\'re done, select the \"debug-\>stop debugging\" option.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step13.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step13.png)

The program we\'ve got in the default empty project is pretty trivial \-- main contains an empty, infinite loop. If we were developing a more meaningful application, we would be adding more code to the source file, building and debugging as needed.

If you\'re making round trips from the editor to the debugger and back, stopping debugging is a reasonable way to switch modes.

If, however, you need to go back to the Device Programming dialog (for example, to change clock settings or adjust other fuse bits), you\'ll need to disable debugWIRE when ending the debug session.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step14.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step14.png)

This clears the DWEN fuse. You can then return to the [first time](https://learn.sparkfun.com/tutorials/servo-trigger-programming-guide/getting-started#firsttime) instructions above. Don\'t forget that the project configuration and device programming need to both be set to ISP. To return to debug mode, you\'ll need to set the DWEN fuse again.

### When You Get Stuck

It plays out like this: Yesterday you were debugging, today you start and decide to go and check the chip configuration in the Device Programming dialog.

Nothing works, and the error details contain \"Got 0xc0, expected 0x00.\"

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step15.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/step15.png)

The trick to unjamming it:

- Set the project to debugWIRE.
- Start a debug session (Debug-\>Start Debugging and Break).
- Once the debugger is initialized, select \"Debug-\>Disable debugWIRE and Close\" to get out.
- Set the project back to ISP, and now the Device Programming dialog should be functional.

### One Final Warning

Be careful playing with the fuse bits. It\'s possible to select invalid clock configurations, or lock the programming interface, which leave the processor in hard to recover states.

Knowing the fundamentals of starting and stopping the debugger, lets look more closely at the Servo Trigger firmware design.

## Firmware Modifications

Let\'s take a look at some of the finer points of the Servo Trigger code.

There\'s a single source file in the project, `ServoTrigger.c`, and some additional configuration in the Atmel Studio project.

### Timing

The range of transit times accessed by the `T` potentiometer is defined by a table of software values \-- the table interprets pot position using an exponential curve, which allows for fine control of very short times on the low end, but still permits a useful longer range at the top. But perhaps these times don\'t fit your application especially well \-- maybe you need extra resolution at the low end, or much longer times at the top end. You can change the timing table to do this.

In the GitHub repository, there is a speadsheet, [translation.ods](https://github.com/sparkfun/Servo_Trigger/blob/master/Firmware/translation.ods), which calculates the timing tables. Simply type the desired time in seconds into the green cells. The sheet recalculates the timing values, and updates the yellow cells. Cut and paste the yellow cells into the `timelut` array.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/9/spreadsheet.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/spreadsheet.png)

The table is only 17 entries long, which seems rather short \-- but keep in mind we\'re using a microcontroller with only 8KB of flash memory and 512 Bytes of RAM \-- we wouldn\'t want the timing table to fill the whole memory. To increase resolution between the table entries, the firmware performs [linear interpolation](http://en.wikipedia.org/wiki/Linear_interpolation) to create more finely grained points in between.

### Modes

The Servo Trigger comes with a couple of response modes that should be useful for most servo control needs, but, in the case they\'re not a good fit, they can be modified.

The two versions of the product (standard and continuous rotation) are managed with a different build configuration for each version. You can select the build configurations in the toolchain tab of the project settings. If all you\'re looking to do is transmute a regular Servo Trigger into a Continuous Rotation one (or vice versa), simply select the desired configuration.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/build-configs.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/build-configs.png)

The modes are configured by defining symbols that get passed to the compiler. All of the modal variations are present in the same source code, enabled using macros. You can select which modes get loaded by changing the compile-time symbols in the project. In Atmel Studio, select the \"Servo Trigger\" tab, then navigate to \"Toolchain-\> AVR/GNU C Compiler-\>Symbols\" item.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/9/CR-macros.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/CR-macros.png)

If you\'re using the command-line tools, the symbol definitions are found in the compiler invocation in the Makefile.

The `FSMA` and `FSMB` symbols determine which modes are programmed on the Servo Trigger. FSMA defines the unjumpered (default) mode, and FSMB defines the jumpered mode. There are five modes currently defined in the source file.

1.  `bistableFSM` - The default mode - when the input is asserted, it moves from position A to B. While input is held, it will stay at B. When released, it moves back to A.
2.  `oneshotFSM` - Does a complete cycle every time the input is asserted - from A to B, then back to A.
3.  `ctpFSM`- A customization of the oneshotFSM for interactive artist Christopher T Palmer, which allows the B-to-A return cycle to be interrupted by a fresh input actuation.
4.  `togglingFSM` - Each time the input is asserted, it changes from A to B, or B to A. This mode is especially useful for driving continous rotation servos.
5.  `astableFSM` - When the input is asserted, it cycles back and forth between A and B. When the input is inactive, it sits where it was.

You can put any mode in either slot, or even put the same mode in both.

------------------------------------------------------------------------

## Implementation Details

As you may have guessed from the names, the modes are implemented using Finite State Machines. [Finite state machines](https://www.sparkfun.com/news/1801) are a design concept the defines a set of states and a corresponding set of rules that determine how to transition between the states.

Within the Servo Trigger, each mode uses the same basic set of states, which in turn describe how it drives the servo. The states are:

1.  Sitting at position A.
2.  Moving from A to B.
3.  Sitting in position B.
4.  Moving from B to A.

The rules that define when the states can change can alter the behavior in significant ways. The different modes of the Servo Trigger are all implemented using the same states but with different transition rules.

FSMs are commonly illustrated using \"bubble diagrams,\" which draw the states as circles and the rules as arrows between the circles. Here\'s the bubble diagram for the bistable FSM.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/bubble-diag2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/9/bubble-diag2.png)

#### Building New State Machines

In the Servo Trigger, a state machine is implemented as a single function, which contains a `switch` statement wherein each state is a `case`. At the start of every PWM cycle, the state machine function is called to determine the pulse width and possibly move to new states.

If you want to implement a new state machine, it can be useful to start by drawing the bubble diagram.

If your new FSM is a slight alteration to an existing one, the next best place to look at the existing FSMs \-- it might be as simple as transplanting a state transition rule from one function to another. If your FSM is more ambitious, it\'s still useful to read and understand how the FSM interacts with the rest of the firmware.

Your application may need a subtle variation of an existing FSM or a complete re-formulation. Since the source code is available, you\'re welcome to modify it to suit your needs!

### Starting From Scratch

The Servo Trigger can also be used as an ATTiny84 development board with three trimpots on it for any application you can dream up. Start with an empty project as described in the [Getting Started](https://learn.sparkfun.com/tutorials/servo-trigger-programming-guide/getting-started) section, and start programming at `main()`!