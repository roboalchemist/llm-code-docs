# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/device-manager/making-changes/redeploy-deployment-manager.md

# Source: https://docs.roboflow.com/deploy/device-manager/making-changes/redeploy-deployment-manager.md

# Redeploy Deployment Manager

In some cases, you want to redeploy Deployment Manager onto an existing device. This is most common when you find an existing device has become corrupted or you have an unrecoverable hardware failure.&#x20;

Rather than doing any manual work, you can simply redeploy the device and it will fully recover all Roboflow configurations with just one step.&#x20;

:warning: Please ensure that you don't redeploy manager onto a second device while the first device is still operational.

To redeploy onto a new device, visit the Deployment Manager dashboard for that device. Then open the options menu on the top-righ and click on "Redeploy Device"

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fzfc395Dg7MilGGZApAY8%2FScreenshot%202026-01-08%20at%2011.16.35%E2%80%AFAM.png?alt=media&#x26;token=ebbfe3ab-2316-4ab8-a741-4ddfccb588b1" alt="" width="164"><figcaption></figcaption></figure>

Then, click on "Generate Redeploy Command" to get the install script.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FPrfqy0McmWUokdCMy8xo%2FScreenshot%202026-01-08%20at%2011.23.04%E2%80%AFAM.png?alt=media&#x26;token=d68dbabd-9d96-47bf-995c-ce409ea20255" alt="" width="375"><figcaption></figcaption></figure>

Then copy the install script and execute it from a terminal on the device with elevated privileges.&#x20;

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FMMEAsk7iDvN9rnPZxXvN%2FScreenshot%202026-01-08%20at%2011.25.29%E2%80%AFAM.png?alt=media&#x26;token=ce900b81-2fb8-442e-98d1-12a240990bd7" alt="" width="375"><figcaption></figcaption></figure>

:warning: Note that the install script is only active for 10 minutes and then expires. After expiration, you'd have to regenerate the install script.
