# Source: https://docs.silabs.com/openthread/3.0.0/bootloader-transitioning-guide-gsdk-v40-and-higher/09-callbacks.md

# Callbacks

In contrast to the AppBuilder workflow, callbacks are now part of **btl_callbacks_stub.c**. This file is added to the project when the **SPI Flash Storage** component is installed. This file contains dummy implementation of callbacks that the bootloader relies on. This file can be found in **gecko_sdk_<version> > platform > bootloader > storage > btl_callbacks_stub.c** as shown.

![image19](/bootloader-transitioning-guide-gsdk-v40-and-higher/0.1/images/sld795-image19.png)