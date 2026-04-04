# Source: https://docs.edgeimpulse.com/tutorials/hardware/particle-photon2-audio-even-detection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Particle Photon 2 - audio event detection

In this tutorial, you'll use machine learning to build a model that recognizes when a doorbell rings. You'll use the Particle Photon 2, a microphone, a cell phone, and Edge Impulse to build this project. You can add the ability to send an SMS message when the doorbell rings by following the tutorial on [Particle's website](https://docs.particle.io/getting-started/machine-learning/machine-learning/).

Audio event detection is a common machine learning task, and is a hard task to solve using rule-based programming. You'll learn how to collect audio data, build a neural network classifier, and how to deploy your model back to a device. At the end of this tutorial, you'll have a firm understanding of applying machine learning on Particle hardware using Edge Impulse.

<Info>
  **Before starting the tutorial**

  After signing up for a free Edge Impulse account, clone the finished project, including all training data, signal processing and machine learning blocks here: [Particle - Doorbell](https://studio.edgeimpulse.com/public/237590/latest). At the end of the process you will have the full project that comes pre-loaded with training and test datasets.
</Info>

## 1. Prerequisites

For this tutorial you'll need the:

* [Particle Photon2 Board](/hardware/boards/particle-photon-2) with the [Edge ML Kit](https://docs.particle.io/reference/datasheets/accessories/edge-ml-kit/).

Before starting ingestion create an [Edge Impulse account](https://studio.edgeimpulse.com/signup) if you haven't already. To collect audio data you can use [any mobile phone](/hardware/devices/mobile-phone). Follow in the instructions on that page to connect your phone to your Edge Impulse project.

Once your device is connected under **Devices** in the studio you can proceed:

<Frame caption="Devices page showing a mobile phone as a connected device">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/abc9ebe-screenshot_2020-04-03_at_100939.png?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=ab97879d9411fe809388085625cc8d60" width="1169" height="358" data-path=".assets/images/abc9ebe-screenshot_2020-04-03_at_100939.png" />
</Frame>

## 2. Collecting your first data

To build this project, you'll need to collect some audio data that will be used to train the machine learning model. Since the goal is to detect the sound of a doorbell, you'll need to collect some examples of that. You'll also need some examples of typical background noise that *doesn't* contain the sound of a doorbell, so the model can learn to discriminate between the two. These two types of examples represent the two *classes* we'll be training our model to detect: unknown noise, or doorbell.

Your phone will show up like any other device in Edge Impulse, and will automatically ask permission to use sensors. Let's start by recording an example of background noise that doesn't contain the sound of a doorbell. On your cell set the label to `unknown`, the sample length to 2 seconds. This indicates that you want to record 1 second of audio, and label the recorded data as `unknown`. You can later edit these labels if needed.

After you click **Start recording**, the device will capture a second of audio and transmit it to Edge Impulse.

When the data has been uploaded, you will see a new line appear under 'Collected data' in the **Data acquisition** tab of your Edge Impulse project. You will also see the waveform of the audio in the 'RAW DATA' box. You can use the controls underneath to listen to the audio that was captured.

<Frame caption="Audio waveform">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/69ef343-screen_shot_2020-01-22_at_40810_pm.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=ebd33707708342e3cf90c4542bebf211" width="588" height="585" data-path=".assets/images/69ef343-screen_shot_2020-01-22_at_40810_pm.png" />
</Frame>

Machine learning works best with lots of data, so a single sample won't cut it. Now is the time to start building your own dataset. For example, use the following two classes, and record around 3 minutes of data per class:

* **doorbell** - Record yourself ringing the doorbell in the same room
* **unknown** - Record the background noise in your house

## 3. Designing an impulse

With the training set in place you can design an impulse. An impulse takes the raw data, slices it up in smaller windows, uses signal processing blocks to extract features, and then uses a learning block to classify new data. Signal processing blocks always return the same values for the same input and are used to make raw data easier to process, while learning blocks learn from past experiences.

For this tutorial we'll use the  signal processing block. Then we'll use a 'Neural Network' learning block, that takes these generated features and learns to distinguish between our different classes (circular or not).

In the studio go to **Create impulse**, set the window size to `1000` (you can click on the `1000 ms.` text to enter an exact value), the window increase to `500`, and add the 'Audio MFCC' and 'Classification (Keras)' blocks. Then click **Save impulse**.

<Frame caption="Impulse with processing and learning blocks">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/particle/particle-doorbell-impulse.png?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=d342c7304d3fa2a0bbd4a01d8e32e103" width="1600" height="646" data-path=".assets/images/particle/particle-doorbell-impulse.png" />
</Frame>

### Configuring the MFCC block

Now that we've assembled the building blocks of our Impulse, we can configure each individual part. Click on the **MFCC** tab in the left hand navigation menu. You'll see a page that looks like this:

<Frame caption="The MFCC page.">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/0799fa6-screenshot_2021-07-14_at_104710.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=8537a0346d08936c84346efca59d8067" width="1054" height="1000" data-path=".assets/images/0799fa6-screenshot_2021-07-14_at_104710.png" />
</Frame>

This page allows you to configure the MFCC block, and lets you preview how the data will be transformed. The right of the page shows a visualization of the MFCC's output for a piece of audio, which is known as a [spectrogram](/studio/projects/processing-blocks/blocks/spectrogram).

The MFCC block transforms a window of audio into a table of data where each row represents a range of frequencies and each column represents a span of time. The value contained within each cell reflects the amplitude of its associated range of frequencies during that span of time. The spectrogram shows each cell as a colored block, the intensity which varies depends on the amplitude.

The patterns visible in a spectrogram contain information about what type of sound it represents. For example, the spectrogram in this image shows a pattern typical of background noise:

<Frame caption="Spectrogram of background noise.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/3f66ee2-screenshot_2021-07-14_at_105147.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=19ec3eaa70eed5897090ff5e2e71e115" width="482" height="197" data-path=".assets/images/3f66ee2-screenshot_2021-07-14_at_105147.png" />
</Frame>

It's interesting to explore your data and look at the types of spectrograms it results in. You can use the dropdown box near the top right of the page to choose between different audio samples to visualize, and drag the white window on the audio waveform to select different windows of data:

<Frame caption="Audio waveform and sample dropdown box.">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/9e69c0f-screen_shot_2020-01-23_at_124438_pm.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=cee0f489453c87400900a80b89b33635" width="1600" height="255" data-path=".assets/images/9e69c0f-screen_shot_2020-01-23_at_124438_pm.png" />
</Frame>

There are a lot of different ways to configure the MFCC block, as shown in the Parameters box:

<Frame caption="The MFCC parameters box.">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/8089784-screenshot_2021-07-14_at_105247.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=7b3d71f1d6f18ef119bf25b5737da91d" width="548" height="691" data-path=".assets/images/8089784-screenshot_2021-07-14_at_105247.png" />
</Frame>

Handily, Edge Impulse provides sensible defaults that will work well for many use cases, so we can leave these values unchanged. You can play around with the noise floor to quickly see the effect it has on the spectrogram.

The spectrograms generated by the MFCC block will be passed into a neural network architecture that is particularly good at learning to recognize patterns in this type of tabular data. Before training our neural network, we'll need to generate MFCC blocks for all of our windows of audio. To do this, click the *Generate features* button at the top of the page, then click the green *Generate features* button. If you have a full 10 minutes of data, the process will take a while to complete:

<Frame caption="Running the feature generation process.">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/e5c68bc-screen_shot_2020-01-23_at_125821_pm.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=39a328d479a9df3279574782df6c7fa9" width="805" height="1000" data-path=".assets/images/e5c68bc-screen_shot_2020-01-23_at_125821_pm.png" />
</Frame>

Once this process is complete the feature explorer shows a visualization of your dataset. Here dimensionality reduction is used to map your features onto a 3D space, and you can use the feature explorer to see if the different classes separate well, or find mislabeled data (if it shows in a different cluster). You can find more information in [visualizing complex datasets](https://edgeimpulse.com/blog/visualizing-complex-datasets-in-edge-impulse/).

Next, we'll configure the neural network and begin training.

### Configuring the neural network

With all data processed it's time to start training a neural network. Neural networks are algorithms, modeled loosely after the human brain, that can learn to recognize patterns that appear in their training data. The network that we're training here will take the MFCC as an input, and try to map this to one of two classes—doorbell or unknown.

Click on **NN Classifier** in the left hand menu. You'll see the following page:

<Frame caption="The NN Classifier page.">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/8db3def-screen_shot_2020-01-23_at_10928_pm.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=775247e152f1760dee777bcab1d87454" width="1600" height="911" data-path=".assets/images/8db3def-screen_shot_2020-01-23_at_10928_pm.png" />
</Frame>

A neural network is composed of layers of virtual "neurons", which you can see represented on the left hand side of the NN Classifier page. An input—in our case, an MFCC spectrogram—is fed into the first layer of neurons, which filters and transforms it based on each neuron's unique internal state. The first layer's output is then fed into the second layer, and so on, gradually transforming the original input into something radically different. In this case, the spectrogram input is transformed over four intermediate layers into just two numbers: the probability that the input represents noise, and the probability that the input represents a doorbell.

During training, the internal state of the neurons is gradually tweaked and refined so that the network transforms its input in *just* the right ways to produce the correct output. This is done by feeding in a sample of training data, checking how far the network's output is from the correct answer, and adjusting the neurons' internal state to make it more likely that a correct answer is produced next time. When done thousands of times, this results in a trained network.

A particular arrangement of layers is referred to as an *architecture*, and different architectures are useful for different tasks. The default neural network architecture provided by Edge Impulse will work well for our current project, but you can also define your own architectures. You can even import custom neural network code from tools used by data scientists, such as TensorFlow and Keras.

The default settings should work, and to begin training, click **Start training**. You'll see a lot of text flying past in the *Training output* panel, which you can ignore for now. Training will take a few minutes. When it's complete, you'll see the *Model* panel appear at the right side of the page.

Congratulations, you've trained a neural network with Edge Impulse! But what do all these numbers mean?

At the start of training, 20% of the training data is set aside for *validation*. This means that instead of being used to train the model, it is used to evaluate how the model is performing. The *Last training performance* panel displays the results of this validation, providing some vital information about your model and how well it is working. Bear in mind that your exact numbers may differ from the ones in this tutorial.

On the left hand side of the panel, *Accuracy* refers to the percentage of windows of audio that were correctly classified. The higher number the better, although an accuracy approaching 100% is unlikely, and is often a sign that your model has *overfit* the training data. You will find out whether this is true in the next stage, during model testing. For many applications, an accuracy above 80% can be considered very good.

The *Confusion matrix* is a table showing the balance of correctly versus incorrectly classified windows. To understand it, compare the values in each row.

The *On-device performance* region shows statistics about how the model is likely to run on-device. *Inferencing time* is an estimate of how long the model will take to analyze one second of data on a typical microcontroller (here: an Arm Cortex-A33 running at 200MHz). *Peak memory usage* gives an idea of how much RAM will be required to run the model on-device.

## 4. Classifying new data

The performance numbers in the previous step show that our model is working well on its training data, but it's extremely important that we test the model on new, unseen data before deploying it in the real world. This will help us ensure the model has not learned to overfit the training data, which is a common occurrence.

Edge Impulse provides some helpful tools for testing our model, including a way to capture live data from your device and immediately attempt to classify it. To try it out, click on **Live classification** in the left hand menu. Your device should show up in the 'Classify new data' panel. Capture 5 seconds of background noise by clicking **Start sampling**.

The sample will be captured, uploaded, and classified. Once this has happened, you'll see a breakdown of the results.

Once the sample is uploaded, it is split into windows–in this case, a total of 41. These windows are then classified. As you can see, our model classified all 41 windows of the captured audio as *noise*. This is a great result! Our model has correctly identified that the audio was background noise, even though this is new data that was not part of its training set.

Of course, it's possible some of the windows may be classified incorrectly. If your model didn't perform perfectly, don't worry. We'll get to troubleshooting later.

<Warning>
  **Misclassifications and uncertain results**

  It's inevitable that even a well-trained machine learning model will sometimes misclassify its inputs. When you integrate a model into your application, you should take into account that it will not always give you the correct answer.

  For example, if you are classifying audio, you might want to classify several windows of data and average the results. This will give you better overall accuracy than assuming that every individual result is correct.
</Warning>

## 5. Model testing

Using the *Live classification* tab, you can easily try out your model and get an idea of how it performs. But to be really sure that it is working well, we need to do some more rigorous testing. That's where the *Model testing* tab comes in. If you open it up, you'll see the sample we just captured listed in the *Test data* panel.

In addition to its training data, every Edge Impulse project also has a test dataset. Samples captured in *Live classification* are automatically saved to the test dataset, and the *Model testing* tab lists all of the test data.

To use the sample we've just captured for testing, we should correctly set its expected outcome. Click the `⋮` icon and select **Edit expected outcome**, then enter `noise`. Now, select the sample using the checkbox to the left of the table and click **Classify selected**.

You'll see that the model's accuracy has been rated based on the test data. Right now, this doesn't give us much more information that just classifying the same sample in the *Live classification* tab. But if you build up a big, comprehensive set of test samples, you can use the *Model testing* tab to measure how your model is performing on real data.

Ideally, you'll want to collect a test set that contains a minimum of 25% the amount of data of your training set. So, if you've collected 10 minutes of training data, you should collect at least 2.5 minutes of test data. You should make sure this test data represents a wide range of possible conditions, so that it evaluates how the model performs with many different types of inputs. For example, collecting test audio for several different doorbells, perhaps moving collecting the audio in a different room, is a good idea.

You can use the *Data acquisition* tab to manage your test data. Open the tab, and then click **Test data** at the top. Then, use the *Record new data* panel to capture a few minutes of test data, including audio for both background noise and doorbells. Make sure the samples are labelled correctly. Once you're done, head back to the *Model testing* tab, select all the samples, and click **Classify selected**.

The screenshot shows classification results from a large number of test samples (there are more on the page than would fit in the screenshot). It's normal for a model to perform less well on entirely fresh data.

For each test sample, the panel shows a breakdown of its individual performance. Samples that contain a lot of misclassifications are valuable, since they have examples of types of audio that our model does not currently fit. It's often worth adding these to your training data, which you can do by clicking the `⋮` icon and selecting **Move to training set**. If you do this, you should add some new test data to make up for the loss!

Testing your model helps confirm that it works in real life, and it's something you should do after every change. However, if you often make tweaks to your model to try to improve its performance on the test dataset, your model may gradually start to overfit to the test dataset, and it will lose its value as a metric. To avoid this, continually add fresh data to your test dataset.

<Danger>
  **Data hygiene**

  It's extremely important that data is never duplicated between your training and test datasets. Your model will naturally perform well on the data that it was trained on, so if there are duplicate samples then your test results will indicate better performance than your model will achieve in the real world.
</Danger>

## 6. Model troubleshooting

If the network performed great, fantastic! But what if it performed poorly? There could be a variety of reasons, but the most common ones are:

1. The data does not look like other data the network has seen before. This is common when someone uses the device in a way that you didn't add to the test set. You can add the current file to the test set by adding the correct label in the 'Expected outcome' field, clicking `⋮`, then selecting **Move to training set**.
2. The model has not been trained enough. Increase number of epochs to `200` and see if performance increases (the classified file is stored, and you can load it through 'Classify existing validation sample').
3. The model is overfitting and thus performs poorly on new data. Try reducing the number of epochs, reducing the learning rate, or adding more data.
4. The neural network architecture is not a great fit for your data. Play with the number of layers and neurons and see if performance improves.

As you see, there is still a lot of trial and error when building neural networks. Edge Impulse is continually adding features that will make it easier to train an effective model.

## 7. Deploying to your device

With the impulse designed, trained and verified you can deploy this model back to your device. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption.

To export your model, click on **Deployment** in the menu. Then under 'Build firmware' select the **Particle Library**.

## 8. Flashing the device

Once optimized parameters have been found, you can click **Build**. This will build a particle workbench compatible package that will run on your development board. After building is completed you'll get prompted to download a zipfile. Save this on your computer. A pop-up video will show how the download process works.

After unzipping the downloaded file, you can open the project in Particle Workbench.

### Flash a Particle Photon 2 Project

The development board does not come with the Edge Impulse firmware. To flash the Edge Impulse firmware:

1. Open a new VS Code window, ensure that Particle Workbench has been installed (see above)
2. Use [VS Code Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) and type in **Particle: Import Project**
   1. Select the `project.properties` file in the directory that you just downloaded and extracted from the section above.
3. Use [VS Code Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) and type in **Particle: Configure Project for Device**
   1. Select **`deviceOS@5.3.2` (or a later version)**
   2. Choose a target. (e.g. **P2** , this option is also used for the Photon 2).
4. It is sometimes needed to manually put your Device into DFU Mode. You may proceed to the next step, but if you get an error indicating that "No DFU capable USB device available" then please follow these step.
   1. Hold down both the **RESET** and **MODE** buttons.
   2. Release only the **RESET** button, while holding the **MODE** button.
   3. Wait for the LED to start flashing yellow.
   4. Release the **MODE** button.
5. Compile and Flash in one command with: **Particle: Flash application & DeviceOS (local)**

<Warning>
  **Local Compile Only!**
  At this time you cannot use the **Particle: Cloud Compile** or **Particle: Cloud Flash** options; local compilation is required.
</Warning>

<iframe src="https://www.youtube.com/embed/A_twb-ategU" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

##### Serial Connection to Computer

The Particle libraries generated by Edge Impulse have serial output through a virtual COM port on the serial cable. The serial settings are 115200, 8, N, 1. Particle Workbench contains a serial monitor accessible via **Particle: Serial Monitor** via the VS Code Command Palette.

<Info>
  **Device compatibility**

  Initial release of the particle integration will rely on the particle-ingestion project and the data forwarder to be installed on the device and computer. This is currently only supported on the Particle Photon 2, but should run on other devices as well.
</Info>

### Stand Alone Example with Static Buffer

This standalone example project contains minimal code required to run the imported impulse on the device. This code is located in `main.cpp`. In this minimal code example, inference is run from a static buffer of input feature data. To verify that our embedded model achieves the exact same results as the model trained in Studio, we want to copy the same input features from Studio into the static buffer in `main.cpp`.

To do this, first head back to Edge Impulse Studio and click on the **Live classification** tab. Follow this video for instructions.

<iframe src="https://www.youtube.com/embed/HdkktDbPhxE" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

In `main.cpp` paste the raw features inside the `static const float features[]` definition, for example:

```cpp  theme={"system"}
static const float features[] = {
    -19.8800, -0.6900, 8.2300, -17.6600, -1.1300, 5.9700, ...
};
```

The project will repeatedly run inference on this buffer of raw features once built. This will show that the inference result is identical to the **Live classification** tab in Studio. Use new sensor data collected in real time on the device to fill a buffer. From there, follow the same code used in `main.cpp` to run classification on live data.

### Running the model on the device

Follow the flashing instructions above to run on device.

Victory! You've now built your first on-device machine learning model.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/4eed33c-ezgif-3-8cebec2be387.gif?s=57b978fa5888ca591a8c2f1e4ea67b3a" width="480" height="360" data-path=".assets/images/4eed33c-ezgif-3-8cebec2be387.gif" />
</Frame>

## 7. Conclusion

Congratulations! Now that you've trained and deployed your model you can go further and build your own custom firmware. We can't wait to see what you'll build! 🚀


Built with [Mintlify](https://mintlify.com).