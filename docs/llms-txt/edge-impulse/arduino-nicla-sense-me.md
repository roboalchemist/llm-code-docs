# Source: https://docs.edgeimpulse.com/hardware/boards/arduino-nicla-sense-me.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Arduino Nicla Sense ME

The Nicla Sense ME is a tiny, low-power tool that sets a new standard for intelligent sensing solutions. With the simplicity of integration and scalability of the Arduino ecosystem, the board combines four state-of-the-art sensors from Bosch Sensortec:

* BHI260AP motion sensor system with integrated AI.
* BMM150 magnetometer.
* BMP390 pressure sensor.
* BME688 4-in-1 gas sensor with AI and integrated high-linearity, as well as high-accuracy pressure, humidity and temperature sensors.

Designed to easily analyze motion and the surrounding environment – hence the “M” and “E” in the name – it measures rotation, acceleration, pressure, humidity, temperature, air quality and CO2 levels by introducing completely new Bosch Sensortec sensors on the market.

Its tiny size and robust design make it suitable for projects that need to combine sensor fusion and AI capabilities on the edge, thanks to a strong computational power and low-consumption combination that can even lead to standalone applications when battery-operated.

The Arduino Nicla Sense ME is available on the [Arduino Store](https://store.arduino.cc/products/nicla-sense-me).

<Frame caption="Arduino Nicla Sense ME">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nicla.png?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=99e1ae1c3c0bbd5b6d8f11d6fe1ef9e4" width="1000" height="750" data-path=".assets/images/nicla.png" />
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

With all the software in place it's time to connect the development board to Edge Impulse.

<iframe src="https://www.youtube.com/embed/dj-2T8DVtSg" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

#### 1. Connect the development board to your computer

Use a micro-USB cable to connect the development board to your computer.

#### 2. Update the firmware

The development board does not come with the right firmware yet. To update the firmware:

1. [Download the latest Edge Impulse ingestion sketch](https://cdn.edgeimpulse.com/firmware/nicla_sense_ingestion.ino).
2. Open the `nicla_sense_ingestion.ino` sketch in a text editor or the Arduino IDE.
3. For data ingestion into your Edge Impulse project, at the top of the file, select 1 or multiple sensors by un-commenting the defines and select a desired sample frequency (in Hz). For example, for the Environmental sensors:

   ```c  theme={"system"}
   /**
    * @brief   Sample & upload data to Edge Impulse Studio.
    * @details Select 1 or multiple sensors by un-commenting the defines and select
    * a desired sample frequency. When this sketch runs, you can see raw sample
    * values outputted over the serial line. Now connect to the studio using the
    * `edge-impulse-data-forwarder` and start capturing data
    */
   // #define SAMPLE_ACCELEROMETER
   // #define SAMPLE_GYROSCOPE
   // #define SAMPLE_ORIENTATION
   #define SAMPLE_ENVIRONMENTAL
   // #define SAMPLE_ROTATION_VECTOR

   /**
    * Configure the sample frequency. This is the frequency used to send the data
    * to the studio regardless of the frequency used to sample the data from the
    * sensor. This differs per sensors, and can be modified in the API of the sensor
    */
   #define FREQUENCY_HZ        10
   ```
4. Then, from your sketch's directory, run the Arduino CLI to compile:

   ```bash  theme={"system"}
   arduino-cli compile --fqbn arduino:mbed_nicla:nicla_sense --output-dir . --verbose
   ```
5. Then flash to your Nicla Sense using the Arduino CLI:

   ```bash  theme={"system"}
   arduino-cli upload --fqbn arduino:mbed_nicla:nicla_sense --input-dir . --verbose
   ```
6. Wait until flashing is complete, and press the RESET button once to launch the new firmware.

#### 3. Data forwarder

From a command prompt or terminal, run:

```bash  theme={"system"}
edge-impulse-data-forwarder
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. You will also name your sensor's axes (depending on which sensor you selected in your compiled `nicla_sense_ingestion.ino` sketch). If you want to switch projects/sensors run the command with `--clean`. Please refer to the table below for the names used for each axis corresponding to the type of sensor:

| **Sensor**                       | **Axis names**                        |
| -------------------------------- | ------------------------------------- |
| `#define SAMPLE_ACCELEROMETER`   | accX, accY, accZ                      |
| `#define SAMPLE_GYROSCOPE`       | gyrX, gyrY, gyrZ                      |
| `#define SAMPLE_ORIENTATION`     | heading, pitch, roll                  |
| `#define SAMPLE_ENVIRONMENTAL`   | temperature, barometer, humidity, gas |
| `#define SAMPLE_ROTATION_VECTOR` | rotX, rotY, rotZ, rotW                |

**Note:** These *exact* axis names are required to run the Edge Impulse Arduino library deployment example applications for the Nicla Sense without any changes.

Else, when deploying the model, you will see an error like the following:

```
Starting inferencing in 2 seconds...
ERR: Nicla sensors don't match the sensors required in the model
Following sensors are required: accel.x + accel.y + accel.z + gyro.x + gyro.y + gyro.z + ori.heading + ori.pitch + ori.roll + rotation.x ...
```

If your axis names are different, when using the generated Arduino Library for the inference, you can modify the `eiSensors nicla_sensors[]` (near line 70) in the sketch example to add your custom names. e.g.:

```
eiSensors nicla_sensors[] =
{
“accel.x”, &get_accX,
“accel.y”, &get_accY,
“accel.z”, &get_accZ,
“gyro.x”, &get_gyrX,
“gyro.y”, &get_gyrY,
“gyro.z”, &get_gyrZ,
“ori.heading”, &get_oriHeading,
“ori.pitch”, &get_oriPitch,
“ori.roll”, &get_oriRoll,
“rotation.x”, &get_rotX,
“rotation.y”, &get_rotY,
“rotation.z”, &get_rotZ,
“rotation.w”, &get_rotW,
“temperature”, &get_temperature,
“barometer”, &get_barrometric_pressure,
“humidity”, &get_humidity,
“gas”, &get_gas,
};
```

#### 4. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Configuring the data forwarder for the Nicla Sense.">
  <img src="https://mintcdn.com/edgeimpulse/ZTVcrLfO8Bn7QR9I/.assets/images/nicla-sense-data-forwarder.png?fit=max&auto=format&n=ZTVcrLfO8Bn7QR9I&q=85&s=6ee3fdc855ec00900911c6a5f7aaa3d8" width="1600" height="509" data-path=".assets/images/nicla-sense-data-forwarder.png" />
</Frame>

<br />

<Frame caption="The Nicla Sense Data forwarder in the Devices tab.">
  <img src="https://mintcdn.com/edgeimpulse/ZTVcrLfO8Bn7QR9I/.assets/images/nicla-sense-devices.png?fit=max&auto=format&n=ZTVcrLfO8Bn7QR9I&q=85&s=e7b0097b5f7ea1f9aeada1465068ea26" width="1600" height="590" data-path=".assets/images/nicla-sense-devices.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with the [Edge Impulse continuous motion recognition tutorial](/tutorials/end-to-end/motion-recognition).

Looking to connect different sensors? Use the `nicla_sense_ingestion` sketch and the Edge Impulse [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) to easily send data from any sensor on the Nicla Sense into your Edge Impulse project.

### Deploying back to device

With the impulse designed, trained and verified you can deploy this model back to your Arduino Nicla Sense ME. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption. Edge Impulse can package the complete impulse - including the signal processing code, neural network weights, and classification code - up into a single library that you can run on your development board.

Use the [Run on Arduino](/hardware/deployments/run-arduino-2-0) tutorial and select one of the Nicla Sense examples.


Built with [Mintlify](https://mintlify.com).