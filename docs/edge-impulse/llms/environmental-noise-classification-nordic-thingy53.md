# Source: https://docs.edgeimpulse.com/projects/expert-network/environmental-noise-classification-nordic-thingy53.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Environmental Noise Classification - Nordic Thingy:53

Created By: Attila Tokes

Public Project Link: [https://studio.edgeimpulse.com/public/146039/latest](https://studio.edgeimpulse.com/public/146039/latest)

## Project Demo

<iframe src="https://www.youtube.com/embed/j1eY-dFecYs" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Intro

Noise pollution can be a significant problem especially in densely populated urban areas. It can have negative effects both humans and the wildlife. Also, noise pollution is often caused by power hungry activities, such as industrial processes, constructions, flights, etc.

A Noise Pollution Monitoring device built on top of the Nordic Thingy:53 development kit, with smart classification capabilities using Edge Impulse can be a good way to monitor this phenomenon in urban areas. Using a set of Noise Pollution Monitoring the noise / environmental pollution from a city can be monitored. Based on the measured data, actions can be taken to improve the situation. Activities causing noise pollution tend to also have a high energy consumption. Replacing this applications with more efficient solutions can reduce their energy footprint they have.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UCyWLrPSEZAmkQ7M/.assets/images/environmental-noise-classification/00-cover.jpg?fit=max&auto=format&n=UCyWLrPSEZAmkQ7M&q=85&s=f18a41eed7cc287dbe29c2609aa0cea5" width="486" height="393" data-path=".assets/images/environmental-noise-classification/00-cover.jpg" />
</Frame>

In this project I will demonstrate how a low power device like the Nordic Thingy:53 can be used in conjunction with an edge machine learning platform like Edge Impulse to build a smart noise / environmental pollution monitor. The PDM microphone of the Nordic Thingy:53 will be used to capture environmental noise. A digital signal processing (DSP) and Inference pipeline built using Edge Impulse will be used to classify audio samples of know activities like construction works, traffic and others.

## Getting Started with the Thingy:53

The Nordic Thingy:53 is comes with the pre-installed firmware, that allows us to easily create machine learning projects with Edge Impulse.

The [nRF Edge Impulse](https://play.google.com/store/apps/details?id=no.nordicsemi.android.nrfei) mobile app is used to interact with Thingy:53. The app also integrates with the [Edge Impulse](https://www.edgeimpulse.com/) embedded machine learning platform.

To get started with the app we will need to create an Edge Impulse account, and a project:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UCyWLrPSEZAmkQ7M/.assets/images/environmental-noise-classification/m-01-create-project-p40.jpg?fit=max&auto=format&n=UCyWLrPSEZAmkQ7M&q=85&s=8062488e530285f3073a012f743c4182" width="432" height="936" data-path=".assets/images/environmental-noise-classification/m-01-create-project-p40.jpg" />
</Frame>

After this we should be able to detect the Thingy:53 in the Devices tab. The thingy will show up as a device named EdgeImpulse.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UCyWLrPSEZAmkQ7M/.assets/images/environmental-noise-classification/m-02-connect-device-p40.jpg?fit=max&auto=format&n=UCyWLrPSEZAmkQ7M&q=85&s=3546e619e9cf7ef8a88ad1893c2f4f0f" width="432" height="936" data-path=".assets/images/environmental-noise-classification/m-02-connect-device-p40.jpg" />
</Frame>

Going to the Inference tab we can try out the pre-installed demo app, which uses the accelerometer data to detect 4 types of movement.

## Collecting Audio Data

The first step of building a machine learning model is to collect some training data.

For this proof-of-concept, I decided to go with 4 classes of sounds:

* **Silence** - a silent room
* **Nature** - sound of birds, rain, etc.
* **Construction** - sounds from a construction site
* **Traffic** - urban traffic sounds

A the source of the audio samples I used a number of Youtube videos, listed in the Resources section.

The audio sample can be collected from the Data tab of the nRF Edge Impulse app:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UCyWLrPSEZAmkQ7M/.assets/images/environmental-noise-classification/m-03-capture-p40.jpg?fit=max&auto=format&n=UCyWLrPSEZAmkQ7M&q=85&s=f74bfaa56a0e8755126b8a792ddec472" width="432" height="936" data-path=".assets/images/environmental-noise-classification/m-03-capture-p40.jpg" />
</Frame>

The audio samples are automatically uploaded to the Edge Impulse Studio project, and should show up in the Data Acquisition tab:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UCyWLrPSEZAmkQ7M/.assets/images/environmental-noise-classification/01-samples.jpg?fit=max&auto=format&n=UCyWLrPSEZAmkQ7M&q=85&s=c8ec6e9573b379f017785b38b1f01f82" width="1600" height="809" data-path=".assets/images/environmental-noise-classification/01-samples.jpg" />
</Frame>

By default all the samples will be put in the Train set. We also need a couple of samples for verification, so we will need to run a Train / Test split:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UCyWLrPSEZAmkQ7M/.assets/images/environmental-noise-classification/02-train-test-split.jpg?fit=max&auto=format&n=UCyWLrPSEZAmkQ7M&q=85&s=5008fa0ca1271a27204809b7d263d380" width="864" height="857" data-path=".assets/images/environmental-noise-classification/02-train-test-split.jpg" />
</Frame>

After this we should have approximately 80% of samples in the Train set, and 20% in the Test set:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UCyWLrPSEZAmkQ7M/.assets/images/environmental-noise-classification/03-train-test-splitted.jpg?fit=max&auto=format&n=UCyWLrPSEZAmkQ7M&q=85&s=39838bb4cde5492e59815dff95e6b57b" width="946" height="95" data-path=".assets/images/environmental-noise-classification/03-train-test-splitted.jpg" />
</Frame>

## Training an Audio Classification Model

Having the audio data, we can start building a machine learning model.

In Edge Impulse project the machine learning pipeline is called an Impulse. An impulse includes the pre-processing, feature extraction and inference steps needed to classify, in our case, audio data.

For this project I went will the following design:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UCyWLrPSEZAmkQ7M/.assets/images/environmental-noise-classification/04-impulse.jpg?fit=max&auto=format&n=UCyWLrPSEZAmkQ7M&q=85&s=7679f888c49f8909e8a8b170b647c4e6" width="1479" height="876" data-path=".assets/images/environmental-noise-classification/04-impulse.jpg" />
</Frame>

* **Time Series Data Input** - with 1 second windows @ 16kHz
* **Audio (MFE) Extractor** - this is the recommended feature extractor for non-voice audio
* **NN** / **Keras Classifier** - a neural network classifier
* **Output with 4 Classes** - Silence, Nature, Traffic, Construction

The impulse blocks were trained mostly with the default settings. The feature extraction block looks like follows:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UCyWLrPSEZAmkQ7M/.assets/images/environmental-noise-classification/05-feature-extract.jpg?fit=max&auto=format&n=UCyWLrPSEZAmkQ7M&q=85&s=eb021aa585117e2e5bf79efce7117e5a" width="1600" height="795" data-path=".assets/images/environmental-noise-classification/05-feature-extract.jpg" />
</Frame>

This is followed by the classification block:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UCyWLrPSEZAmkQ7M/.assets/images/environmental-noise-classification/06-training-output.jpg?fit=max&auto=format&n=UCyWLrPSEZAmkQ7M&q=85&s=fcb31bae400ab464b209ed64fcdd30e0" width="1600" height="839" data-path=".assets/images/environmental-noise-classification/06-training-output.jpg" />
</Frame>

The resulting model is surprisingly good:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UCyWLrPSEZAmkQ7M/.assets/images/environmental-noise-classification/07-training-accuracy.jpg?fit=max&auto=format&n=UCyWLrPSEZAmkQ7M&q=85&s=51dabcb5ef9fa4d3bdd7940638ec8de9" width="1087" height="929" data-path=".assets/images/environmental-noise-classification/07-training-accuracy.jpg" />
</Frame>

Most of the test samples were correctly classified. We only have a couple of mismatches for the Traffic / Construction and Silence / Nature classes. This is however expected, as these sounds can be pretty similar.

## Deploying the Model on the Thingy:53

Building an deploying an embedded application including machine learning used to involve a couple of steps. With the Thingy:53 and Edge Impulse this become much easier.

We just need to go to the Deployment tab, and hit Deploy. The model will automatically start building:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UCyWLrPSEZAmkQ7M/.assets/images/environmental-noise-classification/m-04-build-n-deploy-p40.jpg?fit=max&auto=format&n=UCyWLrPSEZAmkQ7M&q=85&s=dfff88852646e5e0738d405cff058851" width="432" height="936" data-path=".assets/images/environmental-noise-classification/m-04-build-n-deploy-p40.jpg" />
</Frame>

A couple of minutes later the model is built and deployed on our Thingy:53:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/UCyWLrPSEZAmkQ7M/.assets/images/environmental-noise-classification/m-05-test-p40.jpg?fit=max&auto=format&n=UCyWLrPSEZAmkQ7M&q=85&s=90e1bf33a251a15dc2ad79617ab50fed" width="432" height="936" data-path=".assets/images/environmental-noise-classification/m-05-test-p40.jpg" />
</Frame>

## Running Live Inference on the Thingy:53

The Deployment we did earlier should have been uploaded a firmware with the new model on the Thingy:53. Hitting Start on the Inference will start live classification on the device.

I tested the application out with new audio samples for each class:

<iframe src="https://www.youtube.com/embed/j1eY-dFecYs" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## A Network of Devices

In future versions this project could be extended to also include features like:

* Noise level / decibel measurement
* Cloud connectivity via Bluetooth Mesh / Thread
* Solar panel charging

A network of such monitoring devices could be used to monitor the noise / environmental pollution in a city. Based on the collected data high impact / polluting activities can be identified, and can be replaced with better alternatives.

## Resources

**Edge Impulse Project**: [https://studio.edgeimpulse.com/studio/146039](https://studio.edgeimpulse.com/studio/146039)

**Nordic Thingy:53**: [https://www.nordicsemi.com/Products/Development-hardware/Nordic-Thingy-53](https://www.nordicsemi.com/Products/Development-hardware/Nordic-Thingy-53)

**Edge Impulse Documentation**: [https://docs.edgeimpulse.com/](/)

**Sound Sources**:

* Construction: [10 Hours of Construction Sound | Amazing Sounds with Peter Baeten](https://www.youtube.com/watch?v=AB4Ov9t4aq4) (Sunville Sounds)
* Nature: [Bird Watching 4K with bird sounds to relax and study | A day in the backyard](https://www.youtube.com/watch?v=KCl85UpJYZU) (Sunville Sounds) [Beautiful Afternoon In Nature With Singing Birds \~ Stories With Peter Baeten](https://www.youtube.com/watch?v=qvabR_rsfn0) (Sunville Sounds) [Gentle Rain Sounds on Window \~ Calming Rain For Sleeping & Relaxing | Rain Sounds with Peter Baeten](https://www.youtube.com/watch?v=AstZaueBF14) (Sunville Sounds)
* Traffic: [Busy Traffic Sound Effects](https://www.youtube.com/watch?v=YvXK_MPSY0c) (All Things Sound) [Heavy Traffic Sound Effects | Bike Riding in Traffic Roads Sounds | Zoom Hn1 Indian Roads FreeSounds](https://www.youtube.com/watch?v=tt-IbRmIwkM) (To Know Everything) [City Traffic Sounds for Sleep | Highway Ambience at Night | 10 Hours ASMR White Noise](https://www.youtube.com/watch?v=fh3EdeGNKus) (Nomadic Ambience)


Built with [Mintlify](https://mintlify.com).