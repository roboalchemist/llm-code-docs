# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent/extending-deployment-image.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Extending Deployment Image

> Extend the default deployment image with custom tools and configurations for your env zero self-hosted agent

# Extending Deployment Image

env zero self-hosted Kubernetes agent allows you to run deployments on your own infrastructure, giving you more control and security. While the default deployment image includes all the necessary tools for env zero's native features, you may need to install additional tools or specific versions of existing tools to support your custom workflows. This guide will walk you through extending the default deployment image to meet your specific needs.

## Why Extend the Deployment Image?

Extending the deployment image is necessary when you want to:

* **Use custom tools**: If your deployment process relies on tools that are not included in the base image, such as specific CLI tools, testing frameworks, or security scanners.
* **Pre-install env zero supported tools**: To save network bandwidth and reduce deployment times, you can pre-install tools that env zero supports but doesn't include in the base image.
* **Standardize your environment**: Ensure that all your deployments run in a consistent environment with the exact tool versions your organization requires.

## Creating a Custom Dockerfile

To extend the base image, you'll need to create a Dockerfile that uses the env zero deployment image as its base and then adds your custom tools and configurations.

Here's an example of a Dockerfile that pre-installs the `aws` and `gcloud` CLIs with a specific version for gcloud:

```dockerfile Dockerfile theme={null}
# Sets the base image to the latest version of the env zero deployment agent.
FROM ghcr.io/env0/deployment-agent:latest

# Sets an environment variable to specify the version of the Google Cloud CLI to be installed. If you omit this, the default version will be installed.
ENV ENV0_GCLOUD_VERSION=532.0.0

# Executes env zero's "install-package-cli.js" utility, which is provided to pre-install
# CLI tools (e.g., aws, gcloud) into the image before runtime.
RUN node install-package-cli.js aws gcloud

# Custom installtion of your package
RUN curl -sSL "https://github.com/cli/cli/releases/download/v2.53.0/gh_2.53.0_linux_amd64.tar.gz" -o gh.tar.gz \
    && tar -zxvf gh.tar.gz \
    && mv gh_2.53.0_linux_amd64/bin/gh /usr/local/bin/ \
    && rm -rf gh.tar.gz gh_2.53.0_linux_amd64
```

<Info>
  If you are using strictSecurityContext mode, in order to install packages as a pre-installation you need to add the following variable to the command:

  ```dockerfile Dockerfile theme={null}
  RUN STRICT_MODE=true node install-package-cli.js aws az
  ```

</Info>

You can add more `RUN` commands to install your own custom tools or perform other setup tasks.

### Available tools

These tools can be pre-installed in your image using the install-package-cli.js script provided by env0. This script ensures that the specified CLI tools are available during runtime without requiring installation in your deployment steps.

## Build Your Own Image from a Custom Base Image

For advanced use cases, you might want to use your own company's base image, which may already be hardened and configured according to your internal standards. This approach allows you to layer the env zero agent capabilities on top of your existing infrastructure.

<Warning>
  This is an experimental feature

  Building on a custom base image is not officially supported and may lead to unexpected behavior. While it can work, we cannot guarantee that all env zero features will function correctly. Proceed with caution and test thoroughly.
</Warning>

Your base image must include the following tools for the env zero agent to function correctly: `curl` `git` `gnupg` `jq` `nodejs`

### Example Dockerfile using a Custom Base

You can create a Dockerfile that uses your image as a base and copies the necessary env zero agent files from the official image. A multi-stage build is the recommended approach for this.

The package installation commands (apt-get) in the example are for Debian-based systems and should be adapted for your image's specific package manager.

```dockerfile Dockerfile theme={null}
# Example for using another image as a base - Only tested for terraform and basic resource
# AWS CLI and Azure CLI not supported because we compile them fot alpine

# Stage 1: Source Stage
FROM ghcr.io/env0/deployment-agent:latest AS builder

# Stage 2: Final Image
FROM node:latest

USER node
RUN git config --global --add safe.directory "*"

# Set a working directory for the application.
WORKDIR /app

# Copy the service files from the 'builder' stage into the current directory (/app).
COPY --from=builder /usr/build/services/deployment-service .

ENV HOME=/home/node
RUN chown -R node /home/node

USER root
CMD [ "npm", "run", "start:docker-agent" ]
```

## Updating the Agent Configuration

After you have built your custom Docker image and pushed it to a container registry, you need to configure your env zero agent to use this new image. This is done by updating the Helm chart values for your agent installation.

You will need to modify the following values in your `values.yaml` file:

* **`dockerImage`**: Set this to the URL of your custom Docker image in your container registry.
* **`agentImagePullSecret`** *(Optional)*: If your container registry requires authentication, you'll need to create a Kubernetes secret with the credentials and specify the name of the secret here.

Here's an example snippet from a `values.yaml` file:

```yaml values.yaml theme={null}
dockerImage: "your-registry/your-custom-image:your-tag"
agentImagePullSecret: "your-pull-secret"
```

Once you've updated the `values.yaml` file, apply the changes to your Helm release to update the agent with the new image.

## Summary

By following these steps, you can create a custom deployment environment that is tailored to your organization's specific needs, allowing you to run powerful and flexible custom flows in your env zero deployments.

Built with [Mintlify](https://mintlify.com).
