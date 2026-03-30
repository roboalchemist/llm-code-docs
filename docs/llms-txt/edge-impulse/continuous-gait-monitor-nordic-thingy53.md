# Source: https://docs.edgeimpulse.com/projects/expert-network/continuous-gait-monitor-nordic-thingy53.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Continuous Gait Monitor (Anomaly Detection) - Nordic Thingy:53

Created By: Samuel Alexander

Public Project Link: [https://studio.edgeimpulse.com/public/366723/live](https://studio.edgeimpulse.com/public/366723/live)

<Frame caption="01-cover">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/01-cover.jpg?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=b74b7574e7153dd7d6164606ae09ee5c" width="1280" height="720" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/01-cover.jpg" />
</Frame>

## Introduction

Subtle changes in gait can be early indicators of various medical conditions, including neurodegenerative diseases like Parkinson's, multiple sclerosis, balance disorders, and even other injuries with far-reaching health consequences. Early detection often relies on subtle changes in how a person walks, such as reduced speed, shuffling steps, or unsteadiness. Unfortunately, current assessments primarily rely on periodic, in-clinic observations by healthcare professionals, potentially missing subtle yet significant changes occurring between visits. Moreover, subjective self-assessments of gait are often unreliable. This lack of continuous, objective monitoring hinders timely diagnoses, limits the effectiveness of treatment plans, and makes it difficult to track the progression of gait-related conditions. A proactive, data-driven solution is needed to ensure individuals and their healthcare providers have the information necessary for informed decision-making.

<Frame caption="02-gait">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/02-gait.png?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=d53db431f001d8a9d4a2ea90084d389f" width="1280" height="584" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/02-gait.png" />
</Frame>

Image Credit: Can Tunca, "Human Gait Cycle", 2017, via mdpi.com

## Project Overview

This project aims to develop a wearable device for early gait disorder detection. We'll begin by collecting data representing normal gait patterns during walking, running, and standing.  Next, we'll extract relevant features using Edge Impulse tools, focusing on characteristics like leg swing acceleration, stride length, and foot placement (supination/pronation). Employing Edge Impulse's K-means anomaly detection block and feature importance analysis, the device will learn to distinguish healthy gait patterns (based on the individual's established baseline) from potential anomalies.  Initially, inference results will be displayed on a smartphone app. This proof-of-concept can be expanded into a wearable device that alerts users of gait abnormalities and trends, recommending healthcare consultations when appropriate.  Ultimately, our goal is to provide a proactive tool for early disorder identification, enabling timely intervention and improved outcomes.

<Frame caption="03-project">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/03-project.jpg?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=b4f24f8218e7169efc7afa68a1eb3447" width="1280" height="853" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/03-project.jpg" />
</Frame>

### Why the Nordic Thingy:53? Platform Continuity.

The Nordic Thingy:53 leverages the nRF5340 Arm Cortex-M33 SoC, providing the computational resources necessary for on-device AI inference. It also includes a built-in accelerometer to capture detailed gait data and Bluetooth 5.4 for wireless communication. Importantly, the same nRF5340 chip powers the nRF5340 Development Kit, providing a consistent hardware platform throughout the project's development cycle. This means we can easily prototype on the Thingy:53, refine algorithms and sensor selections on the Development Kit, and ultimately transition to a custom wearable design for mass production – all using the same core chip. This approach ensures a smooth and efficient development process.

<Frame caption="04-thingy">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/04-thingy.jpg?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=c7c10ce0f87f9e8d93b413f0c6fb8f48" width="1000" height="1000" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/04-thingy.jpg" />
</Frame>

## Hardware Requirements

* Nordic Thingy:53
* 3D printer

## Software Requirements

* Edge Impulse CLI
* nRF Programmer App (iPhone/Android)
* nRF Connect Desktop

## Dataset Collection

The Thingy:53 was used for collecting a dataset for training the AI model to establish a baseline of normal, healthy gait patterns. This dataset includes three types of movement: standing, walking, and running. To capture realistic data, the user wore the device while performing these activities. The dataset's variety helps the model accurately classify different gait patterns and detect potential abnormalities in various situations.

<Frame caption="05-dataset-collection">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/05-dataset-collection.gif?s=fc0767baa660ad52165e9e1fd0dccb68" width="800" height="450" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/05-dataset-collection.gif" />
</Frame>

