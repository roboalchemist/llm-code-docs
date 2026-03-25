# Source: https://docs.edgeimpulse.com/tutorials/topics/lifecycle-management/ota-thingy53.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Nordic Thingy53

### Introduction

This tutorial is part of the [Lifecycle Management with Edge Impulse](/knowledge/concepts/lifecycle/lifecycle-management) series. If you haven't read the introduction yet, we recommend doing so [here](/knowledge/concepts/lifecycle/ota-model-updates).

We'll guide you through deploying updated machine learning models over-the-air (OTA) to the Nordic Thingy:53 using Edge Impulse. This process leverages the Nordic Thingy:53 app, allowing users to deploy firmware updates and facilitating on-device testing for Lifecycle Management.

#### Key Features of Nordic Thingy:53 OTA Updates:

* User-initiated firmware deployment via the Nordic Thingy:53 app.
* Remote data collection and on-device testing for machine learning models.
* Seamless integration with Edge Impulse for Lifecycle Management.

### Prerequisites

* **Edge Impulse Account**: Sign up if you don't have one [here](https://studio.edgeimpulse.com/signup).
* **Trained Impulse**: If you're new, follow one of our end-to-end [tutorials](/tutorials)
* **Nordic Thingy:53**: Have the device ready and charged.
* **Nordic Thingy:53 App**: Installed on your smartphone or tablet.

### Preparation

Begin by connecting your Nordic Thingy:53 to the Edge Impulse platform and setting it up for data collection and model deployment.

### Step-by-Step Guide

#### 1. Setting Up Nordic Thingy:53 with Edge Impulse

* Connect your Nordic Thingy:53 to the Edge Impulse using the Nordic Thingy:53 app. This will be your interface for managing the device and deploying updates.

#### 2. Collecting Data and Training the Model

* Use the Nordic Thingy:53 to collect relevant data for your machine learning application.
* Upload this data to Edge Impulse and train your model.

#### 3. Deploying the Model via the Nordic Thingy:53 App

* Once your model is trained and ready, use the Nordic Thingy:53 app to deploy it to the device.
* The app allows you to initiate the OTA update, which downloads and installs the latest firmware containing the new model.

#### 4. Remote On-Device Testing

* Conduct remote testing through the app to evaluate the model's performance in real-world scenarios.
* This step is crucial for validating the effectiveness of your machine learning model.

#### 5. Continuous Improvement Cycle

* Continuously collect new data with the Nordic Thingy:53.
* Re-train your model on Edge Impulse with this new data.
* Deploy these updates to the Thingy:53 via the app, maintaining the cycle of Lifecycle Management.

### Conclusion

This tutorial provides a straightforward approach to implementing OTA updates and Lifecycle Management on the Nordic Thingy:53 using Edge Impulse. The user-friendly Nordic Thingy:53 app facilitates easy deployment of firmware updates, making it ideal for rapid prototyping and iterative machine learning model development.

### Additional Resources

* [Nordic Thingy:53 Documentation](https://www.nordicsemi.com/Products/Development-hardware/Nordic-Thingy-53/)
* [Edge Impulse Documentation](/)

This guide helps users leverage the capabilities of the Nordic Thingy:53 for advanced IoT applications, ensuring devices are always updated with the latest intelligence and improvements.


Built with [Mintlify](https://mintlify.com).