# Source: https://learn.sparkfun.com/tutorials/how-to-take-multiple-rfid-readings-simultaneously

## Introduction

In this tutorial, we\'ll show you how to set up the SparkFun Simultaneous RFID Reader to take multiple, if not nearly unlimited, [RFID](https://www.sparkfun.com/rfid) readings simultaneously by connecting either the M7E Hecto or M6E Nano directly to your computer using a USB-C connection and running Universal Reader Assistant (URA) software, which provides a simple and effective interface for configuring and managing your RFID reader. This is really useful for applications like measuring attendance at events, as well livestock management etc.

[![SparkFun Simultaneous RFID Reader - M7E Hecto](https://cdn.sparkfun.com/r/600-600/assets/parts/2/5/0/6/2/WRL-24738-Simultaneous-RFID-Reader-Feature.jpg)](https://www.sparkfun.com/sparkfun-simultaneous-rfid-reader-m7e-hecto.html)

### [SparkFun Simultaneous RFID Reader - M7E Hecto](https://www.sparkfun.com/sparkfun-simultaneous-rfid-reader-m7e-hecto.html) 

[ WRL-24738 ]

The SparkFun M7E Hecto Simultaneous RFID Reader simplifies reading UHF RFID tags (EPCglobal Gen 2) with its powerful M7E-HECT...

[ [\$309.95] ]

## Required Hardware 

To complete this project, you will need the following components:

- [SparkFun Simultaneous RFID Reader - M7E Hecto](https://www.sparkfun.com/products/24738) or\...

- [SparkFun Simultaneous RFID Reader - M6E Nano](https://www.sparkfun.com/products/14066) (older version)

- [Reversible USB A to C Cable - 0.3m](https://www.sparkfun.com/products/15426)

- A computer with a USB-C port (running Windows, which is required for URA software)

- [RFID Tags](https://www.sparkfun.com/categories/559) - we offer a bunch of different types, check out the link to see what works best for your application

For this simple setup, you do not need a microcontroller. However, in many (maybe most) practical applications, it would make sense to connect the RFID Reader to a microcontroller and add an antenna so you could take readings remotely without your computer in front of you and extend the range (which goes up to 3 or 4 feet in this example). Users who prefer to communicate with the RFID reader using the Serial PTH header should solder either wires or header pins to connect them to a 3.3V microcontroller, such as our [RedBoard Artemis](https://www.sparkfun.com/products/15444). Check out our [Hookup Guide](https://docs.sparkfun.com/SparkFun_Simultaneous_RFID_Reader_M7E/hardware_assembly/#communicating-via-usb-c-serial) for instructions on how to do this.

## Setting Up Your Simultaneous RFID Reader

To connect the RFID reader directly to your computer via USB-C. Follow these steps:

- Connect the USB-C Cable: Plug the USB-C end of the cable into the RFID reader and the USB-A end into your computer. This connection will provide both power and data communication between the RFID reader and your computer.

- Check the UART Selection Switch: Ensure that the UART selection switch on the RFID reader is in the correct position for USB operation. This is crucial for proper communication with the software.

## How to Download and Install Universal Reader Assistant (URA)

With the hardware set up, you can now move on to using the Universal Reader Assistant to interact with your RFID reader.

The Universal Reader Assistant (URA) software is a powerful tool designed to help you make full use of the capabilities of your SparkFun Simultaneous RFID Reader. Unfortunately, as mentioned, [the URA is only available for Windows.]

[Download URA](https://www.jadaktech.com/product/thingmagic-universal-reader-assistant/)

### Setting Up the URA

- Download the URA: Visit the [ThingMagic website](https://www.jadaktech.com/product/thingmagic-universal-reader-assistant/) to download the Universal Reader Assistant. Ensure you choose the correct version (32-bit or 64-bit) based on your Windows operating system.
- Install the URA: Once the download is complete, open the installer and follow the instructions provided by the installation wizard.

### Using the Software

- Connect Your RFID Reader: Make sure your Simultaneous RFID Reader is connected to your computer via USB. Open the Universal Reader Assistant after the installation is complete.
- Connection Wizard: Upon opening URA, you will be greeted by the Connection Wizard menu. Here, you can select the reader type and the port your RFID reader is connected to. (If you\'re familiar with the setup, you can skip this selection and move directly to the main menu. Otherwise, select the correct port for your RFID reader and click \"Next.\")

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/4/1/URA-Port_Selection.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/4/1/URA-Port_Selection.jpg)

- Connect to the Reader: The Connection Wizard should display your RFID reader\'s settings. You can click \"Connect & Read\" to start scanning tags immediately or \"Connect\" to access the main window without starting the read operation.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/4/1/URA-M7E_Selected.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/4/1/URA-M7E_Selected.jpg)

## URA Features and Tips

### Exploring URA Features

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/4/1/Screenshot_2024-09-12_at_12.47.24___PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/4/1/Screenshot_2024-09-12_at_12.47.24___PM.png)

The main window of the Universal Reader Assistant offers a wide range of settings and status options for the M6E Nano or M7E Hecto RFID readers. Here are some key features you can explore.

Read/Write Options: Adjust the RFID reader\'s power level, read/write settings, and other operational parameters.

**Practical Tech Tips** - most settings can be adjusted on the right drop down menu. Thermal Management: The RFID reader has an internal temperature sensor to prevent damage from overheating. If you encounter a temperature-limit fault, reduce the read power or improve cooling. Power Level: Start with a moderate power level (e.g., 500 dBm) to prevent the USB port from browning out. You can increase the power as needed but be mindful of thermal limits. Tag Read Efficiency: Experiment with different settings in the URA to optimize the RFID reader\'s performance for your specific application.