# Source: https://docs.edgeimpulse.com/hardware/boards/ti-launchxl.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TI CC1352P Launchpad

The [Texas Instruments CC1352P Launchpad](https://www.ti.com/tool/LAUNCHXL-CC1352P) is a development board equipped with the multiprotocol wireless CC1352P microcontroller. The Launchpad, when paired with the BOOSTXL-SENSORS booster packs, is fully supported by Edge Impulse, and is able to sample accelerometer & microphone data, build models, and deploy directly to the device without any programming required.

If you don't have either booster pack or are using different sensing hardware, you can use the [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) to capture data from any other sensor type, and then follow the [Run TI Launchpad](/hardware/deployments/run-cpp-ti-launchxl) tutorial to run your impulse. Or, you can clone and modify the open source [firmware-ti-launchxl](https://github.com/edgeimpulse/firmware-ti-launchxl) project on GitHub.

The Edge Impulse firmware for this development board is open source and hosted on GitHub: [edgeimpulse/firmware-ti-launchxl](https://github.com/edgeimpulse/firmware-ti-launchxl).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/3ddcdb0-1628047820120_group_29.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=eb41d10728e4608b93d079a1c709d936" width="1493" height="1000" data-path=".assets/images/3ddcdb0-1628047820120_group_29.png" />
</Frame>

### Installing dependencies

To set this device up in Edge Impulse, you will need to install the following software:

1. [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
2. [Texas Instruments UniFlash](https://www.ti.com/tool/UNIFLASH)
   * Install the desktop version for your operating system [here](https://www.ti.com/tool/UNIFLASH)
   * Add the installation directory to your PATH
   * See [Troubleshooting](/hardware/boards/ti-launchxl#troubleshooting) for more details
3. On Linux:
   * GNU Screen: install for example via `sudo apt install screen`.

<Warning>
  **Problems installing the Edge Impulse CLI?**

  See the [Installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Warning>

### Connecting to Edge Impulse

With all the software in place it's time to connect the development board to Edge Impulse.

#### 1. Configure your hardware

To interface the Launchpad with sensor hardware, you will need to either connect the BOOSTXL-SENSORS to collect accelerometer data, or the CC3200AUDBOOST to collect audio data. Follow the guides below based on what data you want to collect.

<Info>
  **Before you start**

  The Launchpad jumper connections should be in their original configuration out of the box. If you have already modified the jumper connections, see the Launchpad's [User Guide](https://dev.ti.com/tirex/explore/node?devtools=LAUNCHXL-CC1352P-2\&node=A__ALFrE12-kDG3RNeAG6i7iA__cc13xx_devtools__FUz-xrs__LATEST) for the original configuration.
</Info>

##### Accelerometer Hardware Configuration Guide

Connecting the BOOSTXL-SENSORS board to the Launchpad is simple. Just orient the sensor board such that the `3V3` and `GND` markings on the booster pack line up with the Launchpad, and then attach the booster pack to the top header pins of the Launchpad, as shown below:

<Frame caption="Launchpad connected with sensor booster pack">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/2f31c09-39855d4-IMG_20210809_074506.jpg?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=0cfc6f81614f6fae5deafbf0bbb2b369" width="1333" height="1000" data-path=".assets/images/2f31c09-39855d4-IMG_20210809_074506.jpg" />
</Frame>

#### Audio Hardware Configuration Guide

**Extra Hardware Required**

You will need five extra [0.1" jumper wires](https://www.adafruit.com/product/266) to connect the CC3200AUDBOOST to the Launchpad, as described in the <a href="https://dev.ti.com/tirex/explore/content/simplelink_audio_plugin_3_30_00_06/docs/Quick_Start_Guide.html#hardware-setup">Texas Instruments documentation</a>.

The CC3200AUDBOOST board requires modifications to interface properly with the CC1352P series of Launchpads. The full documentation regarding these modifications is available from Texas Instruments in their [Quick Start Guide](https://dev.ti.com/tirex/explore/content/simplelink_audio_plugin_3_30_00_06/docs/Quick_Start_Guide.html#hardware-setup), and a summary of the steps to configure the board are shown below.

1. Disconnect conflicting pins on the Launchpad.

`Pins 26-30` on header `J3` conflict with the CC3200AUDBOOST pins and need to be disconnected. To do this easily, TI recommends bending the pins down as shown below.

<Frame caption="Disconnected pins on the CC1352P Launchpad">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/3f57274-launchpad-pin-modifications.jpg?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=7e29fe5853d2a09c36c12fc8ddf9ae3a" width="480" height="640" data-path=".assets/images/3f57274-launchpad-pin-modifications.jpg" />
</Frame>

##### Launchpad modifications are compatible across booster packs

All Edge Impulse supported booster packs do not use `pins 26-30` on header `J3`. If you have modified your Launchpad to interface with the audio booster pack, you can leave these pins disconnected when connecting other boards.

1. Connect jumper wires to the required pins

   The pin connections shown below are required by TI to interface between the two boards. Connect the pins by using jumper wires and following the diagram. For more information see the CC3200AUDBOOST [User Guide](https://www.ti.com/lit/ug/swru383a/swru383a.pdf?ts=1636125907650\&ref_url=https%253A%252F%252Fwww.ti.com%252Ftool%252FCC3200AUDBOOST) and [Quick Start Guide](https://dev.ti.com/tirex/explore/content/simplelink_audio_plugin_3_30_00_06/docs/Quick_Start_Guide.html#hardware-setup)

   <Frame caption="Jumper connections for CC3200AUDBOOST">
     <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/9d14b4a-audio-boosterpack-connections.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=5fd592adfb64df8d4e1399d724e9d7c5" width="1333" height="1000" data-path=".assets/images/9d14b4a-audio-boosterpack-connections.png" />
   </Frame>

   With the pins connected, your board should appear as shown below.

   <Frame caption="Properly configured CC3200AUDBOOST">
     <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/d5da5c4-cc3200audboost.jpg?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=d683c823015aff3cf3b4839cb9d09875" width="1334" height="1000" data-path=".assets/images/d5da5c4-cc3200audboost.jpg" />
   </Frame>

2. Align the `P1` pin on the booster pack with `3V3` pin on the Launchpad, and connect the two boards together.

   <Frame caption="TI Launchpad connected with audio booster pack">
     <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/c16e17a-PXL_20211105_165946590.jpg?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=140b9c7fdc8890a36010c5573cd7e3ed" width="1333" height="1000" data-path=".assets/images/c16e17a-PXL_20211105_165946590.jpg" />
   </Frame>

##### Using Audio and Accelerometer Hardware Simultaneously

In most cases it is possible to connect the sensor and audio booster pack at the same time. Allowing you to quickly switch between accelerometer and audio data collection. The primary constraint is that the BOOSTXL-SENSORS board must not have the TMP007 temperature sensor soldered on, as this conflicts with the audio interface when both booster packs are connected.

1. Ensure that the TMP007 temperature sensor is not present on the sensor booster pack. The board should have an unpopulated footprint for `U5` as shown below:

   <Frame caption="Unpopulated TMP007 footprint on sensor booster pack">
     <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/96d859f-PXL_20211105_1831273831.jpg?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=ddc444d53164de8acff12aeba3f04513" width="1112" height="1000" data-path=".assets/images/96d859f-PXL_20211105_1831273831.jpg" />
   </Frame>

2. Perform all modifications to the Launchpad and audio booster pack described in the [Audio Hardware Configuration Guide](/hardware/boards/ti-launchxl#audio-hardware-configuration-guide)

3. Connect the BOOSTXL-SENSORS booster pack directly to the Launchpad.

   <Frame caption="Launchpad connected with sensor booster pack">
     <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/39855d4-IMG_20210809_074506.jpg?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=c52dc437f6fa286c94b5176fd54ac9b2" width="1333" height="1000" data-path=".assets/images/39855d4-IMG_20210809_074506.jpg" />
   </Frame>

4. Connect the audio booster pack on top of the sensors booster pack. The final board should appear as shown below:

   <Frame caption="Launchpad connected with sensor and audio booster packs">
     <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/eac8b80-1df7f34-launchpad_with_boosterpacks.jpg?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=f62d16f42ad82798c28fa53bc4ec9d4a" width="1334" height="1000" data-path=".assets/images/eac8b80-1df7f34-launchpad_with_boosterpacks.jpg" />
   </Frame>

#### 2. Connect the development board to your computer

Use a micro-USB cable to connect the development board to your computer.

#### 3. Update the firmware

The development board does not come with the right firmware yet. To update the firmware:

1. [Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/ti-launchxl.zip), and unzip the file.
2. Open the flash script for your operating system (`flash_windows.bat`, `flash_mac.command` or `flash_linux.sh`) to flash the firmware.
3. Wait until flashing is complete, and press the RESET button once to launch the new firmware.

#### 4. Setting keys

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

**Which device do you want to connect to?**

The Launchpad enumerates two serial ports. The first is the **Application/User UART**, which the edge-impulse firmware communicates through. The other is an Auxiliary Data Port, which is unused.

When running the `edge-impulse-daemon` you will be prompted on which serial port to connect to. On Mac & Linux, this will appear as:

```
? Which device do you want to connect to? (Use arrow keys)
❯ /dev/tty.usbmodemL42003QP1 (Texas Instruments)
 /dev/tty.usbmodemL42003QP4 (Texas Instruments)
```

Generally, select the lower numbered serial port. This usually corresponds with the **Application/User UART**. On Windows, the serial port may also be verified in the **Device Manager**

If a selected serial port fails to connect. Test the other port before checking [troubleshooting](/hardware/boards/ti-launchxl#troubleshooting) for other common issues.

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### 5. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/68b9582-device-connected.jpg?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=ce5122dc39cf73554891f9bd5c02e0e9" width="1600" height="471" data-path=".assets/images/68b9582-device-connected.jpg" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build and run your first machine learning model with these tutorials:

* [Building a continuous motion recognition system](/tutorials/end-to-end/motion-recognition).
* [Sound recognition](/tutorials/hardware/ti-launchxl-keyword-spotting)

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse, and you can \[run your impulse locally]/run-inference/cpp-library/) with custom firmware or sensor data.

### Troubleshooting

**Failed to flash**

If the UniFlash CLI is not added to your PATH, the install scripts will fail. To fix this, add the installation directory of UniFlash (example `/Applications/ti/uniflash_6.4.0` on macOS) to your PATH on:

* [Windows](https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/)
* [macOS](https://www.architectryan.com/2012/10/02/add-to-the-path-on-mac-os-x-mountain-lion/)
* [linux](https://phoenixnap.com/kb/linux-add-to-path)

If during flashing you encounter further issues, ensure:

* The device is properly connected and/or the cable is not damaged.
* You have the proper permissions to access the USB device and run scripts. On macOS you can manually approve blocked scripts via `System Preferences->Security Settings->Unlock Icon`
* If on Linux you may want to try copying tools/71-ti-permissions.rules to /etc/udev/rules.d/. Then re-attach the USB cable and try again.

Alternatively, the `gcc/build/edge-impulse-standalone.out` binary file may be flashed to the Launchpad using the UniFlash GUI or web-app. See the [Texas Instruments Quick Start Guide](https://software-dl.ti.com/ccs/esd/uniflash/docs/v6_4/uniflash_quick_start_guide.html) for more info.


Built with [Mintlify](https://mintlify.com).