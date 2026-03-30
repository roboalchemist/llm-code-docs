# Source: https://docs.portainer.io/2.33-lts/admin/registries.md

# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/cluster/registries.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/swarm/registries.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/host/registries.md

# Source: https://docs.portainer.io/sts/admin/registries.md

# Source: https://docs.portainer.io/sts/user/kubernetes/cluster/registries.md

# Source: https://docs.portainer.io/sts/user/docker/swarm/registries.md

# Source: https://docs.portainer.io/sts/user/docker/host/registries.md

# Source: https://docs.portainer.io/admin/registries.md

# Source: https://docs.portainer.io/user/kubernetes/cluster/registries.md

# Source: https://docs.portainer.io/user/docker/swarm/registries.md

# Source: https://docs.portainer.io/user/docker/host/registries.md

# Registries

{% hint style="warning" %}
If access to an environment is being managed by a Docker registry [policy](https://docs.portainer.io/admin/environments/policies), access can not be changed or modified from this view as the policy access takes precedence.&#x20;
{% endhint %}

{% hint style="warning" %}
Registry access assigned here only applies to the selected environment. It is not global.
{% endhint %}

This view lets you manage access to each of the registries that are currently available.

## Adding a new registry

From the menu select **Host**, select **Registries** then click **Add registry**. When the global registries page appears, follow [these instructions](https://docs.portainer.io/admin/registries/add).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/IxgctBwTXvJdb7A2Jp1j/2.15-host-registries-add.gif" alt=""><figcaption></figcaption></figure>

## Managing access

{% hint style="warning" %}
If access to a registry is being managed by a registry [policy](https://docs.portainer.io/admin/environments/policies), access can not be changed or modified from this view as the policy access takes precedence.&#x20;
{% endhint %}

To configure access to a registry, from the menu select **Host** then select **Registries**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/u1rsTbqr1lIlHGeLDoq5/2.15-docker_hosts_registries.gif" alt=""><figcaption></figcaption></figure>

Find the registry you want to manage then select **Manage access**.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/yJ3aJ888XZq3jgyAUsFB/2.15-docker_hosts_registries_manage_access.png" alt=""><figcaption></figcaption></figure>

From the dropdown, select the users or teams that you would like to have access, then click **Create access**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/oHql5sHvQqe0xBvSV3y5/2.15-docker_hosts_registries_access.png" alt=""><figcaption></figcaption></figure>
