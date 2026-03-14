# Source: https://docs.edgeimpulse.com/projects/expert-network/smart-baby-swing-arduino-portenta-h7.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart Baby Swing - Arduino Portenta H7

Created By: Manivannan Sivan

Public Project Link: [https://studio.edgeimpulse.com/public/134216/latest](https://studio.edgeimpulse.com/public/134216/latest)

## Project Demo

<iframe src="https://www.youtube.com/embed/v-rFyNGM5qU" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/intro.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=b1abc0167cf63212d539459c095c4363" width="960" height="720" data-path=".assets/images/smart-baby-swing/intro.jpg" />
</Frame>

## Problem Statement

On a typical baby swing rocker only a manual ON/OFF switch, or a swing timer option function can be chosen. But when a baby starts to cry in the middle of the night, the baby swing rocker is normally in the "Off" position, so it cannot calm the baby.

## TinyML Solution

I have automated the baby swing movement with a TinyML model. An Arduino is running audio inferencing and will classify the baby crying sound from room noise and activate the baby swing rocker motor, so that it can calm the baby and help them fall asleep again.

## Overview

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/architecture.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=b6cb53fd8a95d6716714a9d27fa1a650" width="960" height="720" data-path=".assets/images/smart-baby-swing/architecture.jpg" />
</Frame>

The above block diagram explains the overall architecture of the project. The TinyML model is trained in Edge Impulse, and then deployed back to an Arduino Portenta H7.

I have collected baby crying sounds and background room noise for TinyML model training, trained the model with enough data to provide good accuracy, and finally integrated the system with the swing hardware.

## Hardware Required

* Arduino Portenta H7
* Portenta Vision Shield
* Baby swing rocker

## Data Acquisition

For data acquisition, I have collected real baby crying sounds and room noise. I have used an Arduino Portenta H7 with the Vision Shield to collect audio samples. The Arduino Portenta Vision Shield is used because it contains two MP34DT05 microphones which run on 16 MHz.

For initial setup of the Portenta, follow the steps mentioned in [this link](/hardware/boards/arduino-portenta-h7).

Once the Portenta firmware is flashed to the Arduino Portenta H7 hardware, then open the command window in your system and run the below command:

`edge-impulse-daemon`

The Portenta is now connected to Edge Impulse. I have collected a dataset of real baby crying sounds and some normal room noise.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/data-collection.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=99ccdbea666c3fdbe0c93dd5899ee61d" width="1176" height="493" data-path=".assets/images/smart-baby-swing/data-collection.jpg" />
</Frame>

I have collected a datasets of around 2 mins and 41 seconds. This dataset is used for the model training.

## Create Impulse

Inside your Edge Impulse account, in the *Create Impulse* section, the Window Sampling is selected as 2500ms and Window Increase is set as 500ms. I have configured spectrogram as a Preprocessing block.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/impulse.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=bac3bf580cf5d7e39f46a34764cb2e11" width="1167" height="450" data-path=".assets/images/smart-baby-swing/impulse.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/feature-explorer.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=d25a7ce811911e5f17eb542f3a16522c" width="960" height="720" data-path=".assets/images/smart-baby-swing/feature-explorer.jpg" />
</Frame>

## Neural Network Training

I have used a sequential neural network layer. The input data in 2 Dimensions is reshaped into 1 Dimension using a reshape layer. Then a 1 Dimensional convolution layer with Max pooling is used.

### 1D Convolution Layer

The below diagram demonstrates the 1D convolution layer and max pooling filtering.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/neural-network.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=1644e2e990f42319f81535ae627e2010" width="902" height="652" data-path=".assets/images/smart-baby-swing/neural-network.jpg" />
</Frame>

### Max Pooling

The 1D max pooling block moves a pool (window) of a set size over the incoming data with a set stride, computing the maximum in each specific window. The below diagram demonstrates the max pooling technique in 1D input data.

In our network, the max pooling is configured as `MaxPooling1D(pool_size=2, strides=2, padding='same')`. This means the pool size is 2, where it takes 2 indices values and outputs the maximum value in that. And the stride length is 2, so it moves the pool layer twice in one direction.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/max-pooling.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=2cc1880feeb8d253d3ff384fedf209fe" width="1600" height="696" data-path=".assets/images/smart-baby-swing/max-pooling.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/model-network.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=2f0ad07c6010427d8aaae2087b205b0f" width="735" height="645" data-path=".assets/images/smart-baby-swing/model-network.jpg" />
</Frame>

I have configured the training cycles as 100 with a learning rate of 0.005, and achieved good accuracy.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/training.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=8672f1db2ce5694e5bf40645c3aee604" width="878" height="510" data-path=".assets/images/smart-baby-swing/training.jpg" />
</Frame>

## Results

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/accuracy.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=9dd18c9cfaa686c5d9c619c16ac9aaeb" width="902" height="716" data-path=".assets/images/smart-baby-swing/accuracy.jpg" />
</Frame>

Upon completion of training, we can see that we have achieved 98.2% accuracy.

## Model Testing

After the model is trained with good accuracy, I have tested with new data. I have used two datasets for each category (baby cry and room noise) for testing. In testing with unseen data, the model achieved 100% accuracy.

Then next step is deployment to the hardware.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/testing.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=845293a124b5e270993dade04b3ac427" width="814" height="391" data-path=".assets/images/smart-baby-swing/testing.jpg" />
</Frame>

## Deployment

Once the testing is complete, go to the "Deployment" option and select *Build firmware* -> *Arduino Portenta H7* to create a downloadable firmware to flash to the board. I have chosen Quantized (Int8). In Edge Impulse, there is also an option to use the EON compiler for reducing resources and improving accuracy, as well as lower latency.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/eon-compiler.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=d42e15e335cf65583afebc8f42be186f" width="796" height="522" data-path=".assets/images/smart-baby-swing/eon-compiler.jpg" />
</Frame>

Once the build process is completed, the firmware will be packaged in a Zip file and downloaded.

Press the Reset button on the Portenta H7 twice to set it to "Flash mode" and then open the .bat file (if your are using Windows) or run the Mac version if that is your platform, to flash the firmware.

Once the flash is completed, open a new terminal window and run the below command to start inference on the device: `edge-impulse-run-impulse`

The above step will tell us whether the model is able to run smoothly on real hardware. After this step, now comes the real challenge! We need to integrate the Portenta H7 into the baby swing rocker!

For this, we need to deploy this model as source code and add our application on top of it.

So, we click the *Create Library* section in the Studio and select *Arduino*, then download the source code.

Open the Arduino IDE and select *Sketch -> Include library* and *Add .Zip Library*. Then select the downloaded Zip file on your machine.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/arduino-1.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=a60b6b019657981fa5f34a8b29eb09f6" width="796" height="496" data-path=".assets/images/smart-baby-swing/arduino-1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/arduino-2.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=7a2f2533fd70b7d34fccab9ba2f57d34" width="796" height="460" data-path=".assets/images/smart-baby-swing/arduino-2.jpg" />
</Frame>

After including the Library, go to *Examples* and select `portent_h7_microphone_continuous` I have written the application code on top of the default code in the example.

## Application Layer Integration

In the application code, I wrote the logic to activate a relay which is connected to the motor in the baby swing rocker. The below flowchart explains the logic of the application code.

Also, I have added my application code in below GitHub link, which you can directly copy and paste into your Arduino IDE.

> `https://github.com/Manivannan-maker/smartbabyswingrocker`

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/application.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=01940b944e9a882cdb59499dafe24b19" width="960" height="720" data-path=".assets/images/smart-baby-swing/application.jpg" />
</Frame>

The application code will activate the baby swing rocker for 20 seconds, whenever it detects the baby crying sound.

## Hardware Integration

The Arduino Portenta is connected to the 5v DC Relay module. The Common pin in the relay is connected to the Gnd of the battery and NO pin in the relay is connected to the Gnd of the motor in the baby swing rocker whereas the Vcc of the motor is connected directly to the Battery positive terminal.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/hardware.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=0523a58d40edaa88868e73c00a1cb356" width="774" height="578" data-path=".assets/images/smart-baby-swing/hardware.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5Tc6D0OqsEDdaNOc/.assets/images/smart-baby-swing/swing.jpg?fit=max&auto=format&n=5Tc6D0OqsEDdaNOc&q=85&s=0eb19736801f1082fec6a5c1cd80df5c" width="664" height="539" data-path=".assets/images/smart-baby-swing/swing.jpg" />
</Frame>

## Summary

After the wiring is complete, you can test it in real time. I have played the baby crying sound on my phone and after few seconds, the baby swing rocker started to swing. The YouTube video embedded above demonstrates the working demo of this prototype.


Built with [Mintlify](https://mintlify.com).