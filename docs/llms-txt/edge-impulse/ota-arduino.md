# Source: https://docs.edgeimpulse.com/tutorials/topics/lifecycle-management/ota-arduino.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Arduino IDE (for ESP32)

## Introduction

This page is part of the [Lifecycle Management with Edge Impulse](/knowledge/concepts/lifecycle/lifecycle-management) tutorial series. If you haven't read the introduction yet, we recommend you to do so [here](/knowledge/concepts/lifecycle/ota-model-updates).

In this tutorial, we'll guide you through deploying updated impulses over-the-air (OTA) to Arduino using Edge Impulse. We'll build on Arduino firmware update workflow, incorporating Edge Impulse's API to check for updates and download the latest build.

Let's get started!

### Prerequisites:

* **Edge Impulse Account**: If you haven't got one, [sign up here](https://studio.edgeimpulse.com/signup).

* **Trained Impulse**: If you're new, follow our [data acquisition](/studio/projects/data-acquisition) and [impulse design](/studio/projects/impulse-design) guides.

### Key Features of Arduino OTA Updates:

## Arduino OTA Update

## OTA Code

Here’s the complete C code for implementing OTA updates with Edge Impulse on ESP-EYE (ESP32).

```c  theme={"system"}

#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

const char* ssid = "your-SSID";
const char* password = "your-PASSWORD";

void setup() {
  Serial.begin(115200);
  Serial.println("Booting");
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    Serial.println("Connection Failed! Rebooting...");
    delay(5000);
    ESP.restart();
  }

  // Port defaults to 8266
  ArduinoOTA.setPort(8266);

  // Hostname defaults to esp8266-[ChipID]
  ArduinoOTA.setHostname("myesp8266");

  // No authentication by default
  ArduinoOTA.setPassword((const char *)"123");

  ArduinoOTA.onStart([]() {
    Serial.println("Start");
  });
  ArduinoOTA.onEnd([]() {
    Serial.println("\nEnd");
  });
  ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
    Serial.printf("Progress: %u%%\r", (progress / (total / 100)));
  });
  ArduinoOTA.onError([](ota_error_t error) {
    Serial.printf("Error[%u]: ", error);
    if (error == OTA_AUTH_ERROR) Serial.println("Auth Failed");
    else if (error == OTA_BEGIN_ERROR) Serial.println("Begin Failed");
    else if (error == OTA_CONNECT_ERROR) Serial.println("Connect Failed");
    else if (error == OTA_RECEIVE_ERROR) Serial.println("Receive Failed");
    else if (error == OTA_END_ERROR) Serial.println("End Failed");
  });
  ArduinoOTA.begin();
  Serial.println("Ready");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  ArduinoOTA.handle();
}

```

## Prerequisites

* A trained impulse in Edge Impulse Studio
* Installation of required software as detailed in the tutorial

## Preparation

Begin by setting up your device for OTA updates following Espressif's OTA firmware update workflow. Use the built binary from the C++ example and modify it to incorporate OTA functionality.

## Steps to Deploy Impulse to ESP32

### 1. Copy the ESP OTA example and configure your wifi settings

Clone the example repository and adjust it according to your project and connectivity settings.

```bash  theme={"system"}
mkdir ~/ota-esp32
cd ~/ota-esp32
cp -r $IDF_PATH/examples/system/ota .
idf.py set-target esp32
idf.py menuconfig
```

### 2. Server Side OTA

Modify the ESP OTA example server to check for updates to your project

```python  theme={"system"}
import requests
import json
import os

API_KEY = 'your-edge-impulse-api-key'
PROJECT_ID = 'your-project-id'
MODEL_PATH = 'path_to_your_local_model'

def get_last_modification_date():
    url = f'https://studio.edgeimpulse.com/v1/api/{PROJECT_ID}/last-modification-date'
    headers = {'x-api-key': API_KEY}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['lastModificationDate']
    else:
        print(f"Failed to get last modification date: {response.text}")
        return None

def download_model():
    url = f'https://studio.edgeimpulse.com/v1/api/{PROJECT_ID}/deployment/download'
    headers = {'x-api-key': API_KEY}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(MODEL_PATH, 'wb') as file:
            file.write(response.content)
        print("Model downloaded successfully.")
    else:
        print(f"Failed to download the model: {response.text}")

stored_timestamp = None # replace this with logic to get the stored timestamp or hash

# check for recent modifications
last_modification_date = get_last_modification_date()

# compare and download if newer
if last_modification_date and last_modification_date != stored_timestamp:
    print("New model available. Downloading...")
    download_model()

    # update the stored timestamp or hash
    stored_timestamp = last_modification_date

    # restart the device
    os.system('sudo reboot')






```

### 2. Modify the ESP OTA example to check for updates to your project

Modify the Edge Impulse C++ example for ESP32 to check for updates to your project and download the latest build.

We will need to add a few libraries to the project to facilitate the OTA update process. These are taken from the ESP32 OTA example and are already included in the example project.

## Components

### 1. Non-Volatile Storage (NVS)

```c  theme={"system"}
#include "nvs.h"
#include "nvs_flash.h"
```

NVS is utilized to persistently store data like configuration settings, WiFi credentials, or firmware update times, ensuring retention across reboots.

### 2. HTTP Client

```c  theme={"system"}
#include "esp_http_client.h"
```

This library facilitates HTTP requests to the server for checking and retrieving new firmware updates.

### 3. OTA Operations

```c  theme={"system"}
#include "esp_ota_ops.h"
#include "esp_https_ota.h"
```

These headers aid in executing OTA operations, including writing new firmware to the flash and switching boot partitions.

### 4. FreeRTOS Task

```c  theme={"system"}
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
```

FreeRTOS ensures OTA updates are conducted in a separate task, preventing blockage of other tasks and maintaining system operations during the update.

### 3. Updating the Device

Compare the model's timestamp or hash with the stored version. If it's different or newer, call the download\_model() function.

### 4. Monitoring and Repeating the Process

Monitor the device to ensure the new impulse performs as expected and repeat the update process as needed.

## Conclusion

This tutorial provides a comprehensive guide for implementing OTA updates on Espressif ESP-EYE (ESP32) with Edge Impulse. Follow each step meticulously, ensuring all prerequisites and preparation steps are completed before proceeding to the deployment phase. Happy coding!

Note: Adjust the code snippets and steps to suit your specific requirements and always ensure to test thoroughly before deploying updates to live environments.


Built with [Mintlify](https://mintlify.com).