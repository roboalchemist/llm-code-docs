# Source: https://docs.edgeimpulse.com/hardware/boards/arducam-pico4ml-tinyml-dev-kit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Arducam Pico4ML TinyML Dev Kit

<Info>
  **Community board**

  This is a community board by Arducam, and it's not maintained by Edge Impulse. For support head to the [Arducam support page](https://www.arducam.com/contact-arducam/).
</Info>

The Arducam Pico4ML TinyML Dev Kit is a development board from Arducam with a RP2040 microcontroller, QVGA camera, bluetooth module (depending on your version), LCD screen, onboard microphone, accelerometer, gyroscope, and compass. Arducam has created in depth tutorials on how to get started using the Pico4ML Dev Kit with Edge Impulse, including how to collect new data and how to train and deploy your Edge Impulse models to the Pico4ML. The Arducam Pico4ML TinyML Dev Kit has two versions, [the version with BLE](https://www.arducam.com/product/arducam-pico4ml-tinyml-dev-kit-rp2040-board-w-qvga-camera-lcd-screen-onboard-audio-b0330/) and [the version without BLE](https://www.arducam.com/product/rp2040-based-arducam-pico4ml-dev-board-for-machine-vision/).

<Frame caption="Arducam Pico4ML TinyML Dev Kit: RP2040 Board w/ QVGA Camera, Bluetooth module (with or without), LCD Screen, Onboard Audio, & IMU">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/1644fc2-arducam-pico4ml-tinyml-dev-kit-b0330-2.jpeg?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=0950de49e5dc0a8511456a6604ef717f" width="1000" height="1000" data-path=".assets/images/1644fc2-arducam-pico4ml-tinyml-dev-kit-b0330-2.jpeg" />
</Frame>

### Connecting to Edge Impulse

To set up your Arducam Pico4ML TinyML Dev Kit, follow this guide: [Arducam: How to use Edge Impulse to train machine learning models for Raspberry Pico](https://www.arducam.com/docs/pico/arducam-pico4mltinymldevkit/how-to-use-edge-impulse-to-train-machine-learning-models-for-raspberry-pico/).

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with the [Edge Impulse continuous motion recognition tutorial](/tutorials/end-to-end/motion-recognition).

Or you can follow Arducam's tutorial on [How to build a Magic Wand with Edge Impulse for Arducam Pico4ML-BLE](https://www.arducam.com/docs/pico/arducam-pico4mltinymldevkit/how-to-build-a-magic-wand-with-edge-impulse-on-arducam-pico4ml-ble/).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

### Deploying back to device

With the impulse designed, trained and verified you can deploy this model back to your Arducam Pico4ML TinyML Dev Kit. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption. Edge Impulse can package the complete impulse - including the signal processing code, neural network weights, and classification code - up into a single library that you can run on your development board. See the end of the Arducam's [How to use Edge Impulse to train machine learning models for Raspberry Pico](https://docs.arducam.com/Arduino-SPI-camera/Legacy-SPI-camera/Pico/Arducam-Pico4ML-TinyML/train-machine-learning-models/#deploy-model) tutorial for more information on deploying your model onto the device.


Built with [Mintlify](https://mintlify.com).