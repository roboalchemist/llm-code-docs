# Source: https://docs.anyscale.com/container-image.md

# What is a container image?

[View Markdown](/container-image.md)

# What is a container image?

A container image is a package that contains all the code, runtime, system tools, libraries, and settings required to run a container. All Anyscale workloads use a container image to ensure consistent operation across computing environments.

Anyscale uses containers to deploy nodes in a Ray cluster and run your Ray applications. Each container initializes using the container image specified when you configure or submit your workload.

Anyscale provides tools to inject additional files, variables, and configurations into container images through various features and options in the console, config files, and CLI. See [Dependency management on Anyscale](/dependency-management.md).

note

Organization owners can restrict how users interact with container images, including removing the ability for users to launch workloads with Anyscale base images. See [Container image roles](/administration/organization/permissions.md#container-image).

## Images on Anyscale[​](#images "Direct link to Images on Anyscale")

The following table describes the images supported on Anyscale:

| Image type    | Description                                                                                                                                                                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Base images   | These are the official images built, distributed, and maintained by Anyscale. They contain Ray and common Python and system dependencies used in Ray applications. See [Anyscale base images](/reference/base-images.md).                           |
| Custom images | Custom images include files, configurations, and dependencies set by a user. You can build your own images on Anyscale or load images to Anyscale from a private image registry. See [Custom images on Anyscale](/container-image/custom-image.md). |

## Image caching for optimized deploys[​](#cache "Direct link to Image caching for optimized deploys")

*Image caching* optimizes cluster deployment and scaling by storing an optimized version of container image in the cloud object storage connected to your Anyscale cloud.

The first time you launch an Anyscale cluster with a new image, Anyscale creates the cache for the image, storing the image in a formatted optimized for fast node deployment in a Ray cluster.

Once Anyscale has a cache for an image, all future operations that use that image in the Anyscale cloud use the image cache. This eliminates network traffic associated with downloading the image.

## Use a container image in a workspace[​](#use-image "Direct link to Use a container image in a workspace")

To use a container image in a workspace, do the following:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click **Workspaces**.
3. Click **+ Create** and select **Custom blank workspace**. The **New workspace** dialog appears.
4. In the **Name** field, enter a name for the workspace.
5. In the **Select image** field, select an Anyscale base image or custom image.
   <!-- -->
   * To use an image from an external registry, select **Use an image from an external registry**. See [Use container images from an external registry](/container-image/image-registry.md).
6. Click **Create**.

## Use a container image in a job[​](#use-job "Direct link to Use a container image in a job")

When creating jobs with the CLI, specify a container image through the `image_uri` parameter. You can also use the `containerfile` parameter. See the Job [CLI](/reference/job-api.md#anyscale-job-submit) and [SDK](/reference/job-api.md#anyscalejobsubmit) reference for more info.

1. With Job CLI, you can pass the image as an argument:

```
# Pass this in the command line

anyscale job submit -f job.yaml --image-uri anyscale/image/my-image-name:1 --ray-version 2.30.0
```

Or you can pass it inside the job configuration.

```
name: my-first-job
image_uri: anyscale/ray:2.44.0-slim-py312-cu125
working_dir: .
entrypoint: python main.py
```

2. Job SDK:

```
import anyscale
from anyscale.job.models import JobConfig

anyscale.job.submit(
    JobConfig(
        name="my-job",
        image_uri="anyscale/ray:2.30.0-slim-py310",
        entrypoint="python main.py",
        working_dir=".",
    ),
)
```

## Use a container image in a service[​](#use-service "Direct link to Use a container image in a service")

When deploying services, specify a container image through the `image_uri` parameter. You can also use the `containerfile` parameter. See the Service [CLI](/reference/service-api.md#anyscale-service-deploy) and [SDK](/reference/service-api.md#anyscaleservicedeploy) reference for more info.

1. With Service CLI, you can pass the image as an argument:

```
anyscale service deploy -f service.yaml --image-uri anyscale/image/my-image-name:1
```

Or you can pass it inside the service configuration.

```
name: my-first-service
image_uri: anyscale/ray:2.44.0-slim-py312-cu125
working_dir: .
applications:
- import_path: main:app
```

2. Service SDK

```
import anyscale
from anyscale.service.models import ServiceConfig

anyscale.service.deploy(
    ServiceConfig(
        name="my-service",
        image_uri="anyscale/ray:2.30.0-slim-py310",
        applications=[
            {"import_path": "main:app"},
        ],
        working_dir=".",
    ),
)
```
