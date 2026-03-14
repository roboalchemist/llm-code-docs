# Source: https://docs.edgeimpulse.com/hardware/boards/nordic-semi-nrf9160-dk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Nordic Semi nRF9160 DK

The Nordic Semiconductor nRF9160 DK is a development board with an nRF9160 SIP incorporating a Cortex M-33 for your application, a full LTE-M/NB-IoT modem with GPS along with 1 MB of flash and 256 KB RAM. It also includes an nRF52840 board controller with Bluetooth Low Energy connectivity. The Development Kit is fully supported by Edge Impulse. You'll be able to sample raw data, build models, and deploy trained machine learning models directly from the studio. As the nRF9160 DK does not have any built-in sensors we recommend you to pair this development board with the [X-NUCLEO-IKS02A1](https://www.st.com/en/ecosystems/x-nucleo-iks02a1.html) shield (with a MEMS accelerometer and a MEMS microphone).

If you don't have the X-NUCLEO-IKS02A1 shield you can use the [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) to capture data from any other sensor, and then follow the [Run on Zephyr-based Nordic Semiconductor development boards](/hardware/deployments/run-cpp-zephyr-nordic) tutorial to run your impulse. Or, you can modify the example firmware (based on nRF Connect) to interact with other accelerometers or PDM microphones that are supported by Zephyr.

The Edge Impulse firmware for this development board is open source and hosted on GitHub: [edgeimpulse/firmware-nrf-91](https://github.com/edgeimpulse/firmware-nrf-91).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/768dd08-9160.jpg?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=4278f6575e886baacdab7dd67c5f4861" width="1600" height="685" data-path=".assets/images/768dd08-9160.jpg" />
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

<iframe src="https://www.youtube.com/embed/aXxOphYCOn8" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

#### 1. Plugging in the X-NUCLEO-IKS02A1 MEMS expansion shield

Remove the pin header protectors on the nRF9160 DK and plug the X-NUCLEO-IKS02A1 shield into the development board.

<Frame caption="X-NUCLEO-IKS02A1 shield plugged in to the nRF9160 DK">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/172bae4-nrf91_01.jpg?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=744c87b1575682a9b26799206dc486a1" width="1600" height="990" data-path=".assets/images/172bae4-nrf91_01.jpg" />
</Frame>

**Note:** Make sure that the shield does not touch any of the pins in the middle of the development board. This might cause issues when flashing the board or running applications. You can also remove the shield before flashing the board.

<Frame caption="Make sure the shield does not touch any of the pins in the middle of the development board.">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/d3323a4-nrf91_02.jpg?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=6ae3332586c413a5ab928174bd6ab279" width="1600" height="906" data-path=".assets/images/d3323a4-nrf91_02.jpg" />
</Frame>

#### 2. Connect the development board to your computer

Use a micro-USB cable to connect the development board to your computer. There are two USB ports on the development board, use the one on the *short* side of the board. Then, set the power switch to 'on'.

<Frame caption="Connect a micro USB cable to the short USB port on the short side of the board (red). Make sure the power switch is toggled on.">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/8b1d84f-nrf91_03.jpg?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=16375d9bcec7e4c4ba4f92a4fcfa95ee" width="1600" height="738" data-path=".assets/images/8b1d84f-nrf91_03.jpg" />
</Frame>

#### 3. Update the firmware

The development board does not come with the right firmware yet. To update the firmware:

1. The development board is mounted as a USB mass-storage device (like a USB flash drive), with the name `JLINK`. Make sure you can see this drive.
2. Install the [nRF Command Line Tools](https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Command-Line-Tools/Download).
3. [Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/nrf9160-dk.zip).
4. Flash the board controller, **you only need to do this once**. Go to step 4 if you've performed this step before.
   * Ensure that the `PROG/DEBUG` switch is in `nRF52` position.
   * Copy `board-controller.bin` to the `JLINK` mass storage device.

<Frame caption="Ensure that the PROG/DEBUG switch is in nRF52 position to flash the board controller.">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/d8a7378-nrf91_04.jpg?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=d33291289f5224037352a198f186b8f5" width="1600" height="694" data-path=".assets/images/d8a7378-nrf91_04.jpg" />
</Frame>

1. Flash the application:
   * Ensure that the `PROG/DEBUG` switch is in `nRF91` position.
   * Run the flash script for your Operating System.
2. Wait 20 seconds and press the **BOOT/RESET** button.

#### 4. Setting keys

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This starts a wizard which asks you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

The nRF9160 DK exposes multiple UARTs. If prompted, choose the top one:

```
? Which device do you want to connect to? (Use arrow keys)
❯ /dev/tty.usbmodem0009601707951 (SEGGER)
   /dev/tty.usbmodem0009601707953 (SEGGER)
   /dev/tty.usbmodem0009601707955 (SEGGER)
```

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### 5. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/de18ce2-screenshot_2021-08-17_at_162509.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=018b29fa6e145d6d348dfa241d23fe25" width="1600" height="401" data-path=".assets/images/de18ce2-screenshot_2021-08-17_at_162509.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Building a continuous motion recognition system](/tutorials/end-to-end/motion-recognition).
* [Recognizing sounds from audio](/tutorials/end-to-end/sound-recognition).
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.


Built with [Mintlify](https://mintlify.com).