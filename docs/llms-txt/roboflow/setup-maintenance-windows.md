# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/device-manager/setting-up/setup-maintenance-windows.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/device-manager/setting-up/setup-maintenance-windows.md

# Source: https://docs.roboflow.com/deploy/device-manager/setting-up/setup-maintenance-windows.md

# Setup Maintenance Windows

You can schedule when device updates and configuration changes are applied. Maintenance windows help you control disruptions by defining specific time periods for automatic updates, keeping your production devices running smoothly during critical hours.

By default, devices have no maintenance windows and all updates are applied immediately.

#### Set up a Maintenance Window

To set up a maintenance window, go to a specific device's dashboard in Deployment Manager. Go to the options menu on the top right and click on "Maintenance Windows".

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FULOXHZyuL5GEDGAnTkgf%2FScreenshot%202026-01-08%20at%2012.19.52%E2%80%AFPM.png?alt=media&#x26;token=a6ae3546-dc3b-4b0c-aa81-3761daa075a7" alt="" width="151"><figcaption></figcaption></figure>

You can then define maintenance windows for each device based on your operational needs. Choose specific days and times when updates can safely be applied.

Key Options:

* **Timezone** — Set the device's local timezone for accurate scheduling
* **Per-day scheduling** — Configure different windows for each day of the week
* **Same time for all days** — Use a single schedule across multiple days
* **Apply updates immediately** — Bypass maintenance windows when needed&#x20;

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FdXAgj1s498azMKSp2S8G%2FScreenshot%202026-01-08%20at%2012.21.00%E2%80%AFPM.png?alt=media&#x26;token=24ddac74-2aa0-451a-9d4c-6766c956668e" alt="" width="375"><figcaption></figcaption></figure>

#### Updates Outside of Mainenance Windows

Even if a maintenance window is set, users with access to the Roboflow Deployment Manager in the cloud can still choose to override the maintenance window and apply updates immediately if they so choose.
