# Source: https://docs.edgeimpulse.com/projects/expert-network/silabs-xg24-posture-detection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Porting a Posture Detection Project from the SiLabs Thunderboard Sense 2 to xG24

Created By: Salman Faris

Public Project: [https://studio.edgeimpulse.com/public/188507/latest](https://studio.edgeimpulse.com/public/188507/latest)

## Introduction

In this project I'm going to walkthrough how to port an existing project developed on the SiLabs Thunderboard Sense 2, to SiLabs' newer and more powerful xG24 development board.

The original project was developed by [Manivnnan Sivan](https://www.hackster.io/manivannan) to detect correct / incorrect posture of manufacturing workers using a wearable belt.

<Frame caption="Image from original project">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/device_data-acquisition.jpeg?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=40dee306d110fa46069cd8f4113c9175" width="805" height="1000" data-path=".assets/images/silabs-xg24-posture-detection/device_data-acquisition.jpeg" />
</Frame>

I will walk you through how you can clone his Public Edge Impulse project, deploy to a SiLabs Thunderboard Sense 2, test it out, and then build and deploy to the newer SiLabs xG24 device instead.

## About the project : Posture Detection for Worker Safety

You can find more about the project here in the original project documentation, [Worker Safety Posture Detection](/projects/expert-network/posture-detection-for-worker-safety-silabs-thunderboard-sense-2).

The project is intended to help workers in manufacturing. They work in conditions that can put a lot of stress on their bodies. Depending on the worker's role in the production process, they might experience issues related to cramped working conditions, heavy lifting, or repetitive stress.

Poor posture can cause problems for the health of those who work in manufacturing. Along with that, research suggests that making efforts to improve posture among manufacturing employees can lead to significant increases in production. Workers can improve their posture by physical therapy, or simply by being more mindful during their work day.

[Manivnnan Sivan](https://www.hackster.io/manivannan) has created a wearable device using a SiLabs Thunderboard Sense 2 which can be fitted to a worker's waist. The worker can do their normal activities, and the TinyML model running on the hardware will predict the posture and communicate to the worker through BLE communication. The worker can get notified in the Light Blue App on their phone or smartwatch.

## Running the Project on Thunderboard Sense 2

Before porting, we need to run the project on the existing platform to understand how it's run and familiarize ourselves with it's parameters. So let's get started.

### Installing Dependencies

Before you proceed further, there are few other software packages you need to install.

* Edge Impulse CLI - Follow [this link](/tools/clis/edge-impulse-cli/installation) to install necessary tooling to interact with the Edge Impulse Studio.
* LightBlue - This is a mobile application. Install from either Apple Store or Android / Google Play. This will be required to connect the board wirelessly over Bluetooth. The Android version can be found [here](https://play.google.com/store/apps/details?id=com.punchthrough.lightblueexplorer\&hl=en_IN\&gl=US\&pli=1). Apple / iOS users can download the App [here](https://apps.apple.com/us/app/lightblue/id557428110).

### Clone the Project

Go to the Edge Impulse project page using the [link here](https://studio.edgeimpulse.com/public/148375/latest), and clone it.

Click **Clone** on the right corner button to create a copy of the project.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/clone-step1.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=47d118e827f655b90d478b4db9e388a2" width="1600" height="633" data-path=".assets/images/silabs-xg24-posture-detection/clone-step1.png" />
</Frame>

Provide a project name in the text field, and click on the **Clone project** button.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/clone-step2.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=e0862e65697b6acfa4c30c1a7601a44a" width="1600" height="897" data-path=".assets/images/silabs-xg24-posture-detection/clone-step2.png" />
</Frame>

Done, the project is successfully cloned into your Edge Impulse account:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/clone-step3.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=235bb7a25886c14983b70ba4fe9fd01c" width="1600" height="757" data-path=".assets/images/silabs-xg24-posture-detection/clone-step3.png" />
</Frame>

As we clone the project, it will be loaded with the dataset collected by Manivannan.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/clone-step4.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=0601cb2d751aa974ea369974a6ae4f9b" width="1600" height="674" data-path=".assets/images/silabs-xg24-posture-detection/clone-step4.png" />
</Frame>

### Run the Project

We can try to deploy the project on a Thunderboard Sense 2:

1. **Connect the development board to your computer** : Use a micro-USB cable to connect the development board to your computer. The development board should mount as a USB mass-storage device (like a USB flash drive), with the name `TB004`. Make sure you can see this drive.
2. **Update the firmware** : The development board does not come with the right firmware yet. To update the firmware:

   2.1 [Download the latest Edge Impulse firmware.](https://cdn.edgeimpulse.com/firmware/silabs-thunderboard-sense2.bin)

   2.2 Drag the `silabs-thunderboard-sense2.bin` file to the TB004 drive.

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-posture-detection/2023-06-11_16-13.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=c3c6c84b07308fd4517d7f0346b0d7ef" width="1164" height="778" data-path=".assets/images/silabs-xg24-posture-detection/2023-06-11_16-13.png" />
   </Frame>

   2.3 Wait 30 seconds.

Next, open the CLI and run `edgeimpulse-daemon`

From here, Log in with your Edge Impulse credentials and choose the cloned project from the followed project list.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-posture-detection/EIdaemon.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=131f2f3e1762a07486141b069256857e" width="1145" height="1000" data-path=".assets/images/silabs-xg24-posture-detection/EIdaemon.png" />
</Frame>

Then provide a name for the device that is connected to the computer.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-posture-detection/EIdaemon2.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=53b67423f58f25d0cd616c78c61a3bd6" width="1600" height="278" data-path=".assets/images/silabs-xg24-posture-detection/EIdaemon2.png" />
</Frame>

After completing these steps, you will see that the device is connected to the Edge Impulse Studio via the CLI.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/edgeimpulse_connect.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=29d29549435a13fb80de53e4ea95368c" width="1600" height="428" data-path=".assets/images/silabs-xg24-posture-detection/edgeimpulse_connect.png" />
</Frame>

### Build & Deploy the Project

Choose "Deployment" from the left toolbar and then choose the target device as "SiLabs Thunderboard Sense 2", and click "Build" to start the process.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/projectBuild.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=7723ade35c2349a40b8297e10f19fc44" width="1161" height="1000" data-path=".assets/images/silabs-xg24-posture-detection/projectBuild.png" />
</Frame>

After the build completes, a `.bin` file will be automatically generated and downloaded. You need to drag and drop it to the Thunderboard Sense 2 device drive.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-posture-detection/FlashfirmwareDnD.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=389f6ea820cb7b5e6c4b8fe1966b8ab1" width="1600" height="484" data-path=".assets/images/silabs-xg24-posture-detection/FlashfirmwareDnD.png" />
</Frame>

Done, we can now open the LightBlue mobile app to run and see the inference:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/runonSense2.jpg?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=fce69d27ec9ab0fa106dabef3f10fd0e" width="511" height="1000" data-path=".assets/images/silabs-xg24-posture-detection/runonSense2.jpg" />
</Frame>

Alternatively you can run it on a computer, if you don't have access to a phone. Run the command below to see if the tinyML model is inferencing.

`edge-impulse-run-impulse`

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/runonSense2-1.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=b46382be387baf3670686faa268d6a71" width="1300" height="1000" data-path=".assets/images/silabs-xg24-posture-detection/runonSense2-1.png" />
</Frame>

Nice, so far we cloned and implemented the project. Now we are going to port to the new board!

## The New SiLabs EFR32MG24

SiLabs have launched the new EFR32MG24 also known as xG24 Wireless SoCs and they are full of interesting sensors and features making them very good for mesh IoT wireless connectivity using Matter, OpenThread, and Zigbee protocols for smart home, lighting, and building automation products or any other use case you see fit to this combination of sensors and connectivity.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/efr32xg24-dev-kit-layout.jpeg?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=26eb9bcc494ad8e7b3202941088616f5" width="640" height="384" data-path=".assets/images/silabs-xg24-posture-detection/efr32xg24-dev-kit-layout.jpeg" />
</Frame>

The sensors present onboard are an accelerometer, a microphone, environmental sensors comprising temperature, humidity, and air pressure, a Hall sensor, an inertial and an interactional sensor.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/heroshot.jpeg?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=4591c20e6fcb29fddd4a198f310fb554" width="1438" height="1000" data-path=".assets/images/silabs-xg24-posture-detection/heroshot.jpeg" />
</Frame>

## Collect More Data Using the xG24

Compared to the Thunderboard Sense 2, the xG24 does have some changes while connecting to Edge Impulse and uploading the firmware.

1. First - [Download the base firmware image](https://cdn.edgeimpulse.com/firmware/silabs-xg24.zip) - Download the latest Edge Impulse firmware, and unzip the file. Once downloaded, unzip it to obtain the firmware-xg24.hex file, which we will be using in the following steps.
2. **Connect the xG24 Dev Kit to your computer** - Use a micro-USB cable to connect the xG24 Dev Kit to your development computer, and download and install [Simplicity Commander](https://community.silabs.com/s/article/simplicity-commander).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-posture-detection/ConnectG24.webp?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=fe502bcd569f71c22209fe1f2c528845" width="205" height="476" data-path=".assets/images/silabs-xg24-posture-detection/ConnectG24.webp" />
</Frame>

3. **Load the base firmware image with Simplicity Commander** - You can use [Simplicity Commander](https://community.silabs.com/s/article/simplicity-commander) to flash your xG24 Dev Kit with the Edge Impulse [base firmware image](https://cdn.edgeimpulse.com/firmware/silabs-xg24.zip). To do this, first select your board from the dropdown list on the top left corner:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/xg24-dk-commander-select-board.webp?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=d9754f2c1defce6abbc7388b6af6b4b5" width="630" height="227" data-path=".assets/images/silabs-xg24-posture-detection/xg24-dk-commander-select-board.webp" />
</Frame>

Then go to the "Flash" section on the left sidebar, and select the base firmware image file you downloaded in the first step above (i.e., the file named `firmware-xg24.hex`). You can now press the Flash button to load the base firmware image onto the xG24 Dev Kit.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/g24-dk-commander-flash.webp?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=da8f89a125ec565657f0a4fda731ab87" width="996" height="960" data-path=".assets/images/silabs-xg24-posture-detection/g24-dk-commander-flash.webp" />
</Frame>

After this, we can follow the usual method on how we select the device in the Edge Impulse Studio via the CLI.

Next, open the CLI and run `edgeimpulse-daemon`

From here, log in with your Edge Impulse credentials and choose the cloned project from the project list that follows.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7mPJdRN3Ay8aD8d6/.assets/images/silabs-xg24-posture-detection/EIdaemon.png?fit=max&auto=format&n=7mPJdRN3Ay8aD8d6&q=85&s=131f2f3e1762a07486141b069256857e" width="1145" height="1000" data-path=".assets/images/silabs-xg24-posture-detection/EIdaemon.png" />
</Frame>

Then provide a name for the device that is connected to the computer.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/xG24_connection.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=78a4a6684cea7ecd4b334a9c7bf60586" width="1600" height="193" data-path=".assets/images/silabs-xg24-posture-detection/xG24_connection.png" />
</Frame>

After doing these steps, you can see the device is connected to the Edge Impulse Studio via the CLI.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/xG24_device.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=89f69fed89361318d1c3a2e30cf128c1" width="1600" height="355" data-path=".assets/images/silabs-xg24-posture-detection/xG24_device.png" />
</Frame>

I collected a bit of additional data using the xG24, and it looks good.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/xG24_DataCollection.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=c4c906bd11dd2f3dd12bad1eb3775909" width="1559" height="1000" data-path=".assets/images/silabs-xg24-posture-detection/xG24_DataCollection.png" />
</Frame>

Now, we need to retrain the data set, but before that we need to set the target as **SiLabs EFR32MG24**.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/xG24Training.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=0cb2987cea57e7b75d4a4e762eb86a75" width="1600" height="853" data-path=".assets/images/silabs-xg24-posture-detection/xG24Training.png" />
</Frame>

Great, we got nice accuracy in model training.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/xG24_F1Score.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=6ec71afddf55bab93a3dde4700b1fc69" width="1370" height="884" data-path=".assets/images/silabs-xg24-posture-detection/xG24_F1Score.png" />
</Frame>

Now, we can build the model and deploy to the xG24. For the build, we need to choose the correct device first, then click "Build".

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/xG24BuildModel.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=b96ef53be4dd099dcc6c624898c0b6f9" width="1251" height="1000" data-path=".assets/images/silabs-xg24-posture-detection/xG24BuildModel.png" />
</Frame>

After generating the `.bin` file, we need to use [Simplicity Commander](https://community.silabs.com/s/article/simplicity-commander) to flash your xG24 Dev Kit with this firmware. To do this, first select your board from the dropdown list on the top left corner:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/xg24-dk-commander-select-board.webp?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=d9754f2c1defce6abbc7388b6af6b4b5" width="630" height="227" data-path=".assets/images/silabs-xg24-posture-detection/xg24-dk-commander-select-board.webp" />
</Frame>

Then go to the "Flash" section on the left sidebar, and select the generated firmware image file you downloaded after the build process. You can now press the Flash button to load the generated .hex file firmware image onto the xG24 Dev Kit.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/g24-dk-commander-flash.webp?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=da8f89a125ec565657f0a4fda731ab87" width="996" height="960" data-path=".assets/images/silabs-xg24-posture-detection/g24-dk-commander-flash.webp" />
</Frame>

Next, we can use the LightBlue mobile app to run and see the inference.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/xG24App.jpg?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=789701d79749677f09f7002ab30a4325" width="551" height="1000" data-path=".assets/images/silabs-xg24-posture-detection/xG24App.jpg" />
</Frame>

Alternatively, we can run on computer as we did for the Thunderboard Sense 2, if you don't have access to a phone. Run the command below to see if the tinyML model is inferencing.

`edge-impulse-run-impulse`

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/xg24_inference.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=1513214e995abb1b19175919b80e472a" width="1267" height="1000" data-path=".assets/images/silabs-xg24-posture-detection/xg24_inference.png" />
</Frame>

Awesome, we have now successfully ported a project from Thunderboard Sense 2 to the xG24 Dev Kit!

## Conclusion

We can see here, the xG24 does a faster classification of these tinyML datasets without compromising the accuracy.

Here you can see the comparison data, and we can see **91.1765%** increased inferencing speed in the NN Classifier, while the RAM and Flash usage are the same.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/model-optimization_time.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=223fca6d79fd4f2d0c6e2a65a30056e6" width="1600" height="670" data-path=".assets/images/silabs-xg24-posture-detection/model-optimization_time.png" />
</Frame>

Similar results are achieved in the field data when we are inferencing the live data stream. Here we can see a 92.3077% increase in speed in the classification, which is more than what was calculated in the model optimization.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/SJuUZPVSKyEIozfi/.assets/images/silabs-xg24-posture-detection/InferenceTime.png?fit=max&auto=format&n=SJuUZPVSKyEIozfi&q=85&s=5fa50b8e56758832c2cfd7cf5a867373" width="1600" height="656" data-path=".assets/images/silabs-xg24-posture-detection/InferenceTime.png" />
</Frame>

To conclude the porting project post, we can confirm that it's worth to upgrade products and projects using the Thunderboard Sense 2 to the new and efficient SiLabs xG24 Dev Kit.


Built with [Mintlify](https://mintlify.com).