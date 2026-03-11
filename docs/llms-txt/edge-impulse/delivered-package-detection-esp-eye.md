# Source: https://docs.edgeimpulse.com/projects/expert-network/delivered-package-detection-esp-eye.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delivered Package Detection - ESP-EYE

Created By: Solomon Githu

Public Project Link: [https://studio.edgeimpulse.com/public/103841/latest](https://studio.edgeimpulse.com/public/103841/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/parcel-detection/intro.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=166443f7f4f052e0dbd4abcf2327c9d6" width="1046" height="410" data-path=".assets/images/parcel-detection/intro.jpg" />
</Frame>

## Background

As ecommerce availability continues to expand worldwide, many people prefer to shop online and have their purchases delivered to their homes. As a result, package theft has increased along with more parcels being delivered. According to a recent [SafeWise](https://www.safewise.com/blog/metro-areas-porch-theft/) analysis, 210 million shipments will be stolen in 2021. In some cases, thieves follow delivery trucks and steal the package immediately when it has been delivered.

Although there are ways to prevent package theft, such as having packages delivered to the Post Office or giving the courier access to your home remotely, many individuals prefer door deliveries. However, we may not always be around to collect packages, or thieves may be quicker to do so!

## Monitor delivered packages with TinyML

There are a couple of techniques to prevent package theft, but we'll focus on parcels delivered to our front porches or mailboxes. We'll use Edge Impulse to create a Machine Learning model that recognizes parcels. The model will then be deployed on a low-cost, low-power device, the [ESP-EYE](https://www.espressif.com/en/products/devkits/esp-eye/overview) development board. This board has a 2MP camera that we will use to collect live video feeds of our shipments.

To develop our Machine Learning model, we will use FOMO (Faster Objects, More Objects). This is an algorithm developed by Edge Impulse to enable real-time object detection, tracking and counting on microcontrollers. FOMO is 30x faster than MobileNet SSD and runs in \<200K of RAM. On a Raspberry Pi 4, live classification with FOMO achieved \~27.7 frames per second, while SSD MobileNetV2 gave \~1.56fps.

## Things used in this project

### Hardware components

* ESP-EYE Board

### Software

* Edge Impulse Studio

## Quick Start

You can find the public project here: [Parcel Detection - FOMO](https://studio.edgeimpulse.com/public/103841/latest). To add this project into your account, click “Clone this project” at the top of the page. Next, go to “Deploying to ESP-EYE” section below to learn how to deploy the model to the ESP-EYE board.

Alternatively, to create a similar project, follow the next steps after creating a new Edge Impulse project.

## Data Acquisition

First, on the Project Dashboard, we set Labeling method to “Bounding boxes (object detection)”.

We want our Machine Learning model to detect parcels in an image. To do this, we need pictures of parcels! Note that our dataset only includes box parcels and not envelopes or poly-mailer bags. In total, the dataset has 275 images with an 80/20 split for train and test data. If you want to add more images to the dataset, Edge Impulse has an [uploader](/studio/projects/data-acquisition/uploader) that enables different ways of adding data to your project. Afterwards, make sure to perform a Train/test split to re-balance your dataset.

Next, we annotate the images and label a parcel in each image.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/parcel-detection/labeling.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=1d9c832ad669003fa2b06d9a3533e666" width="1365" height="768" data-path=".assets/images/parcel-detection/labeling.jpg" />
</Frame>

## Impulse Design

We can now use our dataset to train our model. This requires two important features: a processing block and learning block. Documentation on Impulse Design can be found [here](/studio/projects/impulse-design).

We first click ”Create Impulse”. Here, set image width and height to 96x96; and Resize mode to Squash. The Processing block is set to “Image” and the Learning block is “Object Detection (images)”. Click ‘Save Impulse’ to use this configuration.

Since the ESP-EYE is resource-constrained device (4MB flash and 8MB PSRAM), we have used 96x96 image size to lower RAM usage.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/parcel-detection/impulse.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=51a15a9d25fc2e4ac08d1a1a1a53d1b0" width="1348" height="759" data-path=".assets/images/parcel-detection/impulse.jpg" />
</Frame>

Next, we go to the processing block “Image” and set Color depth to Grayscale. "Save parameters", and this will open the “Generate Features” tab.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/parcel-detection/images.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=e1c9f4a99d39763ca0fadceedd986ec8" width="1343" height="763" data-path=".assets/images/parcel-detection/images.jpg" />
</Frame>

Next, we generate features from our training dataset by clicking “Generate features”.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/parcel-detection/generate-features.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=188057b6a1bdb0f709088bf73000caaf" width="1339" height="765" data-path=".assets/images/parcel-detection/generate-features.jpg" />
</Frame>

The last step is to train our model. We click “Object Detection” which is our Learning block. 60 training cycles with a learning rate of 0.001 were used for this project. We select the FOMO model, by clicking “Choose a different model”.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/parcel-detection/choose-model.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=3557c38eac15ebe50cc18ca0905fd15c" width="832" height="634" data-path=".assets/images/parcel-detection/choose-model.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/parcel-detection/training.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=68da64a63506522095a4b7574466252e" width="1342" height="758" data-path=".assets/images/parcel-detection/training.jpg" />
</Frame>

After training, the model has an F1 score of 94%. An F1-score combines precision and recall into a single metric.

## Model Testing

When training our model, we used 80% of the data in our dataset. The remaining 20% is used to test the accuracy of the model in classifying unseen data. We need to verify that our model has not overfit, by testing it on new data. If your model performs poorly, then it means that it overfit (crammed your dataset). This can be resolved by adding more dataset and/or reconfiguring the processing and learning blocks, and even adding Data Augmentation. If you need to increase performance a bit, some tips and tricks can be found in this [guide](/knowledge/guides/increasing-model-performance).

Click “Model testing” then “classify all”. Our current model has an accuracy of 91%, which is pretty good.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/parcel-detection/classification-1.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=7429fc2626b70975076a85e0f8d7fcce" width="1345" height="760" data-path=".assets/images/parcel-detection/classification-1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/parcel-detection/classification-2.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=45eb75260dd60e3af9de4c398c8e82b0" width="1337" height="762" data-path=".assets/images/parcel-detection/classification-2.jpg" />
</Frame>

## Deploying to ESP-EYE board

To deploy our model, first go to the “Deployment” section. Next, under “Build firmware” we select Espressif ESP-EYE (ESP32) from the options. To increase performance on the board, we set “Enable EON Compiler” and chose “Quantized(int8)” optimization. This makes our model use 243.9K of RAM and 77.5K of Flash on the board. Chose “Build” and the firmware will be downloaded after the build ends.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/parcel-detection/deploy-1.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=4ac89ce1b5db43a556bc2a57f0d599c3" width="1345" height="764" data-path=".assets/images/parcel-detection/deploy-1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/parcel-detection/deploy-2.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=5fd72d7d50135977159e24a351595adf" width="1346" height="766" data-path=".assets/images/parcel-detection/deploy-2.jpg" />
</Frame>

Connect an ESP-EYE board to your computer, extract the downloaded firmware and run the script in the folder, to upload it to your board. Great! Now we have our model on the ESP-EYE.

To get a live feed of the camera and classification, run the command: `edge-impulse-run-impulse --debug`

Next, enter the provided URL in a browser and you will see live feeds from the ESP-EYE.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/parcel-detection/test.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=c670b86da0d071ded24e8563257e09e2" width="1340" height="648" data-path=".assets/images/parcel-detection/test.jpg" />
</Frame>

The ESP-EYE gives \~ 1 fps, using 96x96 image size. Using a 48x48 image size gives \~5fps, but the model is not accurate in this case. The performance can be related to the ESP-EYE being a constrained device with limited flash and RAM. Inference has a latency of \~850ms with 96x96 image, while \~200ms with a 48x48 image. Larger images have more bytes that need to be processed, while in lower resolutions useful data for object-detection is collapsed, thus resulting in the poor accuracy.

For this use-case of monitoring a front porch, taking one picture every second from ESP-EYE, and analyzing it, is acceptable. However, you can also target higher performance MCUs. FOMO firmware is currently compatible with various boards such as Arduino Nano 33 BLE Sense with a camera, Portenta H7 with a Vision Shield, Himax WE-I Plus, OpenMV, Sony’s Spresense, and Linux-based dev boards. You can also build the model as a library (C++, WebAssembly, TensorRT, Ethos-U, OpenMV, CubeMX, Simplicity Studio Component) and run it on any device!

## Taking it one step farther

We can use this model to monitor delivered parcels, and take some actions such as sounding an alarm or sending a text message when no parcel, or fewer parcels are detected.

A build library will allow us to add custom code to the predictions. We can check if one or more parcels are predicted, save the count, and then monitor the predictions count. If predictions count goes down, that means a parcel(s) is missing and we can raise an alarm using our development board, and even send a signal to other home automation devices such as security cameras or alarms.

Edge Impulse has also developed a feature that enables sending an SMS based on inference from our model. This feature works with Development boards that support Edge Impulse for Linux, such as the Raspberry Pi. The repository and documentation can be found [here](https://github.com/zebular13/example-linux-with-twilio).

<Frame caption="Sending SMS uses Twilio service">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/parcel-detection/twilio.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=add20f4182593b4e8e64f4b048216764" width="1046" height="410" data-path=".assets/images/parcel-detection/twilio.jpg" />
</Frame>

## Conclusion

Developing Machine Learning models with [Edge Impulse](https://www.edgeimpulse.com/) has always been easy! We have seen how we can create a Machine Learning model capable of detecting parcels, but also run it on a constrained-MCU such as the ESP-EYE. FOMO was chosen in this project so that the model could be small, and also fast! We can now monitor packages easily, with minimal cost and power requirements.

This demonstrates the massive potential that TinyML offers to make the world smarter and solve endless problems. Knowledge on deep learning and microcontrollers is not known by everyone, but the Edge Impulse platform provides easy, smarter and faster tools that we can use to create and build edge ML solutions quickly.


Built with [Mintlify](https://mintlify.com).