# Source: https://docs.edgeimpulse.com/tutorials/topics/lifecycle-management/ota-particle-workbench.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Particle Workbench

## Introduction

This page is part of the [Lifecycle Management with Edge Impulse](/knowledge/concepts/lifecycle/lifecycle-management) tutorial series. If you haven't read the introduction yet, we recommend you to do so [here](/knowledge/concepts/lifecycle/ota-model-updates).

In this tutorial, we'll guide you through deploying updated impulses over-the-air (OTA) using the Particle Workbench. We'll build on Particle's firmware update workflow, incorporating Edge Impulse's API to check for updates and download the latest build.

We will modify the Edge Impulse Photon 2 example to incorporate the OTA functionality and update the device with the latest build. Based on the particle workbench OTA example.

## Prerequisites

* **Edge Impulse Account**: If you haven't got one, [sign up here](https://studio.edgeimpulse.com/signup).

* **Trained Impulse**: If you're new, follow one of our end-to-end [tutorials](/tutorials)

* Knowledge of the Particle Workbench

* Installation of required software as detailed in the [Photon 2 example](/hardware/boards/particle-photon-2)

## Preparation

Begin by setting up your device for OTA updates following the particle documentation. [https://docs.particle.io/getting-started/cloud/ota-updates/](https://docs.particle.io/getting-started/cloud/ota-updates/)

Let's get started!

### Key Features of Particle Workbench OTA Updates:

* **Development Devices:** Specific devices can be marked for internal testing to validate firmware updates before a broader rollout.
* **Firmware Upload:** Developers upload the compiled binary to the console, ensuring the firmware version is included.
* **Firmware Locking:** Specific devices can be locked to run certain firmware versions for testing purposes.
* **Release Targets:** Firmware can be released to all devices or specific groups to control the rollout process.
* **Intelligent Firmware Releases:** Ensures timely delivery of updates without disrupting device operation, taking into account the device’s status and activity.

### Particle OTA

Particle OTA is a fully-integrated over-the-air software update system that is built into the Particle IoT PaaS and Device OS. It allows customers to safely and reliably push software updates to single devices or entire fleets of devices directly from Particle’s device management console and developer tools, with no implementation work necessary.

Particle OTA allows you to update your entire IoT device (both the Particle device and any other components) by delivering three kinds of updates:

* Application OTA allows users to update the firmware application they are running on the Particle device in order to introduce new features, fix bugs, and generally improve the software application over time.

* Device OS OTA allows users to update Device OS to the latest version alongside an application update so that Device OS can be kept up to date with improvements and bug fixes while properly testing against the user-generated software application.

* Asset OTA allows users to include bundled assets in an OTA software update that can be delivered to other processors and components in the electronics system so that the Particle device can be responsible not just for updating itself but also the system that surrounds the device.

## On your Edge Impulse project

Export your impulse to the Particle Workbench library:

Add the library through the Particle Workbench via:

1. Extract the .zip library.
2. Particle: Import Project and select project.properties.
   Examples can then be found in:
   yourprojectname/examples/

We created an example repository which contains a small application for your particle device.

```bash  theme={"system"}
git clone https://github.com/edgeimpulse/example-standalone-inferencing-photon2
```

## Creating the Intial Impulse Export to Particle Library and Deployment firmware

You will need to treat this as a new project and follow the instructions in the [Particle Workbench](https://docs.particle.io/tutorials/developer-tools/workbench/) to set up your environment for local development.

### Projects with external libraries

If your project includes a library that has not been registered in the Particle libraries system, you should create a new folder named `/lib/<libraryname>/src` under `/<project dir>` and add the `.h`, `.cpp` & `library.properties` files for your library there. Read the [Firmware Libraries guide](https://docs.particle.io/guide/tools-and-features/libraries/) for more details on how to develop libraries. Note that all contents of the `/lib` folder and subfolders will also be sent to the Cloud for compilation.

## Compiling your project

When you're ready to compile your project, make sure you have the correct Particle device target selected and run `particle compile <platform>` in the CLI or click the Compile button in the Desktop IDE. The following files in your project folder will be sent to the compile service:

* Everything in the `/src` folder, including your `.ino` application file
* The `project.properties` file for your project
* Any libraries stored under `lib/<libraryname>/src`

You should now have a compiled binary file in your project folder named `firmware.bin`.

Next lets look at the OTA functionality and how we can incorporate it into our project.

## Particle Workbench OTA Update Workflow and example

You will need to have a device deployed with an existing firmware containing an impulse before you can roll out a new version. Then you can use the OTA workflow to update the firmware on your device to a new version. While blocking all other devices from updating to the new version.

### Step 1: Testing on Development Devices

<Frame caption="Mark development device">
  <img src="https://mintcdn.com/edgeimpulse/pYR5gDDS-qVBI9Qw/.assets/images/ota/image.png?fit=max&auto=format&n=pYR5gDDS-qVBI9Qw&q=85&s=620bc7be5dcca91d3128da8ff5940ccf" width="1600" height="776" data-path=".assets/images/ota/image.png" />
</Frame>

Mark Devices for Testing: In the Particle console, mark specific devices for internal testing to validate firmware updates.
Upload Firmware: Compile and upload the firmware binary, ensuring to include the product ID and version.

### Step 2: Locking Firmware for Testing

Lock Devices: Lock specific devices to the new firmware version and monitor their behavior.
Unlock Devices: Unlock the devices once testing is complete and you are satisfied with the firmware's performance.

### Step 3: Rolling Out the Firmware

Release Targets: Choose to release the firmware to specific groups or the entire fleet of devices.
Intelligent Firmware Release: Opt for this to have the Particle Device Cloud intelligently manage the update rollout.
Important Tips:
Avoid Disruptions: Utilize Device OS APIs to control OTA availability, ensuring devices aren’t disrupted during critical operations.
Managing OTA Updates: Use the console or REST API to force enable OTA updates if needed.
Monitoring: Keep an eye on the devices' behaviors post-update to quickly identify and address any potential issues.
With Particle's OTA capabilities, developers can ensure that their IoT devices are always running the latest, most secure, and most efficient version of their firmware, enhancing the reliability and functionality of their IoT ecosystems.

## Creating a Webhook for the Edge Impulse ingestion API

This guide supplements the tutorial on OTA Model Updates with Edge Impulse on Particle Workbench, focusing on configuring a Particle webhook for sending data to the Edge Impulse ingestion API.

### Steps for Webhook Configuration:

1. **Access Particle Console**:
   * Visit [Particle Console](https://console.particle.io).
   * Log in with your Particle account credentials.

2. **Navigate to Integrations**:
   * Click on the "Integrations" tab in the left-hand menu.
   * Select "Webhooks" from the available options.

3. **Create a New Webhook**:
   * Click "New Integration".
   * Choose "Webhook".

4. **Webhook Configuration**:
   * **Name**: Assign a descriptive name to your webhook.
   * **Event Name**: Specify the event name that triggers the webhook (e.g., "edge/ingest").
   * **URL**: Set this to the Edge Impulse ingestion API URL, typically something like `https://ingestion.edgeimpulse.com/api/training/data`.
   * **Request Type**: Choose "POST".
   * **Request Format**: Select "Custom".

5. **Custom Request Body**:
   * Input the JSON structure required by Edge Impulse. This will vary based on your project's data schema.

6. **HTTP Headers**:
   * Add necessary headers:
     * `x-api-key`: Your Edge Impulse API key.
     * `Content-Type`: "application/json".
     * `x-file-name`: Use a dynamic data field like `{{PARTICLE_EVENT_NAME}}`.

7. **Advanced Settings**:
   * **Response Topic**: Create a custom topic for webhook responses, e.g., `{{PARTICLE_DEVICE_ID}}/hook-response/{{PARTICLE_EVENT_NAME}}`.
   * **Enforce SSL**: Choose "Yes" for secure transmission.

8. **Save the Webhook**:
   * After entering all details, click "Save".

9. **Test the Webhook**:
   * Use example device firmware to trigger the webhook.
   * Observe the responses in the Particle Console.

10. **Debugging**:

* If errors occur, review the logs for detailed information.
* Ensure payload format aligns with Edge Impulse requirements.
* Verify the accuracy of your API key and other details.

### Custom Template Example:

Copy and paste the following into the Custom Template section of the webhook:

```json  theme={"system"}
{
    "name": "edgeimpulse.com",
    "event": "edge/ingest",
    "responseTopic": "",
    "disabled": true,
    "url": "http://ingestion.edgeimpulse.com/api/training/data",
    "requestType": "POST",
    "noDefaults": true,
    "rejectUnauthorized": false,
    "headers": {
        "x-api-key": "ei_1855db...",
        "x-file-name": "{{PARTICLE_EVENT_NAME}}",
        "x-label": "coffee"
    },
    "json": "{\n  \"payload\": {\n    \"device_name\": \"0a10a...\",\n    \"device_type\": \"photon2\",\n    \"interval_ms\": 20,\n    \"sensors\": [\n      {\n        \"name\": \"volt\",\n        \"units\": \"V\"\n      },\n      {\n        \"name\": \"curr\",\n        \"units\": \"A\"\n      }\n    ],\n    \"values\": [\n{{{PARTICLE_EVENT_VALUE}}}\n    ]\n  },\n  \"protected\": {\n    \"alg\": \"none\",\n    \"ver\": \"v1\"\n  },\n  \"signature\": \"00\"\n}"
}
```

## Closing the Loop to send data to Edge Impulse for Lifecycle Management

Below we will do a basic example of sending data to Edge Impulse for Lifecycle Management.
We could further extend this example to include more advanced checking, utilizing more of Particle OTA functionality, and add checks for model performance and versioning. The code gathers data from analog sensors, processes it, and sends it to Edge Impulse for Lifecycle Management. The webhook is triggered with the event name edge/ingest/sample.

```c  theme={"system"}
#include "Particle.h"

// Sample data array
int sampleData[2][10] = {
    {100, 110, 120, 130, 140, 150, 160, 170, 180, 190}, // Sample voltage data
    {200, 210, 220, 230, 240, 250, 260, 270, 280, 290}  // Sample current data
};

void setup() {
    Serial.begin(9600);
    Particle.connect();
}

void loop() {
    char dataBuf[512];
    JSONBufferWriter writer(dataBuf, sizeof(dataBuf) - 1);

    writer.beginArray();
    for(int i = 0; i < 10; i++) {
        writer.beginArray();
        writer.value(sampleData[0][i]);
        writer.value(sampleData[1][i]);
        writer.endArray();
    }
    writer.endArray();

    Particle.publish("edge/ingest/sample", dataBuf, PRIVATE);
    delay(10000); // Send data every 10 seconds
}
```

This code continuously samples voltage and current, calculates RMS current, and then sends a JSON array of the sampled data to the Edge Impulse ingestion API. The publishData function uses Particle's Particle.publish method to send the data to the specified event. This triggers the webhook configured to send data to Edge Impulse. See the [Particle energy monitor code from our Imagine 2023 demo for a full example](https://github.com/edgeimpulse/particle-energy-monitor-data-ingestion/blob/main/src/2023_edge_impulse_imagine_demo.ino) for more information.

## Conclusion

This tutorial provides a basic guide for implementing OTA updates on your Particle Workbench connected device (Photon 2). It can be extended to include more advanced checking, utilizing more of espressif OTA functionality, and extending the python server to check for model performance and versioning. Happy coding!


Built with [Mintlify](https://mintlify.com).