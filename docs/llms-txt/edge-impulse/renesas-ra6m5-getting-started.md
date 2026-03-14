# Source: https://docs.edgeimpulse.com/projects/expert-network/renesas-ra6m5-getting-started.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Renesas CK-RA6M5 Cloud Kit - Getting Started with Machine Learning

Created By: Swapnil Verma

Public Project Link: [https://studio.edgeimpulse.com/public/233106/latest](https://studio.edgeimpulse.com/public/233106/latest)

## Introduction

The [Renesas CK-RA6M5 Cloud Kit](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ck-ra6m5-cloud-kit-based-ra6m5-mcu-group) enables users to securely connect to the cloud and explore the features of the Cortex M33-based Renesas RA6M5 group of MCUs and cloud services. This development board can run machine-learning models and is officially supported by Edge Impulse.

This is a Getting Started Guide for the Renesas CK-RA6M5 board with Edge Impulse. Here we will connect the board to the Edge Impulse Studio, collect sensor data directly from the board, prepare a machine learning model using the collected data, deploy the model back to the board, and perform inferencing locally on the board. Let's get started!

## Unboxing

The Cloud Kit comes with the following items in the box:

* The CK-RA6M5 development board
* RYZ014A PMOD (CAT-M1 Cellular Module)
* SIM card
* Antenna
* 2 Micro USB to A cables
* Micro USB A/B to A adapter cable
* Documentation

<Frame caption="Renesas CK-RA6M5 Cloud Kit">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/ra6m5-kit.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=f6dedb7d2c0aa50fc38127d1a7c56ba3" width="952" height="960" data-path=".assets/images/renesas-ra6m5-getting-started/ra6m5-kit.jpg" />
</Frame>

## Quick Start Project

Each CK-RA6M5 board comes preinstalled with a quick-start project. Let's run that quick-start project to verify our board is working properly.

* Make sure that (a) J22 is set to link pins 2-3 (b) J21 link is closed and (c) J16 link is open.
* Connect J14 and J20 on the CK-RA6M5 board to USB ports on the host PC using the 2 micro USB cables supplied.
* The power LED (LED6) on the CK-RA6M5 board lights up white, indicating that the CK-RA6M5 board is powered on.

<Frame caption="Board Connection">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/ra6m5-connection.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=38c1dae6ac5234844272d131af700c8c" width="1280" height="563" data-path=".assets/images/renesas-ra6m5-getting-started/ra6m5-connection.jpg" />
</Frame>

Immediately after the power on, the four user LEDs will take on the following states:

<Frame caption="LED Status">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/led-status.gif?s=0c361b12e1e909ee05ef259d0ffc7ee0" width="988" height="864" data-path=".assets/images/renesas-ra6m5-getting-started/led-status.gif" />
</Frame>

* LED1 Red – Off
* LED2 RGB – Off
* LED3 Green – Steady, full intensity
* LED4 Blue – Blinking at 1hz frequency

<Frame caption="LED4 blinking at 1hz">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/led-status-2.gif?s=7af0e0ce3aaadbb325b7fe040de20b6a" width="1069" height="564" data-path=".assets/images/renesas-ra6m5-getting-started/led-status-2.gif" />
</Frame>

Press the user button (S2) on the board to change the blinking frequency of the user LED4 (blue). With every press of the first user button (S2), the frequency will switch from 1 Hz to 5 Hz to 10 Hz and cycle back.

<Frame caption="LED4 blinking at 5hz">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/led-status-3.gif?s=6da7575852491e3b35f9e592962a7564" width="1069" height="575" data-path=".assets/images/renesas-ra6m5-getting-started/led-status-3.gif" />
</Frame>

## Updating the Firmware

In order to connect the CK-RA6M5 board to the Edge Impulse Studio, we need to upgrade the board's firmware. Please follow the official Edge Impulse guide to update its firmware:

[Firmware Update Guide](/hardware/boards/renesas-ck-ra6m5)

Once the board is flashed with Edge Impulse firmware, the real magic starts.

## Edge Impulse Project

To begin, you'll need to create an Edge Impulse account and a project in the Edge Impulse Studio. Please follow the below steps to do so:

* Navigate to the [Edge Impulse Studio](https://studio.edgeimpulse.com/login) and create an account. If you already have an account then please login using your credentials.

<Frame caption="Edge Impulse Studio">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/studio.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=ecaa620b1d6a51847414a5f89f9b6ef5" width="1280" height="615" data-path=".assets/images/renesas-ra6m5-getting-started/studio.jpg" />
</Frame>

* After login, please create a new project, give it a suitable name, and select an appropriate *Project type*.

<Frame caption="Project Type">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/project-type.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=30b4dd7e4e0c0a6bb9bd12d76f14c687" width="593" height="526" data-path=".assets/images/renesas-ra6m5-getting-started/project-type.jpg" />
</Frame>

* After creating a new project, navigate to the *Devices* Tab.

<Frame caption="Device Tab">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/devices.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=4707ce8dc92540f76eb19eead7f05a56" width="1252" height="453" data-path=".assets/images/renesas-ra6m5-getting-started/devices.jpg" />
</Frame>

## Connecting Renesas CK-RA6M5 to Edge Impulse

The next step is connecting our Renesas CK-RA6M5 board to the Edge Impulse Studio, so we can ingest sensor data for the machine learning model. Please follow the below steps to do so:

* Connect the Renesas CK-RA6M5 board to the computer by following the steps mentioned in the *Quick Start* section.
* Open a terminal or command prompt and type `edge-impulse-daemon`. The [Edge Impulse serial daemon](/tools/clis/edge-impulse-cli/serial-daemon) will start and prompt for user credentials.
* After providing user credentials, it will prompt you to select an Edge Impulse project. Please navigate and select the project created in the previous steps, using the arrow keys.

<Frame caption="Daemon">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/daemon.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=bc75de2da1ddc7414381b0b7da63fc00" width="1280" height="871" data-path=".assets/images/renesas-ra6m5-getting-started/daemon.jpg" />
</Frame>

* After selecting the project, it will ask you to give the connected board a name. It is useful when you want to connect multiple boards to the same project.

<Frame caption="Device Naming">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/naming.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=f410912c8d844f4e0049c2278098d51c" width="1280" height="317" data-path=".assets/images/renesas-ra6m5-getting-started/naming.jpg" />
</Frame>

* Now the board should be connected to the selected project. The `edge-impulse-daemon` will tell you which project the board is connected to. We can also verify by checking the **Devices** tab of that project.

<Frame caption="Device Connected">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/connected.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=636c565be32e41e7d93efc271f986600" width="1252" height="366" data-path=".assets/images/renesas-ra6m5-getting-started/connected.jpg" />
</Frame>

It will also list all the sensors available for data gathering.

## Data Gathering

Edge Impulse provides multiple options for [data acquisition](/studio/projects/data-acquisition). In this Getting Started Guide, we will look at the direct data ingestion from the board using `edge-impulse-daemon`. Please follow the below steps for data acquisition:

* Navigate to the *Data Acquisition* tab in the Edge Impulse Studio.

<Frame caption="Data Acquisition">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/data-acquisition.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=f4afb31e0a5df968032cef0447687dc5" width="1280" height="623" data-path=".assets/images/renesas-ra6m5-getting-started/data-acquisition.jpg" />
</Frame>

* Here you will find the *Device* we connected in the previous step and the sensor list. Please select the suitable sensor from the drop-down menu. For this project, I have selected the *Microphone* sensor and used default parameters.
* Add a *Label name* for the sample you are about to collect. I am collecting clap and whistle sounds therefore I will use *clap* and *whistle* as labels.
* Clicking *Start Sampling* will start the sample collection process. Once the sample is collected, it will be automatically uploaded to the Edge Impulse Studio.

<Frame caption="Data Collection Process">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/data-collection.gif?s=e80addd85bf30edf9fe9d6f3c9cf45e5" width="1512" height="982" data-path=".assets/images/renesas-ra6m5-getting-started/data-collection.gif" />
</Frame>

When enough samples are collected, [balance the data](/studio/projects/data-acquisition#dataset-train%2Ftest-split-ratio) and if required [clean the data](/studio/projects/data-acquisition#cropping-samples) as well.

<Frame caption="Dataset Train/Test Split">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/split.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=0da1d987440ff181a97f228ccbf7f37e" width="1280" height="832" data-path=".assets/images/renesas-ra6m5-getting-started/split.jpg" />
</Frame>

## Machine Learning Model Preparation

After data collection, the next step is machine learning model preparation. To do so, please navigate to the [*Impulse design* tab](/studio/projects/impulse-design) and add relevant [preprocessing](/studio/projects/processing-blocks) and [learning blocks](/studio/projects/learning-blocks) to the pipeline.

* Edge Impulse Studio will automatically add an [input block](/studio/projects/impulse-design#input-block) and it will recommend a suitable preprocessing and a learning block based on the data type. I have used the recommended ones in this project with the default arguments.

<Frame caption="Impulse Design">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/impulse-design.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=5c598ffbbf81f35a7bc4adb4f098c953" width="1280" height="759" data-path=".assets/images/renesas-ra6m5-getting-started/impulse-design.jpg" />
</Frame>

* After Impulse design is complete, save the design and navigate to the preprocessing tab (MFE in this case) for the feature generation.

<Frame caption="Preprocessing Block">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/feature-generation.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=722feffadbb13c6c6b767e5e00773b95" width="995" height="960" data-path=".assets/images/renesas-ra6m5-getting-started/feature-generation.jpg" />
</Frame>

Click on the *Save parameters* button, then navigate to the *Generate features* tab and click *Generate features* button for data preprocessing.

<Frame caption="Feature Generation">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/feature-generation-2.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=2e8b852be860ffc7b181899c0fab0b32" width="1051" height="871" data-path=".assets/images/renesas-ra6m5-getting-started/feature-generation-2.jpg" />
</Frame>

* After feature generation, please navigate to the *Learning Tab* ([Classifier](/studio/projects/learning-blocks/blocks/classification) in this case) to design the neural network architecture. I have used the default architecture and parameters recommended by the Edge Impulse Studio. After selecting a suitable configuration, click on the *Start training* button.

<Frame caption="Classifier Design">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/classifier-design.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=5410bf07a82e06833f196d9115a9f9e4" width="968" height="960" data-path=".assets/images/renesas-ra6m5-getting-started/classifier-design.jpg" />
</Frame>

* Once the training is complete, please navigate to the [Model testing](/studio/projects/model-testing) tab, and click *Classify all* button.

<Frame caption="Model Testing">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/model-testing.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=9dbd146848309e7321df0a5ea9935efe" width="1032" height="960" data-path=".assets/images/renesas-ra6m5-getting-started/model-testing.jpg" />
</Frame>

After testing is finished, the Edge Impulse Studio will show the model accuracy, and other parameters.

> Even though it is a simple example, the Edge Impulse Studio prepared an excellent machine learning model just by using the default recommended parameters, in just a couple of minutes.

## Deployment

In this step, we will deploy our prepared model to the Renesas CK-RA6M5 board, so we can perform inference locally on the board.

* Please navigate to the [Deployment](/studio/projects/deployment) tab, select the Renesas CK-RA6M5 board using the search bar, and click on the *Build* button.

<Frame caption="Deployment Tab">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/deployment.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=cfa909e46944e48441a892ec24c1b718" width="1039" height="960" data-path=".assets/images/renesas-ra6m5-getting-started/deployment.jpg" />
</Frame>

* After the *build* is finished, the new firmware will be downloaded automatically to your computer, and the Edge Impulse Studio will provide next-step instructions.

<Frame caption="Next Steps">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/deployment-2.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=92845714bc5fd0e05c1a5d1b1fcdf45a" width="905" height="960" data-path=".assets/images/renesas-ra6m5-getting-started/deployment-2.jpg" />
</Frame>

* Please extract the folder and double-click the `flash_<operating-system>` file. This will flash the newly created firmware on the CK-RA6M5 board. This firmware contains the machine learning model we prepared in the above steps.

<Frame caption="Flashing Firmware">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ra6m5-getting-started/flashing.gif?s=6594a875c7bd91c69df6981341f73332" width="2228" height="1644" data-path=".assets/images/renesas-ra6m5-getting-started/flashing.gif" />
</Frame>

## Inferencing

The next step is testing!! Let's see how well our model performs when run locally on the Renesas CK-RA6M5 board:

<iframe src="https://www.youtube.com/embed/THdl2YIPggY" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

And, that's it. I hope this Getting Started Guide will be useful for you when using the Renesas CK-RA6M5 with Edge Impulse.

If you have any questions, please check out the [Edge Impulse Forum](https://forum.edgeimpulse.com/).


Built with [Mintlify](https://mintlify.com).