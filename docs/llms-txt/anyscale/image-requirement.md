# Source: https://docs.anyscale.com/container-image/image-requirement.md

# Requirements for an Anyscale container image

[View Markdown](/container-image/image-requirement.md)

# Requirements for an Anyscale container image

This page specifies the requirements for creating a standardized image used in Anyscale infrastructure. It details the system requirements, essential software packages, and the Python libraries needed to ensure compatibility and performance on Ray clusters launched by Anyscale.

note

When you use the `docker build` command to build your container image, you should include the `--platform` flag to specify the desired platform architecture. Many virtual machine types supported by Anyscale use `linux/amd64`. You might need to specify a different platform architecture depending on the compute infrastructure you use to deploy your Anyscale cluster.

See [Tutorial: Build a custom container image](/container-image/build-image-tutorial.md).

## System requirements[​](#system-requirements "Direct link to System requirements")

* **Base image**: Use `ubuntu:22.04` as image foundation, ensuring a stable and widely supported Linux environment.
* **User configuration**: Include `ray` user with user ID `1000` and group ID `100`. Also, `ray` needs to be able to run `sudo` without a password.
* **Working directory**: Set `WORKDIR` to `/home/ray`, which designates the primary directory for user operations and application execution. Ensure that the `ray` user has read and write permissions to this directory.
* **Home directory**: Set `/home/ray` as `HOME`, centralizing user configurations and runtime files.
* **Image platform**: Use `amd64` platform (linux/amd64/v4).

## System[​](#system "Direct link to System")

* `sudo`
* `python`
* `bash`
* `openssh-server`
* `openssh-client`
* `rsync`
* `zip`
* `unzip`
* `git`
* `gdb`
* `curl`

## Python[​](#python "Direct link to Python")

* `ray>=2.7`
* `anyscale`
* `packaging`
* `boto3`
* `google`
* `google-cloud-storage`
* `jupyterlab`
* `terminado`

## Anyscale reserved resources[​](#reserved-resources "Direct link to Anyscale reserved resources")

### Filesystem paths[​](#filesystem "Direct link to Filesystem paths")

* `/etc/anyscale`
* `/opt/anyscale`
* `/tmp/anyscale`
* `/tmp/ray`
* `/mnt/`

### Network ports[​](#ports "Direct link to Network ports")

80, 443, 1010, 1012, 2222, 5555, 5903, 6379, 6822, 6823, 6824, 6826, 7878, 8000 ,8076, 8085, 8201, 8265, 8266, 8686, 8687, 8912, 8999, 9090, 9092, 9100, 9478 ,9479, 9480, 9481, 9482

## Workspace dependencies[​](#workspace-deps "Direct link to Workspace dependencies")

If you intend to run the image on workspaces, the following additional dependencies are required:

* **Persistent bash history**: Add `PROMPT_COMMAND="history -a"` to `/home/ray/.bashrc` to ensure that Ray saves the bash history after each command.
* **Source .workspacerc**: `source ~/.workspacerc` if it exists.

## Example Dockerfile[​](#example "Direct link to Example Dockerfile")

The following is an example Dockerfile that defines a custom container image compatible with Anyscale:

```
# syntax=docker/dockerfile:1.3-labs

# Specify the Ray version and Python version to use. You can override this setting at build time.
# Note that the ubuntu:22.04 base image is always Python 3.10.
# You're responsible for installing other versions of Python based on your application requirements.
ARG RAY_VERSION=2.49.2
ARG PYTHON_MAJOR_VERSION=3
ARG PYTHON_MINOR_VERSION=10

# Define the Anyscale image as a named build stage.
ARG ANYSCALE_RAY_IMAGE=anyscale/ray:$RAY_VERSION-py$PYTHON_MAJOR_VERSION$PYTHON_MINOR_VERSION
FROM $ANYSCALE_RAY_IMAGE as anyscale-ray

# Base image.
FROM ubuntu:22.04 as base

# Redeclare the RAY_VERSION and PYTHON_VERSION variables to make them available in the base image.
ARG RAY_VERSION
ARG PYTHON_MAJOR_VERSION
ARG PYTHON_MINOR_VERSION

ENV DEBIAN_FRONTEND=noninteractive

# Install basic dependencies and setup `ray` user with sudoer permissions.
# Note that `ray` user should be (uid: 1000, gid: 100) to work with shared file
# systems.
# Add gdb since Ray dashboard uses `memray attach`, which requires gdb.
RUN <<EOF
#!/bin/bash
set -euxo pipefail

apt-get update -y
apt-get install -y --no-install-recommends sudo tzdata openssh-client openssh-server rsync zip unzip git gdb curl
# Install Python -- you can replace this with whatever Python installation method
# you want (i.e., conda, etc...), as long as `python` is on PATH. At runtime
# Anyscale sources `/home/ray/.bashrc` in case you modify PATH there. This example uses
# virtualenv
apt-get install -y python3-venv

apt-get clean
rm -rf /var/lib/apt/lists/*

# Workaround for https://bugs.launchpad.net/ubuntu/+source/openssh/+bug/45234
mkdir -p /var/run/sshd

useradd -ms /bin/bash -d /home/ray ray --uid 1000 --gid 100
usermod -aG sudo ray
echo 'ray ALL=NOPASSWD: ALL' >> /etc/sudoers
EOF

# Switch to `ray` user.
USER ray
ENV HOME=/home/ray
ENV PATH=/home/ray/virtualenv/bin:$PATH

# Copying Ray and Anyscale Runtime files and requirements.
COPY --from=anyscale-ray /home/ray/requirements_compiled.txt /home/ray/requirements_compiled.txt
COPY --from=anyscale-ray /opt/anyscale /opt/anyscale

RUN <<EOF
#!/bin/bash
# Run as user `ray` from here.
su --login ray
python3 -m venv --system-site-packages /home/ray/virtualenv
export PATH=/home/ray/virtualenv/bin:$PATH

# You only need jupyterlab if you want to access Jupyter notebooks from the Anyscale workspace web UI.
# Note that this only installs `ray[default]` to minimize the amount of dependencies.
# You can add extra libraries such as Ray Tune with `ray[default,tune]` or all of them with `ray[all]`.
# See the Ray docs for more info: https://docs.ray.io/en/latest/ray-overview/installation.html
pip install --no-cache-dir -c /home/ray/requirements_compiled.txt \
    -r /opt/anyscale/runtime-requirements.txt \
    anyscale jupyterlab "ray[default]==${RAY_VERSION}"

# If you want to run your cluster on Amazon Web Services, uncomment out the following lines:
# curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# unzip awscliv2.zip && sudo ./aws/install && rm awscliv2.zip

# If you want to run your cluster on Google Cloud Platform, uncomment the following line:
# pip install --no-cache-dir -c /home/ray/requirements_compiled.txt \
#     google google-cloud-storage smart_open[gcs]

# Start of workspace dependencies: this section is only needed if you want your image to run on workspaces.

# This flushes bash history after each command, so that workspaces can persist it.
echo 'PROMPT_COMMAND="history -a"' >> /home/ray/.bashrc

# If the workspacerc exists, load it.
echo '[ -e ~/.workspacerc ] && source ~/.workspacerc' >> /home/ray/.bashrc

EOF

# Environment setup for the Anyscale Runtime.
ENV ANYSCALE_RAY_SITE_PKG_DIR=/home/ray/virtualenv/lib/python${PYTHON_MAJOR_VERSION}.${PYTHON_MINOR_VERSION}/site-packages
```
