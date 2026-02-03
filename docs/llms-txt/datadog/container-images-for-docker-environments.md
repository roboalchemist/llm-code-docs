# Source: https://docs.datadoghq.com/containers/guide/container-images-for-docker-environments.md

---
title: Container Images for Docker Environments
description: >-
  Overview of available Datadog container images for Docker environments across
  different registries
breadcrumbs: >-
  Docs > Containers > Containers Guides > Container Images for Docker
  Environments
---

# Container Images for Docker Environments

## Overview{% #overview %}

If you are using Docker, there are several container images available through GCR and ECR that you may want to use within your environment:

{% tab title="GCR" %}

| Datadog service                                                                                               | GCR                                                                                                                                            | GCR Pull Command                                                  |
| ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| [Docker Agent](https://docs.datadoghq.com/agent/docker/)                                                      | [Docker Agent (v6+)](https://console.cloud.google.com/artifacts/docker/datadoghq/us/gcr.io/agent)                                              | `docker pull gcr.io/datadoghq/agent`                              |
| Docker Agent (v 5)                                                                                            | [Docker Agent (v5)](https://console.cloud.google.com/artifacts/docker/datadoghq/us/gcr.io/agent)                                               | `docker pull gcr.io/datadoghq/docker-dd-agent`                    |
| [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/)                                                 | [DogStatsD](https://console.cloud.google.com/artifacts/docker/datadoghq/us/gcr.io/dogstatsd)                                                   | `docker pull gcr.io/datadoghq/dogstatsd`                          |
| [Datadog Cluster Agent](https://docs.datadoghq.com/agent/cluster_agent/)                                      | [Cluster Agent](https://console.cloud.google.com/artifacts/docker/datadoghq/us/gcr.io/cluster-agent)                                           | `docker pull gcr.io/datadoghq/cluster-agent`                      |
| [Synthetics Private Location Worker](https://docs.datadoghq.com/getting_started/synthetics/private_location/) | [Synthetics Private Location Worker](https://console.cloud.google.com/artifacts/docker/datadoghq/us/gcr.io/synthetics-private-location-worker) | `docker pull gcr.io/datadoghq/synthetics-private-location-worker` |

{% /tab %}

{% tab title="ECR" %}

| Datadog service                                                                                              | Docker Hub                                                                                               | Docker Pull Command                                                     |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [Docker Agent](https://docs.datadoghq.com/agent/docker/)                                                     | [Docker Agent (v6+)](https://gallery.ecr.aws/datadog/agent)                                              | `docker pull public.ecr.aws/datadog/agent`                              |
| Docker Agent (v 5)                                                                                           | [Docker Agent (v5)](https://gallery.ecr.aws/datadog/docker-dd-agent)                                     | `docker pull public.ecr.aws/datadog/docker-dd-agent`                    |
| [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/)                                                | [DogStatsD](https://gallery.ecr.aws/datadog/dogstatsd)                                                   | `docker pull public.ecr.aws/datadog/dogstatsd`                          |
| [Datadog Cluster Agent](https://docs.datadoghq.com/agent/cluster_agent/)                                     | [Cluster Agent](https://gallery.ecr.aws/datadog/cluster-agent)                                           | `docker pull public.ecr.aws/datadog/cluster-agent`                      |
| [Synthetics Private Location Worker](https://docs.datadoghq.com/getting_started/synthetics/private_location) | [Synthetics Private Location Worker](https://gallery.ecr.aws/datadog/synthetics-private-location-worker) | `docker pull public.ecr.aws/datadog/synthetics-private-location-worker` |

{% /tab %}

If you need to use Docker Hub, see [Docker Hub](https://docs.datadoghq.com/agent/faq/docker-hub/).

## Further reading{% #further-reading %}

- [Get started with the Docker Agent](https://docs.datadoghq.com/agent/docker/)
- [Get started with the Cluster Agent](https://docs.datadoghq.com/agent/cluster_agent/)