A 3D printed shoe clip-on case modification is made for attaching the Thingy:53 to a shoe. You can download the .stl files here: [https://www.thingiverse.com/thing:6558382](https://www.thingiverse.com/thing:6558382)

<Frame caption="06-cad">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/06-cad.png?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=c956c34cde1eeb6b2bc09223c47379c7" width="1280" height="652" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/06-cad.png" />
</Frame>

<br />

<Frame caption="07-mod">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/07-mod.jpg?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=a1e02ca78d95421fdbc5cb11e58c1fff" width="1280" height="720" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/07-mod.jpg" />
</Frame>

<br />

<Frame caption="08-shoe">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/08-shoe.jpeg?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=ad2afa87ee7a5ca15a6b6fedd6d0f270" width="1000" height="1000" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/08-shoe.jpeg" />
</Frame>

This project assumes basic familiarity with connecting the Thingy:53 to Edge Impulse via the nRF Connect app. If needed, refer to this [guide](/hardware/boards/nordic-semi-thingy53) for assistance.

<Frame caption="09-nrfconnect">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/09-nrfconnect.jpeg?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=03b269ef2a9ca82da459f4781d1aa315" width="1039" height="1000" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/09-nrfconnect.jpeg" />
</Frame>

Collect data for each label **(standing, walking, running)** using the nRF Connect app. Choose:

* Sensor: Accelerometer
* Sample Length (ms): 20000
* Frequency (Hz): 20

For each label, we collected 13 repetitions of 20000 ms which equals to 260 seconds for each label. This seems to be plenty enough for our testing, however more data may be necessary if the gait patterns are performed with a larger variety of terrains.

<Frame caption="10-collect-data">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/10-collect-data.jpeg?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=3601f24de7ae86685061d4f099891af1" width="667" height="1000" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/10-collect-data.jpeg" />
</Frame>

Split the 20000 ms sample into 4 sections of 5000 ms windows.

<Frame caption="11-split-sample">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/11-split-sample.png?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=11b830136ca795e920d0b831c602419d" width="1280" height="741" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/11-split-sample.png" />
</Frame>

<br />

<Frame caption="12-complete-dataset">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/12-complete-dataset.png?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=29d635d4e6d943651f3d3d22438f7731" width="1280" height="571" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/12-complete-dataset.png" />
</Frame>

Perform a train/test split if needed, or try to aim for approximately an 80/20 ratio.

<Frame caption="13-train-test-split">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/13-train-test-split.png?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=9f73a71374dbf62f62873592726f03d0" width="1280" height="274" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/13-train-test-split.png" />
</Frame>

## Impulse Design

After thorough testing, including using the EON Tuner, the optimal settings for our time series data were determined.  We employ both a classifier and K-means anomaly detection to enable both gait pattern classification and anomaly scoring.

<Frame caption="14-create-impulse">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/14-create-impulse.png?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=6e809765cf60e26ca4f8afe7917a4b36" width="1280" height="592" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/14-create-impulse.png" />
</Frame>

### Spectral Features

Spectral analysis transforms raw accelerometer data from the time domain into the frequency domain.  This reveals hidden patterns in gait data, such as stride frequency, step regularity, and harmonic components of movement patterns. These extracted spectral features can provide a richer representation of gait characteristics for the neural network, often leading to improved classification accuracy and a clearer understanding of potential gait abnormalities.

<Frame caption="15-spectral-features">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/15-spectral-features.png?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=9d179c00668e4915adea71d18a6276cd" width="1280" height="893" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/15-spectral-features.png" />
</Frame>

### Classifier

As mentioned, these parameter settings are already using optimized values from the EON Tuner.

<Frame caption="16-tuned-classifier">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/16-tuned-classifier.png?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=02f7c2a0d04c46206478bb08b4cdb9a9" width="1280" height="770" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/16-tuned-classifier.png" />
</Frame>

<br />

<Frame caption="17-tuned-testing">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/17-tuned-testing.png?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=9dcc00616f114ae2512f1a646d3c86ee" width="1280" height="766" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/17-tuned-testing.png" />
</Frame>

These are our results before using the EON Tuner (default parameter values and settings).

<Frame caption="18-initial-results">
  <img src="https://mintcdn.com/edgeimpulse/YFRg7QUJGQP2MxTz/.assets/images/continuous-gait-monitor-nordic-thingy53/18-initial-results.jpg?fit=max&auto=format&n=YFRg7QUJGQP2MxTz&q=85&s=fae3b0dc1961f9bb9cf4e80847641a20" width="1280" height="720" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/18-initial-results.jpg" />
</Frame>

The EON Tuner is a valuable tool for finding the best parameter settings and model architecture to maximize accuracy. While it can also optimize for performance or memory usage, our project has sufficient resources in these areas. Therefore, we prioritize accuracy as the primary optimization goal.

<Frame caption="19-eon-tuner-settings">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/continuous-gait-monitor-nordic-thingy53/19-eon-tuner-settings.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=ec4e294352ce708e937874cc4e3f61a4" width="1280" height="772" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/19-eon-tuner-settings.png" />
</Frame>

<br />

<Frame caption="20-eon-tuner">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/continuous-gait-monitor-nordic-thingy53/20-eon-tuner.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=38f5f9737c002347dd107bc5576f8ec7" width="1280" height="647" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/20-eon-tuner.png" />
</Frame>

### Anomaly Detection (K-means)

K-means clustering is chosen for gait anomaly detection due to its computational efficiency and ability to robustly identify distinct clusters. While Gaussian Mixture Models (GMMs) can model more complex data distributions, in our testing K-means excels in identifying distinct clusters like normal walking, running, and standing.

We chose L1 Root Mean Square (RMS) for anomaly detection with accelerometer data (accX, accY, accZ) due to its sensitivity to outliers and interpretability.  L1 RMS emphasizes large deviations, which helps identify significant gait abnormalities and provides insights into the specific directions of those anomalies. It's also more robust to noisy accelerometer data compared to L2 RMS.

<Frame caption="21-anomaly-detection-settings">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/continuous-gait-monitor-nordic-thingy53/21-anomaly-detection-settings.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=113cb8bcbc888dc52bf929b788255d58" width="925" height="1000" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/21-anomaly-detection-settings.png" />
</Frame>

<br />

<Frame caption="22-anomaly-vertical-forward">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/continuous-gait-monitor-nordic-thingy53/22-anomaly-vertical-forward.jpg?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=c93095ddef73139d465285f05196ef24" width="1280" height="740" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/22-anomaly-vertical-forward.jpg" />
</Frame>

<br />

<Frame caption="23-anomaly-forward-sideways">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/continuous-gait-monitor-nordic-thingy53/23-anomaly-forward-sideways.jpg?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=81fdeecbb8dc3dea9a532db023c7d018" width="1280" height="740" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/23-anomaly-forward-sideways.jpg" />
</Frame>

## Deployment

Now the AI model is ready to be deployed to the Edge. Nordic Thingy:53 is selected for our deployment option. For this project we chose unoptimized (float32) to preserve accuracy since our hardware has enough performance and memory headroom.

<Frame caption="24-deployment">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/continuous-gait-monitor-nordic-thingy53/24-deployment.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=00160dd83328ce095035ce5ece94cc79" width="1202" height="1000" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/24-deployment.png" />
</Frame>

After building our model, we'll get the new firmware. Follow this [guide](/hardware/boards/nordic-semi-thingy53#updating-the-firmware) to flash the firmware.

<Frame caption="25-write-firmware-nrfconnect">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/continuous-gait-monitor-nordic-thingy53/25-write-firmware-nrfconnect.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=071d91a011ae2715a6a3f1b6d70655b0" width="1233" height="1000" data-path=".assets/images/continuous-gait-monitor-nordic-thingy53/25-write-firmware-nrfconnect.png" />
</Frame>

## Conclusion

This project successfully demonstrates the potential for wearable AI solutions in early detection of gait disorders. By harnessing the Thingy:53's capabilities and Edge Impulse's streamlined workflow, we developed a device capable of identifying gait anomalies. This tool offers proactive health monitoring, with the potential to alert users to subtle changes that may foreshadow underlying medical conditions.  Future work could expand the dataset for greater robustness, explore additional sensor modalities, and conduct clinical trials to thoroughly validate the system for diagnostic use.

See this project in action:

<iframe src="https://www.youtube.com/embed/l7yP2IttN4Q" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />


Built with [Mintlify](https://mintlify.com).