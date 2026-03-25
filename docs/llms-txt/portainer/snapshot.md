# Source: https://docs.portainer.io/2.33-lts/user/home/snapshot.md

# Source: https://docs.portainer.io/sts/user/home/snapshot.md

# Source: https://docs.portainer.io/user/home/snapshot.md

# Snapshot browsing

Snapshot browsing allows the ability to run remote commands on your Edge devices that are in Async mode. You can browse your device as well as run commands like start, stop, restart, and delete on your containers, stacks and volumes.

To browse your Edge device, on the [home page](https://docs.portainer.io/user/home) locate your Edge device and click the **Browse snapshot** button.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/fUQvuFYZHOMqVfPqKuU2/2.33-home-edge-async-tile.png" alt=""><figcaption></figcaption></figure>

You will be directed to the dashboard for the Edge device, with a **Browsing snapshot** drop down that details the last updated and next updated date, how often the snapshots are taken and the environment status.  You can refer to the [deployment sync options](https://docs.portainer.io/admin/settings/edge#deployment-sync-options)for more details.&#x20;

{% hint style="warning" %}
The information displayed in Portainer for your Edge device is up to date as of the time the latest snapshot (as indicated in the dropdown) was taken. Depending on the [age of the snapshot](https://docs.portainer.io/admin/settings/edge#deployment-sync-options) and the environment, this may not be an up to date representation of the current state of the device, so bear this in mind when taking actions on the device.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/2bTtUQ3qFSGVcWJW6w6c/2.33-snapshot-browse-details.png" alt=""><figcaption></figcaption></figure>

From here, you can browse the device as you would a regular environment.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/V9RRFgtwCIzxYgBhFT07/2.33-snapshot-browse.gif" alt=""><figcaption></figcaption></figure>
