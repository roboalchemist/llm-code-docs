# Source: https://docs.edgeimpulse.com/hardware/deployments/run-cpp-rpi-rp2040.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run C++ library on Raspberry Pi Pico (RP2040)

Impulses can be deployed as a C++ library. This packages all your signal processing blocks, configuration and learning blocks up into a single package. You can include this package in your own application to run the impulse locally. In this tutorial you'll export an impulse, and build an application for Raspberry Pi Pico (RP2040) development board to classify sensor data.

<Info>
  **Knowledge required**

  This tutorial assumes that you're familiar with building applications with C/C++ Pico-SDK for Raspberry Pi Pico (RP2040). If you're unfamiliar with either of these you build binaries directly for your development board from the Deployment page in the studio.
</Info>

**Note:** Are you looking for an example that has all sensors included? The Edge Impulse firmware for Raspberry Pi Pico (RP2040) has that. See [edgeimpulse/firmware-pi-rp2040](https://github.com/edgeimpulse/firmware-pi-rp2040).

### Prerequisites

Make sure you've followed one of the tutorials and have a trained impulse. For the purpose of this tutorial, we’ll assume you trained a [Continuous motion recognition](/tutorials/end-to-end/motion-recognition) model. Also install the following software:

* [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).

The below instructions assume you are using Debian-based Linux distribution. Alternative instructions for those using Microsoft Windows or Apple macOS are provided in the [Getting started with Pico guide](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf) (Sections 9.1 and 9.2).

To build the project, you will need the pico-sdk, CMake, a cross-platform tool used to build the software, and the GNU Embedded Toolchain for Arm. In Debian-based OS, you can install both these via apt from the command line.

```bash  theme={"system"}
sudo apt update
sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential
```

**Note:** Ubuntu and Debian users might additionally need to also install `libstdc++-arm-none-eabi-newlib`.

You'll need the PICO SDK to compile the firmware. You can obtain it from [https://github.com/raspberrypi/pico-sdk](https://github.com/raspberrypi/pico-sdk) and then specify PICO\_SDK\_PATH environmental variable, that would point to exact PICO SDK location on your system. E.g.

```bash  theme={"system"}
cd ~/
git clone --recurse-submodules https://github.com/raspberrypi/pico-sdk
export PICO_SDK_PATH="~/pico-sdk"
```

### Cloning the base repository

We created an example repository which contains a small application for Raspberry Pi Pico (RP2040), which takes the raw features as an argument, and prints out the final classification. Download the application as a .zip, or import this repository using Git:

```
git clone https://github.com/edgeimpulse/example-standalone-inferencing-pico
```

### Deploying your impulse

Head over to your Edge Impulse project, and go to the Deployment tab. From here you can create the full library which contains the impulse and all required libraries. Select C++ library and click Build to create the library.

Download the .zip file and extract the directories in the [example-standalone-inferencing-pico](https://github.com/edgeimpulse/example-standalone-inferencing-pico) folder. Your final folder structure should look like this:

```
example-standalone-inferencing-pico/
├── CMakeLists.txt
├── edge-impulse-sdk
├── LICENSE
├── model-parameters
├── pico_sdk_import.cmake
├── README.md
├── source
└── tflite-model
```

### Running the impulse

With the project ready, it's time to verify that the application works. Head back to the studio and click on Live classification. Then load a validation sample, and click on a row under 'Detailed result'.

<Frame caption="Selecting the row with timestamp '320' under 'Detailed result'.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/5442de6-detailed-result.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=e8e583288e584ff20321d4d96eeaa05b" width="438" height="357" data-path=".assets/images/5442de6-detailed-result.png" />
</Frame>

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

Build the application by calling `make` in the build directory of the project:

```bash  theme={"system"}
mkdir build && cd build
cmake ..
make -j4
```

The fastest method to load firmware onto a RP2040-based board for the first time is by mounting it as a USB Mass Storage Device. Doing this allows you to drag a file onto the board to program the flash. Connect the Raspberry Pi Pico to your computer using a micro-USB cable, making sure that you hold down the **BOOTSEL** button as you do so, to force it into USB Mass Storage Mode. Drag the `ei_rp2040_firmware.uf2` file from the build folder to the newly appeared USB Mass Storage device.

### Seeing the output

To see the output of the impulse, connect to the development board over a serial port on baud rate `115200` and reset the board. You can do this with your favorite serial monitor or with the Edge Impulse CLI:

```
$ edge-impulse-run-impulse --raw
```

This will run the signal processing pipeline, and then classify the output, for example:

```
Edge Impulse standalone inferencing (Raspberry Pi Pico)
Running neural network...
Predictions (time: 8 ms.):
idle:   0.015319
snake:  0.000444
updown: 0.006182
wave:   0.978056
Anomaly score (time: 0 ms.): 0.133557
run_classifier_returned: 0
[0.01532, 0.00044, 0.00618, 0.97806, 0.134]
```

Which matches the values we just saw in the studio. You now have your impulse running on your Raspberry Pi Pico development board


Built with [Mintlify](https://mintlify.com).