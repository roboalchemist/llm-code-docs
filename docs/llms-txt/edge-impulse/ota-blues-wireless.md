# Source: https://docs.edgeimpulse.com/tutorials/topics/lifecycle-management/ota-blues-wireless.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Blues Wireless

### Introduction

This page is part of the [Lifecycle Management with Edge Impulse](/knowledge/concepts/lifecycle/lifecycle-management) tutorial series. If you haven't read the introduction yet, we recommend you to do so [here](/knowledge/concepts/lifecycle/ota-model-updates).

### Overview

OTA DFU with Notehub Blues Wireless have created a unique way to update firmware on your Notecard device is to perform an over-the-air DFU with Notehub.io. For instructions on how to update your Notecard firmware with Notehub.io, please visit the [Manage Notecard Firmware guide](https://dev.blues.io/guides-and-tutorials/notecard-guides/notecard-outboard-firmware-update/).

#### Key Features of Blues Wireless OTA Updates:

* NOFU: Notehub Outbound Firmware Update allows you to update the firmware on the Swan from Notehub.

#### Closing the Loop:

* Blues Wireless has created their own Edge Impulse ingestion API integration which allows you to collect data from the notecard.

#### Prerequisites:

* **Edge Impulse Account**: If you haven't got one, [sign up here](https://studio.edgeimpulse.com/signup).
* **Trained Impulse**: If you're new, follow one of our end-to-end [tutorials](/tutorials)
* **Blues Wireless Account**: If you haven't got one, [sign up here](https://blues.io/).
* **Blues Wireless Notecard**: If you haven't got one, [order here](https://blues.io/).

#### Webinar Recap: Optimized MLOps with Edge Impulse, Blues, and Zephyr:

Watch the full webinar [here](https://www.youtube.com/watch?v=7cLzNz0Sa-Y) for insights into MLOps and its integration with Edge Impulse, Blues, and Zephyr.

<iframe src="https://www.youtube.com/embed/7cLzNz0Sa-Y" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

***

**Webinar Overview:**

**Implementing MLOps Workflow:**

* Data collection using the Notecard.
* Sending data to Edge Impulse for model training.
* Deploying the trained model using Zephyr.
* Monitoring and continuous improvement.

***

### Establishing a Robust MLOps Workflow for TinyML

**Author:** TJ VanToll **link:** [https://dev.blues.io/blog/robust-ml-ops-workflow/](https://dev.blues.io/blog/robust-ml-ops-workflow/)

#### Introduction

In TinyML projects, the effectiveness of a machine learning model greatly depends on the quality of its training data. Gathering comprehensive training data is particularly challenging in TinyML due to the limited power and connectivity of tiny devices. At Blues, in collaboration with Edge Impulse and Zephyr, we have developed a workflow that facilitates MLOps (Machine Learning Operations) for tiny devices.

This tutorial outlines a method to implement a robust MLOps process, focusing on how to collect ML data from remote devices and update ML models on these devices in the field. The result is a workflow that seamlessly integrates data collection and model updating.

see the [Establishing a Robust MLOps Workflow for TinyML Blues Guide](https://dev.blues.io/blog/robust-ml-ops-workflow) for the in depth guide.

#### Collecting ML Data

Let's assume we're managing devices monitoring industrial equipment with accelerometers to detect abnormalities. For a successful MLOps workflow, these devices need to send accelerometer data to the cloud for training an updated model. Here, we use the Blues Notecard for this purpose.

**The Blues Notecard**

The Notecard is a system on module designed for easy connectivity in embedded projects. Its features include:

* 500MB of cellular connectivity
* Global cellular support over LTE-M, NB-IoT, or Cat-1
* Secure device-to-cloud communication
* Low-power hardware and firmware
* Easy embedding options

To set up the hardware, you'll need a Blues Starter Kit, which includes a development board (Notecarrier) and a Swan microcontroller. Additionally, an LIS3DH accelerometer connected to the Notecarrier via a Qwiic cable is required.

**The Firmware**

The project’s firmware gathers accelerometer readings and sends them to the cloud via the Notecard. We use Zephyr for firmware implementation, as it offers both low-level access and development conveniences. Zephyr firmware is compatible with STM32-based boards like the Swan, and the Notecard has a Zephyr SDK.

The firmware performs the following functions:

* Establishes a connection between the Notecard and Notehub
* Gathers data from the accelerometer
* Sends the data to Notehub

For example, the firmware takes accelerometer readings at intervals set by the Edge Impulse SDK and sends this data as a binary stream to Notehub.

#### Sending the Data

Notecard's new firmware (v5.3.1) introduces 'card.binary' APIs, enabling fast data transfer for large data packets. The data is then sent to Notehub using the 'web.post' method.

#### Getting the Data to Edge Impulse

The data from Notehub is forwarded to Edge Impulse through an HTTP server. This server, which can be created using any language or framework, listens for POST requests and parses the floating-point accelerometer values. The data is then sent to Edge Impulse's ingestion API, adding new entries to the model’s training set.

```javascript  theme={"system"}
const emptySignature = Array(64).fill("0").join("");
const body = {
    protected: {
        ver: "v1",
        alg: "none",
        iat: Math.floor(Date.now() / 1000),
    },
    signature: emptySignature,
    payload: {
        device_name: "device-1",
        device_type: "LIS2HH12",
        interval_ms: 1,
        sensors: [
            { name: "accX", units: "m/s2" },
            { name: "accY", units: "m/s2" },
            { name: "accZ", units: "m/s2" },
        ],
        values: data,
    },
};

try {
    await fetch("https://ingestion.edgeimpulse.com/api/training/data", {
        method: "POST",
        headers: {
            "x-api-key": process.env.EDGE_IMPULSE_API_KEY,
            "x-file-name": "test",
            "x-label": "idle",
            "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
    });
} catch (e) {
    console.log("Error publishing data", e);
}
```

see the [section of the Blues Guide](https://dev.blues.io/blog/robust-ml-ops-workflow/) for more information.

#### Updating ML Models

The final aspect of the MLOps process is updating the models on the devices in the field. For this, we use Notecard Outboard Firmware Update. This feature allows OTA firmware updates without writing any code, offering flexibility and safety against bricking devices.

see the [Updating ML Models section of the Blues Guide](https://dev.blues.io/blog/robust-ml-ops-workflow/#updating-ml-models) for more information.

**Notecard Outboard Firmware Update**

* Requires specific wiring (provided in the Blues Starter Kit)
* Activated via a 'card.dfu' request in the firmware
* Involves building a new firmware image file with the updated model
* The new firmware is uploaded to Notehub and applied to devices

see the [What is notecard outbound update? section of the Blues Guide](https://dev.blues.io/blog/robust-ml-ops-workflow/#what-is-notecard-outboard-firmware-update) for more information.

#### Conclusion

The combination of data collection and model updating forms a robust MLOps process. This approach ensures continuous improvement of ML models based on real data and updates models remotely. The provided GitHub samples offer a reference implementation, adaptable to various project needs.

For more information, refer to the \[Notecard Outboard Firmware Update guide]\([https://dev.blues.io/guides-and-tutorials/notecard-guides](https://dev.blues.io/guides-and-tutorials/notecard-guides)

The combination of data collection and model updating forms a robust MLOps process. This approach ensures continuous improvement of ML models based on real data and updates models remotely. The provided GitHub samples offer a reference implementation, adaptable to various project needs.

### Learn More

* **Build Your Edge ML Application**: Follow the step-by-step [Blues Swan tutorial](https://dev.blues.io/guides-and-tutorials/building-edge-ml-applications/blues-swan/).

### Summary

This tutorial acts as a reference to the webinar and tutorial from Blues Wireless: [Optimized MLOps with Edge Impulse, Blues, and Zephyr view the full webinar](https://www.youtube.com/watch?v=7cLzNz0Sa-Y).


Built with [Mintlify](https://mintlify.com).