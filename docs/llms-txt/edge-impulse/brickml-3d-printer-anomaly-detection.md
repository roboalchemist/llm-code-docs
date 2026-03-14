# Source: https://docs.edgeimpulse.com/projects/expert-network/brickml-3d-printer-anomaly-detection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# BrickML Demo Project - 3D Printer Anomaly Detection

Created By: Attila Tokes

Public Project Link: [https://studio.edgeimpulse.com/public/283049/latest](https://studio.edgeimpulse.com/public/283049/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/brick-ml-3d-print.jpg?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=6e4e64fa89a60c5d461e01e8686f957b" width="1600" height="970" data-path=".assets/images/brickml-3d-printer-anomaly-detection/brick-ml-3d-print.jpg" />
</Frame>

## Introduction

[**BrickML**](https://edgeimpulse.com/reference-designs/brickml) is a plug-and-play device from **Edge Impulse** and [**reloc**](http://www.reloc.it/), meant to be a reference design for Edge ML industrial applications. It is designed to monitor machine health, by collecting and analyzing sensor data locally using ML models built with Edge Impulse.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/02-brick-ml-overview.jpg?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=fb69a001e6870a79e11b2ad01127d04b" width="1004" height="747" data-path=".assets/images/brickml-3d-printer-anomaly-detection/02-brick-ml-overview.jpg" />
</Frame>

In terms of specifications BrickML comes with a powerful Cortex-M33 micro-processor, 512KB RAM and various storage options for code and data. It has CAN, LTE, UART, I2C and SPI interfaces, and supports wired and wireless connectivity over USB, Ethernet and Bluetooth 5.1. A wide selection of onboard sensors can readily be used in projects. We get a 9-axis inertial sensor (Bosch BNO055), a humidity and temperature sensor (Renesas HS3001), a digital microphone (Knowles SPH0641LU4H-1) and ADC inputs for current sensing.

BrickML comes with seamless integration with [Edge Impulse Studio](https://studio.edgeimpulse.com/). The device can be used both for data collection, experimentation and running live ML models.

## Getting Started with the BrickML

BrickML is designed to be ready to use out-of-the-box. All we need is connect the device to a Laptop / PC using the provided USB Type-C cable.

On the Laptop / PC we can use the [Edge Impulse CLI](/tools/clis/edge-impulse-cli) tool set to interact with the BrickML device. To install it follow the [Installation](/tools/clis/edge-impulse-cli/installation) guide from the documentation.

Once the Edge Impulse CLI is installed, we connect to the BrickML by plugging it to an USB port, and running the `edge-impulse-daemon` command:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/04-brick-ml-edge-impulse-cli.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=cddb8cf36b6f35fc3cb70ba0250d3d46" width="1102" height="608" data-path=".assets/images/brickml-3d-printer-anomaly-detection/04-brick-ml-edge-impulse-cli.png" />
</Frame>

If we are not already logged in, `edge-impulse-daemon` will ask our Edge Impulse Studio email and password. After this the BrickML should be automatically detected, and we will be asked to choose a Studio project we want to use.

Once connected, the BrickML will show up in the Devices section of our Edge Impulse Studio project, and it should be ready to be used for data collection and model training.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/05-brick-ml-studio-device.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=871027cee59ddefb6256a4b48920165b" width="977" height="417" data-path=".assets/images/brickml-3d-printer-anomaly-detection/05-brick-ml-studio-device.png" />
</Frame>

## 3D Printing Anomaly Detection

For the purpose of this tutorial, I choose to mount the BrickML on a 3D printer. The idea is use the BrickML for anomaly detection. For this, first we will teach the device how the 3D printer normally operates, after which we will build an anomaly detection model that can detect irregularities in the functioning of the 3D printer.

Installing the BrickML to the 3D printer was fairly easy. The BrickML comes in a case with four mounting holes that can be used to mount the device on various equipment. In the case of the 3D printer, I mounted the BrickML to the frame using some M4 bolts and T-nuts.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/21-brick-ml-mount.jpg?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=721c551e39025ffc26da81920045794e" width="569" height="597" data-path=".assets/images/brickml-3d-printer-anomaly-detection/21-brick-ml-mount.jpg" />
</Frame>

After the BrickML is mounted, we can go ahead an create a project from our [Edge Impulse projects page](https://studio.edgeimpulse.com/studio/profile/projects):

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/22-project-creation.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=8136c2079a0bb02b3d54b12ac46cf703" width="632" height="558" data-path=".assets/images/brickml-3d-printer-anomaly-detection/22-project-creation.png" />
</Frame>

As some of the *(optional)* features we will use require an Enterprise account, I selected the aforementioned project type.

> *Note: the steps I will follow in this guide are generic, so it should be easy to apply them on similar projects.*

## Collecting Data

The first step of an AI / ML project is the data collection. In Edge Impulse Studio we do this from the **Data acquisition** tab.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/06-data-collection.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=a2c585a769077ed4ba7ef79015e7ff07" width="1092" height="615" data-path=".assets/images/brickml-3d-printer-anomaly-detection/06-data-collection.png" />
</Frame>

For this tutorial, I decided to collect Inertial sensor data for 3 labels, in large chunks of about \~5 minutes:

* **printing** - 7 samples, 35 minutes of data
* **idle** - 2 samples, 10 minutes of data
* **off** - 1 sample, 5 minutes of data

In the `printing` class, I used a slightly modified G-code file from a previous 3D print, and re-played on the printer. The `idle` and `off` labels are a baseline to be able to detect when the 3D printer does nothing.

The collected samples were split into smaller chunks, and then arranged into Training and Test sets with close to 80/20 proportion:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/07-train-test.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=5fce9a9f265af10df1174d14f4ef8975" width="820" height="571" data-path=".assets/images/brickml-3d-printer-anomaly-detection/07-train-test.png" />
</Frame>

## Designing an Impulse

Now that we have some data, we can continue with the [**Impulse design**](https://studio.edgeimpulse.com/studio/283049/create-impulse) step. The [Impulse](/studio/projects/impulse-design) represents our machine learning pipeline, which includes data collection, pre-processing and learning stages.

For this tutorial I went with the following blocks:

* [**Time Series Data**](/studio/projects/impulse-design#input-block) input
  * with 3-axis accelerometer and gyroscope sensor data, 100 Hz frequency, 4 sec window size + 1 sec increase
* a [**Spectral Analysis**](/studio/projects/processing-blocks/blocks/spectral-analysis) processing block
  * to extract the frequency, power and other characteristics from the inertial sensor data
* a [**Classification**](/studio/projects/learning-blocks/blocks/classification) learning block
  * that classifies the 3 normal operating states
* an [**Anomaly Detection**](/studio/projects/learning-blocks/blocks/anomaly-detection-gmm) learning block
  * capable of detecting states different from normal operation
* **Output Features** consisting of
  * Confidence scores for the 3 classes
  * Anomaly score that indicates unusual behavior

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/08-impulse.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=74112b25375ff5694d0afb9bbd300632" width="1482" height="938" data-path=".assets/images/brickml-3d-printer-anomaly-detection/08-impulse.png" />
</Frame>

### Spectral Analysis

The [**Spectral Analysis**](/studio/projects/processing-blocks/blocks/spectral-analysis)  processing block is used to extract frequency, power and other characteristics from the sensor data. It is ideal for detecting motion patterns in inertial sensor signals. In this project we are using it to process the accelerometer and gyroscope data.

Setting up Spectral Analysis is fairly easy. In most of the cases we can rely on Edge Impulse Studio to chose the appropriate parameters by clicking the <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/00-autotune.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=e545a2d47e4062d84923fab0a89d4bf5" alt="" width="108" height="22" data-path=".assets/images/brickml-3d-printer-anomaly-detection/00-autotune.png" /> button:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/09-spectral-analysis.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=2378c9c6773e9ea0bfd87719ccf46e02" width="1159" height="1000" data-path=".assets/images/brickml-3d-printer-anomaly-detection/09-spectral-analysis.png" />
</Frame>

After saving the parameters, we can head over the Generate features tab and launch spectral feature generation by hitting the *"Generate features"* button. When the feature generation job completes, a visual representation of the generated features is shown in the Feature explorer section:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/10-spectral-analysis-features.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=2d54d4a8ad26d8b6982b394e8fe5a633" width="1600" height="919" data-path=".assets/images/brickml-3d-printer-anomaly-detection/10-spectral-analysis-features.png" />
</Frame>

As we can see the features for the `printing`, and `idle` / `off` classes are well separated.

### Classification

After the feature generation the next step is to generate a Classifier. Here we will train a Neural Network using the default settings, which consists of an Input layer, two Dense layers, and an Output layer:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/11-classifier-settings.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=7e7cbe52ed90b70dd0aeaff58d540525" width="867" height="788" data-path=".assets/images/brickml-3d-printer-anomaly-detection/11-classifier-settings.png" />
</Frame>

The training can be started by using the **"Start training"** button. After a couple of minutes we are presented with the results:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/12-classifier-result.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=369f582d650c46e43938125e70a7bd0b" width="856" height="1000" data-path=".assets/images/brickml-3d-printer-anomaly-detection/12-classifier-result.png" />
</Frame>

As we can see we obtained an accuracy of 99.8% with `printing`, `idle` and `off` states well separated. We have a small number of `idle` and `off` samples overlapping, but this is expected as the two categories are quite similar.

### Anomaly Detection

Anomaly detection can be used detect irregular patterns in the collected sensor data. In Edge Impulse we can implement anomaly detection using one of the two available anomaly detection blocks. For this project, I decided to go with the [**Anomaly Detection (GMM)**](/studio/projects/learning-blocks/blocks/anomaly-detection-gmm) learning block.

In terms of parameters, we need to select a couple of spectral features we want to use for the anomaly detections. After a couple of tries, I went with 10 components with the RMS and Skewness values from the Accelerometer and Gyroscope sensors selected as features.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/13-anomaly-detection-settings.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=2c34e3746871b89d0671d8a428eab2da" width="1091" height="860" data-path=".assets/images/brickml-3d-printer-anomaly-detection/13-anomaly-detection-settings.png" />
</Frame>

*Note: by default, the selection spectral power features for some specific frequency bins. I decided not to use these as it is not guaranteed that real world anomalies will contain these certain frequencies.*

After setting the parameters, the anomaly detection is trained in the usual way, by clicking the *"Start training"* button.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/14-anomaly-detection-output.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=4ab51b73525f2422ed0130d4f681378f" width="1082" height="933" data-path=".assets/images/brickml-3d-printer-anomaly-detection/14-anomaly-detection-output.png" />
</Frame>

In the output we should see that the samples for known classes are in well separated regions. This means the model will be able to easily detect irregularities in the input.

## Testing

Once the training of our model is done, the next step is to test the model. Here, we can evaluate the model against our Test dataset, and we can also test it live on the BrickML device.

To test the model against the Test dataset, we should go to the [**Model testing**](https://studio.edgeimpulse.com/studio/283049/validation) tab, and click the <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/00-button-classify-all.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=eec5c5496f6c1d817d0089e1740cfc02" alt="" width="102" height="30" data-path=".assets/images/brickml-3d-printer-anomaly-detection/00-button-classify-all.png" /> button. After a couple of seconds the classification results are shown:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/15-testing.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=e088e42c3c8f85e921dc44c4b41abefd" width="1451" height="833" data-path=".assets/images/brickml-3d-printer-anomaly-detection/15-testing.png" />
</Frame>

We can see that we got a very good accuracy of 99+%, with a small number of uncertainties between the `idle` and `off` states.

As the model works as expected, we should try [**Live classification**](https://studio.edgeimpulse.com/studio/283049/classification) on newly sampled data from the BrickML device. For this, first we need to connect to the BrickML device, either using `edge-impulse-daemon` or Web USB. After this, we can start collecting some sensor data, by hitting the *"Start sampling"* button with the appropriate parameters:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/16-live-classification.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=a690ac0f04984c1d25396b25c5df8207" width="541" height="414" data-path=".assets/images/brickml-3d-printer-anomaly-detection/16-live-classification.png" />
</Frame>

I tested the model in various conditions. The below screenshot shows the results when running a print:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/17-live-results.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=b4240cdf434419dcad4cf3a91230c05c" width="1430" height="1000" data-path=".assets/images/brickml-3d-printer-anomaly-detection/17-live-results.png" />
</Frame>

During live testing we can also check out the **Anomaly Detection** feature. For this I gave the printer a little shake. The result of this is that the Anomaly score skyrockets, indicating that some irregularity was detected:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/18-live-anomaly.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=f753847c5e195b4532a705045d22f8ff" width="1564" height="1000" data-path=".assets/images/brickml-3d-printer-anomaly-detection/18-live-anomaly.png" />
</Frame>

## Deploying the Model on the BrickML

The final stage of the project is to build and deploy our Impulse to the BrickML device.

To build the image we can go to the [**Deployment**](https://studio.edgeimpulse.com/studio/283049/deployment) tab. There, we need to select the BrickML / Renesas RA6M5 (Cortex-M33 200MHz) as the target, and click the *Build* button:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/19-deployment.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=5ad7e2c300bac5958d2f00a256191ca4" width="941" height="1000" data-path=".assets/images/brickml-3d-printer-anomaly-detection/19-deployment.png" />
</Frame>

Optionally, we can enable the [EON™ Compiler](/studio/projects/deployment/eon-compiler), which is a way to tune the model we build to the target device we selected.

The build will complete in a couple of minutes, and the output will show up the **Build output** section, and it will be ready to download.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/20-deployment-build.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=827e01e08110b1ed3eebc83ac2ed19df" width="715" height="184" data-path=".assets/images/brickml-3d-printer-anomaly-detection/20-deployment-build.png" />
</Frame>

The output is a `.zip` archive containing two files: a signed binary firmware image, and an uploader script.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml-3d-printer-anomaly-detection/23-build-content.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=dc043b7f20bd7b2c54696fd05800eeb5" width="722" height="280" data-path=".assets/images/brickml-3d-printer-anomaly-detection/23-build-content.png" />
</Frame>

The new firmware can be uploaded to the BrickML using the provided `ei_uploader.py` script, by running the following command:

```sh  theme={"system"}
$ python3 ei_uploader.py -s /dev/ttyACM0 -f firmware-brickml.bin.signed
```

After a quick reboot / power cycle we should be able to launch the model using the `edge-impulse-run-impulse` command.

Here is quick video showing the BrickML in action, while running the model:

<iframe src="https://www.youtube.com/embed/XC2BqRqM0xk" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Conclusions

As our example shows, the BrickML is very capable device, that can be used to implement Edge ML solutions with very little development effort.

Using BrickML and Edge Impulse Studio we can easily collect sensor data and train an ML model. The resulting model can be rapidly deployed to the BrickML device, which then runs the inference in real time.

To integrate BrickML into an existing solution, we can use the AT interface it exposes, or we can also chose to the extend its firmware with custom functionality.

## Resources

1. BrickML Product Page,  [https://edgeimpulse.com/reference-designs/brickml](https://edgeimpulse.com/reference-designs/brickml)
2. Edge Impulse Documentation, [https://docs.edgeimpulse.com](https://docs.edgeimpulse.com)


Built with [Mintlify](https://mintlify.com).