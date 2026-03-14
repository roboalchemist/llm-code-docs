# Source: https://docs.edgeimpulse.com/hardware/boards/espressif-esp32.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Espressif ESP-EYE

Espressif ESP-EYE (ESP32) is a compact development board based on Espressif's ESP32 chip, equipped with a 2-Megapixel camera and a microphone. ESP-EYE also offers plenty of storage, with 8 MB PSRAM and 4 MB SPI flash - and it's fully supported by Edge Impulse. You'll be able to sample raw data, build models, and deploy trained machine learning models directly from the studio.

There are plenty of other boards built with ESP32 chip - and of course there are custom designs utilizing ESP32 SoM. Edge Impulse firmware was tested with ESP-EYE and ESP FireBeetle boards, but there is a possibility to modify the firmware to use it with other ESP32 designs. Read more on that in [Using with other boards](/hardware/boards/espressif-esp32#using-with-other-esp32-boards) section of this documentation.

The Edge Impulse firmware for this development board is open source and hosted on GitHub: [edgeimpulse/firmware-espressif-esp32](https://github.com/edgeimpulse/firmware-espressif-esp32).

<Frame caption="Espressif ESP-EYE">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/espressif-esp-eye.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=b471b411b3be2adbae35ddfb8a4b9e07" width="480" height="480" data-path=".assets/images/espressif-esp-eye.jpg" />
</Frame>

## **ESP-DSP Acceleration**

We’ve added [ESP-DSP](https://github.com/espressif/esp-dsp) acceleration to ESP32 deployments.
On supported devices, this significantly speeds up DSP feature extraction (e.g. MFCC for audio) without requiring any changes to your impulse configuration.

**Example: MFCC Keyword Spotting on a regular ESP32 (standard configuration)**

| Configuration   | DSP Time | Inference Time | Anomaly Time | Speed-up |
| --------------- | -------- | -------------- | ------------ | -------- |
| Without ESP-DSP | 297 ms   | 4 ms           | 0 ms         | —        |
| With ESP-DSP    | 54 ms    | 4 ms           | 0 ms         | \~5–6×   |

This results in much lower latency for audio and other DSP-heavy applications.
ESP-DSP is included automatically in Edge Impulse ESP32 builds — no extra setup required.

### Installing dependencies

To set this device up in Edge Impulse, you will need to install the following software:

1. [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
2. Python 3.
3. [ESP Tool](https://github.com/espressif/esptool).
   * The [ESP documentation website](https://docs.espressif.com/projects/esptool/en/latest/esp32/#quick-start) has instructions for macOS and Linux.
4. On Linux:
   * GNU Screen: install for example via `sudo apt install screen`.

<Warning>
  **Problems installing the CLI?**

  See the [Installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Warning>

### Connecting to Edge Impulse

With all the software in place it's time to connect the development board to Edge Impulse.

<iframe src="https://www.youtube.com/embed/xFzX1vdE-k8" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

#### 1. Connect the development board to your computer

Use a micro-USB cable to connect the development board to your computer.

#### 2. Update the firmware

The development board does not come with the right firmware yet. To update the firmware:

1. [Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/espressif-esp32.zip), and unzip the file.
2. Open the flash script for your operating system (`flash_windows.bat`, `flash_mac.command` or `flash_linux.sh`) to flash the firmware.
3. Wait until flashing is complete.

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
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/esp-connected.png?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=6f082a4b81773e621fe9459824767528" width="1518" height="350" data-path=".assets/images/esp-connected.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Building a continuous motion recognition system](/tutorials/end-to-end/motion-recognition).
* [Recognizing sounds from audio](/tutorials/end-to-end/sound-recognition).
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting).
* [Image classification](/tutorials/end-to-end/image-classification).
* [Object detection with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

#### Sensors available

The standard firmware supports the following sensors:

* Camera: OV2640, OV3660, OV5640 modules from Omnivision
* Microphone: I2S microphone on ESP-EYE (MIC8-4X3-1P0)
* LIS3DHTR module connected to I2C (SCL pin 22, SDA pin 21)
* Any analog sensor, connected to A0

The analog sensor and LIS3DHTR module were tested on ESP32 FireBeetle board and [Grove LIS3DHTR module](https://wiki.seeedstudio.com/Grove-3-Axis-Digital-Accelerometer-LIS3DHTR/).

<Frame caption="DFRobot FireBeetle ESP32">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/esp-firebeetle.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=39d6324172c38703554d760aedb589f8" width="1409" height="1000" data-path=".assets/images/esp-firebeetle.jpg" />
</Frame>

#### Using with other ESP32 boards

ESP32 is a very popular chip both in a community projects and in industry, due to its high performance, low price and large amount of documentation/support available. There are other camera enabled development boards based on ESP32, which can use Edge Impulse firmware after applying certain changes, e.g.

* AI-Thinker ESP-CAM
* M5STACK ESP32 PSRAM Timer Camera X (OV3660)
* M5STACK ESP32 Camera Module Development Board (OV2640)

The pins used for camera connection on different development boards are not the same, therefore you will need to change the #define [here](https://github.com/edgeimpulse/firmware-espressif-esp32/blob/main/edge-impulse/ingestion-sdk-platform/sensors/ei_camera.h#L29) to fit your development board, compile and flash the firmware. Specifically for AI-Thinker ESP-CAM, since this board needs an external USB to TTL Serial Cable to upload the code/communicate with the board, the data transfer baud rate must be changed to 115200 [here](https://github.com/edgeimpulse/firmware-espressif-esp32/blob/main/edge-impulse/ingestion-sdk-platform/espressif_esp32/ei_device_espressif_esp32.h#L35).

The analog sensor and LIS3DH accelerometer can be used on any other development board without changes, as long as the interface pins are not changed. If I2C/ADC pins that accelerometer/analog sensor are connected to are different, from described in Sensors available section, you will need to [change the values](https://github.com/AIWintermuteAI/LIS3DHTR_ESP-IDF/blob/641bda8c3e4b706a2365fe87dd4d925f96ea3f8c/src/include/LIS3DHTR.h#L31) in LIS3DHTR component for ESP32, compile and flash it to your board.

Additionally, since Edge Impulse firmware is open-source and available to public, if you have made modifications/added new sensors capabilities, we encourage you to make a PR in firmware repository!

### Deploying back to device

To deploy your impulse on your ESP32 board, please see:

* Generate an [Edge Impulse firmware](/hardware/deployments/run-ei-fw) (ESP32-EYE only)
* Download a [C++ library](/hardware/deployments/run-cpp-espressif-esp32) (using ESP-IDF)
* Download an [Arduino library](/hardware/deployments/run-arduino-2-0)


Built with [Mintlify](https://mintlify.com).