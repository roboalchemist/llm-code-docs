# Source: https://docs.datadoghq.com/security/default_rules/3s2-7iz-qi8.md

---
title: The host's network namespace should be hidden from containers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The host's network namespace should be
  hidden from containers
---

# The host's network namespace should be hidden from containers
Classification:complianceFramework:cis-dockerControl:5.9
## Description{% #description %}

When the networking mode on a container is set to `--net=host`, the container is not placed inside a separate network stack. Effectively, applying this option instructs Docker to not containerize the container's networking. The consequence of this is that the container lives "outside" in the main Docker host and has full access to its network interfaces.

## Rationale{% #rationale %}

Selecting this option is potentially dangerous. It allows the container process to open reserved low numbered ports in the way that any other root process can. It also allows the container to access network services such as D-bus on the Docker host. A container process could potentially carry out undesired actions, such as shutting down the Docker host. This option should not be used unless there is a very specific reason for enabling it.

## Audit{% #audit %}

Use this command: `docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: NetworkMode={{ .HostConfig.NetworkMode }}'` If this returns `NetworkMode=host`, it means that the `--net=host` option was passed when the container was started.

## Remediation{% #remediation %}

You should not pass the ânet=host option when starting any container.

## Impact{% #impact %}

None.

## Default value{% #default-value %}

By default, containers connect to the Docker bridge when starting and do not run in the context of the host's network stack.

## References{% #references %}

1. [https://docs.docker.com/engine/userguide/networking/](https://docs.docker.com/engine/userguide/networking/) 2. [https://docs.docker.com/engine/reference/run/#network-settings](https://docs.docker.com/engine/reference/run/#network-settings)

## CIS controls{% #cis-controls %}

Version 6 12 Boundary Defense Boundary Defense
