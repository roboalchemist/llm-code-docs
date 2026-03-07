# Source: https://docs.silabs.com/openthread/3.0.0/using-sl-coprocessors-with-openthread-border-router/03-build-and-installation-instructions-for-the-ncp-images.md

# Build and Installation Instructions for the NCP Images

## NCP Architecture Overview

In the standard NCP (Network Co-Processor) design, Thread network features run on the SoC while the application layer runs on a separate host processor. The host processor is typically more powerful than the OpenThread device, though it has higher power consumption.

This architecture offers power management advantages: the higher-power host can enter sleep mode while the lower-power OpenThread device stays active to maintain its Thread network connection. Additionally, since the SoC handles only the Thread stack and not the application layer, application development and testing can proceed independently of the OpenThread build.

## Building NCP Images

> **Note**: The following instructions only apply to NCP images built using Simplicity Studio for a given Simplicity SDK release.

To build an NCP image using the latest OpenThread, follow instructions on the [ot-efr32](https://github.com/openthread/ot-efr32) repo.

## Use Precompiled NCP Images

Silicon Labs has precompiled NCP images available for these boards with their associated image locations. The default precompiled images are configured for UART interface.

> **Note**: By default, the Silicon Labs Simplicity SDK uses Thread protocol version 1.4. A set of prebuilt NCP demo applications are provided with the OpenThread SDK.

## Build NCP Images Using Simplicity Studio

Silicon Labs has sample applications for several standard OpenThread NCP images.

1. Select **ot-ncp-ftd** or **ot-ncp-mtd** as an example for the default NCP image for the OpenThread Border Router over UART interface.
2. With your target part connected to your computer, open Simplicity Studio's **Project** tab and select **Create New Project**.
3. The Example Project & demos selection dialog opens. Use the **Keyword** filter to search for **ot-ncp** as an example for the default NCP image for the OpenThread Border Router. Select **ot-ncp-ftd** for Full Thread Device or **ot-ncp-mtd** for Minimal Thread Device and click **Create**.
4. The Project Configuration dialog opens. Rename your project, change the default project file location, and determine if you will link to or copy project files. Note that, if you change any linked resource, it is changed for any other project that references it. Click **FINISH.**
5. The Simplicity Project Configurator opens to the **OVERVIEW** tab. See the online _Simplicity Studio 6 Overview_ for details about the functionality available through the Project Configurator.  
   ![screenshot](/using-sl-coprocessors-with-openthread-border-router/0.1/images/sld1037-image5.png)
6. Compile and flash the application image as described in the [OpenThread Quick Start Guide](/openthread/3.0.0/openthread-quick-start-guide).

## Configure OpenThread Options in the NCP Images Using Simplicity Studio

1. Under the **SOFTWARE COMPONENTS** tab in your NCP project (.slcp), expand the **OpenThread** menu. Select **Stack (FTD)** for an NCP FTD build or **Stack (MTD)** for an NCP MTD build.
2. Click **Configure** to change the settings associated with the OpenThread build.  
   > **Note**: You can select the **Configurable Components** and **Installed Components** checkboxes to filter only those components you can configure successfully.  
   ![screenshot](/using-sl-coprocessors-with-openthread-border-router/0.1/images/sld1037-image6.png)
3. Configure the various compile-time settings for your NCP project. The various build options are explained in the OpenThread documentation at [https://openthread.io/guides/build](https://openthread.io/guides/build).  
   ![screenshot](/using-sl-coprocessors-with-openthread-border-router/0.1/images/sld1037-image7.png)

## Enable Host Wakeup GPIO Functionality

### Overview

The Host Wakeup GPIO feature enables the NCP to wake a sleeping host processor using a dedicated GPIO pin. When the NCP needs host attention (incoming data, network events, etc.), it sets the GPIO HIGH for a configurable duration, allowing the host to remain in low-power sleep states until needed.

### Configuration

1. Open your NCP project in Simplicity Studio and navigate to the **SOFTWARE COMPONENTS** tab.
2. Under the **OpenThread** menu, locate the **Stack (FTD)** or **Stack (MTD)** component and click **Configure**.
3. In the configuration editor, find the **Host wakeup GPIO functionality** section.  
   ![screenshot](/using-sl-coprocessors-with-openthread-border-router/0.1/images/sld1037-image8.png)
4. Enable **Enable host wakeup using a GPIO pin** using the toggle button.
5. Configure the timeout duration (in milliseconds) for clearing the host wakeup GPIO pin using `SL_OPENTHREAD_HOST_CLEAR_PIN_TIMEOUT_MS` (default: 10ms).  
   ![screenshot](/using-sl-coprocessors-with-openthread-border-router/0.1/images/sld1037-image9.png)
6. Configure the GPIO pin assignment:  
   - Navigate to the **Pin Tool** section or GPIO configuration  
   - Set `SL_OPENTHREAD_HOST_WAKEUP_GPIO_PORT` to the desired port (e.g., `SL_GPIO_PORT_C`)  
   - Set `SL_OPENTHREAD_HOST_WAKEUP_GPIO_PIN` to the desired pin number (e.g., `0`)  
   ![screenshot](/using-sl-coprocessors-with-openthread-border-router/0.1/images/sld1037-image10.png)
7. Save your configuration and rebuild the project.
