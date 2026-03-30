# Source: https://docs.edgeimpulse.com/tutorials/topics/lifecycle-management/ota-arduino-iot-cloud.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Arduino IoT Cloud

### Introduction

This page is part of the [Lifecycle Management with Edge Impulse](/knowledge/concepts/lifecycle/lifecycle-management) tutorial series. If you haven't read the introduction yet, we recommend you do so [here](/knowledge/concepts/lifecycle/ota-model-updates).

In this tutorial, we'll guide you through deploying updated impulses over-the-air (OTA) to Arduino using the Arduino IoT Cloud and Edge Impulse.

Let's get started!

#### Prerequisites:

* **Edge Impulse Account**: [Sign up here](https://studio.edgeimpulse.com/signup).
* **Trained Impulse**: If you're new, follow our [data acquisition](/studio/projects/data-acquisition) and [impulse design](/studio/projects/impulse-design) guides.

#### Key Features of Arduino OTA Updates:

* **Remote Update**: Update your Arduino board firmware remotely.
* **Integration with Edge Impulse**: Seamlessly incorporate machine learning models.

### OTA Code

Here’s an example Arduino sketch for implementing OTA updates with Edge Impulse:

To expand the Arduino sketch to work with the Edge Impulse API, you'll need to add functionality to fetch the latest model updates from Edge Impulse and apply them to your device. Below is an extended version of the `loop()`, `connectToWiFi()`, and `onOTAEvent()` functions, integrating Edge Impulse API interactions:

#### `loop()` Function

* The `loop()` function regularly checks for updates from the Edge Impulse API.

```cpp  theme={"system"}
#include <HTTPClient.h>

void loop() {
  ArduinoIoTCloud.update();

  // Check for updates at regular intervals
  static unsigned long lastCheck = 0;
  if (millis() - lastCheck > CHECK_INTERVAL) {
    checkForUpdates();
    lastCheck = millis();
  }

  // Additional code to handle other tasks
}

void checkForUpdates() {
  // Logic to check for last modification date
  HTTPClient http;
  String apiURL = "https://studio.edgeimpulse.com/v1/api/your-project-id/last-modification-date";
  http.begin(apiURL);
  http.addHeader("x-api-key", "your-edge-impulse-api-key");

  int httpCode = http.GET();
  if (httpCode == HTTP_CODE_OK) {
    String payload = http.getString();
    // Parse payload to check for a new model version
    // If a new version is available, trigger the OTA event
    onOTAEvent();
  }
  http.end();
}
```

#### `connectToWiFi()` Function

* The `connectToWiFi()` function includes a maximum number of attempts to connect to WiFi.

```cpp  theme={"system"}
void connectToWiFi() {
  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(5000);
    Serial.print(".");
    attempts++;
    if (attempts >= MAX_ATTEMPTS) {
      Serial.println("Failed to connect to WiFi. Please check your credentials.");
      return;
    }
  }

  Serial.println("Connected to WiFi");
}
```

#### `onOTAEvent()` Function

* The `onOTAEvent()` function is triggered when a new update is available, downloading and applying the update.

```cpp  theme={"system"}
void onOTAEvent() {
  // This function is called when a new OTA firmware is available
  Serial.println("New OTA firmware available. Starting update...");

  // Implement the logic to download and update the firmware
  HTTPClient http;
  String firmwareURL = "https://studio.edgeimpulse.com/v1/api/your-project-id/deployment/download";
  http.begin(firmwareURL);
  http.addHeader("x-api-key", "your-edge-impulse-api-key");

  int httpCode = http.GET();
  if (httpCode == HTTP_CODE_OK) {
    // Here, implement the logic to apply the OTA update.
    // This might involve writing the new firmware to a specific location in flash memory
    // and then rebooting the device to apply the update.
    applyOTAUpdate(http.getStream());
  } else {
    Serial.println("Failed to download the update.");
  }
  http.end();
}

void applyOTAUpdate(WiFiClient &updateStream) {
  // Logic to apply the OTA update
  // Depending on your board and setup, this might involve writing to flash memory
  // and then rebooting the device.
}
```

This sketch sets up the Arduino to connect to the Arduino IoT Cloud and listens for OTA update notifications. When an OTA update is available, the `onOTAEvent` function is called, where you can implement the logic to download and update the firmware.

### Preparing for OTA Updates

1. **Setup Arduino IoT Cloud**: Configure your device and variables in the Arduino IoT Cloud.
2. **Connect your device**: Ensure your Arduino board is connected to the internet.
3. **Integrate with Edge Impulse**: Export your trained impulse from Edge Impulse as an Arduino library.

### Steps to Deploy Impulse to Arduino

1. **Update Sketch**: Incorporate the Edge Impulse library into your Arduino sketch.
2. **Listen for OTA Updates**: Use the Arduino IoT Cloud to push OTA updates to your device.
3. **Test and Monitor**: After deploying the update, monitor your device's performance and ensure the new impulse is functioning correctly.

#### Components

* **ArduinoIoTCloud**: Manages cloud connectivity and OTA updates.
* **WiFiNINA**: Handles WiFi connections for compatible boards.

### Conclusion

This tutorial provides a basic guide for implementing OTA updates on Arduino boards using the Arduino IoT Cloud and integrating with Edge Impulse. Expand and develop this example to suit your project's needs. Remember, testing is crucial before deploying updates in a live environment. Happy coding!


Built with [Mintlify](https://mintlify.com).