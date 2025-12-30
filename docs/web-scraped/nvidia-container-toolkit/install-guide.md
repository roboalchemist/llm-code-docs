# Source: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

Installing the NVIDIA Container Toolkit &#8212; NVIDIA Container Toolkit

  - 

[Skip to main content](#main-content)

    **Back to top

  **
  *
  Ctrl+K

[

NVIDIA Container Toolkit

](index.html)

    Choose version  

  *
  **
  **

# Installing the NVIDIA Container Toolkit[#](#installing-the-nvidia-container-toolkit)

## Installation[#](#installation)

### Prerequisites[#](#prerequisites)

Read [this section](supported-platforms.html) about platform support.

- 
Install the NVIDIA GPU driver for your Linux distribution.
NVIDIA recommends installing the driver by using the package manager for your distribution.
For information about installing the driver with a package manager, refer to
the [*NVIDIA Driver Installation Quickstart Guide*](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html).
Alternatively, you can install the driver by [downloading](https://www.nvidia.com/en-us/drivers/) a `.run` installer.

Note

There is a [known issue](troubleshooting.html#containers-losing-access-to-gpus-with-error-failed-to-initialize-nvml-unknown-error) on systems
where `systemd` cgroup drivers are used that cause containers to lose access to requested GPUs when
`systemctl daemon reload` is run. Refer to the troubleshooting documentation for more information.

### With `apt`: Ubuntu, Debian[#](#with-apt-ubuntu-debian)

Note

These instructions [should work](supported-platforms.html) for any Debian-derived distribution.

- 
Install the prerequisites for the instructions below:

$ sudo apt-get update && sudo apt-get install -y --no-install-recommends \
   curl \
   gnupg2

- Configure the production repository:

$ curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

Optionally, configure the repository to use experimental packages:

$ sudo sed -i -e '/experimental/ s/^#//g' /etc/apt/sources.list.d/nvidia-container-toolkit.list

- Update the packages list from the repository:

$ sudo apt-get update

`.
-->

- Install the NVIDIA Container Toolkit packages:

$ export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.18.1-1
  sudo apt-get install -y \
      nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}

### With `dnf`: RHEL/CentOS, Fedora, Amazon Linux[#](#with-dnf-rhel-centos-fedora-amazon-linux)

Note

These instructions [should work](supported-platforms.html) for many RPM-based distributions.

- 
Install the prerequisites for the instructions below:

$ sudo dnf install -y \
   curl

- Configure the production repository:

$ curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
  sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo

Optionally, configure the repository to use experimental packages:

$ sudo dnf-config-manager --enable nvidia-container-toolkit-experimental

- Install the NVIDIA Container Toolkit packages:

$ export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.18.1-1
  sudo dnf install -y \
      nvidia-container-toolkit-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      nvidia-container-toolkit-base-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container-tools-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container1-${NVIDIA_CONTAINER_TOOLKIT_VERSION}

### With `zypper`: OpenSUSE, SLE[#](#with-zypper-opensuse-sle)

- Configure the production repository:

$ sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo

Optionally, configure the repository to use experimental packages:

$ sudo zypper modifyrepo --enable nvidia-container-toolkit-experimental

- Install the NVIDIA Container Toolkit packages:

$  export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.18.1-1
   sudo zypper --gpg-auto-import-keys install -y \
      nvidia-container-toolkit-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      nvidia-container-toolkit-base-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container-tools-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container1-${NVIDIA_CONTAINER_TOOLKIT_VERSION}

## Configuration[#](#configuration)

### Prerequisites[#](#id1)

- You installed a supported container engine (Docker, Containerd, CRI-O, Podman).

- 
You installed the NVIDIA Container Toolkit.

### Configuring Docker[#](#configuring-docker)

- 
Configure the container runtime by using the `nvidia-ctk` command:

$ sudo nvidia-ctk runtime configure --runtime=docker

The `nvidia-ctk` command modifies the `/etc/docker/daemon.json` file on the host.
The file is updated so that Docker can use the NVIDIA Container Runtime.

- 
Restart the Docker daemon:

$ sudo systemctl restart docker

#### Rootless mode[#](#rootless-mode)

To configure the container runtime for Docker running in [Rootless mode](https://docs.docker.com/engine/security/rootless/),
follow these steps:

- 
Configure the container runtime by using the `nvidia-ctk` command:

$ nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json

- Restart the Rootless Docker daemon:

$ systemctl --user restart docker

- Configure `/etc/nvidia-container-runtime/config.toml` by using the `sudo nvidia-ctk` command:

$ sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place

### Configuring containerd (for Kubernetes)[#](#configuring-containerd-for-kubernetes)

- Configure the container runtime by using the `nvidia-ctk` command:

$ sudo nvidia-ctk runtime configure --runtime=containerd

By default, the `nvidia-ctk` command creates a `/etc/containerd/conf.d/99-nvidia.toml`
drop-in config file and modifies (or creates) the `/etc/containerd/config.toml` file
to ensure that the `imports` config option is updated accordingly. The drop-in file
ensures that containerd can use the NVIDIA Container Runtime.

- 
Restart containerd:

$ sudo systemctl restart containerd

### Configuring containerd (for nerdctl)[#](#configuring-containerd-for-nerdctl)

No additional configuration is needed.
You can just run `nerdctl run --gpus=all`, with root or without root.
You do not need to run the `nvidia-ctk` command mentioned above for Kubernetes.

Refer to the [nerdctl documentation](https://github.com/containerd/nerdctl/blob/main/docs/gpu.md) for more information.

### Configuring CRI-O[#](#configuring-cri-o)

- 
Configure the container runtime by using the `nvidia-ctk` command:

$ sudo nvidia-ctk runtime configure --runtime=crio

By default, the `nvidia-ctk` command creates a `/etc/crio/conf.d/99-nvidia.toml`
drop-in config file. The drop-in file ensures that CRI-O can use the NVIDIA Container Runtime.

- 
Restart the CRI-O daemon:

$ sudo systemctl restart crio

### Configuring Podman[#](#configuring-podman)

For Podman, NVIDIA recommends using [CDI](cdi-support.html) for accessing NVIDIA devices in containers.

## Next Steps[#](#next-steps)

- 
[Running a Sample Workload](sample-workload.html)

    ** On this page

   so the DOM is not blocked -->