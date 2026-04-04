# Source: https://project-chip.github.io/connectedhomeip-doc/examples/lock-app/nxp/README.html

# Matter NXP Door Lock Example Application

## Contents

# Matter NXP Door Lock Example Application

* Overview

* Supported Platforms

* Environment Setup, Building, and Testing

* Data Model

* Manufacturing Data

## Overview

This reference application implements a Door Lock device type. It uses board buttons or `matter-cli` for user input and LEDs for state feedback. You can use this example as a reference for creating your own application.

The example is based on [Project CHIP](https://github.com/project-chip/connectedhomeip) and NXP SDK, and provides a prototype application that demonstrates device commissioning and different cluster control.

The door lock device communicates with clients over a low-power, 802.15.4 Thread network. It can be commissioned into an existing Matter network using a controller such as `chip-tool`.

This example implements a `User-Intent Commissioning Flow`, meaning that the user is required to press a button in order for the device to be ready for commissioning. The initial commissioning is usually performed using the `ble-thread` pairing method.

The Thread network dataset will be transferred on the device using a secure session over Bluetooth LE. In order to start the commissioning process, the user must enable BLE advertising on the device manually. To pair successfully, the commissioner must know the commissioning information corresponding to the device: setup passcode and/or discriminator. This data is usually encoded within a QR code or printed to the device’s UART console.

## Supported Platforms

The Door Lock example is supported on the following platforms :

NXP platform | Dedicated readme  
---|---  
MCXW71 | [NXP MCXW71 Guide](../../../platforms/nxp/nxp_mcxw71_guide.html)  
MCXW72 | [NXP MCXW72 Guide](../../../platforms/nxp/nxp_mcxw72_guide.html)  
  
For details on platform-specific requirements and configurations, please refer to the respective platform’s readme.

A list of popular standard door lock app targets is presented below. These targets can be used with the `build_example.py` tool.

Target name | Description  
---|---  
`nxp-<device>-freertos-lock-app-thread-mtd-frdm` | Default door lock  
`nxp-<device>-freertos-lock-app-thread-mtd-low-power-frdm` | Default low-power door lock  
`nxp-<device>-freertos-lock-app-thread-mtd-low-power-factory-frdm` | Default low-power door lock with factory data  
  
where `device` is one of the supported platforms.

## Environment Setup, Building, and Testing

All the information required to set up the environment, build the application, and test it can be found in the common readme for NXP platforms:

* NXP FreeRTOS Platforms : Refer to the [CHIP NXP Examples Guide for FreeRTOS platforms](../../../platforms/nxp/nxp_examples_freertos_platforms.html)

## Data Model

The application uses an NXP specific data model file:

Path | Description  
---|---  
`zap/lock-app.zap` | Data model for Door Lock device type  
  
## Manufacturing Data

The support for manufacturing data is enabled at build time when you use the appropriate build configuration files for this feature. Please refer to the [NXP Matter examples guide for FreeRTOS](../../../platforms/nxp/nxp_examples_freertos_platforms.html) for details on the build process and available build configurations. Manufacturing data can also be forced in the build command line by using the `CONFIG_CHIP_FACTORY_DATA=y` build option or by using the appropriate `build_examples.py` targets.

For a full guide on the manufacturing flow, please refer to the [Guide for writing manufacturing data on NXP devices](../../../platforms/nxp/nxp_manufacturing_flow.html).
