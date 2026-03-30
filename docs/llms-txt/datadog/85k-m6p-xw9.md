# Source: https://docs.datadoghq.com/security/default_rules/85k-m6p-xw9.md

---
title: The /etc/sysconfig/docker file permissions should be set to 644 or stricter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The /etc/sysconfig/docker file
  permissions should be set to 644 or stricter
---

# The /etc/sysconfig/docker file permissions should be set to 644 or stricter
Classification:complianceFramework:cis-dockerControl:3.21
## Description{% #description %}

You should verify that the `/etc/sysconfig/docker` file permissions are correctly set to 644 or more restrictively.

## Rationale{% #rationale %}

The `/etc/sysconfig/docker` file contains sensitive parameters that may alter the behavior of the Docker daemon. It should therefore be writeable only by root in order to ensure that it is not modified by less privileged users.

## Audit{% #audit %}

Verify that the `/etc/sysconfig/docker` file permissions are set to `644` or more restrictive, by running:

```
stat -c %a /etc/sysconfig/docker
```

## Remediation{% #remediation %}

Run the following command: `chmod 644 /etc/sysconfig/docker`

This sets the file permissions for this file to 644.

## Impact{% #impact %}

None

## Default value{% #default-value %}

This file may not be present on the system and in this case, this recommendation is not applicable.

## References{% #references %}

1. [https://docs.docker.com/engine/admin/configuring/](https://docs.docker.com/engine/admin/configuring/)

## CIS controls{% #cis-controls %}

Version 6

14.4 Protect Information With Access Control Lists All information stored on systems shall be protected with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.

Version 7

14.6 Protect Information through Access Control Lists Protect all information stored on systems with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.
