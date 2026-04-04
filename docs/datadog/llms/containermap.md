# Source: https://docs.datadoghq.com/infrastructure/containermap.md

---
title: Container Map
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Container Map
---

# Container Map

## Overview{% #overview %}

Like [Host Maps](https://docs.datadoghq.com/infrastructure/hostmap/), [Containers Maps](https://app.datadoghq.com/infrastructure/map?node_type=container) give you a big picture of the health of your containers. Datadog integrates with ECS, Docker, Kubernetes, and more. You can see all of your containers together on one screen with customized groupings and filters, as well as metrics made instantly comprehensible through color and shape.

In one place, you can detect outliers, identify usage patterns, avoid resource problems, and make decisions about how to best manage your containers. It doesn't matter if you have 10, 100, or 10,000 containers. [Autodiscovery](https://docs.datadoghq.com/agent/kubernetes/integrations/) automatically detects new containers and accounts for them.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/containermap/containermap.65647dc4b3906034b760b7af3834aff7.png?auto=format"
   alt="Container map part 1" /%}

## Installation{% #installation %}

After deploying the [Agent](https://docs.datadoghq.com/agent/), no other configuration is necessary. For collecting Docker container information in the standard install rather than with the [Docker Agent](https://docs.datadoghq.com/agent/docker/), the `dd-agent` user needs to have permissions to access `docker.sock`. Permission can be given by adding `dd-agent` to the `docker` group.

## Further Reading{% #further-reading %}

- [Get real-time visibility of all of the containers across your environment](https://docs.datadoghq.com/infrastructure/livecontainers/)
- [Understand what is going on at any level of your system](https://docs.datadoghq.com/infrastructure/process/)
