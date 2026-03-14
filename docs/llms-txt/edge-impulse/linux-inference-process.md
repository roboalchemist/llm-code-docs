# Source: https://docs.edgeimpulse.com/hardware/porting/linux-inference/linux-inference-process.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Linux Process Overview

This guide provides a step-by-step process for validating that your Linux device
is ready to run on-device inference with Edge Impulse models. By the end of this
section, you will understand how to run models using the CPU (AI accelerator usage is discussed separately).

<Frame caption="Linux Inferencing Process Overview">
  <img src="https://mintcdn.com/edgeimpulse/F0XbRxP1bJiYpXHo/.assets/images/porting/process-overview.png?fit=max&auto=format&n=F0XbRxP1bJiYpXHo&q=85&s=d255ddf450b4b37b5230535c5672b836" width="497" height="596" data-path=".assets/images/porting/process-overview.png" />
</Frame>

## Linux Inference Methods

Several methods can be used for running an Edge Impulse model on a Linux device;
each method suited for different needs. Each link below contains a guide to
install all the necessary dependencies and test inference on your device for the
selected method

* [Edge Impulse Linux CLI](/hardware/porting/linux-inference/linux-inference-cli)
* [Edge Impulse Linux C++ SDK](/hardware/porting/linux-inference/linux-inference-cpp)
* [Edge Impulse Linux Python SDK](/hardware/porting/linux-inference/linux-inference-python)

Before proceeding with each method, ensure you have a model trained in your Edge
Impulse account. It will be used for deployment in all the methods.
For testing purposes, we recommend cloning the public
[Cars In Parking Garage Project](https://studio.edgeimpulse.com/public/820244/v2),
but you can use another model you may already have.

<Info>
  #### Note

  If the project is cloned correctly, the project should appear in the list of projects in your profile.
  Regardless of the project you will be using - it should be fully completed - all
  the dots in the menu should be green and not grey. This means the model is ready for deployment.
</Info>

## Completion and Next steps

Completion of this process demonstrates that your device is "Edge Impulse Ready"
for inferencing. Now that you have successfully run an inference on your device,
you can explore further integration with Edge Impulse. Consider the following steps:

1. **Data Collection**: Implement data collection from your device to Edge Impulse for model training and improvement.
2. **Custom Sensors**: Integrate custom sensors by modifying the data acquisition code to suit your hardware.
3. **Optimize Performance**: Explore SDK hardware acceleration options available on your device to optimize inference performance.

<Info>
  #### Many Linux Targets Have Support Already!

  Please see the [list of officially supported Linux devices](/hardware). If your
  device is close to one of those devices you might be able to start from those
  documents in order to run data collection and inferencing. If your device is a
  derivative it is likely that the Edge Impulse on-device features work on your device.
  In general the process to test is as follows:

  1. Review the device support documentation and install the pre-requisites.
  2. Install the [Edge Impulse Linux Command Line Interface](https://github.com/edgeimpulse/edge-impulse-linux-cli) on your device.
  3. Complete an Edge Impulse Project and run edge-impulse-linux-runner to run an inference.
</Info>


Built with [Mintlify](https://mintlify.com).