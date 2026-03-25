# Source: https://docs.edgeimpulse.com/hardware/deployments/run-arduino-app-lab.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Arduino App Lab

Impulses can be deployed via App Lab to your Arduino UNO Q. Arduino App Lab is a platform that enables developers to easily build and share Arduino applications and offers an intuitive interface to deploy the application locally in just one click.

In Edge Impulse Studio you can deploy your model as a either `Linux aarch64` or `Linux Arduino UNO Q (GPU)`. Then, import it on your UNO Q to run edge AI applications that use your custom model.

<Frame caption="Arduino App Lab version 0.1.23">
  <img src="https://mintcdn.com/edgeimpulse/7Xfyy0HVFXNw8ySY/.assets/images/arduino-app-lab/arduino-app-lab-v0123.png?fit=max&auto=format&n=7Xfyy0HVFXNw8ySY&q=85&s=01df0b14093b8de0c62342f3f22aadad" width="1600" height="900" data-path=".assets/images/arduino-app-lab/arduino-app-lab-v0123.png" />
</Frame>

This tutorial guides you through deploying App Lab examples applications, and new custom applications that use your own impulse, to the Arduino UNO Q. The tutorial is designed for the Arduino UNO Q (2Gb) using App Lab version 0.1.23.

Here's a video overview of the Arduino UNO Q and how to run custom models from Edge Impulse:

<iframe src="https://www.youtube.com/embed/i_Iq3TTqpgU" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Prerequisites

Before you start, make sure you have completed the [Arduino UNO Q setup](/hardware/boards/arduino-uno-q) using a monitor, keyboard, and mouse to enable WiFi and SSH access. Additionally, make sure you followed one of the following tutorials and have a trained impulse:

* [Sound recognition](/tutorials/end-to-end/sound-recognition)
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Image classification](/tutorials/end-to-end/image-classification)
* [Motion recognition with anomaly detection (only for boards with built-in IMU sensor)](/tutorials/end-to-end/motion-recognition)
* [Object detection with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids)

## Deploying an example application

The Arduino App Lab launches automatically when the UNO Q starts. If you don’t see it, go to Applications (top left corner), navigate to Accessories, and click on Arduino App Lab.

### Keyword spotting

First we are going to deploy the `Hey Arduino` application in the App Lab examples onto the Arduino UNO Q.

<Frame caption="Hey Arduino keyword spotting application from Arduino App Lab version 0.1.23">
  <img src="https://mintcdn.com/edgeimpulse/7Xfyy0HVFXNw8ySY/.assets/images/arduino-app-lab/arduino-app-lab-hey-arduino-edge-impulse.png?fit=max&auto=format&n=7Xfyy0HVFXNw8ySY&q=85&s=386ab03e26ad73926116187062383dc6" width="1600" height="900" data-path=".assets/images/arduino-app-lab/arduino-app-lab-hey-arduino-edge-impulse.png" />
</Frame>

The `Hey Arduino` application is a keyword spotting application designed to trigger an LED matrix animation (a heart shape animation) when the phrase “Hey Arduino” is detected by the microphone.

This application is interesting as it takes advantage of both the CPU and the MCU available on the Arduino UNO Q. The CPU handles the keyword spotting, and the onboard microcontroller runs the Sketch to visualize the LED matrix animations once the keyword has been recognized.

<Frame caption="Hey Arduino app.yaml file from Arduino App Lab version 0.1.23">
  <img src="https://mintcdn.com/edgeimpulse/7Xfyy0HVFXNw8ySY/.assets/images/arduino-app-lab/arduino-app-lab-hey-arduino-app-yaml-edge-impulse.png?fit=max&auto=format&n=7Xfyy0HVFXNw8ySY&q=85&s=afbc5363800049e07145903a48dca7e8" width="1600" height="898" data-path=".assets/images/arduino-app-lab/arduino-app-lab-hey-arduino-app-yaml-edge-impulse.png" />
</Frame>

The application uses the `keyword_spotting` brick. A brick is like a code package that provides a specific functionality that is needed to the application. In this case, it adds the ability to detect sound patterns through a USB microphone and trigger an event when a match occurs.

The `keyword_spotting` brick uses a pre-trained Edge Impulse audio classification model that identifies `Hey Arduino`. It continuously monitors the audio and when it detects the keyword it triggers the microcontroller using the Bridge tool to activate the LED animation.

To deploy the application on your Arduino UNO Q click the green button in the top right corner. The App Launch starts deploying the application locally.

