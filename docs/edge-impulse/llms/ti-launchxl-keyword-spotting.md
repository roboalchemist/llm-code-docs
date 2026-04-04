# Source: https://docs.edgeimpulse.com/tutorials/hardware/ti-launchxl-keyword-spotting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TI LaunchXL - keyword spotting

In this tutorial, you'll use machine learning to build a system that can recognize audible events, particularly your voice through *audio classification*. The system you create will work similarly to "Hey Siri" or "OK, Google" and is able to recognize keywords or other audible events, even in the presence of other background noise or background chatter.

You'll learn how to collect audio data from microphones, use signal processing to extract the most important information, and train a deep neural network that can tell you whether your keyword was heard in a given clip of audio. Finally, you'll deploy the system to an embedded device and evaluate how well it works.

At the end of this tutorial, you'll have a firm understanding of how to classify audio using Edge Impulse.

You can view the finished project, including all data, signal processing and machine learning blocks here: [Tutorial: responding to your voice](https://studio.edgeimpulse.com/public/14225/latest).

<Info>
  **Detect non-voice audio?**

  We have a tutorial for that too! See [Sound recognition](/tutorials/hardware/ti-launchxl-sound-recognition).
</Info>

### 1. Prerequisites

For this tutorial you'll need a supported device. Follow the steps to connect your development board to Edge Impulse.

* [ST B-L475E-IOT01A](/hardware/boards/st-b-l475e-iot01a)
* [Arduino Nano 33 BLE Sense](/hardware/boards/arduino-nano-33-ble-sense)
* [Arduino Portenta H7 + Vision shield](/hardware/boards/arduino-portenta-h7)
* [Espressif ESP-EYE (ESP32)](/hardware/boards/espressif-esp32)
* [Himax WE-I Plus](/hardware/boards/himax-we-i-plus)
* [Nordic Semiconductor nRF52840 DK](/hardware/boards/nordic-semi-nrf52840-dk)
* [Nordic Semiconductor nRF5340 DK](/hardware/boards/nordic-semi-nrf5340-dk)
* [Nordic Semiconductor nRF9160 DK](/hardware/boards/nordic-semi-nrf9160-dk)
* [Silicon Labs Thunderboard Sense 2](/hardware/boards/silabs-thunderboard-sense-2)
* [Sony's Spresense](/hardware/boards/sony-spresense)
* [Raspberry Pi Pico](/hardware/boards/raspberry-pi-pico)
* [NVIDIA Jetson Orin and Nano](/hardware/boards/nvidia-jetson)
* [Any mobile phone](/hardware/devices/mobile-phone) - the easiest option if you don't have one of the above.

If your device is connected under **Devices** in the studio you can proceed:

<Frame caption="Devices tab with the device connected to the remote management interface.">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/cffb2f5-screenshot_2020-11-19_at_215231.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=3a200446ce130e489c5aa2c3c5903382" width="1190" height="373" data-path=".assets/images/cffb2f5-screenshot_2020-11-19_at_215231.png" />
</Frame>

<Info>
  **Device compatibility**

  Edge Impulse can ingest data from any device - including embedded devices that you already have in production. See the documentation for the [Ingestion API](/apis/ingestion) for more information.
</Info>

### 2. Collecting your first data

In this tutorial we want to build a system that recognizes keywords, so your first job is to think of a great one. It can be your name, an action, or even a growl - it's your party. Do keep in mind that some keywords are harder to distinguish from others, and especially keywords with only one syllable (like 'One') might lead to false-positives (e.g. when you say 'Gone'). This is the reason that Apple, Google and Amazon all use at least three-syllable keywords ('Hey Siri', 'OK, Google', 'Alexa'). A good one would be "Hello world".

To collect your first data, go to **Data acquisition**, set your keyword as the label, set your sample length to 10s., your sensor to 'microphone' and your frequency to 16KHz. Then click **Start sampling** and start saying your keyword over and over again (with some pause in between).

<Frame caption="Recording your keyword from the Studio.">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/ab97e9d-screenshot_2020-11-19_at_215957.png?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=4c912133284dce047eb60f9648877cde" width="569" height="476" data-path=".assets/images/ab97e9d-screenshot_2020-11-19_at_215957.png" />
</Frame>

> **Note:** Data collection from a development board might be slow, you can use your [Mobile phone](/hardware/devices/mobile-phone) as a sensor to make this much faster.

Afterwards you have a file like this, clearly showing your keywords, separated by some noise.

!\[10 seconds of 'Hello world' data]\(/.assets/images/68a7c9e-screenshot\_2020-11-19\_at\_221857.png", "Screenshot 2020-11-19 at 22.18.57.png)

This data is not suitable for Machine Learning yet though. You will need to cut out the parts where you say your keyword. This is important because you only want the actual keyword to be labeled as such, and not accidentally label noise, or incomplete sentences (e.g. only "Hello"). Fortunately the Edge Impulse Studio can do this for you. Click `⋮` next to your sample, and select **Split sample**.

<Frame caption="'Split sample' automatically cuts out the interesting parts of an audio file.">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-acquisition-split.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=28fb72bd105d6f297c1bbefc6901fc23" width="1137" height="643" data-path=".assets/images/data-acquisition-split.png" />
</Frame>

If you have a short keyword, enable *Shift samples* to randomly shift the sample around in the window, and then click **Split**. You now have individual 1s. long samples in your dataset. Perfect!

### 3. Building your dataset

Now that you know how to collect data we can consider other data we need to collect. In addition to your keyword we'll also need audio that is *not* your keyword. Like background noise, the TV playing ('noise' class), and humans saying other words ('unknown' class). This is required because a machine learning model has no idea about right and wrong (unless those are your keywords), but only learns from the data you feed into it. The more varied your data is, the better your model will work.

For each of these three classes ('your keyword', 'noise', and 'unknown') you want to capture an even amount of data (balanced datasets work better) - and for a decent keyword spotting model you'll want *at least* 10 minutes in each class (but, the more the better).

Thus, collect 10 minutes of samples for your keyword - do this in the same manner as above. The fastest way is probably through your mobile phone, collecting 1 minute clips, then automatically splitting this data. Make sure to capture wide variations of the keyword: leverage your family and your colleagues to help you collect the data, make sure you cover high and low pitches, and slow and fast speakers.

For the noise and unknown datasets you can either collect this yourself, or make your life a bit easier by using dataset of both 'noise' (all kinds of background noise) and 'unknown' (random words) data that we built for you here: [Keyword Spotting Dataset](/datasets/audio/keyword-spotting).

To import this data, go to **Data acquisition**, click the *Upload* icon, and select a number of 'noise' or 'unknown' samples (there's 25 minutes of each class, but you can select less files if you want), and clicking **Begin upload**. The data is automatically labeled and added to your project.

<Frame caption="Importing the noise and unknown data into your project">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/1f97a38-screenshot_2020-11-19_at_222610.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=685d4bea246fce6f3d922f6aede0fe52" width="590" height="710" data-path=".assets/images/1f97a38-screenshot_2020-11-19_at_222610.png" />
</Frame>

#### Rebalancing your dataset

If you've collected all your training data through the 'Record new data' widget you'll have all your keywords in the 'Training' dataset. This is not great, because you want to keep 20% of your data separate to validate the machine learning model. To mitigate this you can go to **Dashboard** and select **Perform train/test split**. This will automatically split your data between a training class (80%) and a testing class (20%). Afterwards you should see something like this:

<Frame caption="Training data, showing an even split between the three classes">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/90114a4-screenshot_2020-11-19_at_223533.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=24ccd5c3d769844b043d427e8656b726" width="592" height="231" data-path=".assets/images/90114a4-screenshot_2020-11-19_at_223533.png" />
</Frame>

<br />

<Frame caption="Testing data, also showing an even split between the three classes">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/19751b9-screenshot_2020-11-19_at_223548.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=5c19b47b5a5e1b0db067e1dfb3ca284d" width="593" height="228" data-path=".assets/images/19751b9-screenshot_2020-11-19_at_223548.png" />
</Frame>

### 4. Designing your impulse

With the data set in place you can design an impulse. An impulse takes the raw data, slices it up in smaller windows, uses signal processing blocks to extract features, and then uses a learning block to classify new data. Signal processing blocks always return the same values for the same input and are used to make raw data easier to process, while learning blocks learn from past experiences.

For this tutorial we'll use the "MFCC" signal processing block. MFCC stands for Mel Frequency Cepstral Coefficients. This sounds scary, but it's basically just a way of turning raw audio—which contains a large amount of redundant information—into simplified form. Edge Impulse has many other processing blocks for audio, including "MFE" and the "Spectrogram" blocks for non-voice audio, but the "MFCC" block is great for dealing with human speech.

We'll then pass this simplified audio data into a Neural Network block, which will learn to distinguish between the three classes of audio.

In the Studio, go to the **Create impulse** tab, add a *Time series data*, an *Audio (MFCC)* and a *Classification (Keras)* block. Leave the window size to 1 second (as that's the length of our audio samples in the dataset) and click **Save Impulse**.

<Frame caption="An impulse to classify human speech">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/6556142-screenshot_2020-11-19_at_223924.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=96ea453e9aecff95238d4aa6dbe7ee37" width="1182" height="470" data-path=".assets/images/6556142-screenshot_2020-11-19_at_223924.png" />
</Frame>

### 5. Configure the MFCC block

Now that we've assembled the building blocks of our Impulse, we can configure each individual part. Click on the **MFCC** tab in the left hand navigation menu. You'll see a page that looks like this:

<Frame caption="MFCC block looking at an audio file">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/7531f81-screenshot_2020-11-19_at_224116.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=9eeff5cc0d757d2ed892e0cac100fba7" width="1396" height="1000" data-path=".assets/images/7531f81-screenshot_2020-11-19_at_224116.png" />
</Frame>

This page allows you to configure the MFCC block, and lets you preview how the data will be transformed. The right of the page shows a visualization of the MFCC's output for a piece of audio, which is known as a [spectrogram](https://en.wikipedia.org/wiki/Spectrogram). An MFCC spectrogram is a specially tuned spectrogram which highlights frequencies which are common in human speech (Edge Impulse also has normal spectrograms if that's more your thing).

In the spectrogram the vertical axis represents the frequencies (the number of frequency bands is controlled by 'Number of coefficients' parameter, try it out!), and the horizontal axis represents time (controlled by 'frame stride' and 'frame length'). The patterns visible in a spectrogram contain information about what type of sound it represents. For example, the spectrogram in this image shows "Hello world":

<Frame caption="MFCC Spectrogram for 'Hello world'">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/e79529c-screenshot_2020-11-19_at_224533.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=1995284ae19a4559617a796bef22dfdb" width="508" height="136" data-path=".assets/images/e79529c-screenshot_2020-11-19_at_224533.png" />
</Frame>

And the spectrogram in this image shows "On":

<Frame caption="MFCC Spectrogram for 'On'">
  <img src="https://mintcdn.com/edgeimpulse/M1w1EVa0Cr_xPADa/.assets/images/ba5de05-screenshot_2020-11-19_at_224643.png?fit=max&auto=format&n=M1w1EVa0Cr_xPADa&q=85&s=9d232b656fdc59097cb5f456dd865a9f" width="509" height="138" data-path=".assets/images/ba5de05-screenshot_2020-11-19_at_224643.png" />
</Frame>

These differences are not necessarily easy for a person to describe, but fortunately they are enough for a neural network to learn to identify.

It's interesting to explore your data and look at the types of spectrograms it results in. You can use the dropdown box near the top right of the page to choose between different audio samples to visualize, or play with the parameters to see how the spectrogram changes.

In addition, you can see the performance of the MFCC block on your microcontroller below the spectrogram. This is the complete time that it takes on a low-power microcontroller (Cortex-M4F @ 80MHz) to analyze 1 second of data.

<Frame caption="On-device performance is updated automatically when you change parameters">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/f8d2e48-screenshot_2020-11-19_at_224826.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=e38b75447a8be7991c59f2a7b713ea74" width="582" height="255" data-path=".assets/images/f8d2e48-screenshot_2020-11-19_at_224826.png" />
</Frame>

You might think based on this number that we can only classify 2 or 3 windows per second, but we continuously build up the spectrogram (as it has a time component), which takes less time, and we can thus continuously listen for events 5-6x a second, even on an 40MHz processor. This is already implemented on all [fully supported development boards](/hardware), and [easy to implement](/tutorials/topics/inference/sample-audio-continuously) on your own device.

#### Feature explorer

The spectrograms generated by the MFCC block will be passed into a neural network architecture that is particularly good at learning to recognize patterns in this type of tabular data. Before training our neural network, we'll need to generate MFCC blocks for all of our windows of audio. To do this, click the **Generate features** button at the top of the page, then click the green **Generate features** button. This will take a minute or so to complete.

Afterwards you're presented with one of the most useful features in Edge Impulse: the feature explorer. This is a 3D representation showing your complete dataset, with each data-item color-coded to its respective label. You can zoom in to every item, find anomalies (an item that's in a wrong cluster), and click on items to listen to the sample. This is a great way to check whether your dataset contains wrong items, and to validate whether your dataset is suitable for ML (it should separate nicely).

<Frame caption="The feature explorer showing 'Hello world' (in blue), vs. 'unknown' (in green) data. This separates well, so the dataset looks to be in good condition.">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/d87aa8c-screenshot_2020-11-19_at_225322.png?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=d696b62b93aff8fdd2f65f1a95beaca3" width="720" height="630" data-path=".assets/images/d87aa8c-screenshot_2020-11-19_at_225322.png" />
</Frame>

### 6. Configure the neural network

With all data processed it's time to start training a neural network. Neural networks are algorithms, modeled loosely after the human brain, that can learn to recognize patterns that appear in their training data. The network that we're training here will take the MFCC as an input, and try to map this to one of three classes—your keyword, noise or unknown.

Click on **NN Classifier** in the left hand menu. You'll see the following page:

<Frame caption="Neural network configuration">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/24269a7-screenshot_2020-11-19_at_225643.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=89ebd5e782d54116efd8002c071fac54" width="763" height="905" data-path=".assets/images/24269a7-screenshot_2020-11-19_at_225643.png" />
</Frame>

A neural network is composed of layers of virtual "neurons", which you can see represented on the left hand side of the NN Classifier page. An input—in our case, an MFCC spectrogram—is fed into the first layer of neurons, which filters and transforms it based on each neuron's unique internal state. The first layer's output is then fed into the second layer, and so on, gradually transforming the original input into something radically different. In this case, the spectrogram input is transformed over four intermediate layers into just two numbers: the probability that the input represents your keyword, and the probability that the input represents 'noise' or 'unknown'.

During training, the internal state of the neurons is gradually tweaked and refined so that the network transforms its input in *just* the right ways to produce the correct output. This is done by feeding in a sample of training data, checking how far the network's output is from the correct answer, and adjusting the neurons' internal state to make it more likely that a correct answer is produced next time. When done thousands of times, this results in a trained network.

A particular arrangement of layers is referred to as an *architecture*, and different architectures are useful for different tasks. The default neural network architecture provided by Edge Impulse will work well for our current project, but you can also define your own architectures. You can even import custom neural network code from tools used by data scientists, such as TensorFlow and Keras (click the three dots at the top of the page).

Before you begin training, you should change some values in the configuration. Change the *Minimum confidence rating* to 0.6. This means that when the neural network makes a prediction (for example, that there is 0.8 probability that some audio contains "hello world") Edge Impulse will disregard it unless it is above the threshold of 0.6.

Next, enable 'Data augmentation'. When enabled your data is randomly mutated during training. For example, by adding noise, masking time or frequency bands, or warping your time axis. This is a very quick way to make your dataset work better in real life (with unpredictable sounds coming in), and prevents your neural network from overfitting (as the data samples are changed every training cycle).

With everything in place, click **Start training**. You'll see a lot of text flying past in the *Training output* panel, which you can ignore for now. Training will take a few minutes. When it's complete, you'll see the *Last training performance* panel appear at the bottom of the page:

<Frame caption="A trained Machine Learning model that can distinguish keywords!">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/7e6b0fb-screenshot_2020-11-19_at_230109.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=d9e8209405b21fb43fa7d4dd5d42b682" width="1061" height="515" data-path=".assets/images/7e6b0fb-screenshot_2020-11-19_at_230109.png" />
</Frame>

Congratulations, you've trained a neural network with Edge Impulse! But what do all these numbers mean?

At the start of training, 20% of the training data is set aside for *validation*. This means that instead of being used to train the model, it is used to evaluate how the model is performing. The *Last training performance* panel displays the results of this validation, providing some vital information about your model and how well it is working. Bear in mind that your exact numbers may differ from the ones in this tutorial.

On the left hand side of the panel, *Accuracy* refers to the percentage of windows of audio that were correctly classified. The higher number the better, although an accuracy approaching 100% is unlikely, and is often a sign that your model has *overfit* the training data. You will find out whether this is true in the next stage, during model testing. For many applications, an accuracy above 85% can be considered very good.

The *Confusion matrix* is a table showing the balance of correctly versus incorrectly classified windows. To understand it, compare the values in each row. For example, in the above screenshot, 96 of the *helloworld* audio windows were classified as *helloworld*, while 10 of them were incorrectly classified as unknown or noise. This appears to be a great result.

The *On-device performance* region shows statistics about how the model is likely to run on-device. *Inferencing time* is an estimate of how long the model will take to analyze one second of data on a typical microcontroller (an Arm Cortex-M4F running at 80MHz). *Peak RAM usage* gives an idea of how much RAM will be required to run the model on-device.

### 7. Classifying new data

The performance numbers in the previous step show that our model is working well on its training data, but it's extremely important that we test the model on new, unseen data before deploying it in the real world. This will help us ensure the model has not learned to overfit the training data, which is a common occurrence.

Fortunately we've put aside 20% of our data already in the 'Test set' (see **Data acquisition**). This is data that the model has never seen before, and we can use this to validate whether our model actually works on unseen data. To run your model against the test set, head to **Model testing**, select all items and click **Classify selected**.

<Frame caption="Model testing showing 88.62% accuracy on our test set.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/4a23094-screenshot_2020-11-19_at_230423.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=2f84527e5e17141a4db2c16608a1af08" width="1256" height="838" data-path=".assets/images/4a23094-screenshot_2020-11-19_at_230423.png" />
</Frame>

To drill down into a misclassified sample, click the three dots (`⋮`) next to a sample and select **Show classification**. You're then transported to the classification view, which lets you inspect the sample, and compare the sample to your training data. This way you can inspect whether this was actually a classification failure, or whether your data was incorrectly labeled. From here you can either update the label (when the label was wrong), or move the item to the training set to refine your model.

<Frame caption="Inspecting a misclassified label. Here the audio actually only says 'Hello', and thus this sample was mislabeled.">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/8a9bd67-screenshot_2020-11-19_at_230719.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=b6db3995a3bfba0c26d02704f910b0d6" width="1386" height="1000" data-path=".assets/images/8a9bd67-screenshot_2020-11-19_at_230719.png" />
</Frame>

<Warning>
  **Misclassifications and uncertain results**

  It's inevitable that even a well-trained machine learning model will sometimes misclassify its inputs. When you integrate a model into your application, you should take into account that it will not always give you the correct answer.

  For example, if you are classifying audio, you might want to classify several windows of data and average the results. This will give you better overall accuracy than assuming that every individual result is correct.
</Warning>

### 8. Deploying to your device

With the impulse designed, trained and verified you can deploy this model back to your device. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption. Edge Impulse can package up the complete impulse - including the MFCC algorithm, neural network weights, and classification code - in a single C++ library that you can include in your embedded software.

<Info>
  **Mobile phone**

  Your mobile phone can build and download the compiled impulse directly from the mobile client. See 'Deploying back to device' on the [Using your mobile phone](/hardware/devices/mobile-phone) page.
</Info>

To export your model, click on **Deployment** in the menu. Then under 'Build firmware' select your development board, and click **Build**. This will export the impulse, and build a binary that will run on your development board in a single step. After building is completed you'll get prompted to download a binary. Save this on your computer.

### Flashing the device

When you click the **Build** button, you'll see a pop-up with text and video instructions on how to deploy the binary to your particular device. Follow these instructions. Once you are done, we are ready to test your impulse out.

### Running the model on the device

We can connect to the board's newly flashed firmware over serial. Open a terminal and run:

```
$ edge-impulse-run-impulse --continuous
```

<Warning>
  **Serial daemon**

  If the device is not connected over WiFi, but instead connected via the Edge Impulse serial daemon, you'll need stop the daemon. Only one application can connect to the development board at a time.
</Warning>

This will capture audio from the microphone, run the MFCC code, and then classify the spectrogram:

```
Edge Impulse impulse runner v1.9.1
[SER] Connecting to /dev/tty.usbmodem0004401658161
Predictions (DSP: 143 ms., Classification: 13 ms., Anomaly: 0 ms.):
    helloworld: 	0.98828
    noise: 	        0.0039
    unknown: 	    0.00781
```

Great work! You've captured data, trained a model, and deployed it to an embedded device. You can now control LEDs, activate actuators, or send a message to the cloud whenever you say a keyword!

#### Poor performance due to unbalanced dataset?

Is your model working properly in the Studio, but does not recognize your keyword when running in continuous mode on your device? Then this is probably due to dataset imbalance (a lot more unknown / noise data compared to your keyword) in combination with our moving average code to reduce false positives.

When running in continuous mode we run a moving average over the predictions to prevent false positives. E.g. if we do 3 classifications per second you’ll see your keyword potentially classified three times (once at the start of the audio file, once in the middle, once at the end). However, if your dataset is unbalanced (there’s a lot more noise / unknown than in your dataset) the ML model typically manages to only find your keyword in the 'center' window, and thus we filter it out as a false positive.

You can fix this by either:

1. Adding more data :-)
2. Or, by disabling the moving average filter by going into ei\_run\_classifier.h (in the edge-impulse-sdk directory) and removing:

   ```
       for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
           result->classification[ix].value =
               run_moving_average_filter(&classifier_maf[ix], result->classification[ix].value);
       }
   ```

Note that this might increase the number of false positives the model detects.

### 9. Conclusion

Congratulations! you've used Edge Impulse to train a neural network model capable of recognizing audible events. There are endless applications for this type of model, from monitoring industrial machinery to recognizing voice commands. Now that you've trained your model you can integrate your impulse in the firmware of your own embedded device, see the [Deployments](/hardware/deployments) tutorials. There are examples for Mbed OS, Arduino, STM32CubeIDE, Zephyr, and any other target that supports a C++ compiler.

Or if you're interested in more, see our tutorials on [Continuous motion recognition](/tutorials/end-to-end/motion-recognition) or [Image classification](/tutorials/end-to-end/image-classification/). If you have a great idea for a different project, that's fine too. Edge Impulse lets you capture data from any sensor, build [custom processing blocks](/studio/organizations/custom-blocks/custom-processing-blocks) to extract features, and you have full flexibility in your Machine Learning pipeline with the learning blocks.

We can't wait to see what you'll build! 🚀


Built with [Mintlify](https://mintlify.com).