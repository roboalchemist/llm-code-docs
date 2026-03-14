# Source: https://docs.edgeimpulse.com/hardware/boards/nordic-semi-nrf5340-dk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Nordic Semi nRF5340 DK

The Nordic Semiconductor nRF5340 DK is a development board with dual Cortex-M33 microcontrollers, QSPI flash, and an integrated BLE radio - and it's fully supported by Edge Impulse. You'll be able to sample raw data, build models, and deploy trained machine learning models directly from the studio. As the nRF5340 DK does not have any built-in sensors we recommend you to pair this development board with the [X-NUCLEO-IKS02A1](https://www.st.com/en/ecosystems/x-nucleo-iks02a1.html) shield (with a MEMS accelerometer and a MEMS microphone).

If you don't have the X-NUCLEO-IKS02A1 shield you can use the [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) to capture data from any other sensor, and then follow the [Run on Zephyr-based Nordic Semiconductor development boards](/hardware/deployments/run-cpp-zephyr-nordic) tutorial to run your impulse. Or, you can modify the example firmware (based on nRF Connect) to interact with other accelerometers or PDM microphones that are supported by Zephyr.

The Edge Impulse firmware for this development board is open source and hosted on GitHub: [edgeimpulse/firmware-nrf52840-5340](https://github.com/edgeimpulse/firmware-nrf52840-5340).

<Frame caption="Nordic Semiconductors nRF5340 DK development board">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/1e72353-nrf5340dk.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=8ca6ff5e831ee20af6c449b702c7e803" width="754" height="350" data-path=".assets/images/1e72353-nrf5340dk.png" />
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

<iframe src="https://www.youtube.com/embed/MKQIQ2lvJfk" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

#### 1. Plugging in the X-NUCLEO-IKS02A1 MEMS expansion shield

Remove the pin header protectors on the nRF5340 DK and plug the X-NUCLEO-IKS02A1 shield into the development board.

<Frame caption="X-NUCLEO-IKS02A1 shield plugged in to the nRF5340 DK">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/1240902-nrf53_01.jpg?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=23a300b75f367ca8dc0c14dd8b6645e2" width="1400" height="892" data-path=".assets/images/1240902-nrf53_01.jpg" />
</Frame>

**Note:** Make sure that the shield does not touch any of the pins in the middle of the development board. This might cause issues when flashing the board or running applications.

<Frame caption="Make sure the shield does not touch any of the pins in the middle of the development board.">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/9d89f47-nordic06.jpg?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=07a77ae8446ff966bd94e1eb817dec9d" width="1400" height="757" data-path=".assets/images/9d89f47-nordic06.jpg" />
</Frame>

#### 2. Connect the development board to your computer

Use a micro-USB cable to connect the development board to your computer. There are two USB ports on the development board, use the one on the *short* side of the board. Then, set the power switch to 'on'.

<Frame caption="Connect a micro USB cable to the short USB port on the short side of the board (red). Make sure the power switch is toggled on.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/4c188d6-nrf53_02.jpg?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=1647b32876754aff5ec667b7cf51e27b" width="1400" height="709" data-path=".assets/images/4c188d6-nrf53_02.jpg" />
</Frame>

#### 3. Update the firmware

The development board does not come with the right firmware yet. To update the Firmware + Networking Component:

<Info>
  **Firmware + Networking Component** This firmware contains both the application and the networking core firmware component.
</Info>

1. The development board is mounted as a USB mass-storage device (like a USB flash drive), with the name `JLINK`. Make sure you can see this drive.
2. [Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/nrf5340-dk.zip).
3. Install and open the [nRF Connect for Desktop](https://www.nordicsemi.com/Products/Development-tools/nRF-Connect-for-Desktop) and go to the Programmer application
4. Drag and drop the `nrf5340-dk-full.hex` firmware from the downloaded zip in this Programmer application (this firmware contains both application and networking core firmware).
5. Click “Erase & Write” and wait for device to boot up.

#### 4. Setting keys

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This starts a wizard which asks you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

The nRF5340 DK exposes multiple UARTs. If prompted, choose the bottom one:

```
? Which device do you want to connect to? (Use arrow keys)
  /dev/tty.usbmodem0009601707953 (SEGGER)
  /dev/tty.usbmodem0009601707951 (SEGGER)
❯ /dev/tty.usbmodem0009601707955 (SEGGER)
```

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### 5. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/8c32dc9-screenshot_2021-01-18_at_152509.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=97c0c43297eda1c857b2fcfef69f14be" width="1600" height="394" data-path=".assets/images/8c32dc9-screenshot_2021-01-18_at_152509.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Building a continuous motion recognition system](/tutorials/end-to-end/motion-recognition).
* [Recognizing sounds from audio](/tutorials/end-to-end/sound-recognition).
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

### Troubleshooting

#### Failed to flash

If your board fails to flash new firmware (a `FAIL.txt` file might appear on the `JLINK` drive) you can also flash using `nrfjprog`.

1. Install the [nRF Command Line Tools](https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Command-Line-Tools/Download).
2. Flash new firmware via:

```
nrfjprog --program path-to-your.bin -f NRF53 --sectoranduicrerase
```


Built with [Mintlify](https://mintlify.com).