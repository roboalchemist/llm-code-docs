# Source: https://docs.datadoghq.com/security/default_rules/def-000-re3.md

---
title: Verify that All World-Writable Directories Have Sticky Bits Set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify that All World-Writable
  Directories Have Sticky Bits Set
---

# Verify that All World-Writable Directories Have Sticky Bits Set

## Description{% #description %}

When the so-called 'sticky bit' is set on a directory, only the owner of a given file may remove that file from the directory. Without the sticky bit, any user with write access to a directory may remove any file in the directory. Setting the sticky bit prevents users from removing each other's files. In cases where there is no reason for a directory to be world-writable, a better solution is to remove that permission rather than to set the sticky bit. However, if a directory is used by a particular application, consult that application's documentation instead of blindly changing modes.

To set the sticky bit on a world-writable directory *DIR*, run the following command:

```
$ sudo chmod +t DIR

```

## Rationale{% #rationale %}

Failing to set the sticky bit on public directories allows unauthorized users to delete files in the directory structure.

The only authorized public directories are those temporary directories supplied with the system, or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system, by users for temporary file storage (such as `/tmp`), and for directories requiring global read/write access.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

df --local -P | awk '{if (NR!=1) print $6}' \
| xargs -I '$6' find '$6' -xdev -type d \
\( -perm -0002 -a ! -perm -1000 \) 2>/dev/null \
-exec chmod a+t {} +
```

## Warning{% #warning %}

This rule can take a long time to perform the check and might consume a considerable amount of resources depending on the number of directories present on the system. It is not a problem in most cases, but especially systems with a large number of directories can be affected. See `https://access.redhat.com/articles/6999111`.
