# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/device-manager/setting-up/add-a-device.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/device-manager/settoappu/add-a-device.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/device-manager/setting-up/add-a-device.md

# Source: https://docs.roboflow.com/deploy/device-manager/setting-up/add-a-device.md

# Add a Device

To deploy a Workflow with Deployment Manager, you first need to add a device to your Roboflow account.

Adding a device will:

* Install Roboflow Inference, our edge computer vision inference server, and all required dependencies, including Docker.
* Register the device so it can be monitored from your Roboflow account.

:warning: Before proceeding, we strongly recommend you review our [hardware-requirements](https://docs.roboflow.com/deploy/device-manager/setting-up/hardware-requirements "mention") for supported devices.

You can add a new device from the "Deployments" page

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fh4nRF5KZ6Gdqraj1HTdt%2FInstall.gif?alt=media&#x26;token=819a90ff-0296-437e-bb36-c2063c91a7bd" alt=""><figcaption></figcaption></figure>

Execute the command provided after you create your device on a terminal on your device. This command will set up Inference on your system and register your device with the Roboflow dashboard. Your edge device will need an internet connection to run this command.\
\
Congrats! Roboflow's Deployment Manager is now running on your machine. The next step is configuring a stream on the device that runs your computer vision workflow.

{% hint style="info" %}
If you have a corporate firewall in place that applies to your edge hardware, contact your account manager for guidance on how to ensure the installation process runs successfully. You may need to whitelist Roboflow's device management domains, which are <https://api.roboflow.com> and <https://repo.roboflow.com>.
{% endhint %}
