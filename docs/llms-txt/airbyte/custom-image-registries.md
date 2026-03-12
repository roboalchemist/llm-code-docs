# Source: https://docs.airbyte.com/platform/deploying-airbyte/integrations/custom-image-registries.md

# Source: https://docs.airbyte.com/platform/2.0/deploying-airbyte/integrations/custom-image-registries.md

# Source: https://docs.airbyte.com/platform/1.8/deploying-airbyte/integrations/custom-image-registries.md

# Source: https://docs.airbyte.com/platform/1.7/deploying-airbyte/integrations/custom-image-registries.md

# Source: https://docs.airbyte.com/platform/1.6/deploying-airbyte/integrations/custom-image-registries.md

# Custom image registry

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

You can optionally configure Airbyte to pull Docker images from a custom image registry rather than [Airbyte's public Docker repository](https://hub.docker.com/u/airbyte). In this case, Airbyte pulls both platform images (e.g. `server`, `webapp`, `workload-launcher`, etc.) and connector images (e.g. Postgres Source, S3 Destination, etc.) from the configured registry.

Implementing Airbyte this way has several advantages.

* **Security**: Private custom image registries keep images in your network, reducing the risk of external threats.
* **Access control**: You have more control over who can access and modify images.
* **Compliance**: By keeping images in a controlled environment, it's easier to prove compliance with regulatory requirements for data storage and handling.

## Before you start[​](#before-you-start "Direct link to Before you start")

Set up your custom image registry. The examples in this article use GitHub, but you have many options. Here are some popular ones:

| Cloud provider | Service name                | Documentation                                                                                                                                                                                                                                                                                  |
| -------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Google Cloud   | Artifact Registry           | [Quickstart](https://cloud.google.com/artifact-registry/docs/docker/quickstart)                                                                                                                                                                                                                |
| AWS            | Amazon ECR                  | [Getting started with Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-console.html)                                                                                                                                                                         |
| Azure          | Container Registry          | [Quickstart](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal#:~:text=Azure%20Container%20Registry%20is%20a,container%20images%20and%20related%20artifacts.\&text=Then%2C%20use%20Docker%20commands%20to,the%20image%20from%20your%20registry.) |
| DockerHub      | Repositories                | [DockerHub Quickstart](https://docs.docker.com/docker-hub/)                                                                                                                                                                                                                                    |
| GitHub         | Container Registry          | [Working with the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)                                                                                                                                         |
| Self hosted    | Open-source Docker Registry | [Deploy a registry server](https://docs.docker.com/registry/deploying/)                                                                                                                                                                                                                        |

## Custom connectors using fully qualified domain names[​](#custom-connectors-using-fully-qualified-domain-names "Direct link to Custom connectors using fully qualified domain names")

[Custom Docker connectors](/platform/1.6/operator-guides/using-custom-connectors.md) in your workspace that specify an image using a fully qualified domain name (for example, `example.com/airbyte/your-custom-source`) ignore your configured custom image registry and pull images from the domain specified by that connector.

## Get a list of all Airbyte images[​](#get-a-list-of-all-airbyte-images "Direct link to Get a list of all Airbyte images")

To get a list of Airbyte images for the latest version, use abctl.

```
abctl images manifest
```

You should see something like this:

```
airbyte/bootloader:1.3.1
airbyte/connector-builder-server:1.3.1
airbyte/connector-sidecar:1.3.1
airbyte/container-orchestrator:1.3.1
airbyte/cron:1.3.1
airbyte/db:1.3.1
airbyte/mc:latest
airbyte/server:1.3.1
airbyte/webapp:1.3.1
airbyte/worker:1.3.1
airbyte/workload-api-server:1.3.1
airbyte/workload-init-container:1.3.1
airbyte/workload-launcher:1.3.1
bitnami/kubectl:1.28.9
busybox:1.35
busybox:latest
curlimages/curl:8.1.1
minio/minio:RELEASE.2023-11-20T22-40-07Z
temporalio/auto-setup:1.23.0
```

## Step 1: Customize Airbyte to use your image registry[​](#step-1-customize-airbyte-to-use-your-image-registry "Direct link to Step 1: Customize Airbyte to use your image registry")

To pull all platform and connector images from a custom image registry, add the following customization to Airbyte's `values.yaml` file, replacing the `registry` value with your own registry location.

values.yaml

```
global:
  image:
    registry: ghcr.io/NAMESPACE
```

If your registry requires authentication, you can create a Kubernetes secret and reference it in the Airbyte config:

1. Create a Kubernetes secret. In this example, you create a secret called `regcred` from a config file. That file contains authentication information for a private custom image registry. [Learn more about Kubernetes secrets](https://kubernetes.io/docs/tasks/configmap-secret/).

   ```
   kubectl create secret generic regcred \
   --from-file=.dockerconfigjson=<path/to/.docker/config.json> \
   --type=kubernetes.io/dockerconfigjson
   ```

2. Add the secret you created to your `values.yaml` file. In this example, you use your `regcred` secret to authenticate.

   values.yaml

   ```
   global:
     image:
       registry: ghcr.io/NAMESPACE
     imagePullSecrets:
       - name: regcred
   ```

## Step 2: Tag and push Airbyte images[​](#step-2-tag-and-push-airbyte-images "Direct link to Step 2: Tag and push Airbyte images")

Tag and push Airbyte's images to your custom image registry.

In this example, you tag all platform images and push them all to GitHub.

```
abctl images manifest | xargs -L1 -I{} docker tag {} ghcr.io/NAMESPACE/{} && docker push ghcr.io/NAMESPACE/{}
```

You can also pull Airbyte's connector images from Docker, tag them, and push them to your custom image registry. You must do this prior to adding a source or destination.

In this example, you pull a connector from Docker, tag it, and push it to GitHub.

```
docker pull airbyte/destination-google-sheets:latest
docker tag airbyte/desination-google-sheets:latest ghcr.io/NAMESPACE/desination-google-sheets:latest
docker push ghcr.io/NAMESPACE/destination-google-sheets:latest
```

Now, when you install Airbyte, images will come from the custom image registry you configured.
