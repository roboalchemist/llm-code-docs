# Source: https://docs.anyscale.com/dependency-management/init-scripts.md

# Use init scripts with custom images

[View Markdown](/dependency-management/init-scripts.md)

# Use init scripts with custom images

Use init scripts in custom images on Anyscale to add extensible startup logic to all containers in your cluster.

An init script is a shell script that runs inside the Ray container on all nodes before Ray starts. Common use cases include the following:

* Performing commands to fetch resources including codebases, files, data, and dependencies.
* Retrieving private Git repositories.
* Mounting cloud object storage.
* Installing container-based agents for tasks such as logging, monitoring, and security.
* Running tests or verification checks, such as validating network paths or running complex health checks.

## How to use init scripts[​](#how-to-use-init-scripts "Direct link to How to use init scripts")

Anyscale runs all `.sh` files stored in the `/anyscale/init` path on the image as init scripts. To use an init script, do the following:

1. Create the `/anyscale/init` directory in your image.
2. Create or copy an init script into this directory.

If an init script fails to execute on a node, the cluster event log records the standard output and standard error and the node terminates.

All output from init scripts is written into `/tmp/ray/startup-actions.log`.

## Example init script[​](#example-init-script "Direct link to Example init script")

The following example Dockerfile creates two init scripts that run on top of an Anyscale base image.

In this simple example, the logic defined by the init scripts named `script1.sh` and `script2.sh` writes the current timestamp to text files and stdout.

```
FROM anyscale/ray:2.30.0-slim-py310

# Create the directory
RUN sudo mkdir -p /anyscale/init

# Scripts run alphabetically: script1 then script2
RUN echo 'date | sudo tee /tmp/script1_output.txt' | sudo tee /anyscale/init/script1.sh
RUN sudo chmod +x /anyscale/init/script1.sh

RUN echo 'date | sudo tee /tmp/script2_output.txt' | sudo tee /anyscale/init/script2.sh
RUN sudo chmod +x /anyscale/init/script2.sh
```

## Reuse complex init scripts[​](#reuse-complex-init-scripts "Direct link to Reuse complex init scripts")

Reuse complex init scripts by storing them in the shared storage location and then copying the file to the `/anyscale/init` directory, as in the following code example:

```
FROM anyscale/ray:2.46.0-slim-py312

# Create directory for init scripts
RUN sudo mkdir -p /anyscale/init

RUN echo '#!/bin/bash' | sudo tee -a /anyscale/init/script1.sh
RUN echo 'sudo bash /mnt/shared_storage/init_scripts/my_custom_script.sh' | sudo tee -a /anyscale/init/script1.sh
RUN sudo chmod +x /anyscale/init/script1.sh
```
