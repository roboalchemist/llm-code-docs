# Source: https://docs.edgeimpulse.com/tools/clis/edge-impulse-cli/impulse-runner.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Impulse runner

The impulse runner shows the results of your impulse running on your development board. This only applies to ready-to-go binaries built from the studio.

You start the impulse via:

```
$ edge-impulse-run-impulse
```

This will sample data from your real sensors, classify the data, then print the results. E.g.:

```
edge-impulse-run-impulse
Edge Impulse impulse runner v1.7.3
[SER] Connecting to /dev/tty.usbmodem401103
[SER] Serial is connected, trying to read config...
[SER] Retrieved configuration
[SER] Device is running AT command version 1.3.0
[SER] Started inferencing...
Inferencing settings:
        Interval: 16.00 ms.
        Frame size: 375
        Sample length: 2000 ms.
        No. of classes: 4
Starting inferencing, press 'b' to break
Sampling... Storing in file name: /fs/device-classification.4
Predictions (DSP: 16 ms., Classification: 1 ms., Anomaly: 2 ms.):
    idle: 0.91016
    snake: 0.08203
    updown: 0.00391
    wave: 0.00391
    anomaly score: -0.067
Finished inferencing, raw data is stored in '/fs/device-classification.4'. Use AT+UPLOADFILE to send back to Edge Impulse.
```

### Other options

* `--debug` - run the impulse in debug mode, this will print the intermediate DSP results. For image models, a live feed of the camera and inference results will also be locally hosted and available in your browser (More on this below.)
* `--continuous` - run the impulse in continuous mode (not available on all platforms).

### Embedded API Server

The Linux CLI Runner has an embedded API server that allows you to interact with the model easily from any application, environment, or framework that implements an HTTP client. This feature is started with the runner using the `--run-http-server <port>` option.

To start the API server:

```
$ edge-impulse-linux-runner --debug
```

Which will share the link to the web page where you can see the live feed of the camera and inference results.

or

```
$ edge-impulse-linux-runner --run-http-server 3000
```

This will start the API server on port 3000, if you don't have an image model you will not see the http server web page.

#### API Endpoints

Once the server is running, you can send HTTP requests to interact with the model. Here is a simple example using Python:

For time series data...

```
import requests
import json

url = 'http://localhost:3000/classify'
data = {'data': [/* {"timestamp": 0, "x": 0.01, "y": -0.02, "z": 9.81},
        {"timestamp": 16, "x": 0.02, "y": -0.01, "z": 9.80},
        {"timestamp": 32, "x": 0.00, "y": 0.00, "z": 9.79} . . . modify here with your captured data to send to your project */]}

response = requests.post(url, json=data)
print(response.json())
```

For image data, and how to get data from a webcam...

```
import cv2
import os
import requests

image_path = "snapshot.jpeg"

cam = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cam.isOpened():
    raise IOError("Cannot open webcam")

# Capture a frame
ret, frame = cam.read()

# Check if frame is captured successfully
if not ret:
    raise IOError("Cannot read frame")

# Save the frame as an image
cv2.imwrite(image_path, frame)

# Release the webcam
cam.release()

print("Snapshot saved as snapshot.jpeg")

url = 'http://localhost:3000/api/image'
response = requests.post(url, files={'file': open(image_path, 'rb')})
print(response.json())
```

#### How would you use this?

Here are a few examples of how you could use this embedded API server:

Custom Applications:
A custom app running on the same Linux device can interact with the model using an HTTP client, simplifying the integration process.

IoT Devices:
Small IoT devices with an HTTP client in the firmware can send data to the inference server (the runner) in the local network, get results, and leverage powerful ML models without the need for local model storage and inference.

Web Applications:
Web applications can interact with the model running on the Linux device using the HTTP client, enabling powerful ML models in web applications without the need for cloud services.

Mobile Applications:
Mobile applications can interact with the model running on the Linux device using the HTTP client, enabling powerful ML models in mobile applications without the need for cloud services.

### Summary

The impulse runner is a powerful tool that allows you to run your impulse on your development board and interact with it using an embedded API server. This feature is useful for custom applications, IoT devices, web applications, and mobile applications that need to interact with the model running on the Linux device.

For more information on the impulse runner, or to discuss how you may use this please reach us on the [Forum](https://forum.edgeimpulse.com/)


Built with [Mintlify](https://mintlify.com).