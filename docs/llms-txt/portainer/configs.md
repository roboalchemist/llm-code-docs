# Source: https://docs.portainer.io/2.33-lts/user/docker/configs.md

# Source: https://docs.portainer.io/sts/user/docker/configs.md

# Source: https://docs.portainer.io/user/docker/configs.md

# Configs

{% hint style="info" %}
The **Configs** menu is only available to Docker Swarm environments.
{% endhint %}

Docker 17.06 introduced swarm service configs which allow you to store non-sensitive information, such as configuration files, outside a service’s image or running containers. This allows you to keep your images as generic as possible, without the need to bind-mount configuration files into the containers or use environment variables. [Secrets](https://docs.portainer.io/user/docker/secrets) is another option for storing sensitive information.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/eMtUSk9vkBzC4NE3yvEv/2.15-docker_configs_config_list.png" alt=""><figcaption></figcaption></figure>

In Portainer you can add and remove custom configurations for use in deployments.

{% content-ref url="configs/add" %}
[add](https://docs.portainer.io/user/docker/configs/add)
{% endcontent-ref %}

{% content-ref url="configs/remove" %}
[remove](https://docs.portainer.io/user/docker/configs/remove)
{% endcontent-ref %}
