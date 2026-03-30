# Source: https://docs.edgeimpulse.com/hardware/boards/quectel-pi-sg565d.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quectel PI-SG565D

PI-SG565D is an intelligent ecological single-board computer developed by Quectel based on the high-performance 8-core 64-bit processor from Qualcomm QCS6490 (with computing power of up to 12.15 TOPS) and the Qualcomm Adreno™ 643L GPU. It has 8 GB LPDDR4X memory, adopts USB Type-C power supply interface, and can be externally connected to eMMC and SSD. It also supports Wi-Fi 2.4 & 5 G, IEEE 802.11a/b/g/n/ac and Bluetooth 5.0, as well as dual displays (DP and LCM or DP and Micro HDMI). With strong performance and rich multimedia functions, it can meet your requirements for high data rate, multimedia functions and computing power in industrial and consumer applications.

PI-SG565D integrates abundant interfaces, which significantly expands its application in M2M field. It can also be widely used in industries and devices such as edge computing, robotics, industrial control, multimedia terminals, digital billboards, intelligent security systems and industrial-grade PDA, covering various sectors across the entire AIoT field.

PI-SG565D supports Yocto Linux/Debian operating systems, which can meet the requirements of algorithm prototype verification and inference application development.

<Frame caption="Quectel PI-SG565D Single-Board Computer">
  <img src="https://mintcdn.com/edgeimpulse/mdzJEltVozs6zHeq/.assets/images/quectel/QuecPI-X6X-EVB-1-1.png?fit=max&auto=format&n=mdzJEltVozs6zHeq&q=85&s=42291f9f36758002fe599940671a4076" width="1252" height="783" data-path=".assets/images/quectel/QuecPI-X6X-EVB-1-1.png" />
</Frame>

## Getting Started with your Quectel PI-SG565D on Edge Impulse

### 1. Following the Quick Start Guide for the Quectel PI-SG565D

Please follow the [Quick Start Guide](https://developer.quectel.com/doc/quecpi/PI-SG565D/en/product/PI-SG565D.html) provided by Quectel to set up your PI-SG565D board. You will also need a USB webcam to work with images on Edge Impulse.

### 2. Installing the Edge Impulse Linux CLI

On the device install the Edge Impulse CLI and other dependencies via:

```bash  theme={"system"}
$ wget https://cdn.edgeimpulse.com/firmware/linux/setup-edge-impulse-qc-linux.sh
$ sh setup-edge-impulse-qc-linux.sh
```

### 3. Connecting to Edge Impulse

With all dependencies set up, run:

```bash  theme={"system"}
$ edge-impulse-linux
```

This will start a wizard which asks you to log in and choose an Edge Impulse project. If you want to switch projects, or use a different camera (e.g. a USB camera) run the command with the `--clean` argument.

### 4. Verifying that your device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="RB3 Connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/rb3-connected.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=ebe0c0aa62b5d280a4470d624eeaecbb" width="1600" height="223" data-path=".assets/images/qualcomm/rb3-connected.png" />
</Frame>

## Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Responding to your voice](/tutorials/end-to-end/keyword-spotting)
* [Recognize sounds from audio](/tutorials/end-to-end/sound-recognition)
* [Adding sight to your sensors](/tutorials/end-to-end/image-classification)
* [Object detection](/tutorials/end-to-end/object-detection-bounding-boxes)
* [Visual anomaly detection with FOMO-AD](/studio/projects/learning-blocks/blocks/visual-anomaly-detection-fomo-ad)

Looking to connect different sensors? Our [Linux SDK](/tools/libraries/sdks/inference/linux) lets you easily send data from any sensor and any programming language (with examples in Node.js, Python, Go and C++) into Edge Impulse.

## Profiling your models

To profile your models for the Qualcomm QCS6490 processor that is one the PI-SG565D board, follow these steps:

* Make sure to select the Qualcomm Dragonwing RB3 Gen 2 Development Kit as your target device. You can change the target at the top of the page near your user's logo. This kit has the same processor as the PI-SG565D board.
* Head to your [Learning block](/studio/projects/learning-blocks) page in Edge Impulse Studio.
* Click on the **Calculate performance** button.

To provide the on-device performance, we use [Qualcomm AI Hub](https://aihub.qualcomm.com/) in the background (see the image below) which run the compiled model on a physical device to gather metrics such as the mapping of model layers to compute units, inference latency, and peak memory usage. See more on Qualcomm® AI Hub [documentation](https://app.aihub.qualcomm.com/docs/) page.

<Frame caption="Qualcomm profiling using Qualcomm AI Hub">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/qc-profiling-qc-ai-hub.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=78a743f1dba051b9e476cd2c244ef54e" width="1510" height="1000" data-path=".assets/images/qualcomm/qc-profiling-qc-ai-hub.png" />
</Frame>

## Deploying back to device

### Using the Edge Impulse Linux CLI

To run your impulse locally on the RB3, open a terminal and run:

```bash  theme={"system"}
$ edge-impulse-linux-runner
```

This will automatically compile your model with full hardware acceleration, download the model to your RB3 Gen 2, and then start classifying (use `--clean` to switch projects).

Alternatively, you can select the **Linux (AARCH64 with Qualcomm QNN)** option in the **Deployment** page.

<Frame caption="Qualcomm deployment options">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/studio-qc-deployment-options-3.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=3975b7e607c98d35b8d08f5d677c72bc" width="1266" height="748" data-path=".assets/images/qualcomm/studio-qc-deployment-options-3.png" />
</Frame>

This will download an `.eim` model that you can run on your board with the following command:

```bash  theme={"system"}
edge-impulse-linux-runner --model-file downloaded-model.eim
```

### Using the Edge Impulse Linux Inferencing SDKs

Our [Linux SDK](/tools/libraries/sdks/inference/linux) has examples on how to integrate the `.eim` model with your favourite programming language.

<Info>
  You can download either the quantized version and the float32 versions but Qualcomm NN accelerator only supports quantized models. If you select the float32 version, the model will run on CPU.
</Info>

### Using the IM SDK GStreamer option

When selecting this option, you will obtain a `.zip` folder. We provide instructions in the `README.md` file included in the compressed folder.

See more information on [Qualcomm IM SDK GStreamer pipeline](/hardware/deployments/run-qualcomm-im-sdk-gstreamer).

### Image model?

If you have an image model then you can get a peek of what your device sees by being on the same network as your device, and finding the 'Want to see a feed of the camera and live classification in your browser' message in the console. Open the URL in a browser and both the camera feed and the classification are shown:

<Frame caption="Live feed with classification results">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/demo1.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=f5d180c10366b2d54c7aec5f6c2187cc" width="400" height="440" data-path=".assets/images/demo1.png" />
</Frame>

## Troubleshooting

<Accordion title="Capture process failed with code 255">
  ###

  If you start the CLI, and see:

  ```
  Failed to initialize linux tool Capture process failed with code 255
  ```

  You'll need to restart the camera server via:

  ```bash  theme={"system"}
  $ systemctl restart cam-server
  ```
</Accordion>


Built with [Mintlify](https://mintlify.com).