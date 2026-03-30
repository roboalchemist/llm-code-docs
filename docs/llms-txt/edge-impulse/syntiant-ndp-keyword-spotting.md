# Source: https://docs.edgeimpulse.com/tutorials/hardware/syntiant-ndp-keyword-spotting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Syntiant NDPs - keyword spotting

<Info>
  **Keyword spotting**

  This tutorial is for the [Syntiant TinyML](/hardware/boards/syntiant-tinyml-board), [Arduino Nicla Voice](/hardware/boards/arduino-nicla-voice), and the [Avnet RASynBoard (Renesas RA6 and Syntiant NDP 120)](/hardware/boards/avnet-rasynboard). For other development boards, you can follow the standard [Keyword spotting](/tutorials/end-to-end/keyword-spotting) tutorial
</Info>

In this tutorial, you'll use machine learning to build a system that can recognize audible events, particularly your voice through *audio classification*. The system you create will resemble giving audio commands to control a remote control (RC) car such as 'go' and 'stop', even in the presence of other background noise or background chatter. **For the best user experience please use the Chrome browser.**

You'll learn how to collect audio data from the microphone, use signal processing to extract the most important information, and train a deep neural network that can tell you whether your keyword was heard in a given clip of audio. Finally, you'll deploy the system to your Syntiant TinyML Board and evaluate how well it works.

At the end of this tutorial, you'll have a firm understanding of how to classify audio using Edge Impulse for Syntiant hardware.

