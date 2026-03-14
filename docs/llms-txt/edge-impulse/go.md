# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/inference/linux/go.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Linux Go SDK

This library lets you run machine learning models and collect sensor data on [Linux](/tools/libraries/sdks/inference/linux) machines using Go. The SDK is open source and hosted on GitHub: [edgeimpulse/linux-sdk-go](https://github.com/edgeimpulse/linux-sdk-go).

See our [Linux EIM executable guide](/hardware/deployments/run-linux-eim) to learn more about the .eim file format.

### Installation guide

1. Install [Go 1.15](https://go.dev/) or higher.
2. Clone this repository:

   ```
   $ git clone https://github.com/edgeimpulse/linux-sdk-go
   ```
3. Find the example that you want to build and run `go build`:

   ```
   $ cd cmd/eimclassify
   $ go build
   ```
4. Run the example:

   ```
   $ ./eimclassify
   ```

   And follow instructions.
5. This SDK is also published to pkg.go.dev, so you can pull the package from there too.

### Collecting data

Before you can classify data you'll first need to collect it. If you want to collect data from the camera or microphone on your system you can use the Edge Impulse CLI, and if you want to collect data from different sensors (like accelerometers or proprietary control systems) you can do so in a few lines of code.

#### Collecting data from the camera or microphone

To collect data from the camera or microphone, follow the [getting started guide](/tools/libraries/sdks/inference/linux) for your development board.

#### Collecting data from other sensors

To collect data from other sensors you'll need to write some code to collect the data from an external sensor, wrap it in the Edge Impulse Data Acquisition format, and upload the data to the Ingestion service. [Here's an end-to-end example](https://github.com/edgeimpulse/linux-sdk-go/blob/master/cmd/eimcollect/main.go).

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

* [Audio](https://github.com/edgeimpulse/linux-sdk-go/blob/master/cmd/eimaudio/main.go) - grabs data from the microphone and classifies it in realtime.
* [Camera](https://github.com/edgeimpulse/linux-sdk-go/blob/master/cmd/eimimage/main.go) - grabs data from a webcam and classifies it in realtime.
* [Custom data](https://github.com/edgeimpulse/linux-sdk-go/blob/master/cmd/eimclassify/main.go) - classifies custom sensor data.


Built with [Mintlify](https://mintlify.com).