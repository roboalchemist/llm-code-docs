# Source: https://docs.portainer.io/2.33-lts/user/aci/containers/details.md

# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/cluster/details.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/swarm/details.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/host/details.md

# Source: https://docs.portainer.io/sts/user/aci/containers/details.md

# Source: https://docs.portainer.io/sts/user/kubernetes/cluster/details.md

# Source: https://docs.portainer.io/sts/user/docker/swarm/details.md

# Source: https://docs.portainer.io/sts/user/docker/host/details.md

# Source: https://docs.portainer.io/user/aci/containers/details.md

# Source: https://docs.portainer.io/user/kubernetes/cluster/details.md

# Source: https://docs.portainer.io/user/docker/swarm/details.md

# Source: https://docs.portainer.io/user/docker/host/details.md

# Details

This page provides information about the Docker host for the selected environment. The page is split into the following sections: Host Details, Engine Details, and (if enabled) PCI Devices and Physical Disks.

{% hint style="info" %}
This page is only available on Docker Standalone environments.
{% endhint %}

## Host Details

This section describes the host's basic configuration, including the hostname, OS information, kernel version, total CPU and memory. If the environment has the Portainer Agent installed, [host management features](https://docs.portainer.io/user/docker/setup#enable-host-management-features) are enabled, and a `/host` mount has been configured, you can also browse the host file system from here.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/nBXwZt3oS0nrpaOyh8HU/2.15-docker-host-details.png" alt=""><figcaption></figcaption></figure>

## Engine Details

Learn more about the Docker or Podman engine running on your environment, including the Docker/Podman version, the root directory, storage and logging drivers and available volume and network plugins.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/YbhSG7pw2uOylJigTlXa/2.15-docker-host-engine.png" alt=""><figcaption></figcaption></figure>

## PCI Devices and Physical Disks

These sections list the available PCI devices and physical disks on the host.

{% hint style="info" %}
These sections are only visible when [host management features](https://docs.portainer.io/user/docker/setup#enable-host-management-features) are enabled for the environment.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Gso1CHegGfU09jkAeKaC/2.15-docker-host-pci.png" alt=""><figcaption></figcaption></figure>
