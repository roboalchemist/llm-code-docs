# Source: https://docs.edgeimpulse.com/hardware/boards/silabs-thunderboard-sense-2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SiLabs Thunderboard Sense 2

The Silicon Labs Thunderboard Sense 2 is a complete development board with a Cortex-M4 microcontroller, a wide variety of sensors, a microphone, Bluetooth Low Energy and a battery holder - and it's fully supported by Edge Impulse. You'll be able to sample raw data, build models, and deploy trained machine learning models directly from the studio - and even stream your machine learning results over BLE to a phone.

<Warning>
  This board is **Not recommended for new designs**. For a replacement, see the [EFR32xG24 Dev Kit](https://www.silabs.com/development-tools/wireless/efr32xg24-dev-kit) which is [also fully supported by Edge Impulse](/hardware/boards/silabs-xg24-devkit)
</Warning>

The Edge Impulse firmware for this development board is open source and hosted on on GitHub: [edgeimpulse/firmware-silabs-thunderboard-sense-2](https://github.com/edgeimpulse/firmware-silabs-thunderboard-sense-2).

<Frame caption="Silicon Labs Thunderboard Sense 2">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/7a321dd-thunderboard-sense-two-640pxpng.jpeg?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=4a234f4fd3d133cab14e855f66c626fc" width="640" height="545" data-path=".assets/images/7a321dd-thunderboard-sense-two-640pxpng.jpeg" />
</Frame>

### Installing dependencies

To set this device up in Edge Impulse, you will need to install the following software:

1. [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
2. On Linux:
   * GNU Screen: install for example via `sudo apt install screen`.

<Warning>
  **Problems installing the CLI?**

  See the [Installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Warning>

### Connecting to Edge Impulse

With all the software in place it's time to connect the development board to Edge Impulse.

#### 1. Connect the development board to your computer

Use a micro-USB cable to connect the development board to your computer. The development board should mount as a USB mass-storage device (like a USB flash drive), with the name `TB004`. Make sure you can see this drive.

#### 2. Update the firmware

The development board does not come with the right firmware yet. To update the firmware:

1. [Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/silabs-thunderboard-sense2.bin).
2. Drag the `silabs-thunderboard-sense2.bin` file to the `TB004` drive.
3. Wait 30 seconds.

#### 3. Setting keys

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This will start a wizard which will ask you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### 4. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/60c2e13-screenshot_2020-10-04_at_111835.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=4987bf68994cce9e88d4136cc0c0e1a6" width="1600" height="399" data-path=".assets/images/60c2e13-screenshot_2020-10-04_at_111835.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Building a continuous motion recognition system](/tutorials/end-to-end/motion-recognition).
* [Recognizing sounds from audio](/tutorials/end-to-end/sound-recognition).
* [Keyword spotting](/tutorials/end-to-end/sound-recognition).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

Did you know? You can also stream the results of your impulse over BLE to a nearby phone or gateway: see [Streaming results over BLE to your phone](https://github.com/edgeimpulse/firmware-silabs-thunderboard-sense-2#streaming-results-over-ble-to-your-phone).

### Bluetooth Demo

Our firmware is equipped with a simple BLE demo showing how to start/stop the inference over the BLE and acquire the results.

To use the demo, first install the **EFR Connect BLE Mobile App** on your mobile phone:

* [EFR Connect BLE Mobile App at Google Play](https://play.google.com/store/apps/details?id=com.siliconlabs.bledemo)
* [EFR Connect BLE Mobile App at Apple App Store](https://apps.apple.com/pl/app/efr-connect-ble-mobile-app/id1030932759)

Make sure your board is flashed with [a pre-built binary](https://cdn.edgeimpulse.com/firmware/silabs-thunderboard-sense2.bin). Power on the board and run the **EFR Connect BLE Mobile App**

1. Scan your neighborhood for BLE devices

   <Frame caption="Scan for BLE devices">
     <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/silabs-ble-demo/1.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=45fd909b5ffe0f3972a2955ea439e5d4" width="405" height="840" data-path=".assets/images/silabs-ble-demo/1.jpg" />
   </Frame>
2. Look for the device named **Edge Impulse** and tap **Connect**

   <Frame caption="Connect with Edge Impulse device">
     <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/silabs-ble-demo/2.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=fca721fcb9360e63c0c6f2f32d0d7c45" width="405" height="877" data-path=".assets/images/silabs-ble-demo/2.jpg" />
   </Frame>
3. Scroll down to **Unknown service** with UUID `DDA4D145-FC52-4705-BB93-DD1F295AA522` and select **More Info**

   <Frame caption="More info for Unknown service">
     <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-ble-demo/3.jpg?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=d74f233ad25457061f60368941860cfc" width="405" height="877" data-path=".assets/images/silabs-ble-demo/3.jpg" />
   </Frame>
4. Select **Write** for characteristics with UUID `02AA6D7D-23B4-4C84-AF76-98A7699F7FE2`

   <Frame caption="Select write for characteristic">
     <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-ble-demo/4.jpg?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=76bbf0b307c70d09f1690e17fd4dec7d" width="405" height="840" data-path=".assets/images/silabs-ble-demo/4.jpg" />
   </Frame>
5. In the **Hex** field enter `01` and press **Send**. This will start inferencing, the device should start blinking with LEDs.

   <Frame caption="Write 01 to characteristic">
     <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-ble-demo/5.jpg?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=6e44be65fab095e17d2b0396a419af0e" width="405" height="877" data-path=".assets/images/silabs-ble-demo/5.jpg" />
   </Frame>
6. For another characteristic with UUID `61A885A4-41C3-60D0-9A53-6D652A70D29C` enable **Notify** and observe the reported inference results.

   <Frame caption="Enable notify">
     <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-ble-demo/6.jpg?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=1bb98ee2d0f716828e45ef3da05c7575" width="405" height="840" data-path=".assets/images/silabs-ble-demo/6.jpg" />
   </Frame>

   <Frame caption="Observe reported inference results">
     <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-ble-demo/7.jpg?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=d853ea534142e6d1bde8d452b0184071" width="405" height="840" data-path=".assets/images/silabs-ble-demo/7.jpg" />
   </Frame>
7. To stop the inference, send `00` to the characteristics `02AA6D7D-23B4-4C84-AF76-98A7699F7FE2`

### Troubleshooting

#### Dragging and dropping Edge Impulse .bin file results in FAIL.TXT

When dragging and dropping an Edge Impulse pre-built .bin firmware file, the binary seems to flash, but when the device reconnects a FAIL.TXT file appears with the contents "Error while connecting to CPU" and the following errors appear from the [Edge Impulse CLI impulse runner](/tools/clis/edge-impulse-cli/impulse-runner):

```
$ edge-impulse-run-impulse
Edge Impulse impulse runner v1.12.5
[SER] Connecting to /dev/tty.usbmodem0004401612721
[SER] Serial is connected, trying to read config...
[SER] Failed to get info off device:undefined. Is this device running a binary built through Edge Impulse? Reconnecting in 5 seconds...
[SER] Serial is connected, trying to read config...
```

To fix this error, install the Simplicity Studio 5 IDE and flash the binary through the IDE's built in "Upload application..." menu under "Debug Adapters", and select your Edge Impulse firmware to flash:

<Frame caption="Simplicity Studio 5 IDE Debug Adapters window">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/2ef0b3b-screen_shot_2021-03-11_at_91450_am.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=f81e004eb3c5e8b340a102e7c273cb1d" width="1012" height="744" data-path=".assets/images/2ef0b3b-screen_shot_2021-03-11_at_91450_am.png" />
</Frame>

Your Edge Impulse inferencing application should then run successfully with `edge-impulse-run-impulse`.


Built with [Mintlify](https://mintlify.com).