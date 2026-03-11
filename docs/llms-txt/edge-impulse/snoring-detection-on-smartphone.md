# Source: https://docs.edgeimpulse.com/projects/expert-network/snoring-detection-on-smartphone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Snoring Detection on a Smart Phone

Created By: Wamiq Raza

Public Project Link: [https://studio.edgeimpulse.com/public/109559/latest](https://studio.edgeimpulse.com/public/109559/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/intro.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=efd982120a22095cba900888933af5ce" width="648" height="366" data-path=".assets/images/snoring-detection-on-smartphone/intro.jpg" />
</Frame>

## Story

Snoring, a type of sleep disordered breathing, disrupts sleep quality and quantity for both the snorer and, frequently, the person who sleeps with the snorer. Snoring-related sleep deprivation can cause serious physical, emotional, and financial difficulties. Snoring not only disrupts the snorer's sleep, but it can also cause anger between spouses! About 40% of adult males and 24% of adult women snore on a regular basis. Snoring begins when the muscles around the throat relax during sleeping. This narrows the airway, causing vibrations that result in snoring. Snoring is more common when a person sleeps on their back. Sleeping on your side is a natural remedy for snoring. Sleeping on your side rather than your back is a simple and natural treatment for snoring. In this project, a deep learning model for snoring detection is designed to be implemented on a smart phone using the Edge Impulse API, and the model may be put on other embedded systems to detect snoring automatically. A smart phone is linked to the listener module by home Wi-Fi or mobile data to log snoring incidents with timestamps, and the data may be shared to a physician for treatment and monitoring of disorders such as sleep apnea.

### Getting started

This tutorial has the following requirements:

* Basic understanding of software development
* Edge Impulse account
* Android or iOS mobile phone

We will use Edge Impulse, an online development platform for machine learning on edge devices. [Create a free account by signing up here](https://studio.edgeimpulse.com/). Log into your account and give your new project a name by clicking on the title. To run the current project as-is, you can directly clone it to make your own copy, and start executing.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/signup.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=bd91b3b272857d6510f89530896f14f9" width="1091" height="343" data-path=".assets/images/snoring-detection-on-smartphone/signup.jpg" />
</Frame>

## Data Acquisition

This project used a dataset of 1000 sound samples which is divided into two categories: snoring noises and non-snoring sounds. There are 500 examples in each class, the snoring noises were gathered from several web sources and non-snoring sound were gathered from similar web sources. The files were then separated into equal sized one second duration files after silences were removed from them. As a result, each sample lasts one second. Among the snoring samples, 363 samples consist of snoring sounds of children, adult men and adult women without any background sound \[1]. The remaining samples having a background of non-snoring sounds. The 500 non-snoring samples consist of background sounds that are ten categories such as baby crying, the clock ticking, the door opened and closed, total silence and the minor sound of the vibration motor of the gadget, toilet flashing, siren of emergency vehicles, rain and thunderstorms, streetcar sounds, people talking, and background television news. Figure 1 and Figure 2 illustrate the frequency of snoring and non-snoring sound respectively. The dataset can be downloaded from \[2].

<Frame caption="Figure 1: Frequency of snoring audio">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/data-acquisition.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=367b59647bdf60482a2f4018a5fdd252" width="666" height="496" data-path=".assets/images/snoring-detection-on-smartphone/data-acquisition.jpg" />
</Frame>

<br />

<Frame caption="Figure 2: Frequency of non-snoring audio">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/data-acquisition-2.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=4be10e2d40a2549f22d9c7ad86a921c9" width="700" height="508" data-path=".assets/images/snoring-detection-on-smartphone/data-acquisition-2.jpg" />
</Frame>

Once the dataset is ready you can upload it into Edge Impulse. Figure 3 represents the Edge Impulse platform, and how to upload the data. If you don’t want to download or upload data, and just run the project, refer to the section **Getting started** for cloning the current project.

<Frame caption="Figure 3: Uploading data into Edge Impulse platform">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/data-upload.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=8cd8f2d1872a3d6e1d7e4f9b758cdbbd" width="1357" height="696" data-path=".assets/images/snoring-detection-on-smartphone/data-upload.jpg" />
</Frame>

## Creating Your Impulse

Next, we will select signal processing and machine learning blocks, on the **Create impulse** page. The impulse will start out blank, with Raw data and Output feature blocks. Leave the default settings of a 1000 ms Window size and 1000 ms Window increase as shown in Figure 4. This means our audio data will be processed 1 second at a time, starting each 1 second. Using a small window saves memory on the embedded device.

<Frame caption="Figure 4: Creating Impulse block">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/impulse.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=31a1151db9d89d5d09ef9886ab7a4911" width="1288" height="624" data-path=".assets/images/snoring-detection-on-smartphone/impulse.jpg" />
</Frame>

Click on ‘Add a processing block’ and select the **Audio (MFE)** block. Next click on ‘Add a learning block’ and select the **Neural Network (Keras)** block. Click on ‘Save Impulse’ illustrated in Figure 5. The audio block will extract a spectrogram for each window of audio, and the neural network block will be trained to classify the spectrogram as either a 'snoring' or 'no snoring' based on our training dataset. Your resulting impulse will look like this:

<Frame caption="Figure 5: Processing block with MFE and NN classifier">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/learning-block.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=0821a97c70b1f51d9db0796599b61c6a" width="1185" height="585" data-path=".assets/images/snoring-detection-on-smartphone/learning-block.jpg" />
</Frame>

Next we will generate features from the training dataset on the MFE page, as shown in Figure 6. This page shows what the extracted spectrogram looks like for each 1 second window from any of the dataset samples. We can leave the parameters on their defaults.

<Frame caption="Figure 6: Extracted spectrogram">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/spectrogram.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=d1ed561d4f9c70d272e76ff60e74cd38" width="1338" height="655" data-path=".assets/images/snoring-detection-on-smartphone/spectrogram.jpg" />
</Frame>

Next click on the ‘Generate features’ button, which then processes the entire training dataset with this processing block. This creates the complete set of features that will be used to train our Neural Network in the next step. Press the ‘Generate features’ button to start the processing, this will take a couple minutes to complete, and the result of the generated features can be seen in Figure 7.

<Frame caption="Figure 7: Generate features">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/generate-features.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=f95c5903ba6a35d78cdb95371fa34c26" width="1156" height="637" data-path=".assets/images/snoring-detection-on-smartphone/generate-features.jpg" />
</Frame>

We can now proceed to setup and train our neural network on the NN Classifier page. The default neural network works well for continuous sound. Snoring detection is more complicated, so we will configure a richer network using 2D convolution across the spectrogram of each window. 2D convolution processes the audio spectrogram in a similar way to image classification. Refer to the "NN classifier" section in my project for the architecture structure.

## Model Training and Results

To train the model, the number of epochs was set to 100, the leaning rate assigned after several trials is 0.005, and the overall dataset was split into 80% training and 20% validation set. The number of epochs is the number of times the entire dataset is passed through the neural network during training. There is no ideal number for this, and it depends on the data. In Figure 8 we can see the feature explorer for correct and incorrect classification of both classes.

<Frame caption="Figure 8: Feature explorer">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/feature-explorer.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=2a6a4397bbe948aff4b8e2389c346407" width="764" height="770" data-path=".assets/images/snoring-detection-on-smartphone/feature-explorer.jpg" />
</Frame>

The model confusion matrix and on mobile device performance can be seen in Figure 9. The overall accuracy of the quantized int8 model is 94.3%, with 93.5% 'no snoring' and '95.1%' snoring correct classification, and the rest are misclassified.

<Frame caption="Figure 9: Confusion Matrix with model accuracy">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/model-accuracy.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=aa07cedb72357cba1f73ed442723f2b0" width="788" height="562" data-path=".assets/images/snoring-detection-on-smartphone/model-accuracy.jpg" />
</Frame>

After the training model we run the model for testing purposes. It gives us an accuracy of 97.42% on test data, as presented in Figure 10, along with feature exploration.

<Frame caption="Figure 10: Test model accuracy and feature explorer">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/model-testing.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=8624650d1f39bccae3acd6634967a3a6" width="770" height="986" data-path=".assets/images/snoring-detection-on-smartphone/model-testing.jpg" />
</Frame>

## Live Classification

The Live classification page allows us to test the algorithm both with the existing testing data that came with the dataset, or by streaming audio data from your mobile phone or on any microcontroller with audio data processing compatibility. We can start with a simple test by choosing any of the test samples and pressing ‘Load sample’. This will classify the test sample and show the results: in Figure 11 and 12 respectively for both classes with their probability score. We can also test the algorithm with live data. Start with your mobile phone by refreshing the browser page on your phone. Then select your device in the ‘Classify new data’ section and press ‘Start sampling’ as shown in Figure 15.

<Frame caption="Figure 11: Live classification of non-snoring class">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/live-classification.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=2d326103056038c65d91038b8550bc15" width="1138" height="645" data-path=".assets/images/snoring-detection-on-smartphone/live-classification.jpg" />
</Frame>

<br />

<Frame caption="Figure 12: Live classification of snoring class">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/live-classification-2.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=3ee99f012004c08e4fa52b7f17a1c5a7" width="1171" height="639" data-path=".assets/images/snoring-detection-on-smartphone/live-classification-2.jpg" />
</Frame>

## Deployment

In order to deploy the model on a smartphone, go to the browser window on your phone and refresh, then press the ‘Switch to classification mode’ button as shown in Figure 13. This will automatically build the project into a Web Assembly package and execute it on your phone continuously (no cloud required after that, you can even go to airplane mode!). Once you scan the QR code on your mobile it will ask you to access the microphone, as in this project we are using audio data, as shown in Figure 14. After the access is granted, we can see the classification results.

Furthermore, if you would like to extend the project, you can run it on different microcontrollers. Of course, for this project, our aim was to provide the insight of TinyML development on a smartphone.

<Frame caption="Figure 13: Deployment on smartphone">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/deployment.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=b2a77f369352ee27c97564a048745884" width="1330" height="665" data-path=".assets/images/snoring-detection-on-smartphone/deployment.jpg" />
</Frame>

<br />

<Frame caption="Figure 14: Access for microphone">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/classifier.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=68730bfb419c1a8798a8509d4046fb9f" width="538" height="1000" data-path=".assets/images/snoring-detection-on-smartphone/classifier.jpg" />
</Frame>

<br />

<Frame caption="Figure 15: Classification of snoring class on smartphone">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/snoring-detection-on-smartphone/classifier-2.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=9eddb5f396a5afc6b6553c60d6b12531" width="534" height="1000" data-path=".assets/images/snoring-detection-on-smartphone/classifier-2.jpg" />
</Frame>

## Conclusion

This project provides insights of TinyML deployment on a smartphone. In this project, a deep learning model for snoring detection is trained, validated, and tested. A prototype system comprising of a listener module for snoring detection was demonstrated. For future work, extend the default dataset with your own data and background sounds, remember to retrain periodically, and test. You can set up unit tests under the Testing page to ensure that the model is still working as it is extended.

## References

1. T. H. Khan, "A deep learning model for snoring detection and vibration notification using a smart wearable gadget," Electronics, vol. 8, no. 9, article. 987, ISSN 2079-9292, 2019
2. Khan, T. A Deep Learning Model for Snoring Detection and Vibration Notification Using a Smart Wearable Gadget. Electronics 2019, 8, 987. [https://doi.org/10.3390/electronics8090987](https://doi.org/10.3390/electronics8090987)


Built with [Mintlify](https://mintlify.com).