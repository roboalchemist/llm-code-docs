# Source: https://docs.edgeimpulse.com/hardware/boards/infineon-cy8ckit-062s2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Infineon CY8CKIT-062S2 Pioneer Kit

<Warning>
  **CY8CKIT-062S2 Pioneer Kit and CY8CKIT-028-SENSE expansion kit required**

  This guide assumes you have the [IoT sense expansion kit (CY8CKIT-028-SENSE)](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-028-sense/) attached to a [PSoC® 62S2 Wi-Fi® BLUETOOTH® Pioneer Kit](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-062s2-43012/)
</Warning>

The Infineon Semiconductor [PSoC® 62S2 Wi-Fi® BLUETOOTH® Pioneer Kit (Cypress CY8CKIT-062S2)](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-062s2-43012/) enables the evaluation and development of applications using the PSoC 62 Series MCU. This low-cost hardware platform enables the design and debug of the PSoC 62 MCU and the Murata 1LV Module (CYW43012 Wi-Fi + Bluetooth Combo Chip). The PSoC 6 MCU is Infineon' latest, ultra-low-power PSoC specifically designed for wearables and IoT products. The board features a PSoC 6 MCU, and a CYW43012 Wi-Fi/Bluetooth combo module. Infineon CYW43012 is a 28nm, ultra-low-power device that supports single-stream, dual-band IEEE 802.11n-compliant Wi-Fi MAC/baseband/radio and Bluetooth 5.0 BR/EDR/LE. When paired with the [IoT sense expansion kit](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-028-sense/), the PSoC® 62S2 Wi-Fi® BLUETOOTH® Pioneer Kit can be used to easily interface a variety of sensors with the PSoC™ 6 MCU platform, specifically targeted for audio and machine learning applications which are fully supported by Edge Impulse! You'll be able to sample raw data as well as build and deploy trained machine learning models to your PSoC® 62S2 Wi-Fi® BLUETOOTH® Pioneer Kit, directly from the Edge Impulse Studio.

The Edge Impulse firmware for this development board is open source and hosted on GitHub: [edgeimpulse/firmware-infineon-cy8ckit-062s2](https://github.com/edgeimpulse/firmware-infineon-cy8ckit-062s2).

<Frame caption="Infineon IoT sense expansion kit (CY8CKIT-028-SENSE) attached to Infineon CY8CKIT-062S2 Pioneer Kit">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/infineon-cy8ckit-062s2/hardware-details.png?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=751b5f290e1b79cb07fe329e01259101" width="680" height="495" data-path=".assets/images/infineon-cy8ckit-062s2/hardware-details.png" />
</Frame>

### Installing dependencies

To set this device up with Edge Impulse, you will need to install the following software:

1. [Infineon CyProgrammer](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.cypressprogrammer). A utility program we will use to flash firmware images onto the target.
2. The [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation) which will enable you to connect your CY8CKIT-062S2 Pioneer Kit directly to Edge Impulse Studio, so that you can collect raw data and trigger in-system inferences.

<Warning>
  **Problems installing the CLI?**

  See the [Installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Warning>

#### Updating the firmware

Edge Impulse Studio can collect data directly from your CY8CKIT-062S2 Pioneer Kit and also help you trigger in-system inferences to debug your model, but in order to allow Edge Impulse Studio to interact with your CY8CKIT-062S2 Pioneer Kit you first need to flash it with our [base firmware image](https://cdn.edgeimpulse.com/firmware/infineon-cy8ckit-062s2.zip).

##### 1. Download the base firmware image

[Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/infineon-cy8ckit-062s2.zip), and unzip the file. Once downloaded, unzip it to obtain the `firmware-infineon-cy8ckit-062s2.hex` file, which we will be using in the following steps.

##### 2. Connect the CY8CKIT-062S2 Pioneer Kit to your computer

Use a micro-USB cable to connect the CY8CKIT-062S2 Pioneer Kit to your development computer (where you downloaded and installed [Infineon CyProgrammer](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.cypressprogrammer)).

<Frame caption="Connecting the CY8CKIT-062S2 Pioneer Kit to your computer">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/infineon-cy8ckit-062s2/connect.png?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=2eea6057e8d5409975cdf64d7b6f97b8" width="955" height="495" data-path=".assets/images/infineon-cy8ckit-062s2/connect.png" />
</Frame>

##### 3. Load the base firmware image with Infineon CyProgrammer

You can use [Infineon CyProgrammer](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.cypressprogrammer) to flash your CY8CKIT-062S2 Pioneer Kit with our [base firmware image](https://cdn.edgeimpulse.com/firmware/infineon-cy8ckit-062s2.zip). To do this, first select your board from the dropdown list on the top left corner. Make sure to select the item that starts with `CY8CKIT-062S2-43012`:

<Frame caption="Connecting the CY8CKIT-062S2 Pioneer Kit to Infineon CyProgrammer">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/infineon-cy8ckit-062s2/cyprogrammer-select-board.png?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=ea25b555271ee108ded80df7b41658c8" width="771" height="455" data-path=".assets/images/infineon-cy8ckit-062s2/cyprogrammer-select-board.png" />
</Frame>

Then select the base firmware image file you downloaded in the first step above (i.e., the file named `firmware-infineon-cy8ckit-062s2.hex`). You can now press the `Connect` button to connect to the board, and finally the `Program` button to load the base firmware image onto the CY8CKIT-062S2 Pioneer Kit.

<Frame caption="Flashing the CY8CKIT-062S2 Pioneer Kit base image">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/infineon-cy8ckit-062s2/cyprogrammer-flash.png?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=d410fe284de9d14c87723ddf27742bb5" width="1095" height="810" data-path=".assets/images/infineon-cy8ckit-062s2/cyprogrammer-flash.png" />
</Frame>

<Warning>
  **Keep** [**Infineon CyProgrammer**](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.cypressprogrammer) **Handy**

  [Infineon CyProgrammer](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.cypressprogrammer) will be needed to upload any other project built on Edge Impulse, but the base firmware image only has to be loaded once.
</Warning>

### Connecting to Edge Impulse

With all the software in place, it's time to connect the CY8CKIT-062S2 Pioneer Kit to Edge Impulse.

#### 1. Connect the development board to your computer

Use a micro-USB cable to connect the development board to your computer.

#### 2. Setting keys

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### 3. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices** on the left sidebar. The device will be listed there:

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/infineon-cy8ckit-062s2/device-connected.png?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=9f8d81bffb48fd38b5f4c873cebcb29d" width="1082" height="313" data-path=".assets/images/infineon-cy8ckit-062s2/device-connected.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Building a continuous motion recognition system](/tutorials/end-to-end/motion-recognition).
* [Recognizing sounds from audio](/tutorials/end-to-end/sound-recognition).
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.


Built with [Mintlify](https://mintlify.com).