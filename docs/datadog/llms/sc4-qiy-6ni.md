# Source: https://docs.datadoghq.com/security/default_rules/sc4-qiy-6ni.md

---
title: The daemon.json file should have user and group ownership set to root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The daemon.json file should have user
  and group ownership set to root
---

# The daemon.json file should have user and group ownership set to root
Classification:complianceFramework:cis-dockerControl:3.17
## Description{% #description %}

You should verify that the daemon.json file individual ownership and group ownership is correctly set to root.

## Rationale{% #rationale %}

The daemon.json file contains sensitive parameters that could alter the behavior of the docker daemon. It should therefore be owned and group owned by root to ensure it can not be modified by less privileged users.

## Audit{% #audit %}

Verify that the `daemon.json` file is owned and group-owned by root by running:

```
stat -c %U:%G /etc/docker/daemon.json | grep -v root:root
```

The command should return no results.

## Remediation{% #remediation %}

Run `chown root:root /etc/docker/daemon.json`

This sets the ownership and group ownership for the file to root.

## Impact{% #impact %}

None

## Default value{% #default-value %}

This file may not be present on the system, and in that case, this recommendation is not applicable.

## References{% #references %}

1. [https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.
