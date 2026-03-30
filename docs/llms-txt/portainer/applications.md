# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/applications.md

# Source: https://docs.portainer.io/sts/user/kubernetes/applications.md

# Source: https://docs.portainer.io/user/kubernetes/applications.md

# Applications

In Kubernetes, an application is a collection of configuration settings and variables required to run your app. This may consist of a single container or multiple containers with complex interoperability.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/2Ypbcix4AApwyeOy5nRD/2.35-kubernetes-applications-list.png" alt=""><figcaption></figcaption></figure>

You can filter the list of applications by namespace using the **Namespace** dropdown.

Portainer lets you add applications either using a form or through code (for example a manifest or a Helm chart):

{% content-ref url="applications/add" %}
[add](https://docs.portainer.io/user/kubernetes/applications/add)
{% endcontent-ref %}

{% content-ref url="applications/manifest" %}
[manifest](https://docs.portainer.io/user/kubernetes/applications/manifest)
{% endcontent-ref %}

You can also inspect a running application:

{% content-ref url="applications/inspect" %}
[inspect](https://docs.portainer.io/user/kubernetes/applications/inspect)
{% endcontent-ref %}

{% content-ref url="applications/inspect-helm" %}
[inspect-helm](https://docs.portainer.io/user/kubernetes/applications/inspect-helm)
{% endcontent-ref %}

Applications can be edited, webhooks can be configured and volumes can be detached:

{% content-ref url="applications/edit" %}
[edit](https://docs.portainer.io/user/kubernetes/applications/edit)
{% endcontent-ref %}

{% content-ref url="applications/edit-helm" %}
[edit-helm](https://docs.portainer.io/user/kubernetes/applications/edit-helm)
{% endcontent-ref %}

{% content-ref url="applications/webhooks" %}
[webhooks](https://docs.portainer.io/user/kubernetes/applications/webhooks)
{% endcontent-ref %}

{% content-ref url="applications/detach-volume" %}
[detach-volume](https://docs.portainer.io/user/kubernetes/applications/detach-volume)
{% endcontent-ref %}

If you no longer require an application, it can be removed:

{% content-ref url="applications/remove" %}
[remove](https://docs.portainer.io/user/kubernetes/applications/remove)
{% endcontent-ref %}
