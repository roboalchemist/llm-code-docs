# Source: https://docs.datadoghq.com/security/default_rules/pv5-2tt-sp9.md

---
title: The /etc/sysconfig/docker file should be owned by the root account and group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The /etc/sysconfig/docker file should
  be owned by the root account and group
---

# The /etc/sysconfig/docker file should be owned by the root account and group
Classification:complianceFramework:cis-dockerControl:3.20
## Description{% #description %}

You should verify that the `/etc/sysconfig/docker` file individual ownership and group ownership is correctly set to root.

## Rationale{% #rationale %}

The `/etc/sysconfig/docker` file contains sensitive parameters that may alter the behavior of the Docker daemon. It should therefore be individually owned and group owned by root to ensure that it is not modified by less privileged users.

## Audit{% #audit %}

Verify that the `/etc/sysconfig/docker` file is individually owned and group-owned by root by running:

```
stat -c %U:%G /etc/sysconfig/docker | grep -v root:root
```

The command should return no results.

## Remediation{% #remediation %}

Run the following command: `chown root:root /etc/sysconfig/docker`

This sets the ownership and group ownership for the file to root.

## Impact{% #impact %}

None

## Default value{% #default-value %}

This file may not be present on the system, and in this case, this recommendation is not applicable.

## References{% #references %}

1. [https://docs.docker.com/engine/admin/configuring/](https://docs.docker.com/engine/admin/configuring/)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.
