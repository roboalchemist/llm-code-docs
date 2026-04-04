# Source: https://docs.edgeimpulse.com/hardware/boards/nordic-semi-nrf9151-dk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Nordic Semi nRF9151 DK

The Nordic Semiconductor nRF9151 DK is a development board with an nRF9151 SIP incorporating a Cortex M33 for your application, a full LTE-M/NB-IoT and DECT NR+ modem with GPS along with 1 MB of flash and 256 KB RAM. The Development Kit is fully supported by Edge Impulse. You'll be able to sample raw data, build models, and deploy trained machine learning models directly from the studio. As the nRF9151 DK does not have any built-in sensors we recommend you to pair this development board with the [X-NUCLEO-IKS02A1](https://www.st.com/en/ecosystems/x-nucleo-iks02a1.html) shield (with a MEMS accelerometer and a MEMS microphone).

If you don't have the X-NUCLEO-IKS02A1 shield you can use the [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) to capture data from any other sensor, and then follow the [Run on Zephyr-based Nordic Semiconductor development boards](/hardware/deployments/run-cpp-zephyr-nordic) tutorial to run your impulse. Or, you can modify the example firmware (based on nRF Connect) to interact with other accelerometers or PDM microphones that are supported by Zephyr.

The Edge Impulse firmware for this development board is open source and hosted on GitHub: [edgeimpulse/firmware-nrf-9161](https://github.com/edgeimpulse/firmware-nordic-nrf91x1).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nordic/nRF9151dk/nRF9151_DK.png?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=b101dca7f8e4db9385266ea37dfbf96c" width="850" height="350" data-path=".assets/images/nordic/nRF9151dk/nRF9151_DK.png" />
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

#### 1. Plugging in the X-NUCLEO-IKS02A1 MEMS expansion shield

Remove the pin header protectors on the nRF9151 DK and plug the X-NUCLEO-IKS02A1 shield into the development board.

<Frame caption="X-NUCLEO-IKS02A1 shield plugged in to the nRF9151 DK">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nordic/nRF9151dk/nRF9151_DK_IKS02A1.png?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=d24eb4e1fdf1cb29d9375d45f59ab16f" width="1000" height="676" data-path=".assets/images/nordic/nRF9151dk/nRF9151_DK_IKS02A1.png" />
</Frame>

**Note:** Make sure that the shield does not touch any of the pins in the middle of the development board. This might cause issues when flashing the board or running applications. You can also remove the shield before flashing the board.

<Frame caption="Make sure the shield does not touch any of the pins in the middle of the development board.">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/d3323a4-nrf91_02.jpg?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=6ae3332586c413a5ab928174bd6ab279" width="1600" height="906" data-path=".assets/images/d3323a4-nrf91_02.jpg" />
</Frame>

#### 2. Connect the development board to your computer

Use a USB-C cable to connect the development board to your computer. Then, set the power switch to 'on'.

<Frame caption="Connect a USB-C cable to the short USB port on the short side of the board (red). Make sure the power switch is toggled on.">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nordic/nRF9151dk/nRF9151_DK_plugged_in.png?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=49926c24e859aaea113610ff09d2c603" width="1000" height="480" data-path=".assets/images/nordic/nRF9151dk/nRF9151_DK_plugged_in.png" />
</Frame>

#### 3. Configure the board

nRF9151 DK can be configured with Board Configurator tool that is inside [nRF Connect for Desktop](https://www.nordicsemi.com/Products/Development-tools/nRF-Connect-for-Desktop). All information on how this tool works and how to install it can be found in [the document page](https://docs.nordicsemi.com/bundle/nrf-connect-board-configurator/page/index.html).
For our application the board need to have following configuration:

<Frame caption="Configure the board using nRF Connect Board Configurator.">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nordic/nRF9151dk/nRF9151_config.jpg?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=1111f4156b6fc8b13cf0d2d72ecb29b0" width="1278" height="861" data-path=".assets/images/nordic/nRF9151dk/nRF9151_config.jpg" />
</Frame>

#### 4. Update the firmware

The development board does not come with the right firmware yet. To update the firmware:

1. The development board is mounted as a USB mass-storage device (like a USB flash drive), with the name `JLINK`. Make sure you can see this drive.
2. Install the [nRF Command Line Tools](https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Command-Line-Tools/Download).
3. [Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/nrf9151-dk.zip).
4. Flash the application by running the flash script for your Operating System.
5. Wait 20 seconds and press the **BOOT/RESET** button.

#### 5. Setting keys

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This starts a wizard which asks you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

The nRF9151 DK exposes multiple UARTs. If prompted, choose the top one:

```
? Which device do you want to connect to? (Use arrow keys)
❯ /dev/tty.usbmodem0010512237471 (SEGGER)
   /dev/tty.usbmodem0010512237473 (SEGGER)
```

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### 6. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nordic/nRF9151dk/nRF9151_DK_dashboard_status.png?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=e2107701d198dbc2aba74c1c5d28962d" width="1135" height="262" data-path=".assets/images/nordic/nRF9151dk/nRF9151_DK_dashboard_status.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Building a continuous motion recognition system](/tutorials/end-to-end/motion-recognition).
* [Recognizing sounds from audio](/tutorials/end-to-end/sound-recognition).
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.


Built with [Mintlify](https://mintlify.com).