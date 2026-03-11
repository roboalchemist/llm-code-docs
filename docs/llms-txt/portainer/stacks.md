# Source: https://docs.portainer.io/2.33-lts/user/edge/stacks.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/stacks.md

# Source: https://docs.portainer.io/sts/user/edge/stacks.md

# Source: https://docs.portainer.io/sts/user/docker/stacks.md

# Source: https://docs.portainer.io/user/edge/stacks.md

# Source: https://docs.portainer.io/user/docker/stacks.md

# Stacks

A stack is a collection of services, usually related to one application or usage. For example, a WordPress stack definition may include a web server container (such as nginx) and a database container (such as MySQL).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/VxAo6ujlxheJEb0fQPRO/2.20-stacks-list.png" alt=""><figcaption></figcaption></figure>

Within the Stacks list, you’ll see all stacks that have been previously created in the selected environment. If an environment is deleted, any stacks that belonged to it become orphaned. To display any orphaned stacks, click the three dots in the top right corner and select **Show all orphaned stacks**, [the stack will need to be re-associated](https://docs.portainer.io/faqs/troubleshooting/stacks-deployments-and-updates/how-do-i-recover-orphaned-stacks-from-a-previously-deleted-environment) to be fully recovered.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/xVALKOYBQRMNMmbXD1rS/Show-orphaned-stacks-FAQ.png" alt=""><figcaption></figcaption></figure>

When the [new image indicator](https://docs.portainer.io/user/host/setup#other) feature is enabled, the **Images up to date** column indicates whether the local images in the stack are up to date, with a green tick indicating they are up to date and an orange cross indicating that there is a newer version of an image available at the remote registry. A grey hyphen indicates Portainer was unable to determine whether there is an update available for the images.

You can click the **Reload image indicators** button to recheck the images for your stacks for updates, or to recheck a single stack's images you can click the image indicator icon for that stack.

For more on how this works, have a look at [this article](https://docs.portainer.io/faqs/troubleshooting/stacks-deployments-and-updates/how-does-the-image-update-notification-icon-work).

{% content-ref url="stacks/add" %}
[add](https://docs.portainer.io/user/docker/stacks/add)
{% endcontent-ref %}

{% content-ref url="stacks/edit" %}
[edit](https://docs.portainer.io/user/docker/stacks/edit)
{% endcontent-ref %}

{% content-ref url="stacks/template" %}
[template](https://docs.portainer.io/user/docker/stacks/template)
{% endcontent-ref %}

{% content-ref url="stacks/webhooks" %}
[webhooks](https://docs.portainer.io/user/docker/stacks/webhooks)
{% endcontent-ref %}

{% content-ref url="stacks/migrate" %}
[migrate](https://docs.portainer.io/user/docker/stacks/migrate)
{% endcontent-ref %}

{% content-ref url="stacks/remove" %}
[remove](https://docs.portainer.io/user/docker/stacks/remove)
{% endcontent-ref %}
