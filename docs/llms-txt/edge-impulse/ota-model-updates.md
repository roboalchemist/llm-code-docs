# Source: https://docs.edgeimpulse.com/knowledge/concepts/lifecycle/ota-model-updates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OTA model updates

## Introduction

In this section we will explore how firmware updates and other scenarios are currently addressed, with traditional OTA. It should help you to get started planning your own updated impulse across a range of platforms.

Starting with platform-specific examples like Arduino Cloud, Nordic nRF Connect SDK / Zephyr and Golioth, Particle Workbench and Blues Wireless. Finally we will explore building an end-to-end example on the Espressif IDF.

By covering a cross section of platforms we hope to provide a good overview of the process and how it can be applied to your own project. With more generic examples like Arduino, Zephyr and C++ which can be applicable to all other vendors.

<Frame caption="Continuous Learning Sample Architecture">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/continuous_cycle.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=dba2ae7000299e0e767a134f796b6e26" width="1600" height="957" data-path=".assets/images/continuous_cycle.png" />
</Frame>

These tutorials will help you to get started with the following platforms:

* [Arduino](/tutorials/topics/lifecycle-management/ota-arduino)
* [Particle Workbench](/tutorials/topics/lifecycle-management/ota-particle-workbench)
* [Blues Wireless](/tutorials/topics/lifecycle-management/ota-blues-wireless)
* [C++ Espressif IDF](/tutorials/topics/lifecycle-management/ota-espressif-idf)
* [Nordic / Zephyr on Golioth](/tutorials/topics/lifecycle-management/ota-zephyr-golioth)

## Prerequisites

* **Edge Impulse Account**: If you haven't got one, [sign up here](https://studio.edgeimpulse.com/signup).
* **Trained Impulse**: If you're new, follow one of our end-to-end [tutorials](/tutorials)

## Overview

Edge Impulse recognises the need for OTA model updates, as the process is commonly referred to although we are going to be updating the impulse which includes more than just a model, a complete review of your infrastructure is required. Here is an example of the process:

## Detect a change

The initiation of an update to your device can be as straightforward as a call to our API to verify the availability of a new deployment. This verification can be executed either by a server or a device with adequate capabilities. Changes can be dependent on a range of factors, including but not limited to the last modified date of the project, the performance of the model, or the release version of the project e.g. [last modification](/apis/studio/projects/last-modification) date of the project endpoint.

## Download the latest impulse

After we inquire about the last modification, and if an update is available, proceed to [download the latest build](/apis/studio/deployment/download).

We could add further checking for impulse model performance, project release version tracking or other metrics to ensure the update is valid. However in this series we will try to keep it simple and focus on the core process. Here is an example of a more complete process:

* Identify components that influence change: Determine the components of your project that require updates. This could be based on performance metrics, data drift, or new data incorporation.

* Retrain: Focus on retraining based on the identified components of your project.

* Test and Validate: Before deploying the updated components, ensure thorough testing and validation to confirm their performance before sending the update.

* Deploy Updated Components: Utilize available OTA mechanisms to deploy the updated components to your devices. Ensure seamless integration with the existing deployment that remains unchanged.

* Monitor on device Performance: Post-deployment, continuously monitor the performance of the updated model to ensure it meets the desired objectives. See Lifecycle Management for more details.

The aim will be to make sure your device is always equipped with the most recent and efficient impulse, enhancing performance and accuracy.

## Conclusion

We hope this section has helped you to understand the process of OTA model updates and how to implement it in your own project. If you have any questions, please reach out to us on our [forum](https://forum.edgeimpulse.com/).


Built with [Mintlify](https://mintlify.com).