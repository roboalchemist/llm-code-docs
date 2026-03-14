# Source: https://docs.portainer.io/2.33-lts/admin/environments/add/kaas.md

# Source: https://docs.portainer.io/sts/admin/environments/add/kaas.md

# Source: https://docs.portainer.io/admin/environments/add/kaas.md

# Provision KaaS Cluster

{% hint style="danger" %}
Provisioning a KaaS environment from Portainer is deprecated and will be removed in a future release. You will still be able to use any Kubernetes clusters provisioned using this method but will no longer have access to any of the KaaS-specific management functionality.
{% endhint %}

Portainer supports the provisioning of new Kubernetes environments on select cloud providers directly from within the interface, allowing you to spin up a new cloud Kubernetes environment and deploy the Portainer Agent with a few clicks.

{% hint style="info" %}
This feature is only available in [Portainer Business Edition](https://www.portainer.io/business-upsell?from=kaas-provisioning).
{% endhint %}

To get started, from the menu expand **Environment-related**, click **Environments**, then click **Add environment**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/bWERa8LPxJXdwb33Awvh/Add-env-new.gif" alt=""><figcaption></figcaption></figure>

From the wizard select the **Provision KaaS Cluster** option and click **Start Wizard**. Then, select your provider. We currently support the following providers:

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Civo</strong></td><td>Civo Kubernetes</td><td></td><td><a href="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/5bw5dhQhxiSDBsXfE9fD/card-civo-large.png">card-civo-large.png</a></td><td><a href="kaas/civo">civo</a></td></tr><tr><td><strong>Akamai Connected Cloud</strong></td><td>Linode Kubernetes Engine (LKE)</td><td></td><td><a href="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/TNYqbjlu6Mai5NhHydjG/akamai-logo-circle-tile.png">akamai-logo-circle-tile.png</a></td><td><a href="kaas/linode">linode</a></td></tr><tr><td><strong>DigitalOcean</strong></td><td>DigitalOcean Kubernetes (DOKS)</td><td></td><td><a href="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/wYEnXE0ncONnst2gynkY/card-digitalocean-large.png">card-digitalocean-large.png</a></td><td><a href="kaas/digitalocean">digitalocean</a></td></tr><tr><td><strong>Google Cloud</strong></td><td>Google Kubernetes Engine (GKE)</td><td></td><td><a href="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/yBqXaOoTW0Qitf4EiWtY/card-googlecloud-large.png">card-googlecloud-large.png</a></td><td><a href="kaas/gke">gke</a></td></tr><tr><td><strong>Amazon Web Services (AWS)</strong></td><td>Elastic Kubernetes Service (EKS)</td><td></td><td><a href="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/dT7A0XugyZnRy57r5uKa/card-aws-large.png">card-aws-large.png</a></td><td><a href="kaas/eks">eks</a></td></tr><tr><td><strong>Microsoft Azure</strong></td><td>Azure Kubernetes Service (AKS)</td><td></td><td><a href="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/xDahf170ItnIVCIOSuez/card-azure-large.png">card-azure-large.png</a></td><td><a href="kaas/aks">aks</a></td></tr></tbody></table>
