# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/networking/ingresses.md

# Source: https://docs.portainer.io/sts/user/kubernetes/networking/ingresses.md

# Source: https://docs.portainer.io/user/kubernetes/networking/ingresses.md

# Ingresses

An **Ingress** in Kubernetes is an API object that provides routing rules to manage external users' access to the services in a Kubernetes cluster, typically via HTTPS/HTTP. With Ingress, you can easily set up rules for routing traffic without creating a bunch of Load Balancers or exposing each service on the node.

To view, edit or create ingresses in your environment, expand **Networking** and select **Ingresses** from the left hand menu.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/tnERuLBwQW2ZHm7BlI5s/Ingresses.gif" alt=""><figcaption></figcaption></figure>

All the Ingresses that a user has access to are listed on this page.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/2bUxvMwyMYwZnWM0vFqk/2.20-kubernetes-networking-ingresses-list.png" alt=""><figcaption></figcaption></figure>

New Ingress objects can be created either manually or through a manifest:

{% content-ref url="ingresses/add" %}
[add](https://docs.portainer.io/user/kubernetes/networking/ingresses/add)
{% endcontent-ref %}

{% content-ref url="ingresses/manifest" %}
[manifest](https://docs.portainer.io/user/kubernetes/networking/ingresses/manifest)
{% endcontent-ref %}

If you no longer require an Ingress, it can be removed:

{% content-ref url="ingresses/remove-an-ingress" %}
[remove-an-ingress](https://docs.portainer.io/user/kubernetes/networking/ingresses/remove-an-ingress)
{% endcontent-ref %}
