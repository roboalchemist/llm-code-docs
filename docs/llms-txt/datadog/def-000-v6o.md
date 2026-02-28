# Source: https://docs.datadoghq.com/security/default_rules/def-000-v6o.md

---
title: EFS access points should enforce a root directory
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EFS access points should enforce a root
  directory
---

# EFS access points should enforce a root directory

## Description{% #description %}

This control verifies whether Amazon EFS access points are set up to enforce a specific root directory. The control fails if the `Path` value is `/`, which represents the default root directory of the file system.

By enforcing a root directory, NFS clients connecting through the access point are directed to the designated root directory specified on the access point, rather than the default file system root. This ensures data access is restricted, allowing users of the access point to access only the files located within the defined subdirectory.

## Remediation{% #remediation %}

To learn how to configure a root directory for an Amazon EFS access point, refer to the [Enforcing a root directory with an access point](https://docs.aws.amazon.com/efs/latest/ug/enforce-root-directory-access-point.html) section in the Amazon Elastic File System User Guide.
