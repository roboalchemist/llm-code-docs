# Source: https://docs.portainer.io/2.33-lts/admin/environments/add/kube-create.md

# Source: https://docs.portainer.io/sts/admin/environments/add/kube-create.md

# Source: https://docs.portainer.io/admin/environments/add/kube-create.md

# Create a Kubernetes cluster

With Portainer Business Edition you can create a Kubernetes cluster on your existing infrastructure directly from the Portainer UI.&#x20;

{% hint style="info" %}
Portainer connects to your infrastructure and deploy Kubernetes and the Portainer Agent. You can provide your credentials during the deployment or set them up ahead of time in [Shared credentials](https://docs.portainer.io/admin/settings/credentials).
{% endhint %}

At present, we support deploying Talos Kubernetes via Omni and MicroK8s via SSH:

{% content-ref url="kube-create/omni" %}
[omni](https://docs.portainer.io/admin/environments/add/kube-create/omni)
{% endcontent-ref %}

{% content-ref url="kube-create/microk8s" %}
[microk8s](https://docs.portainer.io/admin/environments/add/kube-create/microk8s)
{% endcontent-ref %}
