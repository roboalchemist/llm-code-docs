# Source: https://docs.datadoghq.com/containers/guide/sync_container_images.md

---
title: Synchronize Datadog's images with a private registry
description: >-
  Synchronize Datadog container images from public registries to your private
  registry using Crane or similar tools
breadcrumbs: >-
  Docs > Containers > Containers Guides > Synchronize Datadog's images with a
  private registry
---

# Synchronize Datadog's images with a private registry

Datadog publishes container images in multiple public container registries. While this is convenient for many users, some organizations may want to use a private container registry. This guide explains how to synchronize Datadog's container images to a private registry.

| datadoghq.azurecr.io                                    | dockerhub.io                               | gcr.io                                              | public.ecr.aws                                            |
| ------------------------------------------------------- | ------------------------------------------ | --------------------------------------------------- | --------------------------------------------------------- |
| datadoghq.azurecr.io/agent                              | datadog/agent                              | gcr.io/datadoghq/agent                              | public.ecr.aws/datadog/agent                              |
| datadoghq.azurecr.io/cluster-agent                      | datadog/cluster-agent                      | gcr.io/datadoghq/cluster-agent                      | public.ecr.aws/datadog/cluster-agent                      |
| datadoghq.azurecr.io/operator                           | datadog/operator                           | gcr.io/datadoghq/operator                           | public.ecr.aws/datadog/operator                           |
| datadoghq.azurecr.io/dogstatsd                          | datadog/dogstatsd                          | gcr.io/datadoghq/dogstatsd                          | public.ecr.aws/datadog/dogstatsd                          |
| datadoghq.azurecr.io/synthetics-private-location-worker | datadog/synthetics-private-location-worker | gcr.io/datadoghq/synthetics-private-location-worker | public.ecr.aws/datadog/synthetics-private-location-worker |

## Synchronize images to your private registry{% #synchronize-images-to-your-private-registry %}

### Using Crane{% #using-crane %}

[Crane](https://github.com/google/go-containerregistry/tree/main/cmd/crane) is a tool made by Google to manage container images and registries and can be used to synchronize images between different container registries. For more information about Crane, see the [Crane documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md).

#### Install Crane{% #install-crane %}

For detailed instructions on how to install Crane, see the [Crane README.md](https://github.com/google/go-containerregistry/tree/main/cmd/crane).

#### Copy an image to another registry using Crane{% #copy-an-image-to-another-registry-using-crane %}

Crane can copy images between different container registries while preserving the image's digest.

This means that the copy keeps the same manifest and works with multi-platform images.

To copy an image from one registry to another, use the `crane copy` command.

```shell
crane copy <REGISTRY>/<SOURCE_IMAGE>:<IMAGE_TAG> <REGISTRY>/<DEST_IMAGE>:<IMAGE_TAG>
```

You can use the `-n` flag to avoid overwriting an existing tag in the destination registry.

For example, to copy the default images needed for the Datadog Operator from Docker Hub to a private registry:

```shell
AGENT_VERSION=<AGENT_IMAGE_TAG>
OPERATOR_VERSION=<OPERATOR_IMAGE_TAG>
REGISTRY=<REGISTRY_URL>
crane copy gcr.io/datadoghq/operator:$OPERATOR_VERSION $REGISTRY/operator:$OPERATOR_VERSION
crane copy gcr.io/datadoghq/agent:$AGENT_VERSION $REGISTRY/agent:$AGENT_VERSION
crane copy gcr.io/datadoghq/cluster-agent:$AGENT_VERSION $REGISTRY/cluster-agent:$AGENT_VERSION
```

## How to use a private registry{% #how-to-use-a-private-registry %}

Once you've synchronized the images, you can use this guide to [change the container registry](https://docs.datadoghq.com/containers/guide/changing_container_registry) used by your environment.

**Note**: If using your private registry, you might need to create a pull secret to be able the pull the images. For more information about creating a pull secret, see the [Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#registry-secret-existing-credentials).
