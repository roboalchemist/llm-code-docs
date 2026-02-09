# Source: https://docs.datadoghq.com/security/default_rules/bap-wei-4kf.md

---
title: The Docker server certificate file should be owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Docker server certificate file
  should be owned by root
---

# The Docker server certificate file should be owned by root
Classification:complianceFramework:cis-dockerControl:3.11 
## Description{% #description %}

You should verify that the Docker server certificate file, the file that is passed along with the `--tlscert` parameter, is individual owned and group owned by root.

## Rationale{% #rationale %}

The Docker server certificate file should be protected from any tampering. It is used to authenticate the Docker server based on the given server certificate. It must therefore be individually owned and group owned by root to prevent modification by less privileged users.

## Audit{% #audit %}

Verify that the Docker server certificate file is individually owned and group-owned by root, by running:

```
stat -c %U:%G <path to Docker server certificate file> | grep -v root:root
```

The command should return no results.

## Remediation{% #remediation %}

Run the following command: `chown root:root <path to Docker server certificate file>`

This sets the individual ownership and the group ownership for the Docker server certificate file to root.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the ownership and group-ownership for Docker server certificate file is correctly set to root.

## References{% #references %}

1. [https://docs.docker.com/registry/insecure/](https://docs.docker.com/registry/insecure/)
1. [https://docs.docker.com/engine/security/https/](https://docs.docker.com/engine/security/https/)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.
