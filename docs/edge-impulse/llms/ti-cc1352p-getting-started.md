# Source: https://docs.edgeimpulse.com/projects/expert-network/ti-cc1352p-getting-started.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TI CC1352P Launchpad - Getting Started with Machine Learning

Created By: Swapnil Verma

Public Project Link: [https://studio.edgeimpulse.com/public/238204/latest](https://studio.edgeimpulse.com/public/238204/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/ti-cc1352p-getting-started/header.jpg?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=3f89f7f70360d36e6fb5f1b6da128441" width="900" height="675" data-path=".assets/images/ti-cc1352p-getting-started/header.jpg" />
</Frame>

## Introduction

The [Texas Instruments CC1352P Launchpad](https://www.ti.com/tool/LAUNCHXL-CC1352P) is a development board equipped with the multiprotocol wireless CC1352P microcontroller. The Launchpad, when paired with the [BOOSTXL-SENSORS](https://www.ti.com/lit/ug/slau666b/slau666b.pdf) is [fully supported by Edge Impulse](/hardware), and can sample sensor data, build models, and deploy directly to the device without any programming required.

This is a Getting Started Guide for the TI LAUNCHXL-CC1352P development board with Edge Impulse. Here we will connect the board to the Edge Impulse Studio, collect sensor data directly from the board, prepare a machine learning model using the collected data, deploy the model back to the board, and perform inferencing locally on the board. Let's get started!

## Unboxing

The Launchpad Kit comes with the following items in the box:

* The LAUNCHXL-CC1352P development board
* Micro-USB to USB-A Cable
* Documentation

The BOOSTXL sensor comes with:

* BOOSTXL sensor board
* Documentation

## Quick Start Project

Each LAUNCHXL-CC1352P board comes preinstalled with a quick-start project called Project Zero. Let's run the quick-start project to verify our board is working properly.

* Connect the board to the computer using the provided micro-USB cable.
* Download the SimpleLink Starter smartphone app on your smartphone. This app lets you control the LEDs, see the state of the buttons and send data to the UART.
* Open the app, select Project Zero from the list of available devices, and click on Sensor View to get the GUI.

<Frame caption="SimpleLink Starter Application">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/ti-cc1352p-getting-started/simplelink.jpg?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=4148ccd6dcafc313ea86f9b0d9af0e25" width="256" height="555" data-path=".assets/images/ti-cc1352p-getting-started/simplelink.jpg" />
</Frame>

In the Project Zero GUI, tap on the lights to turn them On/Off on the board. Press the user buttons on the board to see their status on the app.In the Project Zero GUI, tap on the lights to turn them On/Off on the board. Press the user buttons on the board to see their status on the app.

<iframe src="https://www.youtube.com/embed/vSlQIOXhFPc" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

To learn more about Project Zero or user guide please follow [this link](https://dev.ti.com/tirex/explore/node?devtools=LAUNCHXL-CC1352P-2\&node=A__AP29fH4CgXFx6NzMPibGgg__cc13xx_devtools__FUz-xrs__LATEST).

## Updating the Firmware

In this section, we will upgrade the firmware of the development board so we can connect it to the Edge Impulse Studio.

Please follow this official guide to update the firmware:

[Firmware Update Guide](/hardware/boards/ti-launchxl)

## Edge Impulse Project

To begin, you'll need to create an Edge Impulse account and a project in the Edge Impulse Studio. Please follow the below steps to do so:

* Navigate to the [Edge Impulse Studio](https://studio.edgeimpulse.com/login) and create an account. If you already have an account then please login using your credentials.

<Frame caption="Edge Impulse Studio">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/ti-cc1352p-getting-started/studio.jpg?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=ac4f893e55c4f5885e6e93f4606bf7f0" width="740" height="356" data-path=".assets/images/ti-cc1352p-getting-started/studio.jpg" />
</Frame>

* After login, please create a new project, give it a suitable name, and select an appropriate *Project type*.

<Frame caption="Project Type">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/ti-cc1352p-getting-started/project-type.jpg?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=ad93eea88ea116db52e5c54efe78180c" width="594" height="523" data-path=".assets/images/ti-cc1352p-getting-started/project-type.jpg" />
</Frame>

* After creating a new project, let's connect the development board to the Studio.

## Connecting TI Launchpad Kit to Edge Impulse

The next step is connecting our TI LAUNCHXL board to the Edge Impulse Studio, so we can ingest sensor data for the machine learning model. Please follow the below steps to do so:

* Open a terminal or command prompt and type `edge-impulse-daemon`. The Edge Impulse [serial daemon](/tools/clis/edge-impulse-cli/serial-daemon) will start and prompt for user credentials. If you have not installed Edge Impulse CLI as part of the **Update the Firmware** section, then please install it now.
* After providing user credentials, it will prompt you to select an Edge Impulse project. Please navigate and select the project created in the previous steps, using the arrow keys.

<Frame caption="Daemon">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/ti-cc1352p-getting-started/daemon.jpg?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=ef2ad89c2e4bd313c1aad7c59ef5a98f" width="1177" height="960" data-path=".assets/images/ti-cc1352p-getting-started/daemon.jpg" />
</Frame>

* After selecting the project, it will ask you to give the connected board a name. It is useful when you want to connect multiple boards to the same project.

<Frame caption="Device Naming">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/ti-cc1352p-getting-started/naming.jpg?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=e9553bd6d1490ad1ff33e081a8358ee0" width="1280" height="319" data-path=".assets/images/ti-cc1352p-getting-started/naming.jpg" />
</Frame>

* Now the board should be connected to the selected project. The `edge-impulse-daemon` will tell you which project the board is connected to. We can also verify by checking the devices tab of that project.

<Frame caption="Device Connected">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/ti-cc1352p-getting-started/connected.jpg?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=30237a5d0e61e2cb5dff5106532b29b0" width="1280" height="236" data-path=".assets/images/ti-cc1352p-getting-started/connected.jpg" />
</Frame>

## Data Gathering

Edge Impulse provides multiple options for [data acquisition](/studio/projects/data-acquisition). In this Getting Started Guide, we will look at the direct data ingestion from the board using `edge-impulse-daemon`. Please follow the below steps for data acquisition:

* Navigate to the *Data Acquisition* tab in the Edge Impulse Studio.

<Frame caption="Data Acquisition">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/ti-cc1352p-getting-started/data-acquisition.jpg?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=4c5af735a159bc8dbd9203042695e507" width="1234" height="619" data-path=".assets/images/ti-cc1352p-getting-started/data-acquisition.jpg" />
</Frame>

* Here you will find the *Device* we connected in the previous step and the sensor list. Please select the suitable sensor from the drop-down menu. For this project, I have selected the *Accelerometer* sensor and used default parameters.
* Add a *Label name* for the sample you are about to collect. I am collecting up-down, side-to-side and circular motion data therefore I will use up\_down, side\_to\_side and circle as labels. As a default motion, I will also collect stationary data.
* Clicking *Start Sampling* will start the sample collection process. Once the sample is collected, it will be automatically uploaded to the Edge Impulse Studio.

<Frame caption="Data Collection Process">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/ti-cc1352p-getting-started/data-collection.gif?s=e288b22c95d1b6274004e5b869a53219" width="980" height="1140" data-path=".assets/images/ti-cc1352p-getting-started/data-collection.gif" />
</Frame>

When enough samples are collected, [balance the data](/studio/projects/data-acquisition#dataset-train%2Ftest-split-ratio) and if required [clean the data](/studio/projects/data-acquisition#cropping-samples) as well.

<Frame caption="Dataset Train/Test Split">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/ti-cc1352p-getting-started/split.jpg?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=348eae1808043b8f328f8b10947f5dac" width="665" height="555" data-path=".assets/images/ti-cc1352p-getting-started/split.jpg" />
</Frame>

## Machine Learning Model Preparation

After data collection, the next step is machine learning model preparation. To do so, please navigate to the [*Impulse design* tab](/studio/projects/impulse-design) and add relevant [preprocessing](/studio/projects/processing-blocks) and [learning blocks](/studio/projects/learning-blocks) to the pipeline.

* Edge Impulse Studio will automatically add an [input block](/studio/projects/impulse-design#input-block) and it will recommend a suitable preprocessing and a learning block based on the data type. I have used the recommended ones in this project with the default arguments.

<Frame caption="Impulse Design">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/ti-cc1352p-getting-started/impulse-design.jpg?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=77220c063f096ec695b4a970bb1065bf" width="1256" height="889" data-path=".assets/images/ti-cc1352p-getting-started/impulse-design.jpg" />
</Frame>

* After Impulse design is complete, save the design and navigate to the preprocessing tab (Spectral features in this case) for the feature generation.

<Frame caption="Preprocessing Block">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/ti-cc1352p-getting-started/feature-generation.jpg?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=518b9d746723aad6aacea47005feb682" width="890" height="960" data-path=".assets/images/ti-cc1352p-getting-started/feature-generation.jpg" />
</Frame>

Click on the *Save parameters* button, then navigate to the *Generate features* tab and click *Generate features* button for data preprocessing.

<Frame caption="Feature Generation">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/ti-cc1352p-getting-started/feature-generation-2.jpg?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=bc672d9f7797a613c355dd4e8d1fd67f" width="987" height="931" data-path=".assets/images/ti-cc1352p-getting-started/feature-generation-2.jpg" />
</Frame>

* After feature generation, please navigate to the *Learning Tab* ([Classifier](/studio/projects/learning-blocks/blocks/classification) in this case) to design the neural network architecture. I have used the default architecture and parameters recommended by the Edge Impulse Studio. After selecting a suitable configuration, click on the *Start training* button.

<Frame caption="Train a Classifier Model">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/ti-cc1352p-getting-started/classifier-design.jpg?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=10e368b99ab5f98802774c0744fce244" width="1228" height="904" data-path=".assets/images/ti-cc1352p-getting-started/classifier-design.jpg" />
</Frame>

* Once the training is complete, please navigate to the [Model testing](/studio/projects/model-testing) tab, and click *Classify all* button.

<Frame caption="Model Testing">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/ti-cc1352p-getting-started/model-testing.jpg?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=44c470a5e520c1904903e6a1fb5afbba" width="942" height="960" data-path=".assets/images/ti-cc1352p-getting-started/model-testing.jpg" />
</Frame>

After testing is finished, the Edge Impulse Studio will show the model accuracy, and other parameters.

> Even though it is a simple example, the Edge Impulse Studio prepared an excellent machine learning model just by using the default recommended parameters, in just a couple of minutes.

## Deployment

In this step, we will deploy our prepared model to the TI LAUNCHXL-CC1352P development board, so we can perform inference locally on the board.

* Please navigate to the [Deployment](/studio/projects/deployment) tab, select the TI LAUNCHXL-CC1352P board using the search bar, and click on the *Build* button.

<Frame caption="Deployment Tab">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/ti-cc1352p-getting-started/deployment.jpg?fit=max&auto=format&n=cesvU2DH4iEXAkgD&q=85&s=88423688255cb5aa0d657b562c804f40" width="941" height="960" data-path=".assets/images/ti-cc1352p-getting-started/deployment.jpg" />
</Frame>

* After the *build* is finished, the new firmware will be downloaded automatically to your computer, and the Edge Impulse Studio will provide next-step instructions.
* Please extract the folder and double-click the `flash_<operating-system>` file. This will flash the newly created firmware on the TI LAUNCHXL-CC1352P board. This firmware contains the machine learning model we prepared in the above steps.

<Frame caption="Flashing Firmware">
  <img src="https://mintcdn.com/edgeimpulse/cesvU2DH4iEXAkgD/.assets/images/ti-cc1352p-getting-started/flashing.gif?s=18e4f9197a3fc44e6d9e9ea24f461e3a" width="1470" height="1102" data-path=".assets/images/ti-cc1352p-getting-started/flashing.gif" />
</Frame>

## Inferencing

The next step is testing!! Let's see how well our model performs when run locally on the LAUNCHXL-CC1352P board. To start local inferencing, type `edge-impulse-run-impulse` from your terminal or command prompt.

<iframe src="https://www.youtube.com/embed/vIbTSwSMsXY" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

And, that's it. I hope this Getting Started Guide will be useful for you when using the TI LAUNCHXL-CC1352P with Edge Impulse.

If you have any questions, please check out the [Edge Impulse Forum](https://forum.edgeimpulse.com/).


Built with [Mintlify](https://mintlify.com).