# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/inference/linux.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Linux SDKs

Edge Impulse for Linux is the easiest way to build machine learning solutions on real embedded hardware. The Linux SDKs contain tools that let you collect data from sensors, microphones, and cameras, and can run impulses with full hardware acceleration - with easy integration points to write your own applications.

## Inferencing libraries

To build your own applications, or collect data from new sensors, you can use the high-level language SDKs. These use full hardware acceleration, and let you integrate your Edge Impulse models in a few lines of code:

* [C++](/tools/libraries/sdks/inference/linux/cpp)
* [Go](/tools/libraries/sdks/inference/linux/go)
* [Node.js](/tools/libraries/sdks/inference/linux/node-js)
* [Python](/tools/libraries/sdks/inference/linux/python)
* [Rust](/tools/libraries/sdks/inference/linux/rust)

### .eim models

Edge Impulse Linux models are delivered in an `.eim` binary format. This is an executable that contains your signal processing and ML code, compiled with optimizations for your processor or GPU (e.g. NEON instructions on ARM cores) plus a very simple IPC layer (over a Unix socket). See our [Linux EIM executable guide](/hardware/deployments/run-linux-eim) to learn more.

## Supported hardware

### Development boards

This is a list of development boards that are fully supported by Edge Impulse for Linux. Follow the instructions to get started:

* [Advantech ICAM-540](/hardware/devices/advantech-icam-540)
* [IMDT RZ/V2H](/hardware/boards/imdt-rz-v2h)
* [Mac devices](/hardware/devices/macos)
* [Microchip SAMA7G54](/hardware/boards/microchip-sama7)
* [NVIDIA Jetson Orin and Nano](/hardware/boards/nvidia-jetson)
* [Linux x86\_64 devices](/hardware/devices/linux-x86_64)
* [Onlogic FR101](/hardware/devices/onlogic-fr101)
* [Qualcomm Dragonwing RB3 Gen 2 Dev Kit](/hardware/boards/qualcomm-rb3-gen-2-dev-kit)
* [Quectel PI-SG565D](/hardware/boards/quectel-pi-sg565d)
* [Raspberry Pi 4](/hardware/boards/raspberry-pi-4)
* [Renesas RZ/V2L](/hardware/boards/renesas-rz-v2l)
* [Renesas RZ/G2L](/hardware/boards/renesas-rz-g2l)
* [Renesas RZ/V2H](/hardware/boards/renesas-rz-v2h)
* [Texas Instruments SK-TDA4VM](/hardware/boards/ti-sk-tda4vm)
* [Texas Instruments SK-AM62A-LP](/hardware/boards/ti-sk-am62a-lp)
* [Texas Instruments SK-AM668A](/hardware/boards/ti-sk-am68a)

Different development board? Probably no problem! You can use the Linux x86\_64 getting started guide to set up the Edge Impulse for Linux CLI tool, and you can run your impulse on any x86\_64, ARMv7 or AARCH64 Linux target. For support please head to the [forums](https://forum.edgeimpulse.com).

### AI Accelerators

This is a list of AI accelerators that are fully supported by Edge Impulse of Linux. Follow the instructions to get started:

* [BrainChip AKD1000](/hardware/boards/brainchip-akd1000)
* [MemryX MX3](/hardware/boards/memryx-mx3)


Built with [Mintlify](https://mintlify.com).