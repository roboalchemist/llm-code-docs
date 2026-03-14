# Source: https://docs.portainer.io/2.33-lts/admin/settings/credentials.md

# Source: https://docs.portainer.io/sts/admin/settings/credentials.md

# Source: https://docs.portainer.io/admin/settings/credentials.md

# Shared credentials

In this section you can create and manage credentials that are shared at admin level. Shared Git credentials can be used to connect to Git repositories, while the other shared credentials can be used with our [KaaS provisioning functionality](https://docs.portainer.io/admin/environments/add/kaas) and our Kubernetes provisioning feature.

{% hint style="info" %}
The Shared credentials feature is only available in Portainer Business Edition.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SUSAHrtzDZ9RAZVYAo6b/2.18-settings-sharedcreds.png" alt=""><figcaption></figcaption></figure>

To add a new set of credentials, click the **Add credentials** button.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/vPKq0LyfLPABsTwBwIaf/Screenshot%202025-09-15%20at%2010.30.00%E2%80%AFAM.png" alt=""><figcaption></figcaption></figure>

Portainer currently supports the following credential types:

* [Sidero Omni](https://docs.portainer.io/admin/settings/credentials/omni)
* [Civo](https://docs.portainer.io/admin/settings/credentials/civo)
* [Akamai Connected Cloud](https://docs.portainer.io/admin/settings/credentials/linode)
* [DigitalOcean](https://docs.portainer.io/admin/settings/credentials/digitalocean)
* [Google Cloud](https://docs.portainer.io/admin/settings/credentials/gke)
* [Amazon Web Services (AWS)](https://docs.portainer.io/admin/settings/credentials/eks)
* [Microsoft Azure](https://docs.portainer.io/admin/settings/credentials/aks)
* [SSH](https://docs.portainer.io/admin/settings/credentials/ssh) (for use with Kubernetes cluster deployments)
* [Git](https://docs.portainer.io/admin/settings/credentials/git)

To remove a set of credentials, check the box next to the credentials to remove and click **Remove**.
