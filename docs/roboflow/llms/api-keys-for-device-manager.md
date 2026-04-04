# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/device-manager/making-changes/api-keys-for-device-manager.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/device-manager/wou/api-keys-for-device-manager.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/device-manager/making-changes/api-keys-for-device-manager.md

# Source: https://docs.roboflow.com/deploy/device-manager/making-changes/api-keys-for-device-manager.md

# API Keys for Device Manager

When you add a device to Deployment Manager, an API key will be automatically generated. This API key has permissions to access your Workflows and models. The API key can be used by your device to access the Roboflow services required to set up and manage your device.

We recommend using the API keys exclusively for use with one device. You can generate more API keys for other uses (i.e. for uploading data to Roboflow or running inference on a test machine).

You can see automatically generated API keys on the "API Keys" page in your Account Settings:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-6e07960dcad86ec1c2aebf737e5b754bd5bbb0a9%2FScreenshot%202025-06-27%20at%2015.45.47.png?alt=media" alt=""><figcaption></figcaption></figure>

Automatically-generated API keys for use with devices configured with Deployment Manager have the format:

```

Device: [device ID]
```

You can click "View Device" to see the device associated with the key.

When you remove the device from Deployment Manager, its associated key will be automatically revoked.
