# Source: https://docs.portainer.io/2.33-lts/user/docker/containers/ownership.md

# Source: https://docs.portainer.io/sts/user/docker/containers/ownership.md

# Source: https://docs.portainer.io/user/docker/containers/ownership.md

# Change container ownership

Portainer allows you to limit container management to specific teams or users.

From the menu select **Containers** then select the container whose ownership you want to change.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/h36vzbAMEpXlvNaz8DTe/Container-change-ownership.gif" alt=""><figcaption></figcaption></figure>

Under the **Access control** section tick the **Change ownership** checkbox then select the new ownership type, using the table below as a guide.

| Ownership Type | Overview                                                                                                                                |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Administrators | Only Portainer administrators can manage the container.                                                                                 |
| Restricted     | Only teams or users you specify can manage the container.                                                                               |
| Public         | Anyone who has [access to the environment](https://docs.portainer.io/user/docker/containers/broken-reference) can manage the container. |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/5h0Zm4WMylPG537QuneC/2.15-docker_containers_container_access_control.png" alt=""><figcaption></figcaption></figure>

When you've made your selection, click **Update ownership**. When the confirmation message appears, click **Change ownership**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/K7hkzzDAICQpipNsgODq/2.15-container-ownership-confirm.png" alt=""><figcaption></figcaption></figure>
