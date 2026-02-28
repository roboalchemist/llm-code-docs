# Source: https://docs.datadoghq.com/security/default_rules/def-000-dv8.md

---
title: Ensure No World-Writable Files Exist
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure No World-Writable Files Exist
---

# Ensure No World-Writable Files Exist

## Description{% #description %}

It is generally a good idea to remove global (other) write access to a file when it is discovered. However, check with documentation for specific applications before making changes. Also, monitor for recurring world-writable files, as these may be symptoms of a misconfigured application or user account. Finally, this applies to real files and not virtual files that are a part of pseudo file systems such as `sysfs` or `procfs`.

## Rationale{% #rationale %}

Data in world-writable files can be modified by any user on the system. In almost all circumstances, files can be configured using a combination of user and group permissions to support whatever legitimate access is needed without the risk caused by world-writable files.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

FILTER_NODEV=$(awk '/nodev/ { print $2 }' /proc/filesystems | paste -sd,)

# Do not consider /sysroot partition because it contains only the physical
# read-only root on bootable containers.
PARTITIONS=$(findmnt -n -l -k -it $FILTER_NODEV | awk '{ print $1 }' | grep -v "/sysroot")

for PARTITION in $PARTITIONS; do
  find "${PARTITION}" -xdev -type f -perm -002 -exec chmod o-w {} \; 2>/dev/null
done

# Ensure /tmp is also fixed when tmpfs is used.
if grep "^tmpfs /tmp" /proc/mounts; then
  find /tmp -xdev -type f -perm -002 -exec chmod o-w {} \; 2>/dev/null
fi
```

## Warning{% #warning %}

This rule can take a long time to perform the check and might consume a considerable amount of resources depending on the number of files present on the system. It is not a problem in most cases, but especially systems with a large number of files can be affected. See `https://access.redhat.com/articles/6999111`.
