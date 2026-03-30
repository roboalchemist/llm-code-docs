# Source: https://docs.edgeimpulse.com/tutorials/topics/lifecycle-management/ota-espressif-idf.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Espressif IDF

### Introduction

This page is part of the [Lifecycle Management with Edge Impulse](/knowledge/concepts/lifecycle/lifecycle-management) tutorial series. If you haven't read the introduction yet, we recommend you to do so [here](/knowledge/concepts/lifecycle/ota-model-updates).

In this tutorial, we'll guide you through deploying updated impulses over-the-air (OTA) to the ESP32 using Edge Impulse. We'll build on Espressif's end-to-end OTA firmware update workflow, incorporating Edge Impulse's API to check for updates and download the latest build.

We will modify the Edge Impulse C++ example for ESP32, and combine it with the OTA example from the ESP IDF repository. This will allow us to check for updates to your project on the server side of the IDF example and download the latest build. We will then modify the C++ example to incorporate the OTA functionality and update the device with the latest build. Finally we will add calls back to our ingestion service to monitor the performance of the updated impulse, and gather data. Closing the loop on our active learning cycle.

Let's get started!

#### Key Features of Espressif OTA Updates:

### Prerequisites

* **Edge Impulse Account**: If you haven't got one, [sign up here](https://studio.edgeimpulse.com/signup).
* **Trained Impulse**: If you're new, follow one of our end-to-end [tutorials](/tutorials)
* Knowledge of the ESP IDF development framework and C++ for ESP32
* Installation of required software as detailed in the tutorial

### Preparation

Begin by setting up your device for OTA updates following Espressif's OTA firmware update workflow. Use the built binary from the C++ example and modify it to incorporate OTA functionality.

Let's get started!

### On your Espressif ESP-EYE (ESP32) development board

We created an example repository which contains a small application for Espressif ESP32, which takes the raw features as an argument, and prints out the final classification. Download the application as a .zip, or import this repository using Git:

```bash  theme={"system"}
git clone https://github.com/edgeimpulse/example-standalone-inferencing-espressif-esp32
```

We will need to add a few libraries to the project to facilitate the OTA update process. These will be taken from the ESP32 OTA example and are already included in the example project.

### ESP IDF OTA

We are going to use the ESP IDF OTA example as a starting point. Running a python server to check for updates and download the latest build from edge impulse. This detemines if there is a new build available and downloads it to the device.You could add more advanced checking for model performance and versioning to this process. This example will only download the latest build if there is a new build available based on date to save lengthy code examples.

This example is available in the ESP IDF repository. You can find the example in:

```bash  theme={"system"}
$IDF_PATH/examples/system/ota
```

Starting with the device side code, we will need to add a few libraries to the project to facilitate the OTA update process. These are taken from the ESP32 OTA example and are already included in the example project.

### Step 1: Copy the IDF OTA example and clone a fresh version of the edge impulse example C++ inferencing repository

```bash  theme={"system"}
  mkdir ~/ota-esp32
  cd ~/ota-esp32
  cp -r $IDF_PATH/examples/system/ota .
  git clone https://github.com/edgeimpulse/example-standalone-inferencing-espressif-esp32
```

### Now we will set up the Server Side components of the OTA update process

#### 1. Python Server Side OTA

Modify the ESP OTA example python server to check for updates to your project, we will use the date to determine when a new update should be performed to keep things simple. You could add more advanced checking for model performance and versioning to this process. This example will only download the latest build if there is a new build available based on date to save lengthy code examples.

```bash  theme={"system"}
cd ~/ota-esp32/ota
```

```python  theme={"system"}
import requests
import json
import os
import sys

API_KEY = 'your-edge-impulse-api-key'
PROJECT_ID = 'your-project-id'
MODEL_PATH = 'path_to_your_local_model'
TIMESTAMP_PATH = 'last_modification_date.txt'

def get_last_modification_date():
    try:
        url = f'https://studio.edgeimpulse.com/v1/api/{PROJECT_ID}/last-modification-date'
        headers = {'x-api-key': API_KEY}

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        return data['lastModificationDate']
    except Exception as e:
        print(f"Failed to get last modification date: {e}")
        return None

def download_model():
    try:
        url = f'https://studio.edgeimpulse.com/v1/api/{PROJECT_ID}/deployment/download'
        headers = {'x-api-key': API_KEY}

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        with open(MODEL_PATH, 'wb') as file:
            file.write(response.content)
        print("Model downloaded successfully.")
    except Exception as e:
        print(f"Failed to download the model: {e}")

def save_timestamp(timestamp):
    try:
        with open(TIMESTAMP_PATH, 'w') as file:
            file.write(timestamp)
    except Exception as e:
        print(f"Failed to save timestamp: {e}")

def get_stored_timestamp():
    try:
        if os.path.exists(TIMESTAMP_PATH):
            with open(TIMESTAMP_PATH, 'r') as file:
                return file.read().strip()
    except Exception as e:
        print(f"Failed to read stored timestamp: {e}")
    return None

# get the stored timestamp
stored_timestamp = get_stored_timestamp()

# check for recent modifications
last_modification_date = get_last_modification_date()

# compare and download if newer
if last_modification_date and last_modification_date != stored_timestamp:
    print("New model available. Downloading...")
    download_model()

    # update the stored timestamp
    save_timestamp(last_modification_date)
else:
    print("No new model available.")


```

