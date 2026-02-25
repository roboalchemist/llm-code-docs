# Source: https://docs.datadoghq.com/security/default_rules/zpv-fua-5jx.md

---
title: The IPC namespace on the host should remain isolated from containers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The IPC namespace on the host should
  remain isolated from containers
---

# The IPC namespace on the host should remain isolated from containers
Classification:complianceFramework:cis-dockerControl:5.16
## Description{% #description %}

IPC (POSIX/SysV IPC) namespace provides separation of named shared memory segments, semaphores and message queues. The IPC namespace on the host should therefore not be shared with containers and should remain isolated.

## Rationale{% #rationale %}

The IPC namespace provides separation of IPC between the host and containers. If the host's IPC namespace is shared with the container, it would allow processes within the container to see all of IPC communications on the host system. This would remove the benefit of IPC level isolation between host and containers. An attacker with access to a container could get access to the host at this level with major consequences. The IPC namespace should therefore not be shared between the host and its containers.

## Audit{% #audit %}

Run this command: `docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: IpcMode={{ .HostConfig.IpcMode }}'`

If the command returns `host`, it means that the host IPC namespace is shared with the container. Any other result means that it is not shared, and that the system is configured in line with good security practice.

## Remediation{% #remediation %}

Do not start a container with the `--ipc=host` argument. For example, do not start a container with the command `docker run --interactive --tty --ipc=host centos /bin/bash`

## Impact{% #impact %}

Shared memory segments are used in order to accelerate interprocess communications, commonly in high-performance applications. If this type of application is containerized into multiple containers, you might need to share the IPC namespace of the containers in order to achieve high performance. Under these circumstances, you should still only share container specific IPC namespaces and not the host IPC namespace. A container's IPC namespace can be shared with another container. For example, `docker run --interactive --tty --ipc=container:e3a7a1a97c58 centos /bin/bash`

## Default value{% #default-value %}

By default, all containers have their IPC namespace enabled and host IPC namespace is not shared with any container.

## References{% #references %}

1. [https://docs.docker.com/engine/reference/run/#ipc-settings-ipc](https://docs.docker.com/engine/reference/run/#ipc-settings-ipc)
1. [http://man7.org/linux/man-pages/man7/namespaces.7.html](http://man7.org/linux/man-pages/man7/namespaces.7.html)

## CIS controls{% #cis-controls %}

Version 6

18 Application Software Security Application Software Security
