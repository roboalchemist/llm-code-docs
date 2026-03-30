# Source: https://docs.edgeimpulse.com/hardware/deployments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deployments

The [deployment](/studio/projects/deployment) options in Edge Impulse combine all your configuration, signal processing blocks, learning blocks into a single package. You can include this package in your own application to run the impulse locally.

These tutorials show you how to run your impulse, but you'll need to hook in your sensor data yourself. We have a number of examples on how to do that in the [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) documentation, or you can use the full firmware for any of the fully supported [development boards](/hardware) as a starting point - they have everything (including sensor integration) already hooked up.

<Info>
  **Did you know?**

  You can build binaries for supported development boards straight from the studio. These will include your full impulse. See [Run Edge Impulse firmwares](/hardware/deployments/run-ei-fw).
</Info>

## C++ library

Impulses can be deployed as a C++ library. The library does not have any external dependencies and can be built with any C++11 compiler. We have end-to-end guides for:

* [Custom boards](/hardware/deployments/run-cpp)
* [Desktop](/hardware/deployments/run-cpp-desktop)
* [Android](/hardware/deployments/run-cpp-android)
* [Alif Ensemble Series devices](/hardware/deployments/run-cpp-alif-ensemble)
* [Espressif ESP-EYE (ESP32)](/hardware/deployments/run-cpp-espressif-esp32)
* [Himax WE-I Plus](/hardware/deployments/run-cpp-himax-we-i-plus)
* [Raspberry Pi RP2040](/hardware/deployments/run-cpp-rpi-rp2040)
* [SiLabs Thunderboard Sense 2](/hardware/deployments/run-cpp-silabs-thunderboard-sense-2)
* [Sony Spresense](/hardware/deployments/run-cpp-sony-spresense)
* [Syntiant TinyML Board](/hardware/deployments/run-cpp-syntiant-tinyml-board)
* [TI LaunchPad](/hardware/deployments/run-cpp-ti-launchxl)
* [Zephyr-based Nordic boards](/hardware/deployments/run-cpp-zephyr-nordic)

## Arduino

* [Arduino App Lab](/hardware/deployments/run-arduino-app-lab)
* [Arduino library (IDE 2.0)](/hardware/deployments/run-arduino-2-0)
* [Arduino library (IDE 1.18) | Deprecated ](/hardware/deployments/run-arduino-1-18)

## DRP-AI library

* [DRP-AI library Renesas RZ/V2L](/hardware/deployments/run-drpai-rzv2l)
* [DRP-AI TVM i8 library Renesas RZ/V2H](/hardware/deployments/run-drpai-rzv2h)

## WebAssembly library

* [Browser](/hardware/deployments/run-webassembly-browser)
* [Node.js](/hardware/deployments/run-webassembly-node)

## Additional packages

* [Arm KEIL MDK CMSIS-Pack](/hardware/deployments/run-arm-keil-cmsis)
* [Cube.MX CMSIS-Pack](/hardware/deployments/run-cubemx)
* [Docker container](/hardware/deployments/run-docker)
* [Edge Impulse firmwares](/hardware/deployments/run-ei-fw)
* [IAR library](/hardware/deployments/run-iar)
* [Linux EIM](/hardware/deployments/run-linux-eim)
* [Open-CMSIS-Pack](/hardware/deployments/run-open-cmsis-pack)
* [OpenMV library or firmware](/hardware/deployments/run-openmv)
* [Particle library](/hardware/deployments/run-particle)
* [Qualcomm IM SDK GStreamer pipeline](/hardware/deployments/run-qualcomm-im-sdk-gstreamer)
* [Zephyr module](/hardware/deployments/run-zephyr-module)


Built with [Mintlify](https://mintlify.com).