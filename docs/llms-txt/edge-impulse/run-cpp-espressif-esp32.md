# Source: https://docs.edgeimpulse.com/hardware/deployments/run-cpp-espressif-esp32.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run C++ library on Espressif ESP-EYE (ESP32)

Impulses can be deployed as a C++ library. This packages all your signal processing blocks, configuration and learning blocks up into a single package. You can include this package in your own application to run the impulse locally. In this tutorial you'll export an impulse, and build an application for Espressif ESP-EYE (ESP32) development board to classify sensor data using ESP IDF development framework.

<Info>
  **Knowledge required**

  This tutorial assumes that you're familiar with building applications with ESP IDF development framework for ESP-EYE (ESP32). If you're unfamiliar ESP-IDF, you can download a [ready-to-flash binary](/hardware/deployments/run-ei-fw) compatible with the ESP32-EYE or download the generated [Arduino library](/hardware/deployments/run-arduino-2-0) directly from the Deployment page in the studio.
</Info>

**Note:** Are you looking for an example that has sensors included? The Edge Impulse firmware for Espressif ESP-EYE (ESP32) has that. See [edgeimpulse/espressif-esp32](https://github.com/edgeimpulse/firmware-espressif-esp32)

### Prerequisites

Make sure you've followed one of the tutorials and have a trained impulse. For the purpose of this tutorial, we’ll assume you trained an [Continuous motion recognition](/tutorials/end-to-end/motion-recognition) model. Also install the following software:

* [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
* [Espressif ESP IDF](https://docs.espressif.com/projects/esp-idf/en/v4.4/esp32/get-started/index.html#installation-step-by-step)

### Cloning the base repository

We created an example repository which contains a small application for Espressif ESP32, which takes the raw features as an argument, and prints out the final classification. Download the application as a .zip, or import this repository using Git:

```
git clone https://github.com/edgeimpulse/example-standalone-inferencing-espressif-esp32
```

### Deploying your impulse

Head over to your Edge Impulse project, and go to the Deployment tab. From here you can create the full library which contains the impulse and all required libraries. Select C++ library and click Build to create the library.

Download the .zip file and unzip the deployed C++ library from your Edge Impulse project and copy only the folders to the root directory of this repository [example-standalone-inferencing-espressif-esp32](https://github.com/edgeimpulse/example-standalone-inferencing-espressif-esp32) folder. Your final folder structure should look like this:

```
example-standalone-inferencing-espressif-esp32/
├── CMakeLists.txt
├── LICENSE
├── README.md
├── build
├── edge-impulse-sdk
├── main
├── model-parameters
├── partitions.csv
├── sdkconfig
└── tflite-model
```

### Running the impulse

With the project ready, it's time to verify that the application works. Head back to the studio and click on Live classification. Then load a validation sample, and click on a row under 'Detailed result'.

<Frame caption="Selecting the row with timestamp '320' under 'Detailed result'.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/5442de6-detailed-result.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=e8e583288e584ff20321d4d96eeaa05b" width="438" height="357" data-path=".assets/images/5442de6-detailed-result.png" />
</Frame>

<Info>
  In your case, since you might pick a different sample, the values and classification results might be different from the screenshot above. The important thing is that classification result in Studio matches the one from the device - which we will be checking a bit later.
</Info>

To verify that the local application classifies the same, we need the raw features for this timestamp. To do so click on the Copy to clipboard button next to 'Raw features'. This will copy the raw values from this validation file, before any signal processing or inferencing happens.

<Frame caption="Copying the raw features.">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/f2e53b5-wave.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=6f8d0ba48d5dd5894b887a600011753a" width="469" height="381" data-path=".assets/images/f2e53b5-wave.png" />
</Frame>

Open `ei_main.cpp` and paste the raw features inside the `static const float features[]` definition, for example:

```
static const float features[] = {
    -19.8800, -0.6900, 8.2300, -17.6600, -1.1300, 5.9700, ...
};
```

Build the application with ESP IDF in the project directory:

```bash  theme={"system"}
get_idf
clear && idf.py build
```

To flash the project, in the project directory execute:

```bash  theme={"system"}
idf.py flash
```

### Seeing the output

To see the output of the impulse, connect to the development board over a serial port on baud rate `115200` and reset the board. You can do this with your favorite serial monitor or with the Edge Impulse CLI:

```
$ edge-impulse-run-impulse --raw
```

This will run the signal processing pipeline, and then classify the output, for example:

```
Predictions (DSP: 20 ms., Classification: 1 ms., Anomaly: 0 ms.):
[0.00000, 0.00000, 0.99609, 0.00000, -0.729]
```

Which matches the values you just saw in the studio. You now have your impulse running on your Espressif ESP32 development board.


Built with [Mintlify](https://mintlify.com).