# Source: https://docs.edgeimpulse.com/hardware/boards/alif-ensemble.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Alif Ensemble series kits

The [Ensemble](https://alifsemi.com/ensemble/) series of fusion processors from [Alif Semiconductor](https://alifsemi.com/) use ARM's low power Cortex-M55 CPUs with dedicated Ethos-U55 microNPUs to run embedded ML workloads quickly and efficiently. The devices feature both 'High Power' cores designed for large model architectures, as well as 'High Efficiency' cores designed for low power continuous monitoring. The development kit and the application kit are both fully supported by Edge Impulse. The Ensemble kits feature multiple core types, dual MEMS microphones, accelerometers, and a MIPI camera interface.

To get started with the Alif Ensemble processors and Edge Impulse you'll need either the [Alif Ensemble AppKit](https://alifsemi.com/support/kits/ensemble-e7appkit/) or the [Alif Ensemble DevKit](https://alifsemi.com/support/kits/ensemble-e7devkit/).

<Frame caption="Alif Ensemble Group">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/alif/ensemble-group.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=5a63aa4a95935e1f3cbe410332813b2b" width="1600" height="702" data-path=".assets/images/alif/ensemble-group.png" />
</Frame>

## Deployment options

<AccordionGroup>
  <Accordion title="Ethos-U55-128 library (High End Embedded, Shared SRAM)">
    A C++ library with inferencing for devices with an Ethos-U55-128 NPU, High End Embedded with shared SRAM. For example: Alif E7 RTSS-HE.
  </Accordion>

  <Accordion title="Ethos-U55-256 library (High End Embedded, Shared SRAM)">
    A C++ library with inferencing for devices with an Ethos-U55-256 NPU, High End Embedded with shared SRAM. For example: Alif E7 RTSS-HP.
  </Accordion>

  <Accordion title="Alif AI/ML Kit Gen2 HE core">
    A binary containing both the Edge Impulse data acquisition client and your full impulse.
  </Accordion>

  <Accordion title="Alif AI/ML Kit Gen2 HP core">
    A binary containing both the Edge Impulse data acquisition client and your full impulse.
  </Accordion>

  <Accordion title="Alif AI/ML Kit Gen2 HP core - tensor arena statically allocated to SRAM">
    A binary containing both the Edge Impulse data acquisition client and your full impulse.
  </Accordion>

  <Accordion title="Alif Dev Kit Gen2 HE core">
    A binary containing both the Edge Impulse data acquisition client and your full impulse.
  </Accordion>

  <Accordion title="Alif Dev Kit Gen2 HP core">
    A binary containing both the Edge Impulse data acquisition client and your full impulse.
  </Accordion>

  <Accordion title="Alif Dev Kit Gen2 HP core - tensor arena statically allocated to SRAM">
    A binary containing both the Edge Impulse data acquisition client and your full impulse.
  </Accordion>

  <Accordion title="Ethos-U55-128 Open CMSIS Pack">
    A C++ library in Open CMSIS pack format with for devices with an Ethos-U55-128 NPU, High End Embedded with shared SRAM. For example: Alif E7 RTSS-HE.
  </Accordion>

  <Accordion title="Ethos-U55-256 Open CMSIS Pack">
    A C++ library in Open CMSIS pack format with for devices with an Ethos-U55-256 NPU, High End Embedded with shared SRAM. For example: Alif E7 RTSS-HP.
  </Accordion>
</AccordionGroup>

## Installing dependencies

To set this device up in Edge Impulse, you will need to install the following software:

1. [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
2. The latest `Alif Security Toolkit`:

* Navigate to the [Alif Semiconductor Kit documentation page](https://alifsemi.com/kitsensemble/) (you will need to register to create an account with Alif, or log in to your existing Alif account). and download the latest App Security Toolkit (tested with version 0.56.0) for windows or linux.
* Extract the archive, and read through the included `Security Toolkit Quick Start Guide` to finalize the installation
* IMPORTANT: Set an environmental variable called `SETOOLS_ROOT`to the Security Toolkit root path. This is used by Edge Impulse scripts when flashing the Alif development kits. [Example instructions for Linux, Windows, MacOS](https://gcore.com/learning/environment-variables/).

3. (Optional) [Docker Desktop](https://www.docker.com/products/docker-desktop/):

* If you are using MacOS, we recommended installing [Docker Desktop](https://www.docker.com/products/docker-desktop/) in order to use the Alif Security Toolkit for programming.

## Connecting to Edge Impulse

Once you have installed it's time to connect the development board to Edge Impulse.

### Configuring your hardware

To interface the Alif Ensemble AppKit or Development Kit, you'll need to connect your device to the USB port label `PRG USB`.

### Flashing the default firmware to the device

<Info>
  You can program and use serial port of the device if you adjust jumper J15 to connect pins 1-3 and 2-4.
  There will be two serial ports enumerated. The first port is used for programming, the second for serial communication.
</Info>

<Info>
  Inspect `isp_config_data.cfg` in the Security Toolkit directory to ensure the COM port is set correctly to the device attached to your computer.
  There will be two serial ports enumerated. The first port is used for programming, the second for serial communication.
</Info>

After configuring the hardware, the next step is to flash the default Edge Impulse Firmware. This will allow us to collect data directly from your Ensemble device. To update the firmware:

1. [Download the latest Edge Impulse firmware binary](https://cdn.edgeimpulse.com/firmware/alif-e7-gen2.zip) and unzip the file.

2. Open a terminal in the unzipped folder and run the following commands. Use the `HE`, `HP`, or `HP_SRAM` parameter that matches the deployment chosen from the Edge Impulse project. That is, if you Deployed for HP\_SRAM please use the `HP_SRAM` parameters.

#### MacOS or Linux

```
flash.sh <HE, HP, or HP_SRAM>
```

#### Windows

```
flash_win.bat <HE, HP, or HP_SRAM>
```

### Running the Edge Impulse CLI

<Info>
  To use the device serial port, set the jumper accordingly: for the **DevKit** use J26, and for the **AppKit** use J15, connecting pins 1-3 and 2-4.
</Info>

Now, the Ensemble device can connect to the `Edge Impulse CLI` installed earlier. To test the CLI for the first time, either:

Create a new project from the [Edge Impulse project dashboard](https://studio.edgeimpulse.com/studio/profile/projects)

OR

Clone an existing Edge Impulse public project, like this [Face Detection Demo](https://studio.edgeimpulse.com/public/87291/latest). Click the link and then press `Clone` at the top right of the public project.

Then, from a command prompt or terminal on your computer, run:

```
edge-impulse-daemon
```

<Info>
  **Device choice**

  You may see two `FTDI` or `CYPRESS` serial ports enumerated for devices. If so, select the second entry in the list, which generally is the serial data connection to the Ensemble device. Ensure that the jumpers are correctly oriented for serial communication.
</Info>

This will start a wizard which will ask you to log in and choose an Edge Impulse project. You should see your new or cloned project listed on the command line. Use the arrow keys and hit `Enter` to select your project.

### Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to

<Frame caption="Device connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/alif/alif-your-devices-edit.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=e447541ac1e8fe41bcfec00fecd43f09" width="1600" height="385" data-path=".assets/images/alif/alif-your-devices-edit.png" />
</Frame>

## Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials. This will walk you through the process of collecting data and training a new ML model:

* [Image classification - Image Classification Tutorial](/tutorials/end-to-end/image-classification)
* [Object Detection End-to-End Tutorial](/tutorials/end-to-end/object-detection-bounding-boxes)
* [Object detection with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids)
* [Building a continuous motion recognition system](/tutorials/end-to-end/motion-recognition)
* [Recognizing sounds from audio](/tutorials/end-to-end/sound-recognition)
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)

Alternatively, you can test on-device inference with a demo model included in the base firmware binary. To do this, you may run the following command from your terminal:

```
edge-impulse-run-impulse --debug
```

Then, once you've tested out training and deployment with the Edge Impulse Firmware, learn how to integrate impulses with your own custom Ensemble based application:

* [Run on Alif Ensemble Series devices](/hardware/deployments/run-cpp-alif-ensemble)


Built with [Mintlify](https://mintlify.com).