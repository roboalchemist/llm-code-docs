# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/device-manager/monitoring/view-device-logs.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/device-manager/monitaringu/view-device-logs.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/device-manager/monitoring/view-device-logs.md

# Source: https://docs.roboflow.com/deploy/device-manager/monitoring/view-device-logs.md

# View Device Logs

In some cases, you may feel like your device is not operating as you intend. Maybe a workflow step is acting in a strange way or you are not seeing it connect to some service on your network. \
\
To help you debug, Roboflow Deployment Manager makes it easy to see logs from Roboflow services running on your device. \
\
:exclamation:The logs page does NOT display all logs from syslog on your system or logs from non-Roboflow services for security purposes.&#x20;

To see your device logs, click on a device in Deployment Manager, then click on the "Logs" tab:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2F5Wm8luYRGlE5VMy2oXyo%2FScreenshot%202026-01-08%20at%2010.15.08%E2%80%AFAM.png?alt=media&#x26;token=09a9d055-5221-4a11-837a-45ee1e482895" alt=""><figcaption></figcaption></figure>

From here you can see the most recent logs as they are streamed up from the device, download logs if you need to send lines to other stakeholders within your company, filter by time range, and filter by specific Roboflow services.&#x20;

#### For Advanced Users

Roboflow Deployment Manager is orchestrated on top of Docker containers that are each different managed as services running on your device. The most common Roboflow services are:<br>

* Inference - This is the service that actually runs your model and workflows
* Manager - This service works in conjunction with the inference service and handles tracking the different streams. It's the service that manages stopping and starting the workflows that are run on the inference service
* RFDM - This is the service that handles downloading the Docker containers on the device as well as tracks, telemetry, logs, and device health. Think of this is the management layer for all the other services.&#x20;
* HMI - If configured, you may see an HMI service that runs the user interface on the device
* Event Store - If configured, you may see an event store service that can store recent vision event data for viewing in the HMI
* Redis - This deploys a Redis DB that is used for caching various telemetry before it's synchronized to Roboflow.
