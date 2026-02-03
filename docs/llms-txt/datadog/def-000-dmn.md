# Source: https://docs.datadoghq.com/security/default_rules/def-000-dmn.md

---
title: EFS access points should enforce a user identity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EFS access points should enforce a user
  identity
---

# EFS access points should enforce a user identity
 
## Description{% #description %}

This control verifies whether Amazon EFS access points are configured to enforce a specific user identity. The control is marked as non-compliant if a POSIX user identity is not defined during the creation of the EFS access point.

Amazon EFS access points are designed as application-specific entry points into an EFS file system, simplifying the management of application access to shared data. Access points can enforce a user identity, including the associated POSIX group memberships, for all file system requests made through them.

## Remediation{% #remediation %}

For details on configuring a user identity for an Amazon EFS access point, refer to the [Enforcing a user identity using an access point](https://docs.aws.amazon.com/efs/latest/ug/enforce-identity-access-points.html) section in the Amazon Elastic File System User Guide.