<Frame caption="Hey Arduino application deploying to the Arduino UNO Q from the Arduino App Lab">
  <img src="https://mintcdn.com/edgeimpulse/7Xfyy0HVFXNw8ySY/.assets/images/arduino-app-lab/arduino-app-lab-deploy-hey-arduino-edge-impulse.png?fit=max&auto=format&n=7Xfyy0HVFXNw8ySY&q=85&s=4fa018b5964f48c94f35eb92d61c7f1d" width="1600" height="900" data-path=".assets/images/arduino-app-lab/arduino-app-lab-deploy-hey-arduino-edge-impulse.png" />
</Frame>

Once the application is running on the UNO Q, say “Hey Arduino”. The LED animation should appear as soon as the keyword is detected.

<Frame caption="Hey Arduino matrix animation on the Arduino UNO Q">
  <img src="https://mintcdn.com/edgeimpulse/gGy2gpReLwlxzvnv/.assets/images/arduino-app-lab/arduino-uno-q-matrix-hey-arduino-edge-impulse.png?fit=max&auto=format&n=gGy2gpReLwlxzvnv&q=85&s=b363f65e9dd835822c1fee9019c47096" width="1600" height="896" data-path=".assets/images/arduino-app-lab/arduino-uno-q-matrix-hey-arduino-edge-impulse.png" />
</Frame>

### Object detection

If you have connected a USB webcam to your Arduino UNO Q, you can test the application `Detect objects on Camera`.

This application uses two bricks, the `video_object_detection` and the `WebUI - HTML` which hosts a web application and exposes APIs or Websockets to be used in the application.

<Frame caption="Detect Object on Camera application from Arduino App Lab version 0.1.23">
  <img src="https://mintcdn.com/edgeimpulse/7Xfyy0HVFXNw8ySY/.assets/images/arduino-app-lab/aduino-app-lab-detect-object-on-camera-edge-impulse.png?fit=max&auto=format&n=7Xfyy0HVFXNw8ySY&q=85&s=a95858bbacb1eb541d74b1d3ab4b0515" width="1600" height="900" data-path=".assets/images/arduino-app-lab/aduino-app-lab-detect-object-on-camera-edge-impulse.png" />
</Frame>

When you deploy this application on your Arduino UNO Q, a pre-trained Edge Impulse model uses the `video_object_detection` brick to find objects on a live video feed from the camera.

To access the UI of the application, use the browser and go to the local IP address of your Arduino UNO Q using the port `7000`.

<Frame caption="Testing the Video Generic Object Detection application after deploying the Detect Object on Camera application from Arduino App Lab into the Arduino UNO Q">
  <img src="https://mintcdn.com/edgeimpulse/gGy2gpReLwlxzvnv/.assets/images/arduino-app-lab/arduino-app-lab-video-object-generic-detection-edge-impulse.png?fit=max&auto=format&n=gGy2gpReLwlxzvnv&q=85&s=e3c54e8e16701a627d119f3609eb0ea4" width="1538" height="1000" data-path=".assets/images/arduino-app-lab/arduino-app-lab-video-object-generic-detection-edge-impulse.png" />
</Frame>

## Deploying a custom application

Now that you have tested the Arduino App Lab on your Arduino UNO Q, it’s time to create your own application using an impulse trained in your Edge Impulse account.

We are going to replicate the `Detect Objects on Camera` application and we will use a custom model, instead of the pre-trained model that comes with the brick. For this tutorial, we will use a face detection model.

### Creating a new app

Click on “My Apps” in the left menu of the Arduino App Lab and then click on the top right hand corner button called `Create new app +`.

<Frame caption="My Apps section in Arduino App Lab version 0.1.23">
  <img src="https://mintcdn.com/edgeimpulse/7Xfyy0HVFXNw8ySY/.assets/images/arduino-app-lab/arduino-app-lab-myapps.png?fit=max&auto=format&n=7Xfyy0HVFXNw8ySY&q=85&s=503bd65a97066dd90d65247556fa2ffd" width="1600" height="900" data-path=".assets/images/arduino-app-lab/arduino-app-lab-myapps.png" />
</Frame>

Give the application a name, and change the emoji if you’d like.

Inside the application, click on the left menu to add the bricks mentioned earlier (`video_object_detection` and `web_ui`).

