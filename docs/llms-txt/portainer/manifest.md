# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/networking/ingresses/manifest.md

# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/applications/manifest.md

# Source: https://docs.portainer.io/sts/user/kubernetes/networking/ingresses/manifest.md

# Source: https://docs.portainer.io/sts/user/kubernetes/applications/manifest.md

# Source: https://docs.portainer.io/user/kubernetes/networking/ingresses/manifest.md

# Source: https://docs.portainer.io/user/kubernetes/applications/manifest.md

# Add a new application using code

There are two ways to add a new application: [manually by using a form](https://docs.portainer.io/user/kubernetes/applications/add) or automatically by using code. This article explains how to add an application using code.

{% hint style="info" %}
Creating from code isn't just for applications - you can also deploy namespaces, ingresses, ConfigMaps, secrets, volumes and more using code.
{% endhint %}

From the menu, select **Applications** and click **Create from code**. Next, choose whether you want to deploy your application using a **Manifest** or a **Helm chart**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/ttIG27Wy8236Yr6UdMR9/2.35-K8-deploy-from-code.gif" alt=""><figcaption></figcaption></figure>

{% content-ref url="manifest/create" %}
[create](https://docs.portainer.io/user/kubernetes/applications/manifest/create)
{% endcontent-ref %}

{% content-ref url="manifest/helm" %}
[helm](https://docs.portainer.io/user/kubernetes/applications/manifest/helm)
{% endcontent-ref %}
