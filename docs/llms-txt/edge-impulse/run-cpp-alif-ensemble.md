# Source: https://docs.edgeimpulse.com/hardware/deployments/run-cpp-alif-ensemble.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run C++ library on Alif Ensemble Series devices

Impulses can be deployed as a C++ library. This packages all your signal processing blocks, configuration and optimized learning blocks up into a single package. You can include this package in your own application to run the impulse locally. In this tutorial you'll export an impulse, and build an impulse into a custom application using either [ARM GCC](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/downloads) or [ARMCLANG](https://developer.arm.com/downloads/-/arm-compiler-for-embedded) for your Ensemble device.

<Info>
  **Knowledge required**

  This tutorial assumes that you're familiar with building applications using Alif development tools and drivers, as well as Makefile based projects. You will need `make` set up in your environment. If you're unfamiliar with these tools you can build binaries directly for your development board from the **Deployment** page in the studio.
</Info>

### Prerequisites

1. Make sure you followed the [getting started guide](/hardware/boards/alif-ensemble), and have a trained impulse from one of the listed tutorials.
2. Clone the [example-standalone-inferencing-alif](https://github.com/edgeimpulse/example-standalone-inferencing-alif) repository to your working directory.

### Deploying your impulse

Head over to your Edge Impulse project, and go to **Deployment**. From here you can create the full library which contains the impulse and all external required libraries. Select **Ethos u55 Library** and click **Build** to create the library. Then download and extract the `.zip` file.

To add the impulse to your firmware project, paste the `edge-impulse-sdk/`, `model-parameters` and `tflite-model` directories from the downloaded '.zip' file into the `source/` directory of the [example-standalone-inferencing-alif](https://github.com/edgeimpulse/example-standalone-inferencing-alif) repository. Make sure to overwrite any existing files in the `source/` directory.

<Frame caption="Edge Impulse libraries copied into standalone example directory">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/4b82853-screen_shot_2021-08-09_at_94104_am.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=005ccecc64e9331cc6ba9af792e9398e" width="1600" height="960" data-path=".assets/images/4b82853-screen_shot_2021-08-09_at_94104_am.png" />
</Frame>

This standalone example project contains minimal code required to run the imported impulse on the device. This code is located in `ei_main.cpp`. In this minimal code example, inference is run from a static buffer of input feature data. To verify that our embedded model achieves the exact same results as the model trained in Studio, we want to copy the same input features from Studio into the static buffer in `ei_main.cpp`.

To do this, first head back to the studio and click on the **Live classification** tab. Then load a validation sample, and click on a row under 'Detailed result'.

<Frame caption="Selecting the row with timestamp '320' under 'Detailed result'.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/5442de6-detailed-result.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=e8e583288e584ff20321d4d96eeaa05b" width="438" height="357" data-path=".assets/images/5442de6-detailed-result.png" />
</Frame>

To verify that the local application classifies the same result, we need the raw features for this timestamp. To do so click on the 'Copy to clipboard' button next to 'Raw features'. This will copy the raw input values from this validation file, before any signal processing or inferencing happened.

<Frame caption="Copying the raw features.">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/f2e53b5-wave.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=6f8d0ba48d5dd5894b887a600011753a" width="469" height="381" data-path=".assets/images/f2e53b5-wave.png" />
</Frame>

In `ei_main.cpp` paste the raw features inside the `static const float features[]` definition, for example:

```cpp  theme={"system"}
static const float features[] = {
    -19.8800, -0.6900, 8.2300, -17.6600, -1.1300, 5.9700, ...
};
```

The project will repeatedly run inference on this buffer of raw features once built. This will show that the inference result is identical to the **Live classification** tab in Studio. From this starting point, the example project is fully compatible with existing SimpleLink SDK plugins, drivers or custom firmware. Use new sensor data collected in real time on the device to fill a buffer. From there, follow the same code used in `ei_main.cpp` to run classification on live data.

### Building the project

There are three ways to build the project. The first uses the included Docker environment, pre-configured with the ARM GCC toolchain. The other options are to build the project locally with either GCC or ARMCLANG.

When building projects for the Ensemble kit, you have the option to deploy to the 'high efficiency' or 'high performance' cores. For all build options, the core is selected via the `-DTARGET_SUBSYSTEM` parameter when building. The commands below all default to the high performance core, but you can easily switch cores by swapping any `-DTARGET_SUBSYSTEM=HP` parameter to `-DTARGET_SUBSYSTEM=HE`

#### Building with Docker

If you are building with Docker, you will need to have [Docker Desktop](https://www.docker.com/products/docker-desktop) installed.

1. Run the Docker Desktop executable, or start the docker daemon from a terminal as shown below:

```
dockerd
```

2. From the [example-standalone-inferencing-alif](https://github.com/edgeimpulse/example-standalone-inferencing-alif) directory, build the Docker image:

```
$ docker build -t alif-build .
```

3. Build the application by copying the following command to build inside the container:

Windows

```
$ docker run --rm -it -v "%cd%":/app alif-build /bin/bash -c "mkdir -p build && cd build && cmake .. -DTARGET_SUBSYSTEM=HP -DCMAKE_TOOLCHAIN_FILE=../scripts/cmake/toolchains/bare-metal-gcc.cmake && make -j"
```

Linux, macOS

```
$ docker run --rm -it -v $PWD:/app:delegated alif-build /bin/bash -c "mkdir -p build && cd build && cmake .. -DTARGET_SUBSYSTEM=HP -DCMAKE_TOOLCHAIN_FILE=../scripts/cmake/toolchains/bare-metal-gcc.cmake && make -j"
```

The compiled `app.axf` will now be available in the `build/bin` directory.

1. If you see errors when building, read through the [Troubleshooting and optimization](/hardware/deployments/run-cpp-alif-ensemble#troubleshooting-and-optimization) section
2. Connect the board to your computer. Refer back to the [getting started guide](/hardware/boards/alif-ensemble) for how to do this.
3. [Flash the board](/hardware/deployments/run-cpp-alif-ensemble#flash-the-board)

#### Building with ARMCLANG

If you are developing your application in[ARM Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) or [Keil MDK5](https://www2.keil.com/mdk5), you may have an ARMCLANG license and wish to develop in that environment. To build this makefile project with ARMCLANG, first make sure you have followed [ARM instructions](https://developer.arm.com/documentation/dui0741/b/chr1374139991387) to enable and authenticate your compiler

With the ARMCLANG compiler set up, you can build the project via:

```
mkdir -p build
cd build
cmake .. -DTARGET_SUBSYSTEM=HP -DCMAKE_TOOLCHAIN_FILE=../scripts/cmake/toolchains/bare-metal-armclang.cmake
make -j8
```

The compiled `app.axf` will now be available in the `build/bin` directory, and you can [flash the board](/hardware/deployments/run-cpp-alif-ensemble#flash-the-board)

If you see errors when building, first check that your ARMCLANG compiler is properly set up and authenticated, and then read through the [Troubleshooting and optimization](/hardware/deployments/run-cpp-alif-ensemble#troubleshooting-and-optimization) section below.

#### Building with GCC

To build locally with GCC, first download the [ARM GNU toolchain](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/downloads), version 10.2 (2020 q4) or later. Follow the installation instructions and make sure this is the primary arm-gcc compiler in your path.

With the GCC set up, you can build the project via:

```
mkdir -p build
cd build
cmake .. -DTARGET_SUBSYSTEM=HP -DCMAKE_TOOLCHAIN_FILE=../scripts/cmake/toolchains/bare-metal-gcc.cmake
make -j8
```

If you see errors when building, first check that the ARM GCC compiler is correctly added to your path, and then read through the [Troubleshooting and optimization](/hardware/deployments/run-cpp-alif-ensemble#troubleshooting-and-optimization) section below.

The compiled `app.axf` will now be available in `build/bin`, and you can [flash the board](/hardware/deployments/run-cpp-alif-ensemble#flash-the-board)

### Flash the board

1. Grab the `app.axf` from the `build/bin` directory, and note whether you built the application for the high performance or high efficiency core
2. Connect your flash programmer to your debugger of choice, and configure it to select

* For [ARM Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) or [Keil MDK5](https://www2.keil.com/mdk5), see Alif instructions in [AUGD0002](https://alifsemi.com/download/AUGD0002).
* For [OZONE](https://www.segger.com/products/development-tools/ozone-j-link-debugger/), create a new project with the following device settings. Make sure to choose the correct core based on your build settings: <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/alif-ozone.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=0cac13b458abf0e1c49129639d1eaa70" alt="OZONE Ensemble Device" width="1424" height="654" data-path=".assets/images/alif-ozone.png" />

1. Flash and run `app.axf`

Alternatively, Alif provides a `Secure Enclave` to manage secure firmware storage and bootup in production environments. Alif provides documentation on converting .axf files for use with their secure enclave, and then programming the resulting binary regions to the secure enclave in [AUGD0002](https://alifsemi.com/download/AUGD0002).

### View the output

To see the output of the impulse over UART2, connect to the development board over a serial port on baud rate 115,200 and reset the board. You can do this with your favourite serial monitor or with the Edge Impulse CLI:

```
$ edge-impulse-run-impulse --raw
```

This will run the signal processing pipeline, and then classify the output:

```
Edge Impulse standalone inferencing (Alif Ensemble)
Running neural network...
Predictions (DSP: 485 μs., Classification: 746 μs., Anomaly: 0 μs.):
 . . .
```

### Troubleshooting and optimization

#### Timing

Timing calculations are performed in **ei\_classifier\_porting.cpp** and make use of an interrupt attached to SysTick.

* An RTOS may take over this interrupt handler, in which case you should re-implement `ei_read_timer_us` and `_ms`.
* The default calculation is based on the default clock rates of the Alif dev kit (400 MHz for HP core, 160 MHz for HE core). If you change this, redefine `EI_CORE_CLOCK_HZ`.

#### Memory placement

Alif M55 processors have a private fast DTCM, and also access to a larger, but slower, chip global SRAM.

* For `armclang` the linker file attempts to place as much as possible in DTCM, and overflows into SRAM if needed.
* For `gcc`, the linker is unable to auto place based on size. If you get an error during link, see [ensemble.ld](https://github.com/edgeimpulse/example-standalone-inferencing-alif/blob/firmware-dev-fomo/ensemble.ld) and un-comment the line that places the model in SRAM (instead of DTCM). This will only slow down DSP, as the U55 has to use the SRAM bus to access the model regardless of placement.

When your entire program can't fit into DTCM, sometimes customizing placement of objects can improve performance. See [ensemble.sct](https://github.com/edgeimpulse/example-standalone-inferencing-alif/blob/firmware-dev-fomo/ensemble.sct) for example placement commands.

#### Known issues

With debugger attached, my device boots up directly into Bus\_Fault (or possibly another fault). This can especially happen when you entered Hard Fault before your last reset.

* Power cycle your board and reload your program


Built with [Mintlify](https://mintlify.com).