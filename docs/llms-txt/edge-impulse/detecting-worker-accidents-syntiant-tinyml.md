# Source: https://docs.edgeimpulse.com/projects/expert-network/detecting-worker-accidents-syntiant-tinyml.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Detecting Worker Accidents with Audio Classification - Syntiant TinyML

Created By: Solomon Githu

Public Project Link: [https://studio.edgeimpulse.com/public/111611/latest](https://studio.edgeimpulse.com/public/111611/latest)

## Industrial Automation Inefficiencies Towards Accident Detection

The International Labor Organization estimates that there are over 1 million work-related fatalities each year and millions of workers suffer from workplace accidents. However, even as technology advancements have improved worker safety in many industries, some accidents involving workers and machines remain undetected as they occur, possibly even leading to fatalities. This is because of the limitations in Machine Safety Systems. Safety sensors, controllers, switches and other machine accessories have been able to provide safety measures during accidents but some events remain undetected by these systems.

Some accidents which are difficult to be detected in industries includes:

* Falling Objects
* Objects strike or fall on employees
* Slips or Falls of employees
* Chemical burns or exposure
* Workers caught in moving machine parts

## Detecting Worker Accidents with AI

Sound classification is one of the most widely used applications of Machine Learning. When in danger or scared, we humans respond with audible actions such as screaming, crying, or with words such as: "stop", or "help" . This alerts other people that we are in trouble and can also give them instructions such as stopping a machine, or opening/closing a system. We can use sound classification to give hearing to machines and manufacturing setups so that they can be aware of the environment status.

TinyML has enabled us to bring machine learning models to low-cost and low-power microcontrollers. We will use Edge Impulse to develop a machine learning model which is capable of detecting accidents from workers screams and cries. This event can then be used to trigger safety measures such as machine/actuator stop, and sound alarms.

The [Syntiant](https://www.syntiant.com/) TinyML Board is a tiny development board with a microphone and accelerometer, USB host microcontroller and an always-on Neural Decision Processor™, featuring ultra low-power consumption, a fully connected neural network architecture, and fully supported by Edge Impulse. Here are quick start tutorials for [Windows](https://drive.google.com/uc?id=1typui5iFPgFrm_sc9DVpeVH0xDItTvQz\&export=download) and [Mac](https://drive.google.com/uc?id=1jr4pyzAa3LVZzlnCP_WCml7-ZQrxYGrH\&export=download).

<Frame caption="Acoustic Sensing for Machines">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img1_Edge%20Impulse%20Accident%20Detection%20using%20Audio%20Classification.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=6a06a6f6d75b3420c682243a378c486b" width="1600" height="900" data-path=".assets/images/detecting-worker-accidents-with-AI/img1_Edge Impulse Accident Detection using Audio Classification.png" />
</Frame>

## Quick Start

You can find the public project here: [Acoustic Sensing of Worker Accidents](https://studio.edgeimpulse.com/public/111611/latest). To add this project into your account projects, click "Clone this project" at the top of the window. Next, go to the "Deploying to Syntiant TinyML Board" section below to see how you can deploy the model to the Syntiant TinyML board.

Alternatively, to create a similar project, follow the next steps after creating a new Edge Impulse project.

## Data Acquisition

We want to create a model that can recognize both key words and human sounds like cries and screams. For these, we have 4 classes in our model: stop, help, cry and scream. In addition to these classes, we also need another class that is not part of our 4 keywords. We label this class as "unknown" and it has sound of people speaking, machines, and vehicles, among others. Each class has 1 second of audio sounds.

In total, we have 31 minutes of data for training and 8 minutes of data for testing. For the "unknown" class, we can use Edge Impulse Key Spotting Dataset, which can be obtained [here](/datasets/audio/keyword-spotting). From this dataset we use the "noise" audio files.

<Frame caption="Training data">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img2_screenshot%20Data%20Acquisition%20training.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=77c3dd395e2c35381fcef49f8f68f32f" width="518" height="284" data-path=".assets/images/detecting-worker-accidents-with-AI/img2_screenshot Data Acquisition training.png" />
</Frame>

<br />

<Frame caption="testing data">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img3_screenshot%20Data%20Acquisition%20testing.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=5e787131bb25f747d4e8eb04e5087b89" width="513" height="289" data-path=".assets/images/detecting-worker-accidents-with-AI/img3_screenshot Data Acquisition testing.png" />
</Frame>

## Impulse Design

The Impulse design is very unique as we are targeting the Syntiant TinyML board. Under 'Create Impulse' we set the following configurations:

Our window size is 968ms, and window increase is 484ms milliseconds(ms). Click 'Add a processing block' and select Audio (Syntiant). Next, we add a learning block by clicking 'Add a learning block' and select Classification (Keras). Click 'Save Impulse' to use this configuration.

<Frame caption="Create impulse">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img4_screenshot%20Create%20Impulse.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=83be6398216cba96fe4966eef8387359" width="1335" height="635" data-path=".assets/images/detecting-worker-accidents-with-AI/img4_screenshot Create Impulse.png" />
</Frame>

Next we go to our processing block configuration, Syntiant, and first click 'Save parameters'. The preset parameters will work well so we can use them in our case.

On the window 'Generate features', we click the "Generate features" button. Upon completion we see a 3D representation of our dataset. These are the Syntiant blocks that will be passed into the neural network.

<Frame caption="Features">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img5_screenshot%20Generate%20Features.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=3800cf9d4a9228298c98a1425b760453" width="1339" height="645" data-path=".assets/images/detecting-worker-accidents-with-AI/img5_screenshot Generate Features.png" />
</Frame>

Lastly, we need to configure our neural network. Start by clicking "NN Classifier" . Here we set the number of training cycle to 80, with a learning rate of 0.0005. Edge Impulse automatically designs a default Neural Network architecture that works very well without requiring the parameters to be changed. However, if you wish to update some parameters, Data Augmentation can improve your model accuracy. Try adding noise, masking time and frequency bands and asses your model performance with each setting.

With the training cycles and learning rate set, click "Start training", and you will have a neural network when the task is complete. We get an accuracy of 94%, which is pretty good!

<Frame caption="NN parameters">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img6_screenshot%20NN%20Classifier%20parameters.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=51723ad1f8f31cb846ffbb9027dd2507" width="527" height="485" data-path=".assets/images/detecting-worker-accidents-with-AI/img6_screenshot NN Classifier parameters.png" />
</Frame>

<br />

<Frame caption="Training accuracy">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/detecting-worker-accidents-with-AI/img7_screenshot%20NN%20Classifier%20training%20accuracy.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=2a70d69d6ee933023ed7f71667b8cc04" width="519" height="455" data-path=".assets/images/detecting-worker-accidents-with-AI/img7_screenshot NN Classifier training accuracy.png" />
</Frame>

## Model Testing

When training our model, we used 80% of the data in our dataset. The remaining 20% is used to test the accuracy of the model in classifying unseen data. We need to verify that our model has not overfit by testing it on new data. If your model performs poorly, then it means that it overfit (crammed your dataset). This can be resolved by adding more data and/or reconfiguring the processing and learning blocks if needed. Increasing performance tricks can be found in this [guide](/knowledge/guides/increasing-model-performance).

On the left bar, click "Model testing" then "classify all". Our current model has a performance of 91% which is pretty good and acceptable.

From the results we can see new data called "testing" which was obtained from the environment and sent to Edge Impulse. The Expected Outcome column shows which class the collected data belong to. In all cases, our model classifies the sounds correctly as seen in the Result column; it matches the Expected outcome column.

<Frame caption="Model testing">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/detecting-worker-accidents-with-AI/img8_screenshot%20Model%20testing.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=5b049b13193b93d9df691e41bd8b095f" width="1339" height="647" data-path=".assets/images/detecting-worker-accidents-with-AI/img8_screenshot Model testing.png" />
</Frame>

## Deploying to the Syntiant TinyML Board

To deploy our model to the Syntiant Board, first click "Deployment". Here, we will first deploy our model as a firmware on the board. When our audible events (cry, scream, help, stop) are detected, the onboard RGB LED will turn on. When the unknown sounds are detected, the on board RGB LED will be off. This runs locally on the board without requiring an internet connection, and runs with minimal power consumption.

Under "Build Firmware" select Syntiant TinyML.

<Frame caption="Deploy firmware">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/detecting-worker-accidents-with-AI/img9_screenshot%20Deploying%20Firmware.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=656f79c8faac453f9f98f5829cf36c2e" width="1366" height="768" data-path=".assets/images/detecting-worker-accidents-with-AI/img9_screenshot Deploying Firmware.png" />
</Frame>

Next, we need to configure posterior parameters. These are used to tune the precision and recall of our Neural Network activations, to minimize False Rejection Rate and False Activation Rate. More information on posterior parameters can be found here: [Responding to your voice - Syntiant - RC Commands](/tutorials/hardware/syntiant-ndp-keyword-spotting), in "Deploying to your device" section.

Under "Configure posterior parameters" click "Find posterior parameters". Check all classes apart from "unknown", and for calibration dataset we use "No calibration (fastest)". After setting the configurations, click "Find parameters".

<Frame caption="Find posterior parameters">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img10_screenshot%20Deploying%20Find%20posterior%20parameters.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=0aba6cac711242f3578ddf4ab92547d1" width="1366" height="768" data-path=".assets/images/detecting-worker-accidents-with-AI/img10_screenshot Deploying Find posterior parameters.png" />
</Frame>

This will start a new task which we have to wait until it is finished.

<Frame caption="posterior parameters done">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img11_screenshot%20Deploying%20Configure%20posterior%20parameters%20Job%20complete.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=fb9974372f58f502bddf3df4b0ab16dc" width="1366" height="768" data-path=".assets/images/detecting-worker-accidents-with-AI/img11_screenshot Deploying Configure posterior parameters Job complete.png" />
</Frame>

When the job is completed, close the popup window and then click "Build" options to build our firmware. The firmware will be downloaded automatically when the build job completes. Once the firmware is downloaded, we first need to unzip it. Connect a Syntiant TinyML board to your computer using a USB cable. Next, open the unzipped folder and run the flashing script based on your Operating System.

We can connect to the board's firmware over Serial. To do this, open a terminal, select the COM Port of the Syntiant TinyML board with settings 115200 8-N-1 settings (in Arduino IDE, that is 115200 baud Carriage return).

Sounds such as "stop", "help", "aaagh!" or crying will turn the RGB LED to red.

<Frame caption="Syntiant red-light green-light">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img12_Syntiant%20TinyML%20board%20-%20inference%20red%20green.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=5a992d7deb3734eb6d316f23bd24fd84" width="1600" height="900" data-path=".assets/images/detecting-worker-accidents-with-AI/img12_Syntiant TinyML board - inference red green.png" />
</Frame>

<br />

<Frame caption="Predictions on serial port">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img13_Serial%20running%20model%20on%20Syntiant%20board.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=fb5af7045f1dbf16cd0f974208792a2f" width="356" height="684" data-path=".assets/images/detecting-worker-accidents-with-AI/img13_Serial running model on Syntiant board.png" />
</Frame>

For the "unknown" sounds, the RGB LED is off. While configuring the posterior parameters, the detected classes that we selected are the ones which trigger the RGB LED lighting.

## Taking it one step further

We can use our Machine Learning model as a safety feature for actuators, machines or other operations involving people and machines.

To do this we can build custom firmware for our Syntiant TinyML board that turns a GPIO pin HIGH or LOW based on the detected event. The GPIO pin can then be connected to a controller that runs an actuator or a system. The controller can then turn off the actuator or process when a signal is sent by the Syntiant TinyML board.

<Frame caption="Syntiant TinyML wired signalling">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img14_Syntiant%20TinyML%20-%20wired%20signalling.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=5b885e114a9625dbb1baed4f005b0dee" width="740" height="291" data-path=".assets/images/detecting-worker-accidents-with-AI/img14_Syntiant TinyML - wired signalling.png" />
</Frame>

A custom firmware was then created to turn on GPIO 1 HIGH (3.3V) of the Syntiant TinyML Board whenever the alarming sounds are detected. GPIO 1 is next to the GND pin so we can easily use a 2-pin header to connect our TinyML board with another device.

<Frame caption="Syntiant TinyML pinout">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img15_screenshot%20Syntiant%20TinyML%20board%20pinout.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=1812385d7d74da1f5098924bc4449d0b" width="695" height="649" data-path=".assets/images/detecting-worker-accidents-with-AI/img15_screenshot Syntiant TinyML board pinout.png" />
</Frame>

<br />

<Frame caption="Custom firmware">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img16_screenshot%20Arduino%20custom%20firmware%20code.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=9f10b1fc4e3a626337ceffe55468a9c3" width="1312" height="302" data-path=".assets/images/detecting-worker-accidents-with-AI/img16_screenshot Arduino custom firmware code.png" />
</Frame>

Awesome! What's next now? Checkout the custom firmware [here](https://github.com/SolomonGithu/syntiant-tinyml-firmware-acoustic-detection) and add intelligent sensing to your actuators and also home automation devices!

## Intelligent sensing for 8-bit LoRaWAN actuator

I leveraged my TinyML solution and used it to add more sensing to my LoRaWAN actuator. I connected the Syntiant TinyML board to an Atmega and SX1276 based development board called the WaziAct. This board is designed to play as a production LoRa actuator node with an onboard relay which I often use to actuate pumps, solenoids, and electrical devices. I programmed the board to read the pin status connected to the Syntiant TinyML board and when a signal is received it stops executing the main tasks. An alert is also sent to the gateway via LoRa while the main tasks remain halted. The Arduino code can be accessed [here](https://github.com/SolomonGithu/syntiant-tinyml-firmware-acoustic-detection/tree/main/safety_triggering_with_TinyML).

<Frame caption="Syntiant TinyML LoRaWAN actuator">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img17_Syntiant%20and%20an%20IoT%20board.jpg?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=db3301f1ef646fc689a69ca22101b7ba" width="1333" height="1000" data-path=".assets/images/detecting-worker-accidents-with-AI/img17_Syntiant and an IoT board.jpg" />
</Frame>

<br />

<Frame caption="Accident detected">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/detecting-worker-accidents-with-AI/img18_Arduino%20accident%20detected.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=9dcfaed98362ef7d01a38238d022424e" width="309" height="363" data-path=".assets/images/detecting-worker-accidents-with-AI/img18_Arduino accident detected.png" />
</Frame>

Below is a sneak peak of an indoor test… Now my "press a button" LoRaWAN actuations can run without causing harm such as turning on a faulty device, pouring water via solenoid/pump in unsafe conditions, and other accidental events!

<Frame caption="Syntiant TinyML LoRaWAN testing">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/detecting-worker-accidents-with-AI/gif_syntiant_stop.gif" />
</Frame>

## Conclusion

We have seen how we can use sounds to train and deploy our ML solution easily and also run them locally on a development board. TinyML-based intelligent sensing, such as is shown here, is just one of the many solutions that TinyML offers.

With Edge Impulse, developing ML models and deploying them has always been easy. The Syntiant TinyML board was chosen for this project because it provides ultra-low power consumption, fully connected neural network architecture, has an onboard microphone, is physically small, and is also fully supported by Edge Impulse.


Built with [Mintlify](https://mintlify.com).