# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/device-manager/making-changes/update-device-configuration.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/device-manager/making-changes/update-device-configuration.md

# Source: https://docs.roboflow.com/deploy/device-manager/making-changes/update-device-configuration.md

# Update Device Configuration

### Configuring Your Deployment

The Configuration page in Deployment Manager lets you manage services running on your device. This guide provides an overview of the key configuration options.

#### Device Settings

You can rename your device or update its timezone. The device name is purely for display in the Deployment Manager user interface and will not break any integrations. The timezone is used to help display logs and coordinate the scheduling other other device actions. We highly recommend you keep this in line with the physical location of the deployment

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FmQHwTiF9QV5aErJosQsq%2FScreenshot%202026-01-13%20at%2011.01.56%E2%80%AFAM.png?alt=media&#x26;token=1fcd7c77-2426-4767-aff1-f650e5aa7bbd" alt="" width="375"><figcaption></figcaption></figure>

#### Updates / Performance Settings

Versions of services can be configured on the tab for each service. Versions are usually updated by the Roboflow team.&#x20;

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FEP1uAKgx5XZukB7zcEfX%2FScreenshot%202026-01-13%20at%2011.02.25%E2%80%AFAM.png?alt=media&#x26;token=e2b59ba0-afda-4ebf-a83c-442aeffc05e4" alt=""><figcaption></figcaption></figure>

**Version indicators:**

* **Green checkmark** — Running the latest version
* **"Update available"** — A newer version exists

**Automatic Updates** — Enable this toggle (available for inference and manager services) to automatically update during your configured maintenance windows.

> **Note:** If your device reports a different version than configured, you'll see a mismatch indicator.

**Enable TensorRT** — Activates TensorRT optimization for faster inference.

***

#### Additional Services

Roboflow also allows you to add preconfigured additional services to your device, like a local event store, a default HMI UI, and an RTSP simulator for testing. Each of these has their own configuration options. You'll be prompted as needed when you try to add each service.&#x20;

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FX0g93AWHZ6brCnrNgYTF%2FScreenshot%202026-01-13%20at%2011.05.00%E2%80%AFAM.png?alt=media&#x26;token=1814c06b-3592-417c-be24-9863609d2748" alt="" width="563"><figcaption></figcaption></figure>
