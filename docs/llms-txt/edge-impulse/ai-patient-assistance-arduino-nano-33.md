# Source: https://docs.edgeimpulse.com/projects/expert-network/ai-patient-assistance-arduino-nano-33.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI-Powered Patient Assistance - Arduino Nano 33 BLE Sense

Created By: [Adam Milton-Barker](https://www.adammiltonbarker.com/)

Public Project Link: [https://studio.edgeimpulse.com/public/140923/latest](https://studio.edgeimpulse.com/public/140923/latest)

## Project Demo

<iframe src="https://www.youtube.com/embed/JAw5SRfa95g" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Project Repo

[https://www.adammiltonbarker.com/projects/downloads/AI-Patient-Assistance.zip](https://www.adammiltonbarker.com/projects/downloads/AI-Patient-Assistance.zip)

## Introduction

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/intro.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=400641c864e312ec992a176e9e52d784" width="1200" height="800" data-path=".assets/images/ai-patient-assistance/intro.jpg" />
</Frame>

When hospitals are busy it may not always be possible for staff to be close when help is needed, especially if the hospital is short staffed. To ensure that patients are looked after promptly, hospital staff need a way to be alerted when a patient is in discomfort or needs attention from a doctor or nurse.

## Solution

A well known field of Artificial Intelligence is voice recognition. These machine learning and deep learning models are trained to recognize phrases or keywords, and combined with the Internet of Things can create fully autonomous systems that require no human interaction to operate.

As technology has advanced, it is now possible to run voice recognition solutions on low cost, resource constrained devices. This not only reduces costs considerably, but also opens up more possibilities for innovation. The purpose of this project is to show how a machine learning model can be deployed to a low cost IoT device (Arduino Nano 33 BLE SENSE), and used to notify staff when a patient needs their help.

The device will be able to detect three keywords **Doctor**, **Nurse**, and **Help**. The device also acts as a BLE peripheral, BLE centrals/masters such as a central server for example, could connect and listen for data coming from the device. The server could then process the incoming data and send a message to hospital staff or sound an alarm.

## Hardware

* Arduino Nano 33 BLE Sense [Buy](https://store.arduino.cc/products/arduino-nano-33-ble-sense)

## Platform

* Edge Impulse [Visit](https://www.edgeimpulse.com)

## Software

* [Edge Impulse CLI](/tools/clis/edge-impulse-cli)
* [Arduino CLI](https://arduino.github.io/arduino-cli/latest/)
* [Arduino IDE](https://www.arduino.cc/en/software)

## Project Setup

Head over to [Edge Impulse](https://www.edgeimpulse.com) and create your account or login. Once logged in you will be taken to the project selection/creation page.

### Create New Project

Your first step is to create a new project. From the project selection/creation you can create a new project.

<Frame caption="Create Edge Impulse project">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/new-project.png?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=30b6437ffc812cb3459012ac0ac8bb68" width="1600" height="738" data-path=".assets/images/ai-patient-assistance/new-project.png" />
</Frame>

Enter a **project name**, select **Developer** and click **Create new project**.

<Frame caption="Choose project type">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/new-project-2.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=52d0df3e5843b980c0332551536497fc" width="1600" height="746" data-path=".assets/images/ai-patient-assistance/new-project-2.jpg" />
</Frame>

We are going to be creating a voice recognition system, so now we need to select **Audio** as the project type.

### Connect Your Device

<Frame caption="Connect device">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/device.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=3221f21df227562a1ca160e2616386bd" width="1600" height="739" data-path=".assets/images/ai-patient-assistance/device.jpg" />
</Frame>

You need to install the required dependencies that will allow you to connect your device to the Edge Impulse platform. This process is documented on the [Edge Impulse Website](/hardware/boards/arduino-nano-33-ble-sense) and includes installing:

* [Edge Impulse CLI](/tools/clis/edge-impulse-cli)
* [Arduino CLI](https://arduino.github.io/arduino-cli/latest/)

Once the dependencies are installed, connect your device to your computer and press the **RESET** button twice to enter into bootloader mode, the yellow LED should now be pulsating.

Now download the the [latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/arduino-nano-33-ble-sense.zip) and unzip it, then double click on the relevant script for your OS either `flash_windows.bat`, `flash_mac.command` or `flash_linux.sh`.

<Frame caption="Edge Impulse firmware installed">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/firmware.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=3785d067838d7ec082e30218b973388d" width="1600" height="843" data-path=".assets/images/ai-patient-assistance/firmware.jpg" />
</Frame>

Once the firmware has been flashed you should see the output above, hit enter to close command prompt/terminal.

Open a new command prompt/terminal, and enter the following command:

`edge-impulse-daemon`

If you are already connected to an Edge Impulse project, use the following command:

`edge-impulse-daemon --clean`

Follow the instructions to log in to your Edge Impulse account.

<Frame caption="Device connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/connected.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=1535783ee56f08ac077e2ebe7449b499" width="1600" height="679" data-path=".assets/images/ai-patient-assistance/connected.jpg" />
</Frame>

Once complete head over to the devices tab of your project and you should see the connected device.

## Data Acquisition

We are going to create our own dataset, using the built in microphone on the Arduino Nano 33 BLE Sense. We are going to collect data that will allow us to train a machine learning model that can detect the words/phrases **Doctor**, **Nurse**, and **Help**.

We will use the **Record new data** feature on Edge Impulse to record 15 sets of 10 utterances of each of our keywords, and then we will split them into individual samples.

Ensuring your device is connected to the Edge Impulse platform, head over to the **Data Acquisition** tab to continue.

<Frame caption="Data acquisition">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/data-acquisition.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=6f15a0e94fc9284304b5285fcf626f13" width="1600" height="781" data-path=".assets/images/ai-patient-assistance/data-acquisition.jpg" />
</Frame>

In the **Record new data**, make sure you have selected your Arduino Nano 33 BLE Sense, then select **Built in microphone**, set the label as **Doctor**, change the sample length to 20000 (20 seconds), and leave all the other settings as.

Here we are going to record the data for the word **Doctor**. Make sure the microphone is close to you, click **Start sampling** and record yourself saying **Doctor** ten times.

<Frame caption="Recorded sample">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-patient-assistance/recording-1.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=4590db7c1fe52acdb76d6543b5683da1" width="1600" height="750" data-path=".assets/images/ai-patient-assistance/recording-1.jpg" />
</Frame>

You will now see the uploaded data in the **Collected data** window, next we need to split the data into ten individual samples.

<Frame caption="Data split">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-patient-assistance/recording-2.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=5c31bef0a824f227d083361224829650" width="1600" height="777" data-path=".assets/images/ai-patient-assistance/recording-2.jpg" />
</Frame>

Click on the dots to the right of the sample and click on **Split sample**, this will bring up the sample split tool. Here you can move the windows until each of your samples are safely in a window. You can fine tune the splits by dragging the windows until you are happy, then click on **Split**

<Frame caption="Split data">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-patient-assistance/recording-3.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=eb520260705ef1925eb17a5ab367de33" width="1600" height="780" data-path=".assets/images/ai-patient-assistance/recording-3.jpg" />
</Frame>

You will see all of your samples now populated in the **Collected data** window. Now you need to repeat this action 14 more times for the **Doctor** class, resulting in 150 samples for the Doctor class. Once you have finished, repeat this for the remaining classes: **Nurse** and **Help**. You will end up with a dataset of 450 samples, 150 per class.

<Frame caption="Main data">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/data-1.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=3b674bd0c19b230c61d8903be0d0cedf" width="1600" height="775" data-path=".assets/images/ai-patient-assistance/data-1.jpg" />
</Frame>

Now we have all of our main classes complete, but we still need a little more data. We need a **Noise** class that will help our model determine when nothing is being said, and we need an **Unknown** class, for things that our model may come up against that are not in the dataset.

For the noise class we will mix silent samples, and some other general noise samples. First of all record 100 samples with no speaking and store them in an **Noise** class.

<Frame caption="Data upload">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/data-2.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=0c2cf926ef8147652dd0a774d2b0fd10" width="1600" height="778" data-path=".assets/images/ai-patient-assistance/data-2.jpg" />
</Frame>

Next download the [Microsoft Scalable Noisy Speech Dataset](https://github.com/microsoft/MS-SNSD) and extract the data. Navigate to the **Noise** directory and copy 50 random samples. Next go to the **Data Acquisition** tab and upload the new data into the **Noise** class. Finally copy 100 samples from the unknown class and upload to the Edge Impulse platform as an **Unknown** class.

### Split Dataset

<Frame caption="split-data.jpg">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-patient-assistance/split-dataset.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=9ef8960fcf4da694a97465ab9dcbd9b7" width="1600" height="751" data-path=".assets/images/ai-patient-assistance/split-dataset.jpg" />
</Frame>

We need to split the dataset into test and training samples. To do this head to the dashboard and scroll to the bottom of the page, then click on the **Perform train/test split**

<Frame caption="Recorded dataset">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-patient-assistance/train-test.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=86c942dc93f6a9e0a378a2c00cf14dc6" width="1600" height="781" data-path=".assets/images/ai-patient-assistance/train-test.jpg" />
</Frame>

Once you have done this, head back to the data acquisition tab and you will see that your data has been split.

## Create Impulse

<Frame caption="Create Impulse">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/impulse.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=d057b6cf93a7f7f4d1b62114514584aa" width="1600" height="749" data-path=".assets/images/ai-patient-assistance/impulse.jpg" />
</Frame>

Now we are going to create our network and train our model.

<Frame caption="Add processing block">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-patient-assistance/processing-block.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=45b2a46ff11a6bf34a8f47a67ddff2ab" width="1600" height="749" data-path=".assets/images/ai-patient-assistance/processing-block.jpg" />
</Frame>

Head to the **Create Impulse** tab and change the window size to 2000ms. Next click **Add processing block** and select **Audio (MFCC)**, then click **Add learning block** and select **Classification (Keras)**.

<Frame caption="Created Impulse">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/impulse-2.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=19ed8a8f2af0e7d8e3af2c2c79f649bd" width="1600" height="780" data-path=".assets/images/ai-patient-assistance/impulse-2.jpg" />
</Frame>

Now click **Save impulse**.

### MFCC Block

#### Parameters

<Frame caption="Parameters">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/mfcc.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=83a3aec014dec097b9570c39812e2d65" width="1600" height="779" data-path=".assets/images/ai-patient-assistance/mfcc.jpg" />
</Frame>

Head over to the **MFCC** tab and click on the **Save parameters** button to save the MFCC block parameters.

#### Generate Features

<Frame caption="Generate Features">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/generate-features.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=55c464109799b96bbc676b8e20fda660" width="1600" height="775" data-path=".assets/images/ai-patient-assistance/generate-features.jpg" />
</Frame>

If you are not automatically redirected to the **Generate features** tab, click on the **MFCC** tab and then click on **Generate features** and finally click on the **Generate features** button.

<Frame caption="Generated Features">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/generate-features-2.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=12a00095e4bcc321724362ab1d341c2b" width="1600" height="777" data-path=".assets/images/ai-patient-assistance/generate-features-2.jpg" />
</Frame>

Your data should be nicely clustered and there should be as little mixing of the classes as possible. You should inspect the clusters and look for any data that is clustered incorrectly (You don't need to worry so much about the noise and unknown classes being mixed). If you find any data out of place, you can relabel or remove it. If you make any changes click **Generate features** again.

## Training

<Frame caption="Training">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-patient-assistance/training.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=17f829e14a3a1a2f828e28114382545f" width="1600" height="781" data-path=".assets/images/ai-patient-assistance/training.jpg" />
</Frame>

Now we are going to train our model. Click on the **NN CLassifier** tab then click **Auto-balance dataset**, **Data augmentation** and then **Start training**.

<Frame caption="Training complete">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-patient-assistance/training-2.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=2aebee16d5034da978500c27a15e1df7" width="1600" height="749" data-path=".assets/images/ai-patient-assistance/training-2.jpg" />
</Frame>

Once training has completed, you will see the results displayed at the bottom of the page. Here we see that we have 99.2% accuracy. Lets test our model and see how it works on our test data.

## Testing

### Platform Testing

<Frame caption="Test model">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-patient-assistance/testing.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=dd6af2800d0c9ee0e5bafb0bcf500efd" width="1600" height="778" data-path=".assets/images/ai-patient-assistance/testing.jpg" />
</Frame>

Head over to the **Model testing** tab where you will see all of the unseen test data available. Click on the **Classify all** and sit back as we test our model.

<Frame caption="Test model results">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-patient-assistance/testing-2.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=37236f6d5c72125818510eef499835eb" width="1600" height="750" data-path=".assets/images/ai-patient-assistance/testing-2.jpg" />
</Frame>

You will see the output of the testing in the output window, and once testing is complete you will see the results. In our case we can see that we have achieved 96.62% accuracy on the unseen data, and a high F-Score on all classes.

### On Device Testing

<Frame caption="Live testing">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-patient-assistance/testing-3.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=961fe1be08411e7fda353036225199ac" width="1600" height="776" data-path=".assets/images/ai-patient-assistance/testing-3.jpg" />
</Frame>

Now we need to test how the model works on our device. Use the **Live classification** feature to record some samples for classification. Your model should correctly identify the class for each sample.

## Performance Calibration

<Frame caption="Performance Calibration">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/calibration.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=cef44a1b12a30358d230114c4edaa023" width="1600" height="776" data-path=".assets/images/ai-patient-assistance/calibration.jpg" />
</Frame>

Edge Impulse has a great new feature called **Performance Calibration**, or **PerfCal**. This feature allows you to run a test on your model and see how well it will perform in the real world. The system will create a set of post processing configurations for you to choose from. These configurations help to minimize either false activations or false rejections

<Frame caption="Turn on perfcal">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/calibration-2.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=48771e86584c5743f6a0779c70e68da6" width="1600" height="778" data-path=".assets/images/ai-patient-assistance/calibration-2.jpg" />
</Frame>

Once you turn on perfcal, you will see a new tab in the menu called **Performance calibration**. Navigate to the perfcal page and you will be met with some configuration options.

<Frame caption="Perfcal settings">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/calibration-3.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=ac1afe25efd3d486e29efadecae713e1" width="1600" height="768" data-path=".assets/images/ai-patient-assistance/calibration-3.jpg" />
</Frame>

Select the **Noise** class from the drop down, and check the Unknown class in the list of classes below, then click **Run test** and wait for the test to complete.

<Frame caption="Perfcal configs">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/calibration-4.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=475cdf0e0681723b5c286a074dc088b3" width="932" height="541" data-path=".assets/images/ai-patient-assistance/calibration-4.jpg" />
</Frame>

The system will provide a number of configs for you to choose from. Choose the one that best suits your needs and click **Save selected config**. This config will be deployed to your device once you download and install the library on your device.

## Versioning

<Frame caption="Versioning">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-patient-assistance/versioning.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=262fbddee7f1ab99e1232c96f9db7566" width="1600" height="741" data-path=".assets/images/ai-patient-assistance/versioning.jpg" />
</Frame>

We can use the versioning feature to save a copy of the existing network. To do so head over to the **Versioning** tab and click on the **Create first version** button.

<Frame caption="Versions">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-patient-assistance/versioning-2.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=da14eae3301a5bea505cf312f6bd946d" width="1600" height="737" data-path=".assets/images/ai-patient-assistance/versioning-2.jpg" />
</Frame>

This will create a snapshot of your existing model that we can come back to at any time.

## Deployment

Now we will deploy an Arduino library to our device that will allow us to run the model directly on our Arduino Nano 33 BLE Sense.

<Frame caption="Build">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/deployment.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=75015171ead3ba4e3ee6f845f02a69e1" width="1600" height="731" data-path=".assets/images/ai-patient-assistance/deployment.jpg" />
</Frame>

Head to the deployment tab and select **Arduino Library** then scroll to the bottom and click **Build**.

<Frame caption="Build optimizations">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/eon.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=2ed6790fc18672ab3450b306c77ee5f7" width="1600" height="732" data-path=".assets/images/ai-patient-assistance/eon.jpg" />
</Frame>

Note that the EON Compiler is selected by default which will reduce the amount of memory required for our model.

<Frame caption="Arduino library">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/library.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=7079c366363354740c4b36967467e60a" width="1600" height="734" data-path=".assets/images/ai-patient-assistance/library.jpg" />
</Frame>

Once the library is built, you will be able to download it to a location of your choice.

## Arduino IDE

<Frame caption="Arduino library">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/arduino-ide.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=aab1981b2b2a401e8bbd38b8151052c8" width="1600" height="862" data-path=".assets/images/ai-patient-assistance/arduino-ide.jpg" />
</Frame>

Once you have downloaded the library, open up Arduino IDE, click **Sketch** -> **Include library** -> **Upload .ZIP library...**, navigate to the location of your library, upload it and then restart the IDE.

### Non-Continuous Classification

<Frame caption="Non-continuous classification">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/inferencing.gif?s=0cfc2d59ff8e74a40e94df5e5bbbed04" width="600" height="338" data-path=".assets/images/ai-patient-assistance/inferencing.gif" />
</Frame>

Open the IDE again and go to **File** -> **Examples**, scroll to the bottom of the list, go to **AI\_Patient\_Assistance\_inferencing** -> **nano\_ble33\_sense** -> **nano\_ble33\_sense\_microphone**.

Download this project from [here](https://www.adammiltonbarker.com/projects/downloads/AI-Patient-Assistance.zip). Copy the contents of **libraries/ai\_patient\_assistance/ai\_patient\_assistance.ino** into the file and upload to your board. This may take some time.

<Frame caption="Arduino IDE serial">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/library-2.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=a90a8e6ebdf73b549a02bebc882ebed5" width="1600" height="734" data-path=".assets/images/ai-patient-assistance/library-2.jpg" />
</Frame>

Once the script is uploaded, open up serial monitor and you will see the output from the program. The green LED on your device will turn on when it is recording, and off when recording has ended.

<Frame caption="Arduino Nano 33 BLE Sense">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/hardware.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=13c24cfc4b1a417e1c3cb2e2e94571e0" width="1280" height="720" data-path=".assets/images/ai-patient-assistance/hardware.jpg" />
</Frame>

Now you can test your program by saying any of the keywords when the green light is on. If a keyword is detected the red LED will turn on.

### Continuous Classification

<Frame caption="Continuous classification">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/inferencing-2.gif?s=2c3dd405d527b758a8f5e76cd83db059" width="600" height="338" data-path=".assets/images/ai-patient-assistance/inferencing-2.gif" />
</Frame>

Now open **AI\_Patient\_Assistance\_inferencing** -> **nano\_ble33\_sense** -> **nano\_ble33\_sense\_microphone\_continuous**, copy the contents of **libraries/ai\_patient\_assistance/ai\_patient\_assistance\_continuous.ino** into the file and upload to your board.

Once the script is uploaded, open up serial monitor and you will see the output from the program. The red LED will blink when a classification is made.

#### BLE

This program acts as a BLE peripheral which basically advertises itself and waits for a central to connect to it before pushing data to it. In this case our central/master is a smart phone, but in the real world this would be a BLE enabled server that would be able to interact with a database, send SMS, or forward messages to other devices/applications using a machine to machine communication protocol such as MQTT.

<Frame caption="nRF Connect BLE">
  <img src="https://mintcdn.com/edgeimpulse/7V7DYmlHwneiNhtD/.assets/images/ai-patient-assistance/ble.jpg?fit=max&auto=format&n=7V7DYmlHwneiNhtD&q=85&s=2e410d4d6783e39dd6b61f6a19165c34" width="1023" height="720" data-path=".assets/images/ai-patient-assistance/ble.jpg" />
</Frame>

You can use a free BLE app such as [nRF Connect desktop](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-desktop) or [nRF Connect Mobile](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp\&hl=en_GB\&gl=US) to connect to your device and read the data published by it.

When your BLE app connects to the program, the LED light will turn blue, once the app disconnects the LED will turn off.

## Conclusion

Here we have created a simple but effective solution for detecting specific keywords that can be part of a larger automated patient assistance system. Using a fairly small dataset we have shown how the Edge Impulse platform is a useful tool in quickly creating and deploying deep learning models on edge devices.

You can train a network with your own keywords, or build off the model and training data provided in this tutorial. Ways to further improve the existing model could be:

* Record more samples for training
* Record samples from multiple people


Built with [Mintlify](https://mintlify.com).