# Source: https://docs.edgeimpulse.com/hardware/boards/synaptics-katana.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Synaptics Katana EVK

The Synaptics Katana KA10000 board is a low-power AI evaluation kit from Synaptics that has the KA10000 AI Neural Network processor onboard. The evaluation kit is provided with a separate Himax HM01B0 QVGA monochrome camera module and 2 onboard zero power Vesper microphones. The board has an embedded STLIS2Dw12 accelerometer and an optional TI OPT3001 ambient light sensor. The connectivity to the board is provided with an IEEE 802.11n ultra low power WiFi module that is integrated with a Bluetooth 5.x, in addition to 4 Peripheral Modules (PMOD) connectors to provide I2C. UART, GPIO, I2S/SPI interfaces.

The package contains several accessories:

* The Himax image sensor.
* The PMOD-I2C USB firmware configuration board.
* The PMOD-UART USB adapter.
* 2 AAA batteries
* Enclosure.

The Edge Impulse firmware for this board is open source and hosted on GitHub: [edgeimpulse/firmware-synaptics-ka10000](https://github.com/edgeimpulse/firmware-synaptics-ka10000/).

<Frame caption="Synaptics Katana board with the UART and firmware configuration extension PMOD boards.">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/c626189-Synaptics.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=ecf74d2b193877626f243759ca02b539" width="1081" height="1000" data-path=".assets/images/c626189-Synaptics.png" />
</Frame>

### Installing dependencies

To set this device up in Edge Impulse, you will need to install the following software:

1. [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
2. On Linux:
   * GNU Screen: install for example via `sudo apt install screen`.

### Connecting to Edge Impulse

#### 1. Connect the development board to your computer

In order to update the firmware, it is necessary to use the PMOD-I2C USB firmware configuration board. The PMOD-I2C board is connected to the Katana board on the north right PMOD-I2C interface (as shown in the image at the top of this page), then you need to use a USB C cable to connect the firmware configuration board to the host PC.

In addition to the PMOD-I2C configuration board. You need to connect the PMOD-UART extension to the Katana board which is located on the left side of the board. Then you need to use a Micro-USB cable to connect the board to your computer.

#### 2. Update the firmware

The board is shipped originally with a sound detection firmware by default. You can upload new firmware to the flash memory by following these instructions:

* [Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/synaptics-ka10000.zip), and unzip the file.
* Verify that you have correctly connected the firmware configuration board.
* Run the flash script for your operating system (`flash_windows.bat`, `flash_mac.command` or `flash_linux.sh`) to flash the firmware.
* Wait until flashing is complete.

#### 3. Setting keys

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### 4. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse Studio.">
  <img src="https://mintcdn.com/edgeimpulse/bl3dk7kPQkfGIkjp/.assets/images/synaptics_device.png?fit=max&auto=format&n=bl3dk7kPQkfGIkjp&q=85&s=9a38238e95cbdac9df89c6c2ab8be335" width="1600" height="113" data-path=".assets/images/synaptics_device.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials, and board-specific public projects:

* [Image classification](/tutorials/end-to-end/image-classification)
* Eggs AI: [https://studio.edgeimpulse.com/public/20687/latest](https://studio.edgeimpulse.com/public/20687/latest)

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.


Built with [Mintlify](https://mintlify.com).