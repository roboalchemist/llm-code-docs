# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/inference/linux/node-js.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Linux Node.js SDK

This library lets you run machine learning models and collect sensor data on [Linux](/tools/libraries/sdks/inference/linux) machines using Node.js. The SDK is open source and hosted on GitHub: [edgeimpulse/edge-impulse-linux-cli](https://github.com/edgeimpulse/edge-impulse-linux-cli).

See our [Linux EIM executable guide](/hardware/deployments/run-linux-eim) to learn more about the .eim file format.

### Installation guide

Add the library to your application via:

```
$ npm install edge-impulse-linux
```

### Collecting data

Before you can classify data you'll first need to collect it. If you want to collect data from the camera or microphone on your system you can use the Edge Impulse CLI, and if you want to collect data from different sensors (like accelerometers or proprietary control systems) you can do so in a few lines of code.

#### Collecting data from the camera or microphone

To collect data from the camera or microphone, follow the [getting started guide](/tools/libraries/sdks/inference/linux) for your development board.

#### Collecting data from other sensors

To collect data from other sensors you'll need to write some code where you instantiate a `DataForwarder` object, write data samples, and finally call `finalize()` which uploads the data to Edge Impulse. [Here's an end-to-end example](https://github.com/edgeimpulse/edge-impulse-linux-cli/blob/master/examples/js/collect-custom.js).

### Classifying data

To classify data (whether this is from the camera, the microphone, or a custom sensor) you'll need a model file. This model file contains all signal processing code, classical ML algorithms and neural networks - and typically contains hardware optimizations to run as fast as possible. To grab a model file:

1. Train your model in Edge Impulse.
2. [Install the Edge Impulse for Linux CLI](/tools/clis/edge-impulse-linux-cli).
3. Download the model file via:

   ```
   $ edge-impulse-linux-runner --download modelfile.eim
   ```

   This downloads the file into `modelfile.eim`. (Want to switch projects? Add `--clean`)

Then you can start classifying realtime sensor data. We have examples for:

* [Audio](https://github.com/edgeimpulse/edge-impulse-linux-cli/blob/master/examples/js/classify-audio.js) - grabs data from the microphone and classifies it in realtime.
* [Camera](https://github.com/edgeimpulse/edge-impulse-linux-cli/blob/master/examples/js/classify-camera.js) - grabs data from a webcam and classifies it in realtime.
* [Custom data](https://github.com/edgeimpulse/edge-impulse-linux-cli/blob/master/examples/js/classify-custom.js) - classifies custom sensor data.


Built with [Mintlify](https://mintlify.com).