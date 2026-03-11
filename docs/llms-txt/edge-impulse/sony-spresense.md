# Source: https://docs.edgeimpulse.com/hardware/boards/sony-spresense.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sony Spresense

[Sony's Spresense](https://developer.sony.com/develop/spresense/) is a small, but powerful development board with a 6 core Cortex-M4F microcontroller and integrated GPS, and a wide variety of add-on modules including an extension board with headphone jack, SD card slot and microphone pins, a camera board, a sensor board with accelerometer, pressure, and geomagnetism sensors, and Wi-Fi board - and it's fully supported by Edge Impulse. You'll be able to sample raw data, build models, and deploy trained machine learning models directly from the studio.

To get started with the Sony Spresense and Edge Impulse you'll need:

* The Spresense Main Development board.
* The Spresense Extension Board - to connect external sensors.
* A micro-SD card to store samples - this is a necessary add-on as the board will not be able to operate without storing samples.

In addition, you'll want some sensors, these ones are fully supported (note that you can collect data from any sensor on the Spresense with the [data forwarder](/tools/clis/edge-impulse-cli/data-forwarder)):

* For image models: the [Spresense CXD5602PWBCAM1 camera add-on](https://mou.sr/3Y66Ruo) or the [Spresense CXD5602PWBCAM2W HDR camera add-on](https://mou.sr/3Dt9Q6J).
* For accelerometer models: the [Spresense Sensor EVK-70 add-on](https://www.chip1stop.com/USA/en/view/dispDetail/DispDetail?partId=ROHM-0170579\&cid=c1s_sony_spresense_SPRESENSE-SENSOR-EVK-701).
* For audio models: an electret microphone and a 2.2K Ohm resistor, wired to the extension board's audio channel A.s) \[Here is an example picture]]\([https://cdn.edgeimpulse.com/images/spresense-audio.jpg](https://cdn.edgeimpulse.com/images/spresense-audio.jpg))).
  * **Note:** for audio models you must also have a FAT formatted SD card for the extension board, with the Spresense's DSP files included in a `BIN` folder on the card. [Here is a screenshot of the SD card directory](https://cdn.edgeimpulse.com/images/spresense-audio-sd-card.png).
* For other sensor models: see below for SensiEDGE [CommonSense](/hardware/boards/sony-spresense#sensor-fusion-with-sony-spresense-and-sensiedge-commonsense) support.

The Edge Impulse firmware for this development board is open source and hosted on GitHub: [edgeimpulse/firmware-sony-spresense](https://github.com/edgeimpulse/firmware-sony-spresense).

<Frame caption="The Spresense product family.">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/sony/spresense_product.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=abf84a13af696c26022b6fed4686dce1" width="983" height="638" data-path=".assets/images/sony/spresense_product.png" />
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

<iframe src="https://www.youtube.com/embed/OI9AymVUU_4" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

#### 1. Connect the optional camera, sensor, extension board, Wi-Fi add-ons, and SD card

<Frame caption="Spresense main board with attached camera, sensor add-on, Wi-Fi add-on, and extension board.">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/sony/sony-orientation.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=318e7a6f506c25419f64b69c06dfde3e" width="961" height="1000" data-path=".assets/images/sony/sony-orientation.png" />
</Frame>

An SD card is necessary to use the Spresense. Make sure it is formatted in FAT format before inserting it into the Spresense.

#### 2. Connect the development board to your computer

Use a micro-USB cable to connect the main development board (not the extension board) to your computer.

#### 3. Update the bootloader and the firmware

The development board does not come with the right firmware yet. To update the firmware:

1. Install [Python 3.7 or higher](https://www.python.org/downloads/).
2. [Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/sony-spresense.zip), and unzip the file.
3. Open the flash script for your operating system (`flash_windows.bat`, `flash_mac.command` or `flash_linux.sh`) to flash the firmware.
4. Wait until flashing is complete. The on-board LEDs should stop blinking to indicate that the new firmware is running.

#### 4. Setting keys

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

<Info>
  **Mac: Device choice**

  If you have a choice of serial ports and are not sure which one to use, pick /dev/tty.SLAB\_USBtoUART or /dev/cu.usbserial-\*
</Info>

This will start a wizard which will ask you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### 5. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/sony/spresense-in-devices.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=bba29571baf2cc68ac66d859efd9d28d" width="1233" height="291" data-path=".assets/images/sony/spresense-in-devices.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Sound recognition](/tutorials/end-to-end/sound-recognition)
* [Image classification](/tutorials/end-to-end/image-classification)
* [object detection](/tutorials/end-to-end/object-detection-bounding-boxes).
* [Object detection with centroids (FOMO)](/tutorials/topics/post-processing/count-objects-fomo)

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

### Troubleshooting

#### Error when flashing

If you see:

```
ValueError: dlsym(RTLD_DEFAULT, kIOMasterPortDefault): symbol not found
```

Upgrade pyserial:

```
pip3 install --upgrade pyserial
```

#### Daemon does not start

If the `edge-impulse-daemon` or `edge-impulse-run-impulse` commands do not start it might be because of an error interacting with the SD card or because your board has an old version of the bootloader. To see the debug logs, run:

```
edge-impulse-run-impulse --raw
```

And press the RESET button on the board. If you see `Welcome to nash` you'll need to update the bootloader. To do so:

1. Install and launch the Arduino IDE.
2. Go to **Preferences** and under 'Additional Boards Manager URLs' add `https://github.com/sonydevworld/spresense-arduino-compatible/releases/download/generic/package_spresense_index.json` (if there's already text in this text box, add a `,` before adding the new URL).
3. Then go to **Tools > Boards > Board manager**, search for 'Spresense' and click *Install*.
4. Select the right board via: **Tools > Boards > Spresense boards > Spresense**.
5. Select your serial port via: **Tools > Port** and selecting the serial port for the Spresense board.
6. Select the Spresense programmer via: **Tools > Programmer > Spresense firmware updater**.
7. Update the bootloader via **Tools > Burn bootloader**.

Then update the firmware again (from [step 3: Update the bootloader and the firmware](/hardware/boards/sony-spresense#3-update-the-bootloader-and-the-firmware)).

### Sensor Fusion with Sony Spresense and SensiEDGE CommonSense

Edge Impulse has partnered with [SensiEdge](https://www.sensiedge.com/commonsense) to add support for sensor fusion applications to the Sony Spresense by integrating the SensiEDGE CommonSense sensor extension board. The CommonSense comes with a wide array of sensor functionalities that connect seamlessly to the Spresense and the Edge Impulse studio. In addition to the Sony Spresense, the Spresense extension board and a micro-SD card, you will need the CommonSense board which is available to purchase on Mouser.

<Frame caption="SensiEDGE CommonSense sensor board.">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/sony/commonsense.jpg?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=9dfe366697a58827a120343646ecb8ca" width="1001" height="1000" data-path=".assets/images/sony/commonsense.jpg" />
</Frame>

#### Getting started with CommonSense

Connect the Sony Spresense extension board to the Sony Spresense ensuring that the micro-SD card is loaded. Connect the SensiEDGE CommonSense in the orientation shown below - with the connection ports facing the same direction. The HD camera is optional but can be attached if you want to create an image based application.

<Frame caption="Connect the CommonSense to Sony Spresense.">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/sony/commonsense-orientation.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=211e18cb2886638964efdd8999970346" width="1333" height="1000" data-path=".assets/images/sony/commonsense-orientation.png" />
</Frame>

Once the boards are connected, start the [Edge Impulse daemon](/tools/clis/edge-impulse-cli/serial-daemon) from a command prompt or terminal:

```
edge-impulse-daemon
```

This starts a wizard which asks you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

If prompted to select a device, choose `commonsense`:

```
? Which device do you want to connect to?
❯ /dev/tty.usbmodem** (commonsense)
```

Verify that the device is connected by going to the **Devices** tab in your project and checking for the green light as mentioned in the steps above.

Once your device is connected, you are now ready to collect data directly from your CommonSense board and start creating your machine learning application.

If you want to reset the firmware to the default Sony-CommonSense firmware, you can download it [here](https://cdn.edgeimpulse.com/firmware/sony-spresense-commonsense.zip), flash your Sony Spresense and be ready to start again.


Built with [Mintlify](https://mintlify.com).