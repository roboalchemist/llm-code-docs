# Source: https://docs.portainer.io/2.33-lts/user/aci/dashboard.md

# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/dashboard.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/dashboard.md

# Source: https://docs.portainer.io/sts/user/aci/dashboard.md

# Source: https://docs.portainer.io/sts/user/kubernetes/dashboard.md

# Source: https://docs.portainer.io/sts/user/docker/dashboard.md

# Source: https://docs.portainer.io/user/aci/dashboard.md

# Source: https://docs.portainer.io/user/kubernetes/dashboard.md

# Source: https://docs.portainer.io/user/docker/dashboard.md

# Dashboard

The Docker/Swarm dashboard summarizes your Docker Standalone or Docker Swarm environment and shows the components that make up the environment.&#x20;

## Environment info

{% hint style="info" %}
This section is visible only to Docker Standalone and Podman environments.
{% endhint %}

This section shows the environment name, its URL and port along with any [tags](https://docs.portainer.io/admin/environments/tags#tagging-an-environment). You can also see the number of CPU cores (and their available memory), the Docker/Podman version, and whether or not the Portainer Agent is installed.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/aO9bH5mkOTmYJ7nWHolQ/2.15-docker-standalone-dashboard.png" alt=""><figcaption></figcaption></figure>

## Cluster information

{% hint style="info" %}
This section is visible only to Docker Swarm environments.
{% endhint %}

This section shows how many nodes are in the cluster and a link to the [cluster visualizer](https://docs.portainer.io/user/docker/swarm/cluster-visualizer).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/yIncfFFEkravONKFMOlQ/2.15-docker-dashboard-swarm.png" alt=""><figcaption></figcaption></figure>

## Summary tiles

The remaining dashboard is made up of tiles showing the number of [stacks](https://docs.portainer.io/user/docker/stacks), [services](https://docs.portainer.io/user/docker/services) (for Docker Swarm), [containers](https://docs.portainer.io/user/docker/containers) (including health and running-status metrics), [images](https://docs.portainer.io/user/docker/images) (and how much disk space they consume), [volumes](https://docs.portainer.io/user/docker/volumes) and [networks](https://docs.portainer.io/user/docker/networks), and GPUs (if enabled).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/xtWJ9ReVFkGotkWwgnZf/2.15-docker-dashboard-tiles.png" alt=""><figcaption></figcaption></figure>
