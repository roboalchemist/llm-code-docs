# Source: https://docs.portainer.io/2.33-lts/user/docker/containers/attach-volume.md

# Source: https://docs.portainer.io/sts/user/docker/containers/attach-volume.md

# Source: https://docs.portainer.io/user/docker/containers/attach-volume.md

# Attach a volume to a container

{% hint style="danger" %}
This article explains how to attach a new [volume](https://docs.portainer.io/user/docker/volumes) to a running container. This operation destroys the running container and starts a new one with the volume attached.

**Always back up your data before running this operation.**
{% endhint %}

From the menu select **Containers**, select the container that you want to attach a volume to, then click **Duplicate/Edit**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Fiox1VcQk3XAgpqD2fPi/duplicate-container.gif" alt=""><figcaption></figcaption></figure>

Scroll down to **Advanced container settings**. Click **Volumes** then click **map additional volume**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/gF23qomNVcMaBMnqREAc/2.15-docker_containers_container_add_volumes.png" alt=""><figcaption></figcaption></figure>

In the **container** field enter the path. In the **volume** field enter the volume to attach to the container.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/J6gBvWsLsbqwugbbnhZR/2.15-docker_containers_container_adv_volume_mapping.png" alt=""><figcaption></figcaption></figure>

When you're ready, click **Deploy the container**. When the confirmation message appears, click **Replace**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/PNcWAKjVcQJfFcPI2LGU/2.15-container-edit-confirm.png" alt=""><figcaption></figcaption></figure>
