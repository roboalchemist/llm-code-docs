# Source: https://docs.edgeimpulse.com/hardware/boards/nordic-semi-thingy91.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Nordic Semi Thingy:91

The Nordic Semiconductor Thingy:91 is an easy-to-use battery-operated prototyping platform for cellular IoT using LTE-M, NB-IoT and GPS. It is ideal for creating Proof-of-Concept (PoC), demos and initial prototypes in your cIoT development phase. Thingy:91 is built around the [nRF9160 SiP](https://www.nordicsemi.com/Products/nRF9160) and is certified for a broad range of LTE bands globally, meaning the Nordic Thingy:91 can be used just about anywhere in the world. There is an [nRF52840](https://www.nordicsemi.com/Products/nRF52840) multiprotocol SoC on the Thingy:91. This offers the option of adding Bluetooth Low Energy connectivity to your project.

Nordic's Thingy:91 is fully supported by Edge Impulse. You'll be able to sample raw data, build models, and deploy trained machine learning models directly from the studio.

The Edge Impulse firmware for this development board is open source and hosted on GitHub: [edgeimpulse/firmware-nordic-thingy91](https://github.com/edgeimpulse/firmware-nordic-thingy91).

<Frame caption="Thingy:91">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/fa7b5c5-screen_shot_2021-10-07_at_23748_pm.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=a9a870283d20bcd8d6ed37ae5b554ccf" width="1196" height="928" data-path=".assets/images/fa7b5c5-screen_shot_2021-10-07_at_23748_pm.png" />
</Frame>

### Installing dependencies

To set this device up in Edge Impulse, you will need to install the following software:

1. [nRF Connect for Desktop](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-desktop).
2. [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
3. On Linux:
   * GNU Screen: install for example via `sudo apt install screen`.

<Warning>
  **Problems installing the CLI?**

  See the [Installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Warning>

<iframe src="https://www.youtube.com/embed/A0xU8o0AMqY" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

#### Updating the firmware

Before you start a new project, you need to update the Thingy:91 firmware to our latest build.

##### 1. Connect the development board to your computer

Use a micro-USB cable to connect the development board to your computer. Then, set the power switch to 'on'.

##### 2. Download the firmware

[Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/thingy91.zip). The extracted archive contains the following files:

1. `firmware.hex`: the Edge Impulse firmware image for the nRF9160 SoC, and
2. `connectivity-bridge.hex`: a connectivity application for the nRF52840 that you only need on older boards (hardware version \< 1.4)

##### 3. Update the firmware

1. Open nRF Connect for Desktop and launch the *Programmer application*.
2. Scroll down in the menu on the right and make sure **Enable MCUboot** is selected.

<Frame caption="Enable MCUboot">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/055a9b8-screenshot_2021-10-14_at_092546.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=c9bfb2b790c9cd836e2fdea7f131e2a5" width="1015" height="636" data-path=".assets/images/055a9b8-screenshot_2021-10-14_at_092546.png" />
</Frame>

1. Switch off the Nordic Thingy:91.
2. Press the multi-function button (SW3) while switching SW1 to the ON position.

<Frame caption="Switches">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/00eec83-screenshot_2021-10-14_at_093040.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=b2b2824b9bbd673a34cd6a91b700f45a" width="1060" height="692" data-path=".assets/images/00eec83-screenshot_2021-10-14_at_093040.png" />
</Frame>

1. In the Programmer navigation bar, click Select device.
2. In the menu on the right, click **Add HEX file > Browse**, and select the firmware.hex file from the firmware previously downloaded.
3. Scroll down in the menu on the right to Device and click **Write**:

<Frame caption="Flash the firmware">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/d13d260-screenshot_2021-10-14_at_093419.png?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=d769fd21c38bdc8d18c46d4e16456bb9" width="1019" height="645" data-path=".assets/images/d13d260-screenshot_2021-10-14_at_093419.png" />
</Frame>

1. In the **MCUboot DFU** window, click **Write**. When the update is complete, a Completed successfully message appears.
2. You can now disconnect the board.

<Warning>
  **Thingy:91 hardware version \< 1.4.0**

  Updating the firmware with older hardware versions may fail. Moreover, even if the update works, the device may later fail to connect to Edge Impulse Studio:

  ```
  [SER] Serial is connected, trying to read config...
  [SER] Failed to get info off device Timeout when waiting for >  (timeout: 5000) onConnected
  ```

  In these cases, you will also need to flash the `connectivity-bridge.hex` onto the nRF52840 in the Thingy:91. Follow the [steps here to update the nRF52840 SOC application](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/app_dev/device_guides/thingy91/thingy91_updating_fw_programmer.html#updating_the_firmware_in_the_nrf52840_soc) with the `connectivity-bridge.hex` file through USB or using an external probe."
</Warning>

### Connecting to Edge Impulse

With all the software in place it's time to connect the development board to Edge Impulse. From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This starts a wizard which asks you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

The Thingy:91 exposes multiple UARTs. If prompted, choose the first one:

```
? Which device do you want to connect to? (Use arrow keys)
❯ /dev/tty.usbmodem14401 (Nordic Semiconductor)
  /dev/tty.usbmodem14403 (Nordic Semiconductor)
```

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Thingy:91 in Devices tab">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/4aa9d8a-screenshot_2021-10-14_at_121319.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=8413a3d6c33df0572390a3c2f73c77b2" width="1064" height="287" data-path=".assets/images/4aa9d8a-screenshot_2021-10-14_at_121319.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with this tutorial:

* [Building a continuous motion recognition system](/tutorials/end-to-end/motion-recognition).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.


Built with [Mintlify](https://mintlify.com).