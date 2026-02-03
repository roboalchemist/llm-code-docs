# Source: https://docs.datadoghq.com/security/default_rules/9h8-wne-ybj.md

---
title: Containers should not share the host's user namespaces
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Containers should not share the host's
  user namespaces
---

# Containers should not share the host's user namespaces
Classification:complianceFramework:cis-dockerControl:5.30 
## Description{% #description %}

You should not share the host's user namespaces with containers running on it.

## Rationale{% #rationale %}

User namespaces ensure that a root process inside the container will be mapped to a non-root process outside the container. Sharing the user namespaces of the host with the container does not therefore isolate users on the host from users in the containers.

## Audit{% #audit %}

Run this command and ensure that it does not return any value for `UsernsMode`. If it returns a value of `host`, it means that the host user namespace is shared with its containers: `docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: UsernsMode={{ .HostConfig.UsernsMode }}'`

## Remediation{% #remediation %}

Do not share user namespaces between host and containers. For example, do not run the command `docker run --rm -it --userns=host ubuntu bash`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the host user namespace is shared with containers unless user namespace support is enabled.

## References{% #references %}

1. [https://docs.docker.com/engine/security/userns-remap/](https://docs.docker.com/engine/security/userns-remap/)
1. [https://docs.docker.com/engine/reference/commandline/run/#options](https://docs.docker.com/engine/reference/commandline/run/#options)
1. [https://github.com/docker/docker/pull/12648](https://github.com/docker/docker/pull/12648)
1. [https://events.linuxfoundation.org/sites/events/files/slides/User%20Namespaces%20-%20ContainerCon%202015%20-%2016-9-final_0.pdf](https://events.linuxfoundation.org/sites/events/files/slides/User%20Namespaces%20-%20ContainerCon%202015%20-%2016-9-final_0.pdf)

## CIS controls{% #cis-controls %}

Version 6

12 Boundary Defense Boundary Defense
