# Source: https://docs.edgeimpulse.com/projects/expert-network/getting-started-nvidia-tao-renesas-ekra8d1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with the Edge Impulse Nvidia TAO Pipeline - Renesas EK-RA8D1

Created By: Peter Ing

Public Project Link: [https://studio.edgeimpulse.com/public/568291/latest](https://studio.edgeimpulse.com/public/568291/latest)

## Introduction

The Renesas RA8 series is the first product to implement the Arm Cortex-M85, a high-performance MCU core tailored for advanced AI and machine learning at the edge. Featuring Arm Helium technology and enhanced ML instructions, it delivers up to 4x the ML performance of earlier M-series cores. With high clock speeds, energy efficiency, and TrustZone security, it's ideal for tasks like speech recognition, anomaly detection, and image classification on embedded devices.

Edge Impulse includes support for Nvidia TAO transfer learning and deployment of Nvidia Model Zoo models to the Renesas RA8D1.

This project provides a walkthrough of how to use the Renesas EK-RA8D1 Development kit with Edge Impulse using an Nvidia TAO-enabled backend to train Nvidia Model Zoo models for deployment onto the EK-RA8D1. By integrating the EK-RA8D1 with Edge Impulse's Nvidia TAO training pipeline, you can explore advanced machine learning applications and leverage the latest features in model experimentation and deployment.

## Hardware

Renesas EK-RA8D1 - [Evaluation Kit for RA8D1 MCU Group](https://www.renesas.com/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ek-ra8d1-evaluation-kit-ra8d1-mcu-group?srsltid=AfmBOoovp-039RtY9ng5rk2nFEVNOQuruTXKineI1JmVl9tDr64N7Ao2)

## Platform

Edge Impulse [Visit](https://edgeimpulse.com)

## Software

Edge Impulse CLI [Install](/tools/clis/edge-impulse-cli/installation) JLink Flashing Tools [Download](https://www.segger.com/downloads/jlink) Edge Impulse Firmware for EK-RA8D1 [Download](https://cdn.edgeimpulse.com/firmware/renesas-ek-ra8d1.zip)

## Getting Started

### Renesas EK-RA8D1

Renesas supports developers building on the RA8 with various kits, including the EK-RA8D1, a comprehensive evaluation board that simplifies prototyping.

As part of the Renesas Advanced (RA) series of MCU evaluation kits, the EK-RA8D1 features the RA8 Cortex-M85 MCU which is the latest high-end MCU from Arm, superseding the Cortex M7. The Cortex M85 is a high-performance MCU core designed for advanced embedded and edge AI applications. It offers up to 4x the ML performance of earlier Cortex-M cores, powered by Arm Helium technology for accelerated DSP and ML tasks.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/ekra8d1.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=f7ce2e7efc1ec4229ad9913b58d3e178" width="936" height="680" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/ekra8d1.jpg" />
</Frame>

The Renesas EK-RA8D1 evaluation kit is a versatile platform designed for embedded and AI application development. It features USB Full-Speed host and device support with 5V input via USB or external power supply, along with onboard debugging through Segger J-Link® and support for ETM, SWD, and JTAG interfaces. Developers can utilize 3 user LEDs, 2 buttons, and multiple connectivity options, including Seeed Grove® (I2C & analog), Digilent Pmod™ (SPI & UART), Arduino™ UNO R3 headers, MikroElektronika™ mikroBUS, and SparkFun® Qwiic® (I2C). An MCU boot configuration jumper further enhances flexibility, making the EK-RA8D1 ideal for rapid prototyping and testing.

The kit also features a camera and full color LCD display, making it ideal for the development and deployment of edge AI solutions allowing on-device inference results to be rendered to the onboard LCD.

The EK-RA8D1 is an officially supported target in Edge Impulse, which means it can be used to collect data directly into Edge Impulse. Follow [this guide](/hardware/boards/renesas-ek-ra8d1) to enable the EK-RA8D1 to connect to a project.

## Edge Impulse and Nvidia TAO

### Create Edge Impulse Project

To get started, create a project and be sure to use an Enterprise plan as the Nvidia TAO training pipeline requires an Enterprise plan. For more info on the options, see the [plans and pricing](https://edgeimpulse.com/pricing).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/new-project.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=228013d3e55bf2d1527cc61edf503464" width="1431" height="712" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/new-project.jpg" />
</Frame>

### Connect your Device

There two ways to connect the board, either using the Edge Impulse CLI or directly from within the Studio UI. To access via the CLI run the command `edge-impulse-daemon` and provide login credentials, then select the appropriate Studio project to connect your board.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/cli-connect.jpg?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=51e946119d2182db2b6583d35c4bf13c" width="1600" height="657" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/cli-connect.jpg" />
</Frame>

Alternatively, clicking the *Data acquisition* menu item in the left navigation bar presents the data collection page. Select **320x240** to get the maximum resolution out of the camera on the EK-RA8D1 when capturing samples.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/data-acquisition.jpg?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=aa350a1fdb91672f801a57f9073b6cd6" width="1430" height="668" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/data-acquisition.jpg" />
</Frame>

Edge Impulse will ask you if the project is object detection project. Select 'No' to configure the project as an Image classification project when using image data.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/project-type.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=03a52836aa63073c50599f53a6975616" width="1428" height="653" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/project-type.jpg" />
</Frame>

Alternatively, go the Dashboard page by clicking *Dashboard* on the left navigation and select **One label per data item** from the Labeling method dropdown.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/project-type-2.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=a48a31c00390324075edc6e9e879eda1" width="1427" height="714" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/project-type-2.jpg" />
</Frame>

Capture sample images by presenting objects to the camera that you wish to identify, and click the **Start sampling** button to capture a full color image from the board.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/data-1.jpg?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=84467c77269276c4be4dc18ff900696d" width="1424" height="712" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/data-1.jpg" />
</Frame>

Different types or classes of object can be captured, and these can be added by changing the label string in the **Label** text box. For example, a class called `needle_sealed` is created by setting the label to this name and then capturing pictures of sealed needles.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/data-2.jpg?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=9f0c90f9d9829b30eed81a4c6ee357df" width="1424" height="707" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/data-2.jpg" />
</Frame>

Once all images are annotated you should balance your data so that you split your dataset between a Training and Test set. This is done by selecting *Dashboard* from the navigation menu on the left and then scrolling down to find and click the **Perform train / test split** button. Edge Impulse will try to get as close to an 80/20 split as possible depending on the size of your dataset.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/split-1.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=1caa2063627731d965edbf0fdb4a7a73" width="1429" height="713" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/split-1.jpg" />
</Frame>

The data split can be seen at the top of the *Data acquisition* page where you can not only see the split of data items collected by label as a pie chart, but also the resulting split under the TRAIN / TEST SPLIT element.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/split-2.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=9027f6ef0698768fa9b0fcd2f2101aa5" width="934" height="286" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/split-2.jpg" />
</Frame>

### Create Impulse

The next step is to create a new Impulse which is accessed from the Create Impulse menu. Select the **Renesas RA8D1 (Cortex M85 480Mhz)** as the target, doing so automatically targets the EK-RA8D1 which is the RA8D1 based board supported by Edge Impulse.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/target-device.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=0f0da3c48d593b672b359efba614ca71" width="1427" height="712" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/target-device.jpg" />
</Frame>

Set the image width and height to 224px x 224px to match the pretrained backbone dimensions in Nvidia TAO Model Zoo:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/impulse-1.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=dfdd07f2920b248ccaee4ef4830065ab" width="1426" height="705" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/impulse-1.jpg" />
</Frame>

### Feature Generation

Classification requires an Image processing block; this is added by clicking **Add a processing block** and then selecting **Image** from the options presented.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/impulse-2.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=d1ca7cfc0fa76c30ac9b0d6e8361d66d" width="1423" height="706" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/impulse-2.jpg" />
</Frame>

Once the Image processing block is added the Transfer Learning Block needs be added by selecting **Add a learning block** and then choosing the first option, **Transfer Learning (Images)**. Nvidia TAO is based on transfer learning so selecting this block is the first step towards activating the Nvidia TAO classification pipeline in the backend.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/impulse-3.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=b819697743a6d23dea0978ed4e0186ee" width="1430" height="704" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/impulse-3.jpg" />
</Frame>

The resulting Impulse should look as follows before proceeding.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/impulse-4.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=814eba71b7958932e2aee3529a8edd6b" width="1427" height="712" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/impulse-4.jpg" />
</Frame>

The next step is to generate the raw features that will be used to train the model. First click **Save Impulse** then select the *Image* submenu from the Impulse Design menu in the left hand navigation to access the settings of the Image processing block.

In the **Parameters** tab, leave the color depth as RGB as the TAO Models use 3 channel RGB models:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/features-1.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=abc200f1fa048090d203556e0cc5eefb" width="1430" height="704" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/features-1.jpg" />
</Frame>

Under the **Generate features** tab simply click the **Generate features** button to create the scaled down 224x224 images that will be used by TAO to train and validate the model.

The process will take a few seconds to minutes depending on the dataset size. Once done the results of the job are shown and the reduced images are stored in the backend as features to be passed to the model during training and validation.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/features-2.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=08817a1a80027edd5809474477b3372a" width="1430" height="708" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/features-2.jpg" />
</Frame>

### Nvidia TAO Classification

Once the image features are done, a green dot appears next to Images in the Impulse design navigation. The Transfer Learning submenu is then activated, and can be accessed by clicking **Transfer learning** in the navigation pane under Impulse design, this takes you to the configuration area of the learning block.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-1.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=38d605a186a939f26ce923f8f671f166" width="1428" height="715" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-1.jpg" />
</Frame>

To activate Nvidia TAO in the project the default MobileNetV2 model architecture needs to be deleted, by clicking the Delete model (trash can) icon on the lower right corner of the model.

Once this is done you will see there is no model architecture activated for the project, and a button titled "Choose a different model" will be shown in place of the deleted MobileNet model.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-2.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=86387352deff8756748448823409f1fb" width="1426" height="712" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-2.jpg" />
</Frame>

Clicking the "Choose a different model" button will present a list of model architectures available in Edge Impulse. Since the project is configured as Classification, only classification model architectures are available. To access the Nvidia TAO Classification Model scroll down to the bottom.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-3.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=f40b4a7517f83135f9d9fd8e12da1253" width="1424" height="709" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-3.jpg" />
</Frame>

The Nvidia TAO models are only available under Enterprise plans as shown by the labels. For this project we are going to use **Nvidia TAO Image Classification**. Selecting any of the Nvidia TAO models like this activates the Nvidia TAO training environment automatically behind the scenes in the project.

### Training

Once the Nvidia TAO Classification model is selected all the relevant hyperparameters are exposed by the GUI. The default training settings are under the *Training settings* menu and the *Advanced training settings* menu can be expanded to show the full set of parameters specific to TAO.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-4.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=97d4a645f455cc969f8c44365f9542ca" width="1424" height="711" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-4.jpg" />
</Frame>

All of the relevant settings available in TAO including Data augmentation and backbone selection are available from the GUI. The data augmentation features of TAO can be accessed by expanding the *Augmentation settings* menu. Backbone selection is accessed from the *Backbone* dropdown menu and for this project we will be using the **MobileNet v2 (800K params)** backbone.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-6.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=d338bfb684f4098c406ee5422707911b" width="1426" height="708" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-6.jpg" />
</Frame>

It's also essential to select **GPU** for training as TAO only trains on GPU's. Also set the number of training cycles (epochs) to a higher number than the default. Here we start with 300.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-7.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=5082b79dd67b2520139fbae4f0d5c4fd" width="1424" height="708" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-7.jpg" />
</Frame>

All that's left to do is click the **Save and train** button to commence training. This can take from 1 to several hours depending upon the dataset size and other factors such as backbone, etc.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-8.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=bd284e5c1031cf735f8474f3d33e0fc8" width="936" height="554" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-8.jpg" />
</Frame>

Once training is completed, the results are shown:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-9.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=8d708dd9f184a26393f173327c418867" width="1426" height="709" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/training-9.jpg" />
</Frame>

The accuracy and confusion matrix, latency and memory usage are shown for both Unoptimized (float32) and Quantized (int8) models, which can be used with the EK-RA8AD1. Take note of the **PEAK RAM USAGE** and **FLASH USAGE** statistics at the bottom. These indicate if the model will fit within RAM and ROM on the target.

### Model Testing

Before deploying the model to the development kit, the model can first be tested by accessing the *Live classification* menu on the left navigation. Clicking the **Classify all** button runs the Test dataset through the model, and shows the results on the right:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/testing-1.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=9582daeba6f98cea228d60b1671a89f1" width="1426" height="712" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/testing-1.jpg" />
</Frame>

The results are visible in the right side of the window, and can give a good indication of the model performance against the captured dataset.

The Model testing page also allows you to perform realtime classification using uploaded files, by selecting a file from the **Classify existing test sample** dropdown menu and clicking the **Load sample** button.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/testing-2.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=ed38384bc431c5d6e5a2c8f29a63f090" width="1425" height="708" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/testing-2.jpg" />
</Frame>

The results shown when doing this are from the classification being performed in Edge Impulse, not on the device.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/testing-3.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=f3e8ae8456b6d1477efc89ef9ce6d531" width="1427" height="713" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/testing-3.jpg" />
</Frame>

If you wish to test the camera on the EK-RA8D1 but still run the model in Edge Impulse, you can connect the camera using the `edge-impulse-daemon` CLI command to connect the camera just as you would when you perform data acquisition.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/testing-4.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=1854fe1bdfba1544ab76ccf6663cd260" width="1424" height="712" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/testing-4.jpg" />
</Frame>

You can iteratively improve the model by capturing more data and choosing the Retrain model sub menu item which takes you to the retrain page where you can simply click the Train model button to retrain the model with the existing hyperparameters.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/testing-5.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=9ce73c696aff27ca05b88c4c08f1b575" width="1426" height="703" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/testing-5.jpg" />
</Frame>

## Deployment

To test the model directly on the EK-RA8D1, go to the *Deployment* page by clicking the Deployment sub menu item in the left navigation. In the search box type *Renesas*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/deployment-1.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=59e9ffb47b7b1d2f120f6d7e61a3a47b" width="1424" height="712" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/deployment-1.jpg" />
</Frame>

The drop down menu will filter out all the other supported boards and give you two options for the EK-RA8D1. The RA8D1 MCU itself has 2Mb of FLASH for code storage and 1Mb of RAM integrated. The EK-RA8D1 development kit adds 64Mb of external SDRAM and 64Mb of external QSPI FLASH to support bigger models.

The **Quantized (int8)** model should be selected by default and the RAM and ROM usage is shown, which is what you would have seen in the training page when training completed.

* Renesas EK-RA8D1 target – This builds a binary for when RAM and ROM usage fit within the RA8D1 MCU's integrated RAM and FLASH memory.
* Renesas EK-RA8D1 SDRAM target – This builds a binary that loads the model into the external SDRAM when the model is over 1Mb. (Note there is a slight performance penalty as the external RAM has to be accessed over a memory bus and is also SDRAM vs the internal SRAM)

When you click the **Build** button Edge Impulse builds the project and generates a `.zip` archive containing the prebuilt binary and supporting files, which downloads automatically when completed.

This archive contains the same files as the Edge Impulse firmware you would have downloaded when following this guide at the begging of the project when you were connecting your board for the first time. The only difference is that the firmware (.hex) now contains your model vs the default model.

To flash the new firmware to your board, replace the contents of the folder where you have the firmware with the contents of the downloaded archive.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/deployment-2.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=b7a352abdfda1f4d4799b1703c2c252d" width="516" height="286" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/deployment-2.jpg" />
</Frame>

Note, you need to make sure you have connected the USB cable to the JLink port (J10).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/deployment-3.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=b30b21d6a4161147f0f627a462f82de2" width="684" height="1000" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/deployment-3.jpg" />
</Frame>

Run the appropriate command to flash the firmware to the board.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/deployment-4.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=ff10da9855865c76775ec41f79559ed0" width="1218" height="601" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/deployment-4.jpg" />
</Frame>

To test the performance of the image classification on the board and see inference latency and DSP processing time, connect the USB cable to J11.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/deployment-5.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=222ede633eb6b3d63bfd380fd0cee732" width="743" height="1000" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/deployment-5.jpg" />
</Frame>

Then run the `edge-impulse-run-impulse` CLI command:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/j0k3ldYt05ndiX05/.assets/images/getting-started-nvidia-tao-renesas-ekra8d1/results.jpg?fit=max&auto=format&n=j0k3ldYt05ndiX05&q=85&s=1178b3c29947a9080a4809e8afb3ca28" width="979" height="512" data-path=".assets/images/getting-started-nvidia-tao-renesas-ekra8d1/results.jpg" />
</Frame>

The inference execution time and results are then shown in the CLI.

## Conclusion

In this guide we have covered the step by step process of using Edge Impulse's seamless integration of Nvidia's TAO transfer learning image classification model from Nvidia’s model zoo, and how to deploy the model to the Renesas EK-RA8D1 Arm Cortex-M85 MCU development kit. In this way we have shown how Edge Impulse makes it possible to use Nvidia image classification models on an Arm Cortex-M85 MCU.


Built with [Mintlify](https://mintlify.com).