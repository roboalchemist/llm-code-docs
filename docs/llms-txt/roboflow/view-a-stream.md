# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/device-manager/monitoring/view-a-stream.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/device-manager/monitaringu/view-a-stream.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/device-manager/monitoring/view-a-stream.md

# Source: https://docs.roboflow.com/deploy/device-manager/monitoring/view-a-stream.md

# View a Stream

A Stream is a video feed on which a Workflow is running. You can view a Stream from the Streams list from the Deployment Manager dashboard.

Click "Deployments" in the left sidebar, then "Edge Devices", then choose the Device where your stream is running. Then, select the Stream you want to view from your list of Streams:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2F8nF2e31QjQTWvqVNCAqq%2FScreenshot%202026-01-07%20at%205.07.17%E2%80%AFPM.png?alt=media&#x26;token=7d2335e8-030b-4ea1-bb90-29c68fa44c82" alt=""><figcaption></figcaption></figure>

Once you select a Stream, you will be able to see:

* The status of your Stream.
* A recent frame from your Stream
* Information about the Workflow running on the Stream.

Here is an example showing a frame from a Stream:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FZaAH22RZI5EK1MVMMnl7%2FScreenshot%202026-01-07%20at%205.09.36%E2%80%AFPM.png?alt=media&#x26;token=b7888862-dc12-4466-b96d-7b384c119483" alt=""><figcaption></figcaption></figure>

The latest frame feature gives you samples of recent frames to see the results of your computer vision application. Note that this is not a live video as we prioritize compute efficiency for the computer vision model running on device.&#x20;

You can scroll down to see the Workflow your device is running, the parameters used to set up the Workflow, and your Stream configuration.&#x20;

:information\_source: By default, editing your workflow will automatically update the version running on your device. This means you will see your computer application go offline momentarily as we the new weights and workflow definition are downloaded

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FmNPXd5ANZ8hWMlrM0nQr%2FScreenshot%202026-01-08%20at%2010.01.31%E2%80%AFAM.png?alt=media&#x26;token=57bf2adc-9489-479f-bbc7-ef8fb53a8fb0" alt=""><figcaption><p><em>Information about the Workflow running on a device.</em></p></figcaption></figure>
