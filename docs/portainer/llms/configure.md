# Source: https://docs.portainer.io/2.33-lts/user/docker/services/configure.md

# Source: https://docs.portainer.io/sts/user/docker/services/configure.md

# Source: https://docs.portainer.io/user/docker/services/configure.md

# Configure service options

From the menu select **Services** then select the service you want to configure.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/mMkgb1eNe712DRVqFgWl/Select-service-new.gif" alt=""><figcaption></figcaption></figure>

## Service details

In this section you can:

* View a summary of the details about the service.
* Configure the number of replicas.
* Toggle the [service webhook](https://docs.portainer.io/user/docker/services/webhooks) on or off.
* View the [service logs](https://docs.portainer.io/user/docker/services/logs).
* Update, [roll back](https://docs.portainer.io/user/docker/services/rollback) or delete the service.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/LQMFpqG9ZZxRu5IcraZJ/2.15-docker_services_service_details.png" alt=""><figcaption></figcaption></figure>

## Container specification configuration options

### Change container image

Here you can replace the container image with a different image. Select the registry, enter the image name, then click **Apply changes**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/u5gAGmRI2Owopjd9klQn/2.15-docker_services_change_container_image.png" alt=""><figcaption></figcaption></figure>

### Environment variables

It's best to set environment variables when you [create a container](https://docs.portainer.io/user/docker/containers/add) and before deployment. You can still set or edit these variables after deployment if you wish.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/erfr6kwYSSv0Q1Q4nCpg/2.15-docker_services_service_env_var.png" alt=""><figcaption></figcaption></figure>

### Container labels

Labels give you a way to record information about a container, such as the way it's configured. Labels can also be used by Portainer to [hide containers from the interface](https://docs.portainer.io/admin/settings#hidden-containers).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/aM3LlpXN5hnCr2SJv8Xm/2.15-docker_services_service_container_labels.png" alt=""><figcaption></figcaption></figure>

### Mounts

You have the option to either mount or bind volumes in Portainer, and you can also make them read only. To add a mount, first select either **Volume** or **Bind** from the **Type** dropdown.

#### For volume mounts

Select the volume from the **Source** dropdown, enter the container path in the **Target** field tick **Read only** if required then click **Apply changes**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/7RtHNb8ly3ORacpxrgsC/2.15-docker_services_service_mounts_volume.png" alt=""><figcaption></figcaption></figure>

#### For bind mounts

Enter the source path in the **Source** field, enter the container path in the **Target** field, tick **Read only** if required then click **Apply changes**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/jWeQrwLxv3keiaew9gtT/2.15-docker_services_service_mounts_bind.png" alt=""><figcaption></figcaption></figure>

## Networks & ports configuration options

### Networks

You can define one or more networks for a service either before or after deployment. Simply select the network from the dropdown then click **Apply changes**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/RLWSVRbzEA4nhRdea5zF/2.15-docker_services_service_networks.png" alt=""><figcaption></figcaption></figure>

### Published ports

Use this setting to publish ports so they can access a container from outside of the host. You can either add new ports or update existing ports.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/sgCORXo5MLTyTMGrNdAm/2.15-docker_services_service_published_ports.png" alt=""><figcaption></figcaption></figure>

### Hosts file entries

Lets you manually specify a hostname or URL and associate the URL to an internal or external IP address.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Bs2ZOOi6U9l9DNsOsB1E/2.15-docker_services_service_host_entries.png" alt=""><figcaption></figcaption></figure>

## Service specification settings

### Resource limits and reservations

Sets limits on resource utilization, such as memory, CPU reservation and CPU limit.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/pQIalKA2xqDzhATSRJlL/2.15-docker_services_service_resource_limits.png" alt=""><figcaption></figcaption></figure>

### Placement constraints

Use placement constraints to control which nodes a service can be assigned to.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/qXBgwY3l2uBemJCnmWNd/2.15-docker_services_service_placement_constraint.png" alt=""><figcaption></figcaption></figure>

### Placement preferences

While placement constraints limit the nodes a service can run on, placement preferences attempt to place tasks on appropriate nodes in an algorithmic way (by default they are spread evenly).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/iJ5kRiSBfb1TemgkZit3/2.15-docker_services_service_placement_pref.png" alt=""><figcaption></figcaption></figure>

### Restart policy

Docker's restart policies ensure that linked containers are restarted in the correct order, and control the conditions under which they are restarted:

* **Any**: Restart the container under any conditions (restarted host or Docker daemon).
* **On Failure**: Restart the container if it exits due to an error which manifests as a non-zero exit code.
* **None**: Do not automatically restart the container.

You can also adjust the restart delay, maximum attempts and restart window.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/UNkX0RWmgTmcS59Pb6j3/2.15-docker_services_service_restart_policy.png" alt=""><figcaption></figcaption></figure>

### Update configuration

Updates a service according to the parameters you specify. The parameters specified here are the same as `docker service create` (see [Docker's own documentation](https://docs.docker.com/engine/reference/commandline/service_create/) for more information).

Normally, updating a service will only cause the service’s tasks to be replaced with new ones if a change to the service requires recreating the tasks for it to take effect.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/ydX6lZGK0fzgO29F95zx/2.15-docker_services_service_update_config.png" alt=""><figcaption></figcaption></figure>

### Logging driver

Docker includes logging mechanisms called *logging drivers* that get information from the containers and services you're running. Each Docker daemon has a default logging driver which each container will use, unless you configure them to use a different logging driver.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/RnnTGeo1UxeBK1JbPiKP/2.15-docker_services_service_logging_driver.png" alt=""><figcaption></figcaption></figure>

### Service labels

Lets you add metadata to containers using Docker labels either via an array or a dictionary. We recommend that you use reverse-DNS notation to stop labels from conflicting with those used by other software.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/24fAi88KqASCzShZSik2/2.15-docker_services_service_labels.png" alt=""><figcaption></figcaption></figure>

### Configs

Docker 17.06 introduced Swarm service configs. These allow you to store non-sensitive information such as configuration files outside a service’s image or running containers. This keeps images as generic as possible and removes the need to bind-mount configuration files into containers or use environment variables.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/VnJMX6c7DAXmhzcZ4rIj/2.15-docker_services_service_configs.png" alt=""><figcaption></figcaption></figure>

### Secrets

In the context of Docker Swarm services, a secret is a blob of data such as a password, SSH private key, SSL certificate, or another piece of data that should not be transmitted over a network or stored unencrypted in a Dockerfile or in your application’s source code.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/IwTXYiYPxJubJxkpmtub/2.15-docker_services_service_secrets.png" alt=""><figcaption></figcaption></figure>
