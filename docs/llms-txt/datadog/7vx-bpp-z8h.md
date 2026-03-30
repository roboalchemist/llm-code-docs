# Source: https://docs.datadoghq.com/security/default_rules/7vx-bpp-z8h.md

---
title: The TLS CA certificate file should be owned by root account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The TLS CA certificate file should be
  owned by root account
---

# The TLS CA certificate file should be owned by root account
Classification:complianceFramework:cis-dockerControl:3.9
## Description{% #description %}

You should verify that the TLS CA certificate file, the file that is passed along with the `--tlscacert parameter`, is individually owned and group owned by root.

## Rationale{% #rationale %}

The TLS CA certificate file should be protected from any tampering. It is used to authenticate the Docker server based on a given CA certificate. It must be therefore be individually owned and group owned by root to ensure that it cannot be modified by less privileged users.

## Audit{% #audit %}

You should execute the command below to verify that the TLS CA certificate file is owned and group owned by root:

```
stat -c %U:%G <path to TLS CA certificate file> | grep -v root:root
```

This command does not return any data.

## Remediation{% #remediation %}

Run the following command: `chown root:root <path to TLS CA certificate file>`

This sets the individual ownership and group ownership for the TLS CA certificate file to root.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the ownership and group-ownership for TLS CA certificate file is correctly set to root.

## References{% #references %}

1. [https://docs.docker.com/registry/insecure/](https://docs.docker.com/registry/insecure/)
1. [https://docs.docker.com/engine/security/https/](https://docs.docker.com/engine/security/https/)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.