#### 2.

Building the firmware to deploy to our device in the field. We will use the IDF build system to build the firmware. This would be automated but again to save time and complexity we will do this manually.

```bash  theme={"system"}

cd ~/ota-esp32/example-standalone-inferencing-espressif-esp32
idf.py set-target esp32
idf.py build
```

### 3. Updating the Device

Compare the model's timestamp or hash with the stored version. If it's different or newer, call the download\_model() function.

#### 4. Monitoring and Repeating the Process

Monitor the device to ensure the new impulse performs as expected and repeat the update process as needed.

Here we would make calls back to our ingestion service to monitor the performance of the updated impulse, and gather data. Closing the loop on our active learning cycle.

### Device Side of the OTA Update Process

Now lets modify the C++ example to incorporate the device side of the OTA functionality and update our edge impulse project with the device side data. We will add the OTA functionality to the C++ example and update the device with the latest build.

### Step 1: Include Necessary Headers

Include the necessary headers and components in your main ESP32 C++ based edge impulse project. There are a number of components that are required for the OTA update process:

### Components

#### 1. Non-Volatile Storage (NVS)

```c  theme={"system"}
#include "nvs.h"
#include "nvs_flash.h"
```

NVS is utilized to persistently store data like configuration settings, WiFi credentials, or firmware update times, ensuring retention across reboots.

#### 2. HTTP Client

```c  theme={"system"}
#include "esp_http_client.h"
```

This library facilitates HTTP requests to the server for checking and retrieving new firmware updates.

#### 3. OTA Operations

```c  theme={"system"}
#include "esp_ota_ops.h"
#include "esp_https_ota.h"
```

These headers aid in executing OTA operations, including writing new firmware to the flash and switching boot partitions.

#### 4. FreeRTOS Task

```c  theme={"system"}
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
```

FreeRTOS ensures OTA updates are conducted in a separate task, preventing blockage of other tasks and maintaining system operations during the update.

Lets start by adding the necessary headers to the main.cpp file in the edge impulse project.

```cpp  theme={"system"}
#include <stdio.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <esp_system.h>
#include <esp_log.h>
#include <esp_ota_ops.h>
#include <esp_http_client.h>
#include <esp_flash_partitions.h>
#include <esp_partition.h>
#include <nvs.h>
#include <nvs_flash.h>
```

Step 3: OTA Task Implement the OTA task that will handle the OTA update process. Connecting to the python server we created in the beginning of this tutorial. Which is checking for updates to your project

```cpp  theme={"system"}
void simple_ota_example_task(void *pvParameter)
{
  esp_http_client_config_t config = {
      .url = "http://192.168.1.10/your-ota-firmware.bin",
  };

  esp_err_t ret = esp_https_ota(&config);
  if (ret == ESP_OK) {
      esp_restart();
  } else {
      ESP_LOGE("OTA", "Firmware upgrade failed");
  }

  while (1) {
      vTaskDelay(1000 / portTICK_PERIOD_MS);
  }
}
```

In the simple\_ota\_example\_task function, you'll need to replace `http://192.168.1.10/your-ota-firmware.bin` with the actual URL where your firmware binary is hosted.

Step 4: App Main Here’s how the app\_main function should look like:

```cpp  theme={"system"}
void app_main(void)
{
  // Initialize NVS
  esp_err_t ret = nvs_flash_init();
  if (ret == ESP_ERR_NVS_NO_FREE_PAGES || ret == ESP_ERR_NVS_NEW_VERSION_FOUND) {
      ESP_ERROR_CHECK(nvs_flash_erase());
      ret = nvs_flash_init();
  }
  ESP_ERROR_CHECK(ret);

  xTaskCreate(&simple_ota_example_task, "ota_example_task", 8192, NULL, 5, NULL);
}
```

Step 5: Set the target and configuration Make sure you have the partition table set up correctly to support OTA. In the IDF Menu Config, An OTA data partition (type data, subtype ota) must be included in the Partition Table of any project which uses the OTA functions.

```bash  theme={"system"}
cd ~/ota-esp32
idf.py set-target esp32
idf.py menuconfig
```

Step 6: Compile and Flash You should compile the firmware and flash it to your ESP32 using the IDF build system commands.

```bash  theme={"system"}
idf.py build
idf.py -p PORT flash
```

Note: Before you run this code, make sure to replace `http://192.168.1.10.com/your-ota-firmware.bin` with the actual URL where your new firmware binary is hosted. Make sure that your ESP32 is connected to the internet to access this URL. Also, always test OTA functionality thoroughly before deploying it in a production environment.

### Conclusion

This tutorial provides a basic guide for implementing OTA updates on Espressif ESP-EYE (ESP32) with Edge Impulse. It can be extended to include more advanced checking, utilizing more of espressif OTA functionality, and extending the python server to check for model performance and versioning. Happy coding!


Built with [Mintlify](https://mintlify.com).