# Source: https://docs.datadoghq.com/security/default_rules/8xc-5x6-h2k.md

---
title: Containers should not run in privileged mode
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Containers should not run in privileged
  mode
---

# Containers should not run in privileged mode
Classification:complianceFramework:cis-dockerControl:5.4 
## Description{% #description %}

Using the `--privileged` flag provides all Linux kernel capabilities to the container to which it is applied and therefore overwrites the `--cap-add` and `--cap-drop` flags. For this reason, ensure that it is not used.

## Rationale{% #rationale %}

The `--privileged` flag provides all capabilities to the container to which it is applied, and also lifts all the limitations enforced by the device cgroup controller. As a consequence this the container has most of the rights of the underlying host. This flag only exists to allow for specific use cases (for example running Docker within Docker) and should not generally be used.

## Audit{% #audit %}

Run this command: `docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Privileged={{ .HostConfig.Privileged }}'` This command returns `Privileged=false` for each container instance.

## Remediation{% #remediation %}

Do not run containers with the `--privileged` flag. For example, do not start a container using the command `docker run --interactive --tty --privileged centos /bin/bash`

## Impact{% #impact %}

If you start a container without the `--privileged` flag, it will not have excessive default capabilities.

## Default value{% #default-value %}

False

## References{% #references %}

1. [https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.
