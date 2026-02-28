# Source: https://docs.datadoghq.com/security/default_rules/3wk-jj4-zxc.md

---
title: The Docker local storage partition should be separate from other partitions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Docker local storage partition
  should be separate from other partitions
---

# The Docker local storage partition should be separate from other partitions
Classification:complianceFramework:cis-dockerControl:1.2.1
## Description{% #description %}

All Docker containers and their data and metadata are stored in the `/var/lib/docker` directory. By default, `/var/lib/docker` should be mounted under either the `/` or `/var` partitions depending on how the Linux operating system in use is configured.

## Rationale{% #rationale %}

Docker depends on `/var/lib/docker` as the default directory where all Docker-related files, including the images, are stored. This directory could fill up quickly, causing both Docker and the host to become unusable. For this reason, you should create a separate partition (logical volume) for storing Docker files.

## Audit{% #audit %}

To see the partition details for the `/var/lib/docker` mount point, at the Docker host run:

```bash
grep '/var/lib/docker\s' /proc/mounts
```

Alternatively, to see whether the configured root directory is a mount point, run:

```bash
mountpoint -- "$(docker info -f '{{ .DockerRootDir }}')"
```

## Remediation{% #remediation %}

For new installations, you should create a separate partition for the `/var/lib/docker` mount point. For systems that have already been installed, you should use the Logical Volume Manager (LVM) within Linux to create a new partition.

## Impact{% #impact %}

None.

## Default value{% #default-value %}

By default, `/var/lib/docker` is mounted under the `/` or `/var` partitions depending on how the OS is configured.

## References{% #references %}

1. [https://www.projectatomic.io/docs/docker-storage-recommendation/](https://www.projectatomic.io/docs/docker-storage-recommendation/)

## CIS controls{% #cis-controls %}

Version 6.14 Controlled Access Based on the Need to Know
