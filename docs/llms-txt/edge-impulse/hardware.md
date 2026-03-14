# Source: https://docs.edgeimpulse.com/hardware.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Hardware

**We support any edge AI hardware that can run C++, and more!**

You will find on this page a list of edge AI hardware targets that are either maintained by Edge Impulse or by our partners. During the integration and when possible, we leverage and integrate the hardware capabilities (optimized floating point units (FPU), DSP and Neural Network accelerations, GPU or other AI accelerators).

<Columns cols={4}>
  <Card title="Devices" img="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/fa-icon-16x9-tablet-screen-button-solid-full.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=ec2438452b489f37a62acee3dc289aeb" href="/hardware/devices/advantech-icam-540" width="1600" height="900" data-path=".assets/images/fa-icon-16x9-tablet-screen-button-solid-full.png" />

  <Card title="Boards" img="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/fa-icon-16x9-mobile-retro-solid-full.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=031e48b78ff5d18495637f44dd0210a3" href="/hardware/boards/arducam-pico4ml-tinyml-dev-kit" width="1600" height="900" data-path=".assets/images/fa-icon-16x9-mobile-retro-solid-full.png" />

  <Card title="Deployments" img="https://mintcdn.com/edgeimpulse/LXQUM8XrxXJrL7kY/.assets/images/fa-icon-16x9-cube-solid-full.png?fit=max&auto=format&n=LXQUM8XrxXJrL7kY&q=85&s=378bea3a875182ac17012024a4304fb6" href="/hardware/deployments" width="1600" height="900" data-path=".assets/images/fa-icon-16x9-cube-solid-full.png" />
</Columns>

