# Source: https://docs.edgeimpulse.com/tutorials/integrations/arduino-ml-tools.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Arduino Machine Learning Tools

Arduino and Edge Impulse have partnered to bring machine learning tools to all Arduino Cloud users with a branded and integrated experience.

The video below contains an example of the full workflow to train a keyword spotting and to run the model on the Arduino Nano 33 BLE Sense using Arduino ML Tools solution:

<iframe src="https://www.youtube.com/embed/objrKAEb02k" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

### SSO (Single Sign On)

<Info>
  **Arduino Pro users**

  Arduino Pro users will benefit a 60-min per job limit instead of the default 20-min per job limit.
</Info>

You can log in the ML Tools platform using your Arduino Cloud credentials. To access the Arduino Machine Learning Tools platform, either go to [cloud.arduino.cc](https://cloud.arduino.cc/home/) or [mltools.arduino.cc](https://mltools.arduino.cc).

<Frame caption="Arduino Cloud home page">
  <img src="https://mintcdn.com/edgeimpulse/XwnzH-Jo3nDoEg0b/.assets/images/arduino-cloud-home-2.png?fit=max&auto=format&n=XwnzH-Jo3nDoEg0b&q=85&s=eb0603dbf3b8f7be23467280094de65a" width="1600" height="956" data-path=".assets/images/arduino-cloud-home-2.png" />
</Frame>

<br />

<Frame caption="Arduino ML Tools SSO">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-wl-sso.png?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=ee0a937814972c6140ca9329357b4a68" width="1600" height="956" data-path=".assets/images/arduino-wl-sso.png" />
</Frame>

### Create and build a machine learning project

To create a new project, click on your profile picture in the upper right corner and select **+ Create new project**.

<Frame caption="Arduino ML Tools - first login">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-wl-new-user.png?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=d69b466c48fab2399e9e68506339c106" width="1224" height="1000" data-path=".assets/images/arduino-wl-new-user.png" />
</Frame>

Once you create a project, select the project type you want to build using the helper. You will then arrive on your project's **Dashboard**:

<Frame caption="Arduino ML Tools Dashboard">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-wl-dashboard.png?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=06a77adaa17321874ea0cabba72a341e" width="1600" height="956" data-path=".assets/images/arduino-wl-dashboard.png" />
</Frame>

You can also select which board you are using on the **Project Info** card, in the bottom-right corner.

The following boards are currently supported in Arduino ML Tools:

* [Arduino Nano 33 BLE Sense](/hardware/boards/arduino-nano-33-ble-sense)
* [Arduino Nicla Vision](/hardware/boards/arduino-nicla-vision)
* [Arduino Portenta H7 + Vision Shield](/hardware/boards/arduino-portenta-h7)
* [Arduino Nicla Sense ME](/hardware/boards/arduino-nicla-sense-me)\*

\**(only using the ingestion sketch and arduino library deployment, latency calculations may not be available)*

With everything set up you can now build your first machine learning model with these tutorials:

* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Sound recognition](/tutorials/end-to-end/sound-recognition)
* [Image classification](/tutorials/end-to-end/image-classification/)
* [object detection](/tutorials/end-to-end/object-detection-bounding-boxes).
* [Object detection with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids)

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

### Deployment

Once your project is ready, you can either download an [Arduino library](/hardware/deployments/run-arduino-2-0) or a [ready-to-use firmware](/hardware/deployments/run-ei-fw)

<Frame caption="Arduino ML Tools Deployment">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-wl-deployment.png?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=65c78426a8c2411d35376184d8ef7742" width="1600" height="956" data-path=".assets/images/arduino-wl-deployment.png" />
</Frame>

### Share your project

Once you are happy with the results, please share your project publicly and let everyone knows about it:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/zDLKVpMVk0R3iPVV/.assets/images/arduino-mltools-make-project-public.png?fit=max&auto=format&n=zDLKVpMVk0R3iPVV&q=85&s=ce5847f0af9e702ff1302b9f1d60b814" width="1565" height="1000" data-path=".assets/images/arduino-mltools-make-project-public.png" />
</Frame>

Here is an example of the public project made after from the video at the top of this page: [Arduino KWS public project](https://mltools.arduino.cc/public/142511/latest).

### Use the Edge Impulse CLI

By default, no password is set for your user profile as you have logged using Arduino Cloud SSO. If you want to use [Edge Impulse CLI](/tools/clis/edge-impulse-cli), you need to set a password. To do so, click on **Your profile** from the upper-right corner menu:

<Frame caption="Arduino ML Tools - Set user password">
  <img src="https://mintcdn.com/edgeimpulse/b1HV4QAxkg74kTZp/.assets/images/arduino-wl-set-password.png?fit=max&auto=format&n=b1HV4QAxkg74kTZp&q=85&s=af890965acbb4a1b0b54d2dd1c8e2129" width="1224" height="1000" data-path=".assets/images/arduino-wl-set-password.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).