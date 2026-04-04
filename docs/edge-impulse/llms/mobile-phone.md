# Source: https://docs.edgeimpulse.com/hardware/devices/mobile-phone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mobile phone

You can use any smartphone with a modern browser as a fully-supported client for Edge Impulse. You'll be able to sample raw data (from the accelerometer, microphone and camera), build models, and deploy machine learning models directly from the studio. Your phone will behave like any other device, and data and models that you create using your mobile phone can also be deployed to embedded devices.

The mobile client is open source and hosted on GitHub: [edgeimpulse/mobile-client](https://github.com/edgeimpulse/mobile-client). As there are thousands of different phones and operating system versions we'd love to hear from you there if something is amiss.

There's also a video version of this tutorial:

<iframe src="https://www.youtube.com/embed/W_9-bL4br98" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

### Connecting to Edge Impulse

To connect your mobile phone to Edge Impulse, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and head to the **Devices** page. Then click **Connect a new device**.

<Frame caption="Devices page in the studio">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/c66efb1-screenshot_2020-04-03_at_100242.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=7014ec9f8de06c0751355652195f976b" width="1039" height="378" data-path=".assets/images/c66efb1-screenshot_2020-04-03_at_100242.png" />
</Frame>

Select **Mobile phone**, and a QR code will appear. Either scan the QR code with the camera of your phone - many phones will automatically recognize the code and offer to open a browser window - or click on the link above the QR code to open the mobile client.

<Frame caption="Scanning a QR code to connect your phone to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/dce4765-screenshot_2020-04-03_at_100310.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=10b83ac8285381ec205b567da0162729" width="1178" height="596" data-path=".assets/images/dce4765-screenshot_2020-04-03_at_100310.png" />
</Frame>

This opens the mobile client, and registers the device directly. On your phone you see a *Connected* message.

<Frame caption="Connected message in the mobile client">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/7c155ac-f32rfdfw.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=6e9d0f430c1610a53fce45b9d98637e7" width="414" height="747" data-path=".assets/images/7c155ac-f32rfdfw.png" />
</Frame>

That's all! Your device is now connected to Edge Impulse. If you return to the **Devices** page in the studio, your phone now shows as connected. You can change the name of your device by clicking on `⋮`.

<Frame caption="Devices page showing a mobile phone as a connected device">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/abc9ebe-screenshot_2020-04-03_at_100939.png?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=ab97879d9411fe809388085625cc8d60" width="1169" height="358" data-path=".assets/images/abc9ebe-screenshot_2020-04-03_at_100939.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Building a continuous motion recognition system](/tutorials/end-to-end/motion-recognition).
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Sound recognition](/tutorials/end-to-end/sound-recognition)
* [Image classification](/tutorials/end-to-end/image-classification/)
* [object detection](/tutorials/end-to-end/object-detection-bounding-boxes).
* [Object detection with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids)

Your phone will show up like any other device in Edge Impulse, and will automatically ask permission to use sensors.

<Frame caption="Sampling data from the accelerometer on a phone">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/8d1cdd8-hahdfwqe.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=23c004549f55b4699fa4f5c5f163bd36" width="414" height="678" data-path=".assets/images/8d1cdd8-hahdfwqe.png" />
</Frame>

#### No data (using Chrome on Android)?

You might need to enable motion sensors in the Chrome settings via **Settings > Site settings > Motion sensors**.

### Deploying back to device

With the impulse designed, trained and verified you can deploy this model back to your phone. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption. Edge Impulse can package up the complete impulse - including the signal processing code, neural network weights, and classification code - up in a single WebAssembly package that you can straight from the browser.

To do so, just click **Switch to classification mode** at the bottom of the mobile client. This will first build the impulse, and then samples data from the sensor, run the signal processing code, and then classify the data:

<Frame caption="Running the mobile classifier on a keyword spotting model">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/f0d23e6-classifier_mobile.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=0232386124c1339cc7048f8fdcbc7e70" width="414" height="681" data-path=".assets/images/f0d23e6-classifier_mobile.png" />
</Frame>

Victory! You're now running your machine learning model locally in your browser - you can even turn on airplane mode and the model will continue running. You can also [download the WebAssembly](/hardware/deployments/run-webassembly-node) package to include in your own website or Node.js application. 🚀


Built with [Mintlify](https://mintlify.com).