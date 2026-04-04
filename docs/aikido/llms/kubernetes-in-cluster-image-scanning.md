# Source: https://help.aikido.dev/cloud-scanning/kubernetes-cluster-scanning/kubernetes-in-cluster-image-scanning.md

# Kubernetes In-Cluster Image Scanning

{% hint style="info" %}
This functionality is available only for **Pro** and **Advanced** plans. **Contact us** via chat for more information.
{% endhint %}

The Aikido Kubernetes integration supports scanning container images in your Kubernetes clusters without connecting the container registry to Aikido.

## Benefits of In-Cluster Image Scanning

* **Complete coverage** of all images deployed on a cluster, including public images.
* **Real-time scanning**: whenever a pod is launched with a new image, Aikido scans it, and any findings end up in your Aikido feed within minutes.
* **Images never leave your environments**: the Aikido agent only reports SBOMs back to the platform.
* **Less bandwidth**: the Aikido agent first tries to use images cached on the Kubernetes nodes, falling back to pulling them from the registry only if it cannot find or access them. This aspect is especially relevant for organizations using container registries that charge based on traffic.

## Getting Started

You can enable image scanning during the Kubernetes cluster onboarding

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F2gic5wkh5XOSYjHKET7s%2Fimage.png?alt=media&#x26;token=6fe4bc81-25df-4746-8731-27ddd3a1f09b" alt="Aikido Kubernetes cluster onboarding with image scanning enabled" width="375"><figcaption><p>Kubernetes cluster onboarding with image scanning enabled</p></figcaption></figure>

It will also require setting the `sbomCollector.enabled=true` value when installing the Helm chart.

Once running, you will see the images in Aikido on [the containers page](https://app.aikido.dev/containers).

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FyqzTpPY6a9KeSXYaisp4%2Fimage.png?alt=media&#x26;token=81ca7599-ef79-4723-b199-e519fd74461d" alt="Container images reported via the in-cluster Kubernetes scanning"><figcaption><p>Containers reported in Aikido</p></figcaption></figure>

### How Images Are Pulled

The agent (aka the SBOM collector) will attempt to pull images from the local node cache (this is why, by default, it runs as a DaemonSet as root user, allowing it to mount the containerd and Docker sockets).

If the SBOM collector cannot find the images from the node cache (or cannot mount the runtime sockets), it pulls the images from the corresponding registry. For accessing private registries, it supports most authorization mechanisms (node IAM role, imagePullSecrets, workload identity). For more details and how to configure access (where necessary), see [the Helm chart README](https://github.com/AikidoSec/helm-charts?tab=readme-ov-file#in-cluster-image-scanning).

{% hint style="info" %}
**SBOM Collector Secrets Access**

By default, the SBOM collector has access to all secrets from the cluster. This is strictly to allow access when `imagePullSecret` is used. You can [specify the name of the secrets](https://github.com/AikidoSec/helm-charts/blob/main/kubernetes-agent/values.yaml#L75) containing the registry access credentials, thus minimizing the access granted to the SBOM collector.
{% endhint %}

## FAQs

* **What happens when I deploy a new version/tag of an image?**

As you update your workloads, Aikido automatically detects the newly deployed image versions and updates the corresponding containers in the platform. Each workload is correlated to its deployed image, so when a workload moves from `busybox:1.32` to `busybox:1.33`, Aikido reflects that change and scans the new version accordingly.

* **Does this form of scanning benefit from the other container-related features Aikido offers?**

Yes. Images scanned using the in-cluster scanning benefit from all the features offered by Aikido, such as noise reduction, linking to repos, AutoFix, and ELS.

* **Can I ignore specific images?**

The in-cluster scanning will respect the excluded namespaces you set during the cluster onboarding. If you need to exclude specific images from a scanned namespace, we recommend [deactivating the container in Aikido](https://app.aikido.dev/settings/container-image-registry).
