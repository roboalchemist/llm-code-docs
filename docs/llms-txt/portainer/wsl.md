# Source: https://docs.portainer.io/2.33-lts/start/install-ce/server/kubernetes/wsl.md

# Source: https://docs.portainer.io/2.33-lts/start/install-ce/server/swarm/wsl.md

# Source: https://docs.portainer.io/2.33-lts/start/install-ce/server/docker/wsl.md

# Source: https://docs.portainer.io/2.33-lts/start/install/server/kubernetes/wsl.md

# Source: https://docs.portainer.io/2.33-lts/start/install/server/swarm/wsl.md

# Source: https://docs.portainer.io/2.33-lts/start/install/server/docker/wsl.md

# Source: https://docs.portainer.io/sts/start/install-ce/server/kubernetes/wsl.md

# Source: https://docs.portainer.io/sts/start/install-ce/server/swarm/wsl.md

# Source: https://docs.portainer.io/sts/start/install-ce/server/docker/wsl.md

# Source: https://docs.portainer.io/sts/start/install/server/kubernetes/wsl.md

# Source: https://docs.portainer.io/sts/start/install/server/swarm/wsl.md

# Source: https://docs.portainer.io/sts/start/install/server/docker/wsl.md

# Source: https://docs.portainer.io/start/install-ce/server/kubernetes/wsl.md

# Source: https://docs.portainer.io/start/install-ce/server/swarm/wsl.md

# Source: https://docs.portainer.io/start/install-ce/server/docker/wsl.md

# Source: https://docs.portainer.io/start/install/server/kubernetes/wsl.md

# Source: https://docs.portainer.io/start/install/server/swarm/wsl.md

# Source: https://docs.portainer.io/start/install/server/docker/wsl.md

# Install Portainer BE with Docker on WSL / Docker Desktop

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/docker/wsl).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server*, and the *Portainer Agent*. Both elements run as lightweight Docker containers on a Docker engine. This document will help you install the Portainer Server container on your Windows environment with WSL and Docker Desktop. To add a new WSL / Docker Desktop environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/docker/agent).

To get started, you will need:

* The latest version of Docker Desktop installed and working.
* Administrator access on the machine that will host your Portainer Server instance.
* Windows Subsystem for Linux (WSL) installed and a Linux distribution selected. For a new installation we recommend WSL2.
* By default, Portainer Server will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.
* A license key for Portainer Business Edition.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* You are accessing Docker via Unix sockets. Alternatively, you can also connect via TCP.
* SELinux is disabled within the Linux distribution used by WSL. If you require SELinux, you will need to pass the `--privileged` flag to Docker when deploying Portainer.
* Docker is running as root. Portainer with rootless Docker has some limitations, and requires additional configuration.

## Deployment

First, create the volume that Portainer Server will use to store its database:

```bash
docker volume create portainer_data
```

Then, download and install the Portainer Server container:

```
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:lts
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-docker-standalone) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

{% hint style="info" %}
If you require HTTP port `9000` open for legacy reasons, add the following to your `docker run` command:

`-p 9000:9000`
{% endhint %}

Portainer Server has now been installed. You can check to see whether the Portainer Server container has started by running `docker ps`:

```bash
root@server:~# docker ps
CONTAINER ID   IMAGE                                              COMMAND                  CREATED        STATUS        PORTS                                                                                  NAMES
f4ab79732007   portainer/portainer-ee:lts                         "/portainer"             2 weeks ago    Up 29 hours   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp, 0.0.0.0:9443->9000/tcp, :::9443->9443/tcp   portainer
```

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```bash
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install/server/setup)
{% endcontent-ref %}
