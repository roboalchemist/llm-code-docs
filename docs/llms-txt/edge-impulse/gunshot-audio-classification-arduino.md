# Source: https://docs.edgeimpulse.com/projects/expert-network/gunshot-audio-classification-arduino.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Gunshot Audio Classification - Arduino Nano 33 + Portenta H7

Created By: Swapnil Verma

Public Project Link: [https://studio.edgeimpulse.com/public/133765/latest](https://studio.edgeimpulse.com/public/133765/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/intro.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=e434209ede21a17f129e5333d3e15873" width="900" height="675" data-path=".assets/images/gunshot-audio-classification/intro.jpg" />
</Frame>

## Intro Problem

On May 24, 2022, nineteen students and two teachers were fatally shot, and seventeen others were wounded at Robb Elementary School in Uvalde, Texas, United States\[1]. An 18-year-old gunman entered the elementary school and started shooting kids and teachers with a semi-automatic rifle. The sad part is that it is not a one-off event. Gun violence including mass shootings is a real problem, especially in the USA.

<img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/problem1.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=f8f9a038762d0125ff25f0bb80586948" alt="Deaths due to gun violence in 2022 [2]" width="704" height="480" data-path=".assets/images/gunshot-audio-classification/problem1.jpg" />

<img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/problem2.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=67d9ae6a6a206479024fc1e1a5e4c7f7" alt="Deaths due to gun violence in 2022 [2]" width="702" height="455" data-path=".assets/images/gunshot-audio-classification/problem2.jpg" />

## What Can I Do About It?

Gun violence is a massive problem and I alone can not solve it, but I can definitely contribute an engineering solution toward hopefully minimizing casualties.

Here I am proposing a proof of concept to identify gun sounds using a low-cost system and inform emergency services as soon as possible. Using this system, emergency services can respond to a gun incident as quickly as possible thus hopefully minimizing casualties.

## How Does It Work?

My low-cost proof of concept uses multiple microcontroller boards with microphones to capture sound. They use a TinyML algorithm prepared using Edge Impulse to detect any gunshot sound. Upon a positive detection, the system sends a notification to registered services via an MQTT broker.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/design.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=f7214a16b49386c19af2f3e5e4b9ab6c" width="1280" height="433" data-path=".assets/images/gunshot-audio-classification/design.jpg" />
</Frame>

To learn more about the working of the system, please check out the Software section.

## Hardware

The hardware I am using is:

* Arduino Portenta H7
* Arduino Nano BLE Sense
* 9V Battery

<Frame caption="Hardware">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/hardware-1.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=2f106626a3ace79cf99ffc766d503388" width="1280" height="960" data-path=".assets/images/gunshot-audio-classification/hardware-1.jpg" />
</Frame>

<br />

<Frame caption="Internal Layout">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/hardware-2.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=116aedcd4a3c4f964c9b9959bf6de47c" width="972" height="960" data-path=".assets/images/gunshot-audio-classification/hardware-2.jpg" />
</Frame>

In the current hardware iteration, the Arduino Nano BLE Sense is powered by a 9V battery and the Portenta H7 is powered via a laptop, because I am also using the serial port on the Portenta H7 to debug the system.

## Software

The software is divided into 2 main modules:

* Machine Learning
* Communication

### Machine Learning Module

The machine learning module uses a tinyML algorithm prepared using Edge Impulse. This module is responsible for identifying gunshot sounds. It takes sound as input and outputs its classification.

### Dataset

One of the most important parts of any machine learning model is its dataset. In this project, I have used a combination of two different datasets. For the *gunshot* class, I used the [Gunshot audio dataset](https://www.kaggle.com/datasets/emrahaydemr/gunshot-audio-dataset) and for the *other* class, I used the [UrbanSound8K](https://www.kaggle.com/datasets/chrisfilo/urbansound8k) dataset from Kaggle.

Edge Impulse Studio's [Data acquisition tab](/studio/projects/data-acquisition) provides useful features to either record your own data or upload already-collected datasets. I used the upload feature.

<Frame caption="Data Uploader">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/upload-data.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=ab095b097c81c70068d1d7fdbb48f1a8" width="461" height="735" data-path=".assets/images/gunshot-audio-classification/upload-data.jpg" />
</Frame>

While uploading you can also provide a label to the data. This was very helpful because I am using sounds from multiple origins in the *other* class. After uploading the data, I cleaned the data using the Studio's [Crop](/studio/projects/data-acquisition#cropping-samples) and [Split sample](/studio/projects/data-acquisition#splitting-data-sample) feature.

<Frame caption="Crop Sample">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/sample-1.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=a498208c931303d6a40fbf33601ccd85" width="1138" height="703" data-path=".assets/images/gunshot-audio-classification/sample-1.jpg" />
</Frame>

<br />

<Frame caption="Split Sample">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/sample-2.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=6efda397ff9dcf9c226d5cd2f64294d0" width="1138" height="703" data-path=".assets/images/gunshot-audio-classification/sample-2.jpg" />
</Frame>

You can either divide data into test and train sets while uploading or do it at a later time. The Data acquisition tab shows the different classes and [train/test split ratio](/studio/projects/data-acquisition#dataset-train%2Ftest-split-ratio) for our convenience.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/train-split.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=b5ba6626cc0a25b061ad91711f9c4bd4" width="629" height="84" data-path=".assets/images/gunshot-audio-classification/train-split.jpg" />
</Frame>

### Training

After preparing the dataset, we need to design an [Impulse](/studio/projects/impulse-design). The Edge Impulse documentation explains the Impulse design in great detail so please check out their documentation page to learn about Impulse design.

<Frame caption="Impulse Design">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/training.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=2c77b43e8da1f75e41c3089133697113" width="1280" height="515" data-path=".assets/images/gunshot-audio-classification/training.jpg" />
</Frame>

As you can see, I have selected [MFCC](/studio/projects/processing-blocks/blocks/audio-mfcc) as the [preprocessing block](/studio/projects/processing-blocks), and [classification](/studio/projects/learning-blocks/blocks/classification) as the [learning block](/studio/projects/learning-blocks). I have used the default parameters for the MFCC preprocessing. For training, I have slightly modified the default neural network architecture. I have used three 1D convolutional CPD layers with 8, 16 and 24 neurons, respectively. The architecture is illustrated in the below image.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/layers.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=92d721e2ae1e3e23c1f195e909e10cdf" width="1280" height="743" data-path=".assets/images/gunshot-audio-classification/layers.jpg" />
</Frame>

<br />

<Frame caption="Neural Network Architecture">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/layers-2.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=e93fa91a6a034ad8c0c5f6f3fc8f2efb" width="613" height="696" data-path=".assets/images/gunshot-audio-classification/layers-2.jpg" />
</Frame>

Modifying the neural network architecture in the Edge Impulse Studio is very easy. Just click on [Add an extra layer](/studio/projects/learning-blocks/blocks/classification#neural-network-architecture) at the bottom of the architecture and select any layer from the popup.

<Frame caption="Add an Extra Layer">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/layers-3.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=5196d59c9d400cf2e15c964197e03dab" width="787" height="893" data-path=".assets/images/gunshot-audio-classification/layers-3.jpg" />
</Frame>

Or you can also do it from the [Expert mode](/studio/projects/learning-blocks/blocks/classification#expert-mode) if you are feeling masochistic 😉.

<Frame caption="Expert Mode">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/neuralnetwork-1.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=76a3d0791874ac2a87c35917b6460206" width="627" height="484" data-path=".assets/images/gunshot-audio-classification/neuralnetwork-1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/neuralnetwork-2.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=3171147f9c6e10f243b1a2fbc55f276b" width="627" height="887" data-path=".assets/images/gunshot-audio-classification/neuralnetwork-2.jpg" />
</Frame>

I trained the model for 5000 iterations with a 0.0005 learning rate. My final model has 94.5% accuracy.

<Frame caption="Training Performance">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/accuracy.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=8927b3b16dc4e36c0a1e340a8aaf4ab5" width="620" height="837" data-path=".assets/images/gunshot-audio-classification/accuracy.jpg" />
</Frame>

### Testing

The Edge Impulse Studio's [Model testing](/studio/projects/model-testing) tab enables a developer to test the model immediately. It uses the data from the test block and performs the inference using the last trained model. My model had 91.3% accuracy on the test data.

<Frame caption="Model Testing">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/testing.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=0b2137b1cb134c775bd57ba59b1fd521" width="654" height="640" data-path=".assets/images/gunshot-audio-classification/testing.jpg" />
</Frame>

### Versioning

One nice feature Edge Impulse provides is versioning. You can version your project (like Git) to store all data, configuration, intermediate results and final models. You can revert back to earlier versions of your impulse by importing a revision into a new project. I use this feature every time before changing the neural network architecture. That way I don't have to retrain or keep a manual record of the previous architecture.

<Frame caption="Project Versions">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/versioning.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=785ec4521c05b03700f1b2426c0cd0b7" width="1280" height="358" data-path=".assets/images/gunshot-audio-classification/versioning.jpg" />
</Frame>

### Deployment

After completing the training, it's time for deployment. The [Deployment tab](/studio/projects/deployment) of the Edge Impulse Studio provides three main ways of deploying the model onto hardware: (a) by creating a [library](/studio/projects/deployment#deploying-as-a-customizable-library) (b) by building [firmware](/studio/projects/deployment#deploy-as-a-pre-built-firmware), and (c) by running it on a [computer or a mobile phone](/studio/projects/deployment#deploy-to-your-mobile-phone-computer) directly. I knew that I need more functionality from my Arduino hardware apart from inferencing, so I created a library instead of building firmware.

<Frame caption="Deployment">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/deployment.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=51702c0ac0818b41fcc9eabc5fd78389" width="736" height="691" data-path=".assets/images/gunshot-audio-classification/deployment.jpg" />
</Frame>

Just select the type of library you want, and click the Build button at the bottom of the page. This will build a library and download it onto your computer. After downloading, it will also show a handy guide to include this library in your IDE.

<Frame caption="Adding a Library">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/library.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=69ae0252788baf89380b5423cf7a49f2" width="786" height="387" data-path=".assets/images/gunshot-audio-classification/library.jpg" />
</Frame>

The coolest part is that I don't need to retrain the model or do anything extra to deploy the same model onto multiple devices. The examples of the downloaded library will have example code for all the supported devices of the same family.

<Frame caption="Examples">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/arduino-ide.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=c807fae098319e11e31c9f143ad8ba08" width="1280" height="747" data-path=".assets/images/gunshot-audio-classification/arduino-ide.jpg" />
</Frame>

Just select an example as a getting started code, modify it according to your need and flash it. The Arduino Nano BLE Sense and Portenta H7 use the same model generated by Edge Impulse. I trained the model only once, agnostic of the hardware and deployed it on multiple devices which is a time saver.

### Inferencing

Inferencing is the process of running a neural network model to generate output. The image below shows the inference pipeline.

<Frame caption="Gunshot Detection Pipeline">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/inference-pipeline.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=2bcca99112e7faf47f642c3262284539" width="1121" height="280" data-path=".assets/images/gunshot-audio-classification/inference-pipeline.jpg" />
</Frame>

The microphones in the Nano BLE Sense and Portenta H7 pick up the surrounding sound (stages 1 & 2). The sound data is then preprocessed using the MFCC block (stage 3). The preprocessed data is then sent to a Convolutional Neural Network block (stage 4) which classifies it into either the *gunshot* class or the *other* class (stage 5).

To learn more about the project please follow the below link.

> Project Link - [https://studio.edgeimpulse.com/public/133765/latest](https://studio.edgeimpulse.com/public/133765/latest)

The output of the machine learning module is then processed before sending it to the cloud via the Communication module.

### Communication Module

This module is responsible for sharing information between boards and sending positive predictions to the registered emergency services.

<Frame caption="Communication Pipeline">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gunshot-audio-classification/communication-pipeline.jpg?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=bb4f63768229c4fcff32ab4375fa0d9d" width="1280" height="548" data-path=".assets/images/gunshot-audio-classification/communication-pipeline.jpg" />
</Frame>

The Nano BLE Sense sends its inference to the Portenta H7 via BLE. The Portenta H7 then sends the positive output (i.e. detection of gunshot sound) of its inference and Nano BLE's inference to a subscriber via MQTT. I have used the [cloudMQTT](https://www.cloudmqtt.com/) broker for this project.

To download the software please use the below link:

> Software Link - [https://github.com/sw4p/Gunshot\_Detection](https://github.com/sw4p/Gunshot_Detection)

## Testing

My testing setup and the result are illustrated in the video below. The system is connected to my laptop which is also performing the screen recording. On the upper left side, we have an Arduino serial window which is showing the output from the Portenta H7, and on the lower left hand, we have an audio player. On the right-hand side, we have cloudMQTT's WebSocket UI, which shows the incoming notification via MQTT. The sound for this video is played and recorded using my laptop's speaker and microphone.

<iframe src="https://www.youtube.com/embed/9rXkz2Io2ek" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

In the video above I am playing different categories of sound and one of that categories is a gunshot. The system outputs the classification result to the Arduino serial port whenever it detects a sound from the other class but does not send it to the receiver. The moment it detects a gunshot sound, it immediately sends a notification to the receiver via CloudMQTT.

## Code

[https://github.com/sw4p/Gunshot\_Detection](https://github.com/sw4p/Gunshot_Detection)

## References

\[1] [https://en.wikipedia.org/wiki/Robb\\\_Elementary\\\_School\\\_shooting](https://en.wikipedia.org/wiki/Robb\\_Elementary\\_School\\_shooting)

\[2] [https://www.gunviolencearchive.org/](https://www.gunviolencearchive.org/)


Built with [Mintlify](https://mintlify.com).