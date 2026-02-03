# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.containers.dataset.md

---
title: Containers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Containers
---

# Containers

The Containers table provides real-time visibility into all containers across your environment monitored by Datadog. Each row represents a container and includes metadata about resource limits (CPU, memory, threads), lifecycle timestamps (creation and start times), orchestration platform details, container images, and associated tags. This table enables you to monitor container health and performance, track resource allocation across your containerized workloads, correlate containers with their host infrastructure, and gain insights into your Docker, Kubernetes, ECS, and other container orchestration environments. The Datadog Agent automatically discovers and monitors all containers on each host.

```
dd.containers
```

## Fields

| Title              | ID           | Type | Data Type | Description                                                                                                           |
| ------------------ | ------------ | ---- | --------- | --------------------------------------------------------------------------------------------------------------------- |
| CPU Limit          | cpu_limit    | core | string    | The maximum CPU resources allocated to the container.                                                                 |
| Creation Timestamp | created_at   | core | timestamp | The timestamp when the container was created.                                                                         |
| Hostname           | hostname     | core | string    | The hostname of the host running the container.                                                                       |
| Container ID       | id           | core | string    | The unique identifier of the container.                                                                               |
| Container Image    | image        | core | string    | The container image name and tag used to run the container.                                                           |
| Memory Limit       | memory_limit | core | int64     | The maximum memory resources allocated to the container, in bytes.                                                    |
| Container Name     | name         | core | string    | The name assigned to the container.                                                                                   |
| Orchestrator       | orchestrator | core | string    | The container orchestration platform managing the container, such as Kubernetes, ECS, or Docker.                      |
| Start Timestamp    | started_at   | core | timestamp | The timestamp when the container was started.                                                                         |
| Resource Tags      | tags         | core | hstore    | This field contains tags represented as key-value pairs, used to categorize and provide metadata about the container. |
| Thread Limit       | thread_limit | core | int64     | The maximum number of threads allocated to the container.                                                             |
| Container Type     | type         | core | string    | Specifies the type of container runtime or technology used.                                                           |
