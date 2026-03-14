# Source: https://docs.edgeimpulse.com/projects/expert-network/gesture-recognition-patient-communication-silabs-thunderboard-sense-2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Gesture Recognition for Patient Communication - SiLabs Thunderboard Sense 2

Created By: Manivannan Sivan

Public Project Link: [https://studio.edgeimpulse.com/public/147925/latest](https://studio.edgeimpulse.com/public/147925/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/intro.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=185eec046c37a28f5e83adb40637e75b" width="1078" height="675" data-path=".assets/images/patient-gesture-recognition/intro.jpg" />
</Frame>

## Problem Statement

Some hospital patients, elderly people, or patients require constant monitoring might need support at any time. However, they may have difficulty communicating due to injuries, mental ability, energy level / effort, glucose level, or other reasons. It can also be challenging for caretakers to tend to all patients.

## TinyML Solution

I have created a wearable using a SiLabs Thunderboard Sense 2, which can be fitted to the patient’s finger. The patient can call the caretakers by tapping their finger, or rotating it, and the tinyML model running on the hardware will predict the gesture and communicate to the caretakers through BLE communication. The caretakers can get notified in the Light Blue Application on their devices.

<Frame caption="Wearable Prototype">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/prototype.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=56054ed8f51d36aabdb8bf3ff6f0647d" width="914" height="1000" data-path=".assets/images/patient-gesture-recognition/prototype.jpg" />
</Frame>

<br />

<Frame caption="Predicted Model Result in LightBlue App">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/bluetooth-app.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=2b5db8db8ad13bf15f8125c64169e6b4" width="828" height="855" data-path=".assets/images/patient-gesture-recognition/bluetooth-app.jpg" />
</Frame>

I have trained a model with different tap actions and normal hand movements, so that it can classify the normal movements and emergency tap options.

The model will predict an action in any of these categories:

* Help
* Emergency
* Water
* Idle
* Random Movements

Now let’s see how I trained the model and tested it on real hardware in detail.

## Data Acquisition

Connect the Thunderboard Sense 2 board to your system and flash the firmware from this [link](/hardware/boards/silabs-thunderboard-sense-2).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/firmware.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=9b101ec180eca4e5d94645805b3cbc42" width="1562" height="428" data-path=".assets/images/worker-safety-posture-detection/firmware.jpg" />
</Frame>

Once it is flashed, run the below command:

`edge-impulse-daemon`

Now your board is connected to your Edge Impulse account. I have used a cloth finger cover and attached the SiLabs board with a rubber band.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/prototype-2.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=42e01b646e8c367d588356cea6d6571e" width="827" height="1000" data-path=".assets/images/patient-gesture-recognition/prototype-2.jpg" />
</Frame>

### Help

To get any support from caretakers, the patient can use this gesture.

For gesture - "Help", I have just tapped my hand on the flat surface gently with 1 second delay. Let's say for each second, I have done one tap action. I have collected 2 minutes of "Help" data for training and 20 seconds of data for testing.

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/patient-gesture-recognition/help.gif" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/data-acquisition.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=fd79b37d9508aa5a49b940e84dbd2006" width="1600" height="684" data-path=".assets/images/patient-gesture-recognition/data-acquisition.jpg" />
</Frame>

### Emergency

For "Emergency" action, I have continuously tapped the finger with a SiLabs board on a flat surface for five times without any delay. I repeated this process for about 2 minutes to collect enough training data, and another 20 seconds for testing data.

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/patient-gesture-recognition/emergency.gif" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/data-acquisition-2.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=97c37704827fe7af11bdadc7419c81d2" width="1600" height="866" data-path=".assets/images/patient-gesture-recognition/data-acquisition-2.jpg" />
</Frame>

### Water

For basic needs like water, food etc. the patient can use this gesture to communicate. This helps caretakers understand the needs in advance and bring water to them.

Lift the hand slightly from the surface, and move it sideways left and right a few times. Again, I have collected 2 minutes of data for model training, and 20 seconds data for testing.

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/patient-gesture-recognition/water.gif" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/data-acquisition-3.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=560b2fc494f4ba58ccf5880ece105c01" width="1600" height="978" data-path=".assets/images/patient-gesture-recognition/data-acquisition-3.jpg" />
</Frame>

### Idle

Idle action is when the patient is sleeping or keeping their hands idle for some time. This data is collected and trained so that it is differentiated from other actions.

### Random Movements

The model is trained on other movement data like walking, combing hair, getting a drink, etc. Again this is for differentiation.

## Create Impulse

Now we have 10 minutes and 20 seconds of data. And the data is split into a 84:16 ratio as training and testing data.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/AQr6kHeg-keHHzV6/.assets/images/patient-gesture-recognition/train-test.jpg?fit=max&auto=format&n=AQr6kHeg-keHHzV6&q=85&s=531384125d46da560b0865115f748fa9" width="1586" height="760" data-path=".assets/images/patient-gesture-recognition/train-test.jpg" />
</Frame>

In the Create Impulse section inside the Edge Impulse Studio, the sampling window size is set to 4000ms and window increase size also increases to 4000ms.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/impulse.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=4ffe0f3643fb97dc7020684a8826575a" width="1600" height="582" data-path=".assets/images/patient-gesture-recognition/impulse.jpg" />
</Frame>

I have selected spectral features as a preprocessing block, and the Generated Features are shown below:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/feature-explorer.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=e5605f01c3baa025e18e7ff13983f94f" width="1506" height="862" data-path=".assets/images/patient-gesture-recognition/feature-explorer.jpg" />
</Frame>

## Model Training

In Model training, I have used sequential dense neural networks, and the learning rate is set to 0.0005 and the training cycle is 100.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/AQr6kHeg-keHHzV6/.assets/images/patient-gesture-recognition/training-1.jpg?fit=max&auto=format&n=AQr6kHeg-keHHzV6&q=85&s=b64db41dde993841f2dd8cc47154735e" width="1442" height="644" data-path=".assets/images/patient-gesture-recognition/training-1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/AQr6kHeg-keHHzV6/.assets/images/patient-gesture-recognition/training-2.jpg?fit=max&auto=format&n=AQr6kHeg-keHHzV6&q=85&s=49dccd5d55cd4a77932a6a2d8a4a7188" width="1456" height="445" data-path=".assets/images/patient-gesture-recognition/training-2.jpg" />
</Frame>

## Model Accuracy

After training, the model achieved 100% accuracy, and the F1 score is listed below:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/accuracy.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=d5fb017855245e2239ebfd3da2e10050" width="1452" height="723" data-path=".assets/images/patient-gesture-recognition/accuracy.jpg" />
</Frame>

## Model Testing

In Model testing, I have used the Testing data that we set aside earlier.

The model achieved 96% in model testing data. This data was completely new and not used in training sessions. The decrease in model accuracy that we noticed does sometimes happen, in this case it looks like some of the "Random" movements were identified as "Help" actions.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/testing-1.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=bce2cb23bb253963a77c7379386e4c86" width="1464" height="776" data-path=".assets/images/patient-gesture-recognition/testing-1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/testing-2.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=c5b882bd0e948b375f084db7e8b0a80b" width="1414" height="673" data-path=".assets/images/patient-gesture-recognition/testing-2.jpg" />
</Frame>

## Deployment

Go to the Deployment section and select Firmware option - Thunderboard Sense 2. This will download the firmware to your system.

Once the Firmware file is downloaded, copy the `.bin` file and paste it in the `TB004` drive. This will flash the software onto the Thunderboard Sense 2 board. Once it is flashed, reset the board. Connect the 3v battery into it.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/deployment.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=e44511f87093269bf872d8a1335b8232" width="1600" height="642" data-path=".assets/images/worker-safety-posture-detection/deployment.jpg" />
</Frame>

## Testing the Device

To test out a real scenario, download the LightBlue App from the Apple App Store or Google Play Store. This app will be used to communicate with the Thunderboard Sense 2.

Open the App and connect to the Edge Impulse service (Make sure board is powered up).

Change a few settings in the app:

* Subscribe to the 2A56 characteristic.
* Decode the message as UTF8 (click on HEX in the top right corner in LightBlue to switch).
* Connect the wearable to your finger and start performing the different gesture actions.

Enable the "listening" option in the app, as well. You will be notified only when the previous prediction result differs from the current prediction result.

Sample results in the LightBlue app are shown below:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/functionality.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=83853ad577481c7f4ae6462010473693" width="1385" height="1000" data-path=".assets/images/patient-gesture-recognition/functionality.jpg" />
</Frame>

For every action , the predicted result with a timestamp is displayed in the app.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/patient-gesture-recognition/results.jpg?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=00d86875fb0572b4f9a66a5e57e46c22" width="1338" height="679" data-path=".assets/images/patient-gesture-recognition/results.jpg" />
</Frame>

## Summary :

This TinyML-based wearable can be used by patients who can't easily communicate with caretakers for various reasons.


Built with [Mintlify](https://mintlify.com).