<Frame caption="New application created with bricks in Arduino App Lab version 0.1.23">
  <img src="https://mintcdn.com/edgeimpulse/7Xfyy0HVFXNw8ySY/.assets/images/arduino-app-lab/arduino-app-lab-myapp-face-detection-bricks-edge-impulse.png?fit=max&auto=format&n=7Xfyy0HVFXNw8ySY&q=85&s=a8dec6827392952dfdb79d70d75cf73b" width="1600" height="900" data-path=".assets/images/arduino-app-lab/arduino-app-lab-myapp-face-detection-bricks-edge-impulse.png" />
</Frame>

After you create the application, we will perform the rest of the steps over SSH, as some of the source code is not yet available in the App Lab GUI as of version `0.1.23`.

### Copying the impulse

Next, you will need the `.eim` file generated by Edge Impulse Studio for `Linux aarch64`. You can either download the Edge Impulse model using the [Edge Impulse Linux CLI](/tools/clis/edge-impulse-linux-cli) tools.

You can manually copy the `.eim` file to the following folder of the Arduino UNO Q or use VS Code (see below):

```
/home/arduino/.arduino-bricks/ei-models/
```

Placing your model here ensures the `video_object_detection` brick will use it for inference, instead of the default pre-trained model.

#### Using VS Code

To copy the file from your local computer to the Arduino UNO Q using the VS Code, follow these instructions:

* Connect to your Arduino UNO Q via SSH using the `Remote SSH` extension
* Open the target folder
* Drag and drop the `.eim` file from your local computer into that folder

<Frame caption="VS Code access to the Arduino UNO Q to develop the new application">
  <img src="https://mintcdn.com/edgeimpulse/gGy2gpReLwlxzvnv/.assets/images/arduino-app-lab/vs-code-arduino-uno-q-access.png?fit=max&auto=format&n=gGy2gpReLwlxzvnv&q=85&s=615b0e6826a3e5b600d298fe07099dc2" width="1600" height="919" data-path=".assets/images/arduino-app-lab/vs-code-arduino-uno-q-access.png" />
</Frame>

### Building the application

Go to your application in the folder:

```
/home/arduino/ArduinoApps/<name of your application>
```

Edit the `app.yaml` file from SSH using this new variable for the `video_object_detection` brick.

```
name: Faces Detector
description: "Faces Detector by Edge Impulse"
ports: []
bricks:
- arduino:video_object_detection: {
    variables: {
      EI_OBJ_DETECTION_MODEL: /home/arduino/.arduino-bricks/ei-models/<name of your model>.eim
    }
  }
- arduino:web_ui: {}

icon: 😀
```

In this case, you need to edit the `EI_OBJ_DETECTION_MODEL` variable. You can update models for other bricks or use cases using these variables:

```
EI_AUDIO_CLASSIFICATION_MODEL
EI_CLASSIFICATION_MODEL
EI_KEYWORD_SPOTTING_MODEL
EI_MOTION_DETECTION_MODEL
EI_OBJ_DETECTION_MODEL
EI_V_ANOMALY_DETECTION_MODEL
```

#### Copying additional assets

After you have saved your changes, follow the instructions below to copy the assets and webUI files from the example to your application and copy the main Python script.

```
cd ~/.local/share/arduino-app-cli/examples/video-generic-object-detection

cp -r assets/* /home/arduino/ArduinoApps/<name of your application>

cp python/main.py /home/arduino/ArduinoApps/<name of your application>/python/
```

The application is now functionally identical to the `Detect objects on Camera` example that we used before, except it uses your own custom model trained with Edge Impulse Studio.

### Running the application

To run the application, type:

```
cd /home/arduino/ArduinoApps/<name of your application>

python3 main.py
```

Deploy the application and open a browser and access the local IP address (or localhost in the Arduino UNO Q) with port 7000 to see the application. Now you will see the custom model detecting faces instead of generic objects.

<Frame caption="New application deployed in the Arduino UNO Q via Arduino App Lab with an Edge Impulse custom model">
  <img src="https://mintcdn.com/edgeimpulse/7Xfyy0HVFXNw8ySY/.assets/images/arduino-app-lab/arduino-app-lab-video-object-generic-detection-custom-model-edge-impulse.png?fit=max&auto=format&n=7Xfyy0HVFXNw8ySY&q=85&s=b04b7cca64821d1337a7fb8135252189" width="1538" height="1000" data-path=".assets/images/arduino-app-lab/arduino-app-lab-video-object-generic-detection-custom-model-edge-impulse.png" />
</Frame>

Feel free to create your own Arduino App Lab application and share your feedback with us in the [Edge Impulse forum](https://forum.edgeimpulse.com).


Built with [Mintlify](https://mintlify.com).