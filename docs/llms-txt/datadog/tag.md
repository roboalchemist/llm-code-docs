# Source: https://docs.datadoghq.com/containers/kubernetes/tag.md

# Source: https://docs.datadoghq.com/containers/docker/tag.md

---
title: Docker Tag Extraction
description: >-
  Configure automatic tag extraction from Docker container labels and
  environment variables
breadcrumbs: >-
  Docs > Container Monitoring > Docker Agent for Docker, containerd, and Podman
  > Docker Tag Extraction
source_url: https://docs.datadoghq.com/docker/tag/index.html
---

# Docker Tag Extraction

## Overview{% #overview %}

The Datadog Agent can create and assign tags to all metrics, traces, and logs emitted by a container based on its labels or environment variables.

If you are running the Agent as a binary on a host, configure your tag extractions with the Agent tab instructions. If you are running the Agent as a container, configure your tag extraction with the Containerized Agent tab instructions.

### Out-of-the-box tagging{% #out-of-the-box-tagging %}

The Agent can autodiscover and attach tags to all data emitted by containers. The list of tags attached depends on the Agent [cardinality configuration](https://docs.datadoghq.com/agent/docker/tag/#extract-environment-variables-as-tags). [Tag Cardinality](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/?tab=containerizedenvironments#tags-cardinality) can impact billing as different cardinality settings impact the number of emitted metrics.

| Tag                  | Cardinality  | Requirement                                                                                                                                                                     |
| -------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `container_name`     | High         | N/A**Note**: not included for the containerd runtime.                                                                                                                           |
| `container_id`       | High         | N/A                                                                                                                                                                             |
| `rancher_container`  | High         | Rancher environment                                                                                                                                                             |
| `mesos_task`         | Orchestrator | Mesos environment                                                                                                                                                               |
| `docker_image`       | Low          | N/A**Note**: not included for the containerd runtime.                                                                                                                           |
| `image_name`         | Low          | N/A                                                                                                                                                                             |
| `short_image`        | Low          | N/A                                                                                                                                                                             |
| `image_tag`          | Low          | N/A                                                                                                                                                                             |
| `swarm_service`      | Low          | Swarm environment                                                                                                                                                               |
| `swarm_namespace`    | Low          | Swarm environment                                                                                                                                                               |
| `rancher_stack`      | Low          | Rancher environment                                                                                                                                                             |
| `rancher_service`    | Low          | Rancher environment                                                                                                                                                             |
| `env`                | Low          | [Unified service tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging) enabled                                                                   |
| `version`            | Low          | [Unified service tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging) enabled                                                                   |
| `service`            | Low          | [Unified service tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging) enabled                                                                   |
| `marathon_app`       | Low          | Marathon environment                                                                                                                                                            |
| `chronos_job`        | Low          | Mesos environment                                                                                                                                                               |
| `chronos_job_owner`  | Low          | Mesos environment                                                                                                                                                               |
| `nomad_task`         | Low          | Nomad environment                                                                                                                                                               |
| `nomad_job`          | Low          | Nomad environment                                                                                                                                                               |
| `nomad_group`        | Low          | Nomad environment                                                                                                                                                               |
| `git.commit.sha`     | Low          | [org.opencontainers.image.revision](https://github.com/opencontainers/image-spec/blob/02efb9a75ee11e05937b535cc5f228f9343ab2f5/annotations.md#pre-defined-annotation-keys) used |
| `git.repository_url` | Low          | [org.opencontainers.image.source](https://github.com/opencontainers/image-spec/blob/02efb9a75ee11e05937b535cc5f228f9343ab2f5/annotations.md#pre-defined-annotation-keys) used   |

### Unified service tagging{% #unified-service-tagging %}

As a best practice in containerized environments, Datadog recommends using unified service tagging when assigning tags. Unified service tagging ties Datadog telemetry together through the use of three standard tags: `env`, `service`, and `version`. To learn how to configure your environment with unified tagging, see the dedicated [unified service tagging documentation](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging).

## Extract labels as tags{% #extract-labels-as-tags %}

Starting with Agent v6.0+, the Agent can collect labels for a given container and use them as tags to attach to all data emitted by this container.

{% tab title="Containerized Agent" %}
To extract a given container label `<LABEL_NAME>` and transform it as a tag key `<TAG_KEY>` within Datadog, add the following environment variable to the Datadog Agent:

```bash
DD_CONTAINER_LABELS_AS_TAGS='{"<LABEL_NAME>":"<TAG_KEY>"}'
```

For example, you could set up:

```bash
DD_CONTAINER_LABELS_AS_TAGS='{"com.docker.compose.service":"service_name"}'
```

**Note**: `<LABEL_NAME>` is not case-sensitive. For example, if you have labels named `foo` and `FOO`, and you set `DD_CONTAINER_LABELS_AS_TAGS='{"foo": "bar"}'`, both `foo` and `FOO` are mapped to `bar`.

**Note**: `DD_CONTAINER_LABELS_AS_TAGS` is equivalent to the old `DD_DOCKER_LABELS_AS_TAGS`, and `DD_CONTAINER_ENV_AS_TAGS` to `DD_DOCKER_ENV_AS_TAGS`.
{% /tab %}

{% tab title="Agent" %}
To extract a given container label `<LABEL_NAME>` and transform it as a tag key `<TAG_KEY>` within Datadog, add the following configuration block in the [Agent `datadog.yaml` configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-main-configuration-file):

```yaml
container_labels_as_tags:
  <LABEL_NAME>: <TAG_KEY>
```

For example, you could set up:

```yaml
container_labels_as_tags:
  com.docker.compose.service: service_name
```

{% /tab %}

## Extract environment variables as tags{% #extract-environment-variables-as-tags %}

Datadog automatically collects common tags from [Docker, Kubernetes, ECS, Swarm, Mesos, Nomad, and Rancher](https://docs.datadoghq.com/agent/docker/?tab=standard#tagging). To extract even more tags, use the following options:

| Environment Variable               | Description                             |
| ---------------------------------- | --------------------------------------- |
| `DD_CONTAINER_LABELS_AS_TAGS`      | Extract container labels                |
| `DD_CONTAINER_ENV_AS_TAGS`         | Extract container environment variables |
| `DD_KUBERNETES_POD_LABELS_AS_TAGS` | Extract pod labels                      |
| `DD_CHECKS_TAG_CARDINALITY`        | Add tags to check metrics               |
| `DD_DOGSTATSD_TAG_CARDINALITY`     | Add tags to custom metrics              |

Starting with Agent v7.20+, a containerized Agent can Autodiscover tags from container labels. This process allows the Agent to associate custom tags to all data emitted by a container without modifying the Agent `datadog.yaml` file.

Tags should be added using the following format:

```yaml
com.datadoghq.ad.tags: '["<TAG_KEY_1>:<TAG_VALUE_1>", "<TAG_KEY_2>:<TAG_VALUE_2>"]'
```

With Agent v6.0+, the Agent can collect environment variables for a given container and use them as tags to attach to all data emitted by this container.

{% tab title="Containerized Agent" %}
To extract a given container environment variable `<ENVVAR_NAME>` and transform it as a tag key `<TAG_KEY>` within Datadog, add the following environment variable to the Datadog Agent:

```bash
DD_CONTAINER_ENV_AS_TAGS='{"<ENVVAR_NAME>": "<TAG_KEY>"}'
```

For example, you could set up:

```bash
DD_CONTAINER_ENV_AS_TAGS='{"ENVIRONMENT":"env"}'
```

{% /tab %}

{% tab title="Agent" %}
To extract a given container environment variable `<ENVVAR_NAME>` and transform it as a tag key `<TAG_KEY>` within Datadog, add the following configuration block in the [Agent `datadog.yaml` configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-main-configuration-file):

```yaml
container_env_as_tags:
  <ENVVAR_NAME>: <TAG_KEY>
```

For example, you could set up:

```yaml
container_env_as_tags:
  ENVIRONMENT: env
```

{% /tab %}

## Further Reading{% #further-reading %}

- [Getting started with tags](https://docs.datadoghq.com/getting_started/tagging/)
- [Using tags with Datadog](https://docs.datadoghq.com/getting_started/tagging/using_tags/)
- [Limit data collection to a subset of containers only](https://docs.datadoghq.com/agent/guide/autodiscovery-management/)
