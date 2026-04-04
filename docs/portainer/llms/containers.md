# Source: https://docs.portainer.io/2.33-lts/user/aci/containers.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/containers.md

# Source: https://docs.portainer.io/sts/user/aci/containers.md

# Source: https://docs.portainer.io/sts/user/docker/containers.md

# Source: https://docs.portainer.io/user/aci/containers.md

# Source: https://docs.portainer.io/user/docker/containers.md

# Containers

Put simply, a container is a runnable instance of an image. Containers do not hold any persistent data and therefore can be destroyed and recreated as needed.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/FH1qkKCEBLU9oR9pms6d/2.20-containers-list.png" alt=""><figcaption></figcaption></figure>

When the [new image indicator](https://docs.portainer.io/user/host/setup#other) feature is enabled, the **Images up to date** column indicates whether the local images in the container are up to date, with a green tick indicating they are up to date and an orange cross indicating that there is a newer version of an image available at the remote registry. A grey hyphen indicates Portainer was unable to determine whether there is an update available for the images.

You can click the reload button next to the search box to recheck the images for all your containers for updates, or to recheck a single container's image you can click the image indicator icon for that container.

For more on how this works, have a look at [this FAQ article](https://docs.portainer.io/faqs/troubleshooting/stacks-deployments-and-updates/how-does-the-image-update-notification-icon-work).

To add a new container, click **Add container**.

{% content-ref url="containers/add" %}
[add](https://docs.portainer.io/user/docker/containers/add)
{% endcontent-ref %}

Once a container has been created you can inspect it, edit or duplicate it, toggle a container webhook, attach volumes, view logs and statistics, edit ownership, and access its console.

{% content-ref url="containers/view" %}
[view](https://docs.portainer.io/user/docker/containers/view)
{% endcontent-ref %}

{% content-ref url="containers/inspect" %}
[inspect](https://docs.portainer.io/user/docker/containers/inspect)
{% endcontent-ref %}

{% content-ref url="containers/edit" %}
[edit](https://docs.portainer.io/user/docker/containers/edit)
{% endcontent-ref %}

{% content-ref url="containers/advanced" %}
[advanced](https://docs.portainer.io/user/docker/containers/advanced)
{% endcontent-ref %}

{% content-ref url="containers/webhooks" %}
[webhooks](https://docs.portainer.io/user/docker/containers/webhooks)
{% endcontent-ref %}

{% content-ref url="containers/attach-volume" %}
[attach-volume](https://docs.portainer.io/user/docker/containers/attach-volume)
{% endcontent-ref %}

{% content-ref url="containers/logs" %}
[logs](https://docs.portainer.io/user/docker/containers/logs)
{% endcontent-ref %}

{% content-ref url="containers/ownership" %}
[ownership](https://docs.portainer.io/user/docker/containers/ownership)
{% endcontent-ref %}

{% content-ref url="containers/stats" %}
[stats](https://docs.portainer.io/user/docker/containers/stats)
{% endcontent-ref %}

{% content-ref url="containers/console" %}
[console](https://docs.portainer.io/user/docker/containers/console)
{% endcontent-ref %}

If you no longer need a container, you can remove it.

{% content-ref url="containers/remove" %}
[remove](https://docs.portainer.io/user/docker/containers/remove)
{% endcontent-ref %}
