# Source: https://docs.datadoghq.com/security/default_rules/4rp-frf-dq4.md

---
title: The /etc/docker directory should be owned by root account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The /etc/docker directory should be
  owned by root account
---

# The /etc/docker directory should be owned by root account
Classification:complianceFramework:cis-dockerControl:3.5
## Description{% #description %}

You should verify that the `/etc/docker` directory ownership and group ownership is correctly set to root.

## Rationale{% #rationale %}

The `/etc/docker` directory contains certificates and keys in addition to various other sensitive files. It should therefore be individual owned and group owned by root in order to ensure that it can not be modified by less privileged users.

## Audit{% #audit %}

You should execute the command below to verify that the directory is owned and group owned by root:

```
stat -c %U:%G /etc/docker | grep -v root:root
```

This command does not return any data.

## Remediation{% #remediation %}

To resolve this issue, run the following command: `chown root:root /etc/docker`

This sets the ownership and group ownership for the directory to root.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the ownership and group ownership for this directory is correctly set to root.

## References{% #references %}

1. [https://docs.docker.com/engine/security/https/](https://docs.docker.com/engine/security/https/)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.`