<Info>
  **Before starting the tutorial**

  After signing up for a free Edge Impulse account, clone the finished project, including all training data, signal processing and machine learning blocks here: [Tutorial: Syntiant-RC](https://studio.edgeimpulse.com/public/42868/latest). At the end of the process you will have the full project that comes pre-loaded with approx. 2.5 hours of training data.

  The features have been generated for the Syntiant TinyML board. To use it for the Arduino Nicla Voice, just set the `Features extractor` to `log-bin` in the Syntiant DSP block and retrain your impulse.
</Info>

<Warning>
  **Production ready systems**

  While the example Syntiant-RC tutorial project provides good performance, it is not intended to be production ready and is designed to maximize the out-of-box user experience. It is in essence a training vehicle for users of both Edge Impulse and Syntiant to understand the entire workflow. Production ready systems need to have a much more robust training data set to further reduce the likelihood of false positive and negatives.
</Warning>

### 1. Prerequisites

For this tutorial you'll one of the following boards

* [Syntiant TinyML Board](/hardware/boards/syntiant-tinyml-board)
* [Arduino Nicla Voice](/hardware/boards/arduino-nicla-voice)
* [Avnet RASynBoard (Renesas RA6 and Syntiant NDP 120)](/hardware/boards/avnet-rasynboard)

The Syntiant TinyML Board shows up as USB microphone once plugged in, and Edge Impulse can use this interface to record audio directly. For the Arduino Nicla Voice, run the `edge-impulse-daemon` CLI command to start collecting data.

<Info>
  **Device compatibility**

  Edge Impulse can ingest data from any device - including embedded devices that you already have in production. See the documentation for the [Ingestion API](/apis/ingestion) for more information.
</Info>

### 2. Collecting your own voice samples

In this tutorial we want to build a system that recognizes keywords that resemble giving commands to a remote control car such as 'go' and 'stop'. Although the aforementioned public project comes pre-loaded with approx. 2.5 hours of training data, in order to add additional audio samples including your own, we'll show you how you can record audio samples directly from the board.

#### 2.1 For the Syntiant TinyML

To collect your own voice samples, ensure you have selected your system's microphone interface as the "Arduino MKRZero". Then, go to **Devices** -> **Connect a new device**, and choose the option of "Use Your Computer" and allow access to your microphone.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/ebc069e-screenshot_2021-07-26_at_123207.png?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=c8d8e5cd14866dc027fc56511a9b54d3" width="802" height="458" data-path=".assets/images/ebc069e-screenshot_2021-07-26_at_123207.png" />
</Frame>

Set your keyword as the label and set your sample length to 10s. Then click **Start Recording** and start saying your keyword over and over again (with a slight pause in between each utterance).

<Frame caption="Audio Data Collection Interface">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/6cc9301-screen_shot_2021-03-29_at_41902_pm.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=d6bbb9e541794851c6014b8f4fa0ac53" width="1076" height="612" data-path=".assets/images/6cc9301-screen_shot_2021-03-29_at_41902_pm.png" />
</Frame>

<iframe src="https://www.youtube.com/embed/cubI6IPKtiE" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

> **Note:** You can use your [Mobile phone](/hardware/devices/mobile-phone) as a sensor as well.

Afterwards you have a file like this, clearly showing your keywords, separated by some noise. The new data sample will show up in the appropriate Training or Test data bucket.

<Frame caption="10 seconds of 'Go' keyword">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/c686af5-screen_shot_2021-03-29_at_42516_pm.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=244a5d45dfb6cfa8e453a6a046fa13cc" width="1186" height="978" data-path=".assets/images/c686af5-screen_shot_2021-03-29_at_42516_pm.png" />
</Frame>

This data is not suitable for Machine Learning yet though. You will need to cut out the parts where you say your keyword. This is important because you only want the actual keyword to be labeled as such, and not accidentally labeled as noise, or incomplete parts of the utterance. Fortunately the Edge Impulse Studio can do this for you. Click `⋮` next to your sample, and select **Split sample**.

<Frame caption="'Split sample' automatically cuts out the interesting parts of an audio file.">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/6c44c21-screen_shot_2021-03-29_at_42853_pm.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=d5b0fea574a454a806a603905f644893" width="1600" height="882" data-path=".assets/images/6c44c21-screen_shot_2021-03-29_at_42853_pm.png" />
</Frame>

If you have a short keyword, enable *Shift samples* to randomly shift the sample around in the window, and then click **Split**. You now have individual 1s. long samples in your dataset. Perfect!

#### 2.2 For the Arduino Nicla Voice

Run the `edge-impulse-daemon` CLI command and select the project to connect to. Once your board is connected, you can start collecting data from the Data Acquisition page:

<Frame caption="Capture data with Nicla Voice">
  <img src="https://mintcdn.com/edgeimpulse/ZTVcrLfO8Bn7QR9I/.assets/images/nicla-voice-capture.png?fit=max&auto=format&n=ZTVcrLfO8Bn7QR9I&q=85&s=47327c9317e0643c2a37aadb1f3f8903" width="1122" height="902" data-path=".assets/images/nicla-voice-capture.png" />
</Frame>

### 3. Understanding how to construct your dataset

<Info>
  **About this section**

  This section goes through general guidance for collecting your audio data from scratch and not all steps are required for the out-of-box experience workflow, other than adding your own voice samples. Read on to understand more detail about how the dataset was constructed.
</Info>

Now that you know how to collect keyword data let's consider other data we need to collect. In addition to your keyword we'll also need audio that is *not* your keyword. Like background noise, the TV playing, and humans saying other words, all of which go into the openset class. This class is labeled as and will be referred to as 'z\_openset' from here on out. This is required because a machine learning model has no idea about right and wrong (unless those are your keywords), but only learns from the data you feed into it. The more varied your data is, the better your model will work.

For each of your classes (in this case 'go', 'stop', and 'z\_openset') you want to capture an even amount of data (balanced datasets work better) - and for a decent keyword spotting model you'll want at the VERY minimum 10 minutes in each class if you're building your dataset from scratch. For the Syntiant-RC project we've used a subset of the 'Google 30' speech command set for 'go' and 'stop'.

To make this model more responsive to your own voice, do this in the same manner as above. One way of doing this would be to collect 10 seconds clips, then automatically split this data. Make sure to capture wide variations of the keyword and cover high and low pitches.

To add additional data to the 'z\_openset' dataset label you can either collect this yourself, or make your life a bit easier by using dataset of both 'noise' (all kinds of background noise) and 'unknown' (random words) data that we built for you here: [Keyword Spotting Dataset](/datasets/audio/keyword-spotting). In the Syntiant-RC project we used short 1 second clips of NPR radio recordings. We consider the 'z\_openset' a 'negative' class since it does not contain any of the keywords that are of interest such as 'go' and 'stop' (which are considered 'positive' classes).

This is entirely optional, but to import this data, go to **Data acquisition**, click the *Upload* icon, and select a number of 'noise' or 'unknown' samples (there's 25 minutes of each class, but you can select less files if you want), and clicking **Begin upload**. The data is automatically labeled and added to your project. **Make sure you label them 'z\_openset' before uploading so that they go into the pre-existing 'z\_openset' category.**

<Frame caption="Importing other 'z\_openset' data into your project">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/1f97a38-screenshot_2020-11-19_at_222610.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=685d4bea246fce6f3d922f6aede0fe52" width="590" height="710" data-path=".assets/images/1f97a38-screenshot_2020-11-19_at_222610.png" />
</Frame>

#### Rebalancing your dataset

If you've collected all your training data through the 'Record new data' widget you'll have all your keywords in the 'Training' dataset. This is not great, because you want to keep 20% of your data separate to validate the machine learning model. To mitigate this you can go to **Dashboard** and select **Rebalance dataset**. This will automatically split your data between a training class (80%) and a testing class (20%). Afterwards you should see something like this:

<Frame caption="Training data, showing an even split between the three classes">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/ddc6353-screen_shot_2021-07-28_at_114630_am.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=ff8d690d4fa928b3596a2d753c567bfb" width="586" height="300" data-path=".assets/images/ddc6353-screen_shot_2021-07-28_at_114630_am.png" />
</Frame>

<br />

<Frame caption="Testing data, also showing an even split between the three classes">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/6598fb7-screen_shot_2021-07-28_at_114707_am.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=b6984ac4fd9aede613e8d64d11cef7de" width="586" height="300" data-path=".assets/images/6598fb7-screen_shot_2021-07-28_at_114707_am.png" />
</Frame>

<Info>
  **Next steps**

  In the next steps we walk you through in detail how the Syntiant signal processing and neural network blocks were configured. If you imported the project, these are already pre-configured for you so you can just read on to understand more details.
</Info>

### 4. Designing your impulse

With the data set in place you can design an impulse. An impulse takes the raw data, slices it up in smaller windows, uses signal processing blocks to extract features, and then uses a learning block to classify new data. Signal processing blocks always return the same values for the same input and are used to make raw data easier to process, while learning blocks learn from past experiences.

For this tutorial we'll use the "Syntiant" signal processing block. The Syntiant processing block is similar to the [Audio MFE](/studio/projects/processing-blocks/blocks/audio-mfe) block, but using a log-MEL scale plus other transformations specific to the Syntiant audio front-end.

We'll then pass this simplified audio data into a Neural Network block, which will learn to distinguish between the three classes of audio.

In the Studio, go to the **Create impulse** tab, add a *Time series data*, an *Audio (Syntiant)* and a *Neural Network (Keras)* block. Set the window size to 968 ms and the window increase to 484 ms (we'll explain why later), verify that sampling frequency is set to 16000 Hz and click **Save Impulse**.

<Frame caption="Impulse design for speech recognition with Syntiant">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/8ebf52e-screenshot_2022-01-25_at_114650.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=0a1d40ad3c5bef7ccf7f3406b2e97f52" width="1600" height="802" data-path=".assets/images/8ebf52e-screenshot_2022-01-25_at_114650.png" />
</Frame>

### 5. Configure the Syntiant block

Now that we've assembled the building blocks of our Impulse, we can configure each individual part. Click on the **Syntiant** tab in the left hand navigation menu. You'll see a page that looks like this:

<Frame caption="Syntiant processing block configuration">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntiant-dsp.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=47a1fd3260a953ef08f293db4f45fc69" width="1600" height="858" data-path=".assets/images/syntiant-dsp.png" />
</Frame>

This page allows you to configure some parameters of the Syntiant block, and lets you preview how the data will be transformed. The right of the page shows a visualization of the Syntiant's output for a piece of audio. The Syntiant processing block extracts speech features using filterbanks. To get a better understanding of parameters, have a look at the [Audio MFE](/studio/projects/processing-blocks/blocks/audio-mfe) documentation.

Features generated by the Syntiant DSP block are slightly different between the TinyML and Nicla Voice. Set the `features extractor` to:

* *gpu/NDP101* for Syntiant TinyML
* *log-bin/NDP120* for Nicla Voice

<Info>
  **Syntiant block parameters**

  The number of generated features has to be 1,600, which corresponds to the Syntiant Neural Network input layer. To generate 1,600 features, you have to verify the following equation: window size = 1000 x (39 x frame stride + frame length). For our example: window size = 968 ms = 1000 x (39 x 0.024 + 0.032).
</Info>

In the spectrogram the vertical axis represents the frequencies (the number of frequency bands is controlled by 'Number of coefficients' parameter), and the horizontal axis represents time (controlled by 'frame stride' and 'frame length'). The patterns visible in a spectrogram contain information about what type of sound it represents. For example, the spectrogram in this image shows "Go":

<Frame caption="Spectrogram for 'Go'">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/6c7289e-screenhunter_279_mar_29_1657.jpg?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=685ee48ba9aaea1f12981cd381b31641" width="271" height="274" data-path=".assets/images/6c7289e-screenhunter_279_mar_29_1657.jpg" />
</Frame>

These differences are not necessarily easy for a person to describe, but fortunately they are enough for a neural network to learn to identify.

It's interesting to explore your data and look at the types of spectrograms it results in. You can use the dropdown box near the top right of the page to choose between different audio samples to visualize, or play with the parameters to see how the spectrogram changes.

#### Feature explorer

The spectrograms generated by the Syntiant block will be passed into a neural network architecture that is particularly good at learning to recognize patterns in this type of tabular data. Before training our neural network, we'll need to generate Syntiant blocks for all of our windows of audio. To do this, click the **Generate features** button at the top of the page, then click the green **Generate features** button. This will take a minute or so to complete.

Afterwards you're presented with one of the most useful features in Edge Impulse: the feature explorer. This is a 3D representation showing your complete dataset, with each data-item color-coded to its respective label. You can zoom in to every item, find anomalies (an item that's in a wrong cluster), and click on items to listen to the sample. This is a great way to check whether your dataset contains wrong items, and to validate whether your dataset is suitable for ML (it should separate nicely).

<Frame caption="Feature explorer view">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/11a7f8c-screen_shot_2021-07-28_at_114859_am.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=98f269cb546771aaf696f8249d93846e" width="586" height="568" data-path=".assets/images/11a7f8c-screen_shot_2021-07-28_at_114859_am.png" />
</Frame>

### 6. Configure the neural network

With all data processed it's time to start training a neural network. Neural networks are algorithms, modeled loosely after the human brain, that can learn to recognize patterns that appear in their training data. The network that we're training here will take the processing block features as an input, and try to map this to one of the three classes — 'go', 'stop', or 'z\_openset'.

Click on **NN Classifier** in the left hand menu. You'll see the following page:

<Frame caption="Syntiant NN Configuration">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/syntiant-nn.jpg?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=cf5d11640c64ab7e11047d07a94d502a" width="661" height="1000" data-path=".assets/images/syntiant-nn.jpg" />
</Frame>

<Info>
  **Neural Network architectures**

  Syntiant TinyML only supports a Dense architecture. The Arduino Nicla Voice also supports Convolutional models and it is selected by default.
</Info>

With everything in place, click **Start training**. You'll see a lot of text flying past in the *Training output* panel, which you can ignore for now. Training will take a few minutes. When it's complete, you'll see the *Last training performance* panel appear at the bottom of the page:

<Frame caption="Training performance">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/c2e0aca-screen_shot_2021-07-28_at_115151_am.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=b54404995da3dd4e5c9e073bdd1932bc" width="612" height="782" data-path=".assets/images/c2e0aca-screen_shot_2021-07-28_at_115151_am.png" />
</Frame>

Congratulations, you've trained a neural network with Edge Impulse and ready to deploy on your hardware! But what do all these numbers mean?

At the start of training, 20% of the training data is set aside for *validation*. This means that instead of being used to train the model, it is used to evaluate how the model is performing. The *Last training performance* panel displays the results of this validation, providing some vital information about your model and how well it is working. Bear in mind that your exact numbers may differ from the ones in this tutorial.

On the left hand side of the panel, *Accuracy* refers to the percentage of windows of audio that were correctly classified. The higher number the better, although an accuracy approaching 100% is unlikely, and is often a sign that your model has *overfit* the training data. You will find out whether this is true in the next stage, during model testing. For many applications, an accuracy above 85% can be considered very good.

The *Confusion matrix* is a table showing the balance of correctly versus incorrectly classified windows. To understand it, compare the values in each row. For example, in the above screenshot, 98.8% of the *'go'* audio windows were classified as *'go'*, while 1.8% of them were classified to be in the 'stop'. This appears to be a great result.

### 7. Classifying new data

The performance numbers in the previous step show that our model is working well on its training data, but it's extremely important that we test the model on new, unseen data before deploying it in the real world. This will help us ensure the model has not learned to overfit the training data, which is a common occurrence.

Fortunately we've put aside 20% of our data already in the 'Test set' (see **Data acquisition**). This is data that the model has never seen before, and we can use this to validate whether our model actually works on unseen data. To run your model against the test set, head to **Model testing**, and click **Classify all**.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/dd0c3e2-screen_shot_2021-07-28_at_115632_am.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=4c4e03f5caa53426d3ba35371b90047a" width="868" height="854" data-path=".assets/images/dd0c3e2-screen_shot_2021-07-28_at_115632_am.png" />
</Frame>

To drill down into a misclassified sample, click the three dots (`⋮`) next to a sample and select **Show classification**. You're then transported to the classification view, which lets you inspect the sample, and compare the sample to your training data. This way you can inspect whether this was actually a classification failure, or whether your data was incorrectly labeled. From here you can either update the label (when the label was wrong), or move the item to the training set to refine your model.

<Warning>
  **Misclassifications and uncertain results**

  It's inevitable that even a well-trained machine learning model will sometimes misclassify its inputs. When you integrate a model into your application, you should take into account that it will not always give you the correct answer.

  For example, if you are classifying audio, you might want to classify several windows of data and average the results. This will give you better overall accuracy than assuming that every individual result is correct.
</Warning>

### 8. Deploying to your device

With the impulse designed, trained and verified you can deploy this model back to your device. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption.

To export your model, click on **Deployment** in the menu. Then under 'Build firmware' select the Syntiant TinyML or Arduino Nicla Voice.

The final step before building the firmware is to configure the *posterior handler parameters* of the Syntiant chip.

<Info>
  **Pre-configured posterior parameters**

  For the Syntiant-RC project, we've already pre-configured the posterior parameters so you can just go to the 'Build' output step. We recommend skipping to Step 9, but read on for more details about the process of posterior search.
</Info>

<Frame caption="Optimizing posterior parameters">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/97ac8cf-screen_shot_2021-07-28_at_115801_am.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=80f5e1cdfe69ff6286552e67eabbdd6a" width="901" height="1000" data-path=".assets/images/97ac8cf-screen_shot_2021-07-28_at_115801_am.png" />
</Frame>

Those parameters are used to tune the precision and recall of the neural network activations, to minimize False Rejection Rate and False Activation Rate. You can manually edit those parameters in JSON format or use the *Find posterior parameters* to search for the best values:

* Select the classes you want to detect (the z\_openset class should be omitted except for testing purpose)
* Select a calibration dataset: either no calibration (**recommended for TinyML/NDP101**), the reference dataset with common english words from a radio program, or your own calibration dataset.

This calibration dataset is made of 2 files: an audio wav file and a csv file which contains the audio transcript of this program. This audio transcript should ideally have the classes you want to detect. For example you can imagine the following csv file: `go,stop,this,is,an,example,transcript,for,optimizing,the,posterior,parameters,,,it,will,optimize,activations,for,the,go,stop,keywords,`

You can also simplify the csv file and include only the keywords/classes you are interested in optimizing. For instance, if your audio wav files contains only 2 occurrences of 'go' and 'stop': `go,stop,go,stop,`

<Info>
  **Tuning the audio gain for the Syntiant TinyML**

  After generating the posterior parameters, you can change the Syntiant TinyML audio gain by editing the "audio\_pdm\_gain" value at the end of the JSON file. Default value is set to 12 dB.
</Info>

### 9. Flashing the device

Once optimized parameters have been found, you can click **Build**. This will build a Syntiant package that will run on your development board. After building is completed you'll get prompted to download a zipfile. Save this on your computer. A pop-up video will show how the download process works.

After unzipping the downloaded file, run the appropriate flashing script for your operating system, to flash the Syntiant TinyML Board with the Syntiant-RC model and associated firmware. You might see a Microsoft Defender screen pop up when the script is run on Windows 10. It's safe to proceed so select 'More info' and continue.

### 10. Running the model on the device

Run the `edge-impulse-run-impulse` CLI command in your terminal:

```
Edge Impulse impulse runner v1.16.0
[SER] Connecting to /dev/tty.usbmodem2CE0169C2
[SER] Serial is connected, trying to read config...
[SER] Unhandled configuration option management ws //remote-mgmt.edgeimpulse.com
[SER] Retrieved configuration
[SER] Device is running AT command version 1.7.0
[SER] Started inferencing, press CTRL+C to stop...
AT+RUNIMPULSE
Inferencing settings:
	Interval: 0.0625 ms.
	Frame size: 15488
	Sample length: 968 ms.
	No. of classes: 3
Classes:
	go
	stop
	z_openset
> Match: NN0:go
Match: NN0:stop
Match: NN0:stop
```

You can also connect to the board's newly flashed firmware over serial as an alternative. Open a terminal and connect using the appropriate COM port with 115200 8-N-1 settings.

### 11. Conclusion

Congratulations! Now that you've trained and deployed your model you can go further and build your own custom firmware, see [Run on Syntiant TinyML Board](/hardware/deployments/run-cpp-syntiant-tinyml-board).

Or if you're interested in more, see our tutorial on [Motion Recognition - Syntiant TinyML](/tutorials/hardware/syntiant-ndp-motion-recognition).

We can't wait to see what you'll build! 🚀


Built with [Mintlify](https://mintlify.com).