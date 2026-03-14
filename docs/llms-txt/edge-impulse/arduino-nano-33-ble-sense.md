# Source: https://docs.edgeimpulse.com/hardware/boards/arduino-nano-33-ble-sense.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Arduino Nano 33 BLE Sense

The Arduino Nano 33 BLE Sense is a tiny development board with a Cortex-M4 microcontroller, motion sensors, a microphone and BLE - and it's fully supported by Edge Impulse. You'll be able to sample raw data, build models, and deploy trained machine learning models directly from the studio.

<Frame caption="Arduino Nano 33 BLE Sense">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/38d12a5-abx00031_front_3.jpg?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=a82c5fdb68b9c5dedaeb417fbc122afc" width="500" height="375" data-path=".assets/images/38d12a5-abx00031_front_3.jpg" />
</Frame>

You can also use the [Arduino Tiny Machine Learning Kit](https://store-usa.arduino.cc/products/arduino-tiny-machine-learning-kit?selectedStore=us) to run image classification models on the edge with the Arduino Nano and attached OV7675 camera module (or [connect the hardware together via jumper wire and a breadboard](/hardware/boards/arduino-nano-33-ble-sense#connecting-an-off-the-shelf-ov7675-camera-module) if purchased separately).

<Frame caption="Arduino Tiny ML kit">
  <img src="https://mintcdn.com/edgeimpulse/1qRLsCRqNaLvAcJP/.assets/images/arduino-nano-33-ble-sense-tinyml-kit.jpg?fit=max&auto=format&n=1qRLsCRqNaLvAcJP&q=85&s=30378467a738b494e7729fbb1b747fae" width="500" height="375" data-path=".assets/images/arduino-nano-33-ble-sense-tinyml-kit.jpg" />
</Frame>

<Info>
  **Different Arduino Nano 33 BLE Sense Versions**

  Arduino has two different versions (known as "revisions") of the Arduino Nano 33 BLE Sense. Both use the nRF52840 as the processor, but the sensors are different. While the Edge Impulse firmware works with both versions, you need to be careful about choosing the correct version when working with the Arduino IDE.
</Info>

You can tell which version of the Arduino Nano 33 BLE Sense you have by looking at the underside of the board. The first version will simply have *NANO 33 BLE SENSE* written in the silkscreen. The second version will have *NANO 33 BLE SENSE REV2*.

<Frame caption="Arduino Nano 33 BLE Sense Rev2">
  <img src="https://mintcdn.com/edgeimpulse/zDLKVpMVk0R3iPVV/.assets/images/arduino-nano-33-ble-sense-rev2-back.jpg?fit=max&auto=format&n=zDLKVpMVk0R3iPVV&q=85&s=ee4bb6e70ca6642e5c5fb964f9c9cbe1" width="500" height="375" data-path=".assets/images/arduino-nano-33-ble-sense-rev2-back.jpg" />
</Frame>

The Edge Impulse firmware for this development board is open source and hosted on GitHub: [edgeimpulse/firmware-arduino-nano-33-ble-sense](https://github.com/edgeimpulse/firmware-arduino-nano-33-ble-sense).

### Installing dependencies

To set this device up in Edge Impulse, you will need to install the following software:

1. [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
2. [Arduino CLI](https://arduino.github.io/arduino-cli/latest/).
   * Here's an [instruction video for Windows](https://youtu.be/1jMWsFER-Bc).
   * The [Arduino website](https://arduino.github.io/arduino-cli/installation/) has instructions for macOS and Linux.
3. On Linux:
   * GNU Screen: install for example via `sudo apt install screen`.

<Warning>
  **Problems installing the CLI?**

  See the [Installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Warning>

### Connecting to Edge Impulse

With all the software in place it's time to connect the development board to Edge Impulse.

<iframe src="https://www.youtube.com/embed/wOkMZUaPLUM" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

#### 1. Connect the development board to your computer

Use a micro-USB cable to connect the development board to your computer. Then press RESET twice to launch into the bootloader. The on-board LED should start pulsating to indicate this.

<Frame caption="Press RESET twice quickly to launch the bootloader on the Arduino Nano 33 BLE Sense.">
  <img src="https://mintcdn.com/edgeimpulse/M1w1EVa0Cr_xPADa/.assets/images/b302301-out.gif?s=0465d129d6880ecffe218924621f6668" width="320" height="200" data-path=".assets/images/b302301-out.gif" />
</Frame>

#### 2. Update the firmware

The development board does not come with the right firmware yet. To update the firmware:

1. [Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/arduino-nano-33-ble-sense.zip), and unzip the file.
2. Open the flash script for your operating system (`flash_windows.bat`, `flash_mac.command` or `flash_linux.sh`) to flash the firmware.
3. Wait until flashing is complete, and press the RESET button once to launch the new firmware.

#### 3. Setting keys

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### 4. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/M1w1EVa0Cr_xPADa/.assets/images/b5b9f02-arduino03.png?fit=max&auto=format&n=M1w1EVa0Cr_xPADa&q=85&s=ddc714fdbebe4e25c65c504ab43ad22e" width="1103" height="294" data-path=".assets/images/b5b9f02-arduino03.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Sound recognition](/tutorials/end-to-end/sound-recognition)
* [Image classification](/tutorials/end-to-end/image-classification)
* [Object detection](/tutorials/end-to-end/object-detection-bounding-boxes)
* [Object detection with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids)

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

### Deploying back to device

One option to deploy your model is to use the **Arduino library** option on the [Deployment page](/studio/projects/deployment) in your Edge Impulse Studio project. This will combine your model with your chosen processing block and automatically download an Arduino in a .zip file. In the Arduino IDE, select **Sketch > Include Library > Add .ZIP Library...** and select your downloaded .zip file.

Once the library finishes installing, you can select **File > Examples > {name_of_your_project}\_inferencing** to see a list of available Arduino examples for the various supported boards. Notice that you have both Nano 33 Sense and Nano 33 Sense Rev2 options available.

The examples for *camera*, *microphone*, and *microphone\_fusion* under *nano\_ble33\_sense* will work for both boards. You must choose the correct board revision (*nano\_ble33\_sense* or *nano\_ble33\_sense\_rev2*) for the *accelerometer*, *accelerometer\_continuous*, or *fusion* examples, as the accelerometer and environmental sensors are different between the board revisions.

<Frame caption="Edge Impulse inferencing examples in the Arduino IDE">
  <img src="https://mintcdn.com/edgeimpulse/zDLKVpMVk0R3iPVV/.assets/images/arduino-nano-33-ble-sense-examples.jpg?fit=max&auto=format&n=zDLKVpMVk0R3iPVV&q=85&s=bfcd0653b4b531818c6fcd29687200d9" width="1046" height="275" data-path=".assets/images/arduino-nano-33-ble-sense-examples.jpg" />
</Frame>

These examples should give you a good starting place for developing your own edge ML applications on the Arduino. For example, if you train a keyword spotting model to identify the words "yes" and "no," you would deploy the model as an *Arduino library* and upload the *nano\_ble3\_sense\_microphone\_continuous* example to your Nano 33 BLE. Once uploaded, open the Serial Monitor to see the inference results printed out.

<Frame caption="Inference results in Arduino IDE from Edge Impulse model">
  <img src="https://mintcdn.com/edgeimpulse/zDLKVpMVk0R3iPVV/.assets/images/arduino-nano-33-ble-sense-inference-results.png?fit=max&auto=format&n=zDLKVpMVk0R3iPVV&q=85&s=d14faf0009a92e495e93b8fb79076ff2" width="1364" height="1000" data-path=".assets/images/arduino-nano-33-ble-sense-inference-results.png" />
</Frame>

### Troubleshooting

#### Bad CPU type in executable (Macbook M1)

It probably means you don't have Rosetta 2 installed yet (which allows Intel-based apps to run on M1 chips).

The error looks like the following:

```
Flashing board...
Failed uploading: cannot execute upload tool: fork/exec /Users/brianmcfadden/Library/Arduino15/packages/arduino/tools/bossac/1.9.1-arduino2/bossac: bad CPU type in executable

Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.

[Process completed]
```

To install Rosetta 2 you can run this command:

```
softwareupdate --install-rosetta --agree-to-license
```

#### Connecting an off-the-shelf OV7675 camera module

You will need the following hardware:

* Arduino Nano 33 BLE Sense board with headers.
* OV7675 camera module.
* Micro-USB cable.
* Solderless breadboard and female-to-male jumper wires.

First, slot the Arduino Nano 33 BLE Sense board into a solderless breadboard:

<Frame caption="Arduino Nano 33 BLE Sense board with headers inserted into a solderless breadboard.">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/e93bd4f-screen_shot_2021-08-19_at_122750_pm.png?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=c07104b04758a51777133cd55c2964d9" width="1600" height="457" data-path=".assets/images/e93bd4f-screen_shot_2021-08-19_at_122750_pm.png" />
</Frame>

With female-to-male jumper wire, use the following wiring diagram, pinout diagrams, and connection table to link the OV7675 camera module to the microcontroller board via the solderless breadboard:

<Frame caption="OV7675 camera module with female headers connected.">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/d3843ce-screen_shot_2021-08-19_at_122845_pm.png?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=22711f4d0540110553345a26799c26ba" width="1066" height="610" data-path=".assets/images/d3843ce-screen_shot_2021-08-19_at_122845_pm.png" />
</Frame>

<br />

<Frame caption="Wiring diagram showing the OV7675 connections to Arduino Nano 33 BLE Sense.">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/02308f0-screen_shot_2021-08-19_at_122939_pm.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=981697ab7c2f57b5f36b74de2af7da25" width="1034" height="1000" data-path=".assets/images/02308f0-screen_shot_2021-08-19_at_122939_pm.png" />
</Frame>

Download the full pinout diagram of the Arduino Nano 33 BLE Sense [here](https://content.arduino.cc/assets/Pinout-NANOsense_latest.pdf).

<Frame caption="Table with connections between the OV7675 camera module pins and the Arduino Nano 33 BLE Sense.">
  <img src="https://mintcdn.com/edgeimpulse/cU2n98Ml68g1eiRr/.assets/images/bbc75e7-screen_shot_2021-08-19_at_122951_pm.png?fit=max&auto=format&n=cU2n98Ml68g1eiRr&q=85&s=675f0070a2ca5ee9c41ff45054fe0cd1" width="1001" height="1000" data-path=".assets/images/bbc75e7-screen_shot_2021-08-19_at_122951_pm.png" />
</Frame>

Finally, use a micro-USB cable to connect the Arduino Nano 33 BLE Sense development board to your computer.

<Frame caption="Showing all connections between the OV7675 camera module and the Arduino Nano 33 BLE Sense.">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/72fa20d-screen_shot_2021-08-19_at_123103_pm.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=66ef4656186b865a76c1caeaa4d080b6" width="1292" height="736" data-path=".assets/images/72fa20d-screen_shot_2021-08-19_at_123103_pm.png" />
</Frame>

Now build & train your own [image classification model](/tutorials/end-to-end/image-classification) and deploy to the Arduino Nano 33 BLE Sense with Edge Impulse!


Built with [Mintlify](https://mintlify.com).