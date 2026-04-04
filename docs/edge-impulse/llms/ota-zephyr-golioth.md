# Source: https://docs.edgeimpulse.com/tutorials/topics/lifecycle-management/ota-zephyr-golioth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zephyr on Golioth

### Introduction

This page is part of the [Lifecycle Management with Edge Impulse](/knowledge/concepts/lifecycle/lifecycle-management) tutorial series. If you haven't read the introduction yet, we recommend you to do so [here](/knowledge/concepts/lifecycle/ota-model-updates).

In this tutorial, we'll guide you through deploying updated impulses over-the-air (OTA) using the Zephyr RTOS. We'll build on Zephyr's firmware update workflow, incorporating API calls to check for updates to your edge impulse project and download the latest build. As Zephyr does not have an OTA update service, and Golioth is used in their OTA guide. We'll use Golioth's OTA update service to deliver the updated firmware to the device. On devices running Zephyr RTOS, leveraging Golioth's cloud platform for the firmware update portion of the process.

#### Key Features of Golioth OTA Updates:

* Secure and encrypted firmware delivery
* Delta updates to minimize download size
* Integration with Zephyr RTOS

### Prerequisites

* **Edge Impulse Account**: If you haven't got one, [sign up here](https://studio.edgeimpulse.com/signup).
* **Trained Impulse**: If you're new, follow one of our end-to-end [tutorials](/tutorials)
* Knowledge of Zephyr RTOS and nRF Connect SDK
* A Golioth account and the Golioth SDK installed

### Preparation

1. Clone the Golioth Zephyr SDK examples repository:

```bash  theme={"system"}
git clone https://github.com/golioth/zephyr-sdk.git
```

#### On Your nRF9160 Development Board:

2. Navigate to the Golioth firmware examples folder we are going to modify the device firmware update example to connect to the ingestion API to send data back from device.

```bash  theme={"system"}
cd zephyr-sdk/samples/dfu
```

Now copy the edge-impulse-sdk folder from the cloned repository into the dfu folder.

```bash  theme={"system"}
cp -r edge-impulse-sdk zephyr-sdk/samples/dfu
```

#### Include the header file the dfu example

```c  theme={"system"}
#include "edge-impulse-sdk/classifier/ei_run_classifier.h"

```

#### Take the run inference example from your existing project

You will need to merge in the run inference function from your existing project. This will be the function that will be called to run inference on the device.

```c  theme={"system"}
static void run_inference() {
    struct sensor_value accel[3];
    struct device *sensor = device_get_binding(SENSOR_DEV_NAME);
    if (sensor == NULL) {
        printk("Could not get %s device\n", SENSOR_DEV_NAME);
        return;
    }
    sensor_sample_fetch(sensor);
    sensor_channel_get(sensor, SENSOR_CHAN_ACCEL_XYZ, accel);

    float features[3];
    for (int i = 0; i < 3; i++) {
        features[i] = sensor_value_to_double(&accel[i]);
    }
```

#### Add the run inference function to the main loop

Now add the run inference function to the main loop of the dfu example. This will run inference every 2 seconds.

```c  theme={"system"}

int main() {
    struct device *sensor = device_get_binding(SENSOR_DEV_NAME);
    if (sensor == NULL) {
        printk("Could not get %s device\n", SENSOR_DEV_NAME);
        return -1;
    }
    struct sensor_trigger trig;
    trig.type = SENSOR_TRIG_DATA_READY;
    trig.chan = SENSOR_CHAN_ACCEL_XYZ;
    if (sensor_trigger_set(sensor, &trig, sensor_trigger_handler) < 0) {
        printk("Could not set trigger for %s sensor\n", SENSOR_DEV_NAME);
        return -1;
    }

    while (1) {
        k_sleep(K_SECONDS(1));
    }

    return 0;
}
```

#### Add a call back to send sensor data to Edge Impulse with data captured

```c  theme={"system"}
static void sensor_trigger_handler(struct device *dev, struct sensor_trigger *trigger) {
    run_inference();
    // Send data to Edge Impulse via ingestion API
    send_data_to_edge_impulse();

}
```

#### Add the send data to Edge Impulse function

```c  theme={"system"}
static void send_data_to_edge_impulse() {
    // Set up HTTP client request
    struct http_client_request req;
    struct http_client_ctx ctx;
    char data_buf[512];
    snprintf(data_buf, sizeof(data_buf), "{\"label\":\"%s\",\"data\":\"%s\"}", "my_label", "my_data");
    http_client_request_init(&req);
    req.method = HTTP_POST;
    req.url = "http://ingestion.edgeimpulse.com/api/training/data";
    req.protocol = "HTTP/1.1";
    req.host = "ingestion.edgeimpulse.com";
    req.header_fields = "Content-Type: application/json\r\n"
                        "x-api-key: " EDGE_IMPULSE_API_KEY "\r\n";
    req.payload = data_buf;
    req.payload_len = strlen(data_buf);
    http_client_init(&ctx, &req);
    // Send HTTP request
    int ret = http_client_send(&ctx);
    if (ret < 0) {
        printf("HTTP request failed: %d\n", ret);
    } else {
        printf("HTTP request sent successfully\n");
    }
}
```

#### Add the sensor trigger to the main function

```c  theme={"system"}
int main() {
    struct device *sensor = device_get_binding(SENSOR_DEV_NAME);
    if (sensor == NULL) {
        printk("Could not get %s device\n", SENSOR_DEV_NAME);
        return -1;
    }
    struct sensor_trigger trig;
    trig.type = SENSOR_TRIG_DATA_READY;
    trig.chan = SENSOR_CHAN_ACCEL_XYZ;
    if (sensor_trigger_set(sensor, &trig, sensor_trigger_handler) < 0) {
        printk("Could not set trigger for %s sensor\n", SENSOR_DEV_NAME);
        return -1;
    }

    while (1) {
        k_sleep(K_SECONDS(1));
    }

    return 0;
}

```

#### Building and Running

With the classification, ingestion code and Golioth implementation in place, proceed to build and run the application on the nRF9160 Development Board. Utilize the following commands:

```bash  theme={"system"}
west build -b nrf9160dk_nrf9160_ns -p
west flash

```

These commands will build and flash the firmware onto your development board.

#### Verifying The Operation

To verify that the Edge Impulse model is running and updating OTA with Golioth, observe the console output. It should display inference results at regular intervals. Also, you can monitor the device’s firmware version and its updates via the Golioth console.

#### Testing OTA Updates

Simulate an OTA update by changing the Edge Impulse model and repeating the build and flash process. Monitor the Golioth console for updates and check the device console to observe the changes in inference results.

#### Conclusion

Congratulations! You've successfully implemented OTA model updates with Edge Impulse on Zephyr RTOS and nRF Connect SDK, facilitated by Golioth. You can now continuously enhance and deploy machine learning models to your edge devices securely and efficiently.


Built with [Mintlify](https://mintlify.com).