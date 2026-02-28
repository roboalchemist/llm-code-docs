# Source: https://docs.datadoghq.com/security/default_rules/xci-3xk-aim.md

---
title: The Docker instance should not use AUFS as its storage driver
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Docker instance should not use AUFS
  as its storage driver
---

# The Docker instance should not use AUFS as its storage driver
Classification:complianceFramework:cis-dockerControl:2.5
## Description{% #description %}

Do not use `aufs` as the storage driver for your Docker instance.

## Rationale{% #rationale %}

The `aufs` storage driver is the oldest storage driver used on Linux systems. It is based on a Linux kernel patch-set that is unlikely in future to be merged into the main OS kernel. The `aufs` driver is also known to cause some serious kernel crashes. `aufs` has only legacy support within systems using Docker. Most importantly, `aufs` is not a supported driver in many Linux distributions using latest Linux kernels.

## Audit{% #audit %}

Verify that `aufs` is not used as storage driver by running this command and ensuring `aufs` is not listed:

```
docker info --format 'Storage Driver: {{ .Driver }}'
```

## Remediation{% #remediation %}

Do not explicitly use `aufs` as storage driver. For example, do not start Docker daemon with the `--storage-driver aufs` flag.

## Impact{% #impact %}

`aufs` is the only storage driver that allows containers to share executable and shared library memory. It might be useful if you are running thousands of containers with the same program or libraries. However, you should review its use with respect to your organization's security policy.

## Default value{% #default-value %}

By default, Docker uses `devicemapper` as the storage driver on most of the platforms. The default storage driver can vary based on your OS vendor. You should use the storage driver that is recommended by your preferred vendor and which is in line with policy around the applications which are being deployed.

## References{% #references %}

1. [https://docs.docker.com/engine/userguide/storagedriver/selectadriver/#supported-backing-filesystems](https://docs.docker.com/engine/userguide/storagedriver/selectadriver/#supported-backing-filesystems)
1. [http://muehe.org/posts/switching-docker-from-aufs-to-devicemapper/](http://muehe.org/posts/switching-docker-from-aufs-to-devicemapper/)
1. [http://jpetazzo.github.io/assets/2015-03-05-deep-dive-into-docker-storage-drivers.html#1](http://jpetazzo.github.io/assets/2015-03-05-deep-dive-into-docker-storage-drivers.html#1)
1. [https://docs.docker.com/engine/userguide/storagedriver/](https://docs.docker.com/engine/userguide/storagedriver/)

## CIS controls{% #cis-controls %}

Version 6.18 Application Software Security