<Tabs>
  <Tab title="MCU-based hardware">
    For the MCU-based hardware, depending on the integration we provide several or all of the following options:

    * **A default Edge Impulse firmware**, ready to be flashed on the hardware. The firmware capabilities depends on the integration (see also [Edge Impulse firmwares](/hardware/deployments/run-ei-fw)).:
      * **Data collection:** Enables to [connect the hardware](/studio/projects/devices) to Edge Impulse Studio to simplify your getting started journey and ease the [data collection](/studio/projects/data-acquisition#collect-data) from some or all the sensors available.
      * **Inferencing example:** This includes the data sampling, extracting features using the signal processing blocks and run the inference using learning blocks.
      * **[Serial protocol](/tools/protocols/remote-management/serial) and/or [remote management protocol](/tools/protocols/remote-management/websocket)**.
      * **The open-source code for the firmware**, which comes with documentation on how to build and compile the Edge Impulse firmware.
    * **Examples on how to integrate your Impulse with your custom firmware**, either using the [C++ inferencing SDK](/hardware/deployments/run-cpp-overview) or using libraries or components tailored for your hardware development environments. In our [Github repository](https://github.com/orgs/edgeimpulse/repositories?q=example-standalone-inferencing), search for the `example-standalone-inferencing-%target%`
    * **Integrated deployment options** to directly export a ready-to-flash Edge Impulse firmware packaged with your Impulse (including both the signal processing and the machine learning model).
    * **Profiling (estimation of memory, flash and latency)** available in Edge Impulse Studio and in the [Edge Impulse Python SDK](/tools/libraries/sdks/studio/python).
    * **Extensive hardware testing**, to make sure any improvements and changes in Edge Impulse will not break the current integration.

    <Info>
      #### Not on the list?

      If you are using a different hardware target or custom PCB? No problem!

      You can upload data to Edge Impulse in a variety of ways, such as using the [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder), the [Edge Impulse for Linux](/tools/libraries/sdks/inference/linux) SDK, or by [uploading files directly](/studio/projects/data-acquisition/uploader) (e.g. CSV, JPG, WAV).

      From there, your trained model can be deployed as a [C++ library](/hardware/deployments/run-cpp-overview). It can require some effort, but most build systems (for computers, smartphones, and microcontrollers) will work with our C++ library. This, of course, requires that your build system has a C++ compiler and that there is enough flash/RAM on your device to run the library/model. And although we leverage hardware acceleration when possible on the hardware listed in this section, **keep in mind that our [EON Compiler](/studio/projects/deployment/eon-compiler) will optimize your preprocessing and your ai models for any targets compared to traditional compiler options.**

      Also, if you feel like porting the official Edge Impulse firmware to your own board, use this [porting guide](/hardware/porting-guide).
    </Info>
  </Tab>

  <Tab title="Linux-based hardware">
    For the Linux-based hardware, depending on the integration we provide several or all of the following options:

    * **The [Edge Impulse Linux CLI](/tools/clis/edge-impulse-cli)**: It contains tools that let you collect data from any microphone or camera, download the `.eim` (Edge Impulse Models) or run a test application to classify your data, available on your terminal or through a web interface.
    * **Deployment options**:
      * [Linux `.eim`](/studio/projects/deployment#deploy-as-a-linux-eim-binary), Edge Impulse for Linux models are delivered in `.eim` format. This is an executable that contains your signal processing and ML code, compiled with optimizations for your processor, GPU or other AI accelerators.
      * [Docker container](/studio/projects/deployment#deploy-using-a-docker-container), for environments supporting containerized workloads, facilitating deployment on gateways or in the cloud with full hardware acceleration for most Linux targets.
    * **Linux Inferencing SDKs**: To build your own applications, or collect data from new sensors, you can use the high-level language SDKs. These use full hardware acceleration, and let you integrate your Edge Impulse models in a few lines of code
    * **Profiling (estimation of memory, flash and latency)**, available in Edge Impulse Studio and in the [Edge Impulse Python SDK](/tools/libraries/sdks/studio/python).

    <Info>
      #### Not on the list?

      Different development board? Probably no problem! You can use the [Linux x86\_64 getting started guide](/hardware/devices/linux-x86_64) to set up the Edge Impulse for Linux CLI tool or use the [Docker](/hardware/deployments/run-docker), and you can run your impulse on any x86\_64, ARMv7 or AARCH64 Linux target. And although we leverage hardware acceleration when possible on the hardware listed in this section, **keep in mind that our [EON Compiler](/studio/projects/deployment/eon-compiler) will optimize your preprocessing and your ai models for any targets compared to traditional compiler options.**

      You can upload data to Edge Impulse in a variety of ways, such as using the [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder), the [Edge Impulse for Linux](/tools/libraries/sdks/inference/linux) SDK, or by [uploading files directly](/studio/projects/data-acquisition/uploader) (e.g. CSV, JPG, WAV).
    </Info>
  </Tab>
</Tabs>

The hardware targets listed in this section are the perfect way to start building machine learning solutions on real embedded hardware. Edge Impulse's Solution Engineers and Embedded Engineers have a strong expertise with these hardware targets and can help on your integration. Feel free to [contact us](https://edgeimpulse.com/pricing).

## Devices

* [Advantech ICAM-540](/hardware/devices/advantech-icam-540) (Linux | Industrial AI Camera with NVIDIA Orin NX)
* [CODICO Qualcomm Dragonwing Triple Vision Industrial AI Camera](/hardware/devices/jmo-triple-vision-camera) (Linux | Industrial AI Box with 3 Camera Inputs)
* [BrickML](/hardware/devices/brickml) (MCU | Industry Reference Design using RA6M5)
* [Onlogic FR101](/hardware/devices/onlogic-fr101) (QCS6490 | 2x Kryo 360 Gold @ 2.0 GHz + 6x Kryo 360 Silver @ 1.7 GHz + Hexagon 685)
* [OnLogic ML100G](/hardware/devices/onlogic-ml100g) (x86)
* [Seeed reComputer Jetson](/hardware/devices/seeed-recomputer-jetson) (AARCH64 | Cortex-A47 1.43 GHz + NVIDIA Maxwell 128 CUDA cores)
* [Seeed SenseCAP A1101](/hardware/devices/seeed-sensecap-a1101) (MCU | LoRaWAN Vision AI Sensor using Himax)
* [macOS](/hardware/devices/macos) (x86, M1, M2)
* [Linux x86\_64](/hardware/devices/linux-x86_64) (x86\_64)
* [Mobile phone](/hardware/devices/mobile-phone)

## Boards

### MCU

* [Ambiq Apollo4 evaluation boards](/hardware/boards/ambiq-apollo4) (Cortex-M4F 192MHz)
* [Arducam Pico4ML TinyML Dev Kit](/hardware/boards/arducam-pico4ml-tinyml-dev-kit) (RP2040 | Cortex-M0+ 200MHz)
* [Arduino Nano 33 BLE Sense](/hardware/boards/arduino-nano-33-ble-sense) (nRF52840 | Cortex-M4F 64MHz)
* [Arduino Nicla Sense ME](/hardware/boards/arduino-nicla-sense-me) (nRF52832 | Cortex-M4 64MHz)
* [Arduino Nicla Vision](/hardware/boards/arduino-nicla-vision) (STM32H747AII6 | Cortex-M7 480MHz)
* [Arduino Portenta H7](/hardware/boards/arduino-portenta-h7) (STM32H747XI | Cortex-M7 480MHz)
* [Blues Wireless Swan](/hardware/boards/blues-wireless-swan) (STM32L4+ | Cortex-M4 120MHz)
* [Espressif ESP-EYE](/hardware/boards/espressif-esp32) (ESP32 | Xtensa LX6 240MHz)
* [Himax WE-I Plus](/hardware/boards/himax-we-i-plus) (HX6537-A | ARC DSP 400MHz)
* [Infineon CY8CKIT-062-BLE Pioneer Kit](/hardware/boards/infineon-cy8ckit-062-ble) (PSoC63 | Cortex-M4F 150MHz)
* [Infineon CY8CKIT-062S2 Pioneer Kit](/hardware/boards/infineon-cy8ckit-062s2) (PSoC62 | Cortex-M4F 150MHz)
* [Nordic Semi nRF52840 DK](/hardware/boards/nordic-semi-nrf52840-dk) (nRF52840 | Cortex-M4F 64MHz)
* [Nordic Semi nRF5340 DK](/hardware/boards/nordic-semi-nrf5340-dk) (nRF5340 | Cortex-M33 128MHz)
* [Nordic Semi nRF54L15 DK](/hardware/boards/nordic-semi-nrf54L15-dk) (nRF54L15 | Cortex-M33 128MHz)
* [Nordic Semi nRF7002 DK](/hardware/boards/nordic-semi-nrf7002-dk) (nRF7002 | Cortex-M33 128MHz)
* [Nordic Semi nRF9160 DK](/hardware/boards/nordic-semi-nrf9160-dk) (nRF9160 | Cortex-M33 64MHz)
* [Nordic Semi nRF9161 DK](/hardware/boards/nordic-semi-nrf9161-dk) (nRF9160 | Cortex-M33 64MHz)
* [Nordic Semi nRF9151 DK](/hardware/boards/nordic-semi-nrf9151-dk) (nRF9160 | Cortex-M33 64MHz)
* [Nordic Semi Thingy:53](/hardware/boards/nordic-semi-thingy53) (nRF5340 | Cortex-M33 128MHz)
* [Nordic Semi Thingy:91](/hardware/boards/nordic-semi-thingy91) (nRF9160 | Cortex-M33 64MHz)
* [Open MV Cam H7 Plus](/hardware/boards/openmv-cam-h7-plus) (STM32H743II | Cortex-M7 480MHz)
* [Particle Photon 2](/hardware/boards/particle-photon-2) (RTL8721DM | Cortex-M33 200MHz)
* [Particle Boron](/hardware/boards/particle-boron) (nRF52840 | Cortex-M4 64MHz)
* [RAKwireless WisBlock](/hardware/boards/rakwireless-wisblock) (RP2040 | Cortex-M0+ 200MHz, Xtensa LX6 240MHz, ESP32, nRF52840 | Cortex-M4F 64MHz)
* [Raspberry Pi Pico](/hardware/boards/raspberry-pi-pico) (RP2040 | Cortex-M0+ 200MHz, RP2350 | Cortex-M33 150MHz)
* [Renesas CK-RA6M5 Cloud Kit](/hardware/boards/renesas-ck-ra6m5) (RA6M5 | Cortex-M33 200MHz)
* [Renesas EK-RA8D1](/hardware/boards/renesas-ek-ra8d1) (RA8D1 | Cortex-M85 480MHz)
* [Seeed Grove - Vision AI Module](/hardware/boards/seeed-grove-vision-ai) (HX6537-A | ARC DSP 400MHz)
* [Seeed Wio Terminal](/hardware/boards/seeed-wio-terminal) (HX6537-A | ARC DSP 400MHz)
* [Seeed XIAO nRF52840 Sense](/hardware/boards/seeed-xiao-nrf52840-sense) (nRF52840 | Cortex-M4F 64MHz)
* [Seeed XIAO ESP32 S3 Sense](/hardware/boards/seeed-xiao-esp32s3-sense) (ESP32S3 | Xtensa LX7 240MHz)
* [SiLabs Thunderboard Sense 2](/hardware/boards/silabs-thunderboard-sense-2) (EFR32MG12 | Cortex-M4 40MHz)
* [Sony's Spresense](/hardware/boards/sony-spresense) (CXD5602 | Cortex-M4F 156MHz)
* [ST B-L475E-IOT01A](/hardware/boards/st-b-l475e-iot01a) (STM32L4 | Cortex-M4 120MHz)
* [TI CC1352P Launchpad](/hardware/boards/ti-launchxl) (CC1352P | Cortex-M4F 48MHz)

### MCU + AI Accelerators

* [Alif Ensemble series kits](/hardware/boards/alif-ensemble) (Cortex-M55 + Ethos-U55 (multiple cores))
* [Ambiq Apollo5 evaluation boards](/hardware/boards/ambiq-apollo5) (Cortex-M55 250MHz)
* [Arduino Nicla Voice](/hardware/boards/arduino-nicla-voice) (Cortex-M4 + NDP120)
* [Avnet RASynBoard](/hardware/boards/avnet-rasynboard)  (RA6 + NDP120)
* [Nordic Semi nRF54LM20 DK](/hardware/boards/nordic-semi-nrf54LM20-dk) (nRF54LM20 | Cortex-M33 + Nordic Axon NPU)
* [SiLabs xG24 Dev Kit](/hardware/boards/silabs-xg24-devkit) (Cortex-M33 78MHz + SiLabs MVP)
* [STMicroelectronics STM32N6570-DK](/hardware/boards/stm32n6570-dk) (Cortex-M55 + ST Neural-ART Accelerator)
* [Synaptics Katana EVK](/hardware/boards/synaptics-katana) (KA10000)
* [Syntiant Tiny ML Board](/hardware/boards/syntiant-tinyml-board) (NDP101)
* [Seeed Grove Vision AI Module](/hardware/boards/seeed-grove-vision-ai)
* [Seeed Grove Vision AI Module V2 (WiseEye2)](/hardware/boards/seeed-grove-vision-ai-module-v2-wise-eye-2)
* [Himax WiseEye2 ISM Module/Devboard](/hardware/boards/himax-ism-wise-eye-2)

### CPU

* [Arduino UNO Q](/hardware/boards/arduino-uno-q) (ARMv8 | Quad Cortex-A53 2.0GHz)
* [Raspberry Pi 4](/hardware/boards/raspberry-pi-4) (ARMv7 | Cortex-A72 1.5GHz)
* [Raspberry Pi 5](/hardware/boards/raspberry-pi-5) (Cortex-A76 2.4 GHz)
* [Texas Instruments SK-AM62](/hardware/boards/ti-sk-am62) (AM62x | Cortex-A53 1.4GHz)
* [Microchip SAMA7G54](/hardware/boards/microchip-sama7) (SAMA7G54 | Cortex-A7)
* [Renesas RZ/G2L](/hardware/boards/renesas-rz-g2l) (RZ/G2L | Cortex-A55 1.2GHz)

### CPU + AI Accelerators

* [AVNET RZBoard V2L](/hardware/boards/avenet-rz-v2l) (RZ/V2L | Cortex-A55 1.2GHz + DRPAI)
* [BrainChip AKD1000](/hardware/boards/brainchip-akd1000) (x86\_64 or AARCH64 + AKD1000)
* [i.MX 8M Plus EVK](/hardware/boards/nxp-imx8-evk) (i.MX 8M Plus | Cortex-A53 1.8GHz + NPU)
* [Digi ConnectCore 93 Development Kit](/hardware/boards/digi-ccimx93-dvk) (i.MX 93 | Cortex-A55 1.7GHz + NPU)
* [MemryX MX3](/hardware/boards/memryx-mx3) (x84\_64 | MX3 5 TFLOPs)
* [MistyWest MistySOM RZ/V2L](/hardware/boards/mistywest-rz-v2l) (RZ/V2L | Cortex-A55 1.2GHz + DRPAI)
* [Qualcomm IQ9075-EVK Dev Kit](/hardware/boards/qualcomm-iq9075-evk) (QCS9075 | 4x Kryo @ 2.5 GHz + 4x Kryo @ 1.9 GHz + Hexagon + Adreno GPU)
* [Qualcomm Dragonwing RB3 Gen 2 Dev Kit](/hardware/boards/qualcomm-rb3-gen-2-dev-kit) (QCS6490 | 2x Kryo 360 Gold @ 2.0 GHz + 6x Kryo 360 Silver @ 1.7 GHz + Hexagon 685)
* [Quectel PI-SG565D](/hardware/boards/quectel-pi-sg565d) (QCS6490 | 2x Kryo 360 Gold @ 2.0 GHz + 6x Kryo 360 Silver @ 1.7 GHz + Hexagon 685)
* [Advantech AOM 2721 SOM](/hardware/boards/advantech-aom2721-osm) (QCS6490 | Kryo 360 Gold @ 2.7 GHz + 3x Kryo 360 Gold @ 2.4 GHz + 4x Kryo 360 Silver @ 1.9 GHz + Andreo VPU 633)
* [Renesas RZ/V2L](/hardware/boards/renesas-rz-v2l) (RZ/V2L | Cortex-A55 1.2GHz + DRPAI)
* [Renesas RZ/V2H](/hardware/boards/renesas-rz-v2h) (RZ/V2H | Cortex-A55 1.8GHz + Dual Cortex-R8 + TVM/DRP)
* [Texas Instruments SK-TDA4VM](/hardware/boards/ti-sk-tda4vm) (TDA4VM | Cortex-A72 + C7x 8TFLOPs)
* [Texas Instruments SK-AM62A-LP](/hardware/boards/ti-sk-am62a-lp) (AM62A | Cortex-A53 + AI Accelerator 2 TFLOPs)
* [Texas Instruments SK-AM68A](/hardware/boards/ti-sk-am68a) (AM68x | Cortex-A72 + AI Accelerator 8 TFLOPs)
* [Thundercomm Rubik Pi 3](/hardware/boards/thundercomm-rubikpi3) (QCS6490 | 2x Kryo 360 Gold @ 2.0 GHz + 6x Kryo 360 Silver @ 1.7 GHz + Hexagon 685)
* [Tria Vision AI Kit](hardware/boards/tria-vision-ai-kit-6490) (QCS6490 | 2x Kryo 360 Gold @ 2.0 GHz + 6x Kryo 360 Silver @ 1.7 GHz + Hexagon 685)

### GPU

* [NVIDIA Jetson Orin and Nano](/hardware/boards/nvidia-jetson) (Nano: AARCH64 | Cortex-A57 + NVIDIA Maxwell 128 CUDA cores)


Built with [Mintlify](https://mintlify.com).