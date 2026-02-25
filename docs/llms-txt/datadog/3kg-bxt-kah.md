# Source: https://docs.datadoghq.com/security/default_rules/3kg-bxt-kah.md

---
title: The registry certificate files should be individually and group owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The registry certificate files should
  be individually and group owned by root
---

# The registry certificate files should be individually and group owned by root
Classification:complianceFramework:cis-dockerControl:3.7
## Description{% #description %}

You should verify that all the registry certificate files, usually found under the `/etc/docker/certs.d/<registry-name>` directory, are individually owned and group owned by root.

## Rationale{% #rationale %}

The `/etc/docker/certs.d/<registry-name>` directory contains Docker registry certificates. These certificate files must be individually owned and group owned by root to ensure that less privileged users are unable to modify the contents of the directory.

## Audit{% #audit %}

You should execute the command below to verify that the registry certificate files are individually owned and group owned by root:

```
stat -c %U:%G /etc/docker/certs.d/* | grep -v root:root
```

This command does not return any data.

## Remediation{% #remediation %}

Execute the following command: `chown root:root /etc/docker/certs.d/<registry-name>/*`

This sets the individual ownership and group ownership for the registry certificate files to root.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the individual ownership and group ownership for registry certificate files is correctly set to root.

## References{% #references %}

1. [https://docs.docker.com/registry/insecure/](https://docs.docker.com/registry/insecure/)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.
