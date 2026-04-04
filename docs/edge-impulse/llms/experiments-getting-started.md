# Source: https://docs.edgeimpulse.com/projects/expert-network/experiments-getting-started.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with Edge Impulse Experiments

Created By: [Adam Milton-Barker](https://www.adammiltonbarker.com)

Public Project Link: [https://studio.edgeimpulse.com/public/521263/latest](https://studio.edgeimpulse.com/public/521263/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-experiments.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=9e18c57074ad63fae3a9251efb96887e" width="1200" height="675" data-path=".assets/images/experiments-getting-started/edge-impulse-experiments.jpg" />
</Frame>

## Introduction

Edge Impulse Experiments are a powerful new feature that allows users to run multiple active Impulses within a single project. This enables seamless experimentation with various model configurations on the same dataset, offering a more efficient way to compare results.

The updated interface includes a new "Experiments" section, which centralizes Impulse management and integrates the EON Tuner for enhanced trial handling. Along with API enhancements and streamlined processes, these changes significantly accelerate development and improve project organization, making it easier to transition from data collection to deployment.

This project provides a walk through of how to use Experiments, along with a tutorial that will help you get started with Edge Impulse Experiments.

## Hardware

* Arduino Nano RPI2040 Connect [More Info](https://store.arduino.cc/products/arduino-nano-rp2040-connect)

## Platform

* Edge Impulse [Visit](https://www.edgeimpulse.com)

## Software

* Edge Impulse CLI [Install](/tools/clis/edge-impulse-cli/installation)
* Arduino CLI [Download](https://arduino.github.io/arduino-cli/latest/)
* Arduino IDE 2.2.1 [Download](https://www.arduino.cc/en/software)

## Getting Started

### Arduino Nano RPI2040 Connect

<Frame caption="Arduino Nano RPI2040 Connect">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/arduino-nano-rpi2040-connect.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=5df94d68be011aef6ac6155c5db5e496" width="1600" height="901" data-path=".assets/images/experiments-getting-started/arduino-nano-rpi2040-connect.jpg" />
</Frame>

The Arduino Nano RP2040 Connect is a highly versatile development board, bringing the power of the Raspberry Pi RP2040 microcontroller to the compact Nano form factor. Equipped with dual-core 32-bit Arm Cortex-M0+ processors, it enables seamless creation of IoT projects with built-in Wi-Fi and Bluetooth support via the U-blox Nina W102 module. The board includes an accelerometer, gyroscope, RGB LED, and omnidirectional microphone, making it ideal for real-time data collection and embedded AI applications.

<Frame caption="Arduino Nano RPI2040 Connect Pins">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/arduino-nano-rpi2040-connect-pins.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=6b099abbfce6b7c65a66220ea035f22e" width="650" height="650" data-path=".assets/images/experiments-getting-started/arduino-nano-rpi2040-connect-pins.jpg" />
</Frame>

The Nano RP2040 Connect is fully compatible with the Arduino Cloud platform, allowing users to rapidly prototype IoT solutions. It also supports MicroPython for those who prefer Python for programming. With a clock speed of 133 MHz, the board is well-suited for machine learning tasks, offering support for frameworks like TinyML and TensorFlow Lite. Additionally, its 6-axis IMU and temperature sensor expand the board's capability for advanced real-world applications.

To begin working with the Edge Impulse platform and the Nano RPI2040 Connect, follow [this tutorial](/hardware/boards/raspberry-pi-pico) to connect your device.

## Edge Impulse

### Create Edge Impulse Project

<Frame caption="Create Edge Impulse Project">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-project.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=71e1d44f21cf08a438e7b8a73b22fc5b" width="1600" height="755" data-path=".assets/images/experiments-getting-started/edge-impulse-project.jpg" />
</Frame>

Now it's time to create your Edge Impulse project. Head over to [Edge Impulse](https://studio.edgeimpulse.com/), log in, and create your new project.

Edge Impulse offers Experiments to all users, with the Developer plan allowing up to three simultaneous Experiments. Users on the Enterprise plan enjoy unlimited access to Experiments.

<Frame caption="Create Edge Impulse Project Dashboard">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-project-dashboard.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=86565e753a2ee520b1fb07b8c7a23b7b" width="1600" height="754" data-path=".assets/images/experiments-getting-started/edge-impulse-project-dashboard.jpg" />
</Frame>

Once your project is created, you will see the project dashboard which will show you new additions to the platform.

### Connect Your Device

Next you need to connect your device to the Edge Impulse platform. Ensuring you have the Nano connected to your computer, open a command line or terminal and use the following command:

```bash  theme={"system"}
edge-impulse-daemon
```

<Frame caption="Edge Impulse Project Device Connection">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-devices-cmd.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=5f9188d38995a1a1f8eef0d6cfc02e0d" width="1600" height="852" data-path=".assets/images/experiments-getting-started/edge-impulse-devices-cmd.jpg" />
</Frame>

You will be prompted for your Edge Impulse login details to proceed. Once authenticated you will need to choose the COM port that your device is connected to, and then select the Edge Impulse project you want to connect your device to.

<Frame caption="Edge Impulse Project Device Connected">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-devices-rp2040-connected.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=e951dba8fbbc808926f784f5f1779352" width="1600" height="759" data-path=".assets/images/experiments-getting-started/edge-impulse-devices-rp2040-connected.jpg" />
</Frame>

If you now head over to your project and go the `Devices` tab, you will see your device is now connected.

### Collect Data

<Frame caption="Edge Impulse Project Collect Data">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-rp2040-collect-data.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=ea5cc515cbb7fb317fa7a950e1e6f7be" width="1600" height="762" data-path=".assets/images/experiments-getting-started/edge-impulse-rp2040-collect-data.jpg" />
</Frame>

Now that your device is connected to Edge Impulse, it is time to collect some data. Head over to the `Data aquisition` tab and select the RPI2040.

<Frame caption="Edge Impulse Project Collect Normal Data">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-rp2040-collect-data-normal.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=d3a57dd3e43323197ee2510be49206cb" width="1600" height="761" data-path=".assets/images/experiments-getting-started/edge-impulse-rp2040-collect-data-normal.jpg" />
</Frame>

First we will create the `normal` data. This data will represent when a machine is running normally with no abnormal vibrations. Select the `Intertial` sensor and use `Normal` as the label. Next record about 3 minutes data, collected in 10 second samples from the device.

<Frame caption="Edge Impulse Project Collect Vibrations Data">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-rp2040-collect-data-vibrations.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=cf2790460327a7e3a5afd83478e4edb1" width="1600" height="765" data-path=".assets/images/experiments-getting-started/edge-impulse-rp2040-collect-data-vibrations.jpg" />
</Frame>

Next we will collect some `Vibrations` data. Change the label to `Vibrations` and record 3 minutes more of samples, but this time shake the Arduino around while the samples are being recorded.

<Frame caption="Edge Impulse Project Collected Data">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-rp2040-collected-data.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=4032e8adcc9129773ce1372ca6d73593" width="1600" height="764" data-path=".assets/images/experiments-getting-started/edge-impulse-rp2040-collected-data.jpg" />
</Frame>

You should now have about 6 minutes of data. Note that at this point the data is not split into Training and Testing groups.

<Frame caption="Edge Impulse Project Collected Data Split">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-data-train-test-split.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=0ec399a7b734078214b595a8ff6af7ce" width="1600" height="757" data-path=".assets/images/experiments-getting-started/edge-impulse-data-train-test-split.jpg" />
</Frame>

Head to the project dashboard and scroll to the `Danger Zone` at the bottom. Click on the `Perform train/test split` button to split the data.

<Frame caption="Edge Impulse Project Collected Data Split">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-data-split.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=19952014e11cea959bae55fbf2ee58bc" width="1600" height="761" data-path=".assets/images/experiments-getting-started/edge-impulse-data-split.jpg" />
</Frame>

Back on the `Data aquisition` tab, you will now see that the data has been split.

### Create Impulse

<Frame caption="Edge Impulse Project Create Impulse">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-create-impulse.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=a3dac1bb252187c1ec01dc8b265ec432" width="1600" height="760" data-path=".assets/images/experiments-getting-started/edge-impulse-create-impulse.jpg" />
</Frame>

Now it is time to create your Impulse. Head over to the `Create Impulse` tab and you should see the configuration for your Nano RPI2040. You can accept the defaults here.

### Spectral Analysis

<Frame caption="Edge Impulse Project Create Spectral Analysis Impulse">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-create-impulse-spectral.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=f8ccd5085f1cbfec6801c04bc497672a" width="1600" height="761" data-path=".assets/images/experiments-getting-started/edge-impulse-create-impulse-spectral.jpg" />
</Frame>

First we will use the `Spectral Analysis` Processing block. Spectral Analysis is ideal for examining repetitive movements, particularly using accelerometer data. This tool breaks down signals to reveal their frequency and power patterns over time.

Click `Add` to add the Spectral Analysis Processing block to your Impulse.

### Classification

<Frame caption="Edge Impulse Project Create Spectral Analysis Classification Impulse">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-create-impulse-spectral-classification.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=962e49160994cb7daedb8fbbe56263f0" width="1600" height="760" data-path=".assets/images/experiments-getting-started/edge-impulse-create-impulse-spectral-classification.jpg" />
</Frame>

For the Learning block, we will use `Classification` to classify between `Normal` and `Vibrations`. Click `Add` to add the Classification block to your Impulse.

Next click `Save Impulse`.

### Feature Generation

<Frame caption="Edge Impulse Project Spectral Analysis Classification Features">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-generate-features.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=9b68ea13e0dd17145491240e4cdae23d" width="1600" height="762" data-path=".assets/images/experiments-getting-started/edge-impulse-generate-features.jpg" />
</Frame>

Now we will generate the features that the AI model will use to learn. Head over to the `Spectral Features` tab and click on `Autotune parameters`. An autotune job will start and you will see the output on the right hand side of the UI.

<Frame caption="Edge Impulse Project Spectral Analysis Classification Features">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-save-parameters.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=cc635d68394a836f3420f34f071a3088" width="1600" height="765" data-path=".assets/images/experiments-getting-started/edge-impulse-save-parameters.jpg" />
</Frame>

Once the job is complete click `Save parameters`. You will be redirected to the `Generate features` tab.

<Frame caption="Edge Impulse Project Spectral Analysis Classification Features">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-generated-features.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=2b33ec2fb0c85cd3c5c4f66abfc17bbb" width="1600" height="764" data-path=".assets/images/experiments-getting-started/edge-impulse-generated-features.jpg" />
</Frame>

A feature generation job will start, and once finished you will see the features on the right hand side. The features should be nicely clustered, if you notice features that are not clustered correctly you can click on them, review the samples and update your dataset or settings to fix.

### Training

<Frame caption="Edge Impulse Project Spectral Analysis Classification Training">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-train-spectral-classifier.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=e60cb8cb2b9235f2a0a9625bf031e8ef" width="1600" height="762" data-path=".assets/images/experiments-getting-started/edge-impulse-train-spectral-classifier.jpg" />
</Frame>

Now it is time to train our model. Head over to the `Classifier` tab, leave the default settings intact, and click on `Save and train`.

A training job will start, and once completed you will see the results on the right hand side of the UI.

### Testing

<Frame caption="Edge Impulse Project Spectral Analysis Classification Testing">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-train-spectral-classifier-testing.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=8861fdec3935ff2bd44f23c607bcf34e" width="1600" height="763" data-path=".assets/images/experiments-getting-started/edge-impulse-train-spectral-classifier-testing.jpg" />
</Frame>

If you now head over to the `Model testing` tab, you will be able to use your newly trained model on the Test data that was set aside. The Test data was not shown to the model during training, so this will help to evaluate how well the model performs on unseen data.

The testing process will start and you will see the results once complete.

<Frame caption="Edge Impulse Project First Experiment">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-first-experiment.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=c9267e176ffb12ebc8826f1d3682e664" width="1600" height="756" data-path=".assets/images/experiments-getting-started/edge-impulse-first-experiment.jpg" />
</Frame>

If you head to the `Experiments` tab, you will see that you now have your first Experiment listed.

### Deployment

<Frame caption="Edge Impulse Project Deployment">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-deployment.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=c37ea76797a2f99cbaaa7dd1d12ed6ab" width="1600" height="766" data-path=".assets/images/experiments-getting-started/edge-impulse-deployment.jpg" />
</Frame>

You are now able to deploy your model to your Arduino. Head over to the `Deployment` tab and search for Arduino, then follow the steps provided to you to deploy the model to your device.

As this tutorial is specifically related to Experiments, we will continue straight to EON Tuner and creating our next Experiment.

### EON Tuner

<Frame caption="Edge Impulse Project EON Tuner">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-eon-tuner.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=fce213f4fc2404c94acf472c3dfecfde" width="1600" height="761" data-path=".assets/images/experiments-getting-started/edge-impulse-eon-tuner.jpg" />
</Frame>

The EON™ Tuner simultaneously tests multiple model architectures, chosen based on your device and latency needs, to identify the best one for your application. The tuning process can take a while, but you can monitor its progress at any point during the search.

<Frame caption="Edge Impulse Project EON Tuner">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-eon-tuner-run.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=9a2e1c1c79c929d367d6f123b7506e8d" width="1600" height="767" data-path=".assets/images/experiments-getting-started/edge-impulse-eon-tuner-run.jpg" />
</Frame>

On the `Experiments` tab, select `EON Tuner`. For the `Search space configuration` select `Classification` in the `Usecase templates` drop down, then click `Start tuning` to run.

At this point, it is time to grab a coffee and put your feet up, as this will take some time to complete.

## Experiment 2

<Frame caption="Edge Impulse Project EON Tuner">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-eon-tuner-add.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=8140a0314e24ff15bf9b62486efef647" width="1600" height="762" data-path=".assets/images/experiments-getting-started/edge-impulse-eon-tuner-add.jpg" />
</Frame>

If at any time during the EON tuning process, you see a configuration you would like to try, you can simply click the `Add` button for that configuration.

<Frame caption="Edge Impulse Project EON Tuner">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-eon-tuner-choose.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=43f6571ae0f04ac86419224616a8f8d8" width="1600" height="754" data-path=".assets/images/experiments-getting-started/edge-impulse-eon-tuner-choose.jpg" />
</Frame>

Here we see a configuration that has a considerable reduction for latency, RAM, and ROM, so we will use this configuration for our next Experiment.

<Frame caption="Edge Impulse Project Experiment 2">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/experiments-getting-started/edge-impulse-experiment-2.jpg?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=4342d43f4c7b80317a97d1c1b5a78c4e" width="1600" height="759" data-path=".assets/images/experiments-getting-started/edge-impulse-experiment-2.jpg" />
</Frame>

The platform will create the blocks for your new Impulse and add the features automatically for you. If you head back to the `Experiments` tab you will now see your new model waiting for you to test or deploy.

## Experiment 3

While the EON Tuner will help identify the best architectures and configuration automatically, you can also manually add a new Experiment in order to go through the blocks and neural network setup process again, by simply clicking on the "**Create new impulse**" button on the Experiments page.

At this point, once you have trained yet a third model and tested it's results, you now have 3 different models to choose from, and can select the best one to deploy to your device. In the Enterprise plan, you can continue to evaluate and iterate with even more Experiments.

## Conclusion

In this tutorial, we demonstrated how to build a defect detection system with Edge Impulse and the Arduino Nano RP2040, and how to leverage the EON Tuner to optimize your model. From there, we built a second and third model with the new Experiments feature in Edge Impulse to allow us to evaluate different options and results. With this, you can easily refine and enhance your models, showcasing the power and simplicity of Edge Impulse's new Experiments feature for continuous improvement in machine learning projects.


Built with [Mintlify](https://mintlify.com).