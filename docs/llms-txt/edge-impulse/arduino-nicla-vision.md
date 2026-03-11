# Source: https://docs.edgeimpulse.com/hardware/boards/arduino-nicla-vision.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Arduino Nicla Vision

The Nicla Vision is a ready-to-use, standalone camera for analyzing and processing images on the Edge. Thanks to its 2MP color camera, smart 6-axis motion sensor, integrated microphone, and distance sensor, it is suitable for asset tracking, object recognition, and predictive maintenance. Some of its key features include:

* Powerful microcontroller equipped with a 2MP color camera
* Tiny form factor of 22.86 x 22.86 mm
* Integrated microphone, distance sensor, and intelligent 6-axis motion sensor
* Onboard Wi-Fi and Bluetooth® Low Energy connectivity
* Standalone when battery-powered
* Expand existing projects with sensing capabilities
* Enable fast Machine Vision prototyping
* Compatible with Nicla, Portenta, and MKR products

Its exceptional capabilities are supported by a powerful STMicroelectronics STM32H747AII6 Dual ARM® Cortex® processor, combining an M7 core up to 480 Mhz and an M4 core up to 240 Mhz. Despite its industrial strength, it keeps energy consumption low for battery-powered standalone applications.

The Arduino Nicla Vision is available for around 95 EUR from the [Arduino Store](https://store.arduino.cc/products/nicla-vision).

<Frame caption="Arduino Nicla Vision">
  <img src="https://mintcdn.com/edgeimpulse/ZTVcrLfO8Bn7QR9I/.assets/images/nicla-vision.jpg?fit=max&auto=format&n=ZTVcrLfO8Bn7QR9I&q=85&s=b376e3fa87034fc2209b8833464b3589" width="1389" height="750" data-path=".assets/images/nicla-vision.jpg" />
</Frame>

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

There are two ways to connect the Nicla Vision to Edge Impulse:

* Using the official Edge Impulse firmware - it supports all onboard sensors, including camera.
* Using an ingestion script. This supports analog, IMU, proximity sensors and microphone (limited to 8 kHz), but not the camera. It is only recommended if you want to modify the ingestion flow for third-party sensors.

<iframe src="https://www.youtube.com/embed/sWVJv-UDo-c" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

#### 1. Connect the development board to your computer

Use a micro-USB cable to connect the development board to your computer. Under normal circumstances, flash process should work without entering the bootloader manually. However if run into difficulties flashing the board, you can enter the bootloader by pressing RESET twice. The onboard LED should start pulsating to indicate this.

<Frame caption="Press RESET twice quickly to launch the bootloader on the Arduino Nicla Vision.">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nicla_bootloader.gif?s=f8793319b3d99ddc1df49da54e5f9db1" width="680" height="382" data-path=".assets/images/nicla_bootloader.gif" />
</Frame>

#### 2. Update the firmware

The development board does not come with the right firmware yet. To update the firmware:

1. [Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/arduino-nicla-vision.zip), and unzip the file.
2. Open the flash script for your operating system (`flash_windows.bat`, `flash_mac.command` or `flash_linux.sh`) to flash the firmware.
3. Wait until flashing is complete, and press the RESET button once to launch the new firmware.

#### 3. Setting keys

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This will start a wizard which will ask you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### Data ingestion

##### 1. Connect the development board to your computer

Use a micro-USB cable to connect the development board to your computer.

##### 2. Update the firmware

The development board does not come with the right firmware yet. To update the firmware:

1. [Download the latest Edge Impulse ingestion sketches](https://cdn.edgeimpulse.com/firmware/arduino-nicla-vision-ingestion.zip) and unzip the file.
2. Open the `nicla_vision_ingestion.ino` (for IMU/proximity sensor) or `nicla_vision_ingestion_mic.ino`(for microphone) sketch in a text editor or the Arduino IDE.
3. For IMU/proximity sensor data ingestion into your Edge Impulse project, at the top of the file, select 1 or multiple sensors by un-commenting the defines and select the desired sample frequency (in Hz). For example, for the accelerometer sensor:

```c  theme={"system"}
/**
 * @brief   Sample & upload data to Edge Impulse Studio.
 * @details Select 1 or multiple sensors by un-commenting the defines and select
 * a desired sample frequency. When this sketch runs, you can see raw sample
 * values outputted over the serial line. Now connect to the studio using the
 * `edge-impulse-data-forwarder` and start capturing data
 */
#define SAMPLE_ACCELEROMETER
//#define SAMPLE_GYROSCOPE
//#define SAMPLE_PROXIMITY

/**
 * Configure the sample frequency. This is the frequency used to send the data
 * to the studio regardless of the frequency used to sample the data from the
 * sensor. This differs per sensors, and can be modified in the API of the sensor
 */
#define FREQUENCY_HZ        10
```

For microphone data ingestion, you do not need to change the default parameters in the `nicla_vision_ingestion_mic.ino` sketch.

1. Then, from your sketch's directory, run the Arduino CLI to compile:

   ```bash  theme={"system"}
   arduino-cli compile --fqbn arduino:mbed_nicla:nicla_vision --output-dir .
   ```
2. Then flash to your Nicla Vision using the Arduino CLI:

   ```bash  theme={"system"}
   arduino-cli upload --fqbn arduino:mbed_nicla:nicla_vision
   ```

<Info>
  Alternatively if you open the sketch in the Arduino IDE, you can compile and upload the sketch from there.
</Info>

1. Wait until flashing is complete, and press the RESET button once to launch the new firmware.

##### 3a. Data forwarder (Fusion sensors)

From a command prompt or terminal, run:

```bash  theme={"system"}
edge-impulse-data-forwarder
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. You will also name your sensor's axes (depending on which sensor you selected in your compiled `nicla_vision_ingestion.ino` sketch). If you want to switch projects/sensors run the command with `--clean`. Please refer to the table below for the names used for each axis corresponding to the type of sensor:

| **Sensor**                     | **Axis names**   |
| ------------------------------ | ---------------- |
| `#define SAMPLE_ACCELEROMETER` | accX, accY, accZ |
| `#define SAMPLE_GYROSCOPE`     | gyrX, gyrY, gyrZ |
| `#define SAMPLE_PROXIMITY`     | cm               |

**Note:** These *exact* axis names are required for the Edge Impulse Arduino library deployment example applications for the Nicla Vision.

##### 3b. Data forwarder (Microphone)

From a command prompt or terminal, run:

```bash  theme={"system"}
edge-impulse-data-forwarder --baud 1000000 --frequency 8000
```

This will start a wizard which will ask you to log in and choose an Edge Impulse project. You will also name your sensor axes - in the case of the microphone, you need to enter `audio`. If you want to switch projects/sensors run the command with `--clean`.

##### 4. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Configuring the data forwarder for the Nicla Vision.">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nicla_vision_cli.png?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=f1cadecb6990bf9a4f4f6ff83ec645f3" width="1600" height="949" data-path=".assets/images/nicla_vision_cli.png" />
</Frame>

<br />

<Frame caption="The Nicla Vision Data forwarder in the Devices tab.">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nicla_vision_studio.png?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=534c53461aeb6ed2667cbf2adaa368fe" width="1600" height="551" data-path=".assets/images/nicla_vision_studio.png" />
</Frame>

<Info>
  The above screenshots are for Edge Impulse Ingestion scripts and Data forwarder. If you use the official Edge Impulse firmware for the Nicla Vision, the content will be slightly different.
</Info>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Building a continuous motion recognition system](/tutorials/end-to-end/motion-recognition).
* [Recognizing sounds from audio](/tutorials/end-to-end/sound-recognition).
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Image classification](/tutorials/end-to-end/image-classification)
* [Object detection with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids)

Looking to connect different sensors? Use the `nicla_vision_ingestion.ino` sketch and the [Edge Impulse data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) to easily send data from any sensor on the Nicla Vision into your Edge Impulse project.

### Deploying back to device

With the impulse designed, trained and verified you can deploy this model back to your Arduino Nicla Vision. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption. Edge Impulse can package the complete impulse - including the signal processing code, neural network weights, and classification code - up into a single library that you can run on your development board.

Use the [Run on Arduino](/hardware/deployments/run-arduino-2-0) tutorial and select one of the Nicla Vision examples.


Built with [Mintlify](https://mintlify.com).