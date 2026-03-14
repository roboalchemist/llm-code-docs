# Source: https://docs.edgeimpulse.com/projects/expert-network/solar-panel-defect-detection-arduino-portenta-h7.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Solar Panel Defect Detection - Arduino Portenta H7

Created By: Manivannan Sivan

Public Project Link: [https://studio.edgeimpulse.com/public/126645/latest](https://studio.edgeimpulse.com/public/126645/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/intro.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=df1f2793ea917c309a2416d97be34958" width="1111" height="625" data-path=".assets/images/solar-panel-defect-detection/intro.jpg" />
</Frame>

## Problem Statement

### Reasons for Solar Panel Damage

* Microscopic fractures, hot spots and cracks can appear on the surface of solar panel glass cells, and can grow in size over time. These cracks can reduce the effectiveness of solar cells. The lamination, panel frame and waterproofing of the solar system may remain in good condition despite the cracks, making it hard to identify the cause of the problem.
* Storm, hail, snow pressure, lightning and other weather conditions can cause extensive damage to solar modules. External damage may also occur due to fire, animal activity, broken tree branches, icy conditions and excessive heat or cold.
* The scratches from fallen debris can dramatically lower your panels’ energy output. Scratches can hinder sunlight from shining directly onto the cells, and that decreases the amount of solar energy each panel is able to absorb. That, in turn, can increase utility bills, which is one reason to install solar panels in the first place.

### Challenges in Solar Panel Monitoring

* To monitor solar panel and look for damage, manual inspection needs to be done every month or few months.
* In larger areas, monitoring solar panels periodically needs more people, and the time between inspections might be reduced (more inspection needed).
* Manual inspection is more time consuming and less efficient.

## Solution

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/solution.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=22b8a6fe8b4082afc73e9892394754a5" width="902" height="594" data-path=".assets/images/solar-panel-defect-detection/solution.jpg" />
</Frame>

I have developed a TinyML model using Edge Impulse and deployed the model onto an Arduino Portenta H7. This model is trained with solar panel images with cracks on them. In Edge Impulse, I have labeled the cracks in the images and trained using a [FOMO](https://www.edgeimpulse.com/blog/announcing-fomo-faster-objects-more-objects) based model.

### Advantages over Manual Inspection

* It is efficient and less time consuming
* Hourly monitoring is possible using automated inspection
* This prototype, if combined with a drone or self driving robot, can inspect entire solar farms.

## Hardware Required

* Arduino Portenta H7
* Portenta Vision Shield
* Solar panel

## Architecture

For this prototype development, I have used a FOMO-based object detection model to detect the cracks in the solar panel. The below diagram explains the overview of the model development.

The major steps that need to be followed for the model development are:

* Data Acquisition
* Model Training
* Model Testing
* Deployment

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/architecture.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=539fecf788aaf5abd685176818712ce6" width="854" height="700" data-path=".assets/images/solar-panel-defect-detection/architecture.jpg" />
</Frame>

## Data Acquisition

For data acquisition, I have collected the real images of solar panels with cracks using the Arduino Portenta H7 and Vision Shield.

To connect the Portenta for the first time, follow the below steps:

1. Download the zip file [https://cdn.edgeimpulse.com/firmware/arduino-portenta-h7.zip](https://cdn.edgeimpulse.com/firmware/arduino-portenta-h7.zip)
2. Press the Reset button twice to put the device into "boot loader" mode
3. Flash the downloaded firmware by opening the included script (`flash_windows.bat`, `flash_mac.command` or `flash_linux.sh`)
4. After flashing, press the Reset button once.
5. Open a command prompt and run the command `edge-impulse-daemon`

Now the Portenta is connected to the Edge Impulse account. I have placed the solar panel with cracks in front of the Arduino Portenta plus Vision shield. The distance between solar panel and Portenta is adjusted so that it captures the entire solar panel region.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/data-acquisition.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=99bf567407c80776130bad7e96acee0d" width="1334" height="1000" data-path=".assets/images/solar-panel-defect-detection/data-acquisition.jpg" />
</Frame>

Go to the *Data Acquisition* section in Edge Impulse and [capture images](/studio/projects/data-acquisition).

Then go to *Labeling queue* in the *Data acquisition* section to draw bounding boxes around the cracks in the collected images.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/labeling.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=dbc48a2c32f06fd6a7c4d00bee3c54c8" width="946" height="82" data-path=".assets/images/solar-panel-defect-detection/labeling.jpg" />
</Frame>

You can read more about the Labeling queue at this [link](/studio/projects/data-acquisition/labeling-queue).

In the Labelling queue, all the raw images are shown, and we need to drag and drop the markings and label the cracks.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/labeling-2.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=ccef854592509b4ba3eef59a4e21c4f8" width="902" height="468" data-path=".assets/images/solar-panel-defect-detection/labeling-2.jpg" />
</Frame>

So ideally, we add all the cracks as objects in the image.

Once labeling is completed for all images in the dataset, split the dataset into 80:20 ratios for training and testing data.

You can click any dataset and move it to the test data.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/data.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=c03e316115c47295c0aa0ced89845a81" width="884" height="416" data-path=".assets/images/solar-panel-defect-detection/data.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/train-test.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=f93f8243382c5433c7663dbd0ab60656" width="472" height="132" data-path=".assets/images/solar-panel-defect-detection/train-test.jpg" />
</Frame>

So I made the ratios close to 80:20.

## Create Impulse

In the *Create Impulse* section, I have selected Object detection and set a Pixel size of 96x96.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/impulse.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=3f612b2413febb043b5e3d361383b956" width="1179" height="328" data-path=".assets/images/solar-panel-defect-detection/impulse.jpg" />
</Frame>

Then in the *Image* section, I have selected the color depth as “ Grayscale”.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/parameters.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=5b8a3b5e5f64df83ffbb95e809d81c30" width="1166" height="484" data-path=".assets/images/solar-panel-defect-detection/parameters.jpg" />
</Frame>

## Model Training

In the *Object detection* section, I have selected the FOMO model -- FOMO (Faster Objects, More Objects) MobileNetV2 0.35

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/training.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=c2939b0d21d3c86c4c0269d8bc6d284e" width="840" height="174" data-path=".assets/images/solar-panel-defect-detection/training.jpg" />
</Frame>

This [FOMO](/studio/projects/learning-blocks/blocks/object-detection/fomo) model can run Object Detection on resource constrained microcontrollers.

In *Training settings*, I have selected 200 training cycles and a Learning rate as 0.005

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/training-2.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=d6067092e6fd7d4aed3c23ca9ba92b33" width="834" height="288" data-path=".assets/images/solar-panel-defect-detection/training-2.jpg" />
</Frame>

The Neural network architecture is FOMO model.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/neural-network.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=e9c4914ec7be09b5aeb2b64f5425b603" width="838" height="392" data-path=".assets/images/solar-panel-defect-detection/neural-network.jpg" />
</Frame>

## Training Output

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/accuracy.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=dc944fc74edc04b7fded97c0edd88ce6" width="902" height="398" data-path=".assets/images/solar-panel-defect-detection/accuracy.jpg" />
</Frame>

In the training output, the model achieved 85.7% accuracy. Around 23.7% of cracks were identified as background, so, there is room for improvement.

The reason for the misclassification is that cracks and PV cells boundary lines look similar in some cases. In those situations, the model predicts the cracks as background.

To improve the accuracy, data augmentation is selected and data acquisition is done with different camera angles to better predict the cracks in the solar panel.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/testing.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=d50278b6ef9aad5509625937309da074" width="818" height="450" data-path=".assets/images/solar-panel-defect-detection/testing.jpg" />
</Frame>

## Model Testing

In *Model testing*, the model is able to identify cracks in solar panel images. In two of the testing data, it did miss identifying some cracks in the panels. This is normally due to lighting differences and camera angle, but it performs decently with 77.8% accuracy in Model testing.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/testing-2.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=2290a493d13a02cb5eb2dc581d8f201a" width="1160" height="422" data-path=".assets/images/solar-panel-defect-detection/testing-2.jpg" />
</Frame>

## Deployment

Go to the *Deployment* section and select *Build firmware* with Arduino Portenta H7 and download the firmware. Then press the Reset button twice to get into the boot loader mode again and open the downloaded script to flash it, similar to earlier.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/deployment.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=e95ac8d1bbd329a7f8f1196f8c8935b3" width="902" height="352" data-path=".assets/images/solar-panel-defect-detection/deployment.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/optimization.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=b549644c49f09c85b40568f35740b327" width="902" height="308" data-path=".assets/images/solar-panel-defect-detection/optimization.jpg" />
</Frame>

On my Windows system, I opened the `.bat` file to flash it to the Portenta.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/solar-panel-defect-detection/flash.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=d7eb24c8d7035d79f04d17d9aef0de4c" width="902" height="230" data-path=".assets/images/solar-panel-defect-detection/flash.jpg" />
</Frame>

When complete, press the Reset button once. Finally, open a terminal and run the following command: `edge-impulse-run-impulse`

## Summary

This TinyML model based on FOMO is able to identify cracks in solar panels. One of the key advantages is that it can run on constrained devices like microcontrollers, due to the use of Edge Impulse FOMO. This model can also be ported to other devices such as Sony Spresense, ESP–EYE, or larger systems like an Nvidia Jetson Nano.


Built with [Mintlify](https://mintlify.com).