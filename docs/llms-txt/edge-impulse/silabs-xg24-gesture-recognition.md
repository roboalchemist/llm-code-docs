# Source: https://docs.edgeimpulse.com/projects/expert-network/silabs-xg24-gesture-recognition.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Porting a Gesture Recognition Project from the SiLabs Thunderboard Sense 2 to xG24

Created By: Mithun Das

Public Project (to Clone): [https://studio.edgeimpulse.com/public/147925/latest](https://studio.edgeimpulse.com/public/147925/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/intro.jpg?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=a46dccba8db1de51302f858b88af7aaf" width="1333" height="1000" data-path=".assets/images/gesture-recognition-on-silabs-xg24/intro.jpg" />
</Frame>

## Intro

In this project I am not going to explore or research a new TinyML use-case, rather I'll focus on how we can reuse or extend Edge Impulse Public projects for a different microcontroller.

[Manivannan Sivan](https://www.hackster.io/manivannan) had created a project [Gesture Recognition for Patient Communication](/projects/expert-network/gesture-recognition-patient-communication-silabs-thunderboard-sense-2) which is a wearable device running a tinyML model to recognize gesture patterns and send a signal to a mobile application via BLE. Check out his work for more information.

In this project, I am going to walk you through how you can clone his Public Edge Impulse project, deploy to a SiLabs Thunderboard Sense 2 first, test it out, and then build and deploy to the newer SiLabs xG24 device instead.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/wearable.jpg?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=70fdaa8a45e3648d1157ff4f89875bb5" width="1278" height="1000" data-path=".assets/images/gesture-recognition-on-silabs-xg24/wearable.jpg" />
</Frame>

## Installing Dependencies

Before you proceed further, there are few other software packages you need to install.

* Edge Impulse CLI - Follow [this link](/tools/clis/edge-impulse-cli/installation) to install necessary tooling to interact with the Edge Impulse Studio.
* Simplicity Studio 5 - Follow [this link](https://www.silabs.com/developers/simplicity-studio) to install the IDE
* Simplicity Commander - Follow [this link](https://community.silabs.com/s/article/simplicity-commander?language=en_US) to install the software. This will be required to flash firmware to the xG24 board.
* LightBlue - This is a mobile application. Install from either Apple Store or Android / Google Play. This will be required to connect the board wirelessly over Bluetooth.

## Clone And Build

If you don't have an Edge Impulse account, signup for free and log into [Edge Impulse](https://studio.edgeimpulse.com/). Then visit the below [Public Project](/studio/projects/dashboard#1-showcasing-your-public-projects-with-markdown-readmes) to get started.

[https://studio.edgeimpulse.com/public/147925/latest](https://studio.edgeimpulse.com/public/147925/latest)

Click on the "Clone" button at top-right corner of the page.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/studio.png?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=f2a47f193a1bb24c03cfd44e2e015eb6" width="1600" height="934" data-path=".assets/images/gesture-recognition-on-silabs-xg24/studio.png" />
</Frame>

That will bring you to the below popup modal. Enter a name for your project, and click on the "Clone project" button.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/clone.png?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=6b152255f2cba39b75176d6ecbdbb871" width="1084" height="960" data-path=".assets/images/gesture-recognition-on-silabs-xg24/clone.png" />
</Frame>

The project will be duplicated from Mani, into your own Edge Impulse Studio. You can verify by looking at the project name you entered earlier. Now if you navigate to "Create impulse" from the left menu, you will see how the model was created originally.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/create-impulse.png?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=1f8a6f98ec37c56516e34b074ca60d04" width="1280" height="711" data-path=".assets/images/gesture-recognition-on-silabs-xg24/create-impulse.png" />
</Frame>

As you can see, the model was created based on 3-axis accelerometer data. The Window size was set as 4s and window increase was set to 4s as well, which ensures there is no overlap. That means if the input data is of 20s, there will be 5 samples from that data. Spectral Analysis was selected as Digital Signal Processing and Keras was selected for the Learning block.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/retrain.png?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=aada445421e3ca1650712f9074bfd88f" width="1280" height="698" data-path=".assets/images/gesture-recognition-on-silabs-xg24/retrain.png" />
</Frame>

Next, navigate to "Retrain model" from the left menu and click on "Start training". Alternatively, you can also collect more data and train the model with your own gesture movement, or add additional gestures.

If you are going to add new data, you can follow this [Thunderboard Sense 2 documentation](/hardware/boards/silabs-thunderboard-sense-2) to connect your board to the Edge Impulse Studio and capture data. Once you are done with collecting additional data, you will need to retrain the model of course.

## Deploy And Test

When you are done retraining, navigate to the "Deployment" page from the left menu, select "SiLabs Thunderboard Sense 2" under "Build firmware", then click on the "Build" button, which will build your model and download a `.bin` file used to flash to the board.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/deployment-tb2.png?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=68473f5fdf1e5ada03c2eea877b9fff3" width="1280" height="937" data-path=".assets/images/gesture-recognition-on-silabs-xg24/deployment-tb2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/firmware-tb2.png?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=f091cda7363e853c18544613b174e0b7" width="1280" height="956" data-path=".assets/images/gesture-recognition-on-silabs-xg24/firmware-tb2.png" />
</Frame>

If not already connected, go ahead and connect the Thunderboard Sense 2 to your computer via a USB cable. You should see a drive named `TB004` appear. Drag and drop the `.bin` file downloaded in the previous step to the drive. If you see any errors like below, you'll need to use "Simplicity Studio 5" to flash the application, instead.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/error.png?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=ecdc2f649016e743c5c0278f34e93168" width="838" height="212" data-path=".assets/images/gesture-recognition-on-silabs-xg24/error.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/simplicity.gif?s=03bf3aa641880677831823a327fe71cb" width="800" height="482" data-path=".assets/images/gesture-recognition-on-silabs-xg24/simplicity.gif" />
</Frame>

The LEDs on the Thunderboard will flash, indicating the firmware has been updated on the board. Open the LightBlue app, and scan for devices. You should see a device named "Edge Impulse", go ahead and connect to that. Then tap on the "0x2A56" characteristic, then "Listen for notifications". Change the format from "Hex" to "UTF-8 String".

Then, back on the computer, open a Terminal and run the below command, which will start inferencing on the board.

```
edge-impulse-run-impulse
```

Alternatively, you can write a boolean `1` to the characteristic to start the inference on the board. Checkout the .gif for how to do it on an xG24:

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/gesture-recognition-on-silabs-xg24/lightblue-tb2.gif" />
</Frame>

To test if the model is working accurately, move your finger to recreate the gesture pattern that you (or Manivannan!) trained, and you should see a notification on your phone.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/notification.png?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=b6731365dac767a355c925df71bf092b" width="443" height="960" data-path=".assets/images/gesture-recognition-on-silabs-xg24/notification.png" />
</Frame>

At this point, you have learned how to clone a Public Edge Impulse project, capture more data, and deploy to a Thunderboard Sense 2 directly.

## Deploy To the xG24 Dev Kit

Now, we will explore how we can deploy the same model to the newer Silabs xG24 hardware instead. Keep in mind that there are some upgrades and differences between the Thunderboard Sense 2 and the xG24, and the not all of the sensors themselves are identical (some are though). For this project specifically, the original work done by Manivannan recorded data from the Thunderboard's IMU, but the xG24 has a 6-axis IMU. So, we should recollect new data to take advantage of this and ensure our data is applicable. If your use-case is simple enough that new data won't data won't be needed, the sensor you are using is identical between the boards, or that your data collection and model creation steps built a model that is still reliable you might be able to skip this.

If your data is indeed simple enough, you can deploy the model straight to an xG24 without making any changes to the model itself. You only need to revisit the "Deployment" tab in the Edge Impulse Studio, select "SiLabs xG24 Dev Kit" under Build firmware, and Build. For the sake of demonstration we will give it a try in this project, though as mentioned the upgrade from 3-axis to 6-axis data really should be investigated, but the sensor itself is identical between the boards so our data should still be valid. We'll give it a try.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/deployment-xg24.png?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=4b9d27b6b07b2c2d68148972b5c0b9d2" width="1280" height="836" data-path=".assets/images/gesture-recognition-on-silabs-xg24/deployment-xg24.png" />
</Frame>

This will download a .zip file containing a `.hex` file and instructions.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/firmware-xg24.png?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=91625bdac8bde7ff411dae876e8b3909" width="1094" height="188" data-path=".assets/images/gesture-recognition-on-silabs-xg24/firmware-xg24.png" />
</Frame>

Now you can use Simplicity Studio 5 to flash the `.hex` file to the xG24 as shown before, or use Simplicity Commander. You can read more about Commander [here](/hardware/boards/silabs-xg24-devkit).

Once the flashing is done, again use the LightBlue app to connect to your board, and test gestures once again as you did for the Thunderboard Sense 2.

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/gesture-recognition-on-silabs-xg24/lightblue-xg24.gif" />
</Frame>

Once deployed, your same gestures should be recognized and inferencing is performed on the xG24 in the same manner as the Thunderboard Sense 2, with no additional model training or dataset manipulation needed! This makes upgrading existing projects from the Thunderboard to the xG24 extremely simple when the data and sensor output are comparable and you confirm the sensor is the same part number. Again, you'll need to cross check the datasheets, but you may find you can take a Thunderboard Sense 2 project and deploy it directly to the xG24.

One final note is that in this project, the xG24 is roughly twice as fast as the Thunderboard Sense 2 running the same model:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dGsNjDGzExMEV34a/.assets/images/gesture-recognition-on-silabs-xg24/silabs-compare.png?fit=max&auto=format&n=dGsNjDGzExMEV34a&q=85&s=6f5832feb79210b9ef6dd893873b5220" width="1600" height="576" data-path=".assets/images/gesture-recognition-on-silabs-xg24/silabs-compare.png" />
</Frame>

Hopefully this makes upgrading your SiLabs projects easier!


Built with [Mintlify](https://mintlify.com).