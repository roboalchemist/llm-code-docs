# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/device-manager/setting-up/add-a-stream.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/device-manager/settoappu/add-a-stream.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/device-manager/setting-up/add-a-stream.md

# Source: https://docs.roboflow.com/deploy/device-manager/setting-up/add-a-stream.md

# Add a Stream

To run a Workflow on your edge device managed by Deployment Manager, you need to add a Stream. A Stream accepts a camera feed as an input and runs the data from the camera on a chosen Workflow.

To add a Stream, you will need:

* A device set up with Deployment Manager.
* A camera available to the device
* A Workflow that you want to deploy on your device.

Streams can read cameras configured via:

* An RTSP stream, or;
* A webcam plugged directly into your edge device via USB
* An ethernet camera, like a Basler or Lucid camera, plugged directly into your device or available on the same switch (for advanced users)

Adding a Stream has three steps:

1. Add camera information
2. Choose a workflow.
3. Review configuration.

### Add Camera Information

To add a Stream, click on a Device you have registered with Deployment Manager from your dashboard, then click "Add Stream":

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-3c9a7e1c8fa465d860c0c25a35c77e1daa1c5cad%2FScreenshot%202025-06-03%20at%2013.30.40.png?alt=media" alt=""><figcaption></figcaption></figure>

A window will then appear in which you can configure your Stream:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FM5HuvVUT4JIV6KZ67YSB%2FScreenshot%202026-01-07%20at%204.43.56%E2%80%AFPM.png?alt=media&#x26;token=2963f453-30a7-4cdb-bd3b-bc8c9b011437" alt="" width="375"><figcaption></figcaption></figure>

In this window, fill out:

1. The name for your Stream.
2. The video source. This can be either an RTSP URL, or the ID of a camera plugged into your device. If you have only one camera plugged into your device, this ID will likely be 0.
3. Select a Workflow to run on the stream

Once you have filled out this information, click "Create Stream" to proceed to set up a Workflow with your Stream. Initial set up of a new stream can take several minutes as the device downloads the workflow and any associated model weights. Eventually, the Stream will appear in your list of Streams:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FqDV8LAYmYq5p9K9F1XxS%2FScreenshot%202026-01-07%20at%205.07.17%E2%80%AFPM.png?alt=media&#x26;token=07fdcaac-a217-4f38-b3cc-eee7a9dea0db" alt=""><figcaption></figcaption></figure>

When you first add the Stream, the status will show that your Stream is "Provisioning". Once your Workflow is downloaded to your device and is running, the status of your Stream will update to "Running".

When the stream status is "Running", this means:

1. Your Workflow is running on your device.
2. You can view frames and logs from your Stream.
