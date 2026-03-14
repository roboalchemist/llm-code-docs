# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/networking/services.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/services.md

# Source: https://docs.portainer.io/sts/user/kubernetes/networking/services.md

# Source: https://docs.portainer.io/sts/user/docker/services.md

# Source: https://docs.portainer.io/user/kubernetes/networking/services.md

# Source: https://docs.portainer.io/user/docker/services.md

# Services

{% hint style="info" %}
The **Services** menu is only available to Docker Swarm endpoints.
{% endhint %}

A service consists of an image definition and container configuration as well as instructions on how those containers will be deployed across a Swarm cluster.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/gq3I1TkB0RO9cTvF4yap/2.20-services-list.png" alt=""><figcaption></figcaption></figure>

When the [new image indicator](https://docs.portainer.io/user/swarm/setup#other) feature is enabled, the **Images up to date** column indicates whether the local images in the service are up to date, with a green tick indicating they are up to date and an orange cross indicating that there is a newer version of an image available at the remote registry. A grey hyphen indicates Portainer was unable to determine whether there is an update available for the images.

You can click the **Reload image indicators** button to recheck the images for all your services for updates, or to recheck a single service's images you can click the image indicator icon for that service.

For more on how this works, have a look at [this article](https://docs.portainer.io/faqs/troubleshooting/stacks-deployments-and-updates/how-does-the-image-update-notification-icon-work).

{% content-ref url="services/add" %}
[add](https://docs.portainer.io/user/docker/services/add)
{% endcontent-ref %}

{% content-ref url="services/configure" %}
[configure](https://docs.portainer.io/user/docker/services/configure)
{% endcontent-ref %}

Once a service has been created you can scale it to meet your needs, as well as view individual task status and logs.

{% content-ref url="services/scale" %}
[scale](https://docs.portainer.io/user/docker/services/scale)
{% endcontent-ref %}

{% content-ref url="services/tasks" %}
[tasks](https://docs.portainer.io/user/docker/services/tasks)
{% endcontent-ref %}

{% content-ref url="services/logs" %}
[logs](https://docs.portainer.io/user/docker/services/logs)
{% endcontent-ref %}

If you need to undo some changes to a service, you can roll it back.

{% content-ref url="services/rollback" %}
[rollback](https://docs.portainer.io/user/docker/services/rollback)
{% endcontent-ref %}

You can also configure webhooks for your services.

{% content-ref url="services/webhooks" %}
[webhooks](https://docs.portainer.io/user/docker/services/webhooks)
{% endcontent-ref %}
