# Source: https://docs.datadoghq.com/security/default_rules/89n-csr-u3u.md

---
title: The /etc/default/docker file ownership should be set to root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The /etc/default/docker file ownership
  should be set to root
---

# The /etc/default/docker file ownership should be set to root
Classification:complianceFramework:cis-dockerControl:3.19
## Description{% #description %}

You should verify that the `/etc/default/docker` file ownership and group-ownership is correctly set to root.

## Rationale{% #rationale %}

The `/etc/default/docker` file contains sensitive parameters that may alter the behavior of the Docker daemon. It should therefore be individually owned and group owned by root to ensure that it cannot be modified by less privileged users.

## Audit{% #audit %}

Verify that the `/etc/default/docker` file is individually owned and group-owned by root by running:

```
stat -c %U:%G /etc/default/docker | grep -v root:root
```

The command should return no results.

## Remediation{% #remediation %}

Execute the following command: `chown root:root /etc/default/docker`

This sets the ownership and group ownership of the file to root.

## Impact{% #impact %}

None

## Default value{% #default-value %}

This file may not be present on the system, and in this case, this recommendation is not applicable.

## References{% #references %}

1. [https://docs.docker.com/engine/admin/configuring/](https://docs.docker.com/engine/admin/configuring/)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.